"""Backward and forward citation searching of the included studies (protocol §9, "Citation searching").

Seeds: every report R1 judged eligible at full text, and the systematic reviews named in the protocol. Through OpenAlex
(API key OPENALEX_API_KEY in .env):
  backward - every work in the seeds' reference lists (referenced_works);
  forward  - every work citing a seed (filter cites:).
The works are compared with the records of the main search (DOI, OpenAlex ID, normalised title); only new records go
on. Writes search/runs/<date>-citations/records_new.jsonl, raw_backward.jsonl, raw_forward.jsonl and chase_log.json.
Seeds without a DOI are found by exact title in OpenAlex where possible; the log lists those not found.

Template: papers/misophonia-prevalence/search/citation_chase.py; here the topic filter is the AI x dependence pattern
(an AI term within 60 characters of a dependence term, or a companion term with a dependence term).
Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/search/citation_chase.py --run 2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))

import search as S  # noqa: E402  (helpers: get, ENV, norm_doi, _openalex_page, _openalex_rec)
from dedup import doi_key, norm_title  # noqa: E402

REVIEWS = {  # reviews named in the protocol (§6, §9)
    "Dagnino et al. 2026": "10.3389/fpsyg.2026.1900953",
    "Fneich et al. 2026": "10.1007/s11469-026-01724-1",
    "Yan 2026": "10.3389/fpsyg.2026.1827795",
    "An et al. 2026": "10.1057/s41599-026-08959-2",
    "He et al. 2026": "10.3389/fpsyg.2026.1808268",
    "Singh & Sharma 2026": "10.1007/s41347-026-00726-z",
    "Romero-Martinez et al. 2026 (preprint)": "10.21203/rs.3.rs-10599376/v1",
}
SELECT = "id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships,ids,language,cited_by_count"


def work_by_doi(doi: str) -> dict | None:
    try:
        r = S.get(f"https://api.openalex.org/works/doi:{doi}", {"api_key": S.ENV["OPENALEX_API_KEY"],
                                                                "select": SELECT + ",referenced_works"}, tries=2)
        return r.json()
    except Exception:  # noqa: BLE001 - not in OpenAlex
        return None


def work_by_title(title: str, year) -> dict | None:
    t = norm_title(title)
    if len(t) < 25:
        return None
    try:
        r = S.get("https://api.openalex.org/works", {"filter": f"title.search:{title[:200].replace(',', ' ')}",
                                                     "per_page": 10, "api_key": S.ENV["OPENALEX_API_KEY"],
                                                     "select": SELECT + ",referenced_works"}, tries=2)
    except Exception:  # noqa: BLE001
        return None
    for w in r.json().get("results", []):
        if norm_title(w.get("title") or "") == t:
            return w
    return None


def by_ids(ids: list[str]) -> list[dict]:
    out = []
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        r = S.get("https://api.openalex.org/works", {"filter": "ids.openalex:" + "|".join(chunk), "per_page": 50,
                                                     "api_key": S.ENV["OPENALEX_API_KEY"], "select": SELECT})
        out.extend(r.json()["results"])
    return out


AI_RE = (r"(AI|artificial intelligence|chat ?gpt|chatbots?|gen ?ai|generative|llms?|large language models?|"
         r"conversational (agents?|ai)|ai compan|ai friend|replika|character\.ai|xiaoice)")
DEP_RE = r"(addict|dependen|problematic|overreli|over-reli|overuse|compulsive|excessive use|use disorder)"
TOPIC = re.compile(f"{AI_RE}.{{0,60}}{DEP_RE}|{DEP_RE}.{{0,60}}{AI_RE}", re.I | re.S)


def mentions_term(text: str) -> bool:
    """The exposure concept of the main search in title or abstract (AI term near a dependence term)."""
    return bool(TOPIC.search(text or ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="the main search run (records_unique.jsonl)")
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    recs = [json.loads(l) for l in (HERE / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")]
    known_doi = {doi_key(d) for r in recs for d in (r.get("all_dois") or r.get("doi") or "").split(";") if d}
    known_w = {p for r in recs for p in (r.get("source_ids") or "").split(";") if p.startswith("W")}
    known_t = {norm_title(r["title"]) for r in recs if r.get("title")}
    byid = {r["rec_id"]: r for r in recs}
    elig = [r["rec_id"] for r in csv.DictReader((PAPER / "fulltext" / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))
            if r["decision"] == "eligible"]

    seeds, not_found = {}, []
    for k in elig:
        r = byid[k]
        w = None
        ws = [p for p in (r.get("source_ids") or "").split(";") if p.startswith("W")]
        if ws:
            try:
                w = S.get(f"https://api.openalex.org/works/{ws[0]}", {"api_key": S.ENV["OPENALEX_API_KEY"],
                                                                      "select": SELECT + ",referenced_works"}, tries=2).json()
            except Exception:  # noqa: BLE001
                w = None
        if w is None and r.get("doi"):
            w = work_by_doi(r["doi"])
        if w is None:
            w = work_by_title(r.get("title") or "", r.get("year"))
        if w is None:
            not_found.append(k)
            continue
        seeds[k] = w
    for label, doi in REVIEWS.items():
        w = work_by_doi(doi)
        if w is None:
            not_found.append(label)
        else:
            seeds[label] = w

    backward_ids = sorted({x.split("/")[-1] for w in seeds.values() for x in (w.get("referenced_works") or [])})
    backward = by_ids(backward_ids)
    forward = []
    for label, w in seeds.items():
        wid = w["id"].split("/")[-1]
        for x in S._openalex_page(f"cites:{wid}"):
            x["_cites"] = label
            forward.append(x)

    run = HERE / "runs" / f"{a.date}-citations"
    run.mkdir(parents=True, exist_ok=True)
    for name, rows in (("raw_backward.jsonl", backward), ("raw_forward.jsonl", forward)):
        with (run / name).open("w", encoding="utf-8", newline="\n") as f:
            for x in rows:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")

    new, seen = [], set()
    status = {"backward": {"works": len(backward)}, "forward": {"links": len(forward)}}
    for source, rows in (("chase_backward", backward), ("chase_forward", forward)):
        k_known = 0
        for x in rows:
            wid = x["id"].split("/")[-1]
            rec = S._openalex_rec(x, source)
            t = norm_title(rec["title"])
            if wid in known_w or (rec["doi"] and doi_key(rec["doi"]) in known_doi) or (t and t in known_t):
                k_known += 1
                continue
            if wid in seen:
                continue
            seen.add(wid)
            text = f"{rec['title']} {rec['abstract']}"
            rec["mentions_term"] = mentions_term(text)
            new.append(rec)
        status[source.split("_")[1]]["already_in_main_set"] = k_known
    with (run / "records_new.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    log = {"run_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "seeds_found": len(seeds),
           "seeds_not_found": not_found, "backward_reference_ids": len(backward_ids), **status,
           "new_unique_records": len(new), "new_with_condition_term_in_title_or_abstract":
               sum(r["mentions_term"] for r in new),
           "new_by_source": {s: sum(r["source"] == s for r in new) for s in ("chase_backward", "chase_forward")}}
    (run / "chase_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
                                        newline="\n")
    print(json.dumps(log, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
