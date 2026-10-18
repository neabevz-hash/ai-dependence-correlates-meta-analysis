# Supplementary File S3. Changes and clarifications after registration

All changes after registration, dated and justified.

## D1. Registration venue and order (2026-10-16)

- **Planned (§2):** registration on OSF Registries before the final search.
- **Done:** OSF Registries was down for a scheduled cloud migration from 16 October 2026, 13:00 UTC, to 19 October 2026, 13:00 UTC (status.cos.io: "all services of the OSF platform will be inaccessible via both the website and API"). The frozen protocol and the registration package were deposited on Zenodo instead, before the final search: https://doi.org/10.5281/zenodo.23420672 (created 2026-10-16, 14:50:54 UTC). The two files on Zenodo match the package built from tag `ai-dependence-prereg-v1.0` byte for byte (md5 checked on 2026-10-16).
- **Then:** the final search starts after the Zenodo deposit. The OSF registration with the same files follows when OSF is back and links to the Zenodo record; its "Current review stage" field states what had been done by then.
- **Effect on the review:** none on the methods. The protocol was time-stamped before any search result of the final run or any screening was seen.

## D2. Citation searching: topic filter before full-text assessment (2026-10-17)

- **Planned (§9, §11b):** backward and forward citation searching of the included studies and of the reviews in §6, through OpenAlex; the protocol does not say how the new records are screened.
- **Done:** `search/citation_chase.py`, run `search/runs/2026-10-17-citations/`. Seeds: the 124 included reports and seven reviews (Dagnino et al., Fneich et al., Yan, An et al., He et al., Singh & Sharma, Romero-Martínez et al.); all 131 were found in OpenAlex.
  - Results: 3,003 cited works and 1,379 citing links; 3,523 works were not in the main record set.
  - Only the 33 whose title or abstract has the exposure concept (an AI term within 60 characters of a dependence term, as in the screening of the review) went on: records R6001–R6033, straight to full-text assessment with the frozen full-text prompt v1.0. R1 decides every report (`fulltext/decisions/ft_R1_11.md`). The other 3,490 are not screened further.
- **Why:** reference lists of the included studies are dominated by works on education, HCI, technology acceptance and mental health in general. A study that measures AI dependence names it in its title or abstract, which the filter requires. The same approach was used in the misophonia review (its deviations.md, 2026-10-15).
- **Effect on the review:** a study that measured AI dependence without naming it in its title or abstract and that the database search also missed would be lost; reported as a limitation.

## D3. A full text retrieved after the full-text decisions (2026-10-17)

- R0250 (MDPI; Unpaywall marked it open, the publisher site blocked the script) was found as HTML in PMC when the second retrieval pass ran again for the citation-search records. It is assessed like the others: AI proposal with prompt v1.0, R1 decides (`fulltext/decisions/ft_R1_12.md`). No change of method; the PRISMA counts are updated.

## D4. Rules added in the extraction pilot (2026-10-17)

- **Planned (§11c, codebook):** the extraction form is piloted on five studies; any rule added in the pilot is recorded here.
- **Pilot:** jobs R0204, R4336 (with R2687), R4677 (with R3792), R1489 and R2290; prompt draft, Claude Opus 5.5, `extraction/draft/pilot_2026-10-17.jsonl`. Five rules were added before the prompt was frozen (tag `ai-dependence-extraction-prompt-v1.0`):
  1. **Subscale names** are copied exactly from the instrument list of the job, so that each effect links to its type in `instruments.csv`.
  2. **AI system:** the quote names the AI system or tools the participants used.
  3. **Observed and latent correlation of one pair** (R2290 reports both, Table 8 and a Fornell–Larcker table): both are extracted. In the analysis each pair enters once per sample: the observed correlation; the latent one only when no observed correlation is reported. This keeps one row of the same data per pair; §15c sensitivity analysis 3 (excluding latent correlations) is unchanged.
  4. **Time-lagged designs** (R1489 measures AI dependence at T1, self-esteem at T2 and distress at T3, each once): the cross-occasion correlation is the only zero-order association of the pair. It is extracted with wave "lagged: T1-T3" only when no same-occasion correlation of the pair exists, enters the main analysis, and is dropped in an added sensitivity analysis (excluding time-lagged correlations).
  5. **Coefficients shown only in figures** (R4677: a heatmap without printed values) are not extracted; the draft names them.
- **Effect on the review:** rules 3 and 4 settle cases the protocol did not cover; rule 4 adds one sensitivity analysis.

## D5. n when the correlation table gives none (2026-10-18)

- **Planned (§13, codebook):** the n of each correlation is extracted.
- **Found:** two verified samples report no n for the correlation table: S063 (R2518; the table comes from the EFA sample, n = 307, or the CFA sample, n = 361) and S077 (R2823, three-wave panel; 551 at baseline, 533, 521 and 503 complete cases, missing data imputed).
- **Done:** the smallest n the report names is used (307 and 503): a larger sampling variance, so less weight. `analysis/results/n_fallback.csv` lists both.
- **Effect:** 12 effects that would otherwise be lost enter the analysis; the choice is conservative.

## D6. Post hoc type contrast including T4 (2026-10-18)

- **Planned (§15b):** type of dependence measure as the primary moderator, contrast T1 vs T2 vs T3 for each primary correlate with k ≥ 10 samples; T4 reported apart.
- **Found:** for every primary correlate fewer than two of T1–T3 have three or more samples: T2 and T3 scales are rarely paired with the primary correlates (anxiety T3 = 2; loneliness T3 = 2; social anxiety T2 = 2; all others 0–1). Most samples use mixed scales (T4: DAI, AICD), and T1 is the only pure type with k ≥ 3. The registered contrast is not estimable; `analysis/results/type_tests.csv` records it, `by_type.csv` gives the pooled r per type where k ≥ 3.
- **Added post hoc:** the same CHE contrast with T4 as a fourth level, for every correlate (primary or secondary) with k ≥ 10 samples and for types with k ≥ 3 (`analysis/results/posthoc_type_tests.csv`). Reported as post hoc and exploratory.
- **Effect:** the question of the protocol (do the three types differ?) is answered only as "not estimable with current evidence"; the evidence map shows the gap.

## D7. GRADE: starting level and thresholds (2026-10-18)

- **Planned (§17):** GRADE for each primary correlate, adapted for correlational evidence as in the misophonia review; the domains and their criteria in words (risk of bias: share of weight from samples rated "no" on items 1, 3 or 6; inconsistency: prediction interval crossing zero or spanning small and large associations; imprecision: CI including both r < .10 and r > .30; indirectness: few regions, mostly students; publication bias).
- **Set when rating, after the pooled results were known:**
  - Start: high certainty, as for prognostic-factor associations from observational studies (Foroutan et al., 2020, https://doi.org/10.1016/j.jclinepi.2019.12.023) and as in the misophonia review; one level down for each serious domain.
  - Risk of bias: more than half of the inverse-variance weight from samples rated "no" on item 1, 3 or 6.
  - Inconsistency: 95% prediction interval crossing zero.
  - Imprecision: 95% CI including both |r| < .10 and |r| > .30 (for a negative correlation, the CI of −r).
  - Indirectness: fewer than three regions, or more than 75% of samples of university students.
  - Publication bias: with k ≥ 10, Egger-type test (CHE, CR2) p < .10 or a selection-model likelihood-ratio test p < .10.
- Rules and inputs: `analysis/results/grade_inputs.csv`, `manuscript/make_tables.py` (Table 4).

## D8. Benchmark against Huang (2022) not done (2026-10-18)

- **Planned (§15b):** pooled r for depression, anxiety, stress and loneliness set beside the problematic social media use estimates of Huang (2022), https://doi.org/10.1177/0020764020978434, descriptively.
- **Not done:** the article is closed (Unpaywall and OpenAlex: no open copy, 2026-10-17/18) and the abstract gives no coefficients. Under the review's rule of open-access sources only, the numbers cannot be taken from the source; second-hand values are not used.
- **Effect:** none on the pooled results; the comparison is dropped from the Discussion.
