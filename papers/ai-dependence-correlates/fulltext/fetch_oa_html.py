"""Second pass for open-access full texts that fetch_oa.py did not get (protocol, section 11b).

Only legal open-access copies, no author contact; a page that answers with a bot check is recorded as blocked and not
worked around. For every report in retrieval_log.csv with status "not retrieved" and a DOI:
  1. Unpaywall and OpenAlex open-access locations (landing pages and PDF links);
  2. OJS journals (common for the Asian and Latin American journals in this set): an article page
     .../article/view/<id>/<galley> is turned into .../article/download/<id>/<galley>, and the galley links on
     .../article/view/<id> pages are followed;
  3. the HTML full text of an open-access landing page, when it is a full article: at least 15,000 characters
     and a methods or results heading. Tables are kept row by row ("cell | cell"), because correlations sit in tables.
  0. Zenodo records: the PDF file of the record (API), not the landing page.
Texts go to fulltext/text/<rec_id>.txt with SOURCE pdf_zenodo, pdf_ojs, pdf or oa_html; retrieval_log.csv is updated in place.
OSF-hosted preprints (OSF, PsyArXiv) need OSF, which is down from 16 to 19 October 2026: rerun this pass after that.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/fulltext/fetch_oa_html.py --run 2026-10-16
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin

from lxml import html as lhtml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fetch_oa as F  # noqa: E402  (same client, bot-check pattern, PDF reader and log format)

HERE = F.HERE
MIN_CHARS = 15_000
SECTION = re.compile(r"\b(method|methods|methodology|results|findings|participants|measures|metode|hasil|método|resultados)\b", re.I)
OJS_VIEW = re.compile(r"(/article/view/)(\d+)(?:/(\d+))?")


def unpaywall_locations(doi: str) -> list[str]:
    r = F.get(f"https://api.unpaywall.org/v2/{doi}", params={"email": F.EMAIL})
    if r is None or r.status_code != 200:
        return []
    d = r.json()
    if not d.get("is_oa"):
        return []
    urls = []
    for loc in [d.get("best_oa_location") or {}] + (d.get("oa_locations") or []):
        for k in ("url_for_pdf", "url_for_landing_page", "url"):
            if loc.get(k):
                urls.append(loc[k])
    return urls


def openalex_locations(doi: str) -> list[str]:
    r = F.get(f"https://api.openalex.org/works/doi:{doi}", params={"api_key": F.ENV.get("OPENALEX_API_KEY", "")})
    if r is None or r.status_code != 200:
        return []
    w = r.json()
    if not (w.get("open_access") or {}).get("is_oa"):
        return []
    urls = []
    for loc in [w.get("best_oa_location") or {}] + (w.get("locations") or []):
        if loc.get("is_oa"):
            for k in ("pdf_url", "landing_page_url"):
                if loc.get(k):
                    urls.append(loc[k])
    return urls


def html_text(page: bytes) -> str:
    doc = lhtml.fromstring(page)
    for bad in doc.xpath("//script|//style|//nav|//header|//footer|//noscript|//aside|//form"):
        bad.drop_tree()
    root = (doc.xpath("//article") or doc.xpath("//main") or doc.xpath("//*[@id='content' or @class='content']") or [doc])[0]
    for tb in root.xpath(".//table"):
        rows = [" | ".join(" ".join(c.text_content().split()) for c in tr.xpath("./th|./td")) for tr in tb.xpath(".//tr")]
        tb.getparent().replace(tb, lhtml.fromstring(f"<pre>\n=== Table ===\n{chr(10).join(rows)}\n</pre>"))
    text = root.text_content()
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()


def try_pdf(url: str) -> tuple[str | None, int | str, bytes | None, str]:
    data, note = F.fetch_pdf(url)
    if data:
        text, pages = F.pdf_to_text(data)
        if len(text) >= 3_000:
            return text, pages, data, "pdf ok"
        return None, "", None, "pdf too short"
    return None, "", None, note


def zenodo_pdfs(doi: str) -> list[str]:
    """Zenodo records: the PDF is a file of the record, not the landing page."""
    m = re.match(r"10\.5281/zenodo\.(\d+)$", doi)
    if not m:
        return []
    r = F.get(f"https://zenodo.org/api/records/{m.group(1)}")
    if r is None or r.status_code != 200:
        return []
    return [f["links"]["self"] for f in r.json().get("files", []) if f.get("key", "").lower().endswith(".pdf")]


def process(row: dict) -> dict:
    doi = row["doi"]
    tried = []
    for u in zenodo_pdfs(doi):
        text, pages, data, note = try_pdf(u)
        tried.append(f"zenodo:{note}")
        if text:
            return {"text": text, "source": "pdf_zenodo", "url": u, "pages": pages, "data": data, "tried": tried}
    urls = list(dict.fromkeys(unpaywall_locations(doi) + openalex_locations(doi)))
    if not urls:
        tried.append("html:no OA location")
    # OJS: view -> download, and galley links on the article page
    ojs = []
    for u in urls:
        m = OJS_VIEW.search(u)
        if m and m.group(3):
            ojs.append(u.replace(m.group(0), f"/article/download/{m.group(2)}/{m.group(3)}"))
    for u in ojs:
        text, pages, data, note = try_pdf(u)
        tried.append(f"ojs_download:{note}")
        if text:
            return {"text": text, "source": "pdf_ojs", "url": u, "pages": pages, "data": data, "tried": tried}
    for u in urls:
        r = F.get(u)
        if r is None:
            tried.append("html:no response")
            continue
        body = r.content[:400_000]
        if F.BOT.search(body.decode("utf-8", "ignore")):
            tried.append("html:blocked")
            continue
        if r.status_code != 200:
            tried.append(f"html:{r.status_code}")
            continue
        if body[:5] == b"%PDF-":
            text, pages, data, note = try_pdf(u)
            if text:
                return {"text": text, "source": "pdf", "url": u, "pages": pages, "data": data, "tried": tried + ["pdf ok"]}
            continue
        try:
            doc = lhtml.fromstring(r.content)
        except Exception:  # noqa: BLE001
            tried.append("html:unparsable")
            continue
        galleys = [urljoin(str(r.url), h) for h in doc.xpath("//a[contains(@class,'pdf') or contains(@class,'galley')]/@href")
                   if "/article/view/" in h or "/article/download/" in h]
        for g in galleys[:2]:
            m = OJS_VIEW.search(g)
            dl = g.replace(m.group(0), f"/article/download/{m.group(2)}/{m.group(3)}") if m and m.group(3) else g
            text, pages, data, note = try_pdf(dl)
            tried.append(f"ojs_galley:{note}")
            if text:
                return {"text": text, "source": "pdf_ojs", "url": dl, "pages": pages, "data": data, "tried": tried}
        text = html_text(r.content)
        if len(text) >= MIN_CHARS and SECTION.search(text):
            return {"text": text, "source": "oa_html", "url": str(r.url), "pages": "", "data": None, "tried": tried + ["html ok"]}
        tried.append(f"html:not a full article ({len(text)} chars)")
    return {"text": None, "tried": tried}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    done = {r["rec_id"]: r for r in csv.DictReader(F.LOG.open(encoding="utf-8-sig"))}
    todo = [r for r in done.values() if r["status"] != "retrieved" and r.get("doi")]
    if a.limit:
        todo = todo[:a.limit]
    print(f"{len(todo)} reports not retrieved by fetch_oa.py and with a DOI", flush=True)
    lock = threading.Lock()

    def run(row):
        res = process(row)
        out = dict(row)
        out["tried"] = (row.get("tried", "") + " | pass2: " + "; ".join(res["tried"])).strip(" |")
        if res.get("text"):
            now = F.utcnow()
            (F.TEXT / f"{row['rec_id']}.txt").write_text(
                f"REC_ID: {row['rec_id']}\nSOURCE: {res['source']}\nURL: {res['url']}\nRETRIEVED_UTC: {now}\n\n{res['text']}",
                encoding="utf-8")
            if res.get("data"):
                (F.PDF / f"{row['rec_id']}.pdf").write_bytes(res["data"])
            digest = hashlib.sha256(res["data"] if res.get("data") else res["text"].encode("utf-8")).hexdigest()
            out.update(status="retrieved", source=res["source"], url=res["url"], chars=len(res["text"]),
                       pages=res.get("pages", ""), sha256=digest, at_utc=now)
        return out

    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        futures = {pool.submit(run, r): r["rec_id"] for r in todo}
        for n, fut in enumerate(as_completed(futures), 1):
            rid = futures[fut]
            try:
                row = fut.result()
            except Exception as e:  # noqa: BLE001
                row = dict(done[rid])
                row["tried"] = (row.get("tried", "") + f" | pass2 error: {e!r}"[:200]).strip(" |")
            with lock:
                done[rid] = row
                with F.LOG.open("w", encoding="utf-8-sig", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=F.LOG_FIELDS)
                    w.writeheader()
                    w.writerows(done[k] for k in sorted(done))
            print(f"[{n}/{len(todo)}] {rid} {row['status']} {row.get('source', '')}", flush=True)
    got = sum(1 for r in done.values() if r["status"] == "retrieved")
    print(f"retrieved {got} of {len(done)} after pass 2", flush=True)


if __name__ == "__main__":
    main()
