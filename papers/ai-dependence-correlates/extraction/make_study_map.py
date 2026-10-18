"""Link the eligible reports into studies and extraction jobs (protocol §11b "Linking reports", E6).

Reports are linked when they describe the same sample: preprint versions and the article, a thesis and its article, a
scale-development paper and a substantive paper on the same participants. The links below were set from the AI full-text
proposals (field possible_duplicate) and checked against the reported N, setting, dates and sample composition.
A study is a connected group of linked reports. Each sample is extracted once (E6); the other reports of the sample are
attached to the job while the input stays within MAX_CHARS. Template: papers/misophonia-prevalence/extraction/make_study_map.py.

Pairs that only might overlap (same group or university, no evidence of shared participants) stay separate and are listed
in POSSIBLE, so R1 sees them in the verification file.

Writes extraction/study_map.csv (one row per report) and extraction/jobs.json (one job per main report).
Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/extraction/make_study_map.py --run 2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))
from common import eligible_reports, load_records  # noqa: E402
MAX_CHARS = 400_000

# main report -> (additional reports of the same samples, reason). Every report of a group is listed once.
GROUPS = [
    ("R0691", ["R0690"], "Two Research Square versions of one preprint (King Abdulaziz University, N = 521, 15-item AI-Dependency "
     "Scale); the version of record is BMC Psychology 10.1186/s40359-026-05496-0"),
    ("R4677", ["R3792"], "Companion-chatbot users (N = 404, CloudResearch Connect, adapted GPIUS2): arXiv 2410.21596 v3 (R4677, "
     "with the appendix correlation matrix) and the journal version R3792"),
    ("R4336", ["R2687"], "AIDep-22 development (Wu et al.): R4336 Sample 2 (N = 400, 64.8% female, age 18-24, M = 21.17, one "
     "university in Southwest China) matches the sample of R2687 (N = 400, 259 female, M = 21.17, Southwest China) in every "
     "reported characteristic"),
]

# Samples to extract from a main report when it is not simply "every eligible sample in this report".
SAMPLES = {
    "R4336": "Two independent samples: Sample 1 (EFA, N = 400) and Sample 2 (CFA and criterion validity, N = 400). Sample 2 is "
             "also the sample of the attached report R2687: take the correlations of both reports for Sample 2, each "
             "correlation once; if the same pair appears in both with different values, keep R4336's value and describe the "
             "difference in consistency_notes.",
    "R0691": "One sample. Take the values from the main report; where R0690 differs, note it in consistency_notes.",
    "R4677": "One sample. Take the correlation matrix of the appendix; where R3792 differs, note it in consistency_notes.",
}

# Facts the extractor cannot see in the text.
JOB_NOTES: dict[str, str] = {}

# Possible overlaps kept as separate studies (no evidence of shared participants); shown to R1.
POSSIBLE = [
    (["R2703", "R4336"], "Both Chinese undergraduates at one normal or comprehensive university in Southwest China with the AIDep-22; "
     "R2703 has N = 417 (70.3% female, M = 21.21), R4336 Sample 1 has N = 400 (70.2% female)"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    recs = load_records(a.run)
    eligible = set(eligible_reports())

    # union-find over all reports named together in GROUPS
    parent = {k: k for k in eligible}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for main_rec, extra, _ in GROUPS:
        for k in [main_rec, *extra]:
            if k not in eligible:
                raise SystemExit(f"{k} is not an eligible report")
        for k in extra:
            parent[find(k)] = find(main_rec)
    mains = {m for m, _, _ in GROUPS}
    linked = {k for m, extra, _ in GROUPS for k in [m, *extra]}
    singles = sorted(eligible - linked)
    comps: dict[str, list[str]] = {}
    for k in sorted(eligible):
        comps.setdefault(find(k), []).append(k)
    # study order: by the smallest main report id of the group (singletons are their own main)
    def first_main(members):
        return min(k for k in members if k in mains or k in singles)
    order = sorted(comps.values(), key=first_main)
    study_of = {}
    for i, members in enumerate(order, 1):
        for k in members:
            study_of[k] = f"ST{i:03d}"

    possible_of: dict[str, list[str]] = {}
    for members, why in POSSIBLE:
        for k in members:
            others = ", ".join(f"{m} ({study_of[m]})" for m in members if m != k)
            possible_of.setdefault(k, []).append(f"possible overlap with {others}: {why}")

    def chars(k):
        raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
        return len(raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw)

    jobs, rows = [], []
    group_of = {m: (extra, why) for m, extra, why in GROUPS}
    for k in [*sorted(mains), *singles]:
        extra, why = group_of.get(k, ([], ""))
        budget = MAX_CHARS - chars(k)
        attached, listed = [], []
        for e in extra:
            if chars(e) <= budget:
                attached.append(e)
                budget -= chars(e)
            else:
                listed.append(e)
        jobs.append({"job_id": k, "study_id": study_of[k], "main": k, "attached": attached, "listed_only": listed,
                     "link_reason": why, "samples": SAMPLES.get(k, "Extract every eligible sample in the main report."),
                     "job_notes": JOB_NOTES.get(k, ""),
                     "possible_overlap": possible_of.get(k, [])})
    roles = {}
    for j in jobs:
        roles.setdefault(j["main"], []).append(f"main of job {j['job_id']}")
        for e in j["attached"] + j["listed_only"]:
            roles.setdefault(e, []).append(f"additional in job {j['job_id']}")
    for k in sorted(eligible, key=lambda x: (study_of[x], x)):
        u = recs[k]
        rows.append({"study_id": study_of[k], "rec_id": k, "role": "; ".join(roles.get(k, [])),
                     "first_author": u.get("first_author") or "", "year": u.get("year") or "",
                     "doi": u.get("doi") or "", "title": u.get("title") or "",
                     "link_reason": next((why for m, extra, why in GROUPS if k == m or k in extra), ""),
                     "possible_overlap": " | ".join(possible_of.get(k, []))})
    with (HERE / "study_map.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (HERE / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    n_studies = len(order)
    print(f"{len(eligible)} reports -> {n_studies} studies, {len(jobs)} extraction jobs "
          f"({sum(1 for j in jobs if j['attached'])} with attached reports, "
          f"{sum(1 for j in jobs if j['listed_only'])} with reports listed only)")


if __name__ == "__main__":
    main()
