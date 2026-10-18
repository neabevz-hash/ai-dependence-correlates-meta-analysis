# Проверка выписывания — файл 10 из 13

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

## ST091 · - 2025 · Advanced International Journal for Research

Основной отчёт R3037: [текст](../../fulltext/text/R3037.txt) · [PDF](../../fulltext/pdf/R3037.pdf) — «Artificial Intelligence Dependence and Well-Being Among College Students» — [DOI](https://doi.org/10.63363/aijfr.2025.v06i06.3580)
Расхождения в тексте: The AI dependence–digital well-being correlation is reported three different ways. Table 3 gives -0.725. The Results text (p. 3) says "r = –0.32, p < 0.01" and calls the link "moderate". The abstract and Discussion (pp. 1, 4) give r = –0.72 and call it "strong". The table value (-0.725) was extracted. Reliabilities (α = 0.921 for DWBS, 0.87 for DAIS) are given without saying they are for this sample; they are read as sample values.
Заметка ИИ: One cross-sectional sample. The only correlate is digital well-being, and whether it fits the 'wellbeing' construct is doubtful, so the reviewer should decide whether it is eligible. The report gives no data-collection years, mode, response rate, attention checks or funding.

### ST091-1 · College students, Coimbatore (India), n=100
Отчёты: R3037 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **wellbeing** · Digital Well-Being Scale (Gomes et al., 2023) | pearson | **-0.725** | **100** | 1 | Page 3, Table 3 | «AI Dependence 1 -0.725 Digital Well-Being –0.725 1» |

- E1: α ИИ 0.87, α коррелята 0.921; заметка: REVIEWER CHECK: digital well-being = 'healthy, mindful, and balanced technology use'; may not fit the wellbeing key (subjective/psychological wellbeing). Remove if judged ineligible. Text gives r = –0.32 and abstract/discussion r = –0.72; table value used. Pearson assumed ('correlation analysis', r…

**Ключевые поля выборки:**
- **n_analysed: 100** — Page 3, Table 3 — «Correlation Between AI Dependence and Digital Well-Being (N = 100)»
- **population: university_students** — Page 2, Methods — «Students aged 17–25 who were enrolled in a recognized college and willing to participate were included»
- **sampling: convenience** — Page 2, Methods — «a sample of 100 participants was selected through purposive sampling, ensuring that only regular users of AI tools such as ChatGPT, Perplexity, Gemini, and Meta AI were included»
- **ai_system: general_chatbot** — Page 2, Methods — «only regular users of AI tools such as ChatGPT, Perplexity, Gemini, and Meta AI were included»

**Остальные поля:**
- country: IND — Page 1, author affiliations — «Rathinam College of Arts and Science, Coimbatore»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 2, Methods — «A cross-sectional research design was used to study the relationship between AI dependence and digital well-being among college students.»
- clinical_group: NA — NA — «NA»
- age_mean: 20.6 — Page 3, text below Table 1 — «The mean age of the sample was 20.6 years»
- age_sd: NR — NA — «NR»
- age_min: 17 — Page 2, Methods; Table 1 — «The population consisted of students aged 17–25 years»
- age_max: 25 — Page 2, Methods; Table 1 — «The population consisted of students aged 17–25 years»
- pct_female: 62 — Page 2, Table 1 — «Female 62 62%»
- mode: NR — NA — «NR»
- attention_checks: NR — NA — «NR»
- pub_status: journal — Page 1, header — «Advanced International Journal for Research (AIJFR) E-ISSN: 3048-7641»
- language: English — Full text — «Artificial Intelligence Dependence and Well-Being Among College Students»
- funding_coi: NR (no funding or conflict-of-interest statement) — NA — «NR»
- notes: Undergraduate (III B.Sc Psychology) student project. 'Purposive sampling' coded as convenience (non-probability). Country inferred from author affiliation (Coimbatore); data-collection site not stated explicitly. Age min/max are the inclusion range / age-band limits, not observed extremes. Exclusion of students with diagnosed cognitive or psychiatric issues. The only correlate is the Digital Well-Being Scale (Gomes et al., 2023), which measures healthy/balanced technology use; its fit to the 'wellbeing' dictionary key is doubtful (see effect note).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (non-probability) sample of regular AI users. — Page 2, Methods — «a sample of 100 participants was selected through purposive sampling»
2. отклик: **unclear** — Response rate not reported. — NA — «NR»
3. валидная шкала зависимости от ИИ: **yes** — DAIS has a published development/validation study (Morales-García et al., 2024). — Page 2, Methods; Page 5, References — «Morales-García, J., et al. (2024). Development and validation of the Dependence on Artificial Intelligence Scale (DAIS).»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha = 0.87 reported, apparently for this sample. — Page 2, Methods — «the Dependence on Artificial Intelligence Scale (DAIS) by Morales-García et al. (2024) with a reliability of α = 0.87»
5. валидные шкалы коррелятов: **yes** — Digital Well-Being Scale has a published validation (Gomes et al., 2023). — Page 5, References — «Gomes, R., ... (2023). Design and validation of the Digital Well-Being Scale.»
6. качество данных: **unclear** — No attention checks or screening for invalid responses reported. — NA — «NR»

Правки:
- 

Проверено: да

---

## ST092 · Ahmad 2025 · Research Journal of Psychology

Основной отчёт R3076: [текст](../../fulltext/text/R3076.txt) · [PDF](../../fulltext/pdf/R3076.pdf) — «Artificial Intelligence Dependency, Academic Self-Efficacy, and the Imposter Phenomenon in University Students» — [DOI](https://doi.org/10.59075/rjs.v3i4.282)
Расхождения в тексте: (1) The Methods say ASAIDAS has 27 items with α=0.79. Table 2 scores AI dependency as 5 items (α=0.81) and academic self-efficacy as 7 items (α=0.82). (2) AI dependency is M=15.6, SD=3.75 in Table 2 but M=15.63, SD=3.76 in Table 3. Imposter phenomenon is M=37.2, SD=11.5 in Table 2 but M=37.59, SD=12.78 in Table 3. (3) Table 3 contains impossible coefficients, for example ASE–Neuroticism -2.83, AID–'Several times a week' 1.85, Conscientiousness–Weekly -1.34, and also -3.65, -6.26, -1.14, -0.91 and '0014'. This suggests transcription errors in the matrix. (4) The Discussion calls the AID–neuroticism link a 'strong positive relationship' (r=0.22) and the AID–conscientiousness link a 'strong negative relationship' (r=-0.25). These descriptions overstate the tabled values. (5) The Table 3 note defines *** as 'significant at ≤ 0.01', which differs from Table 4 (***p<.001). (6) The BFI-10 over…
Заметка ИИ: One sample. Six Pearson correlations of the 5-item ASAIDAS AI dependency score were extracted, with academic self-efficacy and the BFI-10 Big Five traits, from Table 3 (n=200). Data year not reported. The AI system is coded 'mixed' because ChatGPT (94.5%) was used together with Grammarly, Quillbot, DeepSeek and others.

### ST092-1 · Undergraduates at 4 universities (PU, GCU, NUCES, UMT), Lahore, Pakistan, n=200
Отчёты: R3076 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ACOSTA5 · total (T4) | **self_efficacy** · ASAIDAS Academic Self-efficacy (7 items) | pearson | **-0.40** | **200** | 1 | Page 12, Table 3, row 1 col 2 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |
| E2 | ACOSTA5 · total (T4) | **conscientiousness** · BFI-10 Conscientiousness | pearson | **-0.25** | **200** | 1 | Page 12, Table 3, row 1 col 4 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |
| E3 | ACOSTA5 · total (T4) | **neuroticism** · BFI-10 Neuroticism | pearson | **0.22** | **200** | 1 | Page 12, Table 3, row 1 col 5 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |
| E4 | ACOSTA5 · total (T4) | **openness** · BFI-10 Openness | pearson | **-0.06** | **200** | 1 | Page 12, Table 3, row 1 col 6 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |
| E5 | ACOSTA5 · total (T4) | **agreeableness** · BFI-10 Agreeableness | pearson | **0.04** | **200** | 1 | Page 12, Table 3, row 1 col 7 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |
| E6 | ACOSTA5 · total (T4) | **extraversion** · BFI-10 Extraversion | pearson | **0.04** | **200** | 1 | Page 12, Table 3, row 1 col 8 | «1. AI Dependency - -0.40*** 0.48*** -0.25*** 0.22*** -0.06 0.04 0.04 -0.17*» |

- E1: α ИИ 0.81, α коррелята 0.82; заметка: Academic self-efficacy comes from the same ASAIDAS instrument as the AI dependency score.
- E2: α ИИ 0.81, α коррелята NR; заметка: 2-item subscale. Only the BFI-10 overall alpha (0.24) was reported.
- E3: α ИИ 0.81, α коррелята NR; заметка: 2-item subscale. Only the BFI-10 overall alpha (0.24) was reported.
- E4: α ИИ 0.81, α коррелята NR; заметка: 2-item subscale. Only the BFI-10 overall alpha (0.24) was reported.
- E5: α ИИ 0.81, α коррелята NR; заметка: 2-item subscale. Only the BFI-10 overall alpha (0.24) was reported.
- E6: α ИИ 0.81, α коррелята NR; заметка: 2-item subscale. Only the BFI-10 overall alpha (0.24) was reported.

**Ключевые поля выборки:**
- **n_analysed: 200** — Page 9, Method; Table 1 — «35 questionnaires were rejected as incomplete which reduced the number of participants to 200»
- **population: university_students** — Page 9, Method — «The sample was comprised of 200 undergraduate students aged 18-25 years, undertaking BS (Hons) programs in two public and two private universities»
- **sampling: convenience** — Page 9, Method — «The study adopted a correlational research design with purposive sampling»
- **ai_system: mixed** — Page 10, Table 1 — «Software Using Chat GPT 189 94.5 % Grammarly 60 30.0 % Perplexity 24 12.0 % Copilot 30 15 .0% Deep Seek 52 26 .0 % Quillbot 45 22.5 % Sci space 14 7 .0 %»

**Остальные поля:**
- country: PAK — Page 1; Page 9 — «Centre for Clinical Psychology (CCP), University of The Punjab, Lahore, Pakistan ... University PU 50 25 % GCU 50 25 % NUCES 50 25 % UMT 50 25 %»
- data_years: NR (April to June; year not stated) — Page 9, Method — «The period of data collection was two months April to June, and the overall response rate was 81 percent.»
- design: cross-sectional — Page 1, Abstract — «In this cross-sectional study, a total of 200 undergraduates participated, selected through purposive sampling»
- clinical_group: NA — NA — «NA»
- age_mean: 20.78 — Page 10 — «The mean age of participants was calculated to be 20.78.»
- age_sd: NR — NR — «NR»
- age_min: 18 — Page 9, Method; Page 11 inclusion criteria — «200 undergraduate students aged 18-25 years»
- age_max: 25 — Page 9, Method; Page 11 inclusion criteria — «200 undergraduate students aged 18-25 years»
- pct_female: 62.5 — Page 9, Table 1 — «Female 125 62.5 %»
- mode: paper — Page 9, Method — «The data collection was carried out using printed questionnaires»
- attention_checks: NR — Page 9, Method — «35 questionnaires were rejected as incomplete which reduced the number of participants to 200»
- pub_status: journal — Page 1 — «Research Journal of Psychology (RJP) Online ISSN: 3006-7219 ... Volume 3, Number 4, 2025, Pages 414 – 434»
- language: English — Page 1 — «Artificial Intelligence Dependency, Academic Self-Efficacy, and the Imposter Phenomenon in University Students»
- funding_coi: NR (no funding or conflict-of-interest statement) — NR — «NR»
- notes: Purposive sampling coded as convenience. Paper questionnaires. Only incomplete questionnaires were excluded; no attention checks or careless-responding screening were reported. The AI dependency score is the 5-item AI dependency part of ASAIDAS (Acosta-Enriquez et al., 2025), with K=5 and α=0.81 in Table 2. The Methods describe the whole ASAIDAS as 27 items with α=0.79. Academic self-efficacy is the 7-item ASAIDAS ASE part (α=0.82). Imposter phenomenon (CIPS-10) is not in the construct dictionary and was not extracted. AI-use frequency dummies were not extracted. Table 3 has several impossibl…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive (non-probability) sample from four universities — Page 9, Method — «The study adopted a correlational research design with purposive sampling»
2. отклик: **yes** — Response rate of 81% reported (235 of 288). Usable 200/288 is about 69%, still ≥60%. — Page 9, Method — «Out of the 288 students contacted, 53 of them refused participation ... the overall response rate was 81 percent.»
3. валидная шкала зависимости от ИИ: **yes** — Uses the published ASAIDAS (Acosta-Enriquez et al., 2025). The authors note it has not been validated or adapted in Pakistan. — Page 11, Measuring Instruments; Page 16, Limitations — «Academic Self-Efficacy and AI Dependency Assessment Scale (ASAIDAS; Acosta-Enriquez et al., 2025) ... The assessment of the AI dependency is a new adaptation t…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.81 for the 5-item AI dependency score in this sample — Page 11, Table 2 — «Artificial Intelligence Dependency 5 15.6 3.75 5-25 0.81»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy is measured with the published ASAIDAS and personality with the published BFI-10 (Rammstedt, 2007). Note: BFI-10 total alpha in this sample was 0.24. — Page 11, Measuring Instruments — «Big-Five Personality Inventory ( BFI-10; Rammstedt, 2007)»
6. качество данных: **unclear** — Only incomplete questionnaires were excluded. No attention checks or careless-responding screening were reported. — Page 9, Method — «35 questionnaires were rejected as incomplete»

Правки:
- 

Проверено: да

---

## ST093 · Arora 2025 · International Journal of Interdisciplinary Approaches in Psychology

Основной отчёт R3164: [текст](../../fulltext/text/R3164.txt) · [PDF](../../fulltext/pdf/R3164.pdf) — «A Study on Association between AI and Critical Thinking, Impulsivity, Dependence among Young Adults» — [DOI](https://doi.org/10.61113/ijiap.v3i9.1143)
Расхождения в тексте: The sample size is 55 in the text (p.5, 4.1) but 56 in Tables 1 and 2 (p.6); 56 was used. The Discussion (p.6) gives the DAI-Urgency correlation as 'r= 0.0302', while Table 2 shows 0.302*; the table value was used. The DAI response options listed on p.5 skip point 4 ('Mostly true for me (5) Describe me perfectly'). Sampling is called 'simple random sampling', but participants were interested volunteers using a Google Form.
Заметка ИИ: Small single-author study (n=56) in a minor journal. It reports no reliabilities, no demographics beyond the 18-27 age range, and no statistical method for the correlations (assumed Pearson). All four I-8 facets were coded as impulsivity rows; the reviewer may decide whether to combine them or pick one per sample.

### ST093-1 · Young adults, Chandigarh, India, n=56 (Google Form)
Отчёты: R3164 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **impulsivity** · Impulsive Behavior Short Scale (I-8) Urgency | pearson | **0.302** | **56** | 1 | Page 6, Table 2 | «AI Dependence / -0.044 / 0.088 / 0.302* / -0.038 / -0.044 / 0.015 / —» |
| E2 | DAI · total (T4) | **impulsivity** · Impulsive Behavior Short Scale (I-8) Lack of Premeditation | pearson | **-0.038** | **56** | 1 | Page 6, Table 2 | «AI Dependence / -0.044 / 0.088 / 0.302* / -0.038 / -0.044 / 0.015 / —» |
| E3 | DAI · total (T4) | **impulsivity** · Impulsive Behavior Short Scale (I-8) Lack of Perseverance | pearson | **-0.044** | **56** | 1 | Page 6, Table 2 | «AI Dependence / -0.044 / 0.088 / 0.302* / -0.038 / -0.044 / 0.015 / —» |
| E4 | DAI · total (T4) | **impulsivity** · Impulsive Behavior Short Scale (I-8) Sensation Seeking | pearson | **0.015** | **56** | 1 | Page 6, Table 2 | «AI Dependence / -0.044 / 0.088 / 0.302* / -0.038 / -0.044 / 0.015 / —» |

- E1: заметка: The text gives r = 0.0302 (typo). Correlation type is not stated; assumed Pearson. Subscale has 2 items.
- E2: заметка: Correlation type is not stated; assumed Pearson.
- E3: заметка: Correlation type is not stated; assumed Pearson.
- E4: заметка: Correlation type is not stated; assumed Pearson. Sensation seeking correlates negatively with the other I-8 facets in this sample (-0.496, -0.663).

**Ключевые поля выборки:**
- **n_analysed: 56** — Page 6, Table 1 — «N | 56 | 56 | 56 | 56 | 56 | 56 | 56»
- **population: general_adults** — Page 1, Abstract — «explore the association between AI dependence, critical thinking and impulsive behavior among young adults (18-27 years)»
- **sampling: probability** — Page 5, 4.1 Sample — «The sample was collected by simple random sampling. In which interested participant filled google form with honesty.»
- **ai_system: ai_unspecified** — Page 5, 4.2 Measures — «was used to measure the level of dependence among young adults towards artificial intelligence (AI).»

**Остальные поля:**
- country: IND — Page 5, 4.1 Sample — «The total number of samples obtained were 55 in the city of Chandigarh.»
- data_years: NR — NA — «NR»
- design: cross-sectional — Page 5, 4.3 Procedure — «The participants were informed purpose of the research and questionnaire were filled through google form.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: 18 — Page 1, Abstract — «among young adults (18-27 years)»
- age_max: 27 — Page 1, Abstract — «among young adults (18-27 years)»
- pct_female: NR — Page 7, Conclusion — «this study doesn't include gender difference on respective subject»
- mode: online — Page 5, 4.3 Procedure — «questionnaire were filled through google form»
- attention_checks: NR — Page 5, 4.1 Sample — «interested participant filled google form with honesty»
- pub_status: journal — Page 1, header — «Interna2onal Journal of Interdisciplinary Approaches in Psychology (IJIAP) Vol. 3, Issue 9 September 2025»
- language: English — Full text — «A Study on Association between AI and Critical Thinking, Impulsivity, Dependence among Young Adults»
- funding_coi: NR — NA — «NR»
- notes: Single-author study. Sampling described as 'simple random sampling' but participants were 'interested' persons filling a Google Form, which suggests self-selection; sampling coded as stated by the author, reviewer should check. n = 55 in the text vs 56 in Tables 1-2. Keywords mention ChatGPT and DeepSeek, but the DAI asks about AI in general. Critical thinking (CTDS) correlates are not in the construct dictionary and were not extracted. No reliabilities reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The paper says 'simple random sampling', but recruitment was of interested participants through a Google Form with no sampling frame described. This looks like self-selected convenience sampling. — Page 5, 4.1 Sample — «The sample was collected by simple random sampling. In which interested participant filled google form with honesty.»
2. отклик: **unclear** — No response rate reported. — Page 5, 4.1 Sample — «The total number of samples obtained were 55 in the city of Chandigarh.»
3. валидная шкала зависимости от ИИ: **yes** — Published DAI scale (Morales-García et al., 2024). — Page 5, 4.2 Measures — «The Dependence Artificial Intelligence scale (DAI) (Morales-García et al., 2024), was used to measure the level of dependence»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega reported for DAI in this sample. — Page 5, 4.2 Measures — «The scale has five items which is formatted in Likert-type response manner»
5. валидные шкалы коррелятов: **yes** — Impulsivity measured with the published Impulsive Behavior Short Scale (Groskurth et al., 2022). — Page 5, 4.2 Measures — «The scale was developed by Groskurth, Nießen, Rammstedt, & Lechner (2022). The scale consists of 8 items»
6. качество данных: **unclear** — No attention checks or rules for invalid responses reported. — Page 5, 4.1 Sample — «interested participant filled google form with honesty»

Правки:
- 

Проверено: да

---

## ST094 · Bagheri 2025 · Psychology of Motivation Behavior and Health

Основной отчёт R3196: [текст](../../fulltext/text/R3196.txt) · [PDF](../../fulltext/pdf/R3196.pdf) — «Predicting the Phenomenon of Dependence to Artificial Intelligence Tools based on the Components of Dependence to Mobile Phone in Students (Case Study: ChatGPT)» — [DOI](https://doi.org/10.61838/jpmbh.131)
Расхождения в тексте: 1) The abstract and discussion say the mobile-dependence components predicted "42 percent" of the variance in AI dependence. Table 4 gives R = 0.72 and R² = 0.51 (0.72² ≈ 0.52), so the text and the table disagree. This affects only the regression, not the extracted correlations. 2) The Persian text says the assumptions of no multicollinearity (VIF = 1.36) and no autocorrelation of residuals (Durbin-Watson = 1.83) were "rejected" (رد شد). The values point to the assumptions being met, so the wording looks like an error. 3) The exclusion criteria list "completing its instruments," which looks like a garbled form of incomplete completion. 4) Alphas for the Cell Phone Addiction Scale in this sample are 0.75, 0.80 and 0.91. The alphas cited from Koo (2009; 0.87, 0.78, 0.86) and Atadokht & Ahmadi (2021; 0.66, 0.71, 0.80) are from other samples and were not used. 5) The English extended abstra…
Заметка ИИ: Main text is in Persian; quotes are given in Persian with English translations. The only eligible correlate is problematic smartphone use (three subscales of Koo's CPAS); no mental-health correlates were measured. The AI-dependence measure is a researcher-made instrument with limited validity evidence (expert content validity only), so the rob_3 rating is borderline.

### ST094-1 · Farhangian University students, Tehran, Iran (ChatGPT users), n=500
Отчёты: R3196 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R3196_1 · total (T4) | **problematic_smartphone_use** · Cell Phone Addiction Scale (Koo, 2009) - Withdrawal/Toleran… | pearson | **0.56** | **500** | 1 | Page 8, Table 3 | «کناره گیری/ تحمل وابستگی به ابزارهای هوش مصنوعی 56/0 001/0< [Withdrawal/tolerance / dependence to AI tools / 0.56 / <0.001]» |
| E2 | ADHOC_R3196_1 · total (T4) | **problematic_smartphone_use** · Cell Phone Addiction Scale (Koo, 2009) - Life Dysfunction (… | pearson | **0.42** | **500** | 1 | Page 8, Table 3 | «بدکارکردی زندگی 42/0 001/0< [Life dysfunction / 0.42 / <0.001]» |
| E3 | ADHOC_R3196_1 · total (T4) | **problematic_smartphone_use** · Cell Phone Addiction Scale (Koo, 2009) - Compulsion/Persist… | pearson | **0.51** | **500** | 1 | Page 8, Table 3 | «اجبار/ اصرار 51/0 001/0< [Compulsion/persistence / 0.51 / <0.001]» |

- E1: α ИИ 0.92, α коррелята 0.75; заметка: In the extracted text the RTL numbers appear reversed: '56/0' is 0.56. Two decimals only.
- E2: α ИИ 0.92, α коррелята 0.80; заметка: In the extracted text the RTL numbers appear reversed: '42/0' is 0.42. Two decimals only.
- E3: α ИИ 0.92, α коррелята 0.91; заметка: In the extracted text the RTL numbers appear reversed: '51/0' is 0.51. Two decimals only.

**Ключевые поля выборки:**
- **n_analysed: 500** — Page 3, Findings; Page 7, Findings — «In this study, 500 Farhangian University students participated.»
- **population: university_students** — Page 2, Methodology — «all male and female students of Farhangian University of Tehran city»
- **sampling: probability** — Page 2, Methodology — «a number of male and female universities were randomly selected from among all students of Farhangian University of Tehran, and then a number of classes were randomly selected from each university, and all students in the class were selected as samples if the…»
- **ai_system: general_chatbot** — Page 3, Methodology (inclusion criteria); Title — «the inclusion criteria included using ChatGPT for more than ten hours per week»

**Остальные поля:**
- country: IRN — Page 2, Methodology — «The research population was all male and female students of Farhangian University of Tehran city in the 2025-6 academic years»
- data_years: 2025-2026 (academic year 1404-1405 SH) — Page 2, Methodology; Page 6 — «students of Farhangian University of Tehran city in the 2025-6 academic years»
- design: cross-sectional — Page 2, Methodology — «This study was a descriptive from type of correlation.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 7-8, Table 1 — «سن 19-18 سال 183 60/36 [Age 18-19 years 183 36.60%]»
- age_sd: NR — Page 7-8, Table 1 — «Age reported only in categories»
- age_min: 18 (lowest age category 18-19) — Page 8, Table 1 — «سن 19-18 سال 183 60/36 [Age 18-19 years 183 36.60]»
- age_max: 25 (highest age category 24-25) — Page 8, Table 1 — «25-24 سال 74 80/14 [24-25 years 74 14.80]»
- pct_female: 52.6 — Page 3, Findings; Page 7, Table 1 — «Most of the Farhangian University students participating in the present study were female (263, equivalent to 52.60%)»
- mode: NR — Page 6-7, procedure — «از نمونه ها خواسته شد تا به ابزارهای پژوهش پاسخ دهند [the samples were asked to respond to the research instruments]»
- attention_checks: yes — Page 3, Methodology — «the exclusion criteria included withdrawing from the study, completing its instruments, and not responding to more than ten percent of the items.»
- pub_status: journal — Page 1 — «Psychology of Motivation, Behavior, and Health, Volume 3, Issue 4, PP 1-11»
- language: Persian (Farsi); English extended abstract on pp. 1-3 — Pages 1-3 (English abstract); Pages 4-10 (Persian full text) — «روش‌شناسی‌:این مطالعه توصیفی از نوع همبستگی بود. [Methodology: This study was descriptive of the correlational type.]»
- funding_coi: No funding (self-funded); no conflict of interest declared — Page 10, Conflict of interest / Funding — «هیچ تعارض منافعی وجود نداشت. ... این پژوهش بدون حامی مالی و با هزینه شخصی انجام شد. [There was no conflict of interest. ... This research was conducted without…»
- notes: Single author. Inclusion restricted to students using ChatGPT >10 h/week, not on academic probation, no drug addiction, no psychiatric medication, no psychological services in past 3 months. AI dependence: 12-item researcher-made questionnaire, 4-point (1-4), total 12-48; M = 27.72, SD = 4.43 (Table 2). Sampling is coded probability (random multistage cluster) as the authors describe it, but a fixed n of 500 was drawn from eligible students, so the reviewer should check. The only eligible correlates are the Koo (2009) Cell Phone Addiction Scale subscales (problematic_smartphone_use); no CPAS …

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **yes** — Multistage cluster sampling with random selection of universities and classes; all eligible students in selected classes included. Caveat: eligibility limited to heavy ChatGPT users and fixed n=500, so the sample may no… — Page 2, Methodology — «a number of male and female universities were randomly selected ... then a number of classes were randomly selected from each university, and all students in t…»
2. отклик: **unclear** — No response rate or number approached is reported, and non-responders are not compared. — Page 6, Methodology — «سپس تعداد500 دانشجوی دختر و پسر پس از بررسی مالک های ورود به مطالعه به عنوان نمونه انتخاب شدند [then 500 male and female students were selected as samples afte…»
3. валидная шкала зависимости от ИИ: **yes** — Borderline. A researcher-made 12-item questionnaire; this report gives only content validity (10 experts) and pilot alpha (n=20). No factor analysis and no separate development study. The reviewer may downgrade to 'no'. — Page 7, Instruments 2 — «روایی محتوایی ابزار توسط ده نفر از متخصصان و خبرگان آشنا به حیطه پژوهش تایید و پایایی آن ... در پایلت اولیه بر روی20 نفر ... 86/0 [Content validity was confirm…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.92 in the present sample (n=500). — Page 7, Instruments 2 — «و در پژوهش حاضر بر روی500 نفر از دانشجویان دانشگاه فرهنگیان92/0 به دست آمد [and in the present study on 500 students 0.92 was obtained]»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate is measured with the published Cell Phone Addiction Scale (Koo, 2009). — Page 7, Instruments 3 — «مقیاس اعتیاد به تلفن همراه توسطKoo (2009) با20 گویه در سه مولفه [Cell Phone Addiction Scale by Koo (2009) with 20 items in three components]»
6. качество данных: **yes** — Stated rule for invalid responses: participants not responding to more than 10% of items were excluded. — Page 3, Methodology; Page 6 — «the exclusion criteria included ... not responding to more than ten percent of the items.»

Правки:
- 

Проверено: да

---

## ST095 · Buniel 2025 · Frontiers in Education

Основной отчёт R3265: [текст](../../fulltext/text/R3265.txt) · [PDF](../../fulltext/pdf/R3265.pdf) — «Modeling the influence of AI dependence to research productivity among STEM undergraduate students: case of a state university in the Philippines» — [DOI](https://doi.org/10.3389/feduc.2025.1535466)
Расхождения в тексте: 1) Major problem: Table 6 (Fornell-Larcker) gives AID latent correlations close to zero (RS 0.004, RD 0.054, RSE 0.046, RP 0.032). But the SEM reports standardized paths AID→RS 0.644, AID→RD 0.646 and AID→RSE 0.670 (Table 7). The text says these paths explain 64–67% of the variance, which does not match a single-predictor beta of about 0.65 (R² ≈ .42). The AID row/column of Table 6 and the SEM results cannot both be correct; the reviewer should check before pooling. 2) The text cites 'Table 6 and Figure 3' for the structural results, but those results are in Table 7. 3) Table 4's column 'AVE2' appears to be √AVE, not AVE squared. The text gives the SFL threshold as '≤0.5', which looks like a typo for ≥0.5. 4) The methods say participants signed consent. The ethics statement says ethical review and written consent were not required. 5) Fit indices are reported after correlating error ter…
Заметка ИИ: The only eligible effect is a latent (CFA Fornell-Larcker) correlation between AI dependence and research self-efficacy. Whether research self-efficacy counts as 'academic self-efficacy' (self_efficacy key) needs the reviewer's judgement. Reliability is reported only as composite reliability, not alpha.

### ST095-1 · STEM undergraduates, North Eastern Mindanao State University (state university), Philippines, n=834
Отчёты: R3265 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_efficacy** · Research self-efficacy (RSE), 5 items adapted from Manitzas… | latent | **0.046** | **834** | 1 | Table 6 (p.8) | «RSE / 0.046 / 0.693 / 0.749 / 0.830» |

- E1: α ИИ CR = 0.874, α коррелята CR = 0.917; заметка: Inter-construct correlation from Fornell-Larcker table (CFA). Reliability is composite reliability, not alpha. Research self-efficacy is domain-specific; reviewer to confirm fit with self_efficacy key. Conflicts sharply with SEM path AID→RSE beta = 0.670 (see consistency_notes).

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.67 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 834** — p.1, Abstract; Table 1 — «an online survey was conducted and recorded 834 valid responses from STEM undergraduate students»
- **population: university_students** — p.4, Data and sample — «(b) currently enrolled in any STEM undergraduate degree program»
- **sampling: convenience** — p.4, Data and sample — «The survey was done following convenience sampling technique because of its practicality and cost-effectiveness. To recruit participants, a survey link was shared on university social media groups»
- **ai_system: mixed** — Table 2; p.4 — «Grammarly 259 31.06 ... ChatGPT 524 62.83 ... Google Scholar 310 37.17 ... Others 198 23.74»

**Остальные поля:**
- country: PHL — p.4, Data and sample — «a survey was administered among STEM undergraduate students enrolled in a higher education institution in the Philippines»
- data_years: 2024 — p.5, Data gathering procedure — «with access provided through a link shared from August until October 2024»
- design: cross-sectional — p.4, Data and sample — «To validate the structural model quantitatively, a survey was administered among STEM undergraduate students»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age (Years) 18 205 24.58»
- age_sd: NR — Table 1 — «NR»
- age_min: 18 — Table 1 — «Age (Years) 18 205 24.58»
- age_max: NR (top category '24 and above') — Table 1 — «24 and above 65 7.79»
- pct_female: 47.12 — Table 1 — «Female 393 47.12»
- mode: online — p.5, Data gathering procedure — «The researchers distributed the survey questionnaire through Google Form»
- attention_checks: NR — p.4-5 — «The participants were ensured to meet the inclusion criteria by using screening questions and obtaining informed consent before they proceeded answering.»
- pub_status: journal — p.1, header — «Frontiers in Education ... TYPE Original Research PUBLISHED 16 April 2025»
- language: English — Full text — «Modeling the influence of AI dependence to research productivity among STEM undergraduate students»
- funding_coi: No funding; no conflicts of interest declared — p.13, Funding; Conflict of interest — «The author(s) declare that no financial support was received for the research and/or publication of this article.»
- notes: Inclusion required having done research and having used AI tools for research. AI tools include ChatGPT (62.83%), Grammarly, Google Scholar, reference managers and others. The AID scale is the 5-item Morales-García et al. (2024) scale. Only latent (Fornell-Larcker) correlations are reported; there is no observed correlation matrix and no mean or SD of AID.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sampling via social media links, with peer sharing (snowball) — p.4, Data and sample — «The survey was done following convenience sampling technique ... participants were encouraged to share the survey with eligible peers.»
2. отклик: **unclear** — No response rate reported; only number of valid responses — p.1, Abstract — «recorded 834 valid responses from STEM undergraduate students»
3. валидная шкала зависимости от ИИ: **yes** — 5-item AI dependence scale from Morales-García et al. (2024) development and validation study — Table 3; References — «Morales-García ... (2024). Development and validation of a scale for dependence on artificial intelligence in university students.»
4. надёжность шкалы ИИ в выборке: **yes** — Composite reliability (omega-type) 0.874 for AID in this sample; no alpha reported — Table 4 — «AI dependence (AID) AID1 19.561 0.758 0.582 0.762 0.874»
5. валидные шкалы коррелятов: **no** — Research self-efficacy measured with 5 items compiled from two sources (Manitzas Hill et al., 2022; Wester et al., 2019, a faculty scale), not a single published instrument — Table 3 — «RSE1. I am confident to develop research questions. ... 5 Manitzas Hill et al. (2022) and Wester et al. (2019)»
6. качество данных: **unclear** — Only eligibility screening questions; no attention checks or stated rule for invalid responses, although 'valid responses' is mentioned — p.4, Data and sample — «The participants were ensured to meet the inclusion criteria by using screening questions»

Правки:
- 

Проверено: да

---

## ST096 · Chen 2025 · Frontiers in psychology

Основной отчёт R3300: [текст](../../fulltext/text/R3300.txt) — «Development and validation of the conversational AI dependence scale for Chinese college students.» — [DOI](https://doi.org/10.3389/fpsyg.2025.1621540)
Не выписано ИИ: Study 1 interview sample (n=31, qualitative only; screened with a single 9-point item). Study 1 item/EFA sample (n=547): CAIDS only, no correlates. Study 3 Sample 1 (n=1,081): only descriptives and group comparisons by demographics, no correlations with eligible correlates.
Расхождения в тексте: (1) Study 2 reliability: the total-score alpha (0.86) is lower than every subscale alpha (0.91, 0.91, 0.88, 0.94), which is implausible for a 20-item composite; the split-half for the total (0.81) is also lower. Study 3 reports alpha 0.96 for the total. (2) Table 3: the social media addiction x usage frequency cell (0.36) has no significance stars, unlike similar-sized cells. (3) The abstract and Discussion say CAI dependence significantly predicts lower subjective wellbeing. However, the zero-order r for the total score is -0.05 (ns; Table 4), and the text itself says only withdrawal and negative impact were significantly negatively correlated. Table 5 (adjusted) gives beta -0.14 with R2 = 0.40, an R2 that looks like a typo. (4) Study 1 Bartlett's test df = 190 matches 20 items, though the text describes it as the initial 51-item questionnaire. Table 1 lists 6 Uncontrollability items, …
Заметка ИИ: Two samples extracted: Study 2 (n=687; BSMAS, UCLA-3) and Study 3 Sample 2 (n=892; AIS, DASS-21 subscales, USP-SWB). In Study 2, the ECR-M16 combined 'insecure attachment' score was not extracted because it combines anxiety and avoidance (values listed in the sample notes). Functional difficulties have no dictionary key. Table 5 adjusted betas were not extracted. Values are as printed; the Unicode minus signs were changed to ASCII hyphens.

### ST096-1 · Study 2 validation sample, Chinese college students (Shanghai, Guangzhou, Xi'an, Haikou, Hefei), n=687
Отчёты: R3300 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | CAIDS · total (T4) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS) | pearson | **0.51** | **687** | 1 | Table 3 | «9. Social media addiction / 0.08* / 0.36 / 0.12** / 0.30*** / 0.52*** / 0.26*** / 0.53*** / 0.51***» |
| E2 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS) | pearson | **0.30** | **687** | 1 | Table 3 | «9. Social media addiction / 0.08* / 0.36 / 0.12** / 0.30*** / 0.52*** / 0.26*** / 0.53*** / 0.51***» |
| E3 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS) | pearson | **0.52** | **687** | 1 | Table 3 | «9. Social media addiction / 0.08* / 0.36 / 0.12** / 0.30*** / 0.52*** / 0.26*** / 0.53*** / 0.51***» |
| E4 | CAIDS · Mood modification (CAIDS-20) (T1) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS) | pearson | **0.26** | **687** | 1 | Table 3 | «9. Social media addiction / 0.08* / 0.36 / 0.12** / 0.30*** / 0.52*** / 0.26*** / 0.53*** / 0.51***» |
| E5 | CAIDS · Negative impact (CAIDS-20) (T1) | **problematic_social_media_use** · Bergen Social Media Addiction Scale (BSMAS) | pearson | **0.53** | **687** | 1 | Table 3 | «9. Social media addiction / 0.08* / 0.36 / 0.12** / 0.30*** / 0.52*** / 0.26*** / 0.53*** / 0.51***» |
| E6 | CAIDS · total (T4) | **loneliness** · UCLA Loneliness Scale, 3-item short version (Hughes et al.,… | pearson | **0.35** | **687** | 1 | Table 3 | «10. Loneliness / 0.07 / −0.04 / 0.12** / 0.13*** / 0.32*** / 0.15*** / 0.46*** / 0.35*** / 0.42***» |
| E7 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **loneliness** · UCLA Loneliness Scale, 3-item short version (Hughes et al.,… | pearson | **0.13** | **687** | 1 | Table 3 | «10. Loneliness / 0.07 / −0.04 / 0.12** / 0.13*** / 0.32*** / 0.15*** / 0.46*** / 0.35*** / 0.42***» |
| E8 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **loneliness** · UCLA Loneliness Scale, 3-item short version (Hughes et al.,… | pearson | **0.32** | **687** | 1 | Table 3 | «10. Loneliness / 0.07 / −0.04 / 0.12** / 0.13*** / 0.32*** / 0.15*** / 0.46*** / 0.35*** / 0.42***» |
| E9 | CAIDS · Mood modification (CAIDS-20) (T1) | **loneliness** · UCLA Loneliness Scale, 3-item short version (Hughes et al.,… | pearson | **0.15** | **687** | 1 | Table 3 | «10. Loneliness / 0.07 / −0.04 / 0.12** / 0.13*** / 0.32*** / 0.15*** / 0.46*** / 0.35*** / 0.42***» |
| E10 | CAIDS · Negative impact (CAIDS-20) (T1) | **loneliness** · UCLA Loneliness Scale, 3-item short version (Hughes et al.,… | pearson | **0.46** | **687** | 1 | Table 3 | «10. Loneliness / 0.07 / −0.04 / 0.12** / 0.13*** / 0.32*** / 0.15*** / 0.46*** / 0.35*** / 0.42***» |

- E1: α ИИ 0.86, α коррелята 0.84; заметка: The column is labelled 8. CAID
- E2: α ИИ 0.91, α коррелята 0.84; заметка: Column 4 (Uncontrollability)
- E3: α ИИ 0.91, α коррелята 0.84; заметка: Column 5 (Withdrawal symptoms)
- E4: α ИИ 0.88, α коррелята 0.84; заметка: Column 6 (Mood modification)
- E5: α ИИ 0.94, α коррелята 0.84; заметка: Column 7 (Negative impact)
- E6: α ИИ 0.86, α коррелята 0.85; заметка: Column 8 (CAID)
- E7: α ИИ 0.91, α коррелята 0.85; заметка: Column 4
- E8: α ИИ 0.91, α коррелята 0.85; заметка: Column 5
- E9: α ИИ 0.88, α коррелята 0.85; заметка: Column 6
- E10: α ИИ 0.94, α коррелята 0.85; заметка: Column 7

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: -0.15, -0.11, -0.05, 0.25, 0.27, 0.33, 0.39, 0.41, 0.42, 0.43, 0.44, 0.49 … — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 687** — Table 3 note — «N = 687.»
- **population: university_students** — Section 3.1 — «A total of 750 college students with prior experience using CAI were recruited»
- **sampling: convenience** — Section 3.1 — «A total of 750 college students with prior experience using CAI were recruited through convenience sampling»
- **ai_system: general_chatbot** — Section 1 Introduction — «Conversational artificial intelligence (CAI) technologies refer to intelligent behaviors manifested through language interactions such as conversations and question answering, as exhibited by Chatbot's and intelligent assistants.»

**Остальные поля:**
- country: CHN — Section 3.1 — «recruited through convenience sampling from Shanghai, Guangzhou, Xi'an, Haikou, and Hefei»
- data_years: NR — NA — «NR»
- design: validation study — Section 3 heading; 3.3.1 — «Study 2: reliability analyses and measurement invariance tests ... Confirmatory factor analysis (CFA) was conducted using Mplus 8.3»
- clinical_group: NA — NA — «NA»
- age_mean: 20.41 — Section 3.1 — «Participants ranged in age from 17 to 28 years (M = 20.41, SD = 1.63).»
- age_sd: 1.63 — Section 3.1 — «(M = 20.41, SD = 1.63)»
- age_min: 17 — Section 3.1 — «Participants ranged in age from 17 to 28 years»
- age_max: 28 — Section 3.1 — «Participants ranged in age from 17 to 28 years»
- pct_female: NR — Section 3.1 — «NR»
- mode: mixed — Section 2.2.2 (procedure; Study 2 procedure not separately … — «A questionnaire survey was then conducted through a combination of in-class and online group tests»
- attention_checks: yes — Section 3.1 — «After excluding questionnaires with patterned responses or incomplete information, 687 valid responses were retained»
- pub_status: journal — Header — «Venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1621540»
- language: English — Full text — «Development and validation of the conversational AI dependence scale for Chinese college students»
- funding_coi: 2025 Shaanxi Province Philosophy and Social Science Research Special Project (2025QN0472); Shaanxi University of Technology Doctoral Talent Start-up Project (SLGBSQDXM2501); authors declare no conflict of interest — Funding Statement; Conflict of interest — «financial support from the 2025 Shaanxi Province Philosophy and Social Science Research Special Project (Grant No. 2025QN0472) ... absence of any commercial or…»
- notes: Not extracted: correlations with 'Insecure attachment' (ECR-M16 total score, alpha .87; combines attachment anxiety and avoidance, so it fits neither attachment_anxiety nor attachment_avoidance alone): Uncontrollability .11, Withdrawal .44, Mood modification .10, Negative impact .53, CAID .39 (Table 3). The reviewer may decide whether to add it. Also not extracted: usage indicators (years, frequency, duration). Mode taken from the Study 1 procedure; Study 2 procedure is not described separately. Table 2 gives latent correlations among the CAIDS dimensions only (no correlates).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of college students — Section 3.1 — «recruited through convenience sampling from Shanghai, Guangzhou, Xi'an, Haikou, and Hefei»
2. отклик: **yes** — 91.60% of recruited participants gave valid responses. This is the proportion retained, not a response rate among invited students. — Section 3.1 — «687 valid responses were retained, representing 91.60% of the original sample»
3. валидная шкала зависимости от ИИ: **yes** — The CAIDS-20 was developed and validated in this report (EFA in Study 1, CFA in this sample) — Section 3.3.1 — «The CFA results indicated that the sample data fit the model reasonably well, supporting the four-factor model structure.»
4. надёжность шкалы ИИ в выборке: **yes** — Internal consistency for the total score and all subscales is .86 or higher — Section 3.3.4 — «the internal consistency coefficients for the total score and each dimension were 0.86, 0.91, 0.91, 0.88, and 0.94, respectively»
5. валидные шкалы коррелятов: **yes** — Extracted correlates measured with BSMAS and the UCLA 3-item Loneliness Scale (Hughes et al., 2004), both published — Sections 3.2.2-3.2.3 — «Bergen Social Media Addiction Scale (BSMAS) developed by Andreassen et al. (2016) ... short version of the University of California, Los Angeles (UCLA) Lonelin…»
6. качество данных: **yes** — Stated rule for excluding invalid responses (patterned or incomplete) — Section 3.1 — «After excluding questionnaires with patterned responses or incomplete information»

Правки:
- 

Проверено: да

### ST096-2 · Study 3 Sample 2, Chinese college students (Xi'an, Haikou), n=892
Отчёты: R3300 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | CAIDS · total (T4) | **sleep_quality** · Athens Insomnia Scale (sleep problems) | pearson | **0.35** | **892** | 1 | Table 4 | «CAID / 0.35*** / 0.74*** / 0.73*** / 0.62*** / 0.43*** / 0.49*** / 0.42*** / −0.05» |
| E2 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **sleep_quality** · Athens Insomnia Scale (sleep problems) | pearson | **0.24** | **892** | 1 | Table 4 | «Uncontrollability / 0.24*** / 0.55*** / 0.54*** / 0.44*** / 0.25*** / 0.33*** / 0.26*** / 0.06» |
| E3 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **sleep_quality** · Athens Insomnia Scale (sleep problems) | pearson | **0.35** | **892** | 1 | Table 4 | «Withdrawal symptoms / 0.35*** / 0.64*** / 0.63*** / 0.59*** / 0.41*** / 0.46*** / 0.44*** / −0.11**» |
| E4 | CAIDS · Mood modification (CAIDS-20) (T1) | **sleep_quality** · Athens Insomnia Scale (sleep problems) | pearson | **0.17** | **892** | 1 | Table 4 | «Mood modification / 0.17*** / 0.60*** / 0.59*** / 0.41*** / 0.27*** / 0.33*** / 0.25*** / 0.05» |
| E5 | CAIDS · Negative impact (CAIDS-20) (T1) | **sleep_quality** · Athens Insomnia Scale (sleep problems) | pearson | **0.45** | **892** | 1 | Table 4 | «Negative impact / 0.45*** / 0.78*** / 0.79*** / 0.71*** / 0.54*** / 0.57*** / 0.50*** / −0.15***» |
| E6 | CAIDS · total (T4) | **depression** · DASS-21 Depression (Chinese version, Gong et al., 2010) | pearson | **0.43** | **892** | 1 | Table 4 | «CAID / 0.35*** / 0.74*** / 0.73*** / 0.62*** / 0.43*** / 0.49*** / 0.42*** / −0.05» |
| E7 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **depression** · DASS-21 Depression (Chinese version, Gong et al., 2010) | pearson | **0.25** | **892** | 1 | Table 4 | «Uncontrollability / 0.24*** / 0.55*** / 0.54*** / 0.44*** / 0.25*** / 0.33*** / 0.26*** / 0.06» |
| E8 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **depression** · DASS-21 Depression (Chinese version, Gong et al., 2010) | pearson | **0.41** | **892** | 1 | Table 4 | «Withdrawal symptoms / 0.35*** / 0.64*** / 0.63*** / 0.59*** / 0.41*** / 0.46*** / 0.44*** / −0.11**» |
| E9 | CAIDS · Mood modification (CAIDS-20) (T1) | **depression** · DASS-21 Depression (Chinese version, Gong et al., 2010) | pearson | **0.27** | **892** | 1 | Table 4 | «Mood modification / 0.17*** / 0.60*** / 0.59*** / 0.41*** / 0.27*** / 0.33*** / 0.25*** / 0.05» |
| E10 | CAIDS · Negative impact (CAIDS-20) (T1) | **depression** · DASS-21 Depression (Chinese version, Gong et al., 2010) | pearson | **0.54** | **892** | 1 | Table 4 | «Negative impact / 0.45*** / 0.78*** / 0.79*** / 0.71*** / 0.54*** / 0.57*** / 0.50*** / −0.15***» |
| E11 | CAIDS · total (T4) | **anxiety** · DASS-21 Anxiety (Chinese version, Gong et al., 2010) | pearson | **0.49** | **892** | 1 | Table 4 | «CAID / 0.35*** / 0.74*** / 0.73*** / 0.62*** / 0.43*** / 0.49*** / 0.42*** / −0.05» |
| E12 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **anxiety** · DASS-21 Anxiety (Chinese version, Gong et al., 2010) | pearson | **0.33** | **892** | 1 | Table 4 | «Uncontrollability / 0.24*** / 0.55*** / 0.54*** / 0.44*** / 0.25*** / 0.33*** / 0.26*** / 0.06» |
| E13 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **anxiety** · DASS-21 Anxiety (Chinese version, Gong et al., 2010) | pearson | **0.46** | **892** | 1 | Table 4 | «Withdrawal symptoms / 0.35*** / 0.64*** / 0.63*** / 0.59*** / 0.41*** / 0.46*** / 0.44*** / −0.11**» |
| E14 | CAIDS · Mood modification (CAIDS-20) (T1) | **anxiety** · DASS-21 Anxiety (Chinese version, Gong et al., 2010) | pearson | **0.33** | **892** | 1 | Table 4 | «Mood modification / 0.17*** / 0.60*** / 0.59*** / 0.41*** / 0.27*** / 0.33*** / 0.25*** / 0.05» |
| E15 | CAIDS · Negative impact (CAIDS-20) (T1) | **anxiety** · DASS-21 Anxiety (Chinese version, Gong et al., 2010) | pearson | **0.57** | **892** | 1 | Table 4 | «Negative impact / 0.45*** / 0.78*** / 0.79*** / 0.71*** / 0.54*** / 0.57*** / 0.50*** / −0.15***» |
| E16 | CAIDS · total (T4) | **stress** · DASS-21 Stress (Chinese version, Gong et al., 2010) | pearson | **0.42** | **892** | 1 | Table 4 | «CAID / 0.35*** / 0.74*** / 0.73*** / 0.62*** / 0.43*** / 0.49*** / 0.42*** / −0.05» |
| E17 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **stress** · DASS-21 Stress (Chinese version, Gong et al., 2010) | pearson | **0.26** | **892** | 1 | Table 4 | «Uncontrollability / 0.24*** / 0.55*** / 0.54*** / 0.44*** / 0.25*** / 0.33*** / 0.26*** / 0.06» |
| E18 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **stress** · DASS-21 Stress (Chinese version, Gong et al., 2010) | pearson | **0.44** | **892** | 1 | Table 4 | «Withdrawal symptoms / 0.35*** / 0.64*** / 0.63*** / 0.59*** / 0.41*** / 0.46*** / 0.44*** / −0.11**» |
| E19 | CAIDS · Mood modification (CAIDS-20) (T1) | **stress** · DASS-21 Stress (Chinese version, Gong et al., 2010) | pearson | **0.25** | **892** | 1 | Table 4 | «Mood modification / 0.17*** / 0.60*** / 0.59*** / 0.41*** / 0.27*** / 0.33*** / 0.25*** / 0.05» |
| E20 | CAIDS · Negative impact (CAIDS-20) (T1) | **stress** · DASS-21 Stress (Chinese version, Gong et al., 2010) | pearson | **0.50** | **892** | 1 | Table 4 | «Negative impact / 0.45*** / 0.78*** / 0.79*** / 0.71*** / 0.54*** / 0.57*** / 0.50*** / −0.15***» |
| E21 | CAIDS · total (T4) | **wellbeing** · Ultra-Short Protocol for Measuring Subjective Wellbeing (US… | pearson | **-0.05** | **892** | 1 | Table 4 | «CAID / 0.35*** / 0.74*** / 0.73*** / 0.62*** / 0.43*** / 0.49*** / 0.42*** / −0.05» |
| E22 | CAIDS · Uncontrollability (CAIDS-20) (T1) | **wellbeing** · Ultra-Short Protocol for Measuring Subjective Wellbeing (US… | pearson | **0.06** | **892** | 1 | Table 4 | «Uncontrollability / 0.24*** / 0.55*** / 0.54*** / 0.44*** / 0.25*** / 0.33*** / 0.26*** / 0.06» |
| E23 | CAIDS · Withdrawal symptoms (CAIDS-20) (T1) | **wellbeing** · Ultra-Short Protocol for Measuring Subjective Wellbeing (US… | pearson | **-0.11** | **892** | 1 | Table 4 | «Withdrawal symptoms / 0.35*** / 0.64*** / 0.63*** / 0.59*** / 0.41*** / 0.46*** / 0.44*** / −0.11**» |
| E24 | CAIDS · Mood modification (CAIDS-20) (T1) | **wellbeing** · Ultra-Short Protocol for Measuring Subjective Wellbeing (US… | pearson | **0.05** | **892** | 1 | Table 4 | «Mood modification / 0.17*** / 0.60*** / 0.59*** / 0.41*** / 0.27*** / 0.33*** / 0.25*** / 0.05» |
| E25 | CAIDS · Negative impact (CAIDS-20) (T1) | **wellbeing** · Ultra-Short Protocol for Measuring Subjective Wellbeing (US… | pearson | **-0.15** | **892** | 1 | Table 4 | «Negative impact / 0.45*** / 0.78*** / 0.79*** / 0.71*** / 0.54*** / 0.57*** / 0.50*** / −0.15***» |

- E1: **направление: reversed (higher = poorer sleep quality / insomnia)**; α ИИ 0.96, α коррелята 0.83; заметка: Alpha is reported jointly for Samples 1 and 2
- E2: **направление: reversed (higher = poorer sleep quality / insomnia)**; α ИИ NR, α коррелята 0.83
- E3: **направление: reversed (higher = poorer sleep quality / insomnia)**; α ИИ NR, α коррелята 0.83
- E4: **направление: reversed (higher = poorer sleep quality / insomnia)**; α ИИ NR, α коррелята 0.83
- E5: **направление: reversed (higher = poorer sleep quality / insomnia)**; α ИИ NR, α коррелята 0.83
- E6: α ИИ 0.96, α коррелята 0.92; заметка: Alpha is reported jointly for Samples 1 and 2
- E7: α ИИ NR, α коррелята 0.92
- E8: α ИИ NR, α коррелята 0.92
- E9: α ИИ NR, α коррелята 0.92
- E10: α ИИ NR, α коррелята 0.92
- E11: α ИИ 0.96, α коррелята 0.92; заметка: Alpha is reported jointly for Samples 1 and 2
- E12: α ИИ NR, α коррелята 0.92
- E13: α ИИ NR, α коррелята 0.92
- E14: α ИИ NR, α коррелята 0.92
- E15: α ИИ NR, α коррелята 0.92
- E16: α ИИ 0.96, α коррелята 0.91; заметка: Alpha is reported jointly for Samples 1 and 2
- E17: α ИИ NR, α коррелята 0.91
- E18: α ИИ NR, α коррелята 0.91
- E19: α ИИ NR, α коррелята 0.91
- E20: α ИИ NR, α коррелята 0.91
- E21: α ИИ 0.96, α коррелята 0.92; заметка: Not significant. Alpha is reported jointly for Samples 1 and 2.
- E22: α ИИ NR, α коррелята 0.92; заметка: Not significant
- E23: α ИИ NR, α коррелята 0.92
- E24: α ИИ NR, α коррелята 0.92; заметка: Not significant
- E25: α ИИ NR, α коррелята 0.92

**⚠ Проверка скриптом (обратите внимание):**
- E1, E2, E3, E4, E5: шкала коррелята «наоборот» (знак перевернём в анализе): проверьте направление
- E2, E4, E5, E22, E24: этого числа нет в независимом проходе ИИ по полному тексту — сверьте с таблицей
- в независимом проходе были ещё числа: 0.13, 0.15, 0.30, 0.32, 0.39, 0.51, 0.52, 0.53 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 892** — Table 4 note — «N = 892.»
- **population: university_students** — Section 4.1 — «A total of 950 college students with prior experience using CAI were recruited»
- **sampling: convenience** — Section 4.1 — «A total of 950 college students with prior experience using CAI were recruited through convenience cluster sampling from Xi'an and Haikou.»
- **ai_system: general_chatbot** — Section 1; Section 4.5.1 — «as exhibited by Chatbot's and intelligent assistants ... the students primarily used CAI for virtual assistance and daily communication, answering questions and information retrieval, writing and creative generation»

**Остальные поля:**
- country: CHN — Section 4.1 — «recruited through convenience cluster sampling from Xi'an and Haikou»
- data_years: NR — NA — «NR»
- design: cross-sectional — Section 5.1 — «First, while the cross-sectional design offers valuable theoretical insights, it limits the ability to make causal inferences.»
- clinical_group: NA — NA — «NA»
- age_mean: 19.97 — Section 4.1, Sample 2 — «Participants' ages ranged from 17 to 25 years (M = 19.97, SD = 1.63).»
- age_sd: 1.63 — Section 4.1, Sample 2 — «(M = 19.97, SD = 1.63)»
- age_min: 17 — Section 4.1, Sample 2 — «Participants' ages ranged from 17 to 25 years»
- age_max: 25 — Section 4.1, Sample 2 — «Participants' ages ranged from 17 to 25 years»
- pct_female: 59.00 — Section 4.1, Sample 2 — «892 valid questionnaires were retained (526 female students, 59.00%)»
- mode: mixed — Section 4.3 — «a questionnaire survey was conducted using a combination of in-class and online group tests»
- attention_checks: yes — Section 4.1, Sample 2 — «After excluding questionnaires with patterned responses or incomplete information, 892 valid questionnaires were retained»
- pub_status: journal — Header — «Venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1621540»
- language: English — Full text — «Development and validation of the conversational AI dependence scale for Chinese college students»
- funding_coi: 2025 Shaanxi Province Philosophy and Social Science Research Special Project (2025QN0472); Shaanxi University of Technology Doctoral Talent Start-up Project (SLGBSQDXM2501); authors declare no conflict of interest — Funding Statement; Conflict of interest — «financial support from the 2025 Shaanxi Province Philosophy and Social Science Research Special Project (Grant No. 2025QN0472) ... absence of any commercial or…»
- notes: CAIDS-20 alpha 0.96 is reported jointly for Samples 1 and 2; no subscale alphas are given for Study 3. Not extracted (no dictionary key): Functional Difficulties Scale subscales (friendship, family, academic difficulties). Table 5 betas are adjusted for covariates (gender, age, grade, usage intensity), so they were not extracted. Sleep problems were measured with the Athens Insomnia Scale (higher = poorer sleep), so they are coded as reversed sleep_quality.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience cluster sampling of college students — Section 4.1 — «recruited through convenience cluster sampling from Xi'an and Haikou»
2. отклик: **yes** — Reported effective response rate of 93.89% (valid questionnaires out of those recruited) — Section 4.1, Sample 2 — «yielding an effective response rate of 93.89%»
3. валидная шкала зависимости от ИИ: **yes** — The CAIDS-20 was developed and validated in this report (Studies 1-2) — Section 3.3.1; 4.2.5 — «In both Samples 1 and 2, the CAIDS-20 demonstrated strong reliability and validity, with a Cronbach's alpha of 0.96.»
4. надёжность шкалы ИИ в выборке: **yes** — Total-score alpha of .96, reported for Samples 1 and 2 together — Section 4.2.5 — «In both Samples 1 and 2, the CAIDS-20 demonstrated strong reliability and validity, with a Cronbach's alpha of 0.96.»
5. валидные шкалы коррелятов: **yes** — Extracted correlates measured with published instruments: Athens Insomnia Scale, Chinese DASS-21, USP-SWB — Sections 4.2.1, 4.2.3, 4.2.4 — «Chinese version of the Depression-Anxiety-Stress Scale (DASS-21 ...) revised by Gong et al. (2010) ... Ultra-Short Protocol for Measuring Subjective Wellbeing …»
6. качество данных: **yes** — Stated rule for excluding invalid responses (patterned or incomplete) — Section 4.1, Sample 2 — «After excluding questionnaires with patterned responses or incomplete information»

Правки:
- 

Проверено: да

---

## ST097 · Dr. Syeda Razia Bukhari, Sana Batool, Iqra Shahab, Rabia Jalil, Amna Arshad, Syeda Qareena Zahra, Sabahat Karim, Nimra Jamil, Naser Khan 2025 · Zenodo

Основной отчёт R3377: [текст](../../fulltext/text/R3377.txt) · [PDF](../../fulltext/pdf/R3377.pdf) — «ROLE OF AI DEPENDENCY IN PSYCHOLOGICAL DISTRESS AND ACADEMIC PERFORMANCE AMONG UNIVERSITY STUDENTS» — [DOI](https://doi.org/10.5281/zenodo.14998024)
Расхождения в тексте: 1) Table 1's title says N=250, but its total row and Table 2 say N=300. The gender counts (137+164=301) and percentages (47%+54.7%) do not add up to 300 or 100%. 2) In the text, stress is reported as β=2.08; in Table 4.1, .208 appears in the Beta column of the stress row and 2.08 in a different column. 3) Depression's step R² is given as .42 in the text and table, which is implausible for an incremental R² (.042 is likely). 4) The abstract says 'Random sampling', while the Method describes email or online survey invitations. 5) The abstract mentions academic adjustment and a mediating role, but neither is analysed. 6) Table 2 reports age as coded categories (M=1.93, range 1-5), not years.
Заметка ИИ: No zero-order correlations are reported. The only statistics are from a stepwise multiple regression (Table 4.1). The anxiety, stress and depression betas come from later steps that already contain academic performance and other predictors, so they are multivariable betas and are not extracted. Only the Step 1 beta (academic performance, β=.805) is a single-predictor coefficient, and academic performance is not in the construct dictionary. The reviewer may want to contact the authors for a correlation matrix.

### ST097-1 · University students, SZABIST Islamabad authors (country not stated), n=300
Отчёты: R3377 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 300** — Page 6, Table 1; Table 4.1 (df=298) — «Total 300 100.0»
- **population: university_students** — Page 5, Participants & procedure — «the study comprises a sample of university students from a range of academic fields.»
- **sampling: probability** — Page 1, Abstract — «Random sampling was used to choose the sample.»
- **ai_system: ai_unspecified** — Page 6, Measures, AI Dependency Scale — «need for AI system validation, and worries about AI replacing human talents are some of the features of AI dependency that are measured by the scale.»

**Остальные поля:**
- country: NR — Page 1, author affiliations — «Shaheed Zulfikar Ali Bhutto Institute of Science and Technology, H-8/4 Islamabad (SZABIST, Islamabad Campus)»
- data_years: NR — Page 5, Participants & procedure — «the data was gathered over the course of four weeks.»
- design: cross-sectional — Page 5, Participants & procedure — «This study employs a quantitative research design utilizing a cross-sectional survey method»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 6, Table 2 — «Age 1.93 .976 1 5»
- age_sd: NR — Page 6, Table 2 — «Age 1.93 .976 1 5»
- age_min: 18 — Page 1, Abstract — «There were 300 people in the sample, ranging in age from 18 to 37.»
- age_max: 37 — Page 1, Abstract — «There were 300 people in the sample, ranging in age from 18 to 37.»
- pct_female: 54.7 — Page 6, Table 1 — «Male 137 47% Female 164 54.7 Total 300 100.0»
- mode: online — Page 5, Participants & procedure — «Participants received email invites or an online survey to complete.»
- attention_checks: NR — Pages 5-6, Method — «The data was analyzed using the Statistical Package for the Social Sciences (SPSS) 27 version.»
- pub_status: journal — Page 1, header — «Volume 3, Issue 3, 2025 https://theijssb.com | Bukhari et al., 2025 | Page 286»
- language: English — Full text — «ROLE OF AI DEPENDENCY IN PSYCHOLOGICAL DISTRESS AND ACADEMIC PERFORMANCE AMONG UNIVERSITY STUDENTS»
- funding_coi: NR — Full text — «NR»
- notes: Country is not stated for the sample. All authors are at SZABIST Islamabad, which suggests Pakistan (PAK), but this is inferred, not reported. Sampling is coded 'probability' only because the abstract says 'random sampling'; the Method describes email or online survey invitations, so the reviewer should check this code. Age in Table 2 is coded in categories, so no mean age in years is available. No zero-order correlations are reported (stepwise regression only), so no effects were extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The abstract says 'random sampling', but no sampling frame or procedure is described, and the Method describes email invitations or an online survey with a target sample size, which suggests convenience recruitment. — Page 1, Abstract; Page 5, Participants & procedure — «Random sampling was used to choose the sample. ... Participants received email invites or an online survey to complete.»
2. отклик: **unclear** — No response rate is reported. — Page 5, Participants & procedure — «With a target sample size of 300 students»
3. валидная шкала зависимости от ИИ: **yes** — The 5-item AI Dependency Scale, with Zhang et al. (2024) in the reference list (instrument family ZHANG5), has a published development study. However, the Measures section does not cite it, and its description of the sc… — Page 6, Measures; Page 9, References — «Five items on the AI Dependency Scale are scored on a 5-point Likert scale»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for this sample. Only item-total correlations of 0.80 are mentioned, and it is unclear whether they come from this sample. — Page 6, Measures — «its good psychometric features, which include item-total correlations of 0.80.»
5. валидные шкалы коррелятов: **yes** — Depression, anxiety and stress were measured with the DASS-21, a published instrument. No effects could be extracted, however. — Pages 5-6, Measures — «Depression, Anxiety, and Stress Scale (DASS-21). It has three subscales, each with seven items»
6. качество данных: **unclear** — No attention checks or rules for screening invalid responses are reported. — Pages 5-6, Method — «Frequencies and Descriptive statistics were tabulated for socio-demographic characteristics»

Правки:
- 

Проверено: да

---

## ST098 · Du 2025 · Journal of Computer Assisted Learning

Основной отчёт R3379: [текст](../../fulltext/text/R3379.txt) — «Are Teachers Addicted to AI ? Analysing Factors Influencing Dependence on Generative AI Through the I‐ PACE Model» — [DOI](https://doi.org/10.1002/jcal.70174)
Не выписано ИИ: There is no separate eligible sample. The 10-educator pretest (questionnaire clarity review only, no data reported) was not extracted.
Расхождения в тексте: (1) Gender: the text says 84.57% female. Table 2 lists Female 1480 at 85.57% and Male 270 at 15.43%. Since 1480/1750 = 84.57% and 85.57 + 15.43 > 100, the table percentage is a typo; 84.57 was recorded. (2) Table 4 correlations look internally inconsistent. Every GA correlation is negative (SE −0.65, NC −0.86, MR −0.84, PU −0.88, CA −0.06, PA −0.92), yet all GA items are worded in the addiction direction and the SEM gives a strong positive CA→GA path (β = 0.75) against a near-zero latent r(CA, GA) = −0.06. (3) The text says discriminant validity holds under Fornell–Larcker, but several off-diagonal values equal or exceed the square roots of AVE: PU–PA = 0.94 (diagonal PU 0.94, PA 0.93); GA–PA = |−0.92| > 0.87; GA–PU = |−0.88| > 0.87; NC–GA = |−0.86| near 0.87. (4) The instrument list describes PUCAI as 6 items; this report uses 4 adapted GA items. No figure-only coefficients other than …
Заметка ИИ: One sample (1750 teachers, China, 2025). Only a latent Fornell–Larcker correlation matrix is reported, and no correlate is a standard psychological measure. One tentative effect was extracted: GA with AI-specific mood regulation as escapism/coping motive. AI-specific self-efficacy, AI-specific positive affect, need for cognition, perceived usefulness and cognitive absorption were not extracted under the dictionary rules. The negative GA signs in Table 4 look doubtful and need the reviewer's attention.

### ST098-1 · Teachers using generative AI, Huanghua (Hebei), China, n=1750
Отчёты: R3379 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | PUCAI · total (T1) | **escapism_motive** · Mood regulation (MR), 3 AI-specific items adapted from Hutc… | latent | **−0.84** | **1750** | 1 | Table 4 (p.10), row GA, column MR | «GA −0.65 −0.86 −0.84 −0.88 −0.06 −0.92 0.87 (columns SE NC MR PU CA PA GA)» |

- E1: α ИИ 0.93, α коррелята 0.95; заметка: Fornell–Larcker matrix (sqrt AVE on the diagonal), so treated as latent. Eligibility as escapism/coping motive is tentative. The negative sign is implausible given the item content and the positive SEM paths; check the sign (see consistency_notes). Matrix gives two decimals only.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: -0.65 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 1750** — p.6, 3.3; p.8, 4.1 — «Over the period, 1750 valid responses were collected after a rigorous data- cleaning process.»
- **population: employees** — p.6, 3.3; Table 2 — «targeting teachers who actively use or have experience with generative AI in their teaching practices»
- **sampling: convenience** — p.6, 3.3 Data Collection — «A structured online questionnaire was distributed primarily through internal WeChat groups managed by a local instructional supervisor, which includes nearly all teachers in Huanghua. Additional distribution channels included institutional email lists and sma…»
- **ai_system: general_chatbot** — Table 2; p.8, 4.1 — «DeepSeek and ERNIE Bot are the most frequently used tools, while other platforms such as ChatGPT, 360 Zhinao and Tencent Hunyuan Assistant also feature prominently.»

**Остальные поля:**
- country: CHN — p.6, 3.3 Data Collection — «The survey was conducted in Huanghua, a county- level city located in Hebei Province, China»
- data_years: 2025 — p.6, 3.3 Data Collection — «from 15 January 2025 to 10 February 2025»
- design: cross-sectional — p.13, 5.4 Limitations — «the use of a cross- sectional design restricts the ability to determine causal relationships»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 2 — «Age Below 25 145 8.29% 25–34 499 28.51% 35–44 511 29.20% 45–54 511 29.20% Above 55 84 4.80%»
- age_sd: NR — Table 2 — «Age reported only in categories»
- age_min: NR — Table 2 — «Below 25 145 8.29%»
- age_max: NR — Table 2 — «Above 55 84 4.80%»
- pct_female: 84.57 — p.8, 4.1; Table 2 — «84.57% of participants identify as female and 15.43% as male; Table 2: Gender Female 1480 85.57%»
- mode: online — p.6, 3.3 — «A structured online questionnaire was distributed primarily through internal WeChat groups»
- attention_checks: yes — p.6, 3.3 — «Careless responses (Ward and Meade 2023), as well as those from participants who had never used or were completely unfamiliar with generative AI, were removed …»
- pub_status: journal — p.1, header — «Journal of Computer Assisted Learning, 2026; 42:e70174 ... ORIGINAL ARTICLE OPEN ACCESS»
- language: English — Full text — «Are Teachers Addicted to AI? Analysing Factors Influencing Dependence on Generative AI Through the I- PACE Model»
- funding_coi: No funding reported; authors declare no conflicts of interest — p.14, Funding; Conflicts of Interest — «Funding The authors have nothing to report. Conflicts of Interest The authors declare no conflicts of interest.»
- notes: GA (generative AI addiction) is a 4-item adaptation of Hu, Mao & Kim (2023), not the 6-item version; items rewritten for teaching tasks. Only a latent (Fornell–Larcker) correlation matrix is reported. Most constructs in the matrix were not extracted: self-efficacy is AI-specific self-efficacy (Wang & Chuang 2024, 'confidence in my ability to use generative AI tools'), which the dictionary excludes; need for cognition, perceived usefulness and cognitive absorption have no dictionary key; positive affect is AI-specific affect ('I feel excited when ... using generative AI'), not wellbeing. Mood …

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online questionnaire sent through WeChat groups, email lists and educator networks; no probability sampling, and no response count against the roughly full teacher population. — p.6, 3.3 — «distributed primarily through internal WeChat groups managed by a local instructional supervisor, which includes nearly all teachers in Huanghua. Additional di…»
2. отклик: **unclear** — Neither the number invited nor a response rate is reported; only the number of valid responses is given. — p.6, 3.3 — «Over the period, 1750 valid responses were collected after a rigorous data- cleaning process.»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from a published instrument (Hu et al., 2023), and a CFA in this report gives loadings, CR and AVE (shortened to 4 items and reworded). — Table 1; Table 3 — «Generative AI addiction (GA) ... Hu et al. (2023); GA1 0.88 0.93 0.93 0.77»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.93 for GA in this sample. — Table 3 — «Generative AI addiction (GA) GA1 0.88 0.93 0.93 0.77»
5. валидные шкалы коррелятов: **unclear** — The only extracted correlate (mood regulation) uses newly worded AI-specific items said to be adapted from Hutchison & Gunthert (2013), whose scale measures beliefs about automatic mood regulation. The content differs a… — Table 1; p.6, 3.2 — «their corresponding measurement items were adapted from validated sources ... MR1 I use generative AI tools to reduce the stress of preparing lesson materials.…»
6. качество данных: **yes** — Careless responders were screened out (method not detailed). — p.6, 3.3 — «Careless responses (Ward and Meade 2023) ... were removed to ensure data quality.»

Правки:
- 

Проверено: да

---

## ST099 · Estrada-Araoz 2025 · Sapienza International Journal of Interdisciplinary Studies

Основной отчёт R3420: [текст](../../fulltext/text/R3420.txt) · [PDF](../../fulltext/pdf/R3420.pdf) — «Academic self-efficacy and dependence on artificial intelligence in a sample of university students» — [DOI](https://doi.org/10.51798/sijis.v6i1.916)
Расхождения в тексте: Sampling: the abstract (all three languages) says participants were "selected through probabilistic sampling", but Methods (p.3) says "non-probabilistic convenience sampling"; I coded the Methods version (convenience). Table 6 (p.6): the age-group difference in academic self-efficacy (24.36 vs 30.65, SDs 4.968/5.878) gives a much larger Cohen's d than the reported 0.551, so the reported d values look doubtful (this does not affect the extracted correlation). The 'Originality/value' box on p.1 describes mentoring and does not fit this study (boilerplate error). The correlation of -0.299 is the same in the abstract, the text and Table 7.
Заметка ИИ: One sample, one effect (DAI total × academic self-efficacy, r = -0.299, n = 186). The report gives no reliability for either measure in this sample.

### ST099-1 · Private university branch, Puerto Maldonado, Peru, students (n=186)
Отчёты: R3420 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **self_efficacy** · Academic Situations Specific Perceived Self-Efficacy Scale … | pearson | **-0.299** | **186** | 1 | Page 6, Table 7 | «Academic self-efficacy / Pearson correlation / 1 / -0.299** / Sig. (bilateral) / 0.000 / N / 186» |

- E1: заметка: Same value appears in the abstract and text. Sample-specific alphas not reported (cited alphas are .870 for DAI from the original authors and .800 for ASSPSE from Domínguez 2016).

**Ключевые поля выборки:**
- **n_analysed: 186** — Page 6, Table 7 — «N | 186 | 186»
- **population: university_students** — Page 3, Population and sample — «The population consisted of 1400 students enrolled in the 2024-II cycle in the branch of a private university»
- **sampling: convenience** — Page 3, Population and sample — «the sample consisted of 186 students, selected by non-probabilistic convenience sampling»
- **ai_system: ai_unspecified** — Page 4, Instruments — «assesses the degree to which students depend on AI in their daily academic activities»

**Остальные поля:**
- country: PER — Page 3, Population and sample — «the branch of a private university in the city of Puerto Maldonado (Peru)»
- data_years: 2024 — Page 3, Population and sample — «1400 students enrolled in the 2024-II cycle»
- design: cross-sectional — Page 3, Design — «the study was of a cross-sectional correlational type... collecting data at a single point in time»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 3, Table 1 — «Between 16 and 24 years old | 166 | 89.2»
- age_sd: NR — Page 3, Table 1 — «Between 16 and 24 years old | 166 | 89.2»
- age_min: NR (only age bands reported; lowest band starts at 16) — Page 3, Table 1 — «Between 16 and 24 years old | 166 | 89.2»
- age_max: NR (only age bands reported; highest band ends at 34) — Page 3, Table 1 — «Between 25 and 34 years old | 20 | 10.8»
- pct_female: 63.4 — Page 3, Table 1 — «63.4% were female and 36.6% were male»
- mode: online — Page 4, Instruments; Procedures — «they were structured in a form of the Google Forms platform... students were invited to participate in the study through the WhatsApp messaging platform»
- attention_checks: NR — Page 4, Procedures; Data analysis — «When the participation of the 186 students required for the sample was achieved, access to the survey was deactivated.»
- pub_status: journal — Page 1, header — «Sapienza: International Journal of Interdisciplinary Studies, 6(1), e25008»
- language: English (abstract also in Portuguese and Spanish) — Page 1-9 — «Academic self-efficacy and dependence on artificial intelligence in a sample of university students»
- funding_coi: No funding; no conflict of interest declared — Page 9, end matter — «There is no conflict of interest Source of funding There is no source of funding»
- notes: Only one correlate (academic self-efficacy). The report gives no alpha for this sample; the alphas it cites (DAI .870; ASSPSE .800) are from the original or earlier validation studies. Age is reported only in bands (16-24: 89.2%; 25-34: 10.8%). The sample includes some 16-17-year-olds in the university. The abstract says probabilistic sampling, but Methods says convenience; I coded convenience.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Methods describe non-probabilistic convenience sampling with an online invitation via WhatsApp (the abstract says probabilistic, which conflicts) — Page 3, Population and sample — «selected by non-probabilistic convenience sampling»
2. отклик: **unclear** — No response rate reported; the survey was closed once 186 responses were reached out of a population of 1400 enrolled students — Page 4, Procedures — «When the participation of the 186 students required for the sample was achieved, access to the survey was deactivated.»
3. валидная шкала зависимости от ИИ: **yes** — Published development/validation study of the AI Dependence Scale (Morales et al., 2024) — Page 4, Instruments — «the Artificial Intelligence Dependence Scale (Morales et al., 2024) was applied»
4. надёжность шкалы ИИ в выборке: **unclear** — Only the alpha from the original authors (.870) is cited; no reliability reported for this sample — Page 4, Instruments — «The authors of the instrument determined that the internal consistency was adequate (α = 0.870).»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy measured with ASSPSE, with published psychometric evaluation (Domínguez, 2016) — Page 4, Instruments — «The psychometric properties of the questionnaire were evaluated in a previous study conducted in Peru by Domínguez (2016)»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported — Page 4, Data analysis — «The statistical analysis was carried out using descriptive and inferential statistical techniques.»

Правки:
- 

Проверено: да

---

## ST100 · Galindo‐Domínguez 2025 · RIED Revista Iberoamericana de Educación a Distancia

Основной отчёт R3466: [текст](../../fulltext/text/R3466.txt) — «The influence of learning motivation and procrastination on ChatGPT dependence» — [DOI](https://doi.org/10.5944/ried.45497)
Расхождения в тексте: The text and Table 1 agree for the eligible pair (PRC–GPT r = .231). The text also says amotivation correlates r = .162 with ChatGPT dependence, matching the table, but motivation is not a dictionary construct. Table 1 prints the same alpha (.858) for procrastination and ChatGPT dependence; this may be a coincidence or a typo. The PROCESS mediation results in Table 2 (e.g., PRC → GPT β = .237) are multivariable and not extracted. Figures 1 and 2 are path diagrams only.
Заметка ИИ: One sample, one eligible effect (procrastination × ChatGPT dependence). The motivation subscales were not extracted because they are outside the construct dictionary.

### ST100-1 · Education students, University of the Basque Country, Spain (n=467)
Отчёты: R3466 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | YE_CHATGPT · total (T2) | **procrastination** · Academic Procrastination Scale – Short Form (Yockey, 2016) | pearson | **.231** | **467** | 1 | Tabla 1 (p. 228) | «PRC 2.57 .947 (.858) .231***» |

- E1: α ИИ .858, α коррелята .858; заметка: Same value in text (r = .231; p < .001). The PRC and GPT alphas are both printed as .858.

**Ключевые поля выборки:**
- **n_analysed: 467** — Metodología, Diseño y participantes (p. 225); Tabla 1 (p. 228) — «En este diseño participaron 467 estudiantes universitarios españoles [467 Spanish university students took part in this design]»
- **population: university_students** — Metodología, Diseño y participantes (p. 225) — «40 estudiantes estaban matriculados en el Grado en Educación Infantil, 379 en el Grado en Educación Primaria y 48 en el Máster [40 in Early Childhood Education, 379 in Primary Education, 48 in the Master's]»
- **sampling: convenience** — Metodología, Diseño y participantes (p. 225) — «seleccionados mediante muestreo no probabilístico por conveniencia, basado en la proximidad al equipo de investigación [selected by non-probability convenience sampling, based on proximity to the research team]»
- **ai_system: general_chatbot** — Instrumentos, Dependencia a ChatGPT (p. 226) — «miden hasta qué punto los individuos sienten la necesidad de usar ChatGPT para tareas académicas [measure how far individuals feel the need to use ChatGPT for academic tasks]»

**Остальные поля:**
- country: ESP — Metodología, Diseño y participantes (p. 225) — «participaron 467 estudiantes universitarios españoles del área de educación de la Universidad del País Vasco [467 Spanish university students in education at t…»
- data_years: NR — NA — «NR»
- design: cross-sectional — Metodología, Diseño y participantes (p. 225) — «El estudio empleó un diseño cuantitativo, transversal y no experimental [The study used a quantitative, cross-sectional, non-experimental design]»
- clinical_group: NA — NA — «NA»
- age_mean: 20.44 — Metodología, Diseño y participantes (p. 225) — «(M = 20,44; DT = 2,83)»
- age_sd: 2.83 — Metodología, Diseño y participantes (p. 225) — «(M = 20,44; DT = 2,83)»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 37.0 (173/467; computed) — Metodología, Diseño y participantes (p. 225) — «292 se identificaron como hombres, 173 como mujeres y 2 como otro género [292 identified as men, 173 as women and 2 as another gender]»
- mode: online — Procedimiento (pp. 226-227) — «Los participantes completaron el cuestionario de Google Forms durante las horas de clase, utilizando ordenadores individuales [Participants completed the Googl…»
- attention_checks: NR — Procedimiento; Análisis de datos (p. 227) — «NR»
- pub_status: journal — p. 217, citation — «RIED-Revista Iberoamericana de Educación a Distancia, 29(1), pp. 217-240. https://doi.org/10.5944/ried.45497»
- language: Spanish (abstract also in English) — p. 217 onwards — «Influencia de la motivación hacia el aprendizaje y la procrastinación en la dependencia a ChatGPT»
- funding_coi: NR (no funding or conflict-of-interest statement in the text provided) — NA — «NR»
- notes: Single convenience sample of students taught by the authors, analysed together. Motivation scores (intrinsic, extrinsic, amotivation; short Academic Motivation Scale) are not in the construct dictionary and were not extracted. Only the procrastination–ChatGPT dependence pair is eligible. The report does not say how the scales were translated or adapted into Spanish. Pages were inferred from the printed page footers (217-240).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability convenience sample of the authors' own students. — Metodología, Diseño y participantes (p. 225) — «seleccionados mediante muestreo no probabilístico por conveniencia [selected by non-probability convenience sampling]»
2. отклик: **unclear** — Neither a response rate nor the number of students invited is reported. — Procedimiento (p. 226) — «se definió la muestra, incluyendo a todos los estudiantes que habían sido instruidos por los investigadores participantes [the sample was defined as all studen…»
3. валидная шкала зависимости от ИИ: **yes** — Uses the published ChatGPT Dependence Scale (Ye et al., 2024), with its reliability as reported there. The reviewer should check that Ye et al. (2024) includes a psychometric validation of the scale. — Instrumentos, Dependencia a ChatGPT (p. 226) — «se empleó la Escala de Dependencia a ChatGPT (Ye et al., 2024). Esta escala consta de una sola dimensión con cinco ítems tipo Likert de 5 puntos»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha in this sample is .858. — Tabla 1 (p. 228) — «GPT 2.37 .996 (.858)»
5. валидные шкалы коррелятов: **yes** — Procrastination, the only extracted correlate, was measured with the published short form of the Academic Procrastination Scale (Yockey, 2016). — Instrumentos, Procrastinación (p. 226) — «se utilizó la Versión Corta de la Escala de Procrastinación Académica (Yockey, 2016)»
6. качество данных: **unclear** — The report mentions no attention checks, careless-responding screening or rule for invalid responses. — Análisis de datos (p. 227) — «Todos los análisis paramétricos se justificaron por la distribución normal de todas las variables medidas»

Правки:
- 

Проверено: да

