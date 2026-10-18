"""Full-text stage summary and PRISMA 2020 counts (protocol, section 11b).

Inputs: screening/decisions/tiab_summary.json, fulltext/retrieval_log.csv, fulltext/decisions/ft_R1.csv (from
ft_md.py parse), fulltext/llm/<name>.jsonl (AI proposals) and fulltext/incomplete_texts.csv: retrieved files that turned
out not to contain the report (references only, a repository guide, front matter only). Those count as "reports not
retrieved", not as R1 decisions.

Writes fulltext/prisma_counts.json and prints it.
Run: .venv/Scripts/python.exe papers/ai-dependence-correlates/fulltext/ft_summary.py --name ft_2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    tiab = json.loads((PAPER / "screening" / "decisions" / "tiab_summary.json").read_text(encoding="utf-8"))
    dedup = json.loads((PAPER / "search" / "runs" / tiab["run"] / "dedup_report.json").read_text(encoding="utf-8"))
    log = list(csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")))
    incomplete = {r["rec_id"]: r for r in csv.DictReader((HERE / "incomplete_texts.csv").open(encoding="utf-8-sig"))}
    r1 = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))}
    ai = {}
    for path in [HERE / "llm" / f"{a.name}.jsonl", *sorted((HERE / "llm").glob("ft_late_*.jsonl")),
                 *sorted((HERE / "llm").glob("ft_osf_*.jsonl"))]:   # D3, D9: texts retrieved late
        ai.update({json.loads(l)["conv_id"]: json.loads(l)["codes"] for l in path.open(encoding="utf-8") if l.strip()})
    retrieved = [r["rec_id"] for r in log if r["status"] == "retrieved" and r["rec_id"] not in incomplete]
    assessed = {rid: r1[rid] for rid in retrieved if rid in r1}
    undecided = [rid for rid, r in assessed.items() if r["decision"] not in ("eligible", "not_eligible")]
    ai_map = {"eligible": "eligible", "not_eligible": "not_eligible", "unclear": "unclear"}
    agree = sum(1 for rid, r in assessed.items() if ai_map[ai[rid]["decision"]] == r["decision"])
    same_reason = sum(1 for rid, r in assessed.items() if r["decision"] == "not_eligible" == ai[rid]["decision"]
                      and r["reason"] == ai[rid]["reason"])
    out = {
        "records_identified": dedup["records_total"],
        "records_per_source": dedup["records_per_source"],
        "duplicates_removed": dedup["duplicates_removed"],   # pointer and component records attached are included
        "removed_by_automation": dedup["auto_removed_non_study_records"],
        "records_screened_title_abstract": tiab["records_screened"],
        "records_excluded_title_abstract": tiab["excluded_title_abstract"],
        "reports_sought_for_retrieval": len(log),
        "reports_not_retrieved": len(log) - len(retrieved),
        "reports_not_retrieved_detail": {
            "no_open_access_copy_or_blocked": sum(1 for r in log if r["status"] != "retrieved"),
            "retrieved_file_did_not_contain_the_report": len(incomplete),
        },
        "reports_assessed_for_eligibility": len(assessed),
        "reports_excluded_full_text": dict(Counter(r["reason"] for r in assessed.values() if r["decision"] == "not_eligible")),
        "reports_included": sum(1 for r in assessed.values() if r["decision"] == "eligible"),
        "undecided": undecided,
        "ai_proposals": {
            "agreement_eligible_vs_not": agree, "of": len(assessed),
            "ai_unclear": sum(1 for rid in assessed if ai[rid]["decision"] == "unclear"),
            "same_exclusion_reason": same_reason,
            "r1_accepted_with_equals": sum(1 for r in assessed.values() if r["code"].startswith("=")),
            "r1_eligible_ai_not": sum(1 for rid, r in assessed.items() if r["decision"] == "eligible" and ai[rid]["decision"] == "not_eligible"),
            "r1_not_ai_eligible": sum(1 for rid, r in assessed.items() if r["decision"] == "not_eligible" and ai[rid]["decision"] == "eligible"),
        },
    }
    # identification via other methods (PRISMA 2020): citation searching (deviations.md, D2)
    chase_log = sorted((PAPER / "search" / "runs").glob("*-citations/chase_log.json"))
    if chase_log:
        cl = json.loads(chase_log[-1].read_text(encoding="utf-8"))
        chase_ids = {json.loads(l)["rec_id"] for l in (chase_log[-1].parent / "records_unique.jsonl").open(encoding="utf-8")}
        chase_dec = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / "ft_R1_chase.csv").open(encoding="utf-8-sig"))}
        ret_chase = [r for r in log if r["rec_id"] in chase_ids and r["status"] == "retrieved"]
        out["other_methods_citation_searching"] = {
            "new_works_not_in_main_set": cl["new_unique_records"],
            "without_exposure_concept_in_title_abstract": cl["new_unique_records"] - len(chase_ids),
            "reports_sought": len(chase_ids), "reports_not_retrieved": len(chase_ids) - len(ret_chase),
            "reports_assessed": len(ret_chase),
            "reports_excluded": dict(Counter(chase_dec[r["rec_id"]]["reason"] for r in ret_chase if chase_dec[r["rec_id"]]["decision"] == "not_eligible")),
            "reports_included": sum(1 for r in ret_chase if chase_dec[r["rec_id"]]["decision"] == "eligible"),
        }
        log_main = [r for r in log if r["rec_id"] not in chase_ids]
        out["reports_sought_for_retrieval"] = len(log_main)
        retrieved_main = [r for r in retrieved if r not in chase_ids]
        out["reports_not_retrieved"] = len(log_main) - len(retrieved_main)
        out["reports_not_retrieved_detail"]["no_open_access_copy_or_blocked"] = sum(1 for r in log_main if r["status"] != "retrieved")
    (HERE / "prisma_counts.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
