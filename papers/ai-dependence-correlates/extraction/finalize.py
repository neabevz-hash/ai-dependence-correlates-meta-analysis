"""Verified extraction -> the analysis tables of the protocol (forms/samples.csv, forms/effects.csv).

Reads R1's verified values (extraction/decisions/samples_R1.csv and effects_R1.csv, written by verify_md.py parse),
the drafts (for the risk-of-bias reasons), the record metadata, instruments.csv (R1's types) and the construct
dictionary, and writes the tables in the codebook's format: sample_id S###, study_id ST###, report_ids (main report
first), first author, year and DOI of the main report, region from the country (codebook), effect_id E####, the
canonical subscale name with its type, the role of the correlate (primary or secondary) and the pilot flags of
deviations.md D4 (lagged, observed_pair_exists). Dropped samples and deleted effects are left out. By default only
samples R1 marked verified are written.
Template: papers/misophonia-prevalence/extraction/finalize.py.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/finalize.py --run 2026-10-16 --draft extract_<date>
     (--in DIR / --out DIR / --allow-unverified for code tests on unverified drafts)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402
import verify_md  # noqa: E402

SAMPLE_COLS = ["sample_id", "study_id", "report_ids", "first_author", "year", "doi", "pub_status", "language", "country",
               "region", "data_years", "design", "sampling", "population", "clinical_group", "n_analysed", "age_mean",
               "age_sd", "age_min", "age_max", "pct_female", "ai_system", "mode", "attention_checks", "funding_coi",
               "rob_1", "rob_2", "rob_3", "rob_4", "rob_5", "rob_6", "rob_notes", "notes", "sample_key", "label"]
EFF_COLS = ["effect_id", "sample_id", "wave", "lagged", "exposure_family", "exposure_part", "exposure_type",
            "exposure_alpha", "correlate_construct", "correlate_role", "correlate_instrument", "correlate_alpha",
            "direction_note", "reversed", "stat_type", "observed_pair_exists", "value", "ci_or_se", "n", "location",
            "notes"]
REC = re.compile(r"R\d{4}")
# First authors the source metadata gives wrongly (checked against the PDF title page, 2026-10-18): names as printed.
AUTHOR_FIX = {"R0027": "Silla Jacob",          # Zenodo creators parsed as "SILLA JACOB 1 ... 3" -> "3"
              "R3037": "Jeyakumar Jenifer"}    # Crossref: given "Jeyakumar Jenifer", family "-"

# Codebook (samples.csv, region): filled from the country.
REGION = {
    "mainland_China": ["CHN"],
    "other_East_Asia": ["HKG", "MAC", "TWN", "JPN", "KOR", "PRK", "MNG"],
    "South_Southeast_Asia": ["IND", "PAK", "BGD", "LKA", "NPL", "BTN", "MDV", "AFG", "IDN", "MYS", "PHL", "THA", "VNM",
                             "SGP", "KHM", "LAO", "MMR", "BRN", "TLS"],
    "MENA_Turkiye": ["TUR", "SAU", "ARE", "EGY", "JOR", "IRN", "IRQ", "LBN", "QAT", "KWT", "OMN", "BHR", "MAR", "DZA",
                     "TUN", "LBY", "PSE", "ISR", "YEM", "SYR", "SDN"],
    "Europe": ["GBR", "IRL", "FRA", "DEU", "ESP", "PRT", "ITA", "NLD", "BEL", "LUX", "CHE", "AUT", "DNK", "NOR", "SWE",
               "FIN", "ISL", "POL", "CZE", "SVK", "HUN", "ROU", "BGR", "GRC", "CYP", "MLT", "SVN", "HRV", "SRB", "BIH",
               "MNE", "MKD", "ALB", "XKX", "EST", "LVA", "LTU", "UKR", "BLR", "MDA", "RUS"],
    "Americas": ["USA", "CAN", "MEX", "BRA", "ARG", "CHL", "COL", "PER", "ECU", "BOL", "VEN", "URY", "PRY", "GTM", "HND",
                 "SLV", "NIC", "CRI", "PAN", "CUB", "DOM", "PRI", "JAM", "TTO", "HTI"],
}
REGION_OF = {c: r for r, cs in REGION.items() for c in cs}


def region(country: str) -> str:
    c = (country or "").strip().upper()
    if c.startswith("MULTI"):
        return "multi"
    m = re.match(r"([A-Z]{3})\b", c)
    return REGION_OF.get(m.group(1), "other") if m and m.group(1) not in ("NR", "NA") else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--draft", required=True)
    ap.add_argument("--in", dest="inp", default=str(HERE / "decisions"))
    ap.add_argument("--out", default=str(PAPER / "forms"))
    ap.add_argument("--allow-unverified", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    recs = load_records(a.run)
    verify_md.load_reference()
    drafts = {}
    for line in (HERE / "draft" / f"{a.draft}.jsonl").open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            drafts[d["conv_id"]] = d
    roles = {r["construct"]: r["role"] for r in csv.DictReader((PAPER / "forms" / "construct_dictionary.csv").open(encoding="utf-8"))}
    inp = Path(a.inp)
    samples = list(csv.DictReader((inp / "samples_R1.csv").open(encoding="utf-8")))
    effs = list(csv.DictReader((inp / "effects_R1.csv").open(encoding="utf-8")))
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    reasons, notes_ai = {}, {}
    for key, j, i, s in verify_md.sample_keys(jobs, drafts):
        reasons[key] = {k: s["rob"][f"rob_{k}"] for k in range(1, 7)}
        notes_ai[key] = s.get("notes", "")

    out_s, out_e, skipped, unknown = [], [], [], []
    sid = {}
    for s in samples:
        if s["dropped"]:
            skipped.append(f"{s['sample_key']} dropped by R1: {s['dropped']}")
            continue
        if s["verified"] != "yes" and not a.allow_unverified:
            skipped.append(f"{s['sample_key']} not verified")
            continue
        sid[s["sample_key"]] = f"S{len(sid) + 1:03d}"
        reps = list(dict.fromkeys(REC.findall(s["reports"]))) or [s["job_id"]]
        if s["job_id"] in reps:
            reps.remove(s["job_id"])
        reps = [s["job_id"], *reps]
        main = recs[s["job_id"]]
        notes_rob = []
        for k in range(1, 7):
            r = s[f"rob_{k}"]
            if r in ("no", "unclear"):
                ai = reasons.get(s["sample_key"], {}).get(k, {})
                why = ai.get("reason", "") if ai.get("rating") == r else "rating set by R1"
                notes_rob.append(f"{k}: {r} - {why}")
        out_s.append({
            **{k: s.get(k, "") for k in SAMPLE_COLS if k in s},
            "sample_id": sid[s["sample_key"]], "study_id": s["study_id"], "report_ids": ";".join(reps),
            "first_author": AUTHOR_FIX.get(s["job_id"], main.get("first_author") or ""), "year": main.get("year") or "",
            "doi": main.get("doi") or "",
            "region": region(s.get("country", "")),
            "rob_notes": " | ".join(notes_rob),
            "notes": " | ".join(x for x in (notes_ai.get(s["sample_key"], ""), s.get("r1_comments", "")) if x),
            "sample_key": s["sample_key"], "label": s["label"],
        })
    kept = [e for e in effs if e["sample_key"] in sid]
    observed = {(e["sample_key"], e["exposure_family"], verify_md.canon_part(e["exposure_family"], e["exposure_part"]) or e["exposure_part"],
                 e["correlate_construct"], e["correlate_instrument"].strip().lower())
                for e in kept if e["stat_type"] in ("pearson", "spearman")}
    for e in kept:
        part = verify_md.canon_part(e["exposure_family"], e["exposure_part"])
        if part is None:
            unknown.append(f"{e['sample_key']} {e['eff']}: {e['exposure_family']} / {e['exposure_part']}")
        part = part or e["exposure_part"]
        pair = (e["sample_key"], e["exposure_family"], part, e["correlate_construct"], e["correlate_instrument"].strip().lower())
        out_e.append({
            "effect_id": f"E{len(out_e) + 1:04d}", "sample_id": sid[e["sample_key"]], "wave": e["wave"],
            "lagged": "yes" if e["wave"].strip().lower().startswith("lagged") else "no",
            "exposure_family": e["exposure_family"], "exposure_part": part,
            "exposure_type": verify_md.TYPES.get((e["exposure_family"], part), ""),
            "exposure_alpha": e["exposure_alpha"], "correlate_construct": e["correlate_construct"],
            "correlate_role": roles.get(e["correlate_construct"], ""), "correlate_instrument": e["correlate_instrument"],
            "correlate_alpha": e["correlate_alpha"], "direction_note": e["direction_note"],
            "reversed": "yes" if "revers" in (e["direction_note"] or "").lower() else "no",
            "stat_type": e["stat_type"],
            "observed_pair_exists": "yes" if e["stat_type"] == "latent" and pair in observed else "no",
            "value": e["value"], "ci_or_se": e["ci_or_se"], "n": e["n"], "location": e["location"],
            "notes": e.get("note", ""),
        })
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    for name, cols, rows in (("samples.csv", SAMPLE_COLS, out_s), ("effects.csv", EFF_COLS, out_e)):
        with (out / name).open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    print(f"samples {len(out_s)}, effects {len(out_e)} -> {out}; skipped {len(skipped)}")
    other = sorted({r["country"] for r in out_s if r["region"] == "other"})
    if other:
        print("countries coded region 'other':", ", ".join(other))
    for u in unknown:
        print("exposure part not in instruments.csv:", u)


if __name__ == "__main__":
    main()
