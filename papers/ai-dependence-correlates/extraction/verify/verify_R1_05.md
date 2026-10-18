# Проверка выписывания — файл 5 из 13

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

## ST041 · Li 2026 · BMC psychology

Основной отчёт R1437: [текст](../../fulltext/text/R1437.txt) — «Task complexity and AI dependency among college students: the mediating roles of cognitive load, future anxiety, and task motivation.» — [DOI](https://doi.org/10.1186/s40359-026-04204-2)
Расхождения в тексте: (1) Table 6 gives the same values for TC as for TM (alpha 0.962, CR 0.965, AVE 0.635), but the text gives TC alpha = 0.890. This looks like a copy error in Table 6. (2) Table 3 p-values do not match the t values. AID t = 2.355 is printed with p = 0.610, but with df ≈ 440 that t gives p ≈ .02. So the stated lack of a gender difference in AID may be wrong. The same t (2.355) is printed as 'AID (p)' in Table 1. (3) Percent female is printed as 39.5% / 39.490%, but 175/442 = 39.6%. (4) Tables 4 and 5 are labelled 'M ± SD', but the spread values (about 0.07–0.14) look like standard errors. (5) In Table 11, the TM→AID CI is printed in reversed order (-0.131, -0.242). (6) The HTMT ratios (Table 8; AID–FA 0.719) were not extracted, as the rules require. (7) Other zero-order AID correlations (TM -0.146, CL 0.631, TC 0.636; latent -0.220, 0.648, 0.650) were not extracted because these constructs …
Заметка ИИ: One sample. Effects were extracted only for future anxiety, mapped to 'anxiety' with a note that the mapping is borderline. If the reviewer decides future anxiety does not fit 'anxiety', the study has no eligible effects. Sampling is coded as 'probability' because the authors describe randomly selecting classes. RoB item 1 is rated unclear because the universities were not randomly chosen and participation was through a voluntary online link.

### ST041-1 · Undergraduates at several Chinese universities, online survey 2025, n=442
Отчёты: R1437 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | HUANG5 · total (T1) | **anxiety** · Dark Future Scale (future anxiety, 5 items) | pearson | **0.648** | **442** | 1 | Table 2 | «AID / 2.851 ± 1.181 / -0.036 / -1.421 / -0.146** / 0.631*** / 0.648*** / 0.636*** / 1 (column FA)» |
| E2 | HUANG5 · total (T1) | **anxiety** · Dark Future Scale (future anxiety, 5 items) | latent | **0.666** | **442** | 1 | Table 7 (Fornell-Larcker criterion) | «FA / 0.666 / -0.521 / 0.741 / 0.870 /» |

- E1: α ИИ .896, α коррелята .920; заметка: Borderline mapping: future anxiety (worry about one's academic/career future, Dark Future Scale) is not generalised anxiety. Reviewer to confirm whether it fits 'anxiety' or should be excluded.
- E2: α ИИ .896, α коррелята .920; заметка: PLS-SEM latent construct correlation from the Fornell-Larcker table. Same borderline construct mapping as the Pearson row.

**Ключевые поля выборки:**
- **n_analysed: 442** — Table 2 — «The result of data's description and correlation analysis (n = 442)»
- **population: university_students** — Method, Participants — «Participants were full-time undergraduate students from several universities in China.»
- **sampling: probability** — Method, Procedure — «classes were randomly selected from the undergraduate population, and the survey link was distributed to these classes. Students who were willing to participate accessed the link»
- **ai_system: ai_unspecified** — Measurement tools — «AI dependency (AID), defined as students' tendency to rely excessively on AI tools to complete academic work and make learning-related decisions»

**Остальные поля:**
- country: CHN — Method, Procedure — «we used random sampling among full-time undergraduate students at several universities in China»
- data_years: 2025 — Method, Procedure — «Data were collected between February and April 2025 using an anonymous online questionnaire administered via Questionnaire Star (www.wjx.cn).»
- design: cross-sectional — Limitations and future research — «the dynamic process of how TC and AID change over time is not shown by this study because it is based on cross-sectional data.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Method, Participants — «136 participants were younger than 18 years (30.8%), 235 were between 18 and 22 years (53.1%), and 71 were older than 22 years (16.1%)»
- age_sd: NR — Method, Participants — «In terms of age, 136 participants were younger than 18 years (30.8%)»
- age_min: NR (only category 'younger than 18 years', n=136) — Table 1 — «Age | Under 18 years old | 136 | 30.790%»
- age_max: NR (only category 'older than 22 years', n=71) — Table 1 — «Over 22 years old | 71 | 16.130%»
- pct_female: 39.5 (as reported; 175/442 computes to 39.6) — Method, Participants; Table 1 — «267 male students (60.5%) and 175 female students (39.5%)»
- mode: online — Method, Procedure — «anonymous online questionnaire administered via Questionnaire Star (www.wjx.cn)»
- attention_checks: yes — Method, Procedure — «(3) implausibly short completion times, defined as less than one-third of the median completion time, which indicate insufficient effort responding»
- pub_status: journal — Title page — «BMC psychology; DOI: 10.1186/s40359-026-04204-2»
- language: English — Full text — «Task complexity and AI dependency among college students: the mediating roles of cognitive load, future anxiety, and task motivation»
- funding_coi: No funding; authors declare no competing interests — Funding; Competing interests — «No Funding. ... The authors declare no competing interests.»
- notes: 30.8% of the undergraduate sample reported being younger than 18 years; population coded university_students. 471 questionnaires returned, 442 retained after predefined exclusions (missing >20%, straightlining >=80% extreme responses, completion time < 1/3 median). AI tools not named (no specific chatbot). Only eligible correlate is future anxiety (Dark Future Scale); task motivation, cognitive load and task complexity fit no dictionary key and were not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Report states random selection of classes, but the universities ('several universities') are unnamed and not randomly chosen, participation was voluntary via an online Wenjuanxing link; reviewer to decide whether this c… — Method, Procedure — «With the assistance of student affairs staff and course instructors, classes were randomly selected from the undergraduate population, and the survey link was …»
2. отклик: **unclear** — Number of students invited not reported; only returned questionnaires (471) given, so no response rate can be computed. — Method, Procedure — «In total, 471 questionnaires were initially returned.»
3. валидная шкала зависимости от ИИ: **yes** — Five-item AI Dependence Scale of Huang et al. (2024), with published reliability and CFA evidence; CFA also reported in this sample. — Measurement tools — «measured using the five-item AI Dependence Scale reported by Huang et al. [23]... Huang et al. reported good psychometric properties for this scale»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .896 in this sample. — Measurement tools; Table 6 — «The scale showed good reliability in our data (Cronbach's α = 0.896).»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (future anxiety) was measured with the published Dark Future Scale (with slight wording adjustments). — Measurement tools — «Future anxiety (FA)... was assessed using the Dark Future Scale [45].»
6. качество данных: **yes** — Predefined invalid-response rules: missing data, straightlining, and short completion time. — Method, Procedure — «Predefined criteria were then applied to exclude invalid surveys: (1) questionnaires with more than five missing answers ... (3) implausibly short completion t…»

Правки:
- 

Проверено: да

---

## ST042 · Liu 2026 · BMC psychology

Основной отчёт R1470: [текст](../../fulltext/text/R1470.txt) — «Academic stress and university students' dependency on generative artificial intelligence: a multiple mediation model using PLS-SEM.» — [DOI](https://doi.org/10.1186/s40359-026-03986-9)
Расхождения в тексте: (1) Coefficients differ between Table 7 and Table 8. AS→PE is 0.632 in Table 7 but 0.732 in Table 8, with the same SE and CI. PE→GAID is 0.155 in Table 7 but 0.899 in Table 8 (CI 0.091:0.222). ACA→GAID is 0.124 vs 0.709, and DT→GAID is 0.115 vs 0.699. AS→ACA is 0.645 vs 0.605. In Table 7 the labels H2c and H3c are swapped relative to the hypotheses. (2) The text says construct means range from 3 to 4 and SDs from 0.7 to 0.9. Table 3 gives means of 3.772–4.390 and SDs up to 0.967. (3) Item counts in the text do not match Table 4. Academic stress is described as 5 items, but Table 4 shows AS1-4. Academic anxiety is described as 6 items, but Table 4 shows ACA1-4. Performance expectations are described as 5 items, but Table 4 shows PE2-PE7 (6 items). Desire thinking is described as 6 items, but Table 4 shows DT1-4. GAI dependency is described as 5 items, and Table 4 shows GAID1-4 and GAID6.…
Заметка ИИ: One cross-sectional sample. Two zero-order Pearson correlations were extracted, both coded academic_stress (academic stress and academic anxiety). Performance expectations and desire thinking were not extracted because they have no dictionary key. PLS-SEM paths, HTMT ratios and cross-loadings were not extracted.

### ST042-1 · Chinese university students, 9 comprehensive universities, Wenjuanxing online survey, n=622
Отчёты: R1470 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ACOSTA5 · total (T4) | **academic_stress** · Academic stress (AS), items adapted from Rustam and Tentama | pearson | **0.785** | **622** | 1 | Table 3 | «AS / 0.124** / 0.010 / 0.212** / 0.068 / 0.066 / 0.593** / 0.570** / 0.623** / 0.785** / 1» |
| E2 | ACOSTA5 · total (T4) | **academic_stress** · Academic anxiety (ACA), items adapted from Finch et al. | pearson | **0.611** | **622** | 1 | Table 3 | «GAI / 0.149** / 0.075 / 0.252** / 0.038 / 0.083* / 0.632** / 0.627** / 0.611** / 1» |

- E1: α ИИ 0.876, α коррелята 0.953; заметка: Value is in the AS row, GAI column; the matrix labels GAI dependency as 'GAI'. Table 4 lists 4 AS items (AS1-AS4), but the text says 5 items.
- E2: α ИИ 0.876, α коррелята 0.876; заметка: Coded academic_stress because the dictionary puts academic anxiety there; the reviewer should confirm. Table 4 lists 4 ACA items, but the text says six. This row and the AS row share the same construct key and the same sample, so they should not both be pooled as independent effects.

**Ключевые поля выборки:**
- **n_analysed: 622** — Data collection and participants; Table 1 — «This resulted in a final sample of 622 valid responses»
- **population: university_students** — Data collection and participants; Table 1 — «Recruitment was designed to reach a diverse pool of university students across institutions and academic backgrounds»
- **sampling: quota or online panel** — Data collection and participants — «Participants were recruited via Wenjuanxing (https://www.wjx.cn/), a widely used online questionnaire platform. The platform's random invitation function was used to distribute the survey link to registered users»
- **ai_system: general_chatbot** — Measurements — «respondents were instructed to consider their use of GAI tools when completing typical academic tasks, such as writing course assignments or reports, preparing presentations, studying for examinations»

**Остальные поля:**
- country: CHN — Data collection and participants — «Participants were recruited from comprehensive universities in China»
- data_years: 2025 — Data collection and participants — «Data for this study were collected through an online survey conducted in May 2025»
- design: cross-sectional — Common method bias; Limitations — «the data were collected through self-administered questionnaires at a single measurement occasion»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age | 18–19 | 186 | 30% ... 24–25 | 127 | 21%»
- age_sd: NR — Table 1 — «Age | 18–19 | 186 | 30%»
- age_min: 18 — Table 1 — «Age | 18–19 | 186 | 30%»
- age_max: 25 — Table 1 — «24–25 | 127 | 21%»
- pct_female: 43 — Table 1 — «Female | 266 | 43%»
- mode: online — Data collection and participants — «Data for this study were collected through an online survey conducted in May 2025»
- attention_checks: yes — Data collection and participants — «54 responses were excluded due to incompleteness (defined as more than 10% missing data) or patterned responding (e.g., uniform responses across all items)»
- pub_status: journal — Header — «Year: 2026; venue: BMC psychology; DOI: 10.1186/s40359-026-03986-9»
- language: English — Full text — «Academic stress and university students' dependency on generative artificial intelligence: a multiple mediation model using PLS-SEM»
- funding_coi: Macao Science and Technology Development Fund (FDCT) grants 0071/2023/RIB3, 0065/2024/RIB2; FDCT-GDST joint grant 0003-2024-AGJ. Authors declare no competing interests. — Funding; Competing interests — «The research was funded by the Macao Science and Technology Development Fund (FDCT) (Grant number 0071/2023/RIB3)... The authors declare no competing interests.»
- notes: GAI dependency: 5 items adapted from Acosta-Enriquez et al. [4], 5-point Likert; Table 4 lists items GAID1-4 and GAID6 (no GAID5). Respondents were asked about generative AI tools in general (ChatGPT is named only in the hypothesis rationale). Age was reported only in bands (18-25); the Table 3 'Age' mean of 1.037 is a coded value. Desire thinking and performance expectations have no dictionary key, so they were not extracted. Academic anxiety (Finch et al.) was coded academic_stress following the dictionary rule that test or academic anxiety goes under academic_stress.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Recruited through the Wenjuanxing online platform by random invitation of registered users. This is an online panel, not a probability sample. — Data collection and participants — «Participants were recruited via Wenjuanxing (https://www.wjx.cn/)... The platform's random invitation function was used to distribute the survey link to regist…»
2. отклик: **unclear** — The reported 92% is the share of valid questionnaires among those collected (622/676), not the share of invited people who responded. The number invited is not reported and non-responders were not compared. — Data collection and participants — «This resulted in a final sample of 622 valid responses, corresponding to a valid response rate of 92%.»
3. валидная шкала зависимости от ИИ: **yes** — Items were adapted from a published GAI dependency scale (Acosta-Enriquez et al.), and this report gives loadings, CR and AVE for the scale. — Measurements; Table 4 — «GAI dependency was measured using five items adapted from Acosta-Enriquez et al. [4]»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.876 in this sample. — Table 4 — «GAI Dependency (GAID): CA = 0.876, CR = 0.910, AVE = 0.670»
5. валидные шкалы коррелятов: **yes** — Both extracted correlates were adapted from published scales: academic stress from Rustam and Tentama, academic anxiety from Finch et al. — Measurements — «Students' academic stress was measured using five items adapted from Rustam and Tentama [51]... Academic anxiety was measured using a six-item scale adapted fr…»
6. качество данных: **yes** — States a rule for excluding incomplete and patterned (uniform) responses. — Data collection and participants — «54 responses were excluded due to incompleteness (defined as more than 10% missing data) or patterned responding (e.g., uniform responses across all items)»

Правки:
- 

Проверено: да

---

## ST043 · Liu 2026 · Frontiers in psychology

Основной отчёт R1474: [текст](../../fulltext/text/R1474.txt) · [PDF](../../fulltext/pdf/R1474.pdf) — «Are students dependent on AI in writing courses? Analyzing factors influencing dependence on generative AI through the I-PACE model.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1905037)
Не выписано ИИ: Pre-test sample of 52 students (used only to check item clarity; no correlations reported). Qualitative interview subsample (n = 8, drawn from the main sample; no quantitative data).
Расхождения в тексте: (1) The text (4.2) says inter-construct correlations ranged from −0.049 to 0.633, but Table 4 values range from −0.058 to 0.702; Table 4 values were used. (2) Table 1 gives first-year students as 30.1% (second-year 0%), but the text says '30.1% were second-year students'. (3) H6 SI→TR: the text gives β = 0.306, Table 6 gives 0.404. Table 6 H3 is printed as '−0.0.196'. (4) The ASE*PU interaction is −0.1732 in the text and −0.1733 in Table 8. (5) The PAS scale is cited as 'Dalia and Adel, 2015' in the text but as Bedewy & Gabriel (2015) elsewhere in the references. None of these discrepancies affects the extracted values.
Заметка ИИ: One pooled sample (n = 229) from two universities. Only two pairs are eligible: AI dependence with academic stress and with academic self-efficacy. Both come from a Fornell-Larcker discriminant-validity table and were coded as latent correlations. SEM paths, mediation and moderation effects were not extracted.

### ST043-1 · Undergraduate journalism students, two universities (Fujian & Guangdong), China, n=229
Отчёты: R1474 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **academic_stress** · Perceptions of Academic Stress (PAS) scale, 5 items (AS) | latent | **0.226** | **229** | 1 | Page 10, Table 4 | «AID / −0.058 / −0.006 / 0.163 / 0.226 / 0.343 / 0.093 / 0.752 (columns ASE, AIL, SI, AS, TR, PU, AID)» |
| E2 | BERGEN_ADAPTED · total (T1) | **self_efficacy** · Academic self-efficacy, 5 items adapted from Pintrich & De … | latent | **−0.058** | **229** | 1 | Page 10, Table 4 | «AID / −0.058 / −0.006 / 0.163 / 0.226 / 0.343 / 0.093 / 0.752 (columns ASE, AIL, SI, AS, TR, PU, AID)» |

- E1: α ИИ 0.901, α коррелята 0.830; заметка: Fornell-Larcker table (sqrt AVE on the diagonal), so the off-diagonal values are taken as CFA latent correlations; the report does not say this explicitly. No separate observed correlation matrix is reported.
- E2: α ИИ 0.901, α коррелята 0.925; заметка: Fornell-Larcker table, so the value is taken as a CFA latent correlation; the report does not say this explicitly. Academic self-efficacy here is a measure of general academic self-efficacy, not AI self-efficacy.

**Ключевые поля выборки:**
- **n_analysed: 229** — Page 8, 3.2 Measurements — «After screening, 229 valid samples were retained for analysis.»
- **population: university_students** — Page 6, 3.1 — «who are undergraduate students from a public university in Fujian Province, China, and undergraduate students from a university in Guangdong Province»
- **sampling: convenience** — Page 6, 3.1 — «This study uses the purposeful sampling method, recruiting a total of 266 participants»
- **ai_system: general_chatbot** — Page 6, 3.1 — «The teacher introduced some domestic AI tools that can be used directly, such as Douba, DeepSeek, and Kimi, and also introduced the popular foreign tool ChatGPT»

**Остальные поля:**
- country: CHN — Page 6, 3.1 Sampling and procedure — «undergraduate students from a public university in Fujian Province, China, and undergraduate students from a university in Guangdong Province, China»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 9, 4.2 Common method bias — «the common method bias in this batch of cross-sectional data»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 81.2 — Page 8, Table 1 — «Gender Male 43 18.8 Female 186 81.2»
- mode: online — Page 7, 3.1; Page 8, 3.2 — «participants immediately completing an online questionnaire after finishing the writing of the literature review»
- attention_checks: yes — Page 8, 3.2 — «four incomplete samples were excluded, seven samples with insufficient response time were excluded, and eight straight-line response samples were excluded»
- pub_status: journal — Page 1 — «TYPE Original Research PUBLISHED 11 September 2026 DOI 10.3389/fpsyg.2026.1905037»
- language: English — Page 1 — «Are students dependent on AI in writing courses? Analyzing factors influencing dependence on generative AI through the I-PACE model»
- funding_coi: No funding received; authors declare no conflict of interest — Page 15-16, Funding; Conflict of interest — «The author(s) declared that financial support was not received for this work and/or its publication.»
- notes: Two universities were recruited but analysed as one pooled sample (no separate analyses), so extracted as one sample. Participants all took the same course and received AI-tool training before the survey, which was given right after an in-class writing task. AI dependence: 7 items adapted from the Bergen Facebook Addiction Scale (Andreassen et al., 2012) and the LDS dependence scale. Only academic stress and academic self-efficacy match dictionary constructs. AI literacy, social influence, perceived trust and perceived usefulness are not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposeful (non-probability) sample of students in one course at two universities — Page 6, 3.1 — «This study uses the purposeful sampling method, recruiting a total of 266 participants»
2. отклик: **yes** — 248 of 266 invited students responded (93%); 229 valid (86%) — Page 8, 3.2 — «This study distributed questionnaires to 266 respondents through the Questionnaire Star platform. Among them, 18 respondents did not participate in answering.»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc adaptation of the Bergen/LDS items, but this report gives a CFA (loadings .518–.907, CR = .897, AVE = .566). The reviewer should check whether this counts as validation. — Page 9-10, 4.3; Table 3 — «AI dependence (AID) AID1 0.828 0.901 0.897 0.566»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .901 in this sample — Page 8, 3.2; Table 3 — «After measurement, this construct shows good reliability (α = 0.901).»
5. валидные шкалы коррелятов: **yes** — Academic stress from the published PAS scale; academic self-efficacy adapted from Pintrich & De Groot (1990) — Page 7-8, 3.2 — «Academic stress uses five items from the Perceptions of Academic Stress (PAS) scale (Dalia and Adel, 2015)»
6. качество данных: **yes** — Stated exclusion rules for missing data, straight-lining, short response time and logical inconsistency — Page 8, 3.2 — «we constructed a multi-level questionnaire quality monitoring system to screen out potential invalid feedback»

Правки:
- 

Проверено: да

---

## ST044 · Liu 2026 · Frontiers in psychology

Основной отчёт R1476: [текст](../../fulltext/text/R1476.txt) — «Association between perceived usefulness of generative AI for learning and generative AI dependency among university students in Changde, China: a cross-sectio…» — [DOI](https://doi.org/10.3389/fpsyg.2026.1859317)
Расхождения в тексте: The correlations in the text (GAID–AP r = 0.338; GAID–MSR r = −0.273) match Table 2. Perceived usefulness of generative AI (TAME-ChatGPT) is not a dictionary construct, so it was not extracted. Table 3 and Figure 2 give standardized betas from models with covariates and PROCESS paths; these were not extracted. The report names the GAIDS subscales 'cognitive distress' and 'withdrawal reactions', while the instrument list uses 'Cognitive preoccupation' and 'Withdrawal'. No subscale-level correlations are reported.
Заметка ИИ: One cross-sectional sample. Two effects extracted for the GAIDS total. The MSR→self_control mapping is borderline and needs the reviewer's decision.

### ST044-1 · University students, three institutions in Changde, Hunan, CHN (n = 1,869)
Отчёты: R1476 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **procrastination** · Academic Procrastination Scale-Short Form (Chinese version) | pearson | **0.338** | **1869** | 1 | Table 2 | «Academic procrastination (AP) / 3.63 / 0.69 / 0.324*** / −0.291*** / 1 / ... Generative AI dependency (GAID) / 3.46 / 0.61 / 0.314*** / −0.273*** / 0.338*** / 1» |
| E2 | GAIDS · total (T1) | **self_control** · MSLQ Metacognitive Self-Regulation subscale (Chinese versio… | pearson | **−0.273** | **1869** | 1 | Table 2 | «Generative AI dependency (GAID) / 3.46 / 0.61 / 0.314*** / −0.273*** / 0.338*** / 1» |

- E1: α ИИ NR, α коррелята 0.859; заметка: GAIDS total alpha not reported; subscale alphas .793, .822, .813. Text gives same value (r = 0.338).
- E2: α ИИ NR, α коррелята 0.923; заметка: BORDERLINE construct mapping: metacognitive self-regulation in learning (MSLQ) mapped to self_control ('self-regulation'); reviewer to confirm or drop. Course-anchored, 5-point format instead of original 7-point.

**⚠ Проверка скриптом (обратите внимание):**
- E2: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей

**Ключевые поля выборки:**
- **n_analysed: 1869** — Table 2, note — «N = 1869. Pearson correlations (two-tailed) are reported.»
- **population: university_students** — Methods, Participants — «being a currently enrolled undergraduate or postgraduate student at one of the three participating institutions; (2) being 18 years of age or older»
- **sampling: convenience** — Methods, Participants — «among undergraduate and postgraduate students from selected classes at three higher education institutions ... Anonymous online questionnaires were distributed via Wenjuanxing during students' after-class time, with the assistance of teachers from the selecte…»
- **ai_system: general_chatbot** — Methods, Participants; Measures, Generative AI dependency — «having used generative AI tools to assist learning within the past month ... participants were first asked to identify the generative AI tool they had used most frequently during the past month»

**Остальные поля:**
- country: CHN — Methods, Participants — «three higher education institutions in Changde, Hunan Province, China»
- data_years: 2026 — Methods, Participants — «This cross-sectional questionnaire survey was conducted from March 10 to March 20, 2026»
- design: cross-sectional — Methods, Participants — «This cross-sectional questionnaire survey was conducted from March 10 to March 20, 2026»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Methods, Participants — «273 participants were 18 years old (14.6%), 484 were 19 years old (25.9%), 563 were 20 years old (30.1%), and 549 were aged 21 years or older (29.4%)»
- age_sd: NR — Methods, Participants — «Age reported only in categories»
- age_min: 18 — Methods, Participants — «273 participants were 18 years old (14.6%)»
- age_max: NR — Methods, Participants — «549 were aged 21 years or older (29.4%)»
- pct_female: 54.0 — Methods, Participants — «860 were male (46.0%) and 1,009 were female (54.0%)»
- mode: online — Methods, Participants — «Anonymous online questionnaires were distributed via Wenjuanxing»
- attention_checks: yes — Methods, Participants — «an abnormally short completion time (less than 3 min), which was treated as indicating invalid or insufficiently engaged responding»
- pub_status: journal — Header (venue) — «Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1859317»
- language: English — Full text — «This cross-sectional questionnaire study surveyed 1,869 university students from three higher education institutions in Changde»
- funding_coi: No funding; authors declare no conflict of interest — Funding Statement; Conflict of interest — «financial support was not received for this work and/or its publication ... conducted in the absence of any commercial or financial relationships that could be…»
- notes: Generative AI tools unspecified (participants anchored responses to their most-used generative AI tool for learning); coded general_chatbot. GAIDS dimensions named in report as 'cognitive distress', 'negative consequences', 'withdrawal reactions'; only the total (mean of 11 items) is correlated. Alpha for the GAIDS total not reported (subscale alphas .793/.822/.813). Recruitment via Wenjuanxing with teacher assistance in selected classes; no clustering adjustment.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of selected classes, online survey via Wenjuanxing — Methods, Participants — «students from selected classes at three higher education institutions ... Anonymous online questionnaires were distributed via Wenjuanxing»
2. отклик: **yes** — 1,900 questionnaires distributed, 1,869 valid (98.37%); note this is reported as a valid questionnaire retention rate, the number of students invited is not separately reported — Methods, Participants — «A total of 1,900 questionnaires were distributed. After data screening, 1,869 valid questionnaires were retained, yielding a valid questionnaire retention rate…»
3. валидная шкала зависимости от ИИ: **yes** — Published Generative AI Dependency Scale (Goh et al., 2025); CFA in this sample — Measures, Generative AI dependency — «used the Chinese version of the Generative AI Dependency Scale ... (Goh et al., 2025) ... model fit was good, χ2/df = 1.782, RMSEA = 0.020, CFI = 0.996, and TL…»
4. надёжность шкалы ИИ в выборке: **yes** — Subscale alphas all ≥ .70 in this sample; alpha for the total score (used in correlations) not reported separately — Measures, Generative AI dependency — «Cronbach's alpha values for cognitive distress, negative consequences, and withdrawal reactions were 0.793, 0.822, and 0.813, respectively»
5. валидные шкалы коррелятов: **yes** — Academic Procrastination Scale-Short Form (Yockey, 2016) and MSLQ Metacognitive Self-Regulation subscale (Pintrich et al.) are published instruments (MSLQ adapted to 5-point format) — Measures, Academic procrastination; Metacognitive self-regu… — «Chinese version of the Academic Procrastination Scale-Short Form ... (Yockey, 2016)»
6. качество данных: **yes** — Stated rule excluding incomplete responses and completion time < 3 min — Methods, Participants — «an abnormally short completion time (less than 3 min), which was treated as indicating invalid or insufficiently engaged responding»

Правки:
- 

Проверено: да

---

## ST045 · Liu 2026 · Frontiers in psychiatry

Основной отчёт R1478: [текст](../../fulltext/text/R1478.txt) — «Differentiation under pressure: psychological pathways and latent profiles of GenAI dependence among graduate students.» — [DOI](https://doi.org/10.3389/fpsyt.2026.1894754)
Расхождения в тексте: The text and Table 1 agree (GenAI dependence with research anxiety: r = 0.524). Some Table 1 correlates were not extracted because no construct key clearly fits them: time pressure (r = 0.507; Maruping et al. scale, perceived lack of time for research tasks, alpha 0.746), performance expectancy (r = 0.472), critical thinking (r = 0.305) and research creativity (r = 0.342). The reviewer may want to decide whether time pressure counts as 'academic pressure' (academic_stress). If it does, the extra row would be: total x time pressure, r = 0.507, n = 1157, Table 1. No correlations are reported for the subscales (Functional dependence, Existential dependence). Mediation paths (PROCESS), LPA results and multinomial ORs were not extracted.
Заметка ИИ: This is a single cross-sectional sample with one eligible effect. Age statistics and funding/COI are not reported in the supplied text. The stated 'random sampling' is not backed by a described sampling frame.

### ST045-1 · Graduate students, multiple Chinese provinces (Shaanxi, Shandong, Fujian and others), online survey, n=1,157
Отчёты: R1478 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1478_1 · total (T4) | **academic_stress** · Research anxiety scale (adapted from Wang et al., 4 items) | pearson | **0.524** | **1157** | 1 | Table 1 | «4. GenAI dependence / 0.943 / 0.483 / 3.352 / 0.690 / 0.507** / 0.524** / 0.472** / 0.695» |

- E1: α ИИ 0.913, α коррелята 0.828; заметка: Research anxiety (anxiety about unfinished research tasks) is coded as academic_stress because the dictionary sends academic anxiety there; the reviewer should confirm. The coefficient is an observed correlation (SPSS). The diagonal of the matrix holds the square roots of AVE. Only the total score …

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.51 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 1157** — Table 1 note — «N = 1,157, **p < 0.01.»
- **population: university_students** — Research participants — «administer an online survey to graduate students from universities in Shaanxi, Shandong, Fujian and other provinces»
- **sampling: probability** — Research participants — «This study employed a random sampling method to administer an online survey to graduate students»
- **ai_system: general_chatbot** — Introduction — «Generative AI, exemplified by ChatGPT ... a continuum of reliance on generative AI tools in academic and research-related tasks.»

**Остальные поля:**
- country: CHN — Research participants — «graduate students from universities in Shaanxi, Shandong, Fujian and other provinces»
- data_years: NR — Research participants — «A total of 1,277 questionnaires were collected.»
- design: cross-sectional — Limitations and future research — «First, this study used a cross-sectional survey design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Research participants — «As all participants were graduate students aged 18 years or older»
- age_sd: NR — Research participants — «As all participants were graduate students aged 18 years or older»
- age_min: NR — Research participants — «As all participants were graduate students aged 18 years or older»
- age_max: NR — Research participants — «As all participants were graduate students aged 18 years or older»
- pct_female: 52.204 — Research participants — «there were 553 males (47.796%) and 604 females (52.204%)»
- mode: online — Research participants — «This study employed a random sampling method to administer an online survey»
- attention_checks: yes — Research participants — «After excluding invalid responses due to patterned answering, excessively short or long completion times, or failure to pass attention check questions, 1,157 v…»
- pub_status: journal — Bibliographic record — «venue: Frontiers in psychiatry; DOI: 10.3389/fpsyt.2026.1894754»
- language: English — Full text — «Differentiation under pressure: psychological pathways and latent profiles of GenAI dependence among graduate students»
- funding_coi: NR (no funding or conflict-of-interest statement in the supplied text) — NA — «NA»
- notes: Sampling is coded 'probability' only because the authors say 'random sampling'. No sampling frame is described and recruitment was online, so the reviewer should verify. The only age information is that all participants were 18 or older. The AI dependence scale (Li et al.) has 18 items in two dimensions (functional and existential dependence). Only the total score appears in Table 1.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The report says 'random sampling', but it describes no sampling frame or selection procedure, and recruitment was through an online survey. Whether this was really a probability sample cannot be checked. — Research participants — «This study employed a random sampling method to administer an online survey to graduate students from universities in Shaanxi, Shandong, Fujian and other provi…»
2. отклик: **unclear** — The 90.6% 'effective response rate' is the share of collected questionnaires that were valid. The number of people invited is not reported, so the true response rate is unknown. — Research participants — «A total of 1,277 questionnaires were collected. ... 1,157 valid questionnaires were obtained, yielding an effective response rate of 90.603%.»
3. валидная шкала зависимости от ИИ: **yes** — Uses the published AI dependence scale of Li et al. (37). A CFA in this sample showed good fit. — Research instruments — «Drawing on the AI dependence scale developed by Li et al. (37), this study employed an 18-item instrument ... (χ² = 676.92, df = 134, CFI = 0.95, TLI = 0.95, R…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.913 in this sample. — Research instruments — «In this study, the Cronbach's α coefficient for this scale was 0.913.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate is research anxiety, measured with a 4-item scale adapted from published work (Wang et al., 34). CFA and alpha are reported in this sample. The authors say further validation is needed. — Research instruments — «The research anxiety scale was adapted from Wang et al. (34) ... Cronbach's α for the scale was 0.828. Confirmatory factor analysis indicated acceptable model …»
6. качество данных: **yes** — Attention checks were used, and responses with patterned answering or extreme completion times were excluded. — Research participants — «excluding invalid responses due to patterned answering, excessively short or long completion times, or failure to pass attention check questions»

Правки:
- 

Проверено: да

---

## ST046 · Liu 2026 · Frontiers in human neuroscience

Основной отчёт R1489: [текст](../../fulltext/text/R1489.txt) — «Pathways linking AI dependence to psychological distress: the mediating role of self-esteem and the role of academic achievement.» — [DOI](https://doi.org/10.3389/fnhum.2026.1877234)
Лонгитюд (для описания): This is a three-wave time-lagged design, not a cross-lagged panel. AI dependence was measured only at T1 (November 2025), self-esteem and CGPA at T2 (February 2026), and psychological distress (K10) at T3 (May 2026). Each construct was measured once, so no autoregressive or cross-lagged paths were estimated. In PLS-SEM, standardised paths were: AD(T1) to PD(T3) beta = 0.284, 95% CI [0.223, 0.344]; AD(T1) to SE(T2) beta = −0.149, 95% CI [−0.223, −0.079]; SE(T2) to PD(T3) beta = −0.464. The indirect path AD to SE to PD was beta = 0.069, 95% CI [0.036, 0.105]. These are multivariable paths and were not extracted as effects.
Расхождения в тексте: Text and Table 2 agree on all correlations (AD–SE r = −0.082, p < .05; AD–PD r = 0.312, p < .001). HTMT values (AD–SE 0.165; AD–PD 0.351; Table 4) were not extracted, per the rules. No Fornell-Larcker or latent correlation table is reported. Figures 1 and 2 (models) were not available as text, and no coefficients are shown only in figures. The data availability statement mentions supplementary material, but none was provided. Alphas in the Method section agree with Table 3.
Заметка ИИ: There is one sample with two eligible zero-order correlations. Both are cross-occasion correlations (AD at T1 with self-esteem at T2, and with K10 distress at T3), because the design measured each construct only once.

### ST046-1 · Undergraduates, two universities, China, three-wave time-lagged survey (n = 865)
Отчёты: R1489 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_esteem** · Rosenberg Self-Esteem Scale | pearson | **−0.082** | **865** | lagged: T1-T2 | Table 2 | «3. SE / 30.72 ± 4.67 / 0.195** / −0.082* /» |
| E2 | DAI · total (T4) | **distress** · Kessler Psychological Distress Scale (K10) | pearson | **0.312** | **865** | lagged: T1-T3 | Table 2 | «4. PD / 22.66 ± 7.76 / −0.057 / 0.312** / −0.485**» |

- E1: α ИИ 0.799, α коррелята 0.896; заметка: AI dependence measured at T1, self-esteem at T2; no same-occasion correlation exists because each construct was measured once.
- E2: α ИИ 0.799, α коррелята 0.950; заметка: AI dependence measured at T1, K10 at T3; no same-occasion correlation exists because each construct was measured once.

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 865** — Table 1; Method, Participants and sampling — «865 participants aged 18–24 years provided complete and valid data across all waves and formed the analytic sample»
- **population: university_students** — Method, Participants and sampling — «Participants were eligible if they were enrolled as undergraduates, were aged 18 years or older»
- **sampling: convenience** — Method, Participants and sampling; Procedures — «Purposive sampling was used to recruit undergraduate students from two universities in China... participants were recruited through WeChat, QQ, and university learning management systems.»
- **ai_system: ai_unspecified** — Method, AI dependence; Abstract — «assesses reliance on AI for learning, decision-making, and academic tasks»

**Остальные поля:**
- country: CHN — Method, Participants and sampling — «Purposive sampling was used to recruit undergraduate students from two universities in China»
- data_years: 2025-2026 — Method, Research design — «AI dependence and demographic information at Time 1 (November 2025), self-esteem and CGPA at Time 2 (February 2026), and psychological distress at Time 3 (May …»
- design: other — Method, Research design — «This study used a three-wave time-lagged survey design... because each construct was measured once and no autoregressive or reciprocal paths could be estimated»
- clinical_group: NA — NA — «NA»
- age_mean: 19.56 — Table 1 — «Mean | 19.56 |»
- age_sd: 1.15 — Table 1 — «SD | 1.15 |»
- age_min: 18 — Method, Participants and sampling — «865 participants aged 18–24 years»
- age_max: 24 — Method, Participants and sampling — «865 participants aged 18–24 years»
- pct_female: 70.6 — Table 1 — «Female | 611 | 70.6»
- mode: online — Method, Procedures and attrition — «participants were recruited through WeChat, QQ, and university learning management systems. All participants completed the survey voluntarily after providing e…»
- attention_checks: yes — Method, Procedures and attrition — «Cases were excluded if they could not be matched across waves or showed missing or inconsistent responses.»
- pub_status: journal — Header (venue) — «Frontiers in human neuroscience; DOI: 10.3389/fnhum.2026.1877234»
- language: English — Full text — «Pathways linking AI dependence to psychological distress: the mediating role of self-esteem and the role of academic achievement»
- funding_coi: Funded by Henan Provincial and Xinxiang University teaching reform/education/social science planning projects; authors declare no conflict of interest. — Funding Statement; Conflict of interest — «This work was supported by the 2026 Henan Provincial Higher Education Teaching Reform Research and Practice Project (Grant No. 2026SJGLX559)... conducted in th…»
- notes: Time-lagged design: AI dependence measured only at T1 (Nov 2025), self-esteem at T2 (Feb 2026), K10 distress at T3 (May 2026); each construct measured once, so all AD correlations are cross-occasion. Baseline n = 947; 82 (8.7%) lost. Chinese DAI version without back-translation or pilot. Ethics approval came from Universiti Putra Malaysia although data were collected in China. CGPA not extracted (not in the construct dictionary).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (non-probability) sampling with recruitment via WeChat/QQ/LMS. — Method, Participants and sampling — «Purposive sampling was used to recruit undergraduate students from two universities in China»
2. отклик: **unclear** — Initial response rate among invited students not reported; only retention reported (865/947, 91.3%), with no comparison of completers vs. dropouts. — Method, Procedures and attrition — «At Time 1, 947 students participated. A total of 865 students provided complete and valid data across all three waves, indicating an overall loss of 82 partici…»
3. валидная шкала зависимости от ИИ: **yes** — Published scale (Morales-García et al., 2024) with validation evidence; Chinese adaptation lacked back-translation/pilot, but the measurement model (loadings, CR, AVE) is reported for this sample. — Method, AI dependence — «The original scale demonstrated a unidimensional structure, satisfactory reliability, construct validity, and gender invariance in university students.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.799 in this sample. — Method, AI dependence; Table 3 — «a Chinese version was administered and showed acceptable internal consistency (Cronbach’s alpha = 0.799)»
5. валидные шкалы коррелятов: **yes** — Both correlates measured with published instruments (Rosenberg Self-Esteem Scale, K10). — Method, Instruments — «Psychological distress was assessed using the K10 (Kessler et al., 2002)... The Rosenberg Self-Esteem Scale (Rosenberg, 1965) was used»
6. качество данных: **yes** — Data quality screening stated, with exclusion of missing or inconsistent responses. — Method, Participants and sampling; Procedures and attrition — «After longitudinal matching and data quality screening, 865 participants... Cases were excluded if they could not be matched across waves or showed missing or …»

Правки:
- 

Проверено: да

---

## ST047 · Liu 2026 · Frontiers in Psychology

Основной отчёт R1490: [текст](../../fulltext/text/R1490.txt) · [PDF](../../fulltext/pdf/R1490.pdf) — «Problematic reliance on generative AI among university students: an I-PACE-informed PLS-SEM and fsQCA study» — [DOI](https://doi.org/10.3389/fpsyg.2026.1946110)
Расхождения в тексте: The text and tables agree for the extracted values. In Table 4, PA→MR and PA→PU have identical t-values (4.415) even though their betas differ (0.290 and 0.293). This is a possible typo, but it does not affect the extracted correlations. Figure 2 shows only path coefficients and loadings; no correlations from it were extracted.
Заметка ИИ: The only zero-order correlations reported are latent PLS correlations (Fornell-Larcker, Table 3). No Pearson matrix or descriptive SDs are given. Two pairs were extracted: GA with academic stress (0.435) and GA with AI-based mood regulation (0.302, coded tentatively as escapism_motive). The country is inferred (CHN) from the Chinese-language questionnaire and the Wenjuanxing platform. Age was not reported.

### ST047-1 · University students, Wenjuanxing online survey, China (inferred), n=242
Отчёты: R1490 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1490_1 · total (T1) | **academic_stress** · Academic stress (AS), 4 items adapted from Kohn and Frazer … | latent | **0.435** | **242** | 1 | Page 8, Table 3 (Fornell-Larcker panel) | «AS / 0.390 / 0.288 / 0.391 / 0.433 / 0.364 / 0.309 / 0.435 / 0.850» |
| E2 | ADHOC_R1490_1 · total (T1) | **escapism_motive** · AI-based mood regulation (MR), 3 items adapted from Du et a… | latent | **0.302** | **242** | 1 | Page 8, Table 3 (Fornell-Larcker panel) | «GA / 0.315 / 0.301 / 0.476 / 0.395 / 0.321 / 0.302 / 0.844» |

- E1: α ИИ 0.866, α коррелята 0.872; заметка: PLS-SEM inter-construct correlation from Fornell-Larcker table; HTMT (0.493) not extracted.
- E2: α ИИ 0.866, α коррелята 0.803; заметка: MR = using generative AI to reduce learning frustration/task anxiety (AI-based coping); mapping to escapism_motive needs reviewer confirmation. HTMT (0.361) not extracted.

**Ключевые поля выборки:**
- **n_analysed: 242** — Page 6, 3.1 — «The final analytic sample therefore comprised 242 valid responses.»
- **population: university_students** — Page 5, 3.1; Table 1 — «The participants were adult university students.»
- **sampling: convenience** — Page 5, 3.1 — «recruited through Wenjuanxing, an online survey platform ... using a non-probability procedure; no probabilistic sampling frame was used.»
- **ai_system: general_chatbot** — Page 6, Table 1 — «Frequently used generative AI tools (multiple choice) ChatGPT 126 52.07% Claude 65 26.86% Wenxin Yiyan 40 ... DeepSeek 127 52.48% Doubao 28»

**Остальные поля:**
- country: CHN (inferred; country of participants not explicitly stated) — Page 5, 3.1; Page 7, 3.2 — «recruited through Wenjuanxing, an online survey platform ... The questionnaire was administered in Chinese.»
- data_years: 2026 — Page 5, 3.1 — «between 26 January 2026 and 30 April 2026»
- design: cross-sectional — Page 1, Abstract — «this cross-sectional study examined psychological and academic factors associated with learning-related problematic reliance on generative AI»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 45.45 — Page 6, Table 1 — «Female 110 45.45%»
- mode: online — Page 5, 3.1 — «recruited through Wenjuanxing, an online survey platform»
- attention_checks: yes — Page 6, 3.1 — «Twenty-eight responses were then excluded because the respondents failed the attention-check item ... A further 15 responses were excluded because the same res…»
- pub_status: journal — Page 1 — «Frontiers in Psychology ... TYPE Original Research PUBLISHED 05 October 2026»
- language: English — Page 1 — «Problematic reliance on generative AI among university students: an I-PACE-informed PLS-SEM and fsQCA study»
- funding_coi: No funding; no conflicts of interest declared — Page 15, Funding; Conflict of interest — «financial support was not received for this work and/or its publication. ... conducted in the absence of any commercial or financial relationships that could b…»
- notes: Only latent (Fornell-Larcker) correlations are reported; no observed Pearson matrix. Other GA correlates in Table 3 not extracted because they are AI-specific or not in dictionary: generative-AI use self-efficacy (SE, r=0.315; AI self-efficacy excluded), need for cognition (0.301), perceived usefulness (0.476), cognitive absorption (0.395), positive affect (0.321; contextualized to AI-assisted learning, not general wellbeing). MR (AI-based mood regulation) coded as escapism_motive (coping motive for AI use) - reviewer should confirm.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability online recruitment via Wenjuanxing. — Page 5, 3.1 — «recruited through Wenjuanxing, an online survey platform ... using a non-probability procedure»
2. отклик: **unclear** — Only number of submitted questionnaires reported (289); no response rate or non-responder comparison. — Page 5, 3.1 — «A total of 289 questionnaires were submitted.»
3. валидная шкала зависимости от ИИ: **yes** — Four GA items adapted from published Du et al. (2026) 'Generative AI Addiction' measure; measurement model (loadings, CR, AVE, Fornell-Larcker, HTMT) reported in this report. Instrument coded as study-specific by job; r… — Page 7, 3.2; Page 8, Table 2-3 — «The four outcome items were adapted from the construct labeled "Generative AI Addiction" in Du et al. (2026)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.866 for GA in this sample. — Page 8, Table 2 — «Problematic reliance on generative AI (GA) ... 0.866 0.908 0.712»
5. валидные шкалы коррелятов: **unclear** — AS adapted (4 items) from Kohn & Frazer's academic stress scale; MR adapted via Du et al. (2026) from Hutchison & Gunthert and recontextualized to AI; authors state contextualized measures need further validation. — Page 7, 3.2; Page 14, 5.6 — «AS was adapted from Kohn and Frazer's (1986) academic stress scale. ... Future research should validate the contextualized measures»
6. качество данных: **yes** — Attention-check item and straight-lining screening applied. — Page 6, 3.1 — «Twenty-eight responses were then excluded because the respondents failed the attention-check item»

Правки:
- 

Проверено: да

---

## ST048 · Liu 2026 · Frontiers in Psychology

Основной отчёт R1498: [текст](../../fulltext/text/R1498.txt) · [PDF](../../fulltext/pdf/R1498.pdf) — «When loneliness amplifies the risk of problematic emotional dependence: perceived anthropomorphism and basic psychological need satisfaction in AI companion use» — [DOI](https://doi.org/10.3389/fpsyg.2026.1900817)
Не выписано ИИ: There are no other independent samples. Platform subgroups (Maoxiang n=114, Xingye n=144, Zhumengdao n=134, Replika n=96, Character.AI n=95, Other n=83, five named platforms n=583, companion-purpose records n=631; Table 13) are subsets of the same sample and report only interaction coefficients, so none were extracted.
Расхождения в тексте: (1) Item count for PED is inconsistent: the abstract and Methods/Table 2 list six items (PED1–PED6), but the Introduction says 'the analyses use a revised five-item outcome'. Table 7's df (one-factor χ2(9)) and Table 10 (six indicators) fit six items. (2) The Introduction calls the outcome 'PAD' and the Table 8 footnote calls it 'PD'; elsewhere it is 'PED'. (3) Table 2 labels two loneliness items 'LO4', and the item 'part of a group of friends' appears twice (as LO4 and LO5). (4) The Table 4 note says the alpha values also appear in the Method section, but the Method section gives none. (5) The abstract describes composite-score regressions with HC3 SEs, while Methods describe PLS-SEM in SmartPLS; the coefficients are reported as replicated across both. (6) The 'effective response rate of 83.0%' is valid/collected (666/802), not a true response rate. (7) The Methods state eligibility as…
Заметка ИИ: One sample and one eligible effect: PED total with loneliness, r = 0.194. Attachment anxiety has no zero-order correlation with PED (HTMT only), and the PA and NS correlates are not dictionary constructs.

### ST048-1 · AI companion users, online survey, China, n=666
Отчёты: R1498 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **loneliness** · Loneliness (LO), six adapted UCLA Loneliness Scale v3 / Thr… | pearson | **0.194** | **666** | 1 | Page 8, Table 8 | «LO / 0.188*** / 0.338*** / 0.194*** / 1» |

- E1: **направление: as named (LO4–LO6 reverse-scored so higher = more loneliness)**; α ИИ 0.913, α коррелята 0.946; заметка: PED column of the LO row in Table 8. HTMT PED-LO = 0.209 (Table 6) not extracted.

**⚠ Проверка скриптом (обратите внимание):**
- E1: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление

**Ключевые поля выборки:**
- **n_analysed: 666** — Page 4, Section 3.1 — «A total of 666 valid questionnaires were retained for analysis.»
- **population: general_adults** — Page 4, Section 3.1 — «Eligible respondents were required to be at least 18 years old, have experience using AI companion applications»
- **sampling: convenience** — Page 4, Section 3.1 — «Participants were recruited via AI companion user communities on Weibo and Xiaohongshu.»
- **ai_system: ai_companion** — Page 5, Table 1; Page 5, Section 3.1 — «The most frequently used AI companion products were Maoxiang, Zhumengdao, Xingye, Replika, Character. AI, and other platforms.»

**Остальные поля:**
- country: CHN — Page 1, Abstract — «A cross-sectional online survey was completed by 666 adults in China»
- data_years: 2026 — Page 4, Section 3.1 — «A three-month online survey was conducted through Wenjuanxing from February to April 2026.»
- design: cross-sectional — Page 1, Abstract — «A cross-sectional online survey was completed by 666 adults in China»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 5, Table 1 — «Age 18–25 years 283 42.5% 26–35 years 258 38.7%»
- age_sd: NR — Page 5, Table 1 — «Age 18–25 years 283 42.5%»
- age_min: 18 (eligibility criterion; lowest category 18–25) — Page 4, Section 3.1; Page 5, Table 1 — «Eligible respondents were required to be at least 18 years old»
- age_max: NR (top category 46 years and above) — Page 5, Table 1 — «46 years and above 51 7.7%»
- pct_female: 42.5 — Page 5, Table 1 — «Female 283 42.5%»
- mode: online — Page 4, Section 3.1 — «A three-month online survey was conducted through Wenjuanxing»
- attention_checks: yes — Page 4, Section 3.1 — «Responses were excluded based on predetermined criteria, including short completion time, failed attention checksor incomplete answers.»
- pub_status: journal — Page 1, header — «Frontiers in Psychology ... TYPE Original Research PUBLISHED 13 October 2026»
- language: English — Full text — «When loneliness amplifies the risk of problematic emotional dependence»
- funding_coi: Fujian Provincial Social Science Fund [FJ2025BF077]; Fujian University of Technology [GY-S22084]; no conflicts of interest declared — Page 12, Funding; Conflict of interest — «This work was supported by Research Findings from the Fujian Provincial Social Science Fund Project [FJ2025BF077]; Research Project of Fujian University of Tec…»
- notes: Gender: 210 male, 283 female, 123 other, 50 prefer not to disclose. Some participants used 'Other' platforms (n=83) which may include broader conversational AI; abstract says 'listed AI companion or conversational AI product'. Attachment anxiety (adapted ECR items, alpha .943) was measured but only HTMT (0.205 with PED) and moderation results are reported; no zero-order correlation, so not extracted. Pearson matrix gives three decimals.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience recruitment via online user communities, survey hosted on Wenjuanxing; nonprobability sample acknowledged. — Page 4, Section 3.1; Page 2 — «Participants were recruited via AI companion user communities on Weibo and Xiaohongshu.»
2. отклик: **unclear** — The reported 83.0% is the proportion of valid questionnaires among those collected (666/802), not a response rate among people invited; the true response rate cannot be determined for open community recruitment. — Page 4, Section 3.1 — «After excluding 136 invalid responses, 666 valid questionnaires remained, yielding an effective response rate of 83.0%.»
3. валидная шкала зависимости от ИИ: **yes** — Study-specific items adapted from Bergen/problematic-use scales with no published validation, but this report gives psychometric evidence: one-factor CFA, loadings, AVE, HTMT. Reviewer may want to downgrade, since the a… — Page 8, Section 4.1; Table 7 — «The one-factor PED model fit well, χ2(9) = 12.13, p = 0.206, CFI = 0.999, RMSEA = 0.023, SRMR = 0.013.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for PED in this sample = 0.913. — Page 7, Table 4 — «Problematic emotional dependence (PED) 0.913 0.914 0.932 0.697»
5. валидные шкалы коррелятов: **yes** — Loneliness, the only extracted correlate, used six items adapted from the UCLA Loneliness Scale v3 and the Three-Item Loneliness Scale (published instruments). Note the adaptation and the duplicated LO4 label in Table 2. — Page 5, Section 3.2; Page 6, Table 2 — «Loneliness was measured with six adapted UCLA Loneliness Scale items (Russell, 1996; Hughes et al., 2004).»
6. качество данных: **yes** — Predetermined exclusion criteria included short completion time and failed attention checks. — Page 4, Section 3.1 — «Responses were excluded based on predetermined criteria, including short completion time, failed attention checksor incomplete answers.»

Правки:
- 

Проверено: да

---

## ST049 · Lu 2026 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R1518: [текст](../../fulltext/text/R1518.txt) — «Supportive University Climate and AI Dependence Among Undergraduates: The Sequential Mediating Role of Academic Self-Efficacy and Self-Control.» — [DOI](https://doi.org/10.3390/bs16060902)
Не выписано ИИ: Pilot sample (n = 156 undergraduates, January 2026) used only for scale revision (reliability, EFA); no correlations reported. Not extracted.
Расхождения в тексте: (1) Text says the model explained 16.3% of AI-dependence variance (R2 = 0.163, F = 44.189), but Table 3 gives R2 = 0.283, F = 63.907 for the AI-dependence equation. (2) Text says the indirect-path shares (30.88%, 24.63%, 13.24%) are shares of the total indirect effect; arithmetically they are shares of the total effect (e.g., −0.084/−0.272 = 30.9%). The three indirect effects add to −0.187, against −0.186 in Table 4 (rounding). (3) The AI dependence scale is cited as based on Y. Chen et al. (2025) and W. Li et al. (2026), but the W. Li et al. 2026 reference is about engineering identity. The two-dimensional model is credited elsewhere to L. Li et al. (2026, CAID). (4) The pilot reports a 'four-factor model' after removing two items; which instrument this refers to is unclear. (5) The self-control appendix marks positively worded items '(R)' while saying higher scores mean greater self-c…
Заметка ИИ: One sample, two eligible zero-order correlates (academic self-efficacy, self-control). Supportive university climate is not in the construct dictionary and was not extracted (r with AI dependence = −0.402). Mediation betas and indirect effects were not extracted. AI system coded general_chatbot because the items name 'AI tools (e.g., DeepSeek)' and the scale is adapted from a conversational AI dependence scale; the reviewer may prefer ai_unspecified.

### ST049-1 · Chinese undergraduates, 7 universities in 4 provinces, CHN, n=1142
Отчёты: R1518 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | CAIDS · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale (adapted from van Zyl et al., … | pearson | **−0.442** | **1142** | 1 | Table 2 | «4. AI dependence / 3.66 / 0.56 / −0.402 ** / −0.442 ** / −0.468 ** / 1» |
| E2 | CAIDS · total (T4) | **self_control** · Self-Control Scale (Tangney et al., 2004; Besalti, 2025 rev… | pearson | **−0.468** | **1142** | 1 | Table 2 | «4. AI dependence / 3.66 / 0.56 / −0.402 ** / −0.442 ** / −0.468 ** / 1» |

- E1: α ИИ 0.880, α коррелята 0.875; заметка: AI dependence is the 12-item revision (functional + emotional dependence); only the total score is correlated. Correlation type not stated (SPSS correlation analysis); text gives r = −0.442.
- E2: α ИИ 0.880, α коррелята 0.918; заметка: Higher scores mean greater self-control. Appendix marks the first six items '(R)' even though they are positively worded, so how they were scored is unclear; text gives r = −0.468.

**Ключевые поля выборки:**
- **n_analysed: 1142** — Table 2 — «Descriptive statistics and correlation coefficients (n = 1142).»
- **population: university_students** — Abstract — «Using survey data from 1142 Chinese undergraduates»
- **sampling: convenience** — Section 3.1; Section 6 — «This study employed a multi-stage purposive sampling design. ... recruitment relied on institutional contacts and convenience-based classroom access rather than probability sampling»
- **ai_system: general_chatbot** — Section 3.3.4; Section 1 — «I am accustomed to depending on AI tools (e.g., DeepSeek) to complete academic tasks»

**Остальные поля:**
- country: CHN — Section 3.1 — «participants were recruited from seven full-time undergraduate institutions across four provinces in China»
- data_years: 2026 — Section 3.1 — «Between January and March 2026, participants were recruited from seven full-time undergraduate institutions»
- design: cross-sectional — Section 6 — «First, the cross-sectional design limits causal inference. All data were self-reported at a single time point»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Grade | Freshman | 268 | 23.47%»
- age_sd: NR — Table 1 — «NR»
- age_min: NR — Table 1 — «NR»
- age_max: NR — Table 1 — «NR»
- pct_female: 52.36 — Table 1 — «Female | 598 | 52.36%»
- mode: mixed — Section 3.1 — «Data were collected through a mixed-mode approach combining digital and paper-based modalities. The web-based questionnaire was developed on the Wenjuanxing pl…»
- attention_checks: yes — Section 3.1 — «invalid responses (e.g., repetitive answers, logical inconsistencies, and excessively short response times) were excluded, yielding 1142 valid questionnaires»
- pub_status: journal — Header — «Behav Sci (Basel). 2026 Jun 2;16(6):902. doi: 10.3390/bs16060902»
- language: English — Full text — «Supportive University Climate and AI Dependence Among Undergraduates: The Sequential Mediating Role of Academic Self-Efficacy and Self-Control»
- funding_coi: National Social Science Foundation of China (XIA240334); Jiangsu Provincial Graduate Research Innovation Program (KYCX25-1316). Authors declare no conflicts of interest. — Funding Statement; Conflicts of Interest — «The study was supported by the National Social Science Foundation of China (grant number: XIA240334) and by the Jiangsu Provincial Graduate Research Innovation…»
- notes: AI dependence measure: 12-item, two-dimension revision (functional and emotional dependence). Only the total score appears in the correlation matrix. Online data came through Wenjuanxing/WeChat, offline data through classroom paper questionnaires. Age not reported; only grade distribution is given.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Multi-stage purposive/convenience sampling via institutional contacts, Wenjuanxing online survey plus classroom paper surveys. — Section 6 — «recruitment relied on institutional contacts and convenience-based classroom access rather than probability sampling, limiting representativeness»
2. отклик: **unclear** — The reported 90.78% 'effective response rate' is valid questionnaires / questionnaires obtained (1142/1258), not participation among those invited; the number invited is not reported. — Section 3.1 — «In total, 1258 surveys were obtained. ... yielding 1142 valid questionnaires, with an effective response rate of 90.78%.»
3. валидная шкала зависимости от ИИ: **yes** — Revised from published validated scales (Chen et al., 2025 CAIDS; two-dimensional model of L. Li et al., 2026), with pilot EFA and CFA in this sample reported. — Section 3.3.4 — «AI dependence was evaluated using a revised measure based on established scales (Y. Chen et al., 2025; W. Li et al., 2026)... CFA demonstrated an acceptable fi…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.880 in this sample. — Section 3.3.4 — «The scale showed good internal consistency (Cronbach’s α = 0.880).»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy adapted from van Zyl et al. (2022) General Academic Self-Efficacy Scale; self-control from Tangney et al. (2004) Self-Control Scale (Besalti 2025 revision). Both adapted, with CFA reported. — Sections 3.3.2-3.3.3 — «Academic self-efficacy was measured using an adapted version of the questionnaire developed by van Zyl et al. (2022)... Self-control was assessed using the Sel…»
6. качество данных: **yes** — A stated rule excluded invalid responses (repetitive answers, logical inconsistencies, too-short response times). — Section 3.1 — «invalid responses (e.g., repetitive answers, logical inconsistencies, and excessively short response times) were excluded»

Правки:
- 

Проверено: да

---

## ST050 · Pazer 2026 · International Journal of Personality Psychology

Основной отчёт R1912: [текст](../../fulltext/text/R1912.txt) · [PDF](../../fulltext/pdf/R1912.pdf) — «Big Five personality traits as predictors of emotional dependence on AI-based interaction systems: The mediating role of loneliness» — [DOI](https://doi.org/10.21827/ijpp.12.43577)
Расхождения в тексте: The five Big Five–AEDS correlations in the text (p. 4) match Table 2. The paper gives no zero-order correlation between loneliness (UCLA short form, alpha .90) and AEDS. Only the b-path controlling for neuroticism is reported (beta = .55), so no loneliness row was extracted. Neuroticism–loneliness r = .60 is reported, but that pair does not include AI dependence. Loneliness M/SD are not reported. The mediation numbers do not fit together: c' (.31) + indirect (.33) = .64, but the zero-order neuroticism–AEDS r is .58. If r(N,L) = .60 and b = .55, then r(L,AEDS) would be about .70 and c' would be about .25, not .31. Internal-consistency values for 2-item BFI-10 scales (alpha .78–.86, omega .79–.87) are unusually high for 2 items. Methods mention a 'Pearson correlations' intercorrelation matrix, but Table 2 shows only the AEDS column. Other oddities: there are reference DOI mismatches (e.g.…
Заметка ИИ: One sample (N = 131) with 5 Pearson effects: AEDS total with each Big Five trait. AEDS is a study-specific scale with no validation citation. Several internal numerical inconsistencies are listed in consistency_notes.

### ST050-1 · Online adult AI chatbot users (social media/university boards/research platforms), country NR (author in Germany), N=131
Отчёты: R1912 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1912_1 · total (T3) | **neuroticism** · BFI-10/S Neuroticism | pearson | **.58** | **131** | 1 | Page 4, Table 2 | «Variable AEDS Neuroticism .58*** Extraversion -.41***» |
| E2 | ADHOC_R1912_1 · total (T3) | **extraversion** · BFI-10/S Extraversion | pearson | **-.41** | **131** | 1 | Page 4, Table 2 | «Neuroticism .58*** Extraversion -.41*** Conscientiousness -.36***» |
| E3 | ADHOC_R1912_1 · total (T3) | **conscientiousness** · BFI-10/S Conscientiousness | pearson | **-.36** | **131** | 1 | Page 4, Table 2 | «Extraversion -.41*** Conscientiousness -.36*** Openness -.18*» |
| E4 | ADHOC_R1912_1 · total (T3) | **openness** · BFI-10/S Openness | pearson | **-.18** | **131** | 1 | Page 4, Table 2 | «Conscientiousness -.36*** Openness -.18* Agreeableness -.28**» |
| E5 | ADHOC_R1912_1 · total (T3) | **agreeableness** · BFI-10/S Agreeableness | pearson | **-.28** | **131** | 1 | Page 4, Table 2 | «Openness -.18* Agreeableness -.28** Note. N = 131.» |

- E1: α ИИ .92, α коррелята .86; заметка: Two-item scale; reported alpha .86 (omega .87) is unusually high for 2 items.
- E2: α ИИ .92, α коррелята .82; заметка: Two-item scale.
- E3: α ИИ .92, α коррелята .79; заметка: Two-item scale.
- E4: α ИИ .92, α коррелята .81; заметка: Two-item scale; text gives p = .038.
- E5: α ИИ .92, α коррелята .78; заметка: Two-item scale.

**Ключевые поля выборки:**
- **n_analysed: 131** — Table 2 note — «Note. N = 131.»
- **population: general_adults** — Page 3, Sample and recruitment — «Eligibility required adults (18 years or older) with prior AI chatbot use experience... Fifty-nine percent were students and 41% were employed.»
- **sampling: convenience** — Page 5, Limitations — «the sample of N = 131 adults recruited via online convenience methods is not representative of the broader population»
- **ai_system: general_chatbot** — Page 1, Abstract; Page 3, Measures — «N = 131 adults with AI chatbot experience... "I feel I need my AI assistant to cope with difficult emotions."»

**Остальные поля:**
- country: NR — Page 3, Sample and recruitment; Page 1 affiliation — «Participants were recruited through social media platforms (Instagram, Reddit), university announcement boards, and online research participation platforms.»
- data_years: NR — Page 7 — «Received June 15, 2026 Accepted October 1, 2026»
- design: cross-sectional — Page 3, Study design — «A cross-sectional correlational design with multiple regression and mediation analyses was employed.»
- clinical_group: NA — NA — «NA»
- age_mean: 27.2 — Page 3, Sample and recruitment — «N = 131 adults (M age = 27.2 years, SD = 7.4; range: 18–55 years)»
- age_sd: 7.4 — Page 3, Sample and recruitment — «M age = 27.2 years, SD = 7.4»
- age_min: 18 — Page 3, Sample and recruitment — «range: 18–55 years»
- age_max: 55 — Page 3, Sample and recruitment — «range: 18–55 years»
- pct_female: 55.7 — Page 3, Sample and recruitment — «73 female (55.7%), 55 male (42.0%), and 3 gender-diverse (2.3%)»
- mode: online — Page 3, Study design — «Data were collected via an anonymous online survey»
- attention_checks: NR — Page 3, Method — «The final sample comprised N = 131 adults»
- pub_status: journal — Page 1, header — «International Journal of Personality Psychology 2026, Vol. 12, 84-90»
- language: English — Full text — «Big Five personality traits as predictors of emotional dependence on AI-based interaction systems»
- funding_coi: No specific funding; author declares no conflict of interest — Page 6, Accounts — «This study received no specific funding from any public, commercial, or not-for-profit funding agency... The author declares no conflict of interest.»
- notes: Country not reported: international online recruitment (Instagram, Reddit, research platforms); author affiliation Germany. Population is 59% students and 41% employed; coded general_adults. AEDS is a study-specific scale with no citation. Loneliness was measured but its zero-order correlation with AEDS is not reported. See consistency_notes for the internal numerical inconsistencies.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online convenience recruitment via social media, university boards and online research platforms. — Page 3, Sample and recruitment; Page 5, Limitations — «recruited via online convenience methods is not representative of the broader population»
2. отклик: **unclear** — No response rate or number invited/started reported. — Page 3, Sample and recruitment — «The final sample comprised N = 131 adults»
3. валидная шкала зависимости от ИИ: **no** — AEDS is introduced without a citation or development/validation study; only alpha/omega reported; author calls for validated instruments. — Page 3, Measures; Page 5, Outlook — «The psychometric development of more comprehensive and validated AI emotional dependence instruments is an important methodological priority for the field.»
4. надёжность шкалы ИИ в выборке: **yes** — AEDS alpha .92, omega .93 in this sample. — Page 3, Measures; Table 1 — «The scale demonstrated excellent reliability (α = .92, ω = .93; M = 3.36, SD = 0.80).»
5. валидные шкалы коррелятов: **yes** — Extracted correlates (Big Five) measured with published BFI-10 (Rammstedt & John, 2007). — Page 3, Measures — «Personality was assessed using the BFI-10/S (Rammstedt & John, 2007), a 10-item scale comprising two items per trait.»
6. качество данных: **unclear** — No attention checks, careless-responding screening or exclusion rule reported. — Page 3, Method — «Survey completion took approximately 15–20 minutes; participation was voluntary and uncompensated.»

Правки:
- 

Проверено: да

