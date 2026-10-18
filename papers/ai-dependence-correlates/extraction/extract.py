"""AI extraction and risk-of-bias drafts (protocol §11c, §14): Claude Opus 5.5 fills the extraction form for every job.

Reads the fixed prompt from extract_prompt.md, the construct dictionary from forms/construct_dictionary.csv, the
instrument families of each job's reports from instrument_mentions.csv and instruments.csv (types decided by R1) and
the jobs from jobs.json (make_study_map.py). Appends one JSON line per job to extraction/draft/<name>.jsonl
(resumable). The drafts are stored unchanged; R1 verifies every value.
Template: papers/misophonia-prevalence/extraction/extract.py (same runner; form, dictionary and families changed).

Run (pilot): .venv/Scripts/python.exe papers/ai-dependence-correlates/extraction/extract.py --run 2026-10-16 --name pilot_2026-10-17 --only R0204 R4336 R4677 R4615 R0691
Run (all):   .venv/Scripts/python.exe papers/ai-dependence-correlates/extraction/extract.py --run 2026-10-16 --name extract_<date>
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all  # noqa: E402

sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402
from instrument_families import FAMILIES  # noqa: E402

SEED = 20261022
MAX_CHARS = 400_000  # per report; jobs.json keeps the attached reports within this budget
# Retrieved files that hold a whole journal issue: only the report's own pages ("=== Page N ===" markers) are sent.
PAGE_RANGES = {"R2972": (210, 218)}   # IJMP 2026, 9(5), whole issue of 1.58 million characters; article pp. 210-218


def blocks(md: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", md, re.S)


def field(enum: list[str] | None = None) -> dict:
    value = {"type": "string", "maxLength": 400}
    if enum:
        value = {"type": "string", "enum": enum}
    return {"type": "object",
            "properties": {"value": value, "loc": {"type": "string", "maxLength": 160},
                           "quote": {"type": "string", "maxLength": 600}},
            "required": ["value", "loc", "quote"], "additionalProperties": False}


def text_(n: int) -> dict:
    return {"type": "string", "maxLength": n}


def constructs() -> list[dict]:
    return list(csv.DictReader((PAPER / "forms" / "construct_dictionary.csv").open(encoding="utf-8")))


def build_schema(spec: dict) -> dict:
    sf = spec["sample_fields"]
    en = spec["effect_enums"]
    rob_item = {"type": "object",
                "properties": {"rating": {"type": "string", "enum": spec["rob_ratings"]}, "reason": text_(400),
                               "loc": text_(160), "quote": text_(600)},
                "required": ["rating", "reason", "loc", "quote"], "additionalProperties": False}
    rob = {"type": "object", "properties": {f"rob_{i}": rob_item for i in range(1, 7)},
           "required": [f"rob_{i}" for i in range(1, 7)], "additionalProperties": False}
    eff_props = {
        "exposure_family": text_(80), "exposure_part": text_(160), "exposure_alpha": text_(40),
        "correlate_construct": {"type": "string", "enum": [c["construct"] for c in constructs()]},
        "correlate_instrument": text_(200), "correlate_alpha": text_(40), "direction_note": text_(200),
        "stat_type": {"type": "string", "enum": en["stat_type"]}, "value": text_(120), "ci_or_se": text_(120),
        "n": text_(40), "wave": text_(20), "location": text_(160), "quote": text_(600), "note": text_(400),
    }
    eff = {"type": "object", "properties": eff_props, "required": list(eff_props), "additionalProperties": False}
    s_props = {"label": text_(200), "reports": text_(300),
               **{k: field(v) for k, v in sf.items()},
               "notes": text_(1000), "rob": rob, "effects": {"type": "array", "maxItems": 200, "items": eff}}
    sample = {"type": "object", "properties": s_props, "required": list(s_props), "additionalProperties": False}
    top = {"samples": {"type": "array", "maxItems": 12, "items": sample}, "excluded_samples": text_(1000),
           "longitudinal_note": text_(2000), "consistency_notes": text_(2000), "note": text_(1000)}
    return {"type": "object", "properties": top, "required": list(top), "additionalProperties": False}


def load_prompt() -> tuple[str, str, str, dict]:
    md = (HERE / "extract_prompt.md").read_text(encoding="utf-8")
    b = blocks(md)
    system = next(body for lang, body in b if lang == "" and body.startswith("You are extracting"))
    preamble = next(body for lang, body in b if lang == "" and body.startswith("EXTRACTION FORM"))
    job_tpl = next(body for lang, body in b if lang == "" and body.startswith("CONSTRUCT DICTIONARY"))
    spec = json.loads(next(body for lang, body in b if lang == "json"))
    return system.strip(), preamble, job_tpl, build_schema(spec)


def dictionary_text() -> str:
    return "\n".join(f"- {c['construct']} ({c['role']}): includes {c['includes']}; typical instruments "
                     f"{c['typical_instruments'] or 'none listed'}; excludes {c['excludes'] or 'nothing listed'}"
                     for c in constructs())


def families_text(reports: list[str]) -> str:
    """The instrument families of the job's reports with their total score and subscales (instruments.csv)."""
    label = {fid: lab for fid, lab, _, _ in FAMILIES}
    parts = defaultdict(list)
    for r in csv.DictReader((HERE / "instruments.csv").open(encoding="utf-8")):
        parts[r["family"]].append(r["part"])
    used = defaultdict(list)
    for m in csv.DictReader((HERE / "instrument_mentions.csv").open(encoding="utf-8")):
        if m["rec_id"] in reports:
            used[m["family"]].append(m)
    out = []
    for fid, ms in used.items():
        names = "; ".join(sorted({f"{m['rec_id']}: {m['name']}" for m in ms}))
        head = label.get(fid, "study-specific instrument")
        out.append(f"- {fid}: {head}. As named in the reports: {names}\n  Scores: " + " | ".join(parts[fid]))
    return "\n".join(out) or "- none listed (name any AI-dependence instrument as 'other: <name>')"


def report_text(k: str) -> str:
    raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
    text = raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw
    if k in PAGE_RANGES:
        lo, hi = PAGE_RANGES[k]
        pages = re.split(r"(?m)(?=^=== Page \d+ ===)", text)
        text = "".join(pg for pg in pages
                       if (m := re.match(r"=== Page (\d+) ===", pg)) and lo <= int(m.group(1)) <= hi)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--only", nargs="*", help="job ids (main rec_ids) to process")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=3)
    a = ap.parse_args()
    system, preamble, job_tpl, schema = load_prompt()
    recs = load_records(a.run)
    jobs = json.loads((HERE / "jobs.json").read_text(encoding="utf-8"))
    dictionary = dictionary_text()
    items = []
    for j in jobs:
        if a.only and j["job_id"] not in a.only:
            continue
        main_rec = recs[j["main"]]
        main_text = report_text(j["main"])
        links = []
        if j["link_reason"]:
            links.append(f"Linked reports: {j['link_reason']}")
        if j["attached"]:
            links.append("Attached below (use them only to fill values the main report does not give, or to note "
                         f"differences): {', '.join(j['attached'])}")
        if j["listed_only"]:
            links.append(f"Other reports of these samples, not attached (too long): {', '.join(j['listed_only'])}")
        for po in j["possible_overlap"]:
            links.append(f"Note for the sample notes: {po}")
        if j.get("job_notes"):
            links.append(f"Note for the sample notes: {j['job_notes']}")
        att = []
        for e in j["attached"]:
            u = recs[e]
            t = report_text(e)
            att.append(f"\nATTACHED REPORT {e}\nTitle: {u['title']}\nYear: {u.get('year')}; venue: {u.get('venue')}; "
                       f"DOI: {u.get('doi') or 'none'}\nFull text ({len(t):,} characters):\n{t[:MAX_CHARS]}")
        body = job_tpl.format(
            dictionary=dictionary, families=families_text([j["main"], *j["attached"]]), job_id=j["job_id"],
            study_id=j["study_id"], samples=j["samples"], links="\n".join(links), main_id=j["main"],
            main_title=main_rec["title"], main_year=main_rec.get("year"), main_venue=main_rec.get("venue"),
            main_doi=main_rec.get("doi") or "none", main_chars=f"{len(main_text):,}",
            main_truncated=f"; cut to the first {MAX_CHARS:,} characters" if len(main_text) > MAX_CHARS else "",
            main_text=main_text[:MAX_CHARS], attached="\n".join(att))
        items.append({"conv_id": j["job_id"], "prompt": preamble + "\n" + body})

    # A job with many subscales and correlates can need a long answer (misophonia: 28.6k output tokens for two samples).
    judge = Judge(system_prompt=system, schema=schema, model="claude-opus-5-5", effort="high", timeout=2400,
                  extra_env={"CLAUDE_CODE_MAX_OUTPUT_TOKENS": "64000"})
    out = HERE / "draft" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, lambda it: it["prompt"], judge, out, concurrency=a.concurrency, seed=SEED,
                          limit=a.limit))


if __name__ == "__main__":
    main()
