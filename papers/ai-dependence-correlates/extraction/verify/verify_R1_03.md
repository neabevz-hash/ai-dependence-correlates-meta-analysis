# Проверка выписывания — файл 3 из 13

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

## ST021 · Fu 2026 · Frontiers in psychology

Основной отчёт R0781: [текст](../../fulltext/text/R0781.txt) — «Academic involution atmosphere and AI dependence among university students: the mediating role of academic stress and the moderating role of individual academi…» — [DOI](https://doi.org/10.3389/fpsyg.2026.1857123)
Расхождения в тексте: (1) The direct path from involution atmosphere to AI dependence (model with mediator) is given as β = −0.023 in one sentence and as β = −0.022, p = 0.570, in a later one. (2) The text gives H1 (without mediator) as p < 0.05, but Table 4 gives p = 0.002. The indirect effect is reported as p < 0.05 in one place and p < 0.01 in another; Table 4 gives p = 0.011. (3) Table 1 is misaligned: the '26 and above' age band appears on the 'Education level' row. (4) The Methods name the 'Ethics Committee of the Communication University of China', and the ethics statement gives IRB approval No. XSLL20260104-2. That number seems to be dated 2026, but data were collected in October 2025. The statement also says consent was 'written' although the survey was online. (5) The '93.28% effective response rate' is valid/completed questionnaires, not a response rate. No figure-only coefficients.
Заметка ИИ: There is one effect: a latent (PLS Fornell-Larcker) correlation between AI dependence and academic stress. No observed Pearson correlation matrix is reported. HTMT values and SEM paths were not extracted.

### ST021-1 · Chinese university students, Credamo online panel, China, n=500
Отчёты: R0781 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ZHANG5 · total (T4) | **academic_stress** · Academic stress subscale of the stress scale (Solberg et al… | latent | **0.598** | **500** | 1 | Table 2 (lower-left triangle, Fornell-Larcker) | «Academic stress / 0.908 / 0.911 / 0.929 / 0.686 / 0.598 / 0.198 / 0.287 / 0.828» |

- E1: α ИИ 0.927, α коррелята 0.908; заметка: PLS-SEM inter-construct correlation (lower-left triangle). The 0.649 in the AI dependence row, AS column, is an HTMT value and is not extracted.

**Ключевые поля выборки:**
- **n_analysed: 500** — Methods, Data source and sample description — «36 questionnaires were excluded due to failed attention-check items ... resulting in 500 valid responses»
- **population: university_students** — Abstract; Table 1 — «data from 500 Chinese university students»
- **sampling: quota or online panel** — Methods, Data source and sample description — «questionnaire survey administered through the online platform Credamo, which functions similarly to Amazon Mechanical Turk»
- **ai_system: ai_unspecified** — Methods, Measurements — «"I feel anxious when I cannot use AI tools to complete academic tasks" and "Without AI support, I find it difficult to accomplish academic tasks."»

**Остальные поля:**
- country: CHN — Abstract — «Using PLS-SEM to analyze data from 500 Chinese university students»
- data_years: 2025 — Methods, Data source and sample description — «Data collection was conducted from October 11 to 17, 2025»
- design: cross-sectional — Limitations and prospects — «the cross-sectional survey design captures associations among the variables but does not allow for causal inference»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age | 18–20 | 135 | 27 ... 21–25 | 342 | 68.4»
- age_sd: NR — Table 1 — «Age | 18–20 | 135 | 27»
- age_min: 18 (lowest age band 18–20; exact minimum not reported) — Table 1 — «Age | 18–20 | 135 | 27»
- age_max: NR (top band '26 and above') — Table 1 — «26 and above | 23 | 4.6»
- pct_female: 52.2 — Table 1 — «Gender | Female | 261 | 52.2»
- mode: online — Methods, Data source and sample description — «questionnaire survey administered through the online platform Credamo»
- attention_checks: yes — Methods, Data source and sample description — «36 questionnaires were excluded due to failed attention-check items (e.g., “Please select ‘Strongly Disagree’”)»
- pub_status: journal — Header — «Venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1857123»
- language: English — Full text — «Academic involution atmosphere and AI dependence among university students»
- funding_coi: No funding received; authors declare no conflict of interest — Funding Statement; Conflict of interest — «financial support was not received for this work and/or its publication ... conducted in the absence of any commercial or financial relationships»
- notes: Age is reported only in bands. All correlations are PLS-SEM construct correlations; no observed correlation matrix is given. Participants were paid 3 RMB.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online crowdsourcing panel (Credamo), convenience — Methods, Data source and sample description — «administered through the online platform Credamo, which functions similarly to Amazon Mechanical Turk»
2. отклик: **unclear** — The reported 93.28% is the share of completed questionnaires that were valid, not a response rate among invited participants; the true response rate is not reported — Methods, Data source and sample description — «yielding a total of 536 completed questionnaires ... resulting in 500 valid responses and an effective response rate of 93.28%»
3. валидная шкала зависимости от ИИ: **yes** — Published 5-item scale (Zhang et al., 2024); loadings, AVE and CR reported in this sample — Methods, Measurements; Table 2 — «Following Zhang et al. (2024), AI dependence was measured using a five-item scale»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.927 in this sample — Table 2 — «AI dependence | 0.927 | 0.929 | 0.945 | 0.774»
5. валидные шкалы коррелятов: **yes** — Academic stress measured with published subscale (Solberg et al., 1993) — Methods, Measurements — «Academic stress was measured using the academic stress subscale of the stress scale developed by Solberg et al. (1993), consisting of seven items.»
6. качество данных: **yes** — Attention-check items, failed responses excluded — Methods, Data source and sample description — «36 questionnaires were excluded due to failed attention-check items»

Правки:
- 

Проверено: да

---

## ST022 · Galindo‐Domínguez 2026 · Education and Information Technologies

Основной отчёт R0801: [текст](../../fulltext/text/R0801.txt) · [PDF](../../fulltext/pdf/R0801.pdf) — «When university students’ insecurities drive them to rely excessively on Artificial Intelligence: Relationship between fear of failure, self-esteem, social sup…» — [DOI](https://doi.org/10.1007/s10639-026-14106-w)
Расхождения в тексте: (1) Peer support–ChatGPT dependence: Table 3 shows .122*** (p<.001), but the text (p.11) gives r = .122; p = .008. (2) Table 4 vs text (p.13): the text gives fear of failure β = −.558, p = .594 and self-esteem β = −.250, p = .663. Table 4 gives FOF→SES a1 = −.558 (p<.001), FOF→GPT c1' = −.250 (p = .594) and SES→GPT b1 = −.130 (p = .663). The text also gives the teacher moderation as β = .029, p = .679, but in Table 4 that value is SES*PSS b2. FoF*TSS is −.028, p = .797. (3) ChatGPT Dependency Scale fit: the text (p.10) gives χ²/df = 4.84, RMSEA = .07, GFI = .980, AGFI = .960. Table 2 gives X2/df 3.34, CFI .988, RMSEA .070. (4) Table 3 does not state its n. 467 is assumed because no exclusions or missing data are reported. (5) The fear of failure scale was shortened after CFA (items 1 and 2 removed). This does not affect the extracted correlates.
Заметка ИИ: One cross-sectional sample of Spanish education students (n = 467). Three zero-order Pearson correlations with the ChatGPT Dependency Scale total were extracted: self-esteem and two social support measures (peer and teacher). Data collection years are not reported.

### ST022-1 · University of the Basque Country education students, Spain, n=467
Отчёты: R0801 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | YE_CHATGPT · total (T2) | **self_esteem** · Rosenberg Self-Esteem Scale (SES) | pearson | **-.011** | **467** | 1 | Page 12, Table 3 (SES row, column 5) | «SES 3.91 .800 (.854) .169*** .176*** -.011» |
| E2 | YE_CHATGPT · total (T2) | **social_support** · AFA-R Friends Support dimension (adapted to peers) - Peer S… | pearson | **.122** | **467** | 1 | Page 12, Table 3 (PSS row, column 5) | «PSS 4.25 .831 (.930) .142*** .122***» |
| E3 | YE_CHATGPT · total (T2) | **social_support** · Teacher Support Scale (Torsheim et al., 2000) - Teacher Soc… | pearson | **-.042** | **467** | 1 | Page 12, Table 3 (TSS row, column 5) | «TSS 3.33 .733 (.783) -.042» |

- E1: α ИИ .858, α коррелята .854; заметка: Text p.11 confirms r = −.011; p = .815. n assumed 467 (table n not stated).
- E2: α ИИ .858, α коррелята .930; заметка: Table marks *** (p<.001) but text reports p = .008. n assumed 467. Peer support from university peers ('friends' replaced by 'peers').
- E3: α ИИ .858, α коррелята .783; заметка: Perceived support from teachers; reviewer to decide whether teacher support fits social_support or should be pooled with peer support. n assumed 467.

**Ключевые поля выборки:**
- **n_analysed: 467** — Page 8, 2.1 Participants; Table 3 n not stated — «467 Spanish university students from the University of the Basque Country participated in the study»
- **population: university_students** — Page 8, 2.1 Participants — «40 were enrolled in the Bachelor’s Degree in Early Childhood Education, 379 in the Bachelor’s Degree in Primary Education, and 48 in the Master’s Degree in Secondary Education Teaching»
- **sampling: convenience** — Page 8, 2.1 Participants — «Participants were recruited through non-probabilistic convenience sampling based on proximity to the research team.»
- **ai_system: general_chatbot** — Page 9-10, 2.2.4 Dependence on ChatGPT — «The ChatGPT Dependency Scale (Ye et al., 2024) was used to measure ChatGPT reliance... evaluates the extent of excessive use of ChatGPT for academic purposes.»

**Остальные поля:**
- country: ESP — Page 8, 2.1 Participants — «467 Spanish university students from the University of the Basque Country participated in the study»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 16, 4.3 Limitations — «Secondly, the research design is cross-sectional»
- clinical_group: NA — NA — «NA»
- age_mean: 20.44 — Page 8, 2.1 Participants — «(MAge = 20.44; SD = 2.83)»
- age_sd: 2.83 — Page 8, 2.1 Participants — «(MAge = 20.44; SD = 2.83)»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 37.0 (173/467, computed) — Page 8, 2.1 Participants — «Of these, 292 identified as male, 173 as female, and 2 as another gender.»
- mode: online — Page 10, 2.3 Procedure — «All participants completed the Google Forms questionnaire during class hours on individual computers»
- attention_checks: NR — Page 8, 2.1 Participants — «no exclusion criteria were applied»
- pub_status: journal — Page 1 — «Education and Information Technologies (2026) 31:8291–8310»
- language: English — Full text — «When university students’ insecurities drive them to rely excessively on Artificial Intelligence»
- funding_coi: No funding for the study (open access via CRUE-CSIC agreement); authors declare no competing interests — Page 16-17, Funding; Declarations — «Authors received no funding for the development of this study. ... The authors declare that they have no competing interests.»
- notes: Single sample. Fear of failure (FoF in Learning scale, r = .062 with GPT dependence) not extracted: no dictionary key. Not formally reviewed by an ethics committee. Gender split (62.5% male) is unusual for education degrees; check.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probabilistic convenience sample of students taught by the research team — Page 8, 2.1 Participants — «Participants were recruited through non-probabilistic convenience sampling based on proximity to the research team.»
2. отклик: **unclear** — Response rate not reported; the eligible pool (students of the researchers) is not quantified — Page 10, 2.3 Procedure — «the sample was defined, comprising all students of the researchers involved in the study who were enrolled in educationally related programs»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Ye et al., 2024); CFA in this sample also reported in Table 2 — Page 9-10, 2.2.4; Table 2 — «The ChatGPT Dependency Scale (Ye et al., 2024) was used ... GPT 3.34 .988 .070»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .858 in this sample — Page 12, Table 3 — «GPT 2.37 .996 (.858)»
5. валидные шкалы коррелятов: **yes** — Correlates measured with published instruments (Rosenberg SES; AFA-R Friends Support, wording adapted 'friends' to 'peers'; Teacher Support Scale, Torsheim et al.) — Page 9, 2.2.2-2.2.3 — «the Friends Support dimension of the Social Support from Parents and Friends Scale (AFA-R) ... the term "friends" was replaced with "peers"»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported — Page 8, 2.1 Participants — «no exclusion criteria were applied»

Правки:
- 

Проверено: да

---

## ST023 · Gondal 2026 · Social Prism

Основной отчёт R0868: [текст](../../fulltext/text/R0868.txt) · [PDF](../../fulltext/pdf/R0868.pdf) — «Impact of AI Dependence on Students' Academic Procrastination in Higher Education» — [DOI](https://doi.org/10.69671/socialprism.3.5.2026.69)
Расхождения в тексте: Text and tables agree: β = .44, t = 4.81, R² = .191. The text says all three alphas 'exceeded the .90 threshold', but AI Dependence α = .90 equals the threshold rather than exceeding it (minor). No correlation matrix is reported; the only effect is a single-predictor standardised beta.
Заметка ИИ: The report never states the sample's country. Pakistan is only inferred from the authors' affiliation (UMT Lahore). Age is reported in bands only. Both scales are adapted, uncited 10-item sets.

### ST023-1 · Higher education students, online convenience survey (likely Pakistan), n=100
Отчёты: R0868 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R0868_1 · total (T4) | **procrastination** · Academic Procrastination (Section C, 10 adapted items) | beta_single_predictor | **.44** | **100** | 1 | Page 8, Table 4 | «AI Dependence .44 4.81 < .001 .191 Accepted» |

- E1: α ИИ .90, α коррелята .91; заметка: Standardised beta from a simple linear regression with one predictor (no correlation table reported). R² = .191 gives r ≈ .437, which matches. t = 4.81.

**⚠ Проверка скриптом (обратите внимание):**
- E1: не корреляция, а пересчёт: проверьте, что β с одним предиктором или что группы сравнения верны

**Ключевые поля выборки:**
- **n_analysed: 100** — Page 8, Table 3 — «Table 3: Descriptive Statistics of the Study Variables (N = 100)»
- **population: university_students** — Page 5, Sample of the Study — «The study included a sample of 100 higher education students.»
- **sampling: convenience** — Page 5, Sample of the Study — «A convenience sampling technique was used because it allowed the researcher to collect data from students who were easily accessible»
- **ai_system: ai_unspecified** — Page 5, Population; Page 7, Table 2 — «These students regularly use AI tools for learning and academic activities»

**Остальные поля:**
- country: NR (sample country not stated; all authors are at University of Management and Technology, Lahore, Pakistan, so PAK is likely) — Page 1, affiliations; Page 5, Population of the Study — «The target population consisted of higher education students enrolled in universities.»
- data_years: NR — Page 1 — «Received 27 May 2026; Revised 26 June 2026; Accepted 09 July 2026»
- design: cross-sectional — Page 5, Research Design — «A cross-sectional survey design was used in this study. Data were collected from participants at one point in time»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 7, Table 2 — «Age 18–22 years 32 32.0 23–27 years 49 49.0 28 years and above 19 19.0»
- age_sd: NR — Page 7, Table 2 — «Age 18–22 years 32 32.0 23–27 years 49 49.0»
- age_min: NR (lowest age band is 18–22 years) — Page 7, Table 2 — «Age 18–22 years 32 32.0»
- age_max: NR (highest band is 28 years and above) — Page 7, Table 2 — «28 years and above 19 19.0»
- pct_female: 46 — Page 7, Table 2 — «Female 46 46.0»
- mode: online — Page 6, Data Collection Procedure — «The questionnaire was created using Google Forms and distributed online to higher education students.»
- attention_checks: NR — Page 6, Data Collection Procedure — «Participation was voluntary, and all responses remained anonymous and confidential.»
- pub_status: journal — Page 1, header — «Volume 3(5), 2026, 44-54 Online ISSN: 3006-8886»
- language: English — Full text — «Impact of AI Dependence on Students' Academic Procrastination in Higher Education»
- funding_coi: NR (no funding or conflict-of-interest statement) — Full text — «NR»
- notes: Sample: 71% BS, 26% MPhil/MS, 3% PhD; 37% use AI tools daily. The AI tools are not named for participants (the introduction names ChatGPT, Gemini, Copilot and Claude only in general terms). No correlation matrix is reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online — Page 5, Sample of the Study — «A convenience sampling technique was used»
2. отклик: **unclear** — No response rate reported — Page 6, Data Collection Procedure — «The questionnaire was created using Google Forms and distributed online to higher education students.»
3. валидная шкала зависимости от ИИ: **no** — 10 items 'adapted from previous studies', with no source cited and no validity evidence beyond alpha. 'Unclear' (instrument not named) could also apply. — Page 6, Research Instrument — «Data were collected through a structured questionnaire adapted from previous studies on AI use and academic procrastination. Minor modifications were made»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .90 in this sample — Page 6, Table 1 — «AI Dependence 10 .90»
5. валидные шкалы коррелятов: **no** — Academic procrastination was measured with 10 adapted items; no published instrument is named or cited — Page 6, Research Instrument — «Section C: Academic Pro-crastination (10 items)»
6. качество данных: **unclear** — No screening of invalid or careless responses reported — Page 6-7, Data Analysis — «The collected data were entered into the Statistical Package for the Social Sciences (SPSS) for analysis.»

Правки:
- 

Проверено: да

---

## ST024 · Guo 2026 · Lecture Notes in Education Psychology and Public Media

Основной отчёт R0901: [текст](../../fulltext/text/R0901.txt) · [PDF](../../fulltext/pdf/R0901.pdf) — «A Study on the Double-Edged Sword Effect of STARA Awareness on Task Performance» — [DOI](https://doi.org/10.54254/2753-7048/2026.32192)
Расхождения в тексте: 1. On page 4 the text calls the SA-AID value (0.527) a β ("SA was a positive predictor... AID (β=0.527)"), but it matches the Table 1 correlation. The regression β in Table 2 (M3) is 0.514. 2. The indirect effect of SA→AID→TP is given as 0.026 (positive) with a negative CI [-0.053, -0.004], so the sign is probably wrong. 3. The country is not stated. Credamo and the authors' affiliation (South China University of Technology) suggest China, but this is not confirmed. 4. Age and gender appear only as coded means (Age 2.170; Gender 1.610) without coding keys, so the age statistics and % female cannot be derived. 5. Figure 2 (moderation plot) has no extractable correlations.
Заметка ИИ: There is one cross-sectional sample of 400 employees recruited via Credamo. One eligible effect was extracted: AI dependence (Tang 3-item) with STARA awareness, coded as ai_anxiety (r = 0.527). The reviewer should check whether STARA awareness fits ai_anxiety.

### ST024-1 · Employees surveyed via Credamo (n=400)
Отчёты: R0901 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | TANG3 · total (T2) | **ai_anxiety** · STARA awareness scale (Brougham & Haar), 4 items | pearson | **0.527** | **400** | 1 | Page 4, Table 1 | «AID / 2.368 / 1.002 / 0.009 / -0.161** / -0.029 / -0.186** / 0.527** / 0.157**» |

- E1: α ИИ 0.833, α коррелята 0.904; заметка: STARA awareness is defined as 'the perception and worry of being replaced by AI' and was coded as ai_anxiety (AI-related worry). The reviewer should confirm this fits the construct. The correlation type is not stated; it is assumed to be Pearson from the 'correlation analysis' table.

**Ключевые поля выборки:**
- **n_analysed: 400** — Page 4, Table 1 note — «Note: N=400, *- P<0.05, **- P<0.01.»
- **population: employees** — Abstract, Page 1 — «analyzing the survey data of 400 employees»
- **sampling: convenience** — Page 3, Section 3 — «In Credamo, 453 questionnaires were distributed»
- **ai_system: ai_unspecified** — Page 2, Section 1 — «Employees may give up their efforts to solve problems and more likely to accept the suggestions and decisions made by AI, eventually lead to AI dependence(AID)»

**Остальные поля:**
- country: NR — Page 1, affiliation; Page 3, Section 3 — «In Credamo, 453 questionnaires were distributed»
- data_years: NR — Page 3, Section 3 — «In Credamo, 453 questionnaires were distributed, and after excluding invalid data, 400 valid samples were retained»
- design: cross-sectional — Abstract, Page 1 — «analyzing the survey data of 400 employees»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 4, Table 1 — «Age | 2.170 | 0.962»
- age_sd: NR — Page 4, Table 1 — «Age | 2.170 | 0.962»
- age_min: NR — NA — «NA»
- age_max: NR — NA — «NA»
- pct_female: NR — Page 4, Table 1 — «Gender | 1.610 | 0.488»
- mode: online — Page 3, Section 3 — «In Credamo, 453 questionnaires were distributed»
- attention_checks: NR — Page 3, Section 3 — «after excluding invalid data, 400 valid samples were retained»
- pub_status: conference — Page 1, header — «Proceedings of the 4th International Conference on Social Psychology and Humanity Studies»
- language: English — Full text — «A Study on the Double-Edged Sword Effect of STARA Awareness on Task Performance»
- funding_coi: NR — NA — «NA»
- notes: Age and gender are reported only as coded category means, without coding keys. The country is not stated; Credamo and the Guangzhou affiliation suggest China. 'After excluding invalid data' is stated without criteria.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online recruitment via the Credamo crowdsourcing platform. — Page 3, Section 3 — «In Credamo, 453 questionnaires were distributed»
2. отклик: **yes** — Reported recovery rate of 88.3% (400 valid out of 453), which is at least 60%. — Page 3, Section 3 — «400 valid samples were retained, with a recovery rate of 88.3%»
3. валидная шкала зависимости от ИИ: **yes** — Uses the published Tang et al. (2023) AI dependence scale. — Page 3, Section 3; ref [14] — «AID 3-item multiple-choice Tang scale (Cronbach's α 0.833) [14]»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.833 in this sample. — Page 3, Section 3 — «AID 3-item multiple-choice Tang scale (Cronbach's α 0.833)»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (STARA awareness) was measured with the published Brougham & Haar scale. — Page 3, Section 3 — «4 items of SA were assessed using the Brougham developed scale (Cronbach's α 0.904) [2]»
6. качество данных: **unclear** — Invalid data were excluded, but the criteria (attention checks or other rules) are not stated. — Page 3, Section 3 — «after excluding invalid data, 400 valid samples were retained»

Правки:
- 

Проверено: да

---

## ST025 · Hafeez 2026 · Perspectives in Social Sciences

Основной отчёт R0918: [текст](../../fulltext/text/R0918.txt) · [PDF](../../fulltext/pdf/R0918.pdf) — «GENERATIVE AI DEPENDENCY AND DECISION-MAKING STYLES: A PREDICTIVE STUDY OF ADULTS IN PAKISTAN» — [DOI](https://doi.org/10.63468/pss.101)
Расхождения в тексте: The inclusion criteria required use of a generative AI tool at least once a week. However, Table 1 shows 6 participants who use AI 'Rarely' and 7 who use it 'Never' (12.7%), and the Limitations section admits that 'AI was not screened'. The Sample section first calls participants '102 adults of both male and female students' but then says students and working professionals were included. The Discussion mentions a 'male predominance' in using AI for study, which contradicts the finding that women scored higher. Table 3 r values match the text and the single-predictor β values in Table 6. The Discussion repeats paragraphs (pages 15–18). Figures 1–2 are histograms only and contain no coefficients. The article dates (received Sept 2026, published Oct 2026) do not give the years of data collection.
Заметка ИИ: I extracted one effect, the GAIDS total with MDMQ procrastination. Only the GAIDS total was correlated; no GAIDS subscale correlations were reported. Whether MDMQ decisional procrastination counts as eligible for the procrastination key needs reviewer confirmation.

### ST025-1 · Adults (students and working professionals), Rawalpindi/Islamabad, Pakistan, n=102
Отчёты: R0918 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **procrastination** · Melbourne Decision Making Questionnaire (MDMQ) Procrastinat… | pearson | **−.339** | **102** | 1 | Page 12, Table 3 | «Procrastination / −.339*** / < .001» |

- E1: α ИИ .90, α коррелята .74; заметка: MDMQ procrastination measures decisional procrastination (delaying decisions as a coping style), not general or academic task procrastination; the reviewer should confirm it is eligible for the procrastination key. The single-predictor regression (Table 6, β = −.339) duplicates this r and is not ex…

**Ключевые поля выборки:**
- **n_analysed: 102** — Page 12, Table 3 — «Pearson Correlations Between GAIDS and MDMQ Subscales (N = 102)»
- **population: mixed** — Page 5, Sample; Page 9, Table 1 — «Both students and working professionals were included ... Student 41 40.2 | Working professional 42 41.2 | Both 19 18.6»
- **sampling: convenience** — Page 5, Method, Sample; Page 7, Procedure — «obtained purposively from Rawalpindi and Islamabad ... distributed via academic, professional and social networks»
- **ai_system: general_chatbot** — Page 5, Method, Sample — «using at least one Generative AI tool (e.g., ChatGPT, Google Gemini, Microsoft Copilot, or Claude) at least once a week»

**Остальные поля:**
- country: PAK — Page 5, Method, Sample — «obtained purposively from Rawalpindi and Islamabad, Pakistan by using an online form and face-to-face method»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 4, Introduction — «A cross sectional, predictive correlational design (Creswell & Creswell, 2018; Gravetter & Forzano, 2018) was employed»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 9, Table 1 — «Age 20–30 years 75 73.5 | 31–40 years 27 26.5»
- age_sd: NR — NA — «NR»
- age_min: 20 — Page 5, Method, Sample — «102 adults ... aged between 20 and 40 years»
- age_max: 40 — Page 5, Method, Sample — «102 adults ... aged between 20 and 40 years»
- pct_female: 50.0 — Page 9, Table 1 — «Gender Men 51 50.0 | Women 51 50.0»
- mode: online — Page 7, Procedure — «The questionnaire was designed in the form of a Google Form ... in some instances, the researcher asked the participant(s) to use the same form in person.»
- attention_checks: yes — Page 5, Sample; Page 7, Procedure — «as were those who forgot to mark more than 10% of the items on either of the scales ... checked for missing data and 102 forms were kept for analysis as they w…»
- pub_status: journal — Page 1, header — «Perspectives in Social Sciences ISSN Online: 3106-8464 ... Original Article»
- language: English — Full text — «GENERATIVE AI DEPENDENCY AND DECISION-MAKING STYLES: A PREDICTIVE STUDY OF ADULTS IN PAKISTAN»
- funding_coi: NR — NA — «NR»
- notes: Mode: the abstract/Sample say 'online form and face-to-face method', but Procedure says the same Google Form was completed in person, so coded online; reviewer may prefer mixed. Attention checks coded yes only because of a stated missing-data exclusion rule (>10% unanswered items); there were no attention-check items or careless-responding screening, so reviewer may prefer NR. Sampling was purposive (non-probability), coded convenience. Age given only in bands (73.5% aged 20–30).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive non-probability sample recruited through academic, professional and social networks. — Page 5, Sample; Page 7, Procedure — «obtained purposively from Rawalpindi and Islamabad ... distributed via academic, professional and social networks»
2. отклик: **unclear** — No response rate and no comparison of non-responders reported. — Page 7, Procedure — «Data from completed forms were checked for missing data and 102 forms were kept for analysis as they were fully usable.»
3. валидная шкала зависимости от ИИ: **yes** — GAIDS has a published development and validation study (Goh et al., 2025). — Page 6, Assessment Measures — «Goh et al. (2025) have developed and validated the GAIDS, which measures the dependency on generative AI.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .90 in this sample. — Page 6; Page 10, Table 2 — «the current sample had a Cronbach's alpha value of .90»
5. валидные шкалы коррелятов: **yes** — The extracted correlate (MDMQ procrastination) comes from a published instrument (Mann et al., 1997). — Page 6, Assessment Measures — «The MDMQ (Mann et al., 1997) consists of 22 items that are divided into 4 patterns of coping with decisional conflict»
6. качество данных: **yes** — There was a stated exclusion rule for incomplete responses (>10% missing). There was no attention-check or careless-responding screening, so this rating is borderline. — Page 5, Method, Sample — «as were those who forgot to mark more than 10% of the items on either of the scales»

Правки:
- 

Проверено: да

---

## ST026 · Hazem 2026 · Middle East Current Psychiatry

Основной отчёт R0953: [текст](../../fulltext/text/R0953.txt) · [PDF](../../fulltext/pdf/R0953.pdf) — «Problematic use of AI chatbots for mental health concerns among adolescent psychiatric outpatients: severity, impairment, and coping» — [DOI](https://doi.org/10.1186/s43045-026-00637-y)
Расхождения в тексте: The CIAT-10 vs loneliness rho (−0.037) is the same in Table 2 and in the Discussion. The abstract and abbreviations call the CIAT-10 the 'Concise internet Addiction Test for AI chatbots', while the Methods call it the 'Concise adapted internet Addiction Test'. The Key Points say greater severity was associated with 'greater avoidant coping' (Table 4 rho 0.287); avoidant coping is not in the final regression (Table 5). Zero-order correlations are reported only for the CIAT-10, not for the AIAT-20 total or the clinician-based classification (ADHOC_R0953_3), so no effects were extracted for those. Correlations not extracted because the construct is not in the dictionary: Family Satisfaction Scale (rho −0.344), Brief COPE composites and subscales (Table 4; spearman and partial), trust, daily use minutes, age. The CIAT-10–AIAT-20 correlation is Pearson 0.699 / Spearman 0.600.
Заметка ИИ: I extracted one eligible effect: CIAT-10 total × UCLA Loneliness, Spearman. Most of the reported correlates (coping, family satisfaction, trust) fit no key in the construct dictionary. The sampling/rob_1 'census' coding rests on consecutive clinic recruitment and should be checked by the reviewer.

### ST026-1 · Child and adolescent psychiatry outpatients, Gabès University Hospital, Tunisia, n=92
Отчёты: R0953 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | IAT_ADAPTED · total (T4) | **loneliness** · UCLA Loneliness Scale (Version 3), total score (20 items, A… | spearman | **−0.037** | **92** | 1 | Page 7, Table 2 | «UCLA Loneliness Scale total score / −0.037 (− 0.240 to 0.168) / 0.726» |

- E1: α ИИ 0.794, α коррелята NR; заметка: Exposure score is the CIAT-10 total (10-item short form of the AI-adapted IAT). 95% CI −0.240 to 0.168. n assumed to be 92 (complete-case analysis; n per correlation not stated). The value is also given in the Discussion (p. 10) as 'rho minus 0.037'.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.29 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 92** — Page 6, Results; Table 1 — «A total of 92 participants met the inclusion and exclusion criteria and were included (mean age 13.2 years, SD 1.1)»
- **population: clinical** — Page 3, Participants and recruitment procedure — «Eligible participants were children and adolescents attending routine outpatient consultations for a psychiatric complaint»
- **sampling: census** — Page 3, Participants and recruitment procedure — «Participants were recruited consecutively over the study period.»
- **ai_system: general_chatbot** — Page 3, Participants and recruitment procedure — «they used generative AI chatbots in relation to their psychiatric symptoms or mental health concerns»

**Остальные поля:**
- country: TUN — Page 3, Participants and recruitment procedure — «Child and Adolescent Psychiatry Outpatient Clinic, Gabès University Hospital, Tunisia, between July and December 2025»
- data_years: 2025 — Page 3, Study design and setting — «Participants were recruited consecutively over a 6-month period (from July to December 2025).»
- design: cross-sectional — Page 3, Study design and setting — «We conducted a cross-sectional, descriptive and analytical study in a child and adolescent outpatient psychiatry clinic in Tunisia.»
- clinical_group: Adolescent psychiatric outpatients (depressive disorders, ADHD, anxiety disorders, etc.) who use generative AI chatbots for mental health concerns — Page 6, Table 1 — «Depressive disorders 27 (29.3) | Attention-deficit/hyperactivity disorder (ADHD) 25 (27.2) | Anxiety disorders 22 (23.9)»
- age_mean: 13.2 — Page 6, Table 1 — «Age (year, mean, SD) 13.2 (1.1)»
- age_sd: 1.1 — Page 6, Table 1 — «Age (year, mean, SD) 13.2 (1.1)»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 60.9 — Page 6, Table 1 — «Female 56 (60.9)»
- mode: NR — Page 3, Participants and recruitment procedure — «one investigator led the clinical evaluation, including the assessment of chatbot use and psychiatric comorbidity, while the other investigator administered th…»
- attention_checks: NR — Page 6, Statistical analysis — «All analyses were conducted using complete-case data for each analysis/model, with two-sided α = 0.05.»
- pub_status: journal — Page 1, header — «Hazem et al. Middle East Current Psychiatry (2026) 33:31»
- language: English — Full text — «Problematic use of AI chatbots for mental health concerns among adolescent psychiatric outpatients: severity, impairment, and coping»
- funding_coi: No specific funding; authors declare no competing interests — Page 12, Funding; Competing interests — «This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. ... The authors declare no competing int…»
- notes: Population coded clinical (psychiatric outpatients, all minors; mean age 13.2) – reviewer may prefer 'adolescents'. Sampling coded census because of consecutive recruitment of all eligible clinic attenders; eligibility depended on self-disclosed chatbot use (233 new patients, 148 AI users, 122 used for mental health, 92 included). Primary AI-dependence score is CIAT-10 (10 items derived from the AIAT-20 in this sample). Questionnaires administered in Arabic (Brief COPE, UCLA translated); the article language is English. Mode of administration (paper vs electronic) not stated.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **yes** — Consecutive recruitment of all eligible patients at one clinic over 6 months (census of a defined clinical population); eligibility depended on self-disclosure, so the reviewer should check this rating. — Page 3, Study design and setting — «Participants were recruited consecutively over a 6-month period (from July to December 2025).»
2. отклик: **unclear** — No response rate reported. 92 of 122 mental-health chatbot users were included (75%), but the report does not separate exclusions for eligibility reasons from refusals. — Page 6, Sample characteristics — «148 reported using AI chatbots, and 122 reported using them in relation to mental health concerns. A total of 92 participants met the inclusion and exclusion c…»
3. валидная шкала зависимости от ИИ: **yes** — Adapted IAT; the CIAT-10 was derived and validated in this report (internal consistency, ROC discrimination against the clinician classification), though only in the same dataset. — Page 7, Measurement performance of the CIAT-10 — «Criterion-related discrimination against the clinician-based classification ... (AUC = 0.789, 95% ,bootstrap confidence interval 0.681–0.883), indicating good …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for the CIAT-10 in this sample is 0.794 (AIAT-20 0.888). — Page 7 — «the 10-item Concise Adapted internet Addiction Test for AI Chatbots (CIAT-10) showed acceptable to good internal consistency, as indexed by Cronbach's alpha (α…»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate is the UCLA Loneliness Scale Version 3, a published instrument (Arabic translation by forward–backward translation). — Page 5, Loneliness — «The UCLA Loneliness Scale Version 3 has well-established psychometric properties in the original validation work [21].»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported; only complete-case analysis is mentioned. — Page 6, Statistical analysis — «All analyses were conducted using complete-case data for each analysis/model»

Правки:
- 

Проверено: да

---

## ST027 · He 2026 · Research Square

Основной отчёт R0954: [текст](../../fulltext/text/R0954.txt) · [PDF](../../fulltext/pdf/R0954.pdf) — «Artificial Intelligence Dependency and Associated Factors Among Nursing Master's Students in China: A National Cross-Sectional Study» — [DOI](https://doi.org/10.21203/rs.3.rs-9626863/v1)
Расхождения в тексте: 1. The correlations in the text (p. 8) match Table 2 for all reported variables. 2. Table 2 is cut off on the right (columns after Achievement Motivation are missing), but the AI Dependency column is complete. 3. Table 3 gives a negative B for 'Frequency of AI Tool Use' (-0.880, β = -0.099), while the text and abstract describe frequent AI use as a positive predictor. This may depend on how the frequency variable was coded; not relevant to the zero-order effects. 4. The text says the AICD was developed by Zhang Xing et al. 'in 2024', but reference 26 is dated 2025. 5. The 'valid response rate of 96.46%' is valid questionnaires divided by collected questionnaires, not a response rate among invited students. 6. The reliability values in the methods (AICD 0.88, research self-efficacy 0.913, TIPI 0.60–0.67, SCS 0.862) seem to describe the instruments in earlier studies, not this sample.
Заметка ИИ: One sample; 11 zero-order correlations extracted (AICD total with research self-efficacy, the five TIPI traits and the five SCS subscales). Achievement motivation was not extracted because it fits no dictionary construct. Multivariable regression betas were not extracted.

### ST027-1 · Nursing master's students, 6 universities in 4 provinces, China, n=436
Отчёты: R0954 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **self_efficacy** · Research Self-Efficacy Scale (Zhang et al., 2013; 3 items) | pearson | **-0.025** | **436** | 1 | Table 2, p. 8 | «Research Self-Efficacy / -0.025 / 1» |
| E2 | AICD · total (T4) | **extraversion** · TIPI (Chinese version) Extraversion | pearson | **0.015** | **436** | 1 | Table 2, p. 8 | «Extraversion / 0.015 / 0.231** / 1» |
| E3 | AICD · total (T4) | **agreeableness** · TIPI (Chinese version) Agreeableness | pearson | **-0.119** | **436** | 1 | Table 2, p. 8 | «Agreeableness / -0.119* / 0.140** / -0.080 / 1» |
| E4 | AICD · total (T4) | **conscientiousness** · TIPI (Chinese version) Conscientiousness | pearson | **-0.202** | **436** | 1 | Table 2, p. 8 | «Conscientiousness / -0.202** / 0.326** / 0.097* / 0.302** / 1» |
| E5 | AICD · total (T4) | **neuroticism** · TIPI (Chinese version) Emotional Stability | pearson | **-0.169** | **436** | 1 | Table 2, p. 8 | «Emotional Stability / -0.169** / 0.322** / 0.145** / 0.287** / 0.360** / 1» |
| E6 | AICD · total (T4) | **openness** · TIPI (Chinese version) Openness to Experience | pearson | **-0.136** | **436** | 1 | Table 2, p. 8 | «Openness to Experience / -0.136** / 0.265** / 0.232** / 0.175**» |
| E7 | AICD · total (T4) | **self_control** · Self-Control Scale (Chinese version, Tan & Guo) Impulse Con… | pearson | **-0.294** | **436** | 1 | Table 2, p. 8 | «Impulse Control / -0.294** / 0.145** / -0.075 / 0.373**» |
| E8 | AICD · total (T4) | **self_control** · Self-Control Scale (Chinese version) Healthy Habits | pearson | **-0.240** | **436** | 1 | Table 2, p. 8 | «Healthy Habits / -0.240** / 0.072 / 0.107* / 0.087» |
| E9 | AICD · total (T4) | **self_control** · Self-Control Scale (Chinese version) Resistance to Temptati… | pearson | **-0.072** | **436** | 1 | Table 2, p. 8 | «Resistance to Temptation / -0.072 / 0.302** / 0.083 / 0.217**» |
| E10 | AICD · total (T4) | **self_control** · Self-Control Scale (Chinese version) Focus on Work | pearson | **-0.243** | **436** | 1 | Table 2, p. 8 | «Focus on Work / -0.243** / 0.145** / 0.029 / 0.171**» |
| E11 | AICD · total (T4) | **self_control** · Self-Control Scale (Chinese version) Moderation of Entertai… | pearson | **-0.246** | **436** | 1 | Table 2, p. 8 | «Moderation of Entertainment / -0.246** / 0.075 / 0.039 / 0.129**» |

- E1: заметка: Research-specific self-efficacy. The report gives alpha 0.913, but it is unclear whether this was computed in this sample. AICD alpha 0.88 may come from the original study. Correlation method not stated.
- E2: заметка: The TIPI subscale alphas of 0.60–0.67 are likely from the original validation, not this sample.
- E5: **направление: reversed**; заметка: Emotional stability: higher scores mean lower neuroticism.
- E7: заметка: SCS subscale; higher scores mean better self-control. The SCS alpha of 0.862 is for the Chinese version, apparently not this sample.
- E8: заметка: SCS subscale
- E9: заметка: SCS subscale
- E10: заметка: SCS subscale
- E11: заметка: SCS subscale

**⚠ Проверка скриптом (обратите внимание):**
- E5: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление

**Ключевые поля выборки:**
- **n_analysed: 436** — p. 4, 3.1 — «A total of 452 questionnaires were collected, of which 16 were excluded as invalid. A total of 436 valid questionnaires were included»
- **population: university_students** — p. 3, 2.2 Participants — «students enrolled in nursing master's programs from the 2023 to 2025 cohorts, including full-time students, part-time students»
- **sampling: convenience** — p. 3, 2.2 Participants — «Participants were recruited using a convenience sampling method.»
- **ai_system: general_chatbot** — p. 4, 2.3.6; p. 2 Introduction — «designed to assess individuals' level of dependence on AI chatbots (e.g., ChatGPT) in daily life»

**Остальные поля:**
- country: CHN — p. 3, 2.2 Participants — «Nursing master's students from six universities in four provinces of China were enrolled between October and December 2025.»
- data_years: 2025 — p. 3, 2.2 Participants — «enrolled between October and December 2025»
- design: cross-sectional — p. 3, 2.1 Study Design — «This study used a cross-sectional observational survey design and adopted a convenience sampling method.»
- clinical_group: NA — NA — «NA»
- age_mean: 24.63 — p. 4, 3.1 — «ranged from 20 to 45 years, with an average of 24.63 ± 3.23 years»
- age_sd: 3.23 — p. 4, 3.1 — «with an average of 24.63 ± 3.23 years»
- age_min: 20 — p. 4, 3.1 — «ranged from 20 to 45 years»
- age_max: 45 — p. 4, 3.1 — «ranged from 20 to 45 years»
- pct_female: 82.34 — p. 4, 3.1; Table 1 — «Most participants were female (82.34%)»
- mode: online — p. 4, 2.4 Data Collection — «Data were collected through an online survey. The questionnaire was designed and distributed via Wenjuanxing»
- attention_checks: NR — p. 4, 2.4 and 3.1 — «A total of 452 questionnaires were collected, of which 16 were excluded as invalid.»
- pub_status: preprint — p. 1 — «Posted Date: May 26th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-9626863/v1»
- language: English — whole text — «Artificial Intelligence Dependency and Associated Factors Among Nursing Master's Students in China: A National Cross-Sectional Study»
- funding_coi: Zhejiang Province Health and Industry Science and Technology Program (2025HY0459); authors declare no competing interests — p. 11, Declarations — «This work was supported by the Zhejiang Province Health and Industry Science and Technology Program (grant number 2025HY0459). ... The authors declare that the…»
- notes: ai_system: the dependence scale refers to AI chatbots (e.g., ChatGPT), but the use questions ask about 'AI tools' in research (literature search, drafting, data analysis), so the reviewer may prefer ai_unspecified or mixed. 16 of 452 questionnaires were excluded as invalid, but no criteria are given, so attention_checks is NR. The report does not say which correlation method was used; coefficients are labelled 'r', so they are coded Pearson. Achievement motivation (AMS, r = -0.155) is not extracted because it fits no dictionary key. The SCS total is not reported; only the five subscales are g…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from six universities, recruited online through Wenjuanxing — p. 3, 2.2 — «Participants were recruited using a convenience sampling method.»
2. отклик: **unclear** — The reported 96.46% is valid questionnaires divided by questionnaires collected (436/452). The number of students invited is not reported, so a true response rate cannot be determined. — p. 4, 3.1 — «A total of 452 questionnaires were collected, of which 16 were excluded as invalid. A total of 436 valid questionnaires were included, yielding a valid respons…»
3. валидная шкала зависимости от ИИ: **yes** — The AI Chatbot Dependency Scale has a published development and validation study (Zhang et al., 2025, Cyberpsychol Behav Soc Netw) — p. 4, 2.3.6; ref 26 — «ZHANG X, YIN M, ZHANG M, et al. The Development and Validation of an Artificial Intelligence Chatbot Dependence Scale [J]. Cyberpsychol Behav Soc Netw. 2025;28…»
4. надёжность шкалы ИИ в выборке: **unclear** — An alpha of 0.88 appears in the instrument description next to the citation of the original scale. It is not clear whether it was computed in this sample. — p. 4, 2.3.6 — «The Cronbach's alpha of the scale is 0.88, indicating good reliability and validity.»
5. валидные шкалы коррелятов: **yes** — All extracted correlates were measured with published instruments: the Research Self-Efficacy Scale (Zhang 2013), the Chinese TIPI (Li 2013) and the Chinese SCS (Tan & Guo 2008). — pp. 3-4, 2.3.2-2.3.5 — «The Self-Control Scale (SCS) was developed by Tangney et al. in 2004 and later translated and adapted into Chinese by Tan Shuhua and Guo Yongyu in 2008.»
6. качество данных: **unclear** — 16 questionnaires were excluded as invalid, but no criteria or attention checks are described. All items were mandatory and only one submission per person was allowed. — p. 4, 2.4; 3.1 — «All items in the questionnaire were set as mandatory. Each participant was allowed to submit the questionnaire only once.»

Правки:
- 

Проверено: да

---

## ST028 · Honggang 2026 · Scientific reports

Основной отчёт R0989: [текст](../../fulltext/text/R0989.txt) — «Technostress, digital fatigue, and AI dependency as antecedents of burnout and SDG-4 achievement in EFL classrooms.» — [DOI](https://doi.org/10.1038/s41598-026-45402-7)
Расхождения в тексте: (1) Group sizes: Methods and Table 1 give n=412 Chinese and 133 international students, but the MGA (Table 9) uses n=405 and 128, a total of 533. (2) AI Dependency means: Table 10 gives 3.72 (Chinese) and 3.85 (international), both above the pooled mean of 3.65 in Table 2, which is impossible. (3) Table 3 shows AI Dependency positively correlated with Technology Self-Efficacy (0.15) and SDG Achievement (0.22). This is the opposite sign to the other stressors, and the HTMT for that pair is 0.18. (4) Moderation: the text gives β = 0.18 but Table 8 gives 0.018. The text also points to the wrong tables ('As shown in Table 5' for direct effects; 'Table 6' for mediation). (5) Paths: the subgroup AI dependency → FLA paths (0.18 and 0.23) are both larger than the pooled path (0.15). (6) The DAI is called 'multidimensional' with 'α = 0.87–0.93 across subscales', yet it has 5 items and only a tot…
Заметка ИИ: One sample, one effect (AI dependency x foreign language anxiety, coded academic_stress). The HTMT ratio (0.33) and the SEM paths were not extracted. The internal inconsistencies listed in consistency_notes suggest the data quality of this report should be checked.

### ST028-1 · EFL university students, four public universities, China (Chinese + international), n=545
Отчёты: R0989 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **academic_stress** · Foreign Language Learning Anxiety scale (adapted from Bries… | pearson | **0.29** | **545** | 1 | Table 3 | «3. AI Dependency / 0.42** / 0.38** / 1 ... 4. Foreign Language Anxiety / 0.51** / 0.55** / 0.29** / 1» |

- E1: α ИИ 0.86, α коррелята 0.91; заметка: Coding decision for the reviewer: foreign language (classroom) anxiety is a domain-specific academic anxiety that includes a test-anxiety subscale. The dictionary sends academic and test anxiety to academic_stress, not to anxiety, so it is coded here. The n of Table 3 is not stated; N=545 assumed. …

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.15, 0.42 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 545** — Methodology, Participants and sampling; Table 1 — «The final sample comprised N = 545 participants»
- **population: university_students** — Methodology, Participants and sampling — «n = 412 Chinese domestic EFL students and n = 133 international students enrolled in English-taught programs»
- **sampling: probability** — Methodology, Participants and sampling — «Participants were recruited via a stratified random sampling approach, with stratification based on three criteria»
- **ai_system: ai_unspecified** — Literature review, Perceived AI dependency, digital fatigue and technostress — «perceived AI dependency the sense of reliance on AI tools for learning tasks»

**Остальные поля:**
- country: CHN — Methodology, Participants and sampling — «university-level EFL learners engaged in technology-mediated language learning across four major public universities in China»
- data_years: NR — NA — «NR»
- design: cross-sectional — Methodology, Research design — «This study employs a quantitative, cross-sectional research design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 60.2 — Table 1 — «Gender | Female | 328 | 60.20»
- mode: mixed — Methodology, Data collection procedures — «The main data collection was administered through both online and paper-based surveys across the four participating universities»
- attention_checks: yes — Methodology, Data collection procedures — «all collected data underwent rigorous screening for missing values, outliers, and response patterns»
- pub_status: journal — Header — «Scientific reports; DOI: 10.1038/s41598-026-45402-7»
- language: English — Full text — «Technostress, digital fatigue, and AI dependency as antecedents of burnout and SDG-4 achievement in EFL classrooms»
- funding_coi: NR (no funding or competing-interest statement in the supplied text) — NA — «NR»
- notes: The authors call the sampling stratified random, but they describe no sampling frame, so it is coded 'probability' as stated and rob_1 is rated unclear. Age and data-collection years are not reported. The DAI is described as 'multidimensional' but has 5 items, and only a total score is reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The authors call it stratified random sampling, but they describe no sampling frame, selection procedure or response rate. One stratum is self-reported digital tool use, so a true probability sample is doubtful. — Methodology, Participants and sampling — «Participants were recruited via a stratified random sampling approach, with stratification based on three criteria to ensure representativeness»
2. отклик: **unclear** — No response rate or number invited is reported. — Methodology, Participants and sampling — «The final sample comprised N = 545 participants»
3. валидная шкала зависимости от ИИ: **yes** — The scale is a published instrument (Morales-García et al.) and the report cites previous psychometric evidence. — Methodology, Perceived AI dependency — «This study employed the multidimensional scale developed by Morales-García et al.39 to assess students' Perceived AI Dependency in education, this scale has 5 …»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha is .86 and CR is .88 in this sample. — Table 5 — «3. Perceived AI Dependency | 0.88 | 0.71 | 0.86»
5. валидные шкалы коррелятов: **yes** — The extracted correlate (FLLA) uses a scale adapted from a published instrument (Briesmaster & Briesmaster-Paredes). — Methodology, Foreign language learning anxiety (FLLA) — «Foreign language learning anxiety was measured using a validated scale adapted from Briesmaster and Briesmaster-Paredes40»
6. качество данных: **yes** — The report states screening for response patterns, but gives no criteria and no number excluded. — Methodology, Data collection procedures — «all collected data underwent rigorous screening for missing values, outliers, and response patterns»

Правки:
- 

Проверено: да

---

## ST029 · Hou 2026 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R1000: [текст](../../fulltext/text/R1000.txt) — «AI Dependence and Self-Reported Creativity Among Chinese College Students: The Roles of Motivation for AI Use and Perceived AI Literacy.» — [DOI](https://doi.org/10.3390/bs16091712)
Расхождения в тексте: Some text and Table 4 values differ slightly (not extracted effects). Social motivation index of moderated mediation: text 95% CI [−0.007, −0.0003], Table 4 [−0.007, −0.0004]. Instrumental motivation index: text CI [−0.0014, 0.0004], Table 4 [−0.001, 0.0004]. The text's escape-path contrast low vs high (contrast = 0.005, CI [0.002, 0.019]) looks internally odd. Social motivation's indirect effect has a different sign in the two models: negative in the parallel mediation (Table 2), positive in the moderated model (Table 4). The text's description of Table 1 correlations (AI literacy and creativity negatively related to AI dependence, escape and social motivation) matches the table. Gender percentages use 5760 as denominator, not the analytic n of 5764. Supplementary Tables S1–S2 were not available.
Заметка ИИ: There is only one eligible effect: AI dependence (HUANG5 total) with escape motivation (escapism_motive), r = 0.62, n = 5764. The other Table 1 variables (social, instrumental and entertainment motivation, AI literacy, self-reported creativity) have no key in the construct dictionary.

### ST029-1 · Chinese college students, 37 universities, CHN, n=5764
Отчёты: R1000 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | HUANG5 · total (T1) | **escapism_motive** · Revised AI Use Motivation Scale (Huang et al., 2024), Escap… | pearson | **0.62** | **5764** | 1 | Table 1 | «2. Escape motivation / 1.47 / 0.58 / 0.62 *** / 1 /» |

- E1: α ИИ omega = 0.889, α коррелята omega = 0.929; заметка: Table gives two decimals only. The report calls these 'bivariate correlation analyses' without naming the coefficient; Pearson assumed. Correlations are presumably pooled over multiply imputed data.

**Ключевые поля выборки:**
- **n_analysed: 5764** — 2.1. Participants and Procedure — «resulting in a final analytic sample of 5764 participants (97.43% of the initial sample)»
- **population: university_students** — 2.1. Participants and Procedure — «full-time undergraduate and graduate students»
- **sampling: convenience** — 2.1. Participants and Procedure — «A convenience sampling strategy, supplemented by snowball recruitment, was employed.»
- **ai_system: ai_unspecified** — 2.2.1. AI Dependence; 1. Introduction — «"I have tried to reduce the amount of time I spend on AI but failed" and "I feel anxious and upset when I cannot use artificial intelligence."»

**Остальные поля:**
- country: CHN — 2.1. Participants and Procedure — «The sample covered 37 universities across various regions, including Beijing, Shanghai, Zhengzhou, Guiyang, and other cities.»
- data_years: 2024 — 2.1. Participants and Procedure — «The study targeted full-time undergraduate and graduate students enrolled in the fall semester of 2024.»
- design: cross-sectional — 4.8. Limitations — «First, the cross-sectional design prevents causal conclusions.»
- clinical_group: NA — NA — «NA»
- age_mean: 20.87 — 2.1. Participants and Procedure — «Participants ranged in age from 16 to 38 years (M = 20.87, SD = 2.44).»
- age_sd: 2.44 — 2.1. Participants and Procedure — «Participants ranged in age from 16 to 38 years (M = 20.87, SD = 2.44).»
- age_min: 16 — 2.1. Participants and Procedure — «Participants ranged in age from 16 to 38 years»
- age_max: 38 — 2.1. Participants and Procedure — «Participants ranged in age from 16 to 38 years»
- pct_female: 70.80 — 2.1. Participants and Procedure — «Demographic information was available for 5760 participants. Of these participants, 1668 were male (28.96%), 4078 were female (70.80%)»
- mode: mixed — 2.1. Participants and Procedure — «using both paper-based administration and online surveys»
- attention_checks: yes — 2.1. Participants and Procedure — «Cases with extreme values (|Z| > 4) on key study variables, including completion time, age, and scale scores, were excluded (n = 147). An additional five cases…»
- pub_status: journal — Header — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs16091712»
- language: English — Full text — «AI Dependence and Self-Reported Creativity Among Chinese College Students»
- funding_coi: National Social Science Fund of China (EEA240407); Social Science Planning Project of Henan Province (2025CJY079); authors declare no conflicts of interest — Funding Statement; Conflicts of Interest — «This research was funded by the National Social Science Fund of China (EEA240407) and the Social Science Planning Project of Henan Province (2025CJY079). ... T…»
- notes: Only one correlate in Table 1 maps to the construct dictionary: escape motivation (AI Use Motivation Scale, Huang et al., 2024) -> escapism_motive. Social, instrumental and entertainment motivation, perceived AI literacy and self-reported creativity have no dictionary key and were not extracted. 440/5916 questionnaires were paper-based. Missing data (<20%) handled by multiple imputation. AI system not named for participants; the introduction refers to 'general AI' and conversational AI in general terms.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sampling supplemented by snowball recruitment through personal contacts. — 2.1. Participants and Procedure — «A convenience sampling strategy, supplemented by snowball recruitment, was employed. Questionnaires were distributed and organized through classmates, colleagu…»
2. отклик: **unclear** — No response rate reported; 97.43% is the share of collected questionnaires retained after screening, not a response rate. — 2.1. Participants and Procedure — «A total of 5916 questionnaires were initially collected.»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Huang et al., 2024) adapted from revised Smartphone Addiction Scale; CFA, CR and AVE reported in this sample. — 2.2.1. AI Dependence — «AI dependence was measured using the Chinese version AI Dependence Scale adapted by Huang et al. (2024) ... The standardized factor loadings of all items range…»
4. надёжность шкалы ИИ в выборке: **yes** — McDonald's omega = 0.889 in this sample. — 2.2.1. AI Dependence — «In the present study, McDonald's omega for the scale was 0.889.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (escape motivation) is measured with the published AI Use Motivation Scale (Huang et al., 2024). — 2.2.3. Motivation for AI Use — «Motivation for AI use was measured using the Chinese version revised AI Use Motivation Scale developed by Huang et al. (2024).»
6. качество данных: **yes** — Stated rule excluding extreme values, including completion time, plus data-entry errors; there were no explicit attention-check items. — 2.1. Participants and Procedure — «Cases with extreme values (|Z| > 4) on key study variables, including completion time, age, and scale scores, were excluded (n = 147).»

Правки:
- 

Проверено: да

---

## ST030 · Huang 2026 · Frontiers in psychology

Основной отчёт R1025: [текст](../../fulltext/text/R1025.txt) · [PDF](../../fulltext/pdf/R1025.pdf) — «The dark side of AI in education: AI dependency as a mediator linking academic self-efficacy and teacher support to learning burnout among university students.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1889053)
Расхождения в тексте: (1) Table 3 Panel A is labelled the Fornell–Larcker criterion, but its footnote says the off-diagonal values are Pearson correlations. Its values (−0.424, −0.217) match Table 4 (−0.42, −0.22) to rounding, so each pair is extracted once, as Pearson, from Table 4, the descriptive correlation table. (2) The AI Dependency Scale is described twice in Section 3.2 with different example items: 'I often use AI tools when completing coursework' and 'I often find myself relying on AI tools more than intended when completing coursework'. (3) Table 7 gives the direct effect of teacher support on burnout as −0.057, while the text in 4.5 gives B = −0.089 for the partial mediation model. (4) The standardized β = −0.424 for academic self-efficacy is reported with 95% CI [−0.603, −0.359], which does not appear to be on the standardized scale. (5) HTMT ratios (Table 3 Panel B) and regression/mediation co…
Заметка ИИ: Two eligible effects were extracted, both pairing the AI dependency total score with a correlate. The teacher support → social_support mapping needs the reviewer's decision. Learning burnout, the main outcome, is not in the construct dictionary and was not extracted.

### ST030-1 · Undergraduates, several comprehensive universities, Chengdu, China (n=276)
Отчёты: R1025 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | IAT_ADAPTED · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale (Owen & Froman, 1988; 8 items,… | pearson | **−0.42** | **276** | 1 | Page 7, Table 4 | «2. Academic self-eﬃcacy / 3.49 / 0.69 / −0.42∗∗ / (0.87)» |
| E2 | IAT_ADAPTED · total (T4) | **social_support** · Teacher Support Scale (Skinner & Belmont, 1993; 10 items) | pearson | **−0.22** | **276** | 1 | Page 7, Table 4 | «3. Teacher support / 3.59 / 0.76 / −0.22∗∗ / 0.51∗∗ / (0.91)» |

- E1: α ИИ 0.864, α коррелята 0.874; заметка: Table 3 Panel A (footnote: off-diagonal values are Pearson correlations) gives −0.424 for the same pair. ASE items refer to learning without AI tools.
- E2: α ИИ 0.864, α коррелята 0.915; заметка: Eligibility uncertain: perceived teacher support (one specific source; structure/involvement/autonomy support) rather than general perceived social support. Table 3 Panel A gives −0.217.

**Ключевые поля выборки:**
- **n_analysed: 276** — Page 4, 3.1 — «276 valid questionnaires were retained for subsequent analysis»
- **population: university_students** — Page 4, 3.1 — «participants recruited from undergraduate students enrolled in selected courses»
- **sampling: convenience** — Page 4, 3.1 — «A convenience sampling approach was adopted»
- **ai_system: ai_unspecified** — Page 4, 3.1; Page 5, 3.2 — «0.72% of participants reported rarely using AI tools (e.g., ChatGPT, DeepSeek, Doubao)»

**Остальные поля:**
- country: CHN — Page 4, 3.1 Participants and procedures — «participants recruited from undergraduate students enrolled in selected courses at several comprehensive universities in Chengdu, China.»
- data_years: NR — Page 4, 3.1 — «The questionnaire was distributed electronically during the data collection period»
- design: cross-sectional — Page 4, 3.1 — «This study adopted a cross-sectional research design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 4, 3.1 — «NR»
- age_sd: NR — Page 4, 3.1 — «NR»
- age_min: NR — Page 4, 3.1 — «NR»
- age_max: NR — Page 4, 3.1 — «NR»
- pct_female: 44.2 — Page 4, 3.1 — «154 (55.80%) were male and 122 (44.2%) were female»
- mode: online — Page 4, 3.1 — «An online structured questionnaire survey was conducted using the Questionnaire Star platform (www.wjx.cn)»
- attention_checks: yes — Page 4, 3.1 — «Attention check questions (e.g., "Please select strongly agree in this question.") were included in the questionnaire»
- pub_status: journal — Page 1 — «TYPE Original Research ... Front. Psychol. 17:1889053.»
- language: English — Full text — «The dark side of AI in education: AI dependency as a mediator linking academic self-eﬃcacy and teacher support to learning burnout among university students»
- funding_coi: Funded by Xihua University (Grants xjjg2023038, WX20260004); authors declare no conflict of interest. — Page 12, Funding; Conflict of interest — «This work was supported by Xihua University (Grant No. xjjg2023038 and Grant No. WX20260004). ... conducted in the absence of any commercial or ﬁnancial relati…»
- notes: AI dependency measured with a 7-item study-specific adaptation of Young's IAT (no subscales; the ADS-R subscales in the instrument list do not apply). Items refer to 'AI tools' for coursework; examples given to participants were ChatGPT, DeepSeek, Doubao, so general_chatbot is a plausible alternative code. Academic self-efficacy items were modified to refer to learning without AI (e.g., 'Even without using AI tools...'), which may overlap conceptually with the exposure. Learning burnout (MBI-SS short form) is not in the construct dictionary and was not extracted. Teacher support extracted und…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online via Wenjuanxing (Questionnaire Star) from selected courses. — Page 4, 3.1 — «A convenience sampling approach was adopted»
2. отклик: **yes** — 311 distributed, 311 returned, 276 valid; effective response rate 88.75% (>=60%). — Page 4, 3.1 — «A total of 311 questionnaires were distributed, of which 311 were returned. ... yielding an eﬀective response rate of 88.75%.»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc adaptation of IAT, but psychometric validation reported in this report (EFA/CFA loadings, CR = 0.874, AVE = 0.538, discriminant validity). Authors note content validity was not assessed via expert review or pilot. — Page 6, 4.2, Tables 1-2; Page 11 — «These results provide evidence of satisfactory reliability and convergent validity for all constructs, especially for the adapted AI Dependency Scale.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.864 in this sample. — Page 5, 3.2; Table 2 — «The Cronbach’s alpha for the AI Dependency Scale was 0.864.»
5. валидные шкалы коррелятов: **unclear** — Both correlates based on published instruments (Owen & Froman ASE; Skinner & Belmont teacher support), but ASE items were contextually modified to refer to AI without separate validation beyond this study's CFA. — Page 4, 3.2 — «several items were contextually modiﬁed to reﬂect students’ perceptions of autonomous learning without excessive dependency on AI assistance.»
6. качество данных: **yes** — Attention check items included; incomplete/invalid responses excluded. — Page 4, 3.1 — «Attention check questions (e.g., "Please select strongly agree in this question.") were included ... After excluding incomplete or invalid responses, 276 valid…»

Правки:
- 

Проверено: да

