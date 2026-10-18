# Проверка выписывания — файл 9 из 13

Черновик заполнил ИИ (Claude Opus 5.5) по полному тексту; у каждого значения указано место и цитата. Проверяете вы, один проход.

**Как проверять выборку:**
1. Откройте полный текст по ссылке у исследования.
2. **Ключевые числа** — сверить с таблицей корреляций статьи всегда: в таблице эффектов шкала ИИ и её часть, коррелят, r, n, тип статистики; под таблицей n_analysed, population, sampling, ai_system.
3. Остальные поля и пункты риска смещения: проверить, что значение есть в цитате и место указано верно.
4. Неверное — исправьте строкой в блоке «Правки» этой выборки (по одной правке на строку):
   - `n_analysed = 412`, `sampling = convenience` — поле выборки;
   - `E3.value = -.21`, `E3.correlate_construct = stress`, `E3.n = 398` — поле эффекта E3;
   - `E3 удалить` — убрать эффект (например, частная корреляция или коррелят не из словаря);
   - `+ эффект: exposure_family=DAI; exposure_part=total; correlate_construct=loneliness; correlate_instrument=UCLA-3; stat_type=pearson; value=.24; n=412; wave=1; location=Table 2` — добавить пропущенный эффект;
   - `rob_3 = no` — пункт риска смещения;
   - `выборка удалить: причина` — если это не отдельная выборка или её нельзя брать;
   - после `#` — комментарий для Claude.
5. Когда выборка проверена, напишите `да` после «Проверено:».

**Подсказки в файле:** «⚠ Проверка скриптом» — места, где скрипт нашёл повод присмотреться: r вне [−1; 1]; n эффекта не равно n выборки; коррелят со шкалой «наоборот» (знак перевернём в анализе); часть шкалы не из списка семейства; число не встретилось в независимом проходе ИИ по полному тексту (на этапе решений о включении) или наоборот — там было, а здесь нет. «Расхождения в тексте» — ошибки самих авторов, которые нашёл ИИ; в этом случае ИИ берёт числа из таблицы.

**Тип статистики:** pearson, spearman; latent — корреляция латентных переменных (таблица Форнелла — Ларкера, корреляции факторов); beta_single_predictor — β регрессии с одним предиктором; converted_or / converted_d — сравнение групп, переведём в r. Частные корреляции, β с несколькими предикторами, пути SEM и HTMT не выписываем.
**Конструкты коррелятов** (`forms/construct_dictionary.csv`): первичные — depression, anxiety, stress, loneliness, social_anxiety, self_esteem, procrastination; остальные вторичные. **Тип шкалы ИИ** в таблице — ваше решение по `instrument_types_R1.md`, для справки.
**population:** adolescents, university_students, employees, general_adults, clinical, mixed. **sampling:** probability, census, quota or online panel, convenience, snowball, NR. **ai_system:** general_chatbot, ai_companion, task_assistant, ai_unspecified, mixed.

---

## ST081 · Zhang 2026 · Frontiers in public health

Основной отчёт R2887: [текст](../../fulltext/text/R2887.txt) — «Problematic generative AI use and mental health risks among Chinese university students: latent profiles, network structure, and health literacy as a modifiabl…» — [DOI](https://doi.org/10.3389/fpubh.2026.1910408)
Расхождения в тексте: Text and Table 2 agree (PGU with academic anxiety r = 0.43, sleep problems 0.36, distress 0.46; health literacy -0.31). The exclusion counts (96+54+68+50 = 268) and the retained n (1872/2140 = 87.5%) are internally consistent. Table 2 gives coefficients to two decimals. The network figure (Fig. 3, EBICglasso partial correlations among item/subdimension nodes) and the centrality plots (Fig. 4) are figure-only and/or partial associations, so they were not extracted. Correlations for the PGU subdimensions (loss of control, compulsive use, academic avoidance) are not reported; only profile means appear (Table 4). The CFA/CR/AVE details are in Supplementary Table S3, which was not available.
Заметка ИИ: One sample and three zero-order effects for the PGU total score. Self-regulated learning, health literacy and academic engagement correlations exist but were not extracted because they fit no dictionary key; the reviewer may reconsider self-regulated learning under self_control.

### ST081-1 · Six Chinese universities (eastern, central, western China), undergraduates, n=1872
Отчёты: R2887 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2887_1 · total (T4) | **academic_stress** · Academic anxiety (5 adapted items) | pearson | **0.43** | **1872** | 1 | Table 2 | «2. Academic anxiety / 3.02 / 0.86 / 0.90 / 0.43*** / –» |
| E2 | ADHOC_R2887_1 · total (T4) | **sleep_quality** · Sleep problems (PSQI-type score) | pearson | **0.36** | **1872** | 1 | Table 2 | «3. Sleep problems / 6.17 / 2.83 / 0.81 / 0.36*** / 0.41*** / –» |
| E3 | ADHOC_R2887_1 · total (T4) | **distress** · Psychological distress (6 study items) | pearson | **0.46** | **1872** | 1 | Table 2 | «4. Psychological distress / 2.56 / 0.76 / 0.88 / 0.46*** / 0.55*** / 0.44*** / –» |

- E1: α ИИ 0.91, α коррелята 0.90; заметка: Academic (performance-related) anxiety coded as academic_stress per dictionary (anxiety key excludes academic anxiety). Ad hoc items.
- E2: **направление: reversed (higher scores = poorer sleep quality / more sleep problems)**; α ИИ 0.91, α коррелята 0.81; заметка: PSQI-type approach that also includes delayed bedtime related to digital-device or GenAI use; not the standard PSQI.
- E3: α ИИ 0.91, α коррелята 0.88; заметка: Items cover emotional exhaustion, mental overload, irritability, reduced motivation and inability to cope with academic demands (partly burnout-like content). Ad hoc items.

**⚠ Проверка скриптом (обратите внимание):**
- E2: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление

**Ключевые поля выборки:**
- **n_analysed: 1872** — Methods, Procedure and data quality control; Table 1 — «The final analytic sample comprised 1,872 valid responses.»
- **population: university_students** — Methods, Study design and participants — «Eligible participants were full-time undergraduate students aged 18 years or older who had used at least one GenAI tool»
- **sampling: convenience** — Methods, Study design and participants — «A convenience sampling strategy was used, with efforts to include students from different grades and disciplinary backgrounds.»
- **ai_system: general_chatbot** — Methods, Study design and participants — «had used at least one GenAI tool for academic or personal learning purposes»

**Остальные поля:**
- country: CHN — Methods, Study design and participants — «Participants were recruited from six universities located in eastern, central, and western China.»
- data_years: 2026 — Methods, Study design and participants — «Data were collected between April 20 and May 30, 2026, after ethics approval had been obtained.»
- design: cross-sectional — Methods, Study design and participants — «This cross-sectional survey examined GenAI-related behavioral dysregulation and mental health indicators among Chinese university students.»
- clinical_group: NA — NA — «NA»
- age_mean: 20.31 — Results, Measurement quality...; Table 1 — «The mean age was 20.31 years (SD = 1.43), and 59.4% of participants were female.»
- age_sd: 1.43 — Results, Measurement quality...; Table 1 — «The mean age was 20.31 years (SD = 1.43)»
- age_min: NR (eligibility criterion: 18 or older) — Methods, Study design and participants — «full-time undergraduate students aged 18 years or older»
- age_max: NR — NR — «NR»
- pct_female: 59.4 — Results; Table 1 — «Female | 1,112 (59.4)»
- mode: online — Methods, Procedure and data quality control — «The questionnaire was administered online through a secure Chinese survey platform.»
- attention_checks: yes — Methods, Procedure and data quality control — «one attention-check item was embedded in the questionnaire, and 54 responses that failed this item were excluded. Third, 68 questionnaires completed in less th…»
- pub_status: journal — Title page — «Year: 2026; venue: Frontiers in public health; DOI: 10.3389/fpubh.2026.1910408»
- language: English — Full text — «Problematic generative AI use and mental health risks among Chinese university students»
- funding_coi: No funding received; authors declare no conflicts of interest. — Funding Statement; Conflict of interest — «financial support was not received for this work and/or its publication. ... conducted in the absence of any commercial or financial relationships that could b…»
- notes: AI system is unspecified 'GenAI tool(s)' (no named platforms), coded general_chatbot as unspecified generative AI. Problematic GenAI use is an ad hoc 8-item adapted scale; subscale scores (loss of control, compulsive use, academic avoidance) appear only as profile means (Table 4), with no correlations. Self-regulated learning (r = -0.47 with PGU), health literacy (-0.31) and academic engagement (-0.28) are in Table 2 but were not extracted because they match no dictionary key. Self-regulated learning might arguably map to self_control; the reviewer should decide. The data collection dates (Ap…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited via course groups and online class channels at six universities. — Methods, Study design and participants — «A convenience sampling strategy was used»
2. отклик: **unclear** — The reported 87.5% is the share of submitted questionnaires that were valid (1872/2140). The number of students invited is not reported, so the true response rate is unknown. — Methods, Study design and participants — «268 responses were excluded and 1,872 valid responses were retained for analysis, yielding an effective response rate of 87.5%.»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc adapted 8-item scale, but this report gives psychometric evidence: a CFA of the adapted and selected scales jointly, plus CR, AVE and discriminant validity (details only in Supplementary Table S3, not available).… — Results, Measurement quality...; Discussion, Strengths and … — «CFA supported the measurement structure of the adapted and selected scales, χ2/df = 3.42, CFI = 0.958, TLI = 0.951, RMSEA = 0.036, and SRMR = 0.041.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.91 in this sample. — Methods, Problematic generative AI use; Table 2 — «The scale showed excellent internal consistency in this study (Cronbach's α = 0.91).»
5. валидные шкалы коррелятов: **no** — Academic anxiety (5 items) and psychological distress (6 items) were selected/adapted items, not named published instruments. Sleep problems used a 'PSQI-type approach' with added GenAI-related bedtime content, not the … — Methods, Academic anxiety; Psychological distress; Sleep pr… — «The items were selected and adapted from student academic-anxiety and mental-health research»
6. качество данных: **yes** — Attention-check item, a completion-time threshold and patterned-response screening were applied. — Methods, Procedure and data quality control — «Four data-quality procedures were applied before analysis.»

Правки:
- 

Проверено: да

---

## ST082 · Zhang 2026 · International Journal of Human-Computer Interaction

Основной отчёт R2894: [текст](../../fulltext/text/R2894.txt) · [PDF](../../fulltext/pdf/R2894.pdf) — «The Comparative Trap: How Social Comparison Orientation Drives Problematic Generative AI (GenAI) Use» — [DOI](https://doi.org/10.1080/10447318.2026.2668619)
Расхождения в тексте: Table 3 gives only latent (Fornell-Larcker) correlations; no observed correlation matrix is reported. Correlations of PGAIU with social comparison orientation (0.457), AI flow (0.593) and perceived irreplaceability (0.591) are not extracted because these constructs are not in the dictionary. In the text the SCO→PGAIU direct effect is β = 0.241 (Table 5, standardised) and in Table 6 it is 0.244. 0.244 equals the unstandardised B in Table 5, so the labelling is inconsistent. These are SEM paths and were not extracted. The text says 'Cronbach's alpha coefficients were all above 0.800', which matches Table 2.
Заметка ИИ: I extracted one sample and one effect (a latent correlation between PGAIU and FoMO). The PGAIU here has 5 items, but the PUCAI family is listed with 6. FoMO was reworded for the GenAI context, so the reviewer should check that it still counts as fomo.

### ST082-1 · Chinese GenAI users, CHN, n=396
Отчёты: R2894 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PUCAI · total (T1) | **fomo** · FoMO (adapted from Przybylski et al., 2013 and Chen, 2025; … | latent | **0.517** | **396** | 1 | Page 8, Table 3 | «PGAIU / 0.457 / 0.517 / 0.593 / 0.591 / 0.778 (columns SCO, FoMO, AIF, PI, PGAIU)» |

- E1: α ИИ .883, α коррелята .878; заметка: Fornell-Larcker discriminant validity table (diagonal = sqrt AVE); off-diagonals treated as latent construct correlations. FoMO refers to AI-contextualised FoMO. No observed (Pearson) correlation matrix reported.

**Ключевые поля выборки:**
- **n_analysed: 396** — Page 6, 3.1 Participants — «After removing 130 responses with no GenAI use experience and low-quality responses, 396 valid samples were retained»
- **population: general_adults** — Page 6, 3.1 Participants — «Chinese GenAI users ... 97% aged 19-35. 86.1% held a bachelor's degree or above.»
- **sampling: NR** — Page 6, 3.1 Participants — «The survey was anonymously distributed and collected 526 questionnaires from Chinese GenAI users.»
- **ai_system: general_chatbot** — Page 6, 3.1 Participants — «collected 526 questionnaires from Chinese GenAI users»

**Остальные поля:**
- country: CHN — Page 6, 3.1 Participants — «collected 526 questionnaires from Chinese GenAI users»
- data_years: NR — Page 15, Ethical approval — «The approval reference number is PNU IRB 2025-09-100.»
- design: cross-sectional — Page 14, Conclusion (limitations) — «although cross-sectional surveys are efficient for testing theoretical pathways, they are limited in their ability to explain causal effects»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 7, Table 1 — «Age 19–23 168 42.4 24–27 136 34.4»
- age_sd: NR — Page 7, Table 1 — «Age 19–23 168 42.4»
- age_min: 19 — Page 7, Table 1 — «Age 19–23 168 42.4»
- age_max: NR — Page 7, Table 1 — «32–35 17 4.3 ≥36 12 3.0»
- pct_female: 51.5 — Page 7, Table 1 — «Female 204 51.5»
- mode: NR — Page 6, 3.1 Participants — «The survey was anonymously distributed ... respondents received a 3 RMB reward.»
- attention_checks: yes — Page 6, 3.1 Participants — «To ensure data quality, screening items and attention check questions were included.»
- pub_status: journal — Header (venue) — «International Journal of Human-Computer Interaction; DOI: 10.1080/10447318.2026.2668619»
- language: English — Full text — «The Comparative Trap: How Social Comparison Orientation Drives Problematic Generative AI (GenAI) Use»
- funding_coi: No specific grant; authors declare no competing interests — Page 15, Acknowledgement; Declaration of Interest — «This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. ... The authors report there are no comp…»
- notes: Mode not stated (3 RMB reward suggests online, but this is not reported). Age reported only in bands; the lowest band starts at 19, the top band is open (≥36). Data-collection year not stated; the IRB number (2025-09-100) points to 2025. PGAIU adapted from Hu et al. (2023) with 5 items (PGAIU1-5), not the 6 in the family description, all on 7-point scales. FoMO items adapted to the GenAI context (fear of falling behind in AI productivity). Author contributions list 'Funding acquisition' for J. Lee, although the paper says there was no specific grant.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Recruitment channel and sampling method not described beyond 'anonymously distributed'. — Page 6, 3.1 Participants — «The survey was anonymously distributed and collected 526 questionnaires from Chinese GenAI users.»
2. отклик: **unclear** — No response rate reported; 526 collected, 396 retained after exclusions; non-responders not compared. — Page 6, 3.1 Participants — «After removing 130 responses with no GenAI use experience and low-quality responses, 396 valid samples were retained»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from the published PUCAI (Hu et al., 2023); CFA loadings, CR and AVE reported in this report. Note: shortened to 5 items. — Page 7, 3.2; Page 8, Table 2 — «problematic GenAI use was adapted from Hu et al. (2023)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .883 for PGAIU in this sample. — Page 8, Table 2 — «PGAIU PGAIU1 4.25 1.44 .825 .883 .885 .606»
5. валидные шкалы коррелятов: **yes** — FoMO adapted from published scales (Przybylski et al., 2013; Chen, 2025), though reworded for the GenAI context. — Page 7, 3.2 — «FoMO was adapted from Przybylski et al. (2013) and Chen (2025)»
6. качество данных: **yes** — Attention checks and screening items included; low-quality responses removed. — Page 6, 3.1 Participants — «To ensure data quality, screening items and attention check questions were included.»

Правки:
- 

Проверено: да

---

## ST083 · Zhang 2026 · Frontiers in psychology

Основной отчёт R2898: [текст](../../fulltext/text/R2898.txt) — «The relationship between academic self-efficacy and GenAI dependence among college students: a chain mediation model of academic stress and perceived usefulnes…» — [DOI](https://doi.org/10.3389/fpsyg.2026.1784354)
Лонгитюд (для описания): This is a two-wave time-lagged design with a three-week interval. Academic self-efficacy and academic stress were measured at T1, and perceived usefulness and GenAI dependence at T2. No construct was measured at both waves, so the study reports no cross-lagged or autoregressive paths. Its SEM paths (e.g., academic self-efficacy → GenAI dependence β = −0.233; academic stress → GenAI dependence β = 0.251) are multivariable cross-occasion paths, not cross-lagged effects. The authors say the design is not fully longitudinal.
Расхождения в тексте: The correlation values in the text match Table 1 (r = −0.422 and 0.411 with AID). Table 1 combines the Fornell-Larcker √AVE diagonal with the inter-construct correlations, but the text calls them Pearson correlations, so they were coded as pearson. The CR for AID (0.906) is the same as its Cronbach's alpha (0.906). In Table 4 the total effect point estimate (−0.386) lies outside its own reported bias-corrected CI (−0.404 to −0.245); this does not affect the extracted values. The ethics approval body is named differently in two places ('Academic Ethics Committee of Jinling Institute of Technology' vs. 'School of Business, Jinling Institute of Technology'), and consent is described as 'Informed consent' in one place and 'written informed consent' in another, even though the survey was online.
Заметка ИИ: Age is not reported. pct_female was calculated from 196 female out of 428. The specific GenAI tools are not named; participants were only asked about 'GenAI' in learning contexts, so this was coded as general_chatbot. Both correlations are cross-occasion (T1 correlate, T2 AI dependence).

### ST083-1 · Five universities, eastern China, college students, time-lagged two-wave survey (n = 428)
Отчёты: R2898 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ZHANG5 · total (T4) | **self_efficacy** · Academic self-efficacy scale (adapted from Nielsen et al., … | pearson | **−0.422** | **428** | lagged: T1-T2 | Table 1 | «AID1 / 0.756 / 0.659 / 0.906 / AID / −0.422** / 0.411** / 0.399** / 0.812» |
| E2 | ZHANG5 · total (T4) | **academic_stress** · Academic stress scale (adapted from Zhang et al., 2024), 5 … | pearson | **0.411** | **428** | lagged: T1-T2 | Table 1 | «AID1 / 0.756 / 0.659 / 0.906 / AID / −0.422** / 0.411** / 0.399** / 0.812» |

- E1: α ИИ 0.906, α коррелята 0.918; заметка: Academic self-efficacy measured at wave 1, GenAI dependence at wave 2 (three weeks later); no same-occasion correlation reported. Text describes it as Pearson correlation.
- E2: α ИИ 0.906, α коррелята 0.899; заметка: Academic stress measured at wave 1, GenAI dependence at wave 2 (three weeks later); no same-occasion correlation reported.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 428** — Table 1 — «Table 1: confirmatory factor analysis and correlation analysis results (N = 428).»
- **population: university_students** — Participants and procedure — «The sample included 85 freshmen, 116 sophomores, 144 juniors, and 83 seniors.»
- **sampling: convenience** — Participants and procedure — «Participants were recruited using a convenience sampling strategy from five universities located in eastern China.»
- **ai_system: general_chatbot** — Participants and procedure; GenAI dependence scale — «participants were informed that the questionnaire concerned experiences with GenAI in learning contexts, and all respondents confirmed familiarity with such tools»

**Остальные поля:**
- country: CHN — Participants and procedure — «Participants were recruited using a convenience sampling strategy from five universities located in eastern China.»
- data_years: 2025 — Participants and procedure — «This study conducted an online questionnaire survey between September and November 2025.»
- design: other — Participants and procedure — «A time-lagged data collection design was adopted, in which relevant data were collected in two stages separated by a three-week interval.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 45.8 (196/428, computed) — Participants and procedure — «Among the respondents, 196 were female and 232 were male.»
- mode: online — Participants and procedure — «This study conducted an online questionnaire survey between September and November 2025.»
- attention_checks: NR — Participants and procedure — «A total of 500 questionnaires were distributed to students from five universities, and 459 valid responses were collected in this stage.»
- pub_status: journal — Header — «Venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1784354»
- language: English — Full text — «The relationship between academic self-efficacy and GenAI dependence among college students»
- funding_coi: No funding received; no conflicts of interest declared — Funding Statement; Conflict of interest — «The author(s) declared that financial support was not received for this work and/or its publication.»
- notes: Two waves three weeks apart: academic self-efficacy and academic stress at T1 (n = 459 valid), perceived usefulness and GenAI dependence at T2 (n = 428 matched). No AI usage frequency was measured. Students received an incentive of RMB 5–10.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited through university online channels — Participants and procedure — «Participants were recruited using a convenience sampling strategy from five universities located in eastern China.»
2. отклик: **yes** — Effective response rate 85.6% (428/500) — Participants and procedure — «A total of 428 valid questionnaires were returned, yielding an effective response rate of 85.6%.»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Zhang et al., 2024) with reported reliability and construct validity; CFA in this report — GenAI dependence scale — «The GenAI dependence scale was adapted from Zhang et al. (2024), who reported satisfactory internal consistency (Cronbach's α = 0.852) and confirmed construct …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.906 in this sample — GenAI dependence scale — «In the present study, the GenAI dependence scale demonstrated good internal reliability (Cronbach's α = 0.906).»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy adapted from Nielsen et al. (2018) and Acosta-Enriquez et al. (2025); academic stress adapted from Zhang et al. (2024); both published, adapted with minor modifications — Measurements — «All measurement instruments used in this study were adapted from well-established scales in prior research. Minor modifications were made»
6. качество данных: **unclear** — Refers to 'valid' responses but no screening rule or attention checks described — Participants and procedure — «459 valid responses were collected in this stage.»

Правки:
- 

Проверено: да

---

## ST084 · Zhao 2026 · Frontiers in Psychiatry

Основной отчёт R2909: [текст](../../fulltext/text/R2909.txt) · [PDF](../../fulltext/pdf/R2909.pdf) — «Narcissistic traits and emotional dependence on large language models among adolescents» — [DOI](https://doi.org/10.3389/fpsyt.2026.1958023)
Расхождения в тексте: The text and Table 2 give the same correlations (LLM emotional dependence with anxiety r=0.146; with narcissistic traits 0.301; with physical activity -0.075). Narcissistic traits (FFNI-SF total) and physical activity (PARS-3) were not extracted because neither fits a key in the construct dictionary. The subgroup means in Table 3 are partly inconsistent with the overall mean in Table 2 (M=12.27). The sex and left-behind means weight back to about 12.27 and 12.25. The only-child means (12.68, n=823; 12.15, n=799) weight back to about 12.42, and the grade means weight back to about 12.07. The ethics statement mentions only guardian consent, while the Methods say the adolescents also gave written consent. The age range goes up to 19 in a junior high sample. No values were shown only in figures.
Заметка ИИ: One sample and one eligible effect (anxiety). The rob_1 rating is unclear because the paper calls the design multistage stratified sampling but does not say how schools were chosen. A reviewer should check the sampling code ('probability') against rob_1.

### ST084-1 · Chinese junior high school students, four study areas, N=1,622
Отчёты: R2909 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | SIRVENT · total (T3) | **anxiety** · GAD-2 | pearson | **0.146** | **1622** | 1 | Page 4, Table 2 | «4. LLM emotional dependence 12.27 6.24 0.301*** 0.146*** -0.075** –» |

- E1: α ИИ .948, α коррелята .869; заметка: Row 4 (LLM emotional dependence) by column 2 (Anxiety). The GAD-2 has only two items (inter-item r = .768).

**Ключевые поля выборки:**
- **n_analysed: 1622** — Page 4, Table 1 / Table 2 — «TABLE 1 Demographic characteristics of the study sample (N = 1,622).»
- **population: adolescents** — Page 3, 2.1 Participants — «The participants were aged between 10 and 19 years, with an average age of 14.64 years (standard deviation = 1.65).»
- **sampling: probability** — Page 3, 2.1 Participants — «In each of the four study areas, one ordinary junior high school was selected, and two complete classes were randomly selected from each of the seventh, eighth, and ninth grades at each school, totaling 24 classes.»
- **ai_system: general_chatbot** — Page 4, 2.2.2 — «the measure assessed generalized emotional dependence on LLM-based interaction rather than dependence on a speciﬁc commercial platform»

**Остальные поля:**
- country: CHN — Page 1, Abstract — «A multistage stratiﬁed sample of 1622 Chinese junior high school students was surveyed in November 2025.»
- data_years: 2025 — Page 3, 2.1 Participants — «Data collection was conducted in November 2025»
- design: cross-sectional — Page 9, Discussion (limitations) — «First, the cross-sectional design precludes conclusions regarding temporal precedence or causality»
- clinical_group: NA — NA — «NA»
- age_mean: 14.64 — Page 3, 2.1 Participants — «with an average age of 14.64 years (standard deviation = 1.65)»
- age_sd: 1.65 — Page 3, 2.1 Participants — «with an average age of 14.64 years (standard deviation = 1.65)»
- age_min: 10 — Page 3, 2.1 Participants — «The participants were aged between 10 and 19 years»
- age_max: 19 — Page 3, 2.1 Participants — «The participants were aged between 10 and 19 years»
- pct_female: 50.86 — Page 4, Table 1 — «Girls 825 50.86»
- mode: paper — Page 4-5, 2.3 Quality control — «using paper-and-pencil questionnaires administered collectively in classrooms ... no mobile phones, computers, or web-based survey platforms were used»
- attention_checks: yes — Page 5, 2.3 Quality control — «Questionnaires meeting one or more of the predeﬁned exclusion criteria—substantial missing responses, obvious patterned responding, or logical inconsistencies—…»
- pub_status: journal — Page 1 — «Front. Psychiatry 17:1958023. doi: 10.3389/fpsyt.2026.1958023»
- language: English — Page 1 — «Narcissistic traits and emotional dependence on large language models among adolescents»
- funding_coi: Funded by Anhui Province Research Project on Student Mental Health Education (25XLKT-GX061); no commercial or financial conflicts of interest declared. — Page 10, Funding; Conflict of interest — «This work was supported by the Anhui Province Research Project on Student Mental Health Education (25XLKT-GX061).»
- notes: The paper calls the sampling multistage stratified, with classes chosen at random, but does not say how schools were chosen. Actual LLM use (platform, frequency) was not measured. Clustering by class and school was not accounted for.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Called multistage stratified sampling, and classes within schools were picked at random, but the report does not say how areas or schools were chosen (one school per area, 'selected'). The authors say the sample is not … — Page 3, 2.1; Page 9, Discussion — «one ordinary junior high school was selected, and two complete classes were randomly selected ... although the sample should not be considered nationally repre…»
2. отклик: **yes** — All eligible students in the selected classes were invited, all 1,857 questionnaires were returned, and 87.35% were valid (at least 60%). — Page 3, 2.1 Participants — «All 1,857 questionnaires were returned. After data quality screening, 235 invalid questionnaires were excluded, and 1,622 valid questionnaires were retained, w…»
3. валидная шкала зависимости от ИИ: **yes** — The adapted five-item measure was validated in this report: EFA with parallel analysis in one half-sample and CFA in the other, plus CR and AVE. — Page 4, 2.2.2 — «CFI = 0.987, TLI = 0.974, RMSEA = 0.067 ... Composite reliability (CR = 0.949) and average variance extracted (AVE = 0.788)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .948 in this sample. — Page 4, 2.2.2 — «In the full sample, the measure demonstrated excellent internal consistency (Cronbach’s a = .948)»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, anxiety, was measured with the published GAD-2. — Page 4, 2.2.3 — «Anxiety symptoms were assessed using the two-item Generalized Anxiety Disorder scale (GAD-2)»
6. качество данных: **yes** — Predefined exclusion rules were stated for missing responses, patterned responding and logical inconsistencies. — Page 5, 2.3 Quality control — «predeﬁned exclusion criteria—substantial missing responses, obvious patterned responding, or logical inconsistencies—were excluded from further analysis»

Правки:
- 

Проверено: да

---

## ST085 · Zhu 2026 · Frontiers in psychology

Основной отчёт R2934: [текст](../../fulltext/text/R2934.txt) · [PDF](../../fulltext/pdf/R2934.pdf) — «Perceived AI empowerment and threat in relation to university students' dependence on GenAI: the indirect role of trust in AI.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1940317)
Расхождения в тексте: Text (p. 6–7) and Table 3 agree for DE–PT (r = −0.316). The Fornell–Larcker latent correlation (Table 5) is −0.318. This is a different estimate, not a conflict. Correlations with perceived AI empowerment (r = 0.446) and trust in AI (r = 0.602) were not extracted because neither construct has a dictionary key. HTMT DE–PT = 0.335 (Table 6) was not extracted. SEM and multigroup paths (Tables 8–9, Figure 2) were not extracted. Minor discrepancy: Methods say electronic informed consent was obtained, while the Ethics statement says participants gave written informed consent.
Заметка ИИ: One sample (n = 360). Only perceived AI threat was extracted as a correlate, coded as ai_anxiety, and this mapping needs reviewer confirmation. The paper explicitly says the scale differs from technology anxiety and frames it as a cognitive appraisal. It was extracted because its items express AI-related worry and come partly from the AIAS. If the reviewer rejects the mapping, the study contributes no effects.

### ST085-1 · Chinese university students with GenAI experience, multi-province (Henan, Hubei), n=360
Отчёты: R2934 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2934_1 · total (T2) | **ai_anxiety** · Perceived AI threat (5 items adapted from TAI and AIAS) | pearson | **−0.316** | **360** | 1 | Page 7, Table 3 | «DE / 0.446∗∗ / −0.316∗∗ / 0.602∗∗ / 1 (columns PE, PT, TR, DE)» |
| E2 | ADHOC_R2934_1 · total (T2) | **ai_anxiety** · Perceived AI threat (5 items adapted from TAI and AIAS) | latent | **−0.318** | **360** | 1 | Page 8, Table 5 (Fornell–Larcker criterion) | «PT / −0.318 / 0.027 / 0.859 (columns DE, PE, PT)» |

- E1: α ИИ 0.954, α коррелята 0.934; заметка: Perceived AI threat is framed as a cognitive appraisal of AI risks; the construct mapping to ai_anxiety needs reviewer confirmation. The text gives the same value (r = −0.316, p < 0.01).
- E2: α ИИ 0.954, α коррелята 0.934; заметка: Latent correlation from the Fornell–Larcker table of the four-factor CFA. The construct mapping to ai_anxiety needs reviewer confirmation.

**Ключевые поля выборки:**
- **n_analysed: 360** — Page 5, 3.1 — «After data cleaning, 360 valid questionnaires were retained for subsequent analysis.»
- **population: university_students** — Page 5, 3.1 — «the final sample consisted of 360 GenAI-experienced university students»
- **sampling: convenience** — Page 5, 3.1 — «Participants were recruited using convenience sampling.»
- **ai_system: general_chatbot** — Page 2, Introduction; Page 5, 3.1 — «Students use large language model-based systems to search for information, generate ideas, revise written work... targeting Chinese university students with experience using GenAI»

**Остальные поля:**
- country: CHN — Page 5, 3.1 Participants and procedure — «targeting Chinese university students with experience using GenAI»
- data_years: 2026 — Page 5, 3.1 — «Data collection took place from April 24 to May 25, 2026, across universities in multiple provinces and cities including Henan and Hubei.»
- design: cross-sectional — Page 5, 3.1 — «This study employed a cross-sectional questionnaire design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 5, Table 1 — «Age distribution: 72.8% were under 22 years old, 12.2% aged 22–25, 11.4% aged 26–30, and 3.6% over 30.»
- age_sd: NR — Page 5, Table 1 — «Age distribution: 72.8% were under 22 years old»
- age_min: NR — Page 5, Table 1 — «<22 years old 262 72.8»
- age_max: NR — Page 5, Table 1 — «>30 years old 13 3.6»
- pct_female: 51.7 — Page 5, 3.1 and Table 1 — «including 174 males (48.3%) and 186 females (51.7%)»
- mode: online — Page 5, 3.1 — «The questionnaire was distributed online via the online platform and disseminated through university course groups, learning communities, and social media chan…»
- attention_checks: yes — Page 5, 3.1 — «Excluded responses included those with completion times shorter than the preset minimum threshold (1 min), consecutive identical answers on more than 10 questi…»
- pub_status: journal — Page 1, header — «TYPE Original Research PUBLISHED 23 September 2026 DOI 10.3389/fpsyg.2026.1940317»
- language: English — Full text — «Perceived AI empowerment and threat in relation to university students' dependence on GenAI»
- funding_coi: Funded by National Natural Science Foundation of China (62477008; 62507012), Henan Provincial Education Science Planning (2024JKZD21), Henan Provincial Higher Education key project (24A880014); authors declare no conflict of interest. — Page 12, Funding; Conflict of interest — «This research was supported by the National Natural Science Foundation of China (grant numbers 62477008; 62507012)... conducted in the absence of any commercia…»
- notes: 739 questionnaires collected; 360 retained after quality screening (48.7% retained). Other study variables (perceived AI empowerment, trust in AI) have no key in the construct dictionary and were not extracted. Perceived AI threat (items adapted from TAI, Kieslich et al. 2021, and AIAS, Wang & Wang 2022) is coded as ai_anxiety; the authors frame it as a cognitive appraisal of negative consequences rather than emotional fear, so the reviewer should confirm that it fits this construct. The AI dependence scale has 7 items adapted from Morales-García et al. (2024) and Wu et al. (2026).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online through course groups, learning communities and social media. — Page 5, 3.1 — «Participants were recruited using convenience sampling.»
2. отклик: **unclear** — No response rate reported. The figure of 360 out of 739 shows how many were retained after screening, not a response rate. — Page 5, 3.1 — «A total of 739 questionnaires were initially collected... After data cleaning, 360 valid questionnaires were retained»
3. валидная шкала зависимости от ИИ: **yes** — The items were adapted from published AI dependence scales (Morales-García 2024; Wu et al. 2026). This report also gives CFA evidence for the adapted 7-item scale: loadings .850–.880, CR .954, AVE .749, Fornell-Larcker … — Page 6, 3.2.4; Page 8, Table 4 — «AI dependence was measured with seven items adapted from prior research on dependence on AI, including the AI dependence framework proposed by Morales-García e…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.954 in this sample. — Page 6, 3.2.4 — «In the present sample, Cronbach's α was 0.954.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, perceived AI threat, uses 5 items adapted from two published instruments (TAI; AIAS), with CFA evidence in this report. Caveat: it is a composite adaptation, not an intact published scale. — Page 5, 3.2.2 — «Perceived AI threat was measured using five items adapted from the Threats of Artificial Intelligence (TAI) framework developed by Kieslich et al. (2021) and t…»
6. качество данных: **yes** — Explicit screening rules: minimum completion time, straightlining, and logical inconsistencies. — Page 5, 3.1 — «Excluded responses included those with completion times shorter than the preset minimum threshold (1 min), consecutive identical answers on more than 10 questi…»

Правки:
- 

Проверено: да

---

## ST086 · Zhu 2026 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R2935: [текст](../../fulltext/text/R2935.txt) — «The Double-Edged Sword of AI Efficiency: Self-Efficacy Erosion as a Mediator Linking Instant Gratification and Perceived AI Efficacy to AI Dependency.» — [DOI](https://doi.org/10.3390/bs16040530)
Расхождения в тексте: 1. AI dependency mean: Section 4.1 says 2.92; Table 1 gives 2.929. 2. Subscale means: the text gives means for Y_FunctionalDep (3.223) and Y_AutonomyLoss (2.635), but Table 1 has no subscale rows or correlations. 3. Min and max: Section 4.1 says Table 1 Column (2) presents minimum and maximum values; the table shows only the mean and SD. 4. Significance: the Table 1 note marks significance with * at the 10% level. 5. Table 3: the note says 'unstandardized path coefficients', while the text calls them β. The note also refers to Column (2) where it means Column (4). 6. Table 2 path coefficients (SEM betas) were not extracted.
Заметка ИИ: One sample (n = 576) and one effect extracted: total AI dependency (IAT-adapted ADS-R) with task-domain self-efficacy, r = 0.235. The other correlates in Table 1 fit no dictionary key. Country and data years are not reported.

### ST086-1 · University students (undergraduate and postgraduate), country not stated, n=576
Отчёты: R2935 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | IAT_ADAPTED · total (T4) | **self_efficacy** · Task-Domain Self-Efficacy (Mo_TaskSE), 3 items adapted from… | pearson | **0.235** | **576** | 1 | Table 1, Column (3) | «5 Mo_TaskSE / 0.82 / 3.432 / 0.647 / 0.235 * / 0.396 * / 0.126 * / 0.300 *» |

- E1: α ИИ 0.92, α коррелята 0.82; заметка: Domain-specific self-efficacy: confidence in doing tasks independently in the person's main AI application area (not AI self-efficacy). The reviewer should confirm it fits the self_efficacy key. Subscale (Y_FunctionalDep, Y_AutonomyLoss) correlations are not reported.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.48, 0.66 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 576** — Section 3.1; Table 2 — «576 valid responses were collected»
- **population: university_students** — Section 3.1 — «576 valid responses were collected, comprising 469 undergraduate and 107 postgraduate students.»
- **sampling: NR** — Section 3.1 — «In this study, we employed a questionnaire survey targeting undergraduate and postgraduate students. ... A total of 751 questionnaires were distributed and collected.»
- **ai_system: general_chatbot** — Section 3.1.1 — «defined as a functional and cognitive reliance on generative AI tools rather than pathological addiction»

**Остальные поля:**
- country: NR — Institutional Review Board Statement — «approved by the Tsinghua University Science and Technology Ethics Committee (Project No. THU-04-2026-0055; approved on 2 January 2026)»
- data_years: NR — Institutional Review Board Statement — «approved on 2 January 2026»
- design: cross-sectional — Abstract — «We examine the model using Structural Equation Modeling (SEM) with cross-sectional data collected from 576 users who have engaged with AI.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Section 3.1 — «with ages ranging from 18 to 25 years»
- age_sd: NR — Section 3.1 — «with ages ranging from 18 to 25 years»
- age_min: 18 — Section 3.1 — «with ages ranging from 18 to 25 years»
- age_max: 25 — Section 3.1 — «with ages ranging from 18 to 25 years»
- pct_female: 70 — Section 3.1 — «Among the respondents, 30% were male and 70% were female»
- mode: NR — Section 3.1 — «A total of 751 questionnaires were distributed and collected.»
- attention_checks: NR — Section 3.1 — «After excluding responses from participants who did not meet the study's target criteria (e.g., non-students or incomplete submissions), 576 valid responses we…»
- pub_status: journal — Header — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs16040530»
- language: English — Full text — «The Double-Edged Sword of AI Efficiency: Self-Efficacy Erosion as a Mediator Linking Instant Gratification and Perceived AI Efficacy to AI Dependency»
- funding_coi: No external funding; no conflict of interest declared — Funding Statement; Conflicts of Interest — «This research received no external funding. ... the corresponding author states that there is no conflict of interest.»
- notes: Country is not stated; ethics approval came from Tsinghua University (suggesting CHN), but the country was not inferred. The paper names no specific AI product, only 'generative AI tools' / 'AI tools'. 751 questionnaires were collected and 576 kept after excluding non-students and incomplete submissions. Only one correlate fits the dictionary (task-domain self-efficacy). Instant gratification preference (SPSRQ-based, 4 ad hoc items; r=.480 with AI dependency), perceived AI efficacy (r=.555), erosion of self-efficacy due to AI use (r=.656) and social norms of AI use (r=.389) were not extracted…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The recruitment and sampling method is not described beyond a questionnaire survey aimed at students. It appears to be non-probability, but this is not stated. — Section 3.1 — «we employed a questionnaire survey targeting undergraduate and postgraduate students»
2. отклик: **unclear** — No response rate is given. 751 questionnaires were 'distributed and collected', and 576 were valid after exclusions; that figure is a retention rate, not a response rate. — Section 3.1 — «A total of 751 questionnaires were distributed and collected.»
3. валидная шкала зависимости от ИИ: **yes** — The scale was adapted from the IAT (Young, 1998), and EFA/CFA on this sample (including a split-sample CFA) are reported. The authors themselves call it an adapted indicator rather than a fully established instrument. — Section 3.1.1; Section 3.2; Section 5.3 — «Exploratory and Confirmatory Factor Analyses (EFA/CFA) on the current sample revealed a clear and robust two-factor structure underlying AI dependency»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha in this sample: total .92, Factor 1 .91, Factor 2 .89. — Section 3.1.1 — «Cronbach's α in this study was excellent for Factor 1 (α = 0.91), Factor 2 (α = 0.89), and the overall 15-item scale (α = 0.92).»
5. валидные шкалы коррелятов: **yes** — The one extracted correlate (task-domain self-efficacy) uses 3 items adapted from the published self-efficacy scale in Venkatesh et al. (2003). The adaptation is substantial and no validation is reported beyond alpha an… — Section 3.1.5 — «The 3 items were adapted from the self-efficacy scale used by Venkatesh et al. (2003)»
6. качество данных: **unclear** — Only non-students and incomplete submissions were excluded. No attention checks or careless-responding screening are reported. — Section 3.1 — «After excluding responses from participants who did not meet the study's target criteria (e.g., non-students or incomplete submissions)»

Правки:
- 

Проверено: да

---

## ST087 · Özbay 2026 · Osmangazi Journal of Educational Research

Основной отчёт R2954: [текст](../../fulltext/text/R2954.txt) · [PDF](../../fulltext/pdf/R2954.pdf) — «Exploring the Relationship between Fear of Being without Artificial Intelligence, AI Addiction, and Academic Self-Efficacy among University Students» — [DOI](https://doi.org/10.59409/ojer.1755463)
Расхождения в тексте: 1) Sample size: the Method says 554 students were collected and calls 554 sufficient; the abstract and Table 1 give 544, and the regression df (3,540) fits 544. The 10 cases were presumably dropped by the completeness screen, but the report does not say so. 2) The AIAS–ASE correlation in Table 2 (-.34) has no significance stars, and the text says 'No other statistically significant correlations were observed'. At n=544 this value would be highly significant, so either the stars are missing or the value has a typo. 3) The abstract says 'higher academic self-efficacy appears to reduce it [fear of being without AI]', but the reported r (.09) and regression B (0.41, β 0.11) are positive. 4) The Discussion reverses the regression direction ('AILPES significantly predicted both ASE and AIAS'), although AILPES was the dependent variable. 5) The ASE response anchors are listed as 'Exactly fits …
Заметка ИИ: One cross-sectional sample of Turkish undergraduates. AI dependence was measured with the Turkish adaptation of the Morales-García DAI (called AIAS here) and the AILPES (AIlessphobia) scale. The only eligible dictionary correlate is academic self-efficacy, which gives 4 Pearson effects from Table 2.

### ST087-1 · Artvin Çoruh University undergraduates, Türkiye, n=544
Отчёты: R2954 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale (Jerusalem & Schwarzer; Turkis… | pearson | **-.34** | **544** | 1 | Page 9, Table 2 | «4. AIAS / -.06 / .05 / -.34 / -» |
| E2 | ADHOC_R2954_2 · total (T2) | **self_efficacy** · Academic Self-Efficacy Scale (Jerusalem & Schwarzer; Turkis… | pearson | **.09** | **544** | 1 | Page 9, Table 2; Page 8, text | «5. AILPES / -.09* / .00 / .09* / .59** / -» |
| E3 | ADHOC_R2954_2 · Academic Self-Efficacy Anxiety (T2) | **self_efficacy** · Academic Self-Efficacy Scale (Jerusalem & Schwarzer; Turkis… | pearson | **.09** | **544** | 1 | Page 9, Table 2; Page 8, text | «6. Academic Self-Efficacy Anxiety / -.08 / .01 / .09* / .58** / .92**» |
| E4 | ADHOC_R2954_2 · Lack of Academic Confidence without AI (T2) | **self_efficacy** · Academic Self-Efficacy Scale (Jerusalem & Schwarzer; Turkis… | pearson | **.07** | **544** | 1 | Page 9, Table 2 | «7. Lack of Academic Confidence without AI / -.10* / .03 / .07 / .48** / .87** / .61**» |

- E1: **направление: as named (the author reads higher ASE as higher self-efficacy; response anchors are listed from 'Exactly fits me' to 'Does not fit me at all', so check the sco…**; α ИИ .83, α коррелята .73; заметка: No significance stars are printed for this cell, and the text does not mention it (it says no other significant correlations). With n=544, r=-.34 would be p<.001. The matrix gives two decimals only.
- E2: **направление: as named (the author reads higher ASE as higher self-efficacy; check the anchor direction)**; α ИИ .92, α коррелята .73; заметка: The text gives r = .09, p = .030.
- E3: **направление: as named (the author reads higher ASE as higher self-efficacy; check the anchor direction)**; α ИИ NR, α коррелята .73; заметка: The text gives r = .09, p = .027. Subscale alpha is not reported for this sample.
- E4: **направление: as named (the author reads higher ASE as higher self-efficacy; check the anchor direction)**; α ИИ NR, α коррелята .73; заметка: Not significant. Subscale alpha is not reported for this sample.

**Ключевые поля выборки:**
- **n_analysed: 544** — Page 8, Table 1 — «Descriptive Features of the Students (n=544)»
- **population: university_students** — Page 5, Participants and Procedure — «554 undergraduate students enrolled at Artvin Çoruh University»
- **sampling: convenience** — Page 5, Participants and Procedure — «Participants were recruited through institutional email invitations, and a convenience sampling method was used during the data collection process.»
- **ai_system: ai_unspecified** — Page 6, Data Collection Tools — «the AILPES assesses students' anxiety, fear, and perceived inadequacy when unable to access AI tools (e.g., chatbots, text editors) during educational tasks»

**Остальные поля:**
- country: TUR — Page 5, Participants and Procedure — «data collected from a total of 554 undergraduate students enrolled at Artvin Çoruh University»
- data_years: 2025 — Page 5, Participants and Procedure — «The study was conducted during the Spring semester of 2025 (May–June)»
- design: cross-sectional — Page 5, Research Design — «This study was conducted using a descriptive and correlational research design»
- clinical_group: NA — NA — «NA»
- age_mean: 21.14 — Page 8, Results and Table 1 — «The mean age of the participants was 21.14 ± 1.81 years»
- age_sd: 1.81 — Page 8, Results and Table 1 — «The mean age of the participants was 21.14 ± 1.81 years»
- age_min: NR — Page 8, Table 1 — «18–20 | 211 | 38.8»
- age_max: NR — Page 8, Table 1 — «≥24 | 42 | 7.7»
- pct_female: 58.10 — Page 8, Table 1 — «Female | 316 | 58.10»
- mode: online — Page 5, Participants and Procedure — «participation was confirmed upon full submission of the online survey»
- attention_checks: yes — Page 7, Data Analysis — «data screening procedures were implemented; incomplete questionnaires were excluded, and only responses with at least 80% completion were retained for analysis»
- pub_status: journal — Page 1, header — «Osmangazi Journal of Educational Research Volume 12 (Special Issue) 2025»
- language: English — Full text — «Exploring the Relationship between Fear of Being without Artificial Intelligence, AI Addiction, and Academic Self-Efficacy among University Students»
- funding_coi: No funding; no conflict of interest declared — Page 15, Conflict of Interest; Funding — «I confirm that there is no known conflict of interest regarding the conduct or authorship of this study. Funding There was not any forms of funding for current…»
- notes: Age_min and age_max are not reported; Table 1 gives only age bands (18–20 to ≥24). attention_checks = yes rests only on the completeness rule (≥80% completion). The AIAS is the Turkish adaptation (Savaş, 2024) of the Morales-García DAI. AILPES subscale alphas are not reported for this sample; the total alpha is .92.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited by institutional email at one university. — Page 5, Participants and Procedure — «a convenience sampling method was used during the data collection process»
2. отклик: **unclear** — Number invited and response rate not reported; non-responders not compared. — Page 5, Participants and Procedure — «Participants were recruited through institutional email invitations»
3. валидная шкала зависимости от ИИ: **yes** — AIAS is the Morales-García et al. (2024) Dependence on AI scale, adapted and validated in Turkish by Savaş (2024). — Page 6, Artificial Intelligence Addiction Scale (AIAS) — «Developed by Morales-García et al. (2024) and adapted into Turkish by Savaş (2024), the Artificial Intelligence Addiction Scale consists of 5 items»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .83 in this sample. — Page 6, AIAS — «In the present study, the Cronbach’s alpha coefficient was .83.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate is academic self-efficacy, measured with the published Jerusalem & Schwarzer scale in its Turkish adaptation (Yılmaz et al., 2007). — Page 6, Academic Self-Efficacy Scale — «Originally developed by Jerusalem and Schwarzer (1981) and adapted into Turkish by Yilmaz et al. (2007), this scale includes 7 items»
6. качество данных: **yes** — Stated rule for invalid responses: incomplete questionnaires excluded (at least 80% completion needed). The screening covers completeness only; there were no attention checks or careless-responding checks. Reviewer shou… — Page 7, Data Analysis — «incomplete questionnaires were excluded, and only responses with at least 80% completion were retained for analysis»

Правки:
- 

Проверено: да

---

## ST088 · Özsoy 2026 · Discover Psychology

Основной отчёт R2956: [текст](../../fulltext/text/R2956.txt) · [PDF](../../fulltext/pdf/R2956.pdf) — «Psychometric evaluation of the Turkish version of the AI Chatbot Dependence Scale (AICD-8)» — [DOI](https://doi.org/10.1007/s44202-026-00801-9)
Расхождения в тексте: Text and Table 2 agree for the AICD-8-T correlations (r = .68 with PCUS, .30 with BSMAS, .39 with IAT-SF, .24 with loneliness). Other issues: (1) The Table 2 footnote defines only ** and ***, but single-star values are printed (e.g., 0.12*, -0.15*). (2) The RULS-6 is described as a 'five-point Likert scale ranging from 1 (never) to 4 (always)', which contradicts itself. (3) The Discussion says the link with daily use is strong 'particularly daily ChatGPT use', but Table 2 shows r = .51 for daily chatbot use and only .39 for daily ChatGPT use. (4) Table 1 gives PCUS alpha 0.88 and omega 0.87; the alpha matches the text. (5) Data collection years are not reported. (6) The PCUS is the AI-dependence family used as the convergent-validity measure, and its correlation with the AICD (0.68) is not extracted because it is not a dictionary correlate. No coefficients are shown only in figures.
Заметка ИИ: There is one pooled sample of N=600 (employees and students). I extracted 6 Pearson correlations: AICD-8-T total and PCUS total, each with BSMAS, RULS-6 and IAT-SF. Daily-use hours, age and gender are not dictionary constructs, so they are not extracted.

### ST088-1 · Turkish employees and university students, TUR, n=600
Отчёты: R2956 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS), Turkish version | pearson | **0.30** | **600** | 1 | Table 2, page 6 | «3. Bergen Social Media Addiction Scale / 0.30*** / 0.33*** / -» |
| E2 | AICD · total (T4) | **loneliness** · Revised UCLA Loneliness Scale (RULS-6), Turkish version | pearson | **0.24** | **600** | 1 | Table 2, page 6 | «4. Revised UCLA Loneliness Scale / 0.24*** / 0.36*** / 0.46*** / -» |
| E3 | AICD · total (T4) | **problematic_internet_use** · Internet Addiction Test–Short Form (IAT-SF), Turkish version | pearson | **0.39** | **600** | 1 | Table 2, page 6 | «5. Internet Addiction Test–Short Form / 0.39*** / 0.47*** / 0.78*** / 0.51*** / -» |
| E4 | PCUS · total (T1) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS), Turkish version | pearson | **0.33** | **600** | 1 | Table 2, page 6 | «3. Bergen Social Media Addiction Scale / 0.30*** / 0.33*** / -» |
| E5 | PCUS · total (T1) | **loneliness** · Revised UCLA Loneliness Scale (RULS-6), Turkish version | pearson | **0.36** | **600** | 1 | Table 2, page 6 | «4. Revised UCLA Loneliness Scale / 0.24*** / 0.36*** / 0.46*** / -» |
| E6 | PCUS · total (T1) | **problematic_internet_use** · Internet Addiction Test–Short Form (IAT-SF), Turkish version | pearson | **0.47** | **600** | 1 | Table 2, page 6 | «5. Internet Addiction Test–Short Form / 0.39*** / 0.47*** / 0.78*** / 0.51*** / -» |

- E1: α ИИ 0.86, α коррелята 0.88
- E2: α ИИ 0.86, α коррелята 0.91
- E3: α ИИ 0.86, α коррелята 0.91
- E4: α ИИ 0.88, α коррелята 0.88; заметка: PCUS used as convergent-validity measure (Turkish translation by Hoşgör & Güngördü)
- E5: α ИИ 0.88, α коррелята 0.91
- E6: α ИИ 0.88, α коррелята 0.91

**Ключевые поля выборки:**
- **n_analysed: 600** — Table 1 — «Total (N = 600)»
- **population: mixed** — Abstract — «The sample comprised 600 individuals (249 employees and 351 university students).»
- **sampling: convenience** — Page 9, 5 Limitations — «Moreover, the use of convenience sampling limits the generalizability of the results.»
- **ai_system: general_chatbot** — Page 5, Daily technology use variables; Page 4, Measures — «how many hours per day do you use AI chatbots [ChatGPT, Gemini, Claude, Copilot, DeepSeek, etc.]?»

**Остальные поля:**
- country: TUR — Page 3, 2.1 Participants and recruitment procedure — «comprising employees from the public and private sectors and university students in Türkiye»
- data_years: NR — Page 10, Received date — «Received: 21 December 2025 / Accepted: 19 June 2026»
- design: validation study — Abstract — «the present study translated the AICD-8 into Turkish, and its psychometric properties were evaluated»
- clinical_group: NA — NA — «NA»
- age_mean: 27.62 — Page 3, 2.1 — «The mean age of the participants was 27.62 years (SD = 9.57; range = 18–62).»
- age_sd: 9.57 — Page 3, 2.1 — «The mean age of the participants was 27.62 years (SD = 9.57; range = 18–62).»
- age_min: 18 — Page 3, 2.1 — «(SD = 9.57; range = 18–62)»
- age_max: 62 — Page 3, 2.1 — «(SD = 9.57; range = 18–62)»
- pct_female: 70.5 — Page 3, 2.1 — «Of these participants, 70.5% were female»
- mode: online — Page 3, 2.1 — «The data were collected using an online survey designed to assess the study variables»
- attention_checks: yes — Page 3, 2.1 — «responses failing three attention-check items (e.g., "If you are reading this item, please mark 54"), and straightlining responses ... 41 cases were removed»
- pub_status: journal — Page 1, header — «Discover Psychology (2026) 6:256 https://doi.org/10.1007/s44202-026-00801-9»
- language: English — Full text — «Psychometric evaluation of the Turkish version of the AI Chatbot Dependence Scale (AICD-8)»
- funding_coi: No external funding; authors declare no competing interests — Page 10, Funding; Competing interests — «The present study was conducted without external funding. ... The authors declare no competing interests.»
- notes: The sample pools employees (n=249) and students (n=351), who were recruited through different channels; correlations are reported only for the pooled sample. The PCUS (convergent measure, Turkish translation) is also extracted as an AI-dependence family.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited via university information system and researchers' professional networks — Page 4, 2.1; Page 9, Limitations — «For employees, the survey was shared through the researchers' professional networks. ... the use of convenience sampling limits the generalizability»
2. отклик: **unclear** — Only number of initial participants (641) reported; number invited / response rate not reported — Page 3, 2.1 — «A total of 641 individuals initially participated in the study»
3. валидная шкала зависимости от ИИ: **yes** — AICD-8 has a published development/validation study (Zhang et al.) and CFA validation of the Turkish version is reported here — Page 4, 2.3; Page 5, Results — «The AICD-8 [42] was used to assess chatbot dependence. ... CFA results were as follows: χ² = 66.77, p < .001, χ²/df = 3.71, TLI = 0.96, CFI = 0.97, RMSEA = 0.0…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.86 for AICD-8-T in this sample (PCUS alpha 0.88) — Page 4, 2.3; Table 1 — «In the present study, Cronbach's alpha for the AICD-8-T was 0.86.»
5. валидные шкалы коррелятов: **yes** — All correlates measured with published instruments (Turkish versions of BSMAS, RULS-6, IAT-SF) — Page 4-5, 2.3 Measures — «The BSMAS [2] Turkish version [12] ... The RULS-6 [39] Turkish version [13] ... The IAT-SF [31] Turkish version [24]»
6. качество данных: **yes** — Three attention-check items and straightlining screening applied — Page 3, 2.1 — «responses failing three attention-check items ... and straightlining responses ... 41 cases were removed, resulting in a final sample of 600 participants»

Правки:
- 

Проверено: да

---

## ST089 · Аникин 2026 · International journal of medicine and psychology.

Основной отчёт R2972: [текст](../../fulltext/text/R2972.txt) · [PDF](../../fulltext/pdf/R2972.pdf) — «ИИ-зависимость как предиктор академической прокрастинации у студентов: феноменология, механизмы и риски для психологического здоровья» — [DOI](https://doi.org/10.58224/2658-3313-2026-9-5-210-218)
Расхождения в тексте: The DAI–TPS value r = .237 (p = .029) is the same in the abstract (Russian and English), Results and Conclusions. The DAI–pseudoproductivity r = .318 (p = .003) is not extracted: pseudoproductivity is not in the construct dictionary, and it is a single author-made item (item 4). The 71.4% vs 17.6% comparison between high- and low-DAI students refers to a different statement ("used AI for tasks they had planned to do themselves"), not the stated item-4 indicator, and the group sizes for that comparison are not given. The abstract and Conclusions say AI-mediated procrastination is "statistically associated with deterioration of psychological health indicators", but the methods describe no psychological-health measure and no such statistic is reported. Academic self-efficacy, self-regulation and fear of negative evaluation are discussed as mechanisms but were not measured. The level distri…
Заметка ИИ: I found one eligible effect: DAI total with Tuckman Procrastination Scale, r = .237, n = 85. The paper reports no reliabilities, recruitment method, administration mode, data-collection years or funding statement.

### ST089-1 · Psychology undergraduates, Siberian Federal University, RUS, n=85
Отчёты: R2972 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | other: DAI (Morales-García et al., 2024), Russian translation · total (?) | **procrastination** · Tuckman Procrastination Scale (TPS) total | pearson | **.237** | **85** | 1 | p. 213, Результаты и обсуждения (also abstract p.… | «По результатам корреляционного анализа между суммарными баллами DAI и TPS отмечается положительная статистически значимая связь: r = .237, p = .029. [Correlation between DAI and TPS total scores: r =…» |

- E1: заметка: Instrument: Dependence on Artificial Intelligence Scale, authors' translation. Reported only in the text; there is no correlation matrix. The paper calls the TPS 'academic procrastination', but the TPS measures general procrastination tendency.

**⚠ Проверка скриптом (обратите внимание):**
- E1: шкала ИИ не из списка семейств: напишите, какая это шкала

**Ключевые поля выборки:**
- **n_analysed: 85** — p. 213, Материалы и методы — «в количестве 85 человек (n = 85) [85 persons (n = 85)]»
- **population: university_students** — p. 213, Материалы и методы — «Выборку составили студенты направления подготовки 37.03.01 Психология (бакалавриат) [The sample comprised students of the 37.03.01 Psychology (bachelor's) programme]»
- **sampling: NR** — p. 213, Материалы и методы — «Выборку составили студенты направления подготовки 37.03.01 Психология (бакалавриат) в количестве 85 человек (n = 85). [The sample comprised 85 students of the 37.03.01 Psychology (bachelor's) programme.]»
- **ai_system: ai_unspecified** — p. 213, Материалы и методы (DAI description); p. 213 Результаты — «потребности в обращении к системам ИИ при выполнении задач [need to turn to AI systems when performing tasks]; зависимость от ИИ-инструментов при выполнении учебных задач [dependence on AI tools when doing study tasks]»

**Остальные поля:**
- country: RUS — p. 213, Материалы и методы — «Эмпирическое исследование проводилось на базе Сибирского федерального университета. [The empirical study was conducted at Siberian Federal University.]»
- data_years: NR — p. 213, Материалы и методы — «NR (the report gives no data-collection dates; manuscript submitted 29 April 2026)»
- design: cross-sectional — p. 213, Материалы и методы — «Обработка данных производилась методами описательной статистики и корреляционного анализа (коэффициент r Пирсона). [Data were processed with descriptive statis…»
- clinical_group: NA — NA — «NA»
- age_mean: 20.4 — p. 213, Материалы и методы — «Возраст испытуемых – 18-25 лет (M = 20,4; SD = 1,7) [Participants' age 18-25 years (M = 20.4; SD = 1.7)]»
- age_sd: 1.7 — p. 213, Материалы и методы — «Возраст испытуемых – 18-25 лет (M = 20,4; SD = 1,7) [Participants' age 18-25 years (M = 20.4; SD = 1.7)]»
- age_min: 18 — p. 213, Материалы и методы — «Возраст испытуемых – 18-25 лет [Participants' age 18-25 years]»
- age_max: 25 — p. 213, Материалы и методы — «Возраст испытуемых – 18-25 лет [Participants' age 18-25 years]»
- pct_female: 61 — p. 213, Материалы и методы — «гендерный состав: 61% женщин, 39% мужчин [gender composition: 61% women, 39% men]»
- mode: NR — p. 213, Материалы и методы — «NR (administration mode not described)»
- attention_checks: NR — p. 213, Материалы и методы — «NR (no screening of responses described)»
- pub_status: journal — p. 210, header — «Научно-исследовательский журнал «International Journal of Medicine and Psychology / Международный журнал медицины и психологии» ... Научная статья / Original a…»
- language: Russian (English title, abstract and references also given) — p. 210-211 — «ИИ-зависимость как предиктор академической прокрастинации у студентов [AI dependence as a predictor of academic procrastination in students]»
- funding_coi: NR (no funding or conflict-of-interest statement) — p. 218, Информация об авторах — «NR»
- notes: DAI (Morales-García et al., 2024): 5 items, 1-5 Likert, the authors' own Russian translation with back-translation. It had no psychometric adaptation, and no reliability is reported. The TPS is described as measuring procrastination as a stable personal trait, but the paper calls it academic procrastination. The pseudoproductivity correlate (author-made items, single-item indicator) is not in the construct dictionary, so it is not extracted. The authors call the study a pilot (p. 215, Conclusions).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The report names the target group (psychology bachelor's students at one university) but does not describe how they were recruited or whether the whole cohort was invited. — p. 213, Материалы и методы — «Выбор данной группы обусловлен высокой степенью вовлечённости студентов психологических направлений в использование цифровых инструментов [The group was chosen…»
2. отклик: **unclear** — No response rate and no comparison of non-responders. — p. 213, Материалы и методы — «Выборку составили студенты ... в количестве 85 человек (n = 85).»
3. валидная шкала зависимости от ИИ: **yes** — The DAI has a published development and validation study (Morales-García et al., 2024). Caveat: the authors used their own Russian translation (with back-translation) and did no psychometric adaptation, which they list … — p. 213, Материалы и методы; p. 215, Выводы — «Шкала зависимости от ИИ DAI (Dependence on Artificial Intelligence Scale; Morales-García et al., 2024) [7] – пятипунктовый инструмент ... был выполнен авторски…»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for the DAI in this sample. — p. 213, Материалы и методы — «Ответы фиксировались по шкале Ликерта (1 – «совершенно не соответствует мне»; 5 – «описывает меня идеально»).»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (procrastination) was measured with the published Tuckman Procrastination Scale (Tuckman, 1991). — p. 213, Материалы и методы — «Шкала прокрастинации Б. Тукмана (TPS; Tuckman, 1991) [22] предназначена для диагностики выраженности склонности к прокрастинации»
6. качество данных: **unclear** — No attention checks, careless-responding screening or rule for invalid responses is reported. — p. 213, Материалы и методы — «Обработка данных производилась методами описательной статистики и корреляционного анализа (коэффициент r Пирсона).»

Правки:
- E1.exposure_family = DAI

Проверено: да

---

## ST090 · Чорномидз 2026 · PSYCHOLOGICAL JOURNAL

Основной отчёт R2984: [текст](../../fulltext/text/R2984.txt) · [PDF](../../fulltext/pdf/R2984.pdf) — «DEVELOPMENT AND PSYCHOMETRIC VALIDATION OF THE SCREENING SCALE FOR ARTIFICIAL INTELLIGENCE ADDICTION DIAGNOSIS (AIAS-10+1 V4.0)» — [DOI](https://doi.org/10.31108/1.2026.12.3.1)
Расхождения в тексте: 1) The Discussion (p. 22) says loneliness correlates with "Фактором А так і з Фактором Б" (rs = 0.237). The Results (p. 8) give Factor А rs = 0.237 and Factor В rs = 0.178 with loneliness, and stress with Factor Б (0.199). The Results values are used. 2) The n differs across analyses: 242 for descriptives; 234 for the regression ("після виключення пропущених значень" [after excluding missing values]) and for the v4.0 cut-off validation. The n for the Spearman correlations is not stated. 3) The v4.0 descriptives differ slightly: M = 16.60, SD = 5.45 (N = 234, p. 14) vs M = 16.61, SD = 5.41 (N = 242, Table 9). The quadrant counts in Table 8 (N = 234) differ from Table 12 (N = 242), e.g. 'Ризик подвійний' [double risk] has n = 14 vs 15. 4) Satisfaction with study, self-rated critical thinking and AI-use duration were reported as non-significant, with no coefficients. These variables are no…
Заметка ИИ: All extracted correlations refer to the original AIAS-11 v3.0 scoring, because the correlation analysis comes before the scale revision. The correlates are single ad hoc 3-point items.

### ST090-1 · Ukrainian university students, online survey, N = 242
Отчёты: R2984 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2984_2 · total (T4) | **loneliness** · Single ad hoc item 'відчуття самотності' (feeling of loneli… | spearman | **0.179** | **242** | 1 | Page 8, Розподіл за рівнями залежності та кореляц… | «виявив значущі позитивні зв'язки між ЗІЗ та самотністю (rs = 0.179, p = .005) [significant positive association between the total index and loneliness (rs = 0.179)]» |
| E2 | ADHOC_R2984_2 · total (T4) | **academic_stress** · Single ad hoc item 'Я часто відчуваю стрес через навчання а… | spearman | **0.178** | **242** | 1 | Page 8 | «стресом (rs = 0.178, p = .006) [stress (rs = 0.178, p = .006)]» |
| E3 | ADHOC_R2984_2 · Factor А: Штучна інтимність та антропоморфізація … (T3) | **loneliness** · Single ad hoc loneliness item, 3-point | spearman | **0.237** | **242** | 1 | Page 8 | «самотність найбільше корелює з Фактором А (rs = 0.237, p < .001) [loneliness correlates most strongly with Factor A (rs = 0.237)]» |
| E4 | ADHOC_R2984_2 · Factor Б: Когнітивна атрофія та втрата автономнос… (T2) | **academic_stress** · Single ad hoc stress item (stress because of study or work)… | spearman | **0.199** | **242** | 1 | Page 8 | «тоді як стрес – переважно з Фактором Б (rs = 0.199, p = .002) [whereas stress correlates mainly with Factor Б (rs = 0.199)]» |
| E5 | ADHOC_R2984_2 · Factor В: Втрата контролю та дезадаптивний копінг… (T1) | **loneliness** · Single ad hoc loneliness item, 3-point | spearman | **0.178** | **242** | 1 | Page 8 | «Фактор В також пов'язаний із самотністю (rs = 0.178, p = .006). [Factor В is also associated with loneliness (rs = 0.178).]» |

- E1: α ИИ 0.777, α коррелята NR; заметка: The total index (ЗІЗ) here is the original 11-item v3.0 score, including the reversed item 6. The n for the correlation is not stated: 242 is assumed, while the regression used N = 234.
- E2: α ИИ 0.777, α коррелята NR; заметка: Coded academic_stress because the authors call it 'академічного стресу' (p. 6) and the item refers to study or work. The reviewer may prefer 'stress'. n assumed 242.
- E3: α ИИ 0.777, α коррелята NR; заметка: n assumed 242.
- E4: α ИИ 0.612, α коррелята NR; заметка: Same construct coding as the total-score stress row (academic_stress vs stress). n assumed 242.
- E5: α ИИ 0.505, α коррелята NR; заметка: Subscale alpha is below .60. n assumed 242.

**Ключевые поля выборки:**
- **n_analysed: 242** — Page 6, Результати — «До фінального аналізу увійшли дані 242 респондентів [Data from 242 respondents were included in the final analysis]»
- **population: university_students** — Page 2, Матеріали та методи — «До участі запрошувалися студенти закладів вищої освіти України, які є активними користувачами засобів штучного інтелекту. [Ukrainian university students who actively use AI tools were invited.]»
- **sampling: convenience** — Page 2, Матеріали та методи — «Дослідження проводилося методом онлайн-анкетування на добровільній та анонімній основі. [The study used a voluntary, anonymous online survey.]»
- **ai_system: general_chatbot** — Page 6, Результати — «Найпоширенішим інструментом є ChatGPT (85.5% користувачів), далі – Gemini (Google) (69.4%), Copilot (Microsoft) (15.3%) та Claude (9.1%). [The most common tool is ChatGPT (85.5% of users), then Gemini (69.4%), Copilot (15.3%) and Claude (9.1%).]»

**Остальные поля:**
- country: UKR — Page 2, Матеріали та методи — «До участі запрошувалися студенти закладів вищої освіти України [Students of higher education institutions of Ukraine were invited to participate]»
- data_years: NR — Page 27 — «Дата отримання статті: 21.12.2025 [Date of receipt of the article: 21.12.2025] (collection years not reported)»
- design: validation study — Page 2, Матеріали та методи — «Метою даного дослідження є розробка та комплексна психометрична валідизація нового інструменту скринінгової діагностики [The aim is the development and compreh…»
- clinical_group: NA — NA — «NA»
- age_mean: 19.5 — Page 2 — «Вік респондентів коливався від 18 до 30 років (M = 19.5, SD = 1.4, Мо = 19). [Respondents were aged 18 to 30 (M = 19.5, SD = 1.4, Mo = 19).]»
- age_sd: 1.4 — Page 2 — «(M = 19.5, SD = 1.4, Мо = 19)»
- age_min: 18 — Page 2 — «Вік респондентів коливався від 18 до 30 років [Respondents were aged 18 to 30]»
- age_max: 30 — Page 2 — «Вік респондентів коливався від 18 до 30 років [Respondents were aged 18 to 30]»
- pct_female: 71.5 — Page 2 — «(жіноча стать – 71.5%, n = 173; чоловіча – 28.5%, n = 69) [(female 71.5%, n = 173; male 28.5%, n = 69)]»
- mode: online — Page 2 — «Дослідження проводилося методом онлайн-анкетування [The study was conducted as an online survey]»
- attention_checks: NR — Page 2 — «Критерієм включення слугувала позитивна відповідь на контрольне запитання «Ви користуєтесь штучним інтелектом?»; ... жодного виключення не здійснювалося. [Incl…»
- pub_status: journal — Page 1, header — «PSYCHOLOGICAL JOURNAL Volume 12 Issue 3 (106) 2026»
- language: Ukrainian — Page 27, How to cite — «PSYCHOLOGICAL JOURNAL, 12(3), 7–33. https://doi.org/10.31108/1.2026.12.3.1 [in Ukrainian]»
- funding_coi: NR (no funding or conflict-of-interest statement; the authors say they used Claude Sonnet 4.6 to write the analysis code and edit the text) — Page 3, Методи статистичного аналізу — «автори використовували інструмент штучного інтелекту Claude (Anthropic, модель Claude Sonnet 4.6) для написання та налагодження коду статистичного аналізу [the…»
- notes: All correlations were computed with the original AIAS-11 v3.0 scoring (ADHOC_R2984_2): an 11-item total including the reversed item 6, and the three original factors. The correlates (loneliness, stress) are single ad hoc 3-point items coded 1-3. A self-rated dependence item also correlated with the total (rs = 0.435), but it is not a dictionary construct.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Voluntary online convenience recruitment; the authors themselves name possible selection bias. — Page 23, limitations — «Потенційний selection bias: онлайн-формат рекрутингу міг залучити респондентів із вищою рефлексивністю [Potential selection bias: online recruitment may have a…»
2. отклик: **unclear** — No response rate is reported and non-responders are not described. — Page 2 — «усі 242 респонденти підтвердили факт використання ШІ-інструментів [all 242 respondents confirmed using AI tools]»
3. валидная шкала зависимости от ИИ: **yes** — The AIAS-11 v3.0 is the authors' own instrument, and its psychometric evaluation is reported in this report (alpha, item-total correlations, EFA). That evaluation showed weak subscales and led to the revision. — Page 10, Психометричний аналіз шкали AIAS-11 — «Повна шкала AIAS-11 (11 пунктів, включаючи реверсний П6) продемонструвала задовільну внутрішню узгодженість: α = 0.777. [The full AIAS-11 showed satisfactory i…»
4. надёжность шкалы ИИ в выборке: **yes** — Total-score alpha is .777. Subscale alphas are below .70 for Factor Б (.612) and Factor В (.505); Factor А is .777. — Page 10 — «α = 0.777. ... Фактор А – α = 0.777, Фактор Б – α = 0.612, Фактор В – α = 0.505.»
5. валидные шкалы коррелятов: **no** — Loneliness and stress were each measured with one ad hoc 3-point item (No/Sometimes/Yes). — Page 3 — «Анкета також включала чотири запитання психологічного контексту (рівень стресу, відчуття самотності, ...) за 3-бальною шкалою (Ні / Іноді / Так) [four context …»
6. качество данных: **unclear** — No attention checks or careless-responding screening are reported. The 'control question' was only an eligibility check for AI use. — Page 2 — «Критерієм включення слугувала позитивна відповідь на контрольне запитання «Ви користуєтесь штучним інтелектом?» [Inclusion criterion: a 'yes' to the control qu…»

Правки:
- 

Проверено: да

