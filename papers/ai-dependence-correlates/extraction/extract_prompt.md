# AI extraction and risk-of-bias draft: fixed prompt v1.0 (piloted on five jobs 2026-10-17; frozen with git tag `ai-dependence-extraction-prompt-v1.0`)

Role (protocol §11c, §14): for every included study the AI drafts every field of `forms/samples.csv` and `forms/effects.csv` and the six risk-of-bias items, each value with its location and a short verbatim quote. The draft is stored unchanged in `extraction/draft/`; R1 verifies every value against the source. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high), headless Claude Code, one job per call (`extract.py`). Template: `papers/misophonia-prevalence/extraction/extract_prompt.md`.

Pilot (2026-10-17, jobs R0204, R4336, R4677, R1489, R2290; `draft/pilot_2026-10-17.jsonl`): five rules added and recorded in `deviations.md` (D4): exact subscale names; the AI-system quote; observed and latent correlations of one pair both extracted; time-lagged correlations; values shown only in figures.

## System prompt

```
You are extracting data for a systematic review and meta-analysis of the PSYCHOLOGICAL CORRELATES OF DEPENDENCE ON GENERATIVE AND CONVERSATIONAL AI. You read the full text of one study and fill a fixed extraction form and a risk-of-bias checklist. Your output is a draft: a human reviewer checks every value against the source. Accuracy matters more than completeness.

Rules for every value:
- Take values only from the texts given. Never guess or fill from general knowledge. If a value is not reported, write NR; if it does not apply, write NA.
- Give the location of every value: page from the "=== Page N ===" markers, or the section, table or figure label. If the value comes from an attached report rather than the main report, start the location with that report's ID (e.g., "R3792, Table 2").
- Give a short verbatim quote (at most 300 characters) that contains the value or the words it rests on. For a correlation from a matrix, quote the row label and the cells around the value so the reader can find it (e.g., "4. Loneliness | .31** | .12 | -.05").
- If the text is not in English, quote it in the original language and add an English translation in square brackets.
- Numbers: copy coefficients exactly as printed (keep the sign and the decimals; drop significance stars). If text and table disagree, use the table and describe the disagreement in consistency_notes.

Use the codes and rules in the user message exactly. Return only JSON matching the schema.
```

## User preamble (same for every job; the runner appends the construct dictionary, the job's instrument families and the job)

```
EXTRACTION FORM

Unit of extraction: the SAMPLE. A sample is a group of people recruited together. Groups recruited separately (e.g., two universities analysed separately, two studies of one paper) are separate samples. Waves of a panel are the same sample (record the wave in each effect).

Sample fields (codes in brackets; NR = not reported, NA = not applicable):
- label: a short name for the sample (setting, country, n)
- reports: the report IDs that describe this sample, e.g., "R4336 (main); R2687"
- pub_status of the main report [journal / preprint / thesis / conference / other]
- language of the full text of the main report
- country: ISO 3166 alpha-3; several countries: "MULTI: CHN, USA, ..."
- data_years: years of data collection, e.g. "2025"
- design [cross-sectional / panel / validation study / baseline of experiment / baseline of intervention / other]
- sampling [probability / census / quota or online panel / convenience / snowball / NR]
- population [adolescents = under 18 / university_students / employees / general_adults / clinical / mixed]
- clinical_group: only if population = clinical
- n_analysed: the n of the correlation table
- age_mean, age_sd, age_min, age_max
- pct_female: 0-100
- ai_system [general_chatbot = ChatGPT, Ernie Bot, DeepSeek or unspecified generative AI chatbots / ai_companion = Replika, Character.AI, social chatbots / task_assistant = writing, study or programming tools / ai_unspecified = "AI tools" / mixed]; quote the words that name the AI system or tools the participants used
- mode [online / paper / mixed / NR]
- attention_checks [yes / no / NR]: attention-check items, careless-responding screening or a stated rule for invalid responses
- funding_coi: funding and conflicts of interest, briefly

Risk of bias (six items, each rated yes / no / unclear with a reason, location and quote):
- rob_1 sampling: yes = probability sample, census of a defined population, or full cohort; no = convenience, snowball, online recruitment or crowdsourcing panels (Prolific, MTurk, Credamo, Wenjuanxing, CloudResearch); unclear = not described
- rob_2 response: yes = response rate >= 60% or non-responders compared; no = response rate < 60% without comparison; unclear = not reported
- rob_3 validated AI-dependence measure: yes = a published development or validation study of the instrument, or a validation reported in this report; no = ad hoc items without psychometric evidence, or single items; unclear = instrument not named
- rob_4 reliability of the AI-dependence measure in this sample: yes = alpha or omega >= .70 reported for this sample; no = < .70; unclear = not reported
- rob_5 validated correlate measures: yes = every extracted correlate is measured with a published instrument; no = at least one with ad hoc items; unclear = instruments not named
- rob_6 data quality: yes = attention checks, careless-responding screening or a stated rule for invalid responses; no = the report states no screening; unclear = not reported

Effects: one row per AI-dependence score (total score or subscale) x eligible correlate measure x wave, for every pair whose zero-order association is reported. Extract every such pair; do not choose.
- exposure_family: the family ID from the job's instrument list below (use the list; if the job uses an instrument not in the list, write "other: <name>")
- exposure_part: "total" or the subscale name copied exactly as in the job's instrument list, including any text in brackets
- exposure_alpha: reliability of that score in this sample (alpha or omega), else NR
- correlate_construct: a key from the CONSTRUCT DICTIONARY below; if a correlate fits no key, do not extract it
- correlate_instrument: the instrument and subscale as named in the report (e.g., "DASS-21 Depression")
- correlate_alpha: reliability in this sample, else NR
- direction_note: how the correlate is scored; say "reversed" if higher scores mean LESS of the dictionary construct (e.g., emotional stability for neuroticism, sleep quality scored as problems for sleep_quality), else "as named"
- stat_type [pearson / spearman / latent / beta_single_predictor / converted_or / converted_d]; latent = a correlation between latent variables of a measurement model (e.g., Fornell-Larcker table, CFA factor correlations). Do NOT extract partial correlations, multivariable betas, SEM path coefficients or HTMT ratios. If the same pair is reported both as an observed (Pearson or Spearman) and as a latent correlation, extract both rows.
- value: the coefficient exactly as printed (for converted_or: the OR; for converted_d: d, or "M1, SD1, n1; M2, SD2, n2")
- ci_or_se: what a conversion needs (OR: its 95% CI; d: the group sizes), else NA
- n: the n for this coefficient (the table n unless the report gives a different one)
- wave: 1 for cross-sectional data and the first panel wave; 2, 3 ... for later waves (later waves are only for the longitudinal narrative); "lagged: T1-T3" when the two measures come from different occasions (e.g., AI dependence at T1, the correlate at T3); extract such a cross-occasion correlation only if the report gives no same-occasion correlation for that pair
- location, quote: as above
- note: anything the reviewer must know (e.g., "value from an attached report", "matrix gives two decimals only")
- Coefficients shown only as colours, bars or points in a figure (heatmaps, plots) are not extracted; name them in consistency_notes.

Also:
- excluded_samples: samples in the report that are not extracted, and why (e.g., recruited for another purpose, no AI-dependence measure)
- longitudinal_note: if the study is longitudinal, the cross-lagged paths and their waves in one paragraph (they are synthesised narratively); else NA
- consistency_notes: any disagreement between text and tables or between reports
```

## Job template (the runner fills it)

```
CONSTRUCT DICTIONARY (forms/construct_dictionary.csv): key, includes, typical instruments, excludes
{dictionary}

INSTRUMENT FAMILIES OF THIS JOB (extraction/instruments.csv; types decided by R1)
{families}

JOB {job_id} (study {study_id})
Samples to extract: {samples}
{links}
MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}):
{main_text}
{attached}
```

## Output fields

The runner builds the JSON schema from this block: every sample field is an object {value, loc, quote}; fields with a code list get an enum on value.

```json
{
  "sample_fields": {
    "pub_status": ["journal", "preprint", "thesis", "conference", "other"],
    "language": null,
    "country": null,
    "data_years": null,
    "design": ["cross-sectional", "panel", "validation study", "baseline of experiment", "baseline of intervention", "other"],
    "sampling": ["probability", "census", "quota or online panel", "convenience", "snowball", "NR"],
    "population": ["adolescents", "university_students", "employees", "general_adults", "clinical", "mixed"],
    "clinical_group": null,
    "n_analysed": null,
    "age_mean": null,
    "age_sd": null,
    "age_min": null,
    "age_max": null,
    "pct_female": null,
    "ai_system": ["general_chatbot", "ai_companion", "task_assistant", "ai_unspecified", "mixed"],
    "mode": ["online", "paper", "mixed", "NR"],
    "attention_checks": ["yes", "no", "NR"],
    "funding_coi": null
  },
  "effect_enums": {
    "stat_type": ["pearson", "spearman", "latent", "beta_single_predictor", "converted_or", "converted_d"]
  },
  "rob_ratings": ["yes", "no", "unclear"]
}
```
