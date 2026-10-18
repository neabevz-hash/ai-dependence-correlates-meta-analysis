"""List of open-access reports that only a person in a browser can download (publisher pages with bot checks).

For every report not retrieved by fetch_oa.py that Unpaywall or OpenAlex marks as open access, writes a line with
its open-access link and the file name to save it under (fulltext/manual/<rec_id>.pdf). Reports R1 labelled include
come first. Closed reports are counted, not listed: by R1's decision (deviations.md, 2026-10-11) authors are not
contacted, so they stay "not retrieved".

Template: papers/misophonia-prevalence/fulltext/manual_list.py.
Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/fulltext/manual_list.py --run 2026-10-16
Then save the PDFs and run fetch_oa.py --import-manual.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
EMAIL = "mrexert@gmail.com"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    env = {l.split("=", 1)[0].strip(): l.split("=", 1)[1].strip()
           for l in (ROOT / ".env").read_text(encoding="utf-8").splitlines() if "=" in l and not l.startswith("#")}
    client = httpx.Client(timeout=30, follow_redirects=True, headers={"User-Agent": f"ai-dependence-correlates/1.0 (mailto:{EMAIL})"})
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    final = {r["rec_id"]: r for r in csv.DictReader((PAPER / "screening" / "decisions" / "tiab_final.csv").open(encoding="utf-8-sig"))}
    log = [r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")) if r["status"] != "retrieved"]
    rows, closed, no_doi, osf = [], 0, 0, 0
    for r in log:
        rec, doi = recs[r["rec_id"]], r["doi"]
        if not doi:
            no_doi += 1
            continue
        if doi.startswith(("10.17605/", "10.31234/", "10.31235/", "10.31219/")):   # OSF-hosted: retried by script after OSF is back
            osf += 1
            continue
        link = ""
        u = client.get(f"https://api.unpaywall.org/v2/{doi}", params={"email": EMAIL})
        if u.status_code == 200 and u.json().get("is_oa"):
            best = u.json().get("best_oa_location") or {}
            link = best.get("url_for_landing_page") or best.get("url") or best.get("url_for_pdf") or ""
        if not link:
            w = client.get(f"https://api.openalex.org/works/doi:{doi}",
                           params={"select": "open_access,best_oa_location", "api_key": env.get("OPENALEX_API_KEY", "")})
            if w.status_code == 200 and (w.json().get("open_access") or {}).get("is_oa"):
                best = w.json().get("best_oa_location") or {}
                link = best.get("landing_page_url") or best.get("pdf_url") or (w.json().get("open_access") or {}).get("oa_url") or ""
        time.sleep(0.2)
        if not link:
            closed += 1
            continue
        rows.append({"rec_id": r["rec_id"], "r1": final[r["rec_id"]]["final_decision"], "year": rec.get("year"),
                     "title": rec["title"], "link": link})
    rows.sort(key=lambda x: (x["r1"] != "include", x["rec_id"]))
    lines = ["# Открытые статьи, которые скрипт скачать не смог", "",
             f"Это статьи в открытом доступе, но сайты издателей не отдают их программе (проверка на бота). "
             f"В обычном браузере они открываются. Всего {len(rows)}: сначала те, что вы пометили «включить», потом «не уверен».", "",
             "**Как:** откройте ссылку → скачайте PDF → сохраните в папку `papers/ai-dependence-correlates/fulltext/manual/` "
             "под именем из таблицы (например, `R0123.pdf`). Сколько сделаете — столько и войдёт; остальные пойдут в PRISMA "
             "как «reports not retrieved». Потом напишите — я подхвачу файлы.", "",
             f"Не попали в список: закрытые статьи без открытой версии — {closed}; записи без DOI — {no_doi}; "
             f"препринты и регистрации на OSF — {osf} (OSF закрыт до 19 октября, их скачает скрипт).", "",
             "| # | Ваша метка | Файл | Год | Название | Ссылка |", "| --- | --- | --- | --- | --- | --- |"]
    for i, x in enumerate(rows, 1):
        title = x["title"].replace("|", "/")[:110]
        lines.append(f"| {i} | {'включить' if x['r1'] == 'include' else 'не уверен'} | `{x['rec_id']}.pdf` | {x['year']} | {title} | [открыть]({x['link']}) |")
    (HERE / "MANUAL_PDFS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    (HERE / "manual").mkdir(exist_ok=True)
    print(f"open but not retrieved: {len(rows)} (include {sum(1 for x in rows if x['r1'] == 'include')}); OSF-hosted: {osf}; "
          f"closed: {closed}; no DOI: {no_doi}")


if __name__ == "__main__":
    main()
