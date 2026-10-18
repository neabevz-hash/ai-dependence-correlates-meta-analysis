# Protocol: Psychological correlates of dependence on generative and conversational AI — a systematic review and three-level meta-analysis by type of dependence measure

**Version 1.0, frozen on 2026-10-16** (git tag `ai-dependence-prereg-v1.0`) before the final search and before any screening. Structured by PRISMA-P 2015 (Moher et al., 2015; Shamseer et al., 2015); item numbers in brackets. To be registered on OSF with the Generalized Systematic Review Registration form (van den Akker et al., 2023) and, if its form accepts association reviews, in PROSPERO (it lists more than twenty reviews on AI dependence). Template: `papers/misophonia-prevalence/protocol.md` v1.0. Every reference was verified by DOI via Crossref on 2026-10-16. Novelty check: `novelty/novelty.md`; journals: `journals/journals.md`.

---

## Administrative information

**[1] Title.** Psychological correlates of dependence on generative and conversational AI: a systematic review and three-level meta-analysis by type of dependence measure.

**[2] Registration.** Zenodo, deposited on 2026-10-16 at 14:50 UTC, before the final search, with the frozen protocol and the registration package (the same files as tag `ai-dependence-prereg-v1.0`; md5 checked): https://doi.org/10.5281/zenodo.23420672. OSF Registries was unavailable from 16 to 19 October 2026 (cloud infrastructure migration), so the Zenodo deposit time-stamps the protocol; the OSF registration with the Generalized Systematic Review Registration form follows and links to it (`deviations.md`). PROSPERO, if its form accepts the review. Adding these identifiers and this note is the only change made to this file after freezing.

**[3a] Author and contact.** Martin Rekhert, MA student in clinical psychology, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com.

**[3b] Contributions.** Single author (R1): conceptualisation, eligibility decisions at every stage, data extraction, risk-of-bias appraisal, interpretation, final manuscript. An AI assistant (Claude Opus 5.5, Anthropic, run through Claude Code; Claude Sonnet 5.5 as the second screening pass) is used as a tool for the tasks in §9–§11 and §15: search code, de-duplication, draft screening labels, draft full-text decisions, draft extraction and risk-of-bias ratings, instrument coding drafts, analysis code, translation and text drafts. It is disclosed in the Methods and in the AI declaration. Every AI output is a draft: R1 checks each AI label, extracted value and rating against the source and accepts or overrides it, so all final decisions are R1's.

**[4] Amendments.** Any change after registration is dated, justified and logged in `deviations.md`, and reported in the registration and in the paper.

**[5] Support.** No funding, no sponsor, no conflicts of interest.

---

## Introduction

**[6] Rationale.**

Since late 2022, generative and conversational AI (LLM chatbots such as ChatGPT, AI writing and study assistants, AI companions) has spread rapidly. A large correlational literature now measures "AI dependence", "AI addiction", "problematic ChatGPT use" or "emotional dependence on AI" and relates these scores to mental health. Records with an AI term and a dependence term in the title grew from 53 in 2024 to 187 in 2025 and more than 600 in the first nine months of 2026 (OpenAlex, `novelty/novelty.md`). At least 30 dedicated instruments exist, including a scale for dependence on AI in university students (Morales-García et al., 2024), the Problematic ChatGPT Use Scale (Yu et al., 2024), the Generative AI Dependency Scale (Goh et al., 2025), the AI Chatbot Dependence Scale (Zhang et al., 2025), the LLM Dependence Scale (Li et al., 2025) and the Conversational AI Dependence Scale (Li et al., 2026).

The construct is disputed. One reading treats problematic AI use as a new behavioural addiction, an internet-use disorder in the sense of the I-PACE model (Brand et al., 2016, 2019): predisposing vulnerabilities such as social anxiety and loneliness lead to compensatory use and loss of control. Another reading treats much of what is measured as functional reliance on a useful tool, not pathology, and warns against overpathologising everyday behaviour (Billieux et al., 2015; Ciudad-Fernández et al., 2025). The instruments mirror this split. Some adapt addiction components (salience, mood modification, tolerance, withdrawal, conflict, relapse; Griffiths, 2005). Others measure instrumental reliance on AI for tasks and thinking, and a third group measures emotional reliance and attachment to AI companions. Narrative reviews report that the three groups have different correlates (Dagnino et al., 2026; Yan, 2026), but no quantitative synthesis has tested it.

Existing syntheses are narrative or narrow. Scoping, integrative and narrative reviews list the correlates qualitatively (Dagnino et al., 2026, 37 studies; Fneich et al., 2026, 28; Yan, 2026; An et al., 2026; He et al., 2026). The one completed meta-analysis, a preprint, is limited to university students and pools dependence together with academic misuse such as plagiarism (Romero-Martínez et al., 2026, 53 studies). Several meta-analyses are registered and ongoing: correlates of problematic use and dependence (Zhou, 2026, OSF), factors of AI dependence in students (PROSPERO CRD420251245192), reliance and mental health (CRD420261529723), and single correlates — self-efficacy, digital literacy, academic performance, cognitive skills.

A pooled, measure-aware estimate of how AI dependence relates to depression, anxiety, loneliness, self-esteem and procrastination matters for clinicians, who increasingly see patients using AI for emotional support, for the debate on whether "AI addiction" is a disorder, and for choosing instruments in future research.

**[7] Objectives.**

Review question (PECO):
- **Population:** people of any age and in any setting.
- **Exposure:** a quantitative measure of dependence on, addiction to, problematic or compulsive use of, over-reliance on, or emotional dependence on generative or conversational AI.
- **Comparison:** not applicable (zero-order associations).
- **Outcomes:** psychological and mental-health correlates (§13).

Objectives:
1. **Primary.** Estimate the pooled zero-order correlation between AI dependence and each of seven primary correlates: depression, anxiety, stress, loneliness, social anxiety, self-esteem, procrastination.
2. Test whether these associations differ by type of dependence measure: addiction-type, functional (instrumental) dependence, emotional dependence (§13).
3. Estimate pooled correlations for secondary correlates with at least three independent samples.
4. Examine other sources of heterogeneity: population (adolescents, university students, adults), region, AI type (general chatbots vs AI companions), age, sex composition, design, publication status, year, risk of bias, and observed vs latent correlations.
5. Compare the size of the distress associations with those reported for problematic social media use (Huang, 2022), descriptively.

Expectations stated in advance, to be checked rather than tested: AI dependence correlates positively with depression, anxiety, stress, loneliness, social anxiety and procrastination and negatively with self-esteem; the distress associations are larger for addiction-type and emotional-dependence measures than for functional-dependence measures; most associations are small to moderate (r ≈ .10–.30; Gignac & Szodorai, 2016).

---

## Methods

### [8] Eligibility criteria

**Study designs.** Cross-sectional surveys; the first wave of longitudinal studies; baseline data of experimental or intervention studies; psychometric validation studies that report correlations with an eligible correlate; any other quantitative design reporting a zero-order association between an eligible exposure measure and an eligible correlate.

**Inclusion criteria.**
- I1. **Exposure measure.** A self-report (or informant-report) measure of dependence on, addiction to, problematic or compulsive use of, over-reliance on, or emotional dependence on an AI system. Multi-item scales, validated or ad hoc, are eligible. A single item is eligible only if it explicitly asks about dependence, addiction or inability to stop; single items are coded and tested in sensitivity analyses.
- I2. **AI system.** An interactive AI system that the user converses with or delegates tasks to: LLM chatbots (ChatGPT, Ernie Bot, DeepSeek, Gemini, Copilot and others), AI writing, study or programming assistants, conversational agents and voice assistants, AI companions (Replika, Character.AI and others), and "AI" in general when it is framed as interactive AI tools.
- I3. **Correlate.** At least one eligible correlate (§13) measured with a quantitative instrument.
- I4. **Statistic.** A zero-order association between the exposure and the correlate (§13, "Effect size"), or data from which one can be derived. Authors are not contacted (as in the misophonia review, decision of R1 on 2026-10-11).
- I5. Any language, any publication year, any publication status: journal article, preprint, thesis or dissertation, conference paper with sufficient data.

**Exclusion criteria.**
- E1. Exposure is only frequency, duration or intensity of AI use; trust in AI; acceptance or intention to use (TAM, UTAUT); attitudes; AI literacy; technostress; or fear of AI ("AI anxiety") used as the exposure.
- E2. Over-reliance measured only as behaviour in an experimental task (for example, agreement with wrong AI advice). This is a decision-making construct, not a self-reported pattern of use.
- E3. Embodied social robots; AI used to treat or detect addiction; AI as an analysis tool of the researchers.
- E4. Only partial correlations, multivariable regression coefficients or path coefficients, with no zero-order association available anywhere in the report or its supplementary files.
- E5. Reviews, editorials, commentaries, qualitative studies, case reports.
- E6. Duplicate reports of the same sample. Reports are linked, and the most complete one supplies the data.

### [9] Information sources

Turan University has no access to Scopus, Web of Science, PsycINFO, Embase or the Chinese databases CNKI and Wanfang. Coverage relies on open indexes, on non-English search terms and on citation searching, as in the misophonia review:

- **PubMed**; **Europe PMC** (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org, Authorea); **OpenAlex** (Crossref corpus, repositories, dissertations, non-English journals); **Semantic Scholar**; **Crossref** (posted content, conference papers, INPLASY); **DataCite** (theses, OSF, Zenodo, figshare, ScienceDB); **OpenAIRE Graph** and **CORE** (institutional repositories and theses); **SciELO** (Portuguese and Spanish).
- **Non-English terms** in OpenAlex: Chinese, Korean, Japanese, Turkish, Spanish, Portuguese, Russian, German (§10). Chinese-language journals are reached only as far as OpenAlex indexes them; the gap is reported as a limitation.
- **Instrument-citation search:** all records citing the development papers of the seven most-cited instruments (§10), through OpenAlex.
- **Backward and forward citation searching** of included studies and of the reviews listed in §6, through OpenAlex.
- **Google Scholar:** two queries, the first 200 results of each (Haddaway et al., 2015), retrieved by R1 with Publish or Perish because Google Scholar blocks automated access; only records new to the database set are screened.

The search is validated against an independent seed set: the 37 empirical studies included in the scoping review of Dagnino et al. (2026), which searched Web of Science and Scopus, listed with DOIs (verified via Crossref and DataCite on 2026-10-16) in `search/seed_set.csv`. Recall is reported for all 37 and for those that measured AI dependence quantitatively; misses are examined one by one.

### [10] Search strategy

The search uses the exposure concept only, without terms for the correlates: correlations often sit in tables of studies whose abstracts do not name the correlate. No date or language limits. Strings are reported per PRISMA-S (Rethlefsen et al., 2021); code: `search/search.py`, adapted from `novelty/fetch_sources.py`.

**Phrase set.** 21 AI terms × 25 dependence forms (525 phrases): AI terms — AI, artificial intelligence, ChatGPT, GenAI, generative AI, generative artificial intelligence, chatbot(s), AI chatbots, conversational agent(s), conversational AI, LLM(s), large language model(s), AI companion(s), AI tools, AI technology, Replika; forms — "X addiction", "X dependence", "X dependency", "dependence on X", "dependency on X", "addiction to X", "problematic X use", "problematic use of X", "excessive (use of) X", "compulsive (use of) X", "addictive (use of) X", "X use disorder", "problematic / excessive / compulsive / addictive X usage". The over-reliance forms ("overreliance on X", "over-reliance on X", "X overreliance", "X over-reliance", "X overuse", "overuse of X") are combined with a measurement filter (`AND (scale OR questionnaire OR survey OR inventory OR respondents OR self-report)`), because without it they bring in about 2,500 essays and decision-making experiments (pilot, `novelty/`).

**Companion query.** For AI friends and companions the dependence word is often not next to the AI word ("addiction to the app", "compulsive chat with a social chatbot"), so a Boolean query is added in every source that supports it: (AI friend(s) OR AI friendship OR AI companion(s) OR social chatbot(s) OR companion chatbot(s) OR Replika OR Character.AI OR Xiaoice OR AI girlfriend OR AI boyfriend) AND (addiction OR addicted OR addictive OR dependence OR dependency OR compulsive OR problematic). The "usage" forms and this query were added after the check run missed three of the seed studies (see the check run below).

| Source | Query form |
| --- | --- |
| OpenAlex | `title_and_abstract.search` with the phrase set, in chunks of 40 phrases (over-reliance chunks with the measurement filter as a second `title_and_abstract.search` filter) |
| PubMed | proximity pairs `"<AI term> <dependence term>"[tiab:~3]`: 15 AI terms × 10 dependence terms (addiction, dependence, dependency, addictive, problematic / compulsive / excessive use and usage), and 15 × 3 over-reliance terms with the measurement filter; the companion query in `[tiab]`. Quoted phrases are not used: PubMed silently drops phrases missing from its phrase index |
| Europe PMC | `TITLE_ABS:"…"` with the phrase set, in chunks of 40 phrases |
| Semantic Scholar | bulk search with the phrase set |
| Crossref | 18 `query.bibliographic` queries sorted by relevance, kept while title or abstract contains an AI term within 60 characters of a dependence term |
| DataCite | phrase set in `titles.title`, `descriptions.description`, `subjects.subject` |
| OpenAIRE, CORE | 24 core phrases ("AI dependence", "AI addiction", "problematic ChatGPT use", "chatbot dependence", "emotional dependence on AI" and others): OpenAIRE in five queries of up to five phrases (its API allows at most four OR operators), CORE one query per phrase. CORE matches phrases loosely, so records without the phrase in title or abstract are dropped, and a query stops at the first page of 100 with fewer than five matches |
| SciELO | `(dependencia OR dependência OR adicción OR adição OR "uso problemático") AND ("inteligencia artificial" OR "inteligência artificial" OR ChatGPT OR chatbot)` |
| OpenAlex, non-English | 26 terms: 人工智能依赖, AI依赖, 生成式人工智能依赖, ChatGPT依赖, 人工智能成瘾, AI成瘾, 聊天机器人依赖, 인공지능 의존, AI 의존, AI 중독, 생성형 AI 의존, AI依存, 生成AI依存, yapay zekâ bağımlılığı, ChatGPT bağımlılığı, dependencia de la inteligencia artificial, adicción a la inteligencia artificial, dependência de inteligência artificial, зависимость от искусственного интеллекта, KI-Abhängigkeit and others |
| Google Scholar | `"AI dependence" OR "AI addiction" OR "problematic ChatGPT use" correlation`; `"chatbot dependence" OR "dependence on AI" depression OR anxiety OR loneliness` |

**Instrument-citation search (OpenAlex `cites:`).** Records citing: the scale for dependence on AI in university students (Morales-García et al., 2024); Problematic ChatGPT Use Scale (Yu et al., 2024); Generative AI Dependency Scale (Goh et al., 2025); AI Chatbot Dependence Scale (Zhang et al., 2025); LLM Dependence Scale (Li et al., 2025); Conversational AI Dependence Scale for Chinese college students (Chen et al., 2025); AI dependence scale for Chinese undergraduates (Wu et al., 2026).

**Pilot (2026-10-16, novelty check; `novelty/raw/fetch_log.json`).** OpenAlex 5,287, Semantic Scholar 2,975, DataCite 1,962, Crossref 1,236, PubMed 473, Europe PMC 389, SHARE 105, non-English 69. About 7,600 unique records by DOI and title, about 7,000 on topic, 2,500 of them only through the over-reliance forms. With the measurement filter, about 5,000 records are expected to reach screening.

**Check run of the v1.0 code (2026-10-16; `search/runs/2026-10-16-check/`).**

| Source | Records |
| --- | --- |
| OpenAlex | 3,926 |
| Semantic Scholar | 2,112 |
| DataCite | 1,630 |
| Crossref | 1,166 |
| OpenAIRE | 1,000 |
| CORE | 444 |
| Instrument citations | 400 |
| PubMed | 346 |
| Europe PMC | 281 |
| OpenAlex, non-English | 69 |
| **Total** | **11,374** |

- After de-duplication: 5,258 unique records; 203 removed automatically as non-study records; **5,055 to screen**, 112 of them only through instrument citations and 318 only through pointer sources (DataCite, OpenAIRE, CORE).
- Recall on the seed set: first 32 of 37. Three misses used wording the phrase set lacked ("compulsive ChatGPT usage"; "addiction to the app" of an AI friendship app; "compulsive chat with a social chatbot"), so the "usage" forms and the companion query were added; after that, **35 of 37**. The two remaining misses have no quantitative dependence measure: a study of companionship use and well-being among Character.AI users, and a book chapter on "AI reliance" without an abstract.
- CORE matches phrases loosely and returned thousands of pages; queries now stop at the first page of 100 with fewer than five phrase matches.

The final search runs with the v1.0 code after registration and before screening; dates, counts and software versions go to `search_log.json`. Raw exports are archived with the data release.

### [11] Study records

**[11a] Data management.** As in the misophonia review: git repository with dated commits; de-duplication on DOI (version suffixes ignored), PMID and normalised title with years within ±1 (`search/dedup.py`); pointer sources (DataCite, OpenAIRE, CORE, Google Scholar) attached to the database record with the same title; records that every source types as a non-study record (peer-review reports, datasets, errata, paratext) removed automatically and reported as "removed by automation tools". Data and code are released on GitHub with a Zenodo DOI at submission.

**[11b] Selection process.**
- **Title and abstract: two AI passes, R1 decides every record that either pass keeps; double AI exclusions are audited by the blind calibration (decision of R1, 2026-10-16).**
  1. **Blind calibration.** Before seeing any AI label, R1 screens a random sample of 400 records (`random.Random(20261017).sample` over sorted record IDs). Labels: include / unsure / exclude with a reason code. R1 sees title, abstract, year, venue, record type, language and DOI link; no author names. Decisions are committed before any AI label is shown. A fixed sample of 400 instead of 10% keeps the calibration load comparable to the misophonia review with a three to four times larger record set.
  2. **AI draft, two passes.** Claude Opus 5.5 (`claude-opus-5-5`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`), both at effort high, label every record independently with the same frozen prompt (`screening/llm_screener_prompt.md`): include / unsure / exclude, a reason code and a one-sentence note, "unsure" whenever in doubt. SHA-256 hashes of both label files are committed before unblinding.
  3. **Verification.** R1 reviews, with the AI labels visible, every record that at least one pass labelled include or unsure, and accepts or overrides the labels. R1's decision is final; include and unsure go to full text. Records labelled exclude by both passes are excluded without further human review; their error rate is measured on the calibration sample (step 4). Their list, with both reason codes and notes, is part of the open data.
  4. **Safeguard.** If, in the calibration sample, a record that R1 labelled include or unsure was labelled exclude by both AI passes (a false negative of the AI rule), R1 screens all double-excluded records outside the calibration sample with the AI labels hidden, in random order; every record R1 then marks include or unsure goes to full text.
  - **Tool:** Markdown decision files from `screening/screen_md.py` (from the misophonia review, adapted to show both AI labels), codes `+`, `?`, `-1`…`-6`, `=` to accept the AI label.
  - **Reported:** κ and Gwet's AC1 (Gwet, 2008) between R1 (blind) and each AI pass and their union; sensitivity and specificity with Clopper–Pearson 95% CIs; overrides by direction; whether the safeguard was triggered; how many included studies the AI had labelled exclude.
  - **Rationale:** single-reviewer screening misses about 13% of eligible studies (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). With about 5,000 records, a human check of every AI exclusion would triple R1's load without changing who decides on inclusion: every record kept by either pass, and every full text, is decided by R1. Two independent AI passes lower the chance of a missed record, and the blind calibration measures the miss rate of the AI rule directly; the safeguard returns the double exclusions to R1 if the rule misses even one calibration record.
- **Full text.** Open-access versions only (Unpaywall, PMC, repositories, preprint servers). Non-English texts are machine-translated by the AI assistant (Jackson et al., 2019); R1 checks the numbers against the original tables. The AI drafts a proposal per report: eligible or not, the primary exclusion reason, and where the correlations are (table, page, quote). R1 checks each proposal and decides. Reports without an open full text are listed as "reports not retrieved".
- **Linking reports.** Reports of one sample are linked and the sample is counted once; overlap is judged from authors, sites, dates, sample sizes and ethics approval numbers.
- **AI prompts after screening.** Full-text, extraction, instrument-coding and risk-of-bias prompts are written before full-text screening, piloted on five studies, frozen with git tags and committed before use.

**[11c] Data collection process.**
- **Forms.** Three linked tables: `forms/samples.csv` (one row per independent sample), `forms/effects.csv` (one row per exposure measure × correlate measure × sample × wave), `forms/instruments.csv` (one row per AI-dependence instrument or subscale; §13). Codebook: `forms/extraction_codebook.md`. Piloted on five studies.
- **AI draft.** The AI assistant pre-fills every field with its source location (table, page or quote); the draft is stored unchanged.
- **Verification.** R1 verifies every value against the source; key items (n, r, exposure and correlate instruments, direction of scoring) are always checked against the source table. The share of AI values that R1 corrected is reported, as is the share of AI quotes found verbatim in the source (`quote_check.py`, misophonia).
- **Checks.** |r| ≤ 1; n consistent across tables; reverse-scored correlates recoded so that higher scores mean more of the named construct; retractions and expressions of concern checked through Crossref.

### [12] Data items

Per sample: report details; country; years of data collection; design; sampling method (probability, census, quota or online panel, convenience); population (adolescents under 18, university students, employees, general adults, clinical); n analysed; age (mean, SD); percentage female; AI system (general chatbot or GenAI, AI companion, task-specific assistant, unspecified AI); AI-dependence instrument, version, language, items, subscales, reliability in the sample; for each correlate: construct, instrument, reliability, direction of scoring; the statistic, its type (Pearson, Spearman, latent, converted) and source location; attention checks or careless-responding screening; funding and conflicts of interest.

### [13] Outcomes and prioritisation

**Effect size.** Zero-order correlation between the AI-dependence score and the correlate, analysed as Fisher's z (Borenstein et al., 2009).
- Pearson r: used as reported. Spearman ρ: used as r and coded.
- Standardised β from a regression with that single predictor: equal to r.
- Latent correlations from CFA or SEM measurement models (for example, Fornell–Larcker tables): used and coded as latent; HTMT ratios are not correlations and are not used.
- Group comparisons (dependent vs non-dependent, OR or d): converted to r (Borenstein et al., 2009) and coded as converted.
- Not used: partial correlations, multivariable β, path coefficients.
- Longitudinal studies: the first wave enters the main analysis; cross-lagged associations are synthesised narratively, and pooled if at least five panels report the same pair.

**Correlates.**

| Group | Correlates |
| --- | --- |
| **Primary** (pooled when k ≥ 3 independent samples; reported in a table in any case) | depression; anxiety (general or trait); stress (perceived or psychological, not academic stress); loneliness; social anxiety; self-esteem; procrastination (general or academic) |
| **Secondary** (pooled when k ≥ 3 independent samples) | psychological distress (composite); life satisfaction and well-being; general and academic self-efficacy; self-control; impulsivity; fear of missing out; problematic smartphone use; problematic internet use; problematic social media use; neuroticism and the other Big Five traits; attachment anxiety; attachment avoidance; boredom proneness; mindfulness; sleep quality; academic stress; escapism or coping motives; perceived social support; AI-related anxiety |
| **Out of scope** | AI-specific cognitions (trust, perceived usefulness, performance expectancy, AI literacy, attitudes), academic and cognitive outcomes (grades, critical thinking, creativity), frequency of use. Several of them are covered by registered reviews (§6) |

Construct assignment follows a dictionary of instrument names (`forms/construct_dictionary.csv`), fixed before extraction; the AI drafts the assignment and R1 decides.

**Type of dependence measure (primary moderator).** Coded at the instrument or subscale level by item content, not by scale name, in `forms/instruments.csv` before extraction. The AI drafts the type from the items in the development paper; R1 decides.

| Type | Item content | Examples |
| --- | --- | --- |
| T1 addiction-type | behavioural-addiction components: salience, mood modification, tolerance, withdrawal, conflict, relapse or loss of control (Griffiths, 2005) | Problematic ChatGPT Use Scale (Yu et al., 2024); Problematic Generative AI Use Scale (Besalti et al., 2026); adaptations of the Bergen scales |
| T2 functional dependence | reliance on AI to perform tasks or to think; difficulty working without AI | instrumental subscales of the LLM Dependence Scale (Li et al., 2025) and of CAID (Li et al., 2026); over-reliance scales |
| T3 emotional dependence | reliance on AI for emotional support, attachment-like bond, distress at separation | AIED Scale (Wei et al., 2026); emotional subscale of CAID |
| T4 mixed or unclear | total scores combining types; ad hoc items without item text | — |

The examples are provisional: every instrument, including these, is typed from its items before extraction. When a study reports subscale correlations, each subscale enters with its own type; total scores of multidimensional scales enter as T4 unless all items belong to one type.

**One estimate per sample in single-level analyses.** For sensitivity analyses that need independent effects: the estimate from the instrument the authors designate as primary; otherwise the total score; otherwise the median z.

### [14] Risk of bias in individual studies

Six items adapted from the AXIS tool for cross-sectional studies (Downes et al., 2016), rated yes / no / unclear (`forms/rob.md`):
1. sampling: probability, census or full cohort (yes) vs convenience or online recruitment (no);
2. response rate ≥ 60%, or non-response analysed;
3. the AI-dependence measure has a published validation (factor structure and reliability);
4. reliability of the AI-dependence measure in the sample ≥ .70 (α or ω);
5. the correlate measures are validated instruments;
6. attention checks or careless-responding screening reported.

The AI drafts each rating with a supporting quote; R1 verifies and decides. No summary score; items 1, 3 and 6 enter as moderators and sensitivity filters.

### [15] Data synthesis

**[15a] Narrative synthesis.** Study characteristics by population, region and AI type; an evidence map of instruments × measure types × correlates; longitudinal and cross-lagged findings described.

**[15b] Meta-analysis.**
- **Model.** For each correlate separately: correlated-and-hierarchical-effects (CHE) model on Fisher's z — random effects for samples and for estimates within samples, with an assumed within-sample correlation of 0.6 between estimates (Pustejovsky & Tipton, 2022) — and cluster-robust (CR2) standard errors and tests with small-sample corrections (Pustejovsky & Tipton, 2018). Estimation by REML in `metafor::rma.mv` (Viechtbauer, 2010) with `clubSandwich`. Studies with several independent samples are clustered by study. This handles several scales, subscales or waves per sample (Van den Noortgate et al., 2013; Cheung, 2014; Hedges et al., 2010).
- **Reported:** pooled r with 95% CI and 95% prediction interval (IntHout et al., 2016); variance components and I² at each level; number of studies, samples and estimates.
- **Minimum data:** at least three independent samples per correlate.
- **Primary moderator:** type of dependence measure (T1, T2, T3; T4 reported but not in the contrast), as a categorical moderator in the CHE model for each primary correlate with k ≥ 10 samples. Tested with the cluster-robust Wald test (HTZ).
- **Other moderators** (one at a time, each only when k ≥ 10): population; region (mainland China, other East Asia, South and Southeast Asia, Middle East and North Africa including Türkiye, Europe, Americas, other); AI type; mean age; percentage female; design (cross-sectional vs first wave of a panel); publication status; year; risk-of-bias items 1, 3 and 6; latent vs observed correlation; converted vs reported statistic.
- **Benchmark (descriptive):** pooled r for depression, anxiety, stress and loneliness set beside the problematic social media use estimates of Huang (2022), with CIs; no formal test.

**[15c] Sensitivity analyses** (on the primary correlates):
1. excluding single-item and ad hoc measures;
2. excluding converted statistics;
3. excluding latent correlations;
4. only peer-reviewed reports;
5. within-sample correlation 0.3 and 0.8 instead of 0.6;
6. one estimate per sample with a standard random-effects model (REML, Hartung–Knapp);
7. correlations corrected for unreliability of both measures (Hunter–Schmidt; sample α where reported, otherwise the mean α of that instrument);
8. leave-one-study-out and influence diagnostics.

**[15d] If pooling is not appropriate** (fewer than three samples), estimates are tabulated and shown in forest plots without a pooled value.

**Software.** R 4.6.1 with metafor, clubSandwich and weightr; versions in `analysis/sessionInfo.txt`. Python 3.12 for search, de-duplication, decision files and the AI runner; Claude Code (headless) for AI drafts, with the version stored with every output. Windows 11.

### [16] Meta-biases

- Funnel plots per primary correlate.
- Egger-type test in the multilevel model: the standard error of z as a moderator in the CHE model with CR2 inference (Rodgers & Pustejovsky, 2021).
- On one estimate per sample: PET-PEESE (Stanley & Doucouliagos, 2014) and a three-parameter step-function selection model (Vevea & Hedges, 1995).
- Peer-reviewed vs grey literature compared as a moderator.
- Selective reporting: correlates named in the methods but missing from the correlation table are recorded.

### [17] Confidence in cumulative evidence

GRADE for each primary correlate, adapted for correlational evidence as in the misophonia review. Downgrading for risk of bias (share of weight from samples with "no" on items 1, 3 or 6), inconsistency (prediction interval crossing zero or spanning both small and large associations), imprecision (CI including both r < .10 and r > .30), indirectness (populations from few regions; mostly students) and publication bias. Summary-of-findings table.

---

## Load for the human reviewer (fixed in advance; one round)

Based on the check run of 2026-10-16 (5,055 records to screen); the final numbers are reported in the PRISMA flow diagram.

| Stage | Who | Approximate volume |
| --- | --- | --- |
| Title and abstract, blind calibration | R1 | 400 records |
| Title and abstract, verification | R1 | about 1,500–2,000 records that at least one AI pass kept (of about 5,000). The 3,000–3,500 double AI exclusions are not reviewed unless the safeguard triggers; then they are screened blind |
| Instrument types | R1 verifies an AI draft | about 40–60 instruments, once each |
| Full-text screening | R1 verifies an AI proposal | about 800–1,200 reports, each with the location of the correlations |
| Data extraction | R1 verifies an AI draft | about 150–300 studies; per study about 15 sample fields and 3–15 correlations, each with its source location |
| Risk of bias | R1 verifies an AI draft | 6 items per included study, each with a quote |

No further human coding rounds are planned. There is no second human reviewer, and double AI exclusions at the title-and-abstract stage are not reviewed by a human unless the safeguard triggers; these are limitations, partly offset by two independent AI passes, the blind calibration sample with a reported miss rate, R1's decision on every record kept and every full text, and verification of every extracted value.

---

## Changes from draft v0.1 (2026-10-16)

- Title-and-abstract scheme (§11b): R1 decides every record that either AI pass keeps; double AI exclusions are not reviewed by a human unless the blind calibration finds a miss (decision of R1, 2026-10-16). The load table was updated accordingly.
- Seed set (§9): the 37 empirical studies of Dagnino et al. (2026), DOIs verified; recall reported for all of them and for those that measured AI dependence quantitatively.
- Search code (`search/search.py`), de-duplication and recall scripts (`search/dedup.py`, `search/recall.py`, copied from the misophonia review), screener prompt with two passes (`screening/llm_screener_prompt.md`, `llm_screen.py`), calibration sampling (`screening/calibration.py`), extraction codebook, construct dictionary and risk-of-bias rules (`forms/`) written; check run of the search on 2026-10-16 (`search/runs/2026-10-16-check/`).
- Crossref is queried with `offset` and `sort=score`, because with a cursor it does not sort by relevance.
- After the check run: "usage" forms added to the phrase set (525 phrases instead of 441) and a Boolean companion query added (§10), because three seed studies were missed without them; recall 35 of 37.
- CORE: early stop at the first page of 100 with fewer than five phrase matches (the check run returned thousands of pages of loose matches).

---

## References

- An, C., Lu, K., & Yang, J. (2026). The dependency trap: A systematic review of the contributing factors and consequences of student over-reliance on generative AI in higher education. *Humanities and Social Sciences Communications, 13*(1), 1604. https://doi.org/10.1057/s41599-026-08959-2
- Besalti, M., Akdeniz Kudubeş, A., Kudubeş, İ. E., Özbay, Ö., Durmuş Sarıkahya, S., & Çınar Özbay, S. (2026). Development and psychometric evaluation of the Problematic Generative Artificial Intelligence Use Scale among Turkish university students. *International Journal of Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2026.2652063
- Billieux, J., Schimmenti, A., Khazaal, Y., Maurage, P., & Heeren, A. (2015). Are we overpathologizing everyday life? A tenable blueprint for behavioral addiction research. *Journal of Behavioral Addictions, 4*(3), 119–123. https://doi.org/10.1556/2006.4.2015.009
- Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley. https://doi.org/10.1002/9780470743386
- Brand, M., Wegmann, E., Stark, R., Müller, A., Wölfling, K., Robbins, T. W., & Potenza, M. N. (2019). The Interaction of Person-Affect-Cognition-Execution (I-PACE) model for addictive behaviors: Update, generalization to addictive behaviors beyond internet-use disorders, and specification of the process character of addictive behaviors. *Neuroscience & Biobehavioral Reviews, 104*, 1–10. https://doi.org/10.1016/j.neubiorev.2019.06.032
- Brand, M., Young, K. S., Laier, C., Wölfling, K., & Potenza, M. N. (2016). Integrating psychological and neurobiological considerations regarding the development and maintenance of specific Internet-use disorders: An Interaction of Person-Affect-Cognition-Execution (I-PACE) model. *Neuroscience & Biobehavioral Reviews, 71*, 252–266. https://doi.org/10.1016/j.neubiorev.2016.08.033
- Chen, Y., Wang, M., Yuan, S., & Zhao, Y. (2025). Development and validation of the conversational AI dependence scale for Chinese college students. *Frontiers in Psychology, 16*, 1621540. https://doi.org/10.3389/fpsyg.2025.1621540
- Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229. https://doi.org/10.1037/a0032968
- Ciudad-Fernández, V., von Hammerstein, C., & Billieux, J. (2025). People are not becoming "AIholic": Questioning the "ChatGPT addiction" construct. *Addictive Behaviors, 166*, 108325. https://doi.org/10.1016/j.addbeh.2025.108325
- Dagnino, F. M., Fante, C., Guerrieri, V., & Passarelli, M. (2026). Addicted, attached, or just delegating? A scoping review on "problematic artificial intelligence use". *Frontiers in Psychology, 17*, 1900953. https://doi.org/10.3389/fpsyg.2026.1900953
- Downes, M. J., Brennan, M. L., Williams, H. C., & Dean, R. S. (2016). Development of a critical appraisal tool to assess the quality of cross-sectional studies (AXIS). *BMJ Open, 6*(12), e011458. https://doi.org/10.1136/bmjopen-2016-011458
- Fneich, B., Ahadi, N., Ali, J., & Alkadhimi, F. (2026). Psychological outcomes and correlates associated with over-reliance on artificial intelligence tools: An integrative review. *International Journal of Mental Health and Addiction*. Advance online publication. https://doi.org/10.1007/s11469-026-01724-1
- Gignac, G. E., & Szodorai, E. T. (2016). Effect size guidelines for individual differences researchers. *Personality and Individual Differences, 102*, 74–78. https://doi.org/10.1016/j.paid.2016.06.069
- Goh, A. Y., Hartanto, A., & Majeed, N. M. (2025). Generative artificial intelligence dependency: Scale development, validation, and its motivational, behavioral, and psychological correlates. *Computers in Human Behavior Reports, 20*, 100845. https://doi.org/10.1016/j.chbr.2025.100845
- Griffiths, M. (2005). A 'components' model of addiction within a biopsychosocial framework. *Journal of Substance Use, 10*(4), 191–197. https://doi.org/10.1080/14659890500114359
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology, 61*(1), 29–48. https://doi.org/10.1348/000711006X126600
- Haddaway, N. R., Collins, A. M., Coughlin, D., & Kirk, S. (2015). The role of Google Scholar in evidence reviews and its applicability to grey literature searching. *PLOS ONE, 10*(9), e0138237. https://doi.org/10.1371/journal.pone.0138237
- He, X., Li, S., Cha, R., Wang, L., Shen, Y., Wu, R., Wu, L., Gong, X., & Liu, J. (2026). Artificial intelligence dependency in college students: A critical narrative review. *Frontiers in Psychology, 17*, 1808268. https://doi.org/10.3389/fpsyg.2026.1808268
- Hedges, L. V., Tipton, E., & Johnson, M. C. (2010). Robust variance estimation in meta-regression with dependent effect size estimates. *Research Synthesis Methods, 1*(1), 39–65. https://doi.org/10.1002/jrsm.5
- Huang, C. (2022). A meta-analysis of the problematic social media use and mental health. *International Journal of Social Psychiatry, 68*(1), 12–33. https://doi.org/10.1177/0020764020978434
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), e010247. https://doi.org/10.1136/bmjopen-2015-010247
- Jackson, J. L., Kuriyama, A., Anton, A., Choi, A., Fournier, J.-P., Geier, A.-K., et al. (2019). The accuracy of Google Translate for abstracting data from non–English-language trials for systematic reviews. *Annals of Internal Medicine, 171*(9), 677–679. https://doi.org/10.7326/M19-0891
- Li, L., Wang, T., Wang, Y., Wang, Y., & Zeng, X. (2026). Development and validation of the Conversational AI Dependence Scale (CAID): A dual-dimensional measure of instrumental and emotional dependence. *International Journal of Human–Computer Interaction, 42*(18), 15359–15379. https://doi.org/10.1080/10447318.2026.2618563
- Li, Z., Zhang, Z., Wang, M., & Wu, Q. (2025). From assistance to reliance: Development and validation of the large language model dependence scale. *International Journal of Information Management, 83*, 102888. https://doi.org/10.1016/j.ijinfomgt.2025.102888
- Moher, D., Shamseer, L., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews, 4*, 1. https://doi.org/10.1186/2046-4053-4-1
- Morales-García, W. C., Sairitupa-Sanchez, L. Z., Morales-García, S. B., & Morales-García, M. (2024). Development and validation of a scale for dependence on artificial intelligence in university students. *Frontiers in Education, 9*, 1323898. https://doi.org/10.3389/feduc.2024.1323898
- Oami, T., Okada, Y., & Nakada, T. (2024). Performance of a large language model in screening citations. *JAMA Network Open, 7*(7), e2420496. https://doi.org/10.1001/jamanetworkopen.2024.20496
- Pustejovsky, J. E., & Tipton, E. (2018). Small-sample methods for cluster-robust variance estimation and hypothesis testing in fixed effects models. *Journal of Business & Economic Statistics, 36*(4), 672–683. https://doi.org/10.1080/07350015.2016.1247004
- Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with robust variance estimation: Expanding the range of working models. *Prevention Science, 23*(3), 425–438. https://doi.org/10.1007/s11121-021-01246-3
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z
- Rodgers, M. A., & Pustejovsky, J. E. (2021). Evaluating meta-analytic methods to detect selective reporting in the presence of dependent effect sizes. *Psychological Methods, 26*(2), 141–160. https://doi.org/10.1037/met0000300
- Romero-Martínez, Á., et al. (2026). *Unveiling the dark side of the force: Factors underlying the misuse and dependence of generative artificial intelligence in higher education* [Preprint]. Research Square. https://doi.org/10.21203/rs.3.rs-10599376/v1
- Shamseer, L., Moher, D., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: Elaboration and explanation. *BMJ, 349*, g7647. https://doi.org/10.1136/bmj.g7647
- Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression approximations to reduce publication selection bias. *Research Synthesis Methods, 5*(1), 60–78. https://doi.org/10.1002/jrsm.1095
- van den Akker, O. R., Peters, G.-J. Y., Bakker, C. J., Carlsson, R., Coles, N. A., Corker, K. S., Feldman, G., Moreau, D., Nordström, T., Pickering, J. S., Riegelman, A., Topor, M. K., van Veggel, N., Yeung, S. K., Call, M., Mellor, D. T., & Pfeiffer, N. (2023). Increasing the transparency of systematic reviews: Presenting a generalized registration form. *Systematic Reviews, 12*, 170. https://doi.org/10.1186/s13643-023-02281-7
- Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594. https://doi.org/10.3758/s13428-012-0261-6
- Vevea, J. L., & Hedges, L. V. (1995). A general linear model for estimating effect size in the presence of publication bias. *Psychometrika, 60*(3), 419–435. https://doi.org/10.1007/BF02294384
- Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software, 36*(3), 1–48. https://doi.org/10.18637/jss.v036.i03
- Waffenschmidt, S., Knelangen, M., Sieben, W., Bühn, S., & Pieper, D. (2019). Single screening versus conventional double screening for study selection in systematic reviews: A methodological systematic review. *BMC Medical Research Methodology, 19*, 132. https://doi.org/10.1186/s12874-019-0782-0
- Wei, X., Liu, D., & Cheung, H. N. (2026). *Emotional dependence on AI chatbots: Development and validation of the AIED Scale* [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/yhetz_v1
- Wu, H., Ni, H., Luo, W., & Wu, T. (2026). Development and validation of the AI dependence scale for Chinese undergraduates and a preliminary exploration. *Frontiers in Psychology, 16*, 1725393. https://doi.org/10.3389/fpsyg.2025.1725393
- Yan, D. (2026). A critical narrative synthesis of psychological correlates, measurement, and reported findings on conversational AI engagement and dependence-related constructs. *Frontiers in Psychology, 17*, 1827795. https://doi.org/10.3389/fpsyg.2026.1827795
- Yu, S.-C., Chen, H.-R., & Yang, Y.-W. (2024). Development and validation the Problematic ChatGPT Use Scale: A preliminary report. *Current Psychology, 43*(31), 26080–26092. https://doi.org/10.1007/s12144-024-06259-z
- Zhang, X., Yin, M., Zhang, M., Li, Z., & Li, H. (2025). The development and validation of an artificial intelligence chatbot dependence scale. *Cyberpsychology, Behavior, and Social Networking, 28*(2), 126–131. https://doi.org/10.1089/cyber.2024.0240
- Zhou, S. (2026). *Behavioral addiction or functional reliance? A three-level meta-analysis and meta-analytic structural equation modeling of the correlates of problematic use of and dependence on generative and conversational AI* [Registration]. OSF Registries. https://doi.org/10.17605/osf.io/78bke
- Registrations cited: PROSPERO CRD420251245192, CRD420261529723 (https://www.crd.york.ac.uk/PROSPERO/view/<number>).
