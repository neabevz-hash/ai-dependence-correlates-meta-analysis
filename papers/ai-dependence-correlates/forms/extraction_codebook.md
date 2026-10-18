# Data extraction codebook (draft for v1.0)

Three linked tables. `samples.csv` has one row per independent sample. `instruments.csv` has one row per AI-dependence instrument or subscale. `effects.csv` has one row per exposure measure × correlate measure × sample × wave. Unknown = `NR` (not reported); not applicable = `NA`. Template: `papers/misophonia-prevalence/forms/extraction_codebook.md`.

**Procedure (protocol §11c).**
- The AI assistant pre-fills every field from the full text and, for every value, gives the source location (page, table or figure) and a short verbatim quote. The draft is stored unchanged in `extraction/draft/<sample_id>.json`.
- R1 verifies every field against the source and accepts or corrects it. The verified values go to the three tables.
- Fields marked **[K]** are key fields: R1 always checks them against the source table, never accepts them from the draft unseen.
- Reported: the share of AI values R1 corrected (overall and [K]) and the share of AI quotes found verbatim in the source.
- The form is piloted on five studies before use. Any rule added in the pilot goes to `deviations.md` with a date.

## samples.csv

| Field | Rule |
| --- | --- |
| `sample_id` | `S###`; one per independent sample. A study with two separate samples (e.g., students in two countries analysed separately) gets two IDs |
| `study_id` | `ST###`; links samples and reports of one study |
| `report_ids` | `rec_id`s of all reports of this sample (article, preprint, thesis, scale paper), `;`-separated; the first one supplies the data |
| `first_author`, `year`, `doi` | of the main report |
| `pub_status` | journal / preprint / thesis / conference / other |
| `language` | language of the full text |
| `country` | ISO 3166 alpha-3; multi-country samples: `MULTI` + list in `notes` |
| `region` | mainland_China / other_East_Asia (Hong Kong, Macau, Taiwan, Japan, Korea, Mongolia) / South_Southeast_Asia / MENA_Turkiye / Europe / Americas / other; filled from country |
| `data_years` | years of data collection; `NR` if not stated |
| `design` | cross-sectional / panel (first wave used) / validation study / baseline of experiment / baseline of intervention / other |
| `sampling` **[K]** | probability / census / quota or online panel / convenience / snowball / NR |
| `population` **[K]** | adolescents (<18) / university_students / employees / general_adults / clinical / mixed |
| `clinical_group` | only if population = clinical: diagnosis |
| `n_analysed` **[K]** | the n of the correlation table; if effects use different n, per effect in `effects.csv` |
| `age_mean`, `age_sd`, `age_min`, `age_max` | years |
| `pct_female` | 0–100 |
| `ai_system` **[K]** | general_chatbot (ChatGPT, Ernie Bot, DeepSeek, unspecified GenAI chatbot) / ai_companion (Replika, Character.AI, social chatbots) / task_assistant (writing, study, programming tools) / ai_unspecified ("AI tools") / mixed |
| `mode` | online / paper / mixed |
| `attention_checks` | yes / no / NR |
| `funding_coi` | short text |
| `rob_1` … `rob_6` | yes / no / unclear (see `rob.md`), each with a quote in the draft |
| `notes` | |

## instruments.csv (coded once per instrument, before effect sizes are extracted)

| Field | Rule |
| --- | --- |
| `instrument_id` | `I##`; subscales get their own row: `I##a`, `I##b` |
| `name` | as named by the developers (e.g., Problematic ChatGPT Use Scale; LLM-D12 instrumental subscale) |
| `development_doi` | DOI of the development or validation paper; `adhoc` for study-specific items |
| `items_n`, `response_scale` | |
| `item_text_source` | where the items were read (paper, appendix, supplement); `NR` if no item text is available |
| `type` **[K]** | T1 addiction-type / T2 functional dependence / T3 emotional dependence / T4 mixed or unclear (protocol §13). Rule: T1 when the items operationalise behavioural-addiction components (salience, mood modification, tolerance, withdrawal, conflict, relapse or loss of control); T2 when they ask about relying on AI to perform tasks or to think, or difficulty working without it; T3 when they ask about emotional support, attachment-like bond or distress at separation from the AI. A total score whose items span more than one type is T4; so are ad hoc items without item text |
| `type_rationale` | one sentence citing two or three items |
| `adapted_from` | e.g., BSMAS, IAT, SAS-SV, none |

## effects.csv

| Field | Rule |
| --- | --- |
| `effect_id` | `E####` |
| `sample_id` | link |
| `wave` | 1 for cross-sectional data and the first panel wave; later waves only for the longitudinal narrative synthesis |
| `exposure_instrument_id` **[K]** | link to `instruments.csv`; total score or subscale |
| `exposure_alpha` | reliability in this sample (α or ω), else `NR` |
| `correlate_construct` **[K]** | key from `construct_dictionary.csv`; correlates outside the dictionary are not extracted |
| `correlate_instrument` **[K]** | instrument name and subscale |
| `correlate_alpha` | reliability in this sample, else `NR` |
| `direction_note` | how the correlate is scored; if higher scores mean less of the named construct (e.g., emotional stability for neuroticism, sleep quality scored as problems), state it: the sign is recoded in analysis so that higher = more of the named construct |
| `stat_type` **[K]** | pearson / spearman / latent (CFA or SEM measurement model, e.g. Fornell–Larcker table) / beta_single_predictor / converted_or / converted_d |
| `value` **[K]** | the statistic as printed (r, ρ, latent r, β, OR or d) |
| `ci_or_se` | if the conversion needs it (OR: CI; d: group sizes) |
| `n` **[K]** | n for this correlation |
| `location` | table or page |
| `notes` | |

## Extraction rules

- If the text and a table disagree, take the table and note it.
- Extract every eligible pair: all subscales and the total score of the exposure measure, all correlate measures in the dictionary, each with its own row. Overlapping rows are handled by the multilevel model (protocol §15b).
- HTMT ratios, partial correlations, multivariable β and path coefficients are not extracted.
- A correlation matrix in supplementary files or an open data set counts as reported; with open raw data, R1 may compute the zero-order r and codes `stat_type = pearson` with a note.
- Reports of the same sample (article and preprint, or a scale paper and a substantive paper) are linked; each correlation is taken once, from the most complete report.
- Any rule added during the five-study pilot goes to `deviations.md` with a date.
