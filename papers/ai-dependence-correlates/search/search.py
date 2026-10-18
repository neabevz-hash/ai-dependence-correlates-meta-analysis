"""Automated searches for the AI-dependence correlates meta-analysis (protocol, sections 9-10).

Runs every automated search and writes the raw records to search/runs/<date>/raw/<source>.jsonl and the run log
(query strings, record counts, timestamps) to search/runs/<date>/search_log.json. dedup.py then merges duplicates
and builds the screening list. Template: papers/misophonia-prevalence/search/search.py; phrase sets from the novelty
check (novelty/fetch_sources.py), with the over-reliance forms restricted by a measurement filter (protocol §10).

Sources:
  pubmed           PubMed, proximity pairs [tiab:~3] (quoted phrases are silently dropped when missing from
                   PubMed's phrase index);
  europepmc        Europe PMC including preprints, TITLE_ABS phrases;
  openalex         OpenAlex, title-and-abstract phrase search;
  openalex_non_en  OpenAlex, non-English terms;
  s2               Semantic Scholar bulk search;
  crossref         Crossref, relevance-sorted queries, kept when title or abstract matches (posted content, INPLASY);
  datacite         DataCite (theses, OSF, Zenodo, figshare, ScienceDB);
  openaire         OpenAIRE Graph (repository publications, theses);
  core             CORE API v3 (repositories);
  citations        OpenAlex: records citing the development papers of seven AI-dependence instruments.
Manual sources (SciELO, Google Scholar via Publish or Perish) go through import_manual.py (misophonia) into the same format.

Run:  .venv/Scripts/python.exe papers/ai-dependence-correlates/search/search.py [sources...] [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

# ---------------------------------------------------------------- phrase sets (protocol §10)
AI = ["AI", "artificial intelligence", "ChatGPT", "GenAI", "generative AI", "generative artificial intelligence",
      "chatbot", "chatbots", "AI chatbots", "conversational agent", "conversational agents", "conversational AI",
      "LLM", "LLMs", "large language model", "large language models", "AI companion", "AI companions",
      "AI tools", "AI technology", "Replika"]


def _uniq(xs):
    seen, out = set(), []
    for x in xs:
        if x.lower() not in seen:
            seen.add(x.lower())
            out.append(x)
    return out


DEP_PHRASES = _uniq([p for a in AI for p in (
    f"{a} addiction", f"{a} dependence", f"{a} dependency", f"dependence on {a}", f"dependency on {a}",
    f"addiction to {a}", f"problematic {a} use", f"problematic use of {a}", f"excessive {a} use",
    f"excessive use of {a}", f"compulsive {a} use", f"compulsive use of {a}", f"addictive {a} use",
    f"addictive use of {a}", f"{a} use disorder",
    f"problematic {a} usage", f"excessive {a} usage", f"compulsive {a} usage", f"addictive {a} usage")])
OVR_PHRASES = _uniq([p for a in AI for p in (
    f"overreliance on {a}", f"over-reliance on {a}", f"{a} overreliance", f"{a} over-reliance",
    f"{a} overuse", f"overuse of {a}")])
MEASURE = ["scale", "questionnaire", "survey", "inventory", "respondents", "self-report"]
# AI friends and companions: the dependence word is often not next to the AI word ("addiction to the app",
# "compulsive chat with a social chatbot"), so they get a Boolean AND query (added after the check run, 2026-10-16:
# two seed studies were missed without it).
COMPANION_TERMS = ["AI friend", "AI friends", "AI friendship", "AI companion", "AI companions", "social chatbot",
                   "social chatbots", "companion chatbot", "companion chatbots", "Replika", "Character.AI", "Xiaoice",
                   "AI girlfriend", "AI boyfriend"]
COMPANION_DEP = ["addiction", "addicted", "addictive", "dependence", "dependency", "compulsive", "problematic"]

PM_AI = ["AI", "artificial intelligence", "ChatGPT", "GenAI", "generative AI", "chatbot", "chatbots",
         "conversational agent", "conversational agents", "LLM", "large language model", "large language models",
         "AI companion", "AI companions", "Replika"]
PM_DEP = ["addiction", "dependence", "dependency", "addictive", "problematic use", "compulsive use", "excessive use",
          "problematic usage", "compulsive usage", "excessive usage"]
PM_OVR = ["overreliance", "over-reliance", "overuse"]
PM_MEASURE = " OR ".join(f"{m}[tiab]" for m in MEASURE)

NON_EN = ["人工智能依赖", "AI依赖", "生成式人工智能依赖", "ChatGPT依赖", "人工智能成瘾", "AI成瘾", "聊天机器人依赖",
          "인공지능 의존", "AI 의존", "AI 중독", "생성형 AI 의존", "AI依存", "生成AI依存",
          "yapay zeka bağımlılığı", "yapay zekâ bağımlılığı", "ChatGPT bağımlılığı",
          "dependencia de la inteligencia artificial", "adicción a la inteligencia artificial", "dependencia de ChatGPT",
          "dependência de inteligência artificial", "dependência da inteligência artificial", "dependência do ChatGPT",
          "зависимость от искусственного интеллекта", "зависимость от ИИ", "KI-Abhängigkeit", "KI-Sucht"]

# One query per phrase (OpenAIRE: at most four OR operators per query; CORE: no OR lists inside field queries).
CORE_PHRASES = ["AI dependence", "AI dependency", "AI addiction", "artificial intelligence dependence",
                "artificial intelligence addiction", "ChatGPT addiction", "ChatGPT dependence", "ChatGPT dependency",
                "problematic ChatGPT use", "problematic AI use", "problematic use of AI", "generative AI addiction",
                "generative AI dependence", "chatbot addiction", "chatbot dependence", "dependence on AI",
                "dependence on ChatGPT", "addiction to AI", "AI companion addiction", "emotional dependence on AI",
                "conversational AI dependence", "LLM dependence", "large language model dependence", "AI use disorder"]

CR_QUERIES = ["AI dependence", "AI dependency", "AI addiction", "ChatGPT addiction", "ChatGPT dependence",
              "problematic ChatGPT use", "problematic AI use", "generative AI dependence", "generative AI addiction",
              "chatbot addiction", "chatbot dependence", "artificial intelligence dependence",
              "artificial intelligence addiction", "dependence on artificial intelligence", "AI companion dependence",
              "emotional dependence on AI", "large language model dependence", "conversational AI dependence"]
CR_KEEP = re.compile(
    r"(\bai\b|artificial intelligence|chatgpt|chatbot|generative|genai|\bllms?\b|large language model|conversational|replika)"
    r".{0,60}(addict|dependen|problematic|compulsive|use disorder)|"
    r"(addict|dependen|problematic|compulsive).{0,60}"
    r"(\bai\b|artificial intelligence|chatgpt|chatbot|generative|genai|\bllms?\b|large language model|conversational|replika)",
    re.I | re.S)

# Development papers of the seven most-cited AI-dependence instruments (OpenAlex citations, 2026-10-16).
INSTRUMENT_DOIS = {
    "Dependence on AI, university students (Morales-García et al., 2024)": "10.3389/feduc.2024.1323898",
    "Problematic ChatGPT Use Scale (Yu et al., 2024)": "10.1007/s12144-024-06259-z",
    "Generative AI Dependency Scale (Goh et al., 2025)": "10.1016/j.chbr.2025.100845",
    "AI Chatbot Dependence Scale (Zhang et al., 2025)": "10.1089/cyber.2024.0240",
    "LLM Dependence Scale (Li et al., 2025)": "10.1016/j.ijinfomgt.2025.102888",
    "Conversational AI Dependence Scale (Chen et al., 2025)": "10.3389/fpsyg.2025.1621540",
    "AI dependence scale, Chinese undergraduates (Wu et al., 2026)": "10.3389/fpsyg.2025.1725393",
}

UA = "ai-dependence-correlates-search/1.0 (mailto:mrexert@gmail.com)"


def load_env() -> dict[str, str]:
    env = {}
    if not (ROOT / ".env").exists():   # the public release has no keys; the phrase lists still import
        return env
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


ENV = load_env()
client = httpx.Client(headers={"User-Agent": UA}, timeout=90, follow_redirects=True)


def _request(method: str, url: str, params: dict | None = None, data: dict | None = None, tries: int = 6, **kw):
    last = None
    for i in range(tries):
        try:
            r = client.request(method, url, params=params, data=data, **kw)
        except httpx.HTTPError as e:  # network
            last = e
            time.sleep(3 * (i + 1))
            continue
        if r.status_code == 200:
            return r
        last = r
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(3 * (i + 1))
            continue
        r.raise_for_status()
    raise RuntimeError(f"{method} failed: {url} {params} -> {last}")


def get(url, params=None, **kw):
    return _request("GET", url, params=params, **kw)


def post(url, data, **kw):
    return _request("POST", url, data=data, **kw)


def chunks(xs: list, n: int):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def inv_to_text(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))


def norm_doi(d: str | None) -> str:
    d = (d or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/", "doi:"):
        if d.startswith(p):
            d = d[len(p):]
    return d


def q(p: str) -> str:
    return f'"{p}"'


# ---------------------------------------------------------------- sources
def pubmed_queries() -> list[str]:
    dep = [f'"{a} {d}"[tiab:~3]' for a in PM_AI for d in PM_DEP]
    ovr = [f'"{a} {d}"[tiab:~3]' for a in PM_AI for d in PM_OVR]
    qs = [" OR ".join(ch) for ch in chunks(dep, 35)]
    qs += [f"({' OR '.join(ch)}) AND ({PM_MEASURE})" for ch in chunks(ovr, 45)]
    qs.append("(" + " OR ".join(f'"{c}"[tiab]' for c in COMPANION_TERMS) + ") AND ("
              + " OR ".join(f"{d}[tiab]" for d in COMPANION_DEP) + ")")
    return qs


def _pubmed_parse(x: bytes) -> list[dict]:
    out = []
    root = etree.fromstring(x)
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//MedlineCitation/PMID")
        node = art.find(".//ArticleTitle")
        title = "".join(node.itertext()) if node is not None else ""
        abstract = " ".join("".join(a.itertext()) for a in art.findall(".//Abstract/AbstractText"))
        doi = next((aid.text or "" for aid in art.findall(".//PubmedData/ArticleIdList/ArticleId")
                    if aid.get("IdType") == "doi"), "")
        year = art.findtext(".//JournalIssue/PubDate/Year") or (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
        au = art.find(".//AuthorList/Author")
        first = (au.findtext("LastName") or au.findtext("CollectiveName") or "") if au is not None else ""
        out.append({
            "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": norm_doi(doi), "title": title,
            "abstract": abstract, "year": year, "venue": art.findtext(".//Journal/Title") or "",
            "first_author": first, "type": ";".join(p.text or "" for p in art.findall(".//PublicationType")),
            "language": ";".join(l.text or "" for l in art.findall(".//Language")),
        })
    for art in root.findall(".//PubmedBookArticle"):
        pmid = art.findtext(".//BookDocument/PMID")
        node = art.find(".//BookDocument/ArticleTitle")
        if node is None:
            node = art.find(".//BookDocument/Book/BookTitle")
        out.append({
            "source": "pubmed", "source_id": f"PMID:{pmid}", "pmid": pmid, "doi": "",
            "title": "".join(node.itertext()) if node is not None else "",
            "abstract": " ".join("".join(a.itertext()) for a in art.findall(".//BookDocument/Abstract/AbstractText")),
            "year": art.findtext(".//BookDocument/Book/PubDate/Year") or "",
            "venue": art.findtext(".//BookDocument/Book/BookTitle") or "", "first_author": "",
            "type": "Book Chapter", "language": "",
        })
    return out


def pubmed() -> tuple[list[dict], dict]:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    ids, meta = [], []
    for query in pubmed_queries():
        es = post(base + "esearch.fcgi", {"db": "pubmed", "term": query, "retmax": 9999, "retmode": "json"}).json()["esearchresult"]
        ids += es["idlist"]
        meta.append({"query": query, "count": int(es["count"]), "warnings": es.get("warninglist")})
        time.sleep(0.4)
    ids = list(dict.fromkeys(ids))
    out = []
    for ch in chunks(ids, 200):
        out += _pubmed_parse(post(base + "efetch.fcgi", {"db": "pubmed", "id": ",".join(ch), "retmode": "xml"}).content)
        time.sleep(0.4)
    return out, {"queries": meta, "unique_pmids": len(ids)}


def europepmc() -> tuple[list[dict], dict]:
    measure = " OR ".join(f"TITLE_ABS:{m}" for m in MEASURE)
    queries = [" OR ".join(f"TITLE_ABS:{q(p)}" for p in ch) for ch in chunks(DEP_PHRASES, 40)]
    queries += [f"({' OR '.join(f'TITLE_ABS:{q(p)}' for p in ch)}) AND ({measure})" for ch in chunks(OVR_PHRASES, 40)]
    queries.append("(" + " OR ".join(f"TITLE_ABS:{q(c)}" for c in COMPANION_TERMS) + ") AND ("
                   + " OR ".join(f"TITLE_ABS:{d}" for d in COMPANION_DEP) + ")")
    out, seen, meta = [], set(), []
    for query in queries:
        cursor, n, hit = "*", 0, None
        while True:
            d = post("https://www.ebi.ac.uk/europepmc/webservices/rest/searchPOST", {
                "query": query, "format": "json", "pageSize": 1000, "cursorMark": cursor, "resultType": "core"}).json()
            hit = d.get("hitCount")
            res = d.get("resultList", {}).get("result", [])
            for it in res:
                key = f"{it.get('source')}:{it.get('id')}"
                n += 1
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "source": "europepmc", "source_id": key, "pmid": it.get("pmid") or "",
                    "doi": norm_doi(it.get("doi")), "title": it.get("title", ""), "abstract": it.get("abstractText", ""),
                    "year": it.get("pubYear", ""),
                    "venue": ((it.get("journalInfo") or {}).get("journal") or {}).get("title")
                    or ((it.get("bookOrReportDetails") or {}).get("publisher")) or "",
                    "first_author": (it.get("authorString") or "").split(",")[0].split(" ")[0],
                    "type": ";".join((it.get("pubTypeList") or {}).get("pubType", [])) + f"|src={it.get('source')}",
                    "language": it.get("language", ""),
                })
            nxt = d.get("nextCursorMark")
            if not res or nxt == cursor or n >= (hit or 0):   # a new cursor comes even after the last page
                break
            cursor = nxt
        meta.append({"query": query, "count": hit})
        time.sleep(0.5)
    return out, {"queries": meta}


OA_SELECT = "id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships,ids,language,cited_by_count"


def _openalex_page(filter_str: str) -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        d = get("https://api.openalex.org/works", {"filter": filter_str, "per_page": 200, "cursor": cursor,
                                                   "api_key": ENV["OPENALEX_API_KEY"], "select": OA_SELECT}).json()
        out.extend(d["results"])
        cursor = d["meta"].get("next_cursor") if d["results"] else None
    return out


def _openalex_rec(w: dict, source: str, extra: dict | None = None) -> dict:
    loc = w.get("primary_location") or {}
    auth = w.get("authorships") or []
    rec = {
        "source": source, "source_id": w["id"].replace("https://openalex.org/", ""),
        "pmid": ((w.get("ids") or {}).get("pmid") or "").replace("https://pubmed.ncbi.nlm.nih.gov/", ""),
        "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": inv_to_text(w.get("abstract_inverted_index")),
        "year": w.get("publication_year"), "venue": (loc.get("source") or {}).get("display_name") or "",
        "first_author": ((auth[0].get("author") or {}).get("display_name") or "").split(" ")[-1] if auth else "",
        "type": w.get("type") or "", "language": w.get("language") or "",
    }
    if extra:
        rec.update(extra)
    return rec


def _openalex_union(filters: list[str], source: str) -> tuple[list[dict], list[dict]]:
    out, seen, meta = [], set(), []
    for flt in filters:
        raw = _openalex_page(flt)
        meta.append({"filter": flt, "count": len(raw)})
        for w in raw:
            if w["id"] not in seen:
                seen.add(w["id"])
                out.append(_openalex_rec(w, source))
        time.sleep(0.3)
    return out, meta


def openalex() -> tuple[list[dict], dict]:
    measure = "title_and_abstract.search:" + "|".join(q(m) if " " in m or "-" in m else m for m in MEASURE)
    filters = ["title_and_abstract.search:" + "|".join(q(p) for p in ch) for ch in chunks(DEP_PHRASES, 40)]
    filters += ["title_and_abstract.search:" + "|".join(q(p) for p in ch) + "," + measure for ch in chunks(OVR_PHRASES, 40)]
    filters.append("title_and_abstract.search:(" + " OR ".join(q(c) for c in COMPANION_TERMS) + ") AND ("
                   + " OR ".join(COMPANION_DEP) + ")")
    out, meta = _openalex_union(filters, "openalex")
    return out, {"filters": meta}


def openalex_non_en() -> tuple[list[dict], dict]:
    out, meta = _openalex_union([f"title_and_abstract.search:{q(t)}" for t in NON_EN], "openalex_non_en")
    return out, {"filters": meta}


def citations() -> tuple[list[dict], dict]:
    out, meta = [], {}
    for label, doi in INSTRUMENT_DOIS.items():
        wid = get(f"https://api.openalex.org/works/doi:{doi}", {"api_key": ENV["OPENALEX_API_KEY"], "select": "id"}).json()["id"].split("/")[-1]
        raw = _openalex_page(f"cites:{wid}")
        meta[label] = {"doi": doi, "openalex": wid, "citing_records": len(raw)}
        out.extend(_openalex_rec(w, "citations", {"cites": label}) for w in raw)
    return out, meta


def semantic_scholar() -> tuple[list[dict], dict]:
    measure = " | ".join(q(m) if "-" in m else m for m in MEASURE)
    queries = [" | ".join(q(p) for p in ch) for ch in chunks(DEP_PHRASES, 30)]
    queries += [f"({' | '.join(q(p) for p in ch)}) + ({measure})" for ch in chunks(OVR_PHRASES, 30)]
    queries.append("(" + " | ".join(q(c) for c in COMPANION_TERMS) + ") + (" + " | ".join(COMPANION_DEP) + ")")
    fields = "title,year,externalIds,publicationTypes,venue,abstract,authors"
    out, seen, meta = [], set(), []
    for query in queries:
        token, n = None, 0
        while True:
            params = {"query": query, "fields": fields}
            if token:
                params["token"] = token
            r = None
            for i in range(10):
                r = client.get("https://api.semanticscholar.org/graph/v1/paper/search/bulk", params=params)
                if r.status_code == 200:
                    break
                time.sleep(4 * (i + 1))
            if r is None or r.status_code != 200:
                raise RuntimeError(f"S2 failed: {r.status_code if r is not None else None}")
            d = r.json()
            for it in d.get("data", []):
                n += 1
                if it["paperId"] in seen:
                    continue
                seen.add(it["paperId"])
                ext = it.get("externalIds") or {}
                out.append({
                    "source": "s2", "source_id": f"S2:{it.get('paperId')}", "pmid": str(ext.get("PubMed") or ""),
                    "doi": norm_doi(ext.get("DOI")), "title": it.get("title") or "", "abstract": it.get("abstract") or "",
                    "year": it.get("year"), "venue": it.get("venue") or "",
                    "first_author": ((it.get("authors") or [{}])[0].get("name") or "").split(" ")[-1] if it.get("authors") else "",
                    "type": ";".join(it.get("publicationTypes") or []), "language": "",
                })
            token = d.get("token")
            if not token:
                break
            time.sleep(1.5)
        meta.append({"query": query, "count": n})
        time.sleep(1.5)
    return out, {"queries": meta}


def crossref() -> tuple[list[dict], dict]:
    """Crossref: posted content (Research Square, SSRN, Preprints.org), INPLASY, conference papers.

    With a cursor Crossref does not sort by relevance, so offset + sort=score; a query stops when a page of 1,000
    yields fewer than five records that match CR_KEEP in title or abstract (fuzzy search: the rest is noise).
    """
    out, seen, meta = [], set(), {}
    for query in CR_QUERIES:
        n, kept = 0, 0
        while n < 3000:
            m = get("https://api.crossref.org/works", {
                "query.bibliographic": query, "rows": 1000, "offset": n, "sort": "score", "order": "desc",
                "mailto": "mrexert@gmail.com",
                "select": "DOI,title,type,issued,container-title,abstract,author,publisher"}).json()["message"]
            items = m["items"]
            keep = [it for it in items if CR_KEEP.search(" ".join(it.get("title") or []) + " " + (it.get("abstract") or ""))]
            for it in keep:
                doi = it["DOI"].lower()
                if doi in seen:
                    continue
                seen.add(doi)
                kept += 1
                yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
                out.append({
                    "source": "crossref", "source_id": f"DOI:{doi}", "pmid": "", "doi": norm_doi(doi),
                    "title": " ".join(it.get("title") or []), "abstract": re.sub(r"<[^>]+>", " ", it.get("abstract") or ""),
                    "year": yr or "", "venue": " ".join(it.get("container-title") or []) or it.get("publisher") or "",
                    "first_author": ((it.get("author") or [{}])[0].get("family") or "") if it.get("author") else "",
                    "type": it.get("type") or "", "language": "",
                })
            n += len(items)
            if not items or len(keep) < 5:
                break
            time.sleep(1)
        meta[query] = {"scanned": n, "kept_new": kept}
    return out, {"queries": meta}


def datacite() -> tuple[list[dict], dict]:
    def field_query(terms: str) -> str:
        return f"titles.title:{terms} OR descriptions.description:{terms} OR subjects.subject:{terms}"
    measure = "(" + " OR ".join(q(m) if "-" in m else m for m in MEASURE) + ")"
    queries = [field_query("(" + " OR ".join(q(p) for p in ch) + ")") for ch in chunks(DEP_PHRASES, 40)]
    queries += [f"({field_query('(' + ' OR '.join(q(p) for p in ch) + ')')}) AND ({field_query(measure)})"
                for ch in chunks(OVR_PHRASES, 40)]
    companion = "(" + " OR ".join(q(c) for c in COMPANION_TERMS) + ")"
    queries.append(f"({field_query(companion)}) AND ({field_query('(' + ' OR '.join(COMPANION_DEP) + ')')})")
    out, seen, meta = [], set(), []
    for query in queries:
        url, params, total = "https://api.datacite.org/dois", {"query": query, "page[size]": 1000, "page[cursor]": 1}, None
        while url:
            d = get(url, params).json()
            total = (d.get("meta") or {}).get("total", total)
            for it in d.get("data", []):
                a = it["attributes"]
                doi = norm_doi(a.get("doi"))
                if doi in seen:
                    continue
                seen.add(doi)
                types = a.get("types") or {}
                descs = [dd for dd in a.get("descriptions") or [] if isinstance(dd.get("description"), str)]
                abstract = next((dd["description"] for dd in descs if dd.get("descriptionType") == "Abstract"), "") \
                    or " ".join(dd["description"] for dd in descs)
                creator = (a.get("creators") or [{}])[0] if a.get("creators") else {}
                publisher = a.get("publisher")
                out.append({
                    "source": "datacite", "source_id": f"DataCite:{doi}", "pmid": "", "doi": doi,
                    "title": " ".join(t.get("title", "") for t in (a.get("titles") or [])[:1]),
                    "abstract": abstract[:5000], "year": a.get("publicationYear") or "",
                    "venue": (a.get("container") or {}).get("title")
                    or (publisher.get("name") if isinstance(publisher, dict) else publisher) or "",
                    "first_author": creator.get("familyName") or (creator.get("name") or "").split(",")[0],
                    "type": f"{types.get('resourceTypeGeneral') or ''}/{types.get('resourceType') or ''}",
                    "language": a.get("language") or "",
                })
            url = (d.get("links") or {}).get("next")
            params = None
        meta.append({"query": query, "total": total})
        time.sleep(0.5)
    return out, {"queries": meta}


def openaire() -> tuple[list[dict], dict]:
    """OpenAIRE Graph API (at most four OR operators per query: CORE_PHRASES in groups of five)."""
    out, seen, meta = [], set(), {}
    for ch in chunks(CORE_PHRASES, 5):
        query = " OR ".join(q(p) for p in ch)
        cursor, n, found = "*", 0, None
        while cursor:
            d = get("https://api.openaire.eu/graph/v1/researchProducts",
                    {"search": query, "type": "publication", "pageSize": 100, "cursor": cursor}).json()
            head = d.get("header") or {}
            found = head.get("numFound", found)
            res = d.get("results") or []
            for w in res:
                n += 1
                if w.get("id") in seen:
                    continue
                seen.add(w.get("id"))
                pids = {(p.get("scheme") or "").lower(): p.get("value") for p in (w.get("pids") or [])}
                inst = w.get("instances") or []
                for i in inst:
                    for p in (i.get("pids") or []) + (i.get("alternateIdentifiers") or []):
                        pids.setdefault((p.get("scheme") or "").lower(), p.get("value"))
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                out.append({
                    "source": "openaire", "source_id": f"OpenAIRE:{w.get('id')}", "pmid": str(pids.get("pmid") or ""),
                    "doi": norm_doi(pids.get("doi")), "title": w.get("mainTitle") or "",
                    "abstract": " ".join(w.get("descriptions") or [])[:5000],
                    "year": (w.get("publicationDate") or "")[:4],
                    "venue": (w.get("container") or {}).get("name") or w.get("publisher") or "",
                    "first_author": auth.get("surname") or (auth.get("fullName") or "").split(",")[0],
                    "type": "; ".join(sorted({i.get("type") for i in inst if i.get("type")})) or w.get("type") or "",
                    "language": (w.get("language") or {}).get("code") or "",
                    "url": next((u for i in inst for u in (i.get("urls") or [])), ""),
                })
            cursor = head.get("nextCursor") if res else None
            time.sleep(1)
        meta[query] = {"numFound": found, "retrieved": n}
    return out, {"type": "publication", "queries": meta}


def _fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()


def term_in(term: str, text: str) -> bool:
    """True if the phrase occurs as words; case, accents and plural endings ignored."""
    words = _fold(term.strip('"')).split()
    return re.search(r"\b" + r"\s+".join(re.escape(w) for w in words) + r"\w*", _fold(text)) is not None


def core() -> tuple[list[dict], dict]:
    """CORE API v3, title or abstract, one query per phrase; records without the phrase in title or abstract are
    dropped (CORE matches phrases loosely). At most 10 requests a minute: the client paces itself and honours 429.
    A query stops at the first page of 100 with fewer than five phrase matches (check run 2026-10-16: loose matching
    returned thousands of pages)."""
    out, seen, meta = [], set(), {}
    headers = {"Authorization": f"Bearer {ENV['CORE_API_KEY']}"} if ENV.get("CORE_API_KEY") else {}
    for term in CORE_PHRASES:
        query = f"title:{q(term)} OR abstract:{q(term)}"
        offset, total, dropped = 0, None, 0
        while True:
            for attempt in range(10):
                r = client.get("https://api.core.ac.uk/v3/search/works/", headers=headers,
                               params={"q": query, "limit": 100, "offset": offset, "exclude": "fullText"})
                if r.status_code == 200:
                    break
                until = r.headers.get("x-ratelimit-retry-after")
                try:
                    wait = (datetime.fromisoformat(until.replace("+0000", "+00:00")) - datetime.now(timezone.utc)).total_seconds() + 5
                except (AttributeError, ValueError):
                    wait = 30 * (attempt + 1)
                print(f"core: HTTP {r.status_code}, waiting {max(wait, 5):.0f} s", flush=True)
                time.sleep(min(max(wait, 5), 1200))
            else:
                raise RuntimeError(f"CORE failed for {query!r} at offset {offset}: {r.status_code} {r.text[:200]}")
            d = r.json()
            total = d.get("totalHits", total)
            res = d.get("results") or []
            kept_page = 0
            for w in res:
                if not term_in(term, f"{w.get('title') or ''} {w.get('abstract') or ''}"):
                    dropped += 1
                    continue
                kept_page += 1
                if w.get("id") in seen:
                    continue
                seen.add(w.get("id"))
                auth = (w.get("authors") or [{}])[0] if w.get("authors") else {}
                journals = w.get("journals") or []
                out.append({
                    "source": "core", "source_id": f"CORE:{w.get('id')}", "pmid": str(w.get("pubmedId") or ""),
                    "doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "abstract": (w.get("abstract") or "")[:5000],
                    "year": w.get("yearPublished") or "",
                    "venue": (journals[0].get("title") if journals else "") or w.get("publisher") or "",
                    "first_author": (auth.get("name") or "").split(",")[0].split(" ")[-1],
                    "type": w.get("documentType") or "", "language": ((w.get("language") or {}).get("code") or ""),
                    "url": w.get("downloadUrl") or "",
                })
            offset += len(res)
            time.sleep(7)
            # CORE matches loosely and ranks by relevance: a page of 100 with fewer than 5 phrase matches ends the query
            if not res or offset >= (total or 0) or kept_page < 5:
                break
        meta[query] = {"totalHits": total, "scanned": offset, "dropped_phrase_not_in_title_or_abstract": dropped}
    return out, {"queries": meta, "authenticated": bool(headers)}


SOURCES = {"pubmed": pubmed, "europepmc": europepmc, "openalex": openalex, "openalex_non_en": openalex_non_en,
           "s2": semantic_scholar, "crossref": crossref, "datacite": datacite, "openaire": openaire, "core": core,
           "citations": citations}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="*", default=list(SOURCES))
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    (run / "raw").mkdir(parents=True, exist_ok=True)
    log_path = run / "search_log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    log["_phrase_sets"] = {"dep_phrases": len(DEP_PHRASES), "ovr_phrases": len(OVR_PHRASES), "measure_filter": MEASURE,
                           "companion_terms": COMPANION_TERMS, "companion_dependence_terms": COMPANION_DEP}
    for name in a.sources:
        t0 = time.time()
        try:
            recs, meta = SOURCES[name]()
        except Exception as e:  # noqa: BLE001
            print(f"{name}: FAILED {e!r}", file=sys.stderr, flush=True)
            log[name] = {"error": repr(e), "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        with (run / "raw" / f"{name}.jsonl").open("w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log[name] = {"records": len(recs), "meta": meta,
                     "searched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "seconds": round(time.time() - t0, 1)}
        print(f"{name}: {len(recs)} records", flush=True)
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
