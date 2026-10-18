# Psychological correlates of dependence on generative and conversational AI: data and code

This repository contains the records, decisions, extracted data and analysis code for

> Rekhert, M. (2026). *Psychological correlates of dependence on generative and conversational AI: A systematic review and meta-analysis* [Manuscript submitted for publication]. Preprint: https://doi.org/10.5281/zenodo.23449099

- Protocol (Zenodo, 16 October 2026, deposited before the final search): https://doi.org/10.5281/zenodo.23420672
- Archived release (Zenodo): https://doi.org/10.5281/zenodo.23448773
- Author: Martin Rekhert, Higher School of Psychology, Turan University, Almaty, Kazakhstan (ORCID [0009-0001-2402-2031](https://orcid.org/0009-0001-2402-2031))

## The review in brief

- **Question.** How strongly is dependence on generative and conversational AI associated with depression, anxiety, stress, loneliness, social anxiety, self-esteem and procrastination (and 23 secondary correlates), and does the association differ by type of dependence scale (T1 addiction-type, T2 functional, T3 emotional, T4 mixed)?
- **Search.** 16 October 2026: PubMed, Europe PMC, OpenAlex (also non-English phrases), Semantic Scholar, Crossref, DataCite, OpenAIRE, CORE and works citing seven instrument papers (OpenAlex), no language limits; 11,379 records, 5,056 screened. Citation searching of the included studies and seven reviews on 17 October 2026. Records hosted on OSF, unavailable during an OSF outage, were retrieved on 18 October 2026 (deviations D9).
- **Selection.** One reviewer (the author) decided every record kept by the AI and every full text. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5 through Claude Code 2.1.289, fixed prompts, no tools) labelled titles and abstracts; a blind calibration sample of 400 records triggered the pre-specified safeguard, and the reviewer then screened all double exclusions blind. The AI drafted full-text proposals, scale types and extraction forms; the reviewer verified every value.
- **Included.** 126 reports, 123 studies, 127 independent samples, 74,492 participants, 386 zero-order associations.
- **Analysis.** Correlated and hierarchical effects (CHE) models on Fisher's z with CR2 cluster-robust inference (`metafor`, `clubSandwich`), small-study tests (`weightr`), GRADE.
- **Main results.** Pooled r: depression 0.32, anxiety 0.37, stress 0.35, loneliness 0.28, social anxiety 0.36, procrastination 0.26, self-esteem −0.18; every 95% prediction interval crossed zero. The registered contrast of scale types T1–T3 was not estimable (T2 and T3 scales were rarely used with these correlates).

## Repository layout

All study files are under `papers/ai-dependence-correlates/`.

| Path | Contents |
| --- | --- |
| `protocol.md` | Protocol v1.0 (frozen 16 October 2026, git tag `ai-dependence-prereg-v1.0` in the working repository; deposited on Zenodo) |
| `deviations.md` | Every change and clarification after registration, dated (D1–D9; Supplementary File S3) |
| `search/` | Search, de-duplication, recall and citation-searching scripts; `runs/2026-10-16/`: search log with every query, raw exports (zip), unique records, screening list (CSV, RIS), recall on the seed set; `runs/2026-10-16-check/`: the check run; `runs/2026-10-17-citations/`: citation searching |
| `screening/` | AI screening prompt and runner, both AI passes with the prompt hash and SHA-256 of the label files, blind calibration, safeguard re-screening, verification worksheets and final decisions (`decisions/tiab_final.csv`) |
| `fulltext/` | Retrieval scripts and log (open access only), full-text prompt and AI proposals, the reviewer's worksheets and decisions (`decisions/ft_R1.csv`, `ft_R1_chase.csv`), PRISMA counts |
| `extraction/` | Study map (reports → studies), instrument families and the reviewer's type decisions (`instruments.csv`), extraction prompt and runner, AI drafts (`draft/`), the reviewer's verification worksheets (`verify/`) and verified values (`decisions/`), quote and correction audits, `finalize.py` |
| `forms/` | Extraction codebook, construct dictionary, risk-of-bias rules, and the analysis tables `samples.csv` and `effects.csv` |
| `analysis/` | `analysis.R` (all analyses), `prisma.R`, `figures.R`; `results/` and `figures/` as reported |
| `manuscript/` | Scripts for Tables 1–4 (`make_tables.py` → `tables.md`) and Supplementary Files S1–S9 (`make_supplement.py` → `supplement/`) |
| `harness/` | `llmaudit`: the Claude Code runner used for the AI drafts, agreement statistics (κ, AC1) |

Reviewer worksheets (`*.md` under `screening/`, `fulltext/decisions/`, `extraction/verify/`, `extraction/decisions/`) have instructions in Russian, the reviewer's working language; records, AI drafts and decisions are in English, and every decision is also in a CSV file.

Not included: full texts and PDFs of the reports and of the scale development papers (copyright), API keys.

## Reproducing the analysis

The analysis runs from the released files and needs no API access. Tested with Python 3.12 and R 4.6.1 (metafor, clubSandwich, weightr, dplyr, readr, tidyr, ggplot2, jsonlite).

```bash
# verified extraction -> analysis tables (forms/samples.csv, forms/effects.csv)
python papers/ai-dependence-correlates/extraction/finalize.py --run 2026-10-16 --draft extract_2026-10-17
# meta-analysis -> analysis/results/, analysis/figures/
Rscript papers/ai-dependence-correlates/analysis/analysis.R
Rscript papers/ai-dependence-correlates/analysis/prisma.R
Rscript papers/ai-dependence-correlates/analysis/figures.R
# Tables 1-4 and Supplementary Files S1-S9
python papers/ai-dependence-correlates/manuscript/make_tables.py
python papers/ai-dependence-correlates/manuscript/make_supplement.py
```

Run the commands from the repository root. The release was checked by running them in a clean copy: the analysis tables, all result files, Tables 1–4 and Supplementary Files S1–S9 came out identical (line endings aside).

Re-running the search, retrieval or the AI drafts needs network access and keys (`.env.example`): `OPENALEX_API_KEY` and `CORE_API_KEY` for the search, and `CLAUDE_CODE_OAUTH_TOKEN` (output of `claude setup-token`) for the Claude Code runs. Python packages for those steps: `httpx`, `lxml`, `pyyaml`, `jsonschema` (`pip install -e harness`).

## Licenses and citation

Code (`*.py`, `*.R`, `harness/`): MIT (`LICENSE`). Data and documents: CC BY 4.0 (`LICENSE-DATA.md`); bibliographic records, abstracts and quotations from the included reports remain with their copyright holders. Please cite the article and this repository (`CITATION.cff`).
