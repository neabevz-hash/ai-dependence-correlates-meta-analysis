"""OSF-hosted records after the OSF outage of 16-18 October 2026 (deviations.md, D9): registrations and projects.

Most records with a 10.17605/osf.io DOI that went to full text are OSF registrations (preregistration forms) or
projects, not reports: they have no primary file, so fetch_oa.py cannot download them. For a registration, the
registration form is its full text: title, description, schema and every registered answer, taken from the OSF API
(/v2/registrations/<guid>/) and written to fulltext/text/<rec_id>.txt. A project (node) has no report: its
description and file list are logged, and the record stays "not retrieved" unless a manuscript file is among the files.
The OSF API limits anonymous requests (HTTP 429): the script waits between requests and backs off on 429.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/fulltext/fetch_osf_registrations.py R0491 R0617 ...
"""
from __future__ import annotations

import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
LOG = HERE / "retrieval_log.csv"
TEXT = HERE / "text"
UA = "ai-dependence-correlates-search/1.0 (mailto:mrexert@gmail.com)"
client = httpx.Client(headers={"User-Agent": UA}, timeout=90, follow_redirects=False)


def get(url: str) -> httpx.Response:
    for attempt in range(8):
        r = client.get(url)
        if r.status_code != 429:
            time.sleep(4)
            return r
        time.sleep(60 * (attempt + 1))
    return r


def flat(v, depth=0) -> str:
    if isinstance(v, dict):
        return "; ".join(f"{k}: {flat(x, depth + 1)}" for k, x in v.items() if x not in (None, "", [], {}))
    if isinstance(v, list):
        return "; ".join(flat(x, depth + 1) for x in v if x not in (None, "", [], {}))
    return str(v)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ids = sys.argv[1:]
    rows = list(csv.DictReader(LOG.open(encoding="utf-8-sig")))
    by = {r["rec_id"]: r for r in rows}
    for rid in ids:
        row = by[rid]
        guid = row["doi"].split("osf.io/")[1].split("_")[0]
        g = get(f"https://api.osf.io/v2/guids/{guid}/")
        loc = g.headers.get("location", "")
        kind = "registrations" if "/registrations/" in loc else "nodes" if "/nodes/" in loc else "preprints" if "/preprints/" in loc else f"unknown ({g.status_code})"
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        if kind == "registrations":
            r = get(f"https://api.osf.io/v2/registrations/{guid}/")
            a = r.json()["data"]["attributes"]
            answers = a.get("registration_responses") or {}
            if not answers:
                answers = {k: (v.get("value") if isinstance(v, dict) else v) for k, v in (a.get("registered_meta") or {}).items()}
            lines = [f"OSF REGISTRATION {guid} ({a.get('registration_supplement') or 'schema not stated'})",
                     f"Title: {a.get('title')}", f"Registered: {a.get('date_registered')}",
                     f"Description: {a.get('description') or ''}", "", "=== Registered answers ==="]
            lines += [f"{k}: {flat(v)}" for k, v in answers.items() if v not in (None, "", [], {})]
            text = "\n".join(lines)
            (TEXT / f"{rid}.txt").write_text(f"REC_ID: {rid}\nSOURCE: osf_registration_form\nURL: https://osf.io/{guid}/\n"
                                             f"RETRIEVED_UTC: {now}\n\n{text}", encoding="utf-8")
            row.update({"status": "retrieved", "source": "osf_registration_form", "url": f"https://api.osf.io/v2/registrations/{guid}/",
                        "chars": str(len(text)), "pages": "", "sha256": "", "at_utc": now,
                        "tried": (row["tried"] + " | osf registration form (API) ok, 2026-10-18").strip(" |")})
            print(f"{rid} {guid} registration: {len(text):,} characters, {len(answers)} answers")
        else:
            note = f"osf {kind}: no report (2026-10-18)"
            if kind == "nodes":
                n = get(f"https://api.osf.io/v2/nodes/{guid}/").json()["data"]["attributes"]
                f = get(f"https://api.osf.io/v2/nodes/{guid}/files/osfstorage/")
                names = [i["attributes"]["name"] for i in (f.json().get("data") or [])] if f.status_code == 200 else []
                note = f"osf project without a report: files {names[:6]} (2026-10-18)"
                print(f"{rid} {guid} project: {n.get('title', '')[:70]} | files {names[:6]}")
            else:
                print(f"{rid} {guid} {kind}")
            row["tried"] = (row["tried"] + " | " + note).strip(" |")
    with LOG.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
