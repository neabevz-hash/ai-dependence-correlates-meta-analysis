"""Supplementary files built from the logs and the verified tables, so that every number matches the record of the work.

S1_search.md        - search strategies, dates and counts per source (PRISMA-S), de-duplication, seed-set recall,
                      citation searching
S2_scales.md        - AI-dependence instrument families and their types (T1-T4) as decided by R1
S3_deviations.md    - every change and clarification after registration (deviations.md)
S4_ai.md            - the AI assistant's roles, models, prompts and their hashes, runs and agreement with R1
S5_excluded.md      - reports excluded at full text (database search and citation searching), with the primary reason
S6_samples.md       - characteristics of the included samples and the reports of each study
S7_effects.md       - every extracted zero-order association (forms/effects.csv)
S8_rob.md           - risk of bias (six AXIS-based items) per sample
S9_analyses.md      - pooled r by scale type, moderators, sensitivity analyses, leave-one-study-out, small-study effects
Template: papers/misophonia-prevalence/manuscript/make_supplement.py.

Run: .venv/Scripts/python.exe -I papers/ai-dependence-correlates/manuscript/make_supplement.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
OUT = HERE / "supplement"
RUN = PAPER / "search" / "runs" / "2026-10-16"
CHASE = PAPER / "search" / "runs" / "2026-10-17-citations"
RES = PAPER / "analysis" / "results"
sys.path.insert(0, str(HERE))
from make_tables import LABEL, TYPE  # noqa: E402
sys.path.insert(0, str(PAPER / "extraction"))
from finalize import AUTHOR_FIX  # noqa: E402

REASON_TEXT = {"no_eligible_correlate": "no correlate from the dictionary", "E5_design": "design (review, qualitative, other)",
               "E1_no_dependence_measure": "no measure of AI dependence", "E4_no_zero_order": "no zero-order association",
               "E3_out_of_scope": "out of scope", "other": "other"}
SOURCES = {"pubmed": ("PubMed", "NCBI E-utilities; phrase pairs within three words in title or abstract ([tiab:~3])"),
           "europepmc": ("Europe PMC", "REST API, searchPOST, TITLE_ABS phrases"),
           "openalex": ("OpenAlex", "API, title_and_abstract.search, phrases joined by OR"),
           "openalex_non_en": ("OpenAlex, other languages", "API, title_and_abstract.search, Chinese, Spanish, Portuguese, Turkish, Korean, Japanese, Russian and other phrases"),
           "s2": ("Semantic Scholar", "Graph API, bulk search, phrases joined by the OR operator (pipe)"),
           "crossref": ("Crossref", "REST API, query.bibliographic, sorted by relevance (offset), records kept only with the phrase in title or abstract"),
           "datacite": ("DataCite", "REST API, titles and descriptions"),
           "openaire": ("OpenAIRE Graph", "API, research products of type publication, at most four OR operators per query"),
           "core": ("CORE", "API v3, title or abstract, one query per phrase; early stop at a page of 100 with fewer than five phrase matches")}


def fmt(n) -> str:
    return f"{int(n):,}"


def cell(x) -> str:
    return re.sub(r"\s+", " ", str(x or "")).replace("|", "/").strip()


def jl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.open(encoding="utf-8") if l.strip()]


def records() -> dict[str, dict]:
    recs = {r["rec_id"]: r for r in jl(RUN / "records_unique.jsonl")}
    if (CHASE / "records_unique.jsonl").exists():
        recs.update({r["rec_id"]: r for r in jl(CHASE / "records_unique.jsonl")})
    return recs


def s1() -> str:
    log = json.loads((RUN / "search_log.json").read_text(encoding="utf-8"))
    dd = json.loads((RUN / "dedup_report.json").read_text(encoding="utf-8"))
    rc = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    ch = json.loads((CHASE / "chase_log.json").read_text(encoding="utf-8"))
    sys.path.insert(0, str(PAPER / "search"))
    import search as S   # the phrase lists exactly as run
    started = (RUN / "started_utc.txt").read_text(encoding="utf-8").strip()
    L = ["# Supplementary File S1. Search strategies (PRISMA-S)", "",
         f"Final search started {started}, after the protocol was deposited (Zenodo, 10.5281/zenodo.23420672). No date, "
         "language or publication-type limits. Code: `search/search.py`; every query exactly as run, with its count, is in "
         "`search/runs/2026-10-16/search_log.json` of the data release.", "",
         "| Source | Interface and query form | Searched (UTC) | Queries | Records |", "| --- | --- | --- | --- | --- |"]
    for key, (name, iface) in SOURCES.items():
        v = log[key]
        m = v.get("meta", {})
        q = m.get("queries", m.get("filters", {}))
        L.append(f"| {name} | {iface} | {v['searched_at_utc'][:16].replace('T', ' ')} | {len(q)} | {fmt(v['records'])} |")
    cit = log["citations"]
    L.append(f"| Instrument citations | OpenAlex, works citing the development papers of {len(cit['meta'])} instruments | "
             f"{cit['searched_at_utc'][:16].replace('T', ' ')} | {len(cit['meta'])} | {fmt(cit['records'])} |")
    L += ["", "## Phrase sets", "",
          f"**AI terms ({len(S.AI)}):** " + "; ".join(S.AI) + ".", "",
          "**Dependence forms (19), with {a} for each AI term:** {a} addiction; {a} dependence; {a} dependency; dependence on "
          "{a}; dependency on {a}; addiction to {a}; problematic {a} use; problematic use of {a}; excessive {a} use; "
          "excessive use of {a}; compulsive {a} use; compulsive use of {a}; addictive {a} use; addictive use of {a}; "
          "{a} use disorder; problematic {a} usage; excessive {a} usage; compulsive {a} usage; addictive {a} usage.", "",
          "**Over-reliance forms (6):** overreliance on {a}; over-reliance on {a}; {a} overreliance; {a} over-reliance; "
          "{a} overuse; overuse of {a}. Over-reliance phrases were kept only with a measurement word in the title or "
          "abstract: " + ", ".join(S.MEASURE) + ".", "",
          f"Distinct phrases after removing duplicates: {len(S.DEP_PHRASES)} dependence and {len(S.OVR_PHRASES)} over-reliance "
          f"({len(S.DEP_PHRASES) + len(S.OVR_PHRASES)} in all).", "",
          "**AI companions (Boolean):** (" + " OR ".join(f'"{t}"' for t in S.COMPANION_TERMS) + ") AND (" +
          " OR ".join(S.COMPANION_DEP) + ").", "",
          "**PubMed proximity pairs:** each of " + "; ".join(S.PM_AI) + " with each of " + "; ".join(S.PM_DEP) +
          " within three words ([tiab:~3]).", "",
          "**Crossref queries:** " + "; ".join(S.CR_QUERIES) + ".", "",
          "**CORE and OpenAIRE phrases:** " + "; ".join(S.CORE_PHRASES) + ".", "",
          "**Instrument papers (citing works through OpenAlex):** " +
          "; ".join(f"{k} ({v['doi']}; {v['citing_records']} citing)" for k, v in cit["meta"].items()) + ".", "",
          "## De-duplication and recall", "",
          f"- Records retrieved: {fmt(dd['records_total'])}; unique: {fmt(dd['unique_records'])}; duplicates removed: "
          f"{fmt(dd['duplicates_removed'])} (of which {fmt(dd['pointer_or_component_records_attached'])} pointer or component "
          "records attached to their database record).",
          f"- Removed automatically as non-study records (datasets, peer-review reports, paratext, software, registrations "
          f"or figures as typed by the source): {fmt(dd['auto_removed_non_study_records'])}. Records screened: "
          f"{fmt(dd['records_to_screen'])}.",
          f"- Recall on the seed set (the {rc['seed_studies']} empirical studies of Dagnino et al., 2026): "
          f"{rc['in_screening_list']} of {rc['seed_studies']}; not found: " +
          "; ".join(f"{s['study']} ({s['year']})" for s in rc["studies"] if not s.get("to_screen")) +
          " (no quantitative measure of AI dependence).", "",
          "## Citation searching (deviations.md, D2)", "",
          f"Run on {ch['run_at_utc'][:16].replace('T', ' ')} UTC through OpenAlex (`search/citation_chase.py`); seeds: the "
          f"124 included reports and seven reviews; {ch['seeds_found']} found in OpenAlex.",
          f"- Backward: {fmt(ch['backward']['works'])} cited works, {fmt(ch['backward']['already_in_main_set'])} already in the "
          f"record set. Forward: {fmt(ch['forward']['links'])} citing links, {fmt(ch['forward']['already_in_main_set'])} already "
          "in the set.",
          f"- New records: {fmt(ch['new_unique_records'])}; with an AI term within 60 characters of a dependence term in the "
          f"title or abstract: {ch['new_with_condition_term_in_title_or_abstract']} (assessed at full text); included: 0."]
    return "\n".join(L) + "\n"


def s2() -> str:
    inst = list(csv.DictReader((PAPER / "extraction" / "instruments.csv").open(encoding="utf-8")))
    ment = list(csv.DictReader((PAPER / "extraction" / "instrument_mentions.csv").open(encoding="utf-8")))
    drafts = {d["conv_id"]: d["codes"] for d in jl(PAPER / "extraction" / "llm" / "types_2026-10-17.jsonl")}
    sys.path.insert(0, str(PAPER / "extraction"))
    from instrument_families import FAMILIES
    label = {f: (lab, doi) for f, lab, doi, _ in FAMILIES}
    by_fam = defaultdict(list)
    for m in ment:
        by_fam[m["family"]].append(m)
    parts = defaultdict(list)
    for r in inst:
        parts[r["family"]].append(r)
    L = ["# Supplementary File S2. AI-dependence instruments and their types", "",
         "Type by item content (protocol §13): T1 addiction-type (behavioural-addiction components), T2 functional "
         "dependence (reliance on AI for tasks and thinking), T3 emotional dependence (emotional support, attachment-like "
         "bond), T4 mixed or unclear. The AI drafted a type for every total score and subscale; the reviewer decided each "
         f"(changed from the draft: {sum(1 for r in inst if r['type'] != r['draft'])} of {len(inst)} scores). "
         "Study-specific instruments are listed as ADHOC_<report>.", "",
         "| Family | Instrument | Development paper | Reports | Evidence | Total score | Subscales (type) |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    order = sorted(parts, key=lambda f: (f.startswith("ADHOC_"), -len(by_fam[f]), f))
    for f in order:
        rows = parts[f]
        tot = next(r for r in rows if r["part"] == "total")
        subs = "; ".join(f"{cell(r['part'])} ({r['type']})" for r in rows if r["part"] != "total") or "none"
        lab, doi = label.get(f, (cell(by_fam[f][0]["name"]) if by_fam[f] else "", ""))
        L.append(f"| {f} | {cell(lab)} | {doi or 'NA'} | {', '.join(m['rec_id'] for m in by_fam[f])} | "
                 f"{drafts.get(f, {}).get('evidence', 'NR')} | {tot['type']} | {subs} |")
    c = Counter(r["type"] for r in inst if r["part"] == "total")
    L += ["", "Total scores by type: " + "; ".join(f"{TYPE[t]}: {c[t]}" for t in ("T1", "T2", "T3", "T4")) + "."]
    return "\n".join(L) + "\n"


def s3() -> str:
    md = (PAPER / "deviations.md").read_text(encoding="utf-8")
    return "# Supplementary File S3. Changes and clarifications after registration\n" + md.split("\n", 1)[1]


def run_row(task: str, prompt: str, path: Path) -> str:
    rows = jl(path)
    shas = sorted({r["judge"]["system_prompt_sha"] for r in rows})
    cli = sorted({r["judge"]["cli_version"].replace(" (Claude Code)", "") for r in rows})
    models = sorted({m for r in rows for m in r.get("models_used", [])})
    when = f"{min(r['judged_at'] for r in rows)[:16]} to {max(r['judged_at'] for r in rows)[:16]}".replace("T", " ")
    return f"| {task} | `{prompt}` | {fmt(len(rows))} | {when} | {', '.join(shas)} | {', '.join(cli)} | {', '.join(models)} |"


def s4() -> str:
    cal = json.loads((PAPER / "screening" / "decisions" / "calibration_stats.json").read_text(encoding="utf-8"))
    tiab = json.loads((PAPER / "screening" / "decisions" / "tiab_summary.json").read_text(encoding="utf-8"))
    pc = json.loads((PAPER / "fulltext" / "prisma_counts.json").read_text(encoding="utf-8"))
    cs = json.loads((PAPER / "extraction" / "decisions" / "correction_stats.json").read_text(encoding="utf-8"))
    qc = json.loads((PAPER / "extraction" / "decisions" / "quote_check.json").read_text(encoding="utf-8"))
    runs = [
        ("Title and abstract labels, pass 1", "screening/llm_screener_prompt.md", PAPER / "screening/llm/2026-10-16_opus.jsonl"),
        ("Title and abstract labels, pass 2", "screening/llm_screener_prompt.md", PAPER / "screening/llm/2026-10-16_sonnet.jsonl"),
        ("Full-text proposals", "fulltext/ft_prompt.md (tag ai-dependence-ft-prompt-v1.0)", PAPER / "fulltext/llm/ft_2026-10-16.jsonl"),
        ("Full-text proposals, citation searching", "fulltext/ft_prompt.md (same)", PAPER / "fulltext/llm/ft_chase_2026-10-17.jsonl"),
        ("Full-text proposal, late retrieval (D3)", "fulltext/ft_prompt.md (same)", PAPER / "fulltext/llm/ft_late_2026-10-17.jsonl"),
        ("Instruments of the included reports", "extraction/instr_prompt.md", PAPER / "extraction/llm/instr_2026-10-17.jsonl"),
        ("Instrument types (drafts)", "extraction/instrument_types.py (system prompt in the script)", PAPER / "extraction/llm/types_2026-10-17.jsonl"),
        ("Extraction and risk-of-bias drafts", "extraction/extract_prompt.md (tag ai-dependence-extraction-prompt-v1.0)",
         PAPER / "extraction/draft/extract_2026-10-17.jsonl"),
    ]
    a = cal["ai_rule_full_text_unless_both_exclude"]
    L = ["# Supplementary File S4. Use of an AI assistant", "",
         "Claude Opus 5.5 (`claude-opus-5-5`) and, for the second screening pass, Claude Sonnet 5.5 (`claude-sonnet-5-5`), "
         "both at reasoning effort high, ran through Claude Code in headless mode (`claude -p`) with a fixed system prompt, a "
         "JSON output schema and no tools; one item per call. Every output is stored with the hash of the system prompt and of "
         "the rendered prompt, the model actually used and the Claude Code version. Every label, proposal, type, extracted "
         "value and rating was a draft that the reviewer (R1) accepted or corrected.", "",
         "| Task | Prompt | Items | Run (UTC) | System prompt SHA-256 (first 16) | Claude Code | Models used |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    L += [run_row(*r) for r in runs if r[2].exists()]
    L += ["", "## Agreement with the reviewer", "",
          f"- Title and abstract, blind calibration sample (n = {cal['n_calibration']}, labels hidden from R1): the rule "
          f"\"full text unless both passes exclude\" had sensitivity {a['sensitivity']:.2f} (95% CI {a['sensitivity_ci'][0]:.2f}–"
          f"{a['sensitivity_ci'][1]:.2f}), specificity {a['specificity']:.2f} ({a['specificity_ci'][0]:.2f}–"
          f"{a['specificity_ci'][1]:.2f}), κ {a['kappa']:.2f}, Gwet's AC1 {a['ac1']:.2f}. It missed "
          f"{len(cal['rule_false_negatives'])} records R1 marked unsure and none marked include; the safeguard was triggered, "
          f"and R1 screened all double exclusions blind ({fmt(sum(tiab['by_stage']['re-screening (blind)'].values()))} records; "
          f"{fmt(tiab['by_stage']['re-screening (blind)'].get('unsure', 0) + tiab['by_stage']['re-screening (blind)'].get('include', 0))} "
          "returned to full text).",
          f"- Verification with labels shown: {fmt(tiab['verification']['records'])} records kept by at least one pass; R1 "
          f"accepted the AI label for {fmt(tiab['verification']['accepted_ai_label_with_equals'])} and excluded "
          f"{fmt(tiab['verification']['r1_excluded_although_a_pass_kept'])}.",
          f"- Full text: R1 accepted the AI proposal for {pc['ai_proposals']['r1_accepted_with_equals']} of "
          f"{pc['ai_proposals']['of']} reports; no report changed from eligible to not eligible or back.",
          f"- Extraction: R1 verified {fmt(cs['drafted_values'])} drafted values ({cs['verified_samples']} samples, "
          f"{cs['drafted_effects']} effects) and corrected {cs['values_corrected']} ({cs['key_values_corrected']} of "
          f"{fmt(cs['key_values'])} key values); effects added by R1: {cs['effects_added_by_R1']}.",
          f"- Supporting quotes found verbatim in the source by script: {qc['effects']['found_verbatim']} of "
          f"{qc['effects']['quotes_checked']} for effects and {qc['key_fields']['found_verbatim']} of "
          f"{qc['key_fields']['quotes_checked']} for key sample fields (`extraction/quote_check.py`)."]
    return "\n".join(L) + "\n"


def s5() -> str:
    recs = records()
    L = ["# Supplementary File S5. Reports excluded at full text", ""]
    for part, name in (("Database search", "ft_R1.csv"), ("Citation searching", "ft_R1_chase.csv")):
        ft = [r for r in csv.DictReader((PAPER / "fulltext" / "decisions" / name).open(encoding="utf-8-sig"))
              if r["decision"] == "not_eligible"]
        L += [f"## {part}", "", f"{len(ft)} reports, with the primary reason (PRISMA 2020).", "",
              "| Record | First author | Year | Title | DOI | Reason |", "| --- | --- | --- | --- | --- | --- |"]
        for r in sorted(ft, key=lambda x: (x["reason"], x["rec_id"])):
            u = recs.get(r["rec_id"], {})
            L.append(f"| {r['rec_id']} | {cell(u.get('first_author'))} | {u.get('year') or ''} | {cell(u.get('title'))} | "
                     f"{u.get('doi') or ''} | {REASON_TEXT.get(r['reason'], r['reason'])} |")
        L.append("")
    return "\n".join(L)


def s6() -> str:
    s = list(csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8")))
    e = list(csv.DictReader((PAPER / "forms" / "effects.csv").open(encoding="utf-8")))
    scales = defaultdict(set)
    for x in e:
        scales[x["sample_id"]].add(f"{x['exposure_family']} ({x['exposure_type']})")
    L = ["# Supplementary File S6. Included samples", "",
         f"{len({x['study_id'] for x in s})} studies, {len(s)} independent samples. NR, not reported.", "",
         "| Sample | Study (main report) | Country | Population | Sampling | n | Age, mean | % female | AI system | Scales (type) |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in s:
        L.append("| " + " | ".join(cell(c) for c in [
            x["sample_id"], f"{x['first_author']} {x['year']} ({x['report_ids'].split(';')[0]})", x["country"],
            x["population"], x["sampling"], x["n_analysed"], x["age_mean"], x["pct_female"], x["ai_system"],
            ", ".join(sorted(scales[x["sample_id"]])) or "no eligible effect"]) + " |")
    recs = records()
    reports = defaultdict(list)
    for x in s:
        for rid in x["report_ids"].split(";"):
            if rid and rid not in reports[x["study_id"]]:
                reports[x["study_id"]].append(rid)
    L += ["", "## Reports of the included studies", "",
          "Study code, then each report: first author (year). Title. Source. DOI or record identifier.", ""]
    for st in sorted(reports):
        refs = []
        for rid in reports[st]:
            u = recs.get(rid, {})
            title = cell(u.get("title")).rstrip(".")
            doi = f"https://doi.org/{u['doi']}" if u.get("doi") else rid
            refs.append(f"{AUTHOR_FIX.get(rid, u.get('first_author') or '')} ({u.get('year') or 'n.d.'}). {title}. "
                        f"*{cell(u.get('venue'))}*. {doi}")
        L.append(f"- **{st}.** " + " — ".join(refs))
    return "\n".join(L) + "\n"


def s7() -> str:
    e = list(csv.DictReader((PAPER / "forms" / "effects.csv").open(encoding="utf-8")))
    L = ["# Supplementary File S7. Extracted zero-order associations", "",
         f"{len(e)} effects. Stat: pearson, spearman, latent (measurement-model correlation), beta (single predictor). "
         "Value as printed; rev = higher correlate scores mean less of the construct (sign reversed in the analysis); "
         "lagged = measures from different occasions (D4); observed pair = a latent r whose observed r is also reported "
         "(the latent one is not used, D4).", "",
         "| Effect | Sample | Scale · part (type) | Correlate · instrument | Stat | Value | n | Flags | Location |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in e:
        flags = ", ".join(f for f, on in (("rev", x["reversed"] == "yes"), ("lagged", x["lagged"] == "yes"),
                                           ("observed pair", x["observed_pair_exists"] == "yes"),
                                           (f"wave {x['wave']}", x["wave"] not in ("1", "") and x["lagged"] != "yes")) if on)
        L.append("| " + " | ".join(cell(c) for c in [
            x["effect_id"], x["sample_id"], f"{x['exposure_family']} · {x['exposure_part']} ({x['exposure_type']})",
            f"{LABEL.get(x['correlate_construct'], x['correlate_construct'])} · {x['correlate_instrument']}",
            x["stat_type"].replace("beta_single_predictor", "beta"), x["value"], x["n"], flags, x["location"]]) + " |")
    return "\n".join(L) + "\n"


def s8() -> str:
    s = list(csv.DictReader((PAPER / "forms" / "samples.csv").open(encoding="utf-8")))
    ab = {"yes": "Y", "no": "N", "unclear": "U"}
    L = ["# Supplementary File S8. Risk of bias (six items adapted from AXIS)", "",
         "Items (`forms/rob.md`; Downes et al., 2016): 1 sampling (probability or census); 2 response; 3 validated "
         "AI-dependence measure; 4 reliability of that measure in the sample; 5 validated correlate measures; 6 data-quality "
         "checks. Y yes, N no, U unclear. The reason for each N and U is in `forms/samples.csv` (`rob_notes`).", "",
         "| Sample | Study | 1 | 2 | 3 | 4 | 5 | 6 |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for x in s:
        L.append("| " + " | ".join([x["sample_id"], cell(f"{x['first_author']} {x['year']}")] +
                                   [ab.get(x[f"rob_{i}"], x[f"rob_{i}"]) for i in range(1, 7)]) + " |")
    L += ["", "Samples rated yes / no / unclear: " + "; ".join(
        f"item {i}: {sum(x[f'rob_{i}'] == 'yes' for x in s)} / {sum(x[f'rob_{i}'] == 'no' for x in s)} / "
        f"{sum(x[f'rob_{i}'] == 'unclear' for x in s)}" for i in range(1, 7)) + "."]
    return "\n".join(L) + "\n"


def f2(x) -> str:
    try:
        return f"{float(x):.2f}".replace("-", "−")
    except (TypeError, ValueError):
        return "–"


def p3(x) -> str:
    try:
        p = float(x)
        return "< 0.001" if p < 0.001 else f"{p:.3f}"
    except (TypeError, ValueError):
        return "–"


def rows(name: str) -> list[dict]:
    return list(csv.DictReader((RES / name).open(encoding="utf-8")))


def s9() -> str:
    L = ["# Supplementary File S9. Additional analyses", "",
         "CHE model on Fisher's z with CR2 inference unless stated; r back-transformed. k, independent samples.", "",
         "## S9.1. Pooled r by type of AI-dependence scale (all correlates with k ≥ 3 in a type)", "",
         "| Correlate | Type | k | r (95% CI) | 95% PI |", "| --- | --- | --- | --- | --- |"]
    for r in rows("by_type.csv"):
        if r["r"] not in ("", "NA"):
            L.append(f"| {LABEL.get(r['analysis'], r['analysis'])} | {r['type']} | {r['k_samples']} | {f2(r['r'])} "
                     f"({f2(r['ci.lb'])} to {f2(r['ci.ub'])}) | {f2(r['pi.lb'])} to {f2(r['pi.ub'])} |")
    L += ["", "Post hoc contrast including T4 (D6): " + "; ".join(
        f"{LABEL.get(r['correlate'], r['correlate'])}: {r['r_by_type'].replace('-', '−')}, F({float(r['df_num']):.0f}, "
        f"{float(r['df_denom']):.1f}) = {float(r['F']):.2f}, p {p3(r['p'])}" for r in rows("posthoc_type_tests.csv")) + ".",
          "", "## S9.2. Moderators (primary correlates with k ≥ 10; HTZ Wald tests)", "",
          "| Correlate | Moderator | k | F | df (num, denom) | p | Levels or slope |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows("moderators.csv"):
        if r["F"] not in ("", "NA"):
            L.append(f"| {LABEL.get(r['correlate'], r['correlate'])} | {r['moderator']} | {r['k_samples']} | "
                     f"{float(r['F']):.2f} | {float(r['df_num']):.0f}, {float(r['df_denom']):.1f} | {p3(r['p'])} | {cell(r['note'])} |")
    L += ["", "Pooled r per level: `analysis/results/moderator_levels.csv`. Moderators with fewer than two levels of two or "
              "more samples were not tested (`moderators.csv`).", "",
          "## S9.3. Sensitivity analyses (primary correlates)", "",
          "| Correlate | Analysis | k | r (95% CI) |", "| --- | --- | --- | --- |"]
    for r in rows("sensitivity.csv"):
        est = f"{f2(r['r'])} ({f2(r['ci.lb'])} to {f2(r['ci.ub'])})" if r["r"] not in ("", "NA") else cell(r["note"])
        L.append(f"| {LABEL.get(r['correlate'], r['correlate'])} | {r['analysis']} | {r['k_samples']} | {est} |")
    loo = defaultdict(list)
    for r in rows("leave_one_study_out.csv"):
        if r["r"] not in ("", "NA"):
            loo[r["correlate"]].append(float(r["r"]))
    L += ["", "## S9.4. Leave one study out", "",
          "| Correlate | Studies left out | Range of pooled r |", "| --- | --- | --- |"]
    for c, v in loo.items():
        L.append(f"| {LABEL.get(c, c)} | {len(v)} | {f2(min(v))} to {f2(max(v))} |")
    L += ["", "## S9.5. Small-study effects (primary correlates with k ≥ 10)", "",
          "| Correlate | k | Egger-type slope (p) | PET r (p) | PET-PEESE r | Selection model r | LRT p |",
          "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rows("publication_bias.csv"):
        if r["egger_p"] not in ("", "NA"):
            L.append(f"| {LABEL.get(r['correlate'], r['correlate'])} | {r['k_samples']} | {f2(r['egger_slope'])} "
                     f"({p3(r['egger_p'])}) | {f2(r['pet_r'])} ({p3(r['pet_p'])}) | {f2(r['pet_peese_r'])} | "
                     f"{f2(r['selection_r'])} | {p3(r['selection_lrt_p'])} |")
    L += ["", "Egger-type test: standard error of z as a moderator in the CHE model, CR2 (Rodgers and Pustejovsky, 2021). "
              "PET-PEESE and the three-parameter selection model (one-sided cut-point p = 0.025; weightr) on one effect per "
              "sample (z averaged within sample). Funnel plots: Supplementary Figs. S8–S10."]
    return "\n".join(L) + "\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    for name, fn in [("S1_search.md", s1), ("S2_scales.md", s2), ("S3_deviations.md", s3), ("S4_ai.md", s4),
                     ("S5_excluded.md", s5), ("S6_samples.md", s6), ("S7_effects.md", s7), ("S8_rob.md", s8),
                     ("S9_analyses.md", s9)]:
        (OUT / name).write_text(fn(), encoding="utf-8", newline="\n")
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
