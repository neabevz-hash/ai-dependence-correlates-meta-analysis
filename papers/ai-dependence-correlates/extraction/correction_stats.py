"""Share of AI-drafted values R1 corrected (protocol §11c), overall, for the key items and by field.

Compares the stored drafts with R1's corrections (extraction/decisions/corrections_R1.csv, from verify_md.py parse).
Denominator: every drafted value of the verified samples - the sample fields, the six risk-of-bias ratings and the
effect fields. Key items: n_analysed, population, sampling, ai_system (samples) and exposure family and part,
correlate construct and instrument, direction of scoring, statistic type, value and n (effects).
A deleted effect counts as one corrected key value; an added effect as one missed key value.
Writes extraction/decisions/correction_stats.json.
Template: papers/misophonia-prevalence/extraction/correction_stats.py.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/correction_stats.py
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_md import EFF_FIELDS, KEY_EFF, KEY_SAMPLE, SAMPLE_FIELDS  # noqa: E402

EVIDENCE = ("location", "quote", "note")   # evidence for a value, not data
EFF_DATA = [f for f in EFF_FIELDS if f not in EVIDENCE]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dec", help="folder of the parsed decisions (default extraction/decisions)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    dec = Path(a.dec) if a.dec else HERE / "decisions"
    samples = list(csv.DictReader((dec / "samples_R1.csv").open(encoding="utf-8")))
    effs = list(csv.DictReader((dec / "effects_R1.csv").open(encoding="utf-8")))
    corr = list(csv.DictReader((dec / "corrections_R1.csv").open(encoding="utf-8"))) if (dec / "corrections_R1.csv").exists() else []
    verified = {s["sample_key"] for s in samples if s["verified"] == "yes" and not s["dropped"]}
    n_eff_drafted = sum(1 for e in effs if e["sample_key"] in verified and e["eff"].startswith("E")) + \
        sum(1 for c in corr if c["sample_key"] in verified and c["r1_value"] == "deleted")
    total = len(verified) * (len(SAMPLE_FIELDS) + 6) + n_eff_drafted * len(EFF_DATA)
    key_total = len(verified) * len(KEY_SAMPLE) + n_eff_drafted * len(KEY_EFF)
    c_ver = [c for c in corr if c["sample_key"] in verified and c["field"] not in EVIDENCE]
    changed = [c for c in c_ver if c["target"] != "new"]
    key_changed = [c for c in changed if c["key_field"] == "yes"]
    added = [c for c in c_ver if c["target"] == "new"]
    by_field = Counter((c["target"] if c["target"] == "sample" or c["target"].startswith("rob") else "effect", c["field"])
                       for c in changed)
    out = {
        "verified_samples": len(verified), "drafted_effects": n_eff_drafted,
        "drafted_values": total, "values_corrected": len(changed),
        "share_corrected": round(len(changed) / total, 4) if total else None,
        "key_values": key_total, "key_values_corrected": len(key_changed),
        "share_key_corrected": round(len(key_changed) / key_total, 4) if key_total else None,
        "effects_added_by_R1": len(added),
        "by_field": {f"{t}.{f}": n for (t, f), n in by_field.most_common()},
    }
    (dec / "correction_stats.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
                                               newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
