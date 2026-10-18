"""Final title/abstract decisions (protocol, section 11b). Template: papers/misophonia-prevalence/screening/tiab_final.py.

Every record gets R1's decision from one of three places:
  calibration   R1's blind label when it agrees with the AI rule (full text unless both passes exclude);
                otherwise R1's decision in the verification files (blind label and both AI labels shown);
  re-screening  R1's blind label for double AI exclusions outside the calibration sample (safeguard triggered);
  verification  R1's decision with both AI labels shown, for records outside the sample that at least one pass kept.
Records R1 finally labels include or unsure go to full-text screening.

Writes screening/decisions/tiab_final.csv and tiab_summary.json (numbers for PRISMA and the Methods).
Run: .venv/Scripts/python.exe papers/ai-dependence-correlates/screening/tiab_final.py --run 2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEC = HERE / "decisions"
PASSES = ("opus", "sonnet")


def read(path: Path) -> dict[str, dict]:
    return {r["rec_id"]: r for r in csv.DictReader(path.open(encoding="utf-8-sig"))}


def full(d: str) -> bool:
    return d in ("include", "unsure")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = a.run
    screening = list(csv.DictReader((HERE.parent / "search" / "runs" / run / "screening.csv").open(encoding="utf-8-sig")))
    ai: dict[str, dict] = {}
    for p in PASSES:
        for line in (HERE / "llm" / f"{run}_{p}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                ai.setdefault(d["conv_id"], {})[p] = d["codes"]
    sample = set(json.loads((HERE / "calibration" / run / "sample_meta.json").read_text(encoding="utf-8"))["rec_ids_in_display_order"])
    cal, res, ver = read(DEC / "calibration_R1.csv"), read(DEC / "rescreen_R1.csv"), read(DEC / "verify_R1.csv")

    rows, problems = [], []
    for s in screening:
        rid = s["rec_id"]
        both_exclude = all(ai[rid][p]["decision"] == "exclude" for p in PASSES)
        rule = "exclude" if both_exclude else "full_text"
        if rid in sample:
            blind = cal[rid]["decision"]
            if full(blind) == (rule == "full_text"):
                final, where = blind, "calibration (agreed with AI rule)"
            elif rid in ver:
                final, where = ver[rid]["decision"], "calibration (resolved, labels shown)"
            else:
                final, where = "", "MISSING"
        elif rid in res:
            final, where = res[rid]["decision"], "re-screening (blind)"
        elif rid in ver:
            final, where = ver[rid]["decision"], "verification (AI labels shown)"
        else:
            final, where = "", "MISSING"
        if not final:
            problems.append(rid)
        rows.append({"rec_id": rid, "final_decision": final, "full_text": full(final), "decided_in": where,
                     "ai_rule": rule, "opus": ai[rid]["opus"]["decision"], "sonnet": ai[rid]["sonnet"]["decision"],
                     "opus_reason": ai[rid]["opus"]["reason"], "sonnet_reason": ai[rid]["sonnet"]["reason"],
                     "r1_blind": cal.get(rid, res.get(rid, {})).get("decision", ""),
                     "verify_code": ver.get(rid, {}).get("code", ""), "title": s["title"]})
    with (DEC / "tiab_final.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    v_out = [r for r in rows if r["decided_in"].startswith("verification")]
    agree_passes = [r for r in v_out if r["opus"] == r["sonnet"]]
    cal_res = [r for r in rows if r["decided_in"].startswith("calibration (resolved")]
    resc = [r for r in rows if r["decided_in"].startswith("re-screening")]
    summary = {
        "run": run, "records_screened": len(rows), "missing_decisions": problems,
        "to_full_text": sum(r["full_text"] for r in rows),
        "excluded_title_abstract": sum(1 for r in rows if r["final_decision"] == "exclude"),
        "final_labels": dict(Counter(r["final_decision"] for r in rows)),
        "by_stage": {k: dict(Counter(r["final_decision"] for r in rows if r["decided_in"] == k))
                     for k in sorted({r["decided_in"] for r in rows})},
        "verification": {
            "records": len(v_out),
            "passes_agree": len(agree_passes),
            "accepted_ai_label_with_equals": sum(1 for r in v_out if r["verify_code"].startswith("=")),
            "r1_excluded_although_a_pass_kept": sum(1 for r in v_out if r["final_decision"] == "exclude"),
            "r1_excluded_although_both_kept": sum(1 for r in v_out if r["final_decision"] == "exclude"
                                                 and full(r["opus"]) and full(r["sonnet"])),
            "final_by_pass_pattern": {
                "both_kept": dict(Counter(r["final_decision"] for r in v_out if full(r["opus"]) and full(r["sonnet"]))),
                "one_kept": dict(Counter(r["final_decision"] for r in v_out if full(r["opus"]) != full(r["sonnet"]))),
            },
        },
        "calibration_resolutions": {
            "records": len(cal_res),
            "final_equals_r1_blind": sum(1 for r in cal_res if r["final_decision"] == r["r1_blind"]),
            "full_text_after_resolution": sum(r["full_text"] for r in cal_res),
        },
        "safeguard": {"re_screened": len(resc), "moved_to_full_text": sum(r["full_text"] for r in resc),
                      "moved_include": sum(1 for r in resc if r["final_decision"] == "include"),
                      "moved_unsure": sum(1 for r in resc if r["final_decision"] == "unsure")},
    }
    (DEC / "tiab_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
