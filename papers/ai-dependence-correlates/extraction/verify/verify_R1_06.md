# Проверка выписывания — файл 6 из 13

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

## ST051 · Pradeep 2026 · Research Square

Основной отчёт R1950: [текст](../../fulltext/text/R1950.txt) · [PDF](../../fulltext/pdf/R1950.pdf) — «Scaffolding and fading generative AI support shapes dependency and anxiety among undergraduate law students» — [DOI](https://doi.org/10.21203/rs.3.rs-10503738/v1)
Не выписано ИИ: Non-LLB respondents who completed the baseline survey were excluded by the authors and no data are reported for them. No other separately recruited samples. The full cross-sectional wave samples (M1 n=126, M2 n=107, M3 n=122) are the same cohort as the panel and report no dependency–correlate correlations.
Лонгитюд (для описания): Three-wave single-arm panel (M1 week 1, unstructured AI use; M2 week 8, AI as Reviewer; M3 week 15, AI as Minimal Reviewer). Matched panel n=51. No cross-lagged models were estimated. The only cross-occasion association is the Spearman rho = .38 (p = .007, n = 49) between M1 AI dependency and M3 academic anxiety. The authors say no interaction term was tested and present this as a predictive association, not moderation. Mean change in the panel: dependency 3.08 -> 2.97 -> 3.16 (Friedman chi2=1.67, p=.433; M2->M3 Wilcoxon p=.031, not significant after Bonferroni correction). Anxiety 2.96 -> 2.88 -> 3.11 (chi2=6.46, p=.040; M2<M3 significant). A median split on baseline AI usage frequency (heavy n=22, light n=29) showed only descriptively a steeper rise in anxiety and dependency among heavy users (Fig. 4). Phase is fully confounded with time in the semester.
Расхождения в тексте: 1) Section 4.4 says "anxiety and dependency both rose significantly when AI was minimised (M2 to M3)" and Table 5 marks dependency "M2 < M3*". The note under Table 5, the abstract and Section 4.9 say the dependency change (p = .031) missed the Bonferroni threshold and is a non-significant trend. 2) The panel has n = 51, but the dependency–anxiety rho is reported with n = 49; the missing cases are not explained. 3) Section 3.5 describes Spearman correlations on "individual change scores", while Section 4.6 and Fig. 3 describe M1 dependency against M3 anxiety levels. 4) Section 4.5 calls the Kruskal–Wallis analysis an "independent check", whereas Section 3.5 says the samples overlap and are not fully independent. 5) Fig. 3 (scatterplot), Fig. 4 (median-split trajectories) and Fig. 5 (dependency item distributions) are figure-only and give no further coefficients. 6) Table 3 alphas come fr…
Заметка ИИ: There is one sample and one lagged effect. All measures, including dependency and anxiety, are the author's own short scales without validation. Academic anxiety is mapped to academic_stress following the dictionary rule that test or academic anxiety is coded as academic_stress. Confidence and AI usage frequency do not match any dictionary key. Self-efficacy matches a key, but its association with dependency is not reported.

### ST051-1 · First-year LLB cohort, General Sir John Kotelawala Defence University, Sri Lanka (M1 n=126; matched panel n=51; correlation n=49)
Отчёты: R1950 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1950_1 · total (T4) | **academic_stress** · Self-authored academic anxiety scale (3 items: task-related… | spearman | **.38** | **49** | lagged: T1-T3 | Page 14, Section 4.6; Fig. 3; Abstract | «baseline AI dependency (M1) significantly predicted final academic anxiety (M3). ... (Fig. 3, ρ = .38, p = .007, n = 49)» |

- E1: α ИИ .67, α коррелята .63; заметка: Cross-occasion correlation (dependency at M1, anxiety at M3). No same-occasion correlation is reported for this pair. Alphas are taken from the full wave samples (Table 3), not from the panel. n = 49, while the panel has 51. Section 3.5 says the Spearman correlations used 'individual change scores'…

**⚠ Проверка скриптом (обратите внимание):**
- E1: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 49 (for the only dependency–correlate coefficient; matched panel n = 51; M1 n = 126)** — Page 14, Section 4.6 — «(Fig. 3, ρ = .38, p = .007, n = 49)»
- **population: university_students** — Page 9, Section 3.2 — «Participants included 79 women and 47 men aged 20 to 21 years enrolled in Introduction to Information Technology»
- **sampling: convenience** — Page 9, Section 3.2 — «Participation was voluntary, unassessed, and conducted with informed consent following institutional ethical approval.»
- **ai_system: general_chatbot** — Page 9, Section 3.2 — «AI engagement was operationalised through the free web-based platforms of ChatGPT and Gemini.»

**Остальные поля:**
- country: LKA — Page 2, Abstract — «embedded in a first-year Bachelor of Laws (LLB) cohort at a Sri Lankan state university»
- data_years: NR — Page 8, Section 3.2 — «The study was embedded in a first-year LLB course at a Sri Lankan university across one five-month semester.»
- design: panel — Page 2, Abstract — «Likert-scale data were collected at all three points (n = 126, 107, and 122) alongside 355 open-ended reflections; a matched longitudinal panel (n = 51)»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 9, Section 3.2 — «aged 20 to 21 years»
- age_sd: NR — Page 9, Section 3.2 — «aged 20 to 21 years»
- age_min: 20 — Page 9, Section 3.2 — «aged 20 to 21 years»
- age_max: 21 — Page 9, Section 3.2 — «aged 20 to 21 years»
- pct_female: 62.7 (79/126; computed from M1 counts; not reported for panel) — Page 9, Section 3.2 — «Participants included 79 women and 47 men»
- mode: NR — Page 20, Consent to participate — «used it across all three questionnaire waves»
- attention_checks: NR — Page 10, Section 3.3 — «Non-compliant submissions were excluded from the quantitative analyses but retained for descriptive reporting.»
- pub_status: preprint — Page 1 — «Research Article ... Posted Date: August 25th, 2026 DOI: https://doi.org/10.21203/rs.3.rs-10503738/v1»
- language: English — Page 1 — «Scaffolding and fading generative AI support shapes dependency and anxiety among undergraduate law students»
- funding_coi: No funding; author declares no competing interests — Page 20, Competing interests; Funding — «The author declares that no funds, grants, or other support were received during the preparation of this manuscript.»
- notes: Single-arm design-based research study with three phases (M1 unstructured, M2 AI as Reviewer, M3 AI as Minimal Reviewer). All 13 items were written by the author for this study. The only zero-order association between AI dependency and an eligible correlate is the lagged Spearman rho between M1 dependency and M3 academic anxiety. 'Academic anxiety' (task-related anxiety, worry about mistakes, course-related stress) is coded as academic_stress. The study also measured self-efficacy (author-written), but no correlation with dependency is reported. Non-compliant submissions (protocol compliance,…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Voluntary participants from a single course cohort (convenience sample). Cohort size is not reported. — Page 9, Section 3.2 — «Participation was voluntary, unassessed, and conducted with informed consent»
2. отклик: **no** — No response rate is given for the cohort. The coefficient comes from the matched panel, which lost about 60% of M1 respondents, and completers were not compared with dropouts (the full-sample Kruskal–Wallis tests are no… — Page 18, Section 7 Limitations — «The matched panel (n = 51) reflects approximately 60% attrition from M1.»
3. валидная шкала зависимости от ИИ: **no** — Author-written 3-item dependency scale; no validation study published or reported. — Page 10, Section 3.4 — «All 13 items were self-authored for this study, developed in line with Bandura's guidelines ... rather than adapted from an existing validated scale»
4. надёжность шкалы ИИ в выборке: **no** — Alpha at M1 (the wave used for the extracted coefficient) is .67, below .70. Alpha was .66 at M2 and .77 at M3. — Page 12, Table 3 — «AI dependency | .67 | .66 | .77»
5. валидные шкалы коррелятов: **no** — Academic anxiety is measured with 3 author-written items (alpha .61–.70). — Page 10, Section 3.4 — «The anxiety items addressed task-related anxiety, worry about making mistakes, and course-related stress.»
6. качество данных: **unclear** — No attention checks or careless-responding screening reported. Exclusions were only for non-LLB respondents and protocol non-compliance. — Pages 9–10, Sections 3.2–3.3 — «Non-LLB respondents who completed the baseline survey were excluded from all analyses»

Правки:
- 

Проверено: да

---

## ST052 · Prasad 2026 · Genetics and Molecular Research

Основной отчёт R1953: [текст](../../fulltext/text/R1953.txt) · [PDF](../../fulltext/pdf/R1953.pdf) — «“A STUDY TO ASSESS THE IMPACT OF OVER RELIANCE TO AI DIALOGUE ON COGNITIVE ABILITY AND ACADEMIC STRESS AMONG GENERATION-Z STUDENTS IN SELECTED COLLEGE OF NURSI…» — [DOI](https://doi.org/10.4238/14h2vp05)
Расхождения в тексте: (1) AI reliance–academic stress: Table 6 and the abstract Results give r = 0.36, but the abstract Conclusion gives r = 0.38. (2) AI reliance–cognitive ability (not extracted): Table 5 gives r = -0.42, but the abstract Results and Conclusion print r = 0.42 without a minus sign while calling it negative. (3) Cognitive ability–academic stress (not extracted): Table 7 gives r = -0.31, but the abstract Conclusion gives r = -0.45 and the results narrative prints 'r = 0.31' while calling it negative. (4) The results narrative cites the wrong tables: the AI reliance–stress correlation is attributed to Table 5 instead of Table 6, and the later bullets are shifted by one table number. (5) The 'Mean Difference' column in Tables 5–7 does not match the means shown (e.g., 54.6 vs 67.4 gives -12.8, but 54.6 vs 8.1 is listed as 46.5, and 8.1 vs 67.4 as -59.3). (6) Methods describe a 'baseline assessmen…
Заметка ИИ: There is only one eligible effect (AI reliance x academic stress). Both instruments are self-structured, and no reliability is reported for either. Cognitive ability is outside the construct dictionary. The paper has several numerical inconsistencies, so the reviewer should check the table value.

### ST052-1 · B.Sc. Nursing students, College of Nursing, L.L.R.M Medical College, Meerut, India (n = 200)
Отчёты: R1953 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1953_1 · total (T4) | **academic_stress** · Self-structured Academic stress questionnaire (total, score… | pearson | **0.36** | **200** | 1 | Page 7, Table 6 | «AI reliance 6.2 54.6 -12.8 0.36 0.002 Significant* Academic stress 8.1 67.4» |

- E1: заметка: Karl Pearson r. The abstract Results and Discussion give r = 0.36, but the abstract Conclusion gives r = 0.38. The results narrative attributes this value to 'Table 5'.

**Ключевые поля выборки:**
- **n_analysed: 200** — Page 7, Table 6 — «TABLE 6: Relationship Between Level of AI Usage and Level of Academic Stress Among Generation-Z Students N=200»
- **population: university_students** — Page 4, Table 1 — «Current course B.Sc. Nursing 200 100%»
- **sampling: convenience** — Page 2, Methodology — «The total 200 Participants meeting the inclusion and exclusion criteria were selected through Non-probability Convenience Sampling technique»
- **ai_system: general_chatbot** — Page 2, Inclusion criteria; Page 5, Table 1 — «4- Using AI dialogue. ... Type of AI tool used ChatGPT 109 54.5% Google 29 14.5% Meta AI 2 1% All of the above 60 30%»

**Остальные поля:**
- country: IND — Page 2, Methodology — «The study was conducted among Generation-Z nursing students of the College of Nursing, L.L.R.M Medical College, Meerut.»
- data_years: 2026 — Page 2, Methodology — «The data collection was carried out from 8 April 2026 to 16 April 2026.»
- design: cross-sectional — Page 2, Methodology — «A quantitative research approach with a descriptive correlational research design was adapted for the study.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 3, Table 1 — «Age in years 17–19 years 24 12% 20–22 years 112 56%»
- age_sd: NR — Page 3, Table 1 — «Age in years 17–19 years 24 12%»
- age_min: 17 (lower bound of lowest age category 17–19 years; exact minimum NR) — Page 3, Table 1 — «Age in years 17–19 years 24 12%»
- age_max: 28 (upper bound of highest age category 26–28 years; exact maximum NR) — Page 3, Table 1 — «26–28 years 3 1.5%»
- pct_female: 74 — Page 3, Table 1 — «Gender Male 52 26% Female 148 74%»
- mode: mixed — Page 2, Methodology — «The baseline assessment was conducted on 8 April 2026 through a Google Form. ... The researcher assembled the participants and administered the study tools.»
- attention_checks: NR — Page 2, Methodology — «All completed questionnaires were collected and checked for completeness before proceeding to data analysis.»
- pub_status: journal — Page 1, header — «Genetics and Molecular Research 25 (18s): 2026»
- language: English — Full text — «A STUDY TO ASSESS THE IMPACT OF OVER RELIANCE TO AI DIALOGUE ON COGNITIVE ABILITY AND ACADEMIC STRESS»
- funding_coi: NR (no funding or conflict-of-interest statement) — Full text — «NR»
- notes: AI-dependence measure is a self-structured 'level of AI usage' tool (score range 18-90, labelled AI reliance); academic stress measured with a self-structured questionnaire (score range 25-125). Mode: demographics collected via Google Form; the study tools were given in person by the researcher, so paper administration is likely but not stated. Methods mention a 'baseline' (8 April) and a 'final data collection' (16 April), but the design is a single descriptive correlational survey. Cognitive ability (self-structured cognitive tool) is not in the construct dictionary and is not extracted. St…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability convenience sample from one nursing college. — Page 2, Methodology — «selected through Non-probability Convenience Sampling technique»
2. отклик: **unclear** — No response rate or comparison of non-responders reported. — Page 2, Methodology — «The total 200 Participants meeting the inclusion and exclusion criteria were selected»
3. валидная шкала зависимости от ИИ: **no** — Self-structured AI usage/reliance tool; no development or validation evidence reported. — Page 1, Abstract (Methodology) — «The data was collected with demographic questionnaire and self-structured level of AI usage, self-structured Academic stress questionnaire and self- structured…»
4. надёжность шкалы ИИ в выборке: **unclear** — No reliability coefficient reported for the AI reliance tool. — Full text — «NR»
5. валидные шкалы коррелятов: **no** — Academic stress was measured with a self-structured questionnaire; no psychometric evidence reported. — Page 1, Abstract (Methodology) — «self-structured Academic stress questionnaire»
6. качество данных: **unclear** — Only a completeness check is mentioned; there are no attention checks and no careless-responding screening. — Page 2, Methodology — «All completed questionnaires were collected and checked for completeness before proceeding to data analysis.»

Правки:
- 

Проверено: да

---

## ST053 · Qin 2026 · Frontiers in Psychology

Основной отчёт R1991: [текст](../../fulltext/text/R1991.txt) · [PDF](../../fulltext/pdf/R1991.pdf) — «Achievement emotions in AI-assisted learning, academic self-efficacy, and learning engagement and AI dependence among university students in statistics-related…» — [DOI](https://doi.org/10.3389/fpsyg.2026.1994136)
Расхождения в тексте: 1) Consent: Section 2.1 says that going on past the online consent page counted as consent, but the Ethics statement says participants gave 'written informed consent'. 2) Total association of positive emotions with engagement: the text gives 0.337 (estimated without the mediator), while Table 5 gives a mean conditional total of 0.341. For AI dependence the figures are 0.383 (text) vs 0.382 (Table 5). These rest on different definitions, not typing errors. 3) The text correlations (r = −0.12 for self-efficacy with AI dependence, and others) match Table 1. 4) The Fornell–Larcker comparison is described only in words, and latent correlations between factors are not reported, so no latent rows were extracted. 5) Points for the reviewer to check: the timeline is very short (data March–May 2026, received 10 Sep, accepted 25 Sep 2026), measurement-model fit is unusually uniform (loadings 0.78–…
Заметка ИИ: I extracted one effect: the AI dependence total score with academic self-efficacy. The other variables in Table 1 do not fit any key in the construct dictionary, so they were not extracted. These are positive achievement emotions and negative achievement emotions (both AI-context-specific composites, not general wellbeing or anxiety), learning engagement (UWES-S) and AI literacy. The report gives no correlations for the subscales of the AI dependence scale.

### ST053-1 · Statistics-related undergraduates, 3 universities, Shijiazhuang, China (n = 700)
Отчёты: R1991 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R1991_1 · total (T2) | **self_efficacy** · Academic self-efficacy (8 items adapted from MSLQ self-effi… | pearson | **−0.12** | **700** | 1 | Page 5, Table 1 (row 5, column 3) | «5. AI dependence / 2.82 / 0.78 / 0.90 / 0.20*** / 0.19*** / −0.12** / −0.08*» |

- E1: α ИИ 0.90, α коррелята 0.88; заметка: The items were adapted to the AI-assisted statistics context (e.g., 'even when AI explanations are imperfect'). They still measure academic self-efficacy, not AI self-efficacy, but the reviewer should confirm eligibility. Two decimals only. No subscale-level correlations are reported.

**Ключевые поля выборки:**
- **n_analysed: 700** — Page 5, Table 1 — «TABLE 1 Descriptive statistics, reliabilities, and bivariate correlations (N = 700).»
- **population: university_students** — Page 3, 2.1 — «Participants were 700 undergraduate students recruited from applied statistics and related programs»
- **sampling: convenience** — Page 3, 2.1 — «The three participating universities were selected to span institutional profiles ... Recruitment targeted intact class groups in statistics and data science programs»
- **ai_system: mixed** — Page 4, 2.2 Measures — «replaced the object of each statement with reference to AI tools used in statistics coursework, such as chat assistants, code generators, and automated explainers.»

**Остальные поля:**
- country: CHN — Page 3, 2.1 Participants and procedure — «at three universities in Shijiazhuang, Hebei Province, China»
- data_years: 2026 — Page 3, 2.1 — «Data were collected between March and May 2026.»
- design: cross-sectional — Page 1, Abstract (Methods) — «A cross-sectional survey was conducted with 700 undergraduate students»
- clinical_group: NA — NA — «NA»
- age_mean: 19.81 — Page 3, 2.1 — «All participants were at least 18 years old (M = 19.81, SD = 1.27, range 18.0 to 23.8).»
- age_sd: 1.27 — Page 3, 2.1 — «(M = 19.81, SD = 1.27, range 18.0 to 23.8)»
- age_min: 18.0 — Page 3, 2.1 — «range 18.0 to 23.8»
- age_max: 23.8 — Page 3, 2.1 — «range 18.0 to 23.8»
- pct_female: 55.1 — Page 3, 2.1 — «The sample included 386 women (55.1%) and 314 men (44.9%)»
- mode: online — Page 3, 2.1 — «instructors distributed a QR code linking to an anonymous online questionnaire hosted on the Wenjuanxing platform»
- attention_checks: yes — Page 4, 2.1 — «We excluded 31 protocols showing invariant responding (the same response option on at least 95% of items) and 8 protocols with more than 10% missing values»
- pub_status: journal — Page 1, header — «Frontiers in Psychology ... TYPE Original Research PUBLISHED 07 October 2026»
- language: English — Full text — «Achievement emotions in AI-assisted learning, academic self-efficacy, and learning engagement and AI dependence among university students»
- funding_coi: No funding received; no conflicts of interest declared — Page 10, Funding; Conflict of interest — «The author(s) declared that financial support was not received for this work ... conducted in the absence of any commercial or financial relationships»
- notes: Recruited from 24 intact classes. Class-level ICCs were negligible (≤ 0.014). The AI dependence scale was written for this study (7 items, two domains). Wenjuanxing only hosted the questionnaire; it was not a recruitment panel. Self-reported frequency of AI use for coursework ranged from never to always.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample: three universities chosen by the authors, intact classes recruited, no probability sampling. — Page 3, 2.1 — «The three participating universities were selected to span institutional profiles ... Recruitment targeted intact class groups»
2. отклик: **yes** — Response rate 94.5% of invited students (89.5% after exclusions). — Page 4, 2.1 — «Of 782 students invited, 739 returned questionnaires (94.5%).»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc 7-item scale written for this study, but the report includes validation evidence: expert content review, an item-level two-factor CFA with good fit, and alpha/omega. The authors themselves say further validation … — Page 4, 2.2; Page 6, 3.2 — «For AI dependence, a two-factor item-level model separating difficulty without AI from uncritical acceptance fitted the data well, χ2(13) = 9.28, p = 0.751, CF…»
4. надёжность шкалы ИИ в выборке: **yes** — alpha = .90 and omega = .90 in this sample. — Page 4, 2.2; Page 7, Table 3 — «The scale reliability was α = 0.90.»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (academic self-efficacy) comes from the published MSLQ self-efficacy subscale, adapted to the AI-assisted statistics context. — Page 4, 2.2 — «Academic self-efficacy was measured with eight items adapted from the self-efficacy subscale of the Motivated Strategies for Learning Questionnaires (Pintrich …»
6. качество данных: **yes** — Stated rule for invalid responses: invariant responding on at least 95% of items, or more than 10% missing values. — Page 4, 2.1 — «We excluded 31 protocols showing invariant responding (the same response option on at least 95% of items)»

Правки:
- 

Проверено: да

---

## ST054 · Rizal 2026 · International Journal of Evaluation and Research in Education (IJERE)

Основной отчёт R2096: [текст](../../fulltext/text/R2096.txt) · [PDF](../../fulltext/pdf/R2096.pdf) — «Procrastination trap: how personality traits fuel generative artificial intelligence over-reliance and erode academic performance» — [DOI](https://doi.org/10.11591/ijere.v15i4.39382)
Расхождения в тексте: The text says Cronbach's alphas 'ranged from 0.64 to 0.93', but Table 1 gives a maximum of 0.937 for Openness, so the text appears to round. The PLS path coefficients in Table 5 (multivariable, not extracted) differ from the latent correlations in Table 2: Conscientiousness->AIO beta=-0.444 vs r=-0.473; Neuroticism beta=0.402 vs r=0.350; Openness beta=0.473 vs r=0.531; AIO->Procrastination beta=0.319 vs r=0.484. The abstract mentions 'decreased levels of deep learning engagement', which was not measured. The Methods say performance was measured as satisfaction with current grades, but the Limitations call it 'self-reporting measures of grade point average (GPA)'. The number of AI over-reliance items is not reported. Figure 2 (structural model) shows path estimates only, and no correlations were taken from figures.
Заметка ИИ: I extracted one sample from R2096 (n=200 undergraduates, East Malaysia, October 2025). It gives four latent correlations (Fornell-Larcker table) between GenAI over-reliance (ZHANG5 total) and BFI conscientiousness, neuroticism and openness and academic procrastination. The report has no observed correlation matrix. Age, % female and mode of administration are not reported.

### ST054-1 · Undergraduates (Computer Science & International Finance), Universiti Malaysia Sabah, East Malaysia, n=200
Отчёты: R2096 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ZHANG5 · total (T4) | **conscientiousness** · BFI Conscientiousness (9 items) | latent | **-0.473** | **200** | 1 | Table 2, p. 6 | «Conscientiousness (CON) -0.473 0.792» |
| E2 | ZHANG5 · total (T4) | **neuroticism** · BFI Neuroticism (8 items) | latent | **0.350** | **200** | 1 | Table 2, p. 6 | «Neuroticism (NEU) 0.350 0.096 0.799» |
| E3 | ZHANG5 · total (T4) | **openness** · BFI Openness to experience (10 items) | latent | **0.531** | **200** | 1 | Table 2, p. 6 | «Openness (OPE) 0.531 -0.144 -0.019 0.801» |
| E4 | ZHANG5 · total (T4) | **procrastination** · Academic procrastination items generated from Tuckman (1991… | latent | **0.484** | **200** | 1 | Table 2, p. 6 | «Procrastination (PROC) 0.484 -0.314 0.078 0.376 -0.336 0.767» |

- E1: α ИИ 0.765, α коррелята 0.925; заметка: Fornell-Larcker latent (PLS composite) correlation.
- E2: α ИИ 0.765, α коррелята 0.918; заметка: Fornell-Larcker latent (PLS composite) correlation.
- E3: α ИИ 0.765, α коррелята 0.937; заметка: Fornell-Larcker latent (PLS composite) correlation.
- E4: α ИИ 0.765, α коррелята 0.640; заметка: Fornell-Larcker latent (PLS composite) correlation; procrastination items ad hoc/adapted, alpha below .70.

**Ключевые поля выборки:**
- **n_analysed: 200** — Abstract, p. 1; Section 5, p. 8 — «PLS-SEM analysis of 200 undergraduate students»
- **population: university_students** — Section 3.1, p. 5 — «A total of 200 undergraduate students enrolled in either a Computer Science or an International Finance program»
- **sampling: convenience** — Section 3.1, p. 5 — «A total of 200 undergraduate students enrolled in either a Computer Science or an International Finance program participated in this research via purposive sampling.»
- **ai_system: general_chatbot** — Section 1, p. 1 — «how GenAI tools (like ChatGPT, Gemini, and Copilot) are being utilized by students»

**Остальные поля:**
- country: MYS — Abstract, p. 1; Section 6, p. 9 — «Our research focused on early-adopters in Computer Science and International Finance at a University located in East Malaysia.»
- data_years: 2025 — Section 3.1, p. 5 — «conducted over a four-week period in October 2025»
- design: cross-sectional — Section 6, p. 9 — «One limitation relates with the cross-sectional design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: NR — NR — «NR»
- mode: NR — Section 3.1, p. 5 — «Data collection occurred solely in the classroom to minimize distractions»
- attention_checks: NR — Sections 3.1-4, pp. 5-6 — «NR»
- pub_status: journal — Page 1, header — «International Journal of Evaluation and Research in Education (IJERE) Vol. 15, No. 4, August 2026, pp. 3362~3374»
- language: English — Full text — «Procrastination trap: how personality traits fuel generative artificial intelligence over-reliance and erode academic performance»
- funding_coi: No funding; authors declare no conflicts of interest — p. 10, Funding information; Conflict of interest statement — «No funding was involved. ... The authors have no financial or personal relationships that could inappropriately influence or bias the content of this study.»
- notes: AI dependence measured as 'GenAI over-reliance' (AIO), items adapted from Zhang et al. (2024) [35]; number of AIO items not reported. All correlations are latent-variable (PLS composite) correlations from the Fornell-Larcker table (Table 2); no observed Pearson matrix reported. Mode of classroom administration (paper vs online) not stated. Academic performance (self-rated satisfaction with grades) not extracted (not in dictionary). Pilot study (n=30) used only for item wording.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive sampling of students in two programmes at one university. — Section 3.1, p. 5 — «participated in this research via purposive sampling»
2. отклик: **unclear** — No response rate or number approached reported. — Section 3.1, p. 5 — «Participation was strictly voluntary and anonymous to promote honest responses.»
3. валидная шкала зависимости от ИИ: **yes** — AIO items adapted from the published AI dependence measure of Zhang et al. (2024); measurement model (CR, AVE) also reported. — Section 3.1, p. 5; Ref [35] — «The items assessing GenAI over-reliance were adapted from problem-based measures designed to evaluate the development of dependence, as well as habitually rely…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for AI over-reliance = 0.765. — Table 1, p. 6 — «AI over-reliance 0.765 0.851 0.590»
5. валидные шкалы коррелятов: **no** — Big Five measured with BFI (published), but academic procrastination measured with items 'generated from' Tuckman and Lay studies, not a named published instrument (alpha .640). — Section 3.1, pp. 5-6 — «Academic procrastination was evaluated using items generated from seminal research studies on the intention to delay the completion of academic work [32], [36].»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported. — Sections 3.1-4, pp. 5-6 — «NR»

Правки:
- 

Проверено: да

---

## ST055 · Saiyed 2026 · Zenodo (CERN European Organization for Nuclear Research)

Основной отчёт R2164: [текст](../../fulltext/text/R2164.txt) · [PDF](../../fulltext/pdf/R2164.pdf) — «Beyond AI Use: Examining The Predictive Quality of AI Dependency & Distress Intolerance in Avoidance Coping Among Young Adults in Mumbai» — [DOI](https://doi.org/10.5281/zenodo.23116713)
Расхождения в тексте: (1) The AI-dependence correlation with avoidance coping is r = 0.273 in Table 2 and the text. The regression gives R = 0.249 and a standardized beta of 0.272 (Tables 3.1/3.3). In Table 3.1, R2 = 0.062 does not match R2 change = 0.074. (2) Table 3.2 and the text give p = .009, but the text also says "AI Dependency significantly predicts Avoidance Coping (p < .001)". (3) Table 1 gives an AID maximum of 5.50 on a 1-5 scale (range 4.50), which is impossible. (4) The text calls r = 0.273 a "strong" correlation. (5) Gender counts (60 F + 29 M = 89) do not add up to N = 90. (6) The text cites Huang et al. (2026), but the reference list has Huang et al. 2024. (7) The scale's reliability values come from the original paper, not this sample. (8) The journal issue says December 2026, but the article was published 3 October 2026. The header DOI ends 23116714 and the job DOI ends 23116713.
Заметка ИИ: One cross-sectional sample (N=90, Mumbai, ChatGPT/Gemini users) using the GAIDS total score. Zero-order correlations are reported only with distress intolerance and avoidance coping. Neither is a dictionary construct, so no effect rows are extracted.

### ST055-1 · Young adult AI users, Mumbai, India (n=90)
Отчёты: R2164 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 90** — Page 4, Table 2 — «Table 2. Pearson Product Moment Correlation Coefficient between the variables (N=90)»
- **population: general_adults** — Page 3, Participants — «All participants were young adults ... The age range of the sample was 18 to 25 years (M=20.8, SD=2.38).»
- **sampling: convenience** — Page 3, Procedure — «Convenience sampling technique was employed with the help of online google forms to collect responses from participants.»
- **ai_system: general_chatbot** — Page 3, Participants — «have been using AI apps such as ChatGPT & Gemini»

**Остальные поля:**
- country: IND — Page 3, Participants — «All participants were young adults, have been using AI apps such as ChatGPT & Gemini and residing in Mumbai.»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 4, Results — «Inferential statistics used in the study were Pearson's Product-Moment correlation and Simple Linear Regression.»
- clinical_group: NA — NA — «NA»
- age_mean: 20.8 — Page 3, Participants — «The age range of the sample was 18 to 25 years (M=20.8, SD=2.38).»
- age_sd: 2.38 — Page 3, Participants — «The age range of the sample was 18 to 25 years (M=20.8, SD=2.38).»
- age_min: 18 — Page 3, Participants — «The age range of the sample was 18 to 25 years»
- age_max: 25 — Page 3, Participants — «The age range of the sample was 18 to 25 years»
- pct_female: 66.7 (60 of 90; calculated) — Page 3, Participants — «The total number of participants, selected through convenience sampling, in the study were 90 (60 Females, 29 Males).»
- mode: online — Page 3, Procedure — «with the help of online google forms to collect responses from participants»
- attention_checks: NR — Page 4, Results — «Out of 102 young adults who filled the form, 90 were selected as the final sample.»
- pub_status: journal — Page 1, header — «International Journal of Arts, Social Sciences and Humanities (A Quarterly, Refereed, & Peer Reviewed International Journal)»
- language: English — Full text — «Beyond AI Use: Examining The Predictive Quality of AI Dependency & Distress Intolerance in Avoidance Coping Among Young Adults in Mumbai»
- funding_coi: NR — NA — «NR»
- notes: No eligible effects: the only correlates are distress intolerance (Distress Tolerance Scale) and avoidance coping (Ways of Coping Escape-Avoidance subscale). Neither matches a key in the construct dictionary. Avoidance coping is general coping with stressors, not an escapism motive for using AI or technology. For the reviewer, the reported zero-order r values are: GAIDS total with avoidance coping r = 0.273; GAIDS total with distress intolerance r = 0.129 (Table 2, N=90). 12 of 102 respondents were excluded without a stated reason. Gender adds up to 89, not 90.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online through Google Forms. — Page 3, Procedure — «Convenience sampling technique was employed with the help of online google forms to collect responses from participants.»
2. отклик: **unclear** — No response rate is reported. 90 of 102 form-fillers were retained, but this is retention, not response. — Page 4, Results — «Out of 102 young adults who filled the form, 90 were selected as the final sample.»
3. валидная шкала зависимости от ИИ: **yes** — Published Generative AI Dependency Scale with a development and validation study (Goh et al., 2025). — Page 3, Research Tools — «AI Dependency was measured using Generative AI Dependency Scale, published by Goh et al. in 2025. The scale consists of 11 items»
4. надёжность шкалы ИИ в выборке: **unclear** — Only the alpha from the original validation (.93) is cited. No reliability is reported for this sample. — Page 3, Research Tools — «The scale includes excellent internal consistency with Cronbach's Alpha of (.93) and good test-retest reliability with an ICC of 0.87 (Goh et al., 2025).»
5. валидные шкалы коррелятов: **yes** — No dictionary-eligible correlate was extracted. The measured correlates use published instruments (Distress Tolerance Scale; Ways of Coping Scale-Revised). — Page 3, Research Tools — «Distress Intolerance was measured using Distress Tolerance Scale, published by Simons & Gaher in 2005.»
6. качество данных: **unclear** — 12 respondents were excluded, but no attention checks or exclusion rule are described. — Page 4, Results — «Out of 102 young adults who filled the form, 90 were selected as the final sample.»

Правки:
- 

Проверено: да

---

## ST056 · Sariaslan 2026 · Research on Education and Psychology

Основной отчёт R2202: [текст](../../fulltext/text/R2202.txt) · [PDF](../../fulltext/pdf/R2202.pdf) — «Perceived Social Support and Artificial Intelligent Chatbot Addiction Among University Students: The Parallel Mediating Roles of Loneliness and Social Anxiety» — [DOI](https://doi.org/10.54535/rep.1989072)
Расхождения в тексте: The text correlations (p. 11) match Table 3 exactly. Table 4 gives single-predictor standardized betas (PSS→AICA β = −.093, the same value as r); these were not extracted separately because the Pearson r is available. Figure 1 shows unstandardized path coefficients (not extracted). Two minor reference inconsistencies, not relevant to the extracted data: the text cites Hayes (2022) but the reference list has Hayes (2017); the text cites Menard (1995) but the list has Menard (2002). Data collection years are not stated; ethics approval number 2026/172 and publication in 2026 suggest 2026, so data_years is coded NR. An earlier version was presented orally at a congress (Konya, June 2026); no separate report was provided.
Заметка ИИ: One cross-sectional sample of Turkish university students (N = 1,010). The AI-dependence measure is the Turkish AI Chatbot Addiction Scale (Zhang et al., 2025 adaptation; AICD family). Three zero-order Pearson correlations were extracted: with loneliness, social anxiety and perceived social support. Please check: sampling and recruitment are not described (rob_1 rated unclear), and rob_6 was rated yes based on removal of multivariate outliers with inconsistent responses, not on attention-check items.

### ST056-1 · University students, Türkiye, online survey, n=1010
Отчёты: R2202 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **loneliness** · UCLA Loneliness Scale–Short Form (ULS-6), Turkish version | pearson | **.321** | **1010** | 1 | Page 11, Table 3 | «4. AI Chatbot Addiction / −.093** / .321** / .326** / —» |
| E2 | AICD · total (T4) | **social_anxiety** · Social Anxiety Scale–Short Form (Nunes et al., 2018; Turkis… | pearson | **.326** | **1010** | 1 | Page 11, Table 3 | «4. AI Chatbot Addiction / −.093** / .321** / .326** / —» |
| E3 | AICD · total (T4) | **social_support** · Scale of Perceived Social Support–Short Form (F-SozU K-3), … | pearson | **−.093** | **1010** | 1 | Page 11, Table 3 | «4. AI Chatbot Addiction / −.093** / .321** / .326** / —» |

- E1: α ИИ .897, α коррелята .757; заметка: Omega for loneliness = .779. Text agrees (r = .321).
- E2: α ИИ .897, α коррелята .916; заметка: Omega = .914. Text agrees (r = .326).
- E3: α ИИ .897, α коррелята .800; заметка: Omega = .802. Text agrees (r = −.093).

**Ключевые поля выборки:**
- **n_analysed: 1010** — Page 11, Table 3 note — «Note. N = 1,010.»
- **population: university_students** — Page 8, Participants — «the final sample comprised 1,010 university students with complete data»
- **sampling: NR** — Page 8, Participants; Page 10, Data Collection Procedure — «The initial study sample consisted of 1,028 university students who completed the online survey.»
- **ai_system: general_chatbot** — Page 2, Introduction; Page 8, Participants — «AI chatbots such as ChatGPT, Gemini, Claude, and Copilot ... Regarding the frequency of AI chatbot use, the largest proportions of participants reported using AI chatbots "frequently" (40.2%)»

**Остальные поля:**
- country: TUR — Page 10, Data Collection Procedure — «Following approval from the Social and Human Sciences Scientific Research and Publication Ethics Committee of Karamanoğlu Mehmetbey University (Approval No. 20…»
- data_years: NR — Page 10, Data Collection Procedure — «(Approval No. 2026/172), data were collected through an online survey.»
- design: cross-sectional — Page 1, Abstract — «Utilizing a cross-sectional correlational framework, data were gathered from 1,010 university students»
- clinical_group: NA — NA — «NA»
- age_mean: 21.96 — Page 8, Participants — «with a mean age of 21.96 years (SD = 2.90)»
- age_sd: 2.90 — Page 8, Participants — «with a mean age of 21.96 years (SD = 2.90)»
- age_min: 18 — Page 8, Participants; Table 1 — «Participants were aged 18 years or older ... 18–21 years 469 46.4»
- age_max: NR — Page 8, Table 1 — «35 years and older 10 1.0»
- pct_female: 71.7 — Page 8, Participants — «Of the participants, 724 (71.7%) were female and 286 (28.3%) were male.»
- mode: online — Page 10, Data Collection Procedure — «data were collected through an online survey.»
- attention_checks: yes — Page 8, Participants — «multivariate outlier analyses were conducted, and three additional participants whose response patterns were identified as inconsistent with the overall data s…»
- pub_status: journal — Page 1, header — «RESEARCH ON EDUCATION AND PSYCHOLOGY (REP) ... Research Article ... https://doi.org/10.54535/rep.1989072»
- language: English — Full text — «Perceived Social Support and Artificial Intelligent Chatbot Addiction Among University Students»
- funding_coi: No external funding; authors declare no conflict of interest. — Page 19, Conflict of Interest; Page 20, Funding — «There is no conflict of interest in the research. ... The authors declare that no external funding or financial assistance was received for the research»
- notes: 15 never-users of AI chatbots and 3 multivariate outliers were excluded (1,028 → 1,010). Primary purpose of use was academic/educational for 72.7%. Data collection year not stated (ethics approval no. 2026/172). The attention_checks code rests on outlier screening only; there were no attention-check items.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Online survey of volunteer university students; recruitment/sampling method not described (likely convenience, but not stated). — Page 8, Participants; Page 10 — «The initial study sample consisted of 1,028 university students who completed the online survey.»
2. отклик: **unclear** — No response rate reported; only completers (1,028) described. — Page 8, Participants — «The initial study sample consisted of 1,028 university students who completed the online survey.»
3. валидная шкала зависимости от ИИ: **yes** — AI Chatbot Addiction Scale developed and validated by Zhang et al. (2025); Turkish adaptation published (conference proceedings). — Page 9, Data Collection Instruments — «Artificial Intelligence Chatbot Addiction Scale, originally developed by Zhang et al. (2025) and adapted into Turkish by Yıldız-Durak and Balıkçı (2025).»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha .897 and omega .897 in this sample. — Page 9, Data Collection Instruments — «In the present study, the scale demonstrated excellent internal consistency, with a Cronbach's alpha coefficient of .897 and a McDonald's omega coefficient of …»
5. валидные шкалы коррелятов: **yes** — All correlates measured with published instruments: F-SozU K-3, ULS-6, Social Anxiety Scale–Short Form (all with Turkish adaptations). — Page 9, Data Collection Instruments — «Scale of PSS–Short Form, the AI Chatbot Addiction Scale, the UCLA Loneliness Scale–Short Form (ULS-6), and the SA Scale–Short Form.»
6. качество данных: **yes** — Data screened for quality: non-users excluded and multivariate outliers with inconsistent response patterns removed (no explicit attention-check items; reviewer to confirm this counts). — Page 8, Participants — «Prior to the analyses, the dataset was screened for eligibility and data quality. ... three additional participants whose response patterns were identified as …»

Правки:
- 

Проверено: да

---

## ST057 · Sarıtaş 2026 · Sakarya Üniversitesi Holistik Sağlık Dergisi

Основной отчёт R2206: [текст](../../fulltext/text/R2206.txt) · [PDF](../../fulltext/pdf/R2206.pdf) — «Can Artificial Intelligence Replace Nursing? Examining Nursing Students’ Attitudes, Anxiety, and Dependency» — [DOI](https://doi.org/10.54803/sauhsd.1924219)
Расхождения в тексте: Reliabilities in the text are rounded versions of Table 1 (DAI: 0.82 in text vs .818 in table; AIAS: 0.96 vs .957). The table values were used. The DAI-AIAS correlation is .415 in both text and Table 3. Not extracted because they are not dictionary constructs: DAI with GAAIS-PA (.215) and DAI with GAAIS-NA (-.472). Also not extracted: the regression betas in Table 4. No figures.
Заметка ИИ: One sample and one eligible effect: DAI total with AI anxiety (AIAS total). AIAS is described as having four subdimensions, but only the total score is correlated.

### ST057-1 · Nursing students, Mugla Sitki Kocman University, Turkiye, n=373
Отчёты: R2206 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **ai_anxiety** · Artificial Intelligence Anxiety Scale (AIAS; Wang & Wang, T… | pearson | **.415** | **373** | 1 | Page 5, Table 3 | «AIAS / 1 / .415** ; text: a moderate positive correlation was identified between AIAS and DAI scores (r = .415, p <0.001)» |

- E1: α ИИ .818, α коррелята .957; заметка: Text and table agree.

**Ключевые поля выборки:**
- **n_analysed: 373** — Page 4, Table 1; Page 5, Table 3 — «Table 1. Normality Tests and Reliability Coefficients of the Measured Variables (n =373)»
- **population: university_students** — Page 2, 2.1 — «The inclusion criteria were being enrolled as an undergraduate nursing student, being 18 years of age or older»
- **sampling: convenience** — Page 2, 2.1 — «Data were collected from students who met these criteria. Therefore, a convenience sampling approach was used.»
- **ai_system: ai_unspecified** — Page 3, 2.2.3 — «Higher scores indicate greater dependence on artificial intelligence, whereas lower scores indicate minimal dependence.»

**Остальные поля:**
- country: TUR — Page 2, 2.1 — «The study population consisted of 620 nursing students registered in the Faculty of Health Sciences of Muğla Sıtkı Koçman University in Türkiye.»
- data_years: 2025 — Page 3, 2.3 — «Data collection was conducted in February 2025 through face-to-face administration of self-report questionnaires at the faculty.»
- design: cross-sectional — Page 1, Abstract — «A descriptive, cross-sectional, and correlational design was employed with a sample of 373 nursing students»
- clinical_group: NA — NA — «NA»
- age_mean: 20.84 — Page 4, Table 2 — «Age (Mean±SD)= 20.84±3.54»
- age_sd: 3.54 — Page 4, Table 2 — «Age (Mean±SD)= 20.84±3.54»
- age_min: NR — Page 2, 2.1 — «being 18 years of age or older (inclusion criterion only; observed minimum not reported)»
- age_max: NR — NR — «NR»
- pct_female: 68.1 (computed: 254/373) — Page 4, Table 2 — «Sex Female Male ... 254 119»
- mode: paper — Page 3, 2.3 — «face-to-face administration of self-report questionnaires at the faculty ... written informed consent was obtained»
- attention_checks: NR — Page 3, 2.3-2.4 — «No attention checks or invalid-response rule reported; Cook distance used for regression outliers only: Outliers were identified using the Cook distance.»
- pub_status: journal — Page 1, header — «Sakarya University Journal of Holistic Health ... Vol. 9, No. 2, 93-103, 2026 ... Research Article»
- language: English — Full text — «Can Artificial Intelligence Replace Nursing? Examining Nursing Students' Attitudes, Anxiety, and Dependency»
- funding_coi: Funding not reported; no conflict of interest declared — Page 9, Article Information Form — «Conflict of Interest Disclosure: No potential conflict of interest was declared by authors.»
- notes: Single sample. Only AI-related correlate in the dictionary is AI anxiety (AIAS total). GAAIS positive/negative attitudes toward AI are not dictionary constructs and were not extracted. Paper mode inferred from face-to-face administration with written consent; the paper format is not stated explicitly. pct_female computed from Table 2 counts.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample from one faculty — Page 2, 2.1 — «Therefore, a convenience sampling approach was used.»
2. отклик: **unclear** — No response rate reported. 373 of a population of 620 took part (60.2%), but the report does not say how many were invited and does not compare non-responders — Page 2, 2.1 — «The study population consisted of 620 nursing students ... The study was completed with 373 nursing students.»
3. валидная шкала зависимости от ИИ: **yes** — DAI is a published scale (Morales-García et al., 2024) with a Turkish validation (Savaş, 2024) — Page 3, 2.2.3 — «The DAI Scale, originally introduced by Morales-García et al. (2024) [13], was adapted into Turkish by Savaş (2024) through validity and reliability procedures.»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .818 in this sample — Page 4, Table 1 — «DAI | .818 | 12.39±4.28»
5. валидные шкалы коррелятов: **yes** — AIAS (Wang & Wang, 2022) is a published scale with a Turkish adaptation by Terzi — Page 3, 2.2.2 — «The instrument designed by Wang and Wang (2022) [11] to assess fear related to artificial intelligence was adapted into Turkish by Terzi through validity and r…»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported — Page 3, 2.3-2.4 — «Outliers were identified using the Cook distance.»

Правки:
- 

Проверено: да

---

## ST058 · Seki 2026 · Research on Education and Psychology

Основной отчёт R2241: [текст](../../fulltext/text/R2241.txt) · [PDF](../../fulltext/pdf/R2241.pdf) — «Turkish Version of the Generative AI Dependency Scale: Validity, Reliability, and Psychometric Properties» — [DOI](https://doi.org/10.54535/rep.1886848)
Не выписано ИИ: Pilot study with 11 English Language Teaching undergraduates (p.4) was used only to check item clarity; no correlations were reported, so it is not extracted.
Расхождения в тексте: Table 2 and the text agree (GAIDS total with YIAT r = .51, with AICAS r = .72). The correlations between GAIDS and AICAS (total .72; Cognitive Preoccupation .65; Negative Consequences .54; Withdrawal .61) are between two AI-dependence measures (exposure families GAIDS and AICD). They are not in the construct dictionary, so they were not extracted as effects. AICAS alpha = .91. No AICAS–YIAT correlation is reported. The report calls the AICD instrument the 'Artificial Intelligence Chatbot Addiction Scale' but cites Zhang et al. (2025), 'Artificial Intelligence Chatbot Dependence Scale'. The YIAT-SF is also called the 'Internet Addiction Scale' (p.5, p.8). The population is described as university students (p.4) but as a 'Turkish adult sample' in the Conclusion (p.8) and as 'Turkish participants' in the Abstract. Subscription-status percentages add up to 107.3% (60.3 + 2.7 + 24.3 + 20), p…
Заметка ИИ: Single-sample psychometric validation study. The only eligible correlate is the YIAT-SF (problematic_internet_use), giving 4 effect rows (GAIDS total and 3 subscales). Data years are not stated; 2026 is implied by the ethics approval and submission dates.

### ST058-1 · Turkish university students, online GAIDS adaptation sample (TUR, n=411)
Отчёты: R2241 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | GAIDS · total (T1) | **problematic_internet_use** · Short Form of Young's Internet Addiction Test (YIAT-SF), Tu… | pearson | **.51** | **411** | 1 | Table 2, p.7; text p.7 | «1. Generative AI Dependency Scale / 2.37 / .69 / .88 / .89 / .51** / .72**» |
| E2 | GAIDS · Cognitive preoccupation (3 items; one report call… (T2) | **problematic_internet_use** · Short Form of Young's Internet Addiction Test (YIAT-SF), Tu… | pearson | **.44** | **411** | 1 | Table 2, p.7 | «2. Cognitive Preoccupation / 2.63 / .89 / .79 / .80 / .44** / .65**» |
| E3 | GAIDS · Negative consequences (4 items) (T1) | **problematic_internet_use** · Short Form of Young's Internet Addiction Test (YIAT-SF), Tu… | pearson | **.42** | **411** | 1 | Table 2, p.7 | «3. Negative Consequences / 2.48 / .72 / .67 / .68 / .42** / .54**» |
| E4 | GAIDS · Withdrawal (4 items) (T1) | **problematic_internet_use** · Short Form of Young's Internet Addiction Test (YIAT-SF), Tu… | pearson | **.43** | **411** | 1 | Table 2, p.7 | «4. Withdrawal / 2.09 / .82 / .88 / .89 / .43** / .61**» |

- E1: α ИИ .88 (omega .89), α коррелята .88; заметка: n not printed in Table 2; taken as full sample n=411.
- E2: α ИИ .79 (omega .80), α коррелята .88; заметка: n not printed in Table 2; taken as full sample n=411.
- E3: α ИИ .67 (omega .68), α коррелята .88; заметка: n not printed in Table 2; taken as full sample n=411. Subscale alpha below .70.
- E4: α ИИ .88 (omega .89), α коррелята .88; заметка: n not printed in Table 2; taken as full sample n=411.

**Ключевые поля выборки:**
- **n_analysed: 411** — p.4, Participants; Table 2 (n not printed in table) — «A total of 411 university students ... were included in the study»
- **population: university_students** — p.4, Participants — «A total of 411 university students living in different provinces of Türkiye, with ages ranging from 18 to 49»
- **sampling: convenience** — p.4, Procedure — «Data were collected online using Google Forms distributed through platforms such as e-mail, WhatsApp, and social media.»
- **ai_system: general_chatbot** — p.4, Participants — «ChatGPT was the most used tool with 380 users (92.5%), followed by Copilot (113, 27.5%), NotebookLM (90, 21.9%), Claude (13, 3.2%), and Genspark (3, 0.7%)»

**Остальные поля:**
- country: TUR — p.4, Participants — «A total of 411 university students living in different provinces of Türkiye»
- data_years: NR (implied 2026: ethics approval 09 Jan 2026 obtained before data collection; manuscript received 11 Feb 2026) — p.4, Procedure; p.9, Ethical Approval; p.1 — «the data collection process was initiated following ethical approval ... (Approval Date: January 09, 2026; Decision No: 2026/16)»
- design: validation study — p.3-4, aim — «this study aims to adapt the Generative Artificial Intelligence Dependency Scale to Turkish culture and to comprehensively determine its psychometric propertie…»
- clinical_group: NA — NA — «NA»
- age_mean: 22.34 — p.4, Participants — «with ages ranging from 18 to 49, were included in the study (M= 22.34, SD= 4.49)»
- age_sd: 4.49 — p.4, Participants — «(M= 22.34, SD= 4.49)»
- age_min: 18 — p.4, Participants — «with ages ranging from 18 to 49»
- age_max: 49 — p.4, Participants — «with ages ranging from 18 to 49»
- pct_female: 83.0 — p.4, Participants — «The participants comprised 341 women (83.0%) and 70 men (17.0%).»
- mode: online — p.4, Procedure — «Data were collected online using Google Forms»
- attention_checks: NR — p.4-6, Procedure/Data Analysis — «No attention checks, careless-responding screening or invalid-response rule reported.»
- pub_status: journal — p.1, header — «RESEARCH ON EDUCATION AND PSYCHOLOGY (REP) ... Research Article ... https://doi.org/10.54535/rep.1886848»
- language: English — Full text — «Turkish Version of the Generative AI Dependency Scale: Validity, Reliability, and Psychometric Properties»
- funding_coi: No specific funding; authors report no conflicts of interest — p.9, Conflict of Interest; Funding — «The authors report no potential conflicts of interest ... This study did not receive any specific grant or financial support from public, commercial, or non-pr…»
- notes: Psychometric adaptation study. AICAS (family AICD) was given as a criterion measure. Its correlations with GAIDS are between two exposure measures and were not extracted. The NC subscale has alpha .67 and item 4 loads at .31.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience online sample recruited via e-mail, WhatsApp and social media. — p.4, Procedure — «Data were collected online using Google Forms distributed through platforms such as e-mail, WhatsApp, and social media.»
2. отклик: **unclear** — Response rate not reported; open online distribution. — p.4, Procedure — «Data were collected online using Google Forms distributed through platforms such as e-mail, WhatsApp, and social media.»
3. валидная шкала зависимости от ИИ: **yes** — GAIDS has a published development/validation study (Goh et al., 2025) and CFA validation of the Turkish version is reported here. — p.5, Measures; p.6, CFA — «The Generative Artificial Intelligence Dependency Scale (GAIDS) ... was developed by Goh et al. (2025) ... the three-factor structure of the GAIDS was confirme…»
4. надёжность шкалы ИИ в выборке: **yes** — Total alpha .88, omega .89 in this sample (Negative Consequences subscale alpha .67 is below .70). — Table 2, p.7 — «1. Generative AI Dependency Scale | 2.37 | .69 | .88 | .89»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate (YIAT-SF) is a published instrument with Turkish adaptation. — p.5, Measures — «The Short Form of Young's Internet Addiction Test (YIAT-SF) was developed by Young (1998) and transformed into a short form by Pawlikowski et al. (2013). The T…»
6. качество данных: **unclear** — No information on attention checks or screening of invalid responses. — p.4-6 — «Participation was anonymous, and all participants were informed that their responses would be used solely for scientific purposes»

Правки:
- 

Проверено: да

---

## ST059 · Shen 2026 · Behavioral sciences (Basel, Switzerland)

Основной отчёт R2290: [текст](../../fulltext/text/R2290.txt) — «AI Chatbot Dependence as an Indirect Link Between Social Anxiety and Psychological Resilience: The Moderating Role of Perceived Social Support.» — [DOI](https://doi.org/10.3390/bs16091505)
Расхождения в тексте: Section 4.5 says 'Table 8 reports b, β, t, p, confidence intervals, R2, and f2', but those values are in Table 9; Table 8 holds the descriptives and correlations. The observed Pearson correlations (Table 8: SA–AICD 0.623, PSS–AICD −0.479) differ from the latent Fornell–Larcker correlations (Table 6: 0.691, −0.524), as expected. Both are extracted. The text matches Table 8 (r = 0.623). For MSPSS, Table 3 gives CR 0.940 and α 0.939. HTMT ratios (Table 7: SA—AICD 0.683; AICD—PSS 0.521) were not extracted, as the form requires. Figure 2 shows only the interaction plot; no coefficients are shown in figures only.
Заметка ИИ: I extracted one sample with four effects: Pearson and latent correlations of the AICDS total with social anxiety (SIAS-6) and with perceived social support (MSPSS). Resilience (CD-RISC-10) was the main outcome but has no key in the construct dictionary, so it was not extracted.

### ST059-1 · Wenjuanxing adult AI chatbot users, China, n=395
Отчёты: R2290 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **social_anxiety** · SIAS-6 (Six-Item Social Interaction Anxiety Scale) | pearson | **0.623** | **395** | 1 | Table 8 | «AICD / 3.903 / 1.343 / 0.623 *** /» |
| E2 | AICD · total (T4) | **social_support** · MSPSS (12-item) | pearson | **−0.479** | **395** | 1 | Table 8 | «PSS / 5.314 / 1.100 / −0.578 *** / −0.479 *** /» |
| E3 | AICD · total (T4) | **social_anxiety** · SIAS-6 (Six-Item Social Interaction Anxiety Scale) | latent | **0.691** | **395** | 1 | Table 6 (Fornell–Larcker Criterion) | «AICD / 0.691 / 0.738 /» |
| E4 | AICD · total (T4) | **social_support** · MSPSS (12-item) | latent | **−0.524** | **395** | 1 | Table 6 (Fornell–Larcker Criterion) | «PSS / −0.623 / −0.524 / 0.753 /» |

- E1: α ИИ 0.905, α коррелята 0.920; заметка: Observed composite-score Pearson correlation; also in text (r = 0.623, p < 0.001).
- E2: α ИИ 0.905, α коррелята 0.939; заметка: Observed composite-score Pearson correlation.
- E3: α ИИ 0.905, α коррелята 0.920; заметка: Inter-construct (latent) correlation from CFA Fornell–Larcker table; diagonal 0.738 is sqrt(AVE).
- E4: α ИИ 0.905, α коррелята 0.939; заметка: Inter-construct (latent) correlation from CFA Fornell–Larcker table.

**Ключевые поля выборки:**
- **n_analysed: 395** — Table 1; Section 4.1 — «Demographic Characteristics of Respondents (N = 395).»
- **population: general_adults** — Section 3.1; Table 1 — «The final analytic sample consisted of 395 adult participants (97.53% of the initially obtained records).»
- **sampling: quota or online panel** — Section 3.1 — «The survey was conducted on the Wenjuanxing platform using its sample-recruitment service in China. Participants received RMB 7 after completing the questionnaire.»
- **ai_system: general_chatbot** — Section 3.1 — «answered a screening question asking whether they had used an AI chatbot such as ChatGPT, Claude, Gemini, or Character.AI during the previous six months»

**Остальные поля:**
- country: CHN — Section 3.1 — «The survey was conducted on the Wenjuanxing platform using its sample-recruitment service in China.»
- data_years: NR — Section 3.1 — «NR»
- design: cross-sectional — Abstract — «Cross-sectional survey data from 395 adult AI chatbot users recruited through an online survey platform in China»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age | 18–25 | 49 | 12.41 26–35 | 228 | 57.72 36–45 | 91 | 23.04 46 years or above | 27 | 6.84»
- age_sd: NR — Table 1 — «Age was recorded as under 18, 18–25, 26–35, 36–45, or 46 years or above»
- age_min: 18 — Section 3.1; Table 1 — «one because the respondent was younger than 18 years ... Age | 18–25 | 49 | 12.41»
- age_max: NR — Table 1 — «46 years or above | 27 | 6.84»
- pct_female: 52.91 — Table 1 — «Female | 209 | 52.91»
- mode: online — Section 3.1 — «The survey was conducted on the Wenjuanxing platform»
- attention_checks: yes — Section 3.1 — «six because the questionnaires were completed in less than 1 min, one because of straight-line responding across all scale items»
- pub_status: journal — Header — «Behavioral sciences (Basel, Switzerland); DOI: 10.3390/bs16091505»
- language: English — Full text — «AI Chatbot Dependence as an Indirect Link Between Social Anxiety and Psychological Resilience»
- funding_coi: No external funding; authors declare no conflicts of interest. — Funding Statement; Conflicts of Interest — «This research received no external funding. ... The authors declare no conflicts of interest.»
- notes: Single sample. AI system coded general_chatbot: screening examples were mainly general chatbots (ChatGPT, Claude, Gemini) but also named Character.AI (companion); reviewer may consider 'mixed'. Age only in bands (mean/SD NR). Psychological resilience (CD-RISC-10) not extracted: no matching dictionary key. HTMT ratios (Table 7) and regression betas not extracted as the form requires. 405 records obtained, 10 excluded (2 non-users, 6 speeders, 1 straight-liner, 1 minor).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online panel recruitment through Wenjuanxing sample service (crowdsourcing panel). — Section 3.1 — «The survey was conducted on the Wenjuanxing platform using its sample-recruitment service in China.»
2. отклик: **unclear** — Response rate among invited panel members not reported; 97.53% is retention of obtained records after screening, not a response rate. — Section 3.1 — «A total of 405 response records were initially obtained. ... The final analytic sample consisted of 395 adult participants (97.53% of the initially obtained re…»
3. валидная шкала зависимости от ИИ: **yes** — Published AICDS (Zhang et al., 2025); CFA, AVE and CR also reported in this report. — Section 3.2; Tables 3, 5 — «AI chatbot dependence was measured using the eight-item AICDS developed by Zhang et al. (2025)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.905 in this sample. — Table 3 — «AICD | AICD1 | 0.756 | 0.545 | 0.905 | 0.905»
5. валидные шкалы коррелятов: **yes** — Extracted correlates measured with published instruments (SIAS-6, MSPSS). — Section 3.2 — «Social anxiety was captured with the SIAS-6 (Peters et al., 2012). ... Perceived social support was assessed with the 12-item MSPSS (Zimet et al., 1988)»
6. качество данных: **yes** — Speeding (<1 min) and straight-lining exclusions stated. — Section 3.1 — «six because the questionnaires were completed in less than 1 min, one because of straight-line responding across all scale items»

Правки:
- 

Проверено: да

---

## ST060 · Shumaila Afzal 2026 · Research Journal of Psychology

Основной отчёт R2320: [текст](../../fulltext/text/R2320.txt) · [PDF](../../fulltext/pdf/R2320.pdf) — «Role of Young People Safely Trust AI-Based Mental Health Support, and Psychological Factors Predict Dependence, Trust, or Help-Seeking» — [DOI](https://doi.org/10.59075/rjs.v4i1.395)
Расхождения в тексте: (1) Timeline problem: the report says data were collected January–April 2026, but it also says the article was received on 11 Feb 2026, accepted on 14 Mar 2026 and published online on 18 Mar 2026. Data collection would therefore have ended after publication. The reviewer should check whether the data are genuine. (2) Table 3 gives F(6,395) for the active help-seeking model, but the text gives F(5,396), even though six predictors are listed. (3) The text says alphas ranged from .79 to .92, but the highest alpha in Table 2 is .91. (4) The DAI-MH alpha of .89 is called a pilot alpha in Measures and appears unchanged in Table 2. The STAI-T alpha of .91 is likewise the value Measures attributes to earlier studies. (5) Stigma with help-seeking, r = –.40, is flagged ** but would be p < .001 at N = 402. (6) The text calls 71.4% of the sample university students, but Table 1 gives that figure fo…
Заметка ИИ: One sample and one eligible effect: DAI-MH total with STAI-T trait anxiety, r = .55. The AI system is coded ai_unspecified because participants used a mix of AI mental-health tools (chatbots such as Woebot/Wysa, plus apps). Population is coded mixed because participants were recruited from universities and from community youth groups.

### ST060-1 · Pakistani young people aged 18-30, universities and community youth groups, Pakistan (n = 402)
Отчёты: R2320 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2320_1 · total (T1) | **anxiety** · STAI-T (Urdu version), trait anxiety | pearson | **.55** | **402** | 1 | Page 12, Table 2 (row 4, column 2) | «4. Trait anxiety 3.21 0.92 .91 –.15** .55*** –.12* — ; text: Unhealthy dependence was positively related with trait anxiety (r = .55, p < .001)» |

- E1: α ИИ .89, α коррелята .91; заметка: Multiple imputation was used for item-level missing data. The STAI-T alpha of .91 in Table 2 is the same as the value the Measures section gives from earlier Pakistani studies.

**Ключевые поля выборки:**
- **n_analysed: 402** — Page 12, Table 2 — «Table 2 Descriptive Statistics, Reliabilities and Bivariate Correlations (N =402)»
- **population: mixed** — Page 9-10, Procedure; Page 11, Table 1 — «the research team engaged five universities in Lahore, Karachi, Islamabad and rural Punjab, and three community-based youth groups.»
- **sampling: convenience** — Page 7-8, Participants and Sampling — «Stratified purposive sampling technique was used to select the participants covering major urban (Lahore, Karachi and Islamabad) and semi‑urban/rural areas of the provinces of Punjab and Sindh.»
- **ai_system: ai_unspecified** — Page 7, Participants and Sampling; Page 8, Measures — «have been aware of or had interacted with AI‑based mental health tools (e.g., Chatbots such as Woebot, Wysa, or local mental health applications)»

**Остальные поля:**
- country: PAK — Page 8, Participants and Sampling — «(b) Pakistani nationality and residing in Pakistan»
- data_years: 2026 — Page 9, Procedure of Data Collection — «Data collection was done for four months from January to April 2026.»
- design: cross-sectional — Page 7, Research Design — «The type of research that was conducted was quantitative, cross-sectional and correlational.»
- clinical_group: NA — NA — «NA»
- age_mean: 22.7 — Page 11, text below Table 1 — «with a mean age of 22.7 years (SD = 3.1)»
- age_sd: 3.1 — Page 11, text below Table 1 — «with a mean age of 22.7 years (SD = 3.1)»
- age_min: 18 — Page 11, Table 1; Page 8 inclusion criteria — «18–22 years 246 61.2»
- age_max: 30 — Page 11, Table 1; Page 8 inclusion criteria — «27–30 years 50 12.4»
- pct_female: 58.2 — Page 11, Table 1 — «Female 234 58.2»
- mode: mixed — Page 10, Procedure — «approached interested students with a paper questionnaire and/or a tablet-based version ... The recruitment process was done online using a secure link provide…»
- attention_checks: yes — Page 11, Data Screening — «after discarding 18 cases that had too many missing data points (more than 20%) or that exhibited straight‑lining.»
- pub_status: journal — Page 1, header — «Research Journal of Psychology (RJP) Online ISSN: 3006-7219 ... Volume 4, Number 1, 2026, Pages 908 – 926»
- language: English — Full text — «Role of Young People Safely Trust AI-Based Mental Health Support, and Psychological Factors Predict Dependence, Trust, or Help-Seeking»
- funding_coi: NR (no funding or conflict-of-interest statement in the report) — Full text — «NR»
- notes: The AI tools were mental-health AI tools (chatbots such as Woebot/Wysa, plus apps), so ai_system is coded ai_unspecified. 21.4% of participants had never used such a tool; inclusion required only having used or heard of one. The DAI-MH is an ad hoc adaptation of the Smartphone Addiction Scale. Timeline problem: data collection (Jan–Apr 2026) runs past the publication date (18 Mar 2026). See consistency_notes.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (non-probability) sampling through universities, community youth groups, WhatsApp groups, mailing lists and social media. — Page 7-8; Page 10 — «Stratified purposive sampling technique was used to select the participants»
2. отклик: **unclear** — The reported 'effective response rate' of 95.7% is the share of obtained questionnaires that were kept (402/420). It is not the share of people approached who took part. The true response rate is not reported. — Page 11, Data Screening — «A total of 420 participants' data were obtained. A total of 402 young people (effective response rate 95.7%) was included in the final analytic sample»
3. валидная шкала зависимости от ИИ: **no** — The DAI-MH was built for this study by adapting the Smartphone Addiction Scale. Its only psychometric evidence is a pilot alpha; the authors say it was not validated with CFA. — Page 8, Unhealthy Dependence; Page 17, Limitations — «cross‑cultural adaptation of scales (e.g., Dependence on AI Mental Health Support) was pilot‑tested but was not fully validated with confirmatory factor analys…»
4. надёжность шкалы ИИ в выборке: **yes** — Table 2 reports alpha = .89 for unhealthy dependence. The Measures section gives the same value as a pilot alpha, so it is unclear whether .89 comes from the main sample. — Page 12, Table 2 — «2. Unhealthy dependence 2.15 0.86 .89»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, trait anxiety, was measured with the published STAI-T (Urdu version). — Page 9, Trait Anxiety — «The State‑Trait Anxiety Inventory-Trait version (STAI-T) (Spielberger, 1983) Urdu version (Hashmi & Khurshid, 2019) 20 items.»
6. качество данных: **yes** — Cases with straight-lining or more than 20% missing data were removed. — Page 11, Data Screening — «after discarding 18 cases that had too many missing data points (more than 20%) or that exhibited straight‑lining.»

Правки:
- 

Проверено: да

