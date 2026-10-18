# Проверка выписывания — файл 12 из 13

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

## ST111 · Wu 2025 · Frontiers in psychology

Основной отчёт R4336: [текст](../../fulltext/text/R4336.txt) — «Development and validation of the AI dependence scale for Chinese undergraduates and a preliminary exploration.» — [DOI](https://doi.org/10.3389/fpsyg.2025.1725393)
Приложен R2687: [текст](../../fulltext/text/R2687.txt) — «AI anxiety and AI dependence among undergraduates: a moderated mediation model of AI self-efficacy and AI literacy.»
Связь отчётов: AIDep-22 development (Wu et al.): R4336 Sample 2 (N = 400, 64.8% female, age 18-24, M = 21.17, one university in Southwest China) matches the sample of R2687 (N = 400, 259 female, M = 21.17, Southwest China) in every reported characteristic
⚠ Возможное пересечение (держим раздельно; если видите общие данные — напишите в «Правки»): possible overlap with R2703 (ST072): Both Chinese undergraduates at one normal or comprehensive university in Southwest China with the AIDep-22; R2703 has N = 417 (70.3% female, M = 21.21), R4336 Sample 1 has N = 400 (70.2% female)
Не выписано ИИ: Pilot sample (n = 30 undergraduates): item testing and cognitive interviews only, no correlates. Expert panel (n = 5): content validity only. The combined N = 800 analyses (Tables 9–13) pool Samples 1 and 2, so they are not a separate sample, and they report only demographic comparisons. Sample 1 is extracted but has no eligible correlates.
Расхождения в тексте: 1) In R4336, the text says Sample 2's largest groups were "sophomores (30.0%) and freshmen (26.8%)". Table 3 instead shows juniors at 30.0%, freshmen at 26.8% and sophomores at 17.8%; R2687 Table 1 matches Table 3. 2) The two reports describe Sample 2 differently: - University type: R4336 says a "comprehensive university"; R2687 says a "normal university". - Recruitment: R4336 says links were distributed for two weeks; R2687 says Wenjuanxing was used for 2 months (Sep–Nov 2025), with strata by major and gender. - AIDep-22 scores: R2687 gives M = 3.12, SD = 0.82, alpha .93. R4336 gives M = 3.94, SD = 0.39, alpha .87 for the combined N = 800 sample, and alpha .867 for Sample 1. - CFA fit: R4336 reports χ2/df 1.128, CFI .994, RMSEA .018. R2687 reports χ2/df 2.092, CFI .955, RMSEA .052. The reviewer should confirm that the two reports describe the same sample. 3) No pair appears in both rep…
Заметка ИИ: I extracted the subscales of the Academic Self-Efficacy Scale (SEA, SEC, SSE and CSE) as well as the ASE total. SSE (social) and CSE (computer self-efficacy) may not count as general or academic self-efficacy; the reviewer should decide whether to keep them. The AIDep-22 reliabilities for Sample 2 come from R2687, because R4336 gives no alpha for Sample 2 alone.

### ST111-1 · Sample 1 (EFA), one comprehensive university, Southwest China, undergraduates, N = 400
Отчёты: R4336 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 400** — Participants and data collection; Table 3 — «The first sample (N = 400), designated for the EFA»
- **population: university_students** — Participants and data collection — «The finalized AIDep-22 was administered to two independent samples of undergraduate students»
- **sampling: quota or online panel** — Participants and data collection — «Within each stratum, intact classes were randomly selected and invitation quotas were set proportionally to the overall enrollment of each major category. Data was collected anonymously from an online questionnaire platform.»
- **ai_system: ai_unspecified** — Introduction — «this study defines AI dependence as a persistent pattern of excessive reliance on AI tools for academic purposes»

**Остальные поля:**
- country: CHN — Participants and data collection — «Both samples were recruited from a comprehensive university in Southwest China.»
- data_years: NR — Participants and data collection — «The second sample (N = 400)... was collected one month later from a distinct cohort of students at the same university»
- design: validation study — Exploratory factor analysis — «The EFA was conducted on data from Sample 1 to identify the underlying factor structure of the AIDep-22.»
- clinical_group: NA — NA — «NA»
- age_mean: 21.19 — Participants and data collection — «The participants' ages ranged from 18 to 24 years (M = 21.19, SD = 1.48).»
- age_sd: 1.48 — Participants and data collection — «(M = 21.19, SD = 1.48)»
- age_min: 18 — Participants and data collection — «ages ranged from 18 to 24 years»
- age_max: 24 — Participants and data collection — «ages ranged from 18 to 24 years»
- pct_female: 70.2 — Participants and data collection; Table 3 — «was composed of 281 females (70.2%) and 119 males (29.8%)»
- mode: online — Participants and data collection — «Data was collected anonymously from an online questionnaire platform.»
- attention_checks: NR — Participants and data collection — «Data was collected anonymously from an online questionnaire platform. Links were then distributed by course instructors»
- pub_status: journal — Header — «venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1725393»
- language: English — Full text — «Development and validation of the AI dependence scale for Chinese undergraduates and a preliminary exploration»
- funding_coi: NR — Full text — «No funding or conflict-of-interest statement in the supplied text»
- notes: No eligible correlate was measured in Sample 1 (EFA only), so no effects were extracted. Possible overlap with R2703 (ST072): both samples are Chinese undergraduates at one university in Southwest China and use the AIDep-22. R2703 has N = 417 (70.3% female, M = 21.21); Sample 1 has N = 400 (70.2% female, M = 21.19). AIDep-22 alphas in Sample 1: total .867, ED .849, FD .886, CD .858, LoC .865.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Intact classes were randomly selected within major strata, but participation was voluntary through online links with quotas and no response data are given. Not clearly a probability sample. — Participants and data collection — «Within each stratum, intact classes were randomly selected and invitation quotas were set proportionally... Links were then distributed by course instructors a…»
2. отклик: **unclear** — Response rate not reported for Sample 1. — Participants and data collection — «The first sample (N = 400), designated for the EFA»
3. валидная шкала зависимости от ИИ: **yes** — This report develops and validates the AIDep-22 (EFA, CFA, reliability, validity). — Abstract — «this study developed and validated the AI Dependence Scale (AIDep-22)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha in Sample 1 = .867 total, subscales .849–.886. — Exploratory factor analysis — «Cronbach's alpha for the AIDep-22 was 0.867. The subscales also demonstrated high reliability: emotional dependence (α = 0.849), functional dependence (α = 0.8…»
5. валидные шкалы коррелятов: **unclear** — No correlates were measured or extracted in Sample 1, so this item does not apply. — Exploratory factor analysis — «The EFA was conducted on data from Sample 1»
6. качество данных: **unclear** — R4336 reports no attention checks or screening for invalid responses. — Participants and data collection — «The data collection process was voluntary and anonymous.»

Правки:
- 

Проверено: да

### ST111-2 · Sample 2 (CFA/criterion validity), one university, Southwest China, undergraduates, N = 400
Отчёты: R4336 (main); R2687

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AIDEP22 · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale (Pribeanu et al., 2023) – ASE … | pearson | **−0.46** | **400** | 1 | Table 7 | «ASE total / −0.46* / −0.32* / −0.28* / −0.29* / −0.28*» |
| E2 | AIDEP22 · Emotional dependence (5 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – ASE total | pearson | **−0.32** | **400** | 1 | Table 7 | «ASE total / −0.46* / −0.32* / −0.28* / −0.29* / −0.28*» |
| E3 | AIDEP22 · Functional dependence (6 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – ASE total | pearson | **−0.28** | **400** | 1 | Table 7 | «ASE total / −0.46* / −0.32* / −0.28* / −0.29* / −0.28*» |
| E4 | AIDEP22 · Cognitive dependence (5 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – ASE total | pearson | **−0.29** | **400** | 1 | Table 7 | «ASE total / −0.46* / −0.32* / −0.28* / −0.29* / −0.28*» |
| E5 | AIDEP22 · Loss of control (6 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – ASE total | pearson | **−0.28** | **400** | 1 | Table 7 | «ASE total / −0.46* / −0.32* / −0.28* / −0.29* / −0.28*» |
| E6 | AIDEP22 · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale – SEA (self-efficacy with self… | pearson | **−0.35** | **400** | 1 | Table 7 | «SEA / −0.35* / −0.25* / −0.17* / −0.25* / −0.22*» |
| E7 | AIDEP22 · Emotional dependence (5 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SEA | pearson | **−0.25** | **400** | 1 | Table 7 | «SEA / −0.35* / −0.25* / −0.17* / −0.25* / −0.22*» |
| E8 | AIDEP22 · Functional dependence (6 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SEA | pearson | **−0.17** | **400** | 1 | Table 7 | «SEA / −0.35* / −0.25* / −0.17* / −0.25* / −0.22*» |
| E9 | AIDEP22 · Cognitive dependence (5 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SEA | pearson | **−0.25** | **400** | 1 | Table 7 | «SEA / −0.35* / −0.25* / −0.17* / −0.25* / −0.22*» |
| E10 | AIDEP22 · Loss of control (6 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SEA | pearson | **−0.22** | **400** | 1 | Table 7 | «SEA / −0.35* / −0.25* / −0.17* / −0.25* / −0.22*» |
| E11 | AIDEP22 · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale – SEC (self-efficacy with the … | pearson | **−0.32** | **400** | 1 | Table 7 | «SEC / −0.32* / −0.24* / −0.23* / −0.20* / −0.14*» |
| E12 | AIDEP22 · Emotional dependence (5 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SEC | pearson | **−0.24** | **400** | 1 | Table 7 | «SEC / −0.32* / −0.24* / −0.23* / −0.20* / −0.14*» |
| E13 | AIDEP22 · Functional dependence (6 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SEC | pearson | **−0.23** | **400** | 1 | Table 7 | «SEC / −0.32* / −0.24* / −0.23* / −0.20* / −0.14*» |
| E14 | AIDEP22 · Cognitive dependence (5 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SEC | pearson | **−0.20** | **400** | 1 | Table 7 | «SEC / −0.32* / −0.24* / −0.23* / −0.20* / −0.14*» |
| E15 | AIDEP22 · Loss of control (6 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SEC | pearson | **−0.14** | **400** | 1 | Table 7 | «SEC / −0.32* / −0.24* / −0.23* / −0.20* / −0.14*» |
| E16 | AIDEP22 · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale – SSE (social self-efficacy) | pearson | **−0.19** | **400** | 1 | Table 7 | «SSE / −0.19* / −0.10* / −0.13* / −0.13* / −0.14*» |
| E17 | AIDEP22 · Emotional dependence (5 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SSE | pearson | **−0.10** | **400** | 1 | Table 7 | «SSE / −0.19* / −0.10* / −0.13* / −0.13* / −0.14*» |
| E18 | AIDEP22 · Functional dependence (6 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SSE | pearson | **−0.13** | **400** | 1 | Table 7 | «SSE / −0.19* / −0.10* / −0.13* / −0.13* / −0.14*» |
| E19 | AIDEP22 · Cognitive dependence (5 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – SSE | pearson | **−0.13** | **400** | 1 | Table 7 | «SSE / −0.19* / −0.10* / −0.13* / −0.13* / −0.14*» |
| E20 | AIDEP22 · Loss of control (6 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – SSE | pearson | **−0.14** | **400** | 1 | Table 7 | «SSE / −0.19* / −0.10* / −0.13* / −0.13* / −0.14*» |
| E21 | AIDEP22 · total (T4) | **self_efficacy** · Academic Self-Efficacy Scale – CSE (computer self-efficacy) | pearson | **−0.15** | **400** | 1 | Table 7 | «CSE / −0.15* / −0.12* / −0.09+ / −0.06 / −0.11*» |
| E22 | AIDEP22 · Emotional dependence (5 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – CSE | pearson | **−0.12** | **400** | 1 | Table 7 | «CSE / −0.15* / −0.12* / −0.09+ / −0.06 / −0.11*» |
| E23 | AIDEP22 · Functional dependence (6 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – CSE | pearson | **−0.09** | **400** | 1 | Table 7 | «CSE / −0.15* / −0.12* / −0.09+ / −0.06 / −0.11*» |
| E24 | AIDEP22 · Cognitive dependence (5 items) (T2) | **self_efficacy** · Academic Self-Efficacy Scale – CSE | pearson | **−0.06** | **400** | 1 | Table 7 | «CSE / −0.15* / −0.12* / −0.09+ / −0.06 / −0.11*» |
| E25 | AIDEP22 · Loss of control (6 items) (T1) | **self_efficacy** · Academic Self-Efficacy Scale – CSE | pearson | **−0.11** | **400** | 1 | Table 7 | «CSE / −0.15* / −0.12* / −0.09+ / −0.06 / −0.11*» |
| E26 | AIDEP22 · total (T4) | **ai_anxiety** · Artificial Intelligence Anxiety Scale (AIAS; Wang & Wang, 2… | pearson | **0.528** | **400** | 1 | R2687, Table 2 | «4. AI dependence / 3.12 / 0.82 / 0.93 / 0.528*** / –0.492*** / –0.530***» |

- E1: α ИИ 0.93 (R2687), α коррелята NR; заметка: Correlation type not stated; Pearson assumed. Exposure alpha from R2687.
- E2: α ИИ 0.88 (R2687), α коррелята NR; заметка: Correlation type not stated; Pearson assumed.
- E3: α ИИ 0.87 (R2687), α коррелята NR; заметка: Correlation type not stated; Pearson assumed.
- E4: α ИИ 0.88 (R2687), α коррелята NR; заметка: Correlation type not stated; Pearson assumed.
- E5: α ИИ 0.89 (R2687), α коррелята NR; заметка: Correlation type not stated; Pearson assumed.
- E6: α ИИ 0.93 (R2687), α коррелята NR; заметка: ASE subscale; overlaps with the ASE total.
- E7: α ИИ 0.88 (R2687), α коррелята NR; заметка: ASE subscale.
- E8: α ИИ 0.87 (R2687), α коррелята NR; заметка: ASE subscale.
- E9: α ИИ 0.88 (R2687), α коррелята NR; заметка: ASE subscale.
- E10: α ИИ 0.89 (R2687), α коррелята NR; заметка: ASE subscale.
- E11: α ИИ 0.93 (R2687), α коррелята NR; заметка: ASE subscale.
- E12: α ИИ 0.88 (R2687), α коррелята NR; заметка: ASE subscale.
- E13: α ИИ 0.87 (R2687), α коррелята NR; заметка: ASE subscale.
- E14: α ИИ 0.88 (R2687), α коррелята NR; заметка: ASE subscale.
- E15: α ИИ 0.89 (R2687), α коррелята NR; заметка: ASE subscale.
- E16: α ИИ 0.93 (R2687), α коррелята NR; заметка: Social self-efficacy subscale of the ASE; reviewer to decide whether it is eligible.
- E17: α ИИ 0.88 (R2687), α коррелята NR; заметка: Social self-efficacy subscale of ASE.
- E18: α ИИ 0.87 (R2687), α коррелята NR; заметка: Social self-efficacy subscale of ASE.
- E19: α ИИ 0.88 (R2687), α коррелята NR; заметка: Social self-efficacy subscale of ASE.
- E20: α ИИ 0.89 (R2687), α коррелята NR; заметка: Social self-efficacy subscale of ASE.
- E21: α ИИ 0.93 (R2687), α коррелята NR; заметка: Computer self-efficacy subscale of the ASE (not AI self-efficacy); reviewer to decide whether it is eligible.
- E22: α ИИ 0.88 (R2687), α коррелята NR; заметка: Computer self-efficacy subscale of ASE.
- E23: α ИИ 0.87 (R2687), α коррелята NR; заметка: Computer self-efficacy subscale of ASE; p < .10.
- E24: α ИИ 0.88 (R2687), α коррелята NR; заметка: Computer self-efficacy subscale of ASE; non-significant.
- E25: α ИИ 0.89 (R2687), α коррелята NR; заметка: Computer self-efficacy subscale of ASE.
- E26: α ИИ 0.93, α коррелята 0.94; заметка: Value from the attached report R2687; not reported in R4336.

**Ключевые поля выборки:**
- **n_analysed: 400** — Table 7 — «[table note] N = 400. ASE, Academic Self-Efficacy»
- **population: university_students** — Participants and data collection — «The finalized AIDep-22 was administered to two independent samples of undergraduate students»
- **sampling: quota or online panel** — Participants and data collection; R2687, Participants and sampling — «intact classes were randomly selected and invitation quotas were set proportionally... R2687: 420 online questionnaires were distributed via Wenjuanxing»
- **ai_system: ai_unspecified** — Introduction — «this study defines AI dependence as a persistent pattern of excessive reliance on AI tools for academic purposes»

**Остальные поля:**
- country: CHN — Participants and data collection — «Both samples were recruited from a comprehensive university in Southwest China.»
- data_years: 2025 — R2687, Participants and sampling — «Data collection lasted 2 months between September and November 2025.»
- design: validation study — Confirmatory factor analysis — «A CFA was performed on the Sample 2 dataset to validate the four-factor structure»
- clinical_group: NA — NA — «NA»
- age_mean: 21.17 — Participants and data collection — «ranging from 18 to 24 years (M = 21.17, SD = 1.51)»
- age_sd: 1.51 — Participants and data collection — «(M = 21.17, SD = 1.51)»
- age_min: 18 — Participants and data collection — «ranging from 18 to 24 years»
- age_max: 24 — Participants and data collection — «ranging from 18 to 24 years»
- pct_female: 64.8 — Participants and data collection; Table 3 — «This sample consisted of 259 females (64.8%) and 141 males (35.2%)»
- mode: online — Participants and data collection — «Data was collected anonymously from an online questionnaire platform.»
- attention_checks: yes — R2687, Participants and sampling — «responses were excluded if they... contained more than 20% missing data, had completion times of less than 120 s, or showed obvious invalid response patterns s…»
- pub_status: journal — Header — «venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1725393»
- language: English — Full text — «Development and validation of the AI dependence scale for Chinese undergraduates and a preliminary exploration»
- funding_coi: NR — Full text — «No funding or conflict-of-interest statement in the supplied text of R4336 or R2687»
- notes: Linked to R2687 as the job instructs: the two reports give the same N, sex split, age M/SD and year/major/AI-use distributions. However, the university type, collection period and AIDep-22 mean, alpha and CFA fit differ (see consistency_notes). The AIDep-22 exposure alphas come from R2687, because R4336 gives no alpha for Sample 2 alone (only CR .87–.89 and alphas for the combined N = 800). I extracted the Academic Self-Efficacy subscales (SEA, SEC, SSE, CSE) as well as the ASE total; the reviewer may keep only the total. Not eligible: the AI usage behaviours (Table 7) and AI self-efficacy / …

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Intact classes were randomly selected within major strata, but participation was voluntary through online links with quotas (Wenjuanxing per R2687). Not clearly a probability sample. — Participants and data collection; R2687, Participants and s… — «Within each stratum, intact classes were randomly selected and invitation quotas were set proportionally»
2. отклик: **yes** — R2687 reports 400 valid of 420 distributed questionnaires (95.2%); R4336 reports none. — R2687, Participants and sampling — «Ultimately, 400 valid questionnaires were retained, with an effective response rate of 95.2%.»
3. валидная шкала зависимости от ИИ: **yes** — The AIDep-22 is developed and validated in this report (EFA, CFA, convergent and discriminant validity). — Confirmatory factor analysis — «The hypothesized four-factor model demonstrated an adequate fit to the data»
4. надёжность шкалы ИИ в выборке: **yes** — R2687 reports alpha .93 for the total and .87–.89 for the subscales in this sample; R4336 reports CR .87–.89 for Sample 2. — R2687, Measures – AI dependence; R4336 Table 5 — «The overall internal consistency coefficient was 0.93. Cronbach's α values for the four dimensions were 0.88 (ED), 0.87 (FD), 0.88 (CD), and 0.89 (LC)»
5. валидные шкалы коррелятов: **yes** — The Academic Self-Efficacy Scale (Pribeanu et al., 2023) and the AIAS (Wang & Wang, 2022) are published instruments. — Criterion validity; R2687, Measures – AI Anxiety — «assessed against the validated Academic Self-Efficacy Scale (Pribeanu et al., 2023)»
6. качество данных: **yes** — R2687 states exclusion rules: more than 20% missing data, completion under 120 s, straight-lining or inconsistent answers. — R2687, Participants and sampling — «had completion times of less than 120 s, or showed obvious invalid response patterns such as straight-lining or internally inconsistent answers»

Правки:
- 

Проверено: да

---

## ST112 · Yankouskaya 2025 · ACM Transactions on the Web

Основной отчёт R4363: [текст](../../fulltext/text/R4363.txt) · [PDF](../../fulltext/pdf/R4363.pdf) — «LLM-D12: A Dual-Dimensional Scale of Instrumental and Relational Dependencies on Large Language Models» — [DOI](https://doi.org/10.1145/3765895)
Не выписано ИИ: Pilot sample (N = 27; page 7): used only to check whether items were understood, with no correlates analysed. The EFA and CFA halves (N = 263 each) are random splits of the same sample, not separate samples.
Расхождения в тексте: Zero-order Pearson correlations between the LLM-D12 subscales (Instrumental, Relationship) and Internet Addiction (IAT-7, alpha .826; problematic_internet_use) and ATAI Fear (alpha .715; ai_anxiety) are shown only in Figure 2 (p. 17). No numbers are given in the text, so nothing was extracted. The text describes these correlations only in words: Instrumental Dependency correlated 'strongly positive' with Internet Addiction and 'weak negative' with ATAI Fear; for Relationship Dependency the negative correlation with ATAI Fear was 'small and at borderline of significance (p=.048)'. Steiger tests are reported. The regression betas on p. 18 come from multivariable models and were not extracted. The only other correlation-type statistic is the squared latent correlation between the two subscales (.503), which is not a correlate. Sample size and age: 646 people were recruited; 532 remained af…
Заметка ИИ: I found one eligible sample. Its correlations with eligible constructs (internet addiction, AI fear) appear only in Figure 2, so no effect rows were extracted. The reviewer may want to request the values from the OSF data (osf.io/5fxq7). pub_status is coded 'journal' (ACM TWEB, in press), but the supplied full text is the arXiv preprint version. Sampling is coded 'quota or online panel' because participants came from Prolific; the authors describe it as a convenience sample.

### ST112-1 · UK adult LLM users, Prolific, n=526
Отчёты: R4363 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 526** — Page 16, Table 7 — «Total Sample (n = 526)»
- **population: general_adults** — Page 6, 2.2 Participants — «they must be 18 years or older, currently residing in the UK»
- **sampling: quota or online panel** — Page 8, 2.3 Procedure; Page 24, 4.6 — «The participants were recruited using Prolific online platform (www.prolific.com).»
- **ai_system: general_chatbot** — Page 32, Appendix 1; Page 6 — «Thinking specifically about the large language model (LLM) you use most often (such as ChatGPT, DeepSeek, Gemini, Copilot, etc.)»

**Остальные поля:**
- country: GBR — Page 6, 2.2 Participants — «they must be 18 years or older, currently residing in the UK, and identifying as British in terms of culture and norms»
- data_years: 2025 — Page 8, 2.3 Procedure — «The main study was conducted between the end of March 2025 and mid-April 2025.»
- design: validation study — Page 1, Abstract — «we developed and validated a new 12-item questionnaire to measure LLM dependency, referred to as LLM-D12»
- clinical_group: NA — NA — «NA»
- age_mean: 28.17 — Page 9, 2.4.1 — «532 participants (Mean age = 28.17, SD = 5.91, 50.29% males, 48.57% females»
- age_sd: 5.91 — Page 9, 2.4.1 — «Mean age = 28.17, SD = 5.91»
- age_min: NR (inclusion criterion: 18 years or older) — Page 6, 2.2 Participants — «First, they must be 18 years or older»
- age_max: NR — Page 25, 4.6 — «the majority of our participants were aged 18–40 years, with only a small proportion being older»
- pct_female: 48.57 — Page 9, 2.4.1 — «50.29% males, 48.57% females, 1.14% non-binary and missing the response»
- mode: online — Page 8, 2.3 Procedure — «The survey was developed and distributed using SurveyMonkey (www.surveymonkey.com).»
- attention_checks: yes — Page 9, 2.4.1 — «After initial inspection and removing participants who did not complete or failed attention checks, 532 participants»
- pub_status: journal — Page 1 — «This is a preprint; the paper is currently in press. https://doi.org/10.48550/arXiv.2506.06874»
- language: English — Full text — «LLM-D12: A Dual-Dimensional Scale of Instrumental and Relational Dependencies on Large Language Models»
- funding_coi: Qatar National Research Fund NPRP 14 C-0916-210015; open access fund from Qatar National Library; conflicts of interest not reported — Page 26, Acknowledgments — «This publication was supported by NPRP- 14-Cluster Grant # NPRP 14 C- 0916–210015 from the Qatar National Research Fund (a member of the Qatar Foundation).»
- notes: Age and sex figures refer to the 532 participants left after cleaning; correlations use 526 (2 non-binary and 4 missing gender responses excluded). The correlations with Internet Addiction and ATAI Fear appear only in Figure 2, so no numeric effects were extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Recruited via the Prolific crowdsourcing platform; the authors call it a convenience sample. — Page 8, 2.3; Page 24, 4.6 — «Another limitation of our study is the use of a convenience sample recruited through online platforms.»
2. отклик: **unclear** — No response rate reported. 646 people provided data and 532 remained after removing incomplete responses and attention-check failures. Non-responders were not compared. — Page 6; Page 9 — «In total, data were collected from 646 individuals.»
3. валидная шкала зависимости от ИИ: **yes** — LLM-D12 is developed and validated in this report (EFA, CFA, reliability, discriminant validity). — Pages 13-16 — «The CFI was 0.958 and the TLI was 0.947»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha is .84 for Instrumental and .91 for Relationship Dependency. No alpha is reported for the total score. — Page 16, 3.5.1 — «Cronbach’s alpha for Relationship Dependency was 0.91 and for Instrumental Dependency was 0.84»
5. валидные шкалы коррелятов: **yes** — The eligible correlates (internet addiction, IAT-7; AI fear, ATAI Fear subscale) are published instruments. No numeric coefficients could be extracted. — Pages 7-8 — «Internet Addiction was measured using the Internet Addiction Test (IAT-7)»
6. качество данных: **yes** — Attention checks were used and failed cases were removed. — Page 9, 2.4.1 — «removing participants who did not complete or failed attention checks»

Правки:
- 

Проверено: да

---

## ST113 · Yao 2025 · Frontiers in psychology

Основной отчёт R4365: [текст](../../fulltext/text/R4365.txt) — «Connecting self-esteem to problematic AI chatbot use: the multiple mediating roles of positive and negative psychological states.» — [DOI](https://doi.org/10.3389/fpsyg.2025.1453072)
Расхождения в тексте: Cronbach's alpha disagrees between the text and Table 3. Escapism: 0.817 in the text, 0.831 in Table 3; the table value is used. AI chatbot flow: 0.877 in the text, 0.887 in Table 3; not extracted. The text says alphas range from 0.831 to 0.935, which matches Table 3. Table 5 (HTMT) and Table 6 (PLS-SEM paths) were not extracted, as the rules require. In Table 6, SA → PACU has p = 0.001 at t = 2.321, which is internally inconsistent. Tables 8 and 9 are mislabelled ('Model 3' appears in both).
Заметка ИИ: There is one sample, and only latent (Fornell-Larcker) correlations are available; no observed correlation matrix is reported. The country (CHN) is inferred, not stated.

### ST113-1 · Online AI chatbot users, snowball via social media/IT Q&A communities (China implied), n=563
Отчёты: R4365 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **self_esteem** · Rosenberg Self-esteem Scale (RSES, 8-item Chinese adaptatio… | latent | **−0.453** | **563** | 1 | Table 4 | «PACU / −0.453 / 0.447 / 0.450 / 0.455 / 0.818» |
| E2 | BERGEN_ADAPTED · total (T1) | **social_anxiety** · Social Anxiety Scale for Social Media Users (SAS-SMU), 7 it… | latent | **0.447** | **563** | 1 | Table 4 | «PACU / −0.453 / 0.447 / 0.450 / 0.455 / 0.818» |
| E3 | BERGEN_ADAPTED · total (T1) | **escapism_motive** · Escapism (adapted from Hirschman, 1983), 4 AI-chatbot items | latent | **0.450** | **563** | 1 | Table 4 | «PACU / −0.453 / 0.447 / 0.450 / 0.455 / 0.818» |

- E1: α ИИ 0.877, α коррелята 0.935; заметка: PLS-SEM latent variable correlation from Fornell-Larcker table; no observed Pearson matrix reported.
- E2: α ИИ 0.877, α коррелята 0.913; заметка: Latent variable correlation (Fornell-Larcker table).
- E3: α ИИ 0.877, α коррелята 0.831; заметка: Latent variable correlation. Escapism alpha is 0.831 in Table 3 but 0.817 in the text; the table value is used. Items include 'AI chatbots help me avoid loneliness' and 'get what I want without much effort'.

**Ключевые поля выборки:**
- **n_analysed: 563** — Data collection — «Finally, 563 questionnaires were collected with an effective rate of 87.56%.»
- **population: general_adults** — Table 1; Data collection — «Student | 177 | 31.44% ... Enterprise employee | 226 | 40.14%»
- **sampling: snowball** — Data collection — «We recruited participants based on the virtual snowball sampling method to increase sample size and representativeness»
- **ai_system: general_chatbot** — Questionnaire development — «A screening question was used to confirm that they have used at least one chatbot product.»

**Остальные поля:**
- country: CHN — Methodology, Questionnaire development; Footnote 1; Ethics … — «This study used RSES as adapted into Chinese ... The scale validity was shown in an existing study conducted on Chinese online users»
- data_years: NR — Data collection — «The cross-sectional survey lasted days.»
- design: cross-sectional — Data collection — «The cross-sectional survey lasted days. We collected 643 completed questionnaires in total.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age 18–19 | 47 | 8.35% 20–29 | 268 | 47.60%»
- age_sd: NR — Table 1 — «Age 18–19 | 47 | 8.35%»
- age_min: 18 — Data collection; Table 1 — «teenagers (individuals under the age of 18) were excluded from our sample»
- age_max: NR — Table 1 — «Above 50 | 18 | 3.20%»
- pct_female: 45.65 — Table 1 — «Female | 257 | 45.65%»
- mode: online — Data collection; Footnote 1 — «The questionnaire was managed by a professional online survey platform.1 ... https://www.wjx.cn/»
- attention_checks: yes — Questionnaire development; Data collection — «attention-checking items such as reverse wording and instructed response items were implemented ... Eighty unqualified responses were excluded owing to careles…»
- pub_status: journal — Header — «venue: Frontiers in psychology; DOI: 10.3389/fpsyg.2025.1453072»
- language: English — Full text — «Connecting self-esteem to problematic AI chatbot use: the multiple mediating roles of positive and negative psychological states»
- funding_coi: National Natural Science Foundation of China, Shandong Social Science Foundation, China Postdoctoral Science Foundation; no conflicts declared — Funding Statement; Conflict of interest — «supported ... by the National Natural Science Foundation of China ... The authors declare that the research was conducted in the absence of any commercial or f…»
- notes: Country not stated explicitly; inferred from Chinese-adapted scales, wjx.cn platform and Tsinghua ethics approval. Sample mixes students (31%) and employees (40%); coded general_adults. Participants paid small monetary rewards. AI chatbot flow (ACF) correlate not in construct dictionary, not extracted. PACU = 5-item BSMAS adaptation (item B3 removed).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Virtual snowball sampling via social media and IT Q&A communities on Wenjuanxing. — Data collection — «We recruited participants based on the virtual snowball sampling method»
2. отклик: **unclear** — No response rate among those invited; 87.56% is the proportion of completed questionnaires retained after screening. — Data collection — «We collected 643 completed questionnaires in total. Eighty unqualified responses were excluded ... effective rate of 87.56%.»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from the BSMAS (published), with CFA loadings, AVE and CR reported in this report. — Questionnaire development; Table 3 — «The construct of PACU was adapted from the brief version of the Bergen Social Media Addiction Scale (BSMAS) (Andreassen et al., 2012)»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.877 in this sample. — Table 3 — «Problematic AI chatbot use | PACU1 | 0.756 | 0.670 ... Cronbach’s α: 0.877»
5. валидные шкалы коррелятов: **yes** — Correlates were adapted from published scales (RSES, SAS-SMU, Hirschman escapism). The escapism items were reworded for AI chatbots. — Questionnaire development — «The construct of escapism was adapted from Hirschman (1983) with four items»
6. качество данных: **yes** — Attention-check items were used and careless responses excluded. — Questionnaire development; Data collection — «attention-checking items such as reverse wording and instructed response items were implemented throughout the questionnaire»

Правки:
- 

Проверено: да

---

## ST114 · Huang 2024 · Psychology research and behavior management

Основной отчёт R4615: [текст](../../fulltext/text/R4615.txt) — «AI Technology panic-is AI Dependence Bad for Mental Health? A Cross-Lagged Panel Model and the Mediating Roles of Motivations for AI Use Among Adolescents.» — [DOI](https://doi.org/10.2147/prbm.s440889)
Лонгитюд (для описания): Two waves, spring and autumn semester 2022, analysed with a CLPM controlling for gender, age and subjective SES. Depression and AI dependence (Figure 3A; good model fit): T1 depression -> T2 AI dependence β = 0.104, p < .001; T1 AI dependence -> T2 depression β = 0.018, p = .188. Anxiety and AI dependence (Figure 3B): T1 anxiety -> T2 AI dependence β = 0.078, p < .001; T1 AI dependence -> T2 anxiety β = 0.018, p = .191. In the half-longitudinal mediation models, T1 AI escape motivation -> T2 AI dependence β = 0.115 (depression model) and 0.118 (anxiety model), both p < .001. T1 depression -> T2 escape motivation β = 0.072, and T1 anxiety -> T2 escape motivation β = 0.074. The indirect effect via escape motivation was 0.008 [0.006, 0.015] for depression and 0.009 [0.006, 0.013] for anxiety. The indirect effect via social motivation was 0.005 (depression) and 0.006 (anxiety). Entertainmen…
Расхождения в тексте: 1. Attrition arithmetic: 5057 - 1209 = 3848, not the 3843 reported as analysed. 2. The GAD-7 is described as rated 1-4 and the PHQ-9 as rated 0-3, but the Table 1 means (1.82 and 1.68) look like item-mean scores on similar scales, so the scoring is unclear. 3. The AI dependence CFA at T1 reports TLI (0.987) higher than CFI (0.955), which is unusual and possibly a typo. 4. In the Discussion the escape and social motivation results are matched to H3 and H4 in the reverse order of the hypotheses in the Introduction. 5. The Table 1 column header shows "1" where "10" is expected. 6. Item-level prevalence of AI dependence (Figure 2) and path coefficients in Figures 3-5 are SEM or figure results and were not extracted as correlations.
Заметка ИИ: I extracted one sample with six correlations: the AI Dependence Scale total score with anxiety, depression and AI escape motivation, at T1 and T2. AI social, entertainment and instrumental motivations do not match any key in the construct dictionary, so I left them out. pct_female was calculated from the male count. No funding or COI statement appeared in the supplied text.

### ST114-1 · Chinese adolescent ICT cohort, two waves 2022 (n=3843)
Отчёты: R4615 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4615_1 · total (T1) | **anxiety** · GAD-7 | pearson | **0.18** | **3843** | 1 | Table 1 | «1. T1 Anxiety / 1.82 ± 0.74 / — / 0.79 / 0.18 / 0.26 / 0.25» |
| E2 | ADHOC_R4615_1 · total (T1) | **depression** · PHQ-9 | pearson | **0.21** | **3843** | 1 | Table 1 | «2. T1 Depression / 1.68 ± 0.63 / / — / 0.21 / 0.29 / 0.24» |
| E3 | ADHOC_R4615_1 · total (T1) | **escapism_motive** · AI Use Motivation Scale – escape motivation | pearson | **0.49** | **3843** | 1 | Table 1 | «3. T1 AI dependence / 1.52 ± 0.62 / / / — / 0.49 / 0.41 / 0.19» |
| E4 | ADHOC_R4615_1 · total (T1) | **anxiety** · GAD-7 | pearson | **0.24** | **3843** | 2 | Table 1 | «8. T2 Anxiety / 1.73 ± 0.74 / ... / — / 0.85 / 0.24 / 0.32 / 0.30» |
| E5 | ADHOC_R4615_1 · total (T1) | **depression** · PHQ-9 | pearson | **0.26** | **3843** | 2 | Table 1 | «9. T2 Depression / 1.65 ± 0.66 / ... / — / 0.26 / 0.34 / 0.31» |
| E6 | ADHOC_R4615_1 · total (T1) | **escapism_motive** · AI Use Motivation Scale – escape motivation | pearson | **0.65** | **3843** | 2 | Table 1 | «10. T2 AI dependence / 1.70 ± 0.72 / ... / — / 0.65 / 0.59 / 0.30 / 0.31» |

- E1: α ИИ 0.881, α коррелята 0.909; заметка: Matrix gives two decimals only
- E2: α ИИ 0.881, α коррелята 0.896; заметка: Matrix gives two decimals only
- E3: α ИИ 0.881, α коррелята NR (range .862-.895 all subscales); заметка: Escape motivation to use AI. Only a range of alphas is reported across the four motivation subscales.
- E4: α ИИ 0.953, α коррелята 0.942; заметка: Same-occasion correlation at T2; for the longitudinal narrative
- E5: α ИИ 0.953, α коррелята 0.930; заметка: Same-occasion correlation at T2; for the longitudinal narrative
- E6: α ИИ 0.953, α коррелята NR (range .882-.935 all subscales); заметка: Same-occasion correlation at T2; for the longitudinal narrative

**⚠ Проверка скриптом (обратите внимание):**
- E4, E5, E6: поздняя волна: в основной анализ не идёт, только в описание
- в независимом проходе были ещё числа: 0.10, 0.11, 0.13, 0.16, 0.19, 0.22 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 3843** — Methods, Participants — «the final number of participants in the later analysis was 3843 adolescents»
- **population: adolescents** — Abstract — «3843 adolescents (Male = 1848, Mage = 13.21 ± 2.55)»
- **sampling: NR** — Methods, Participants; Procedure — «Participants were taken from the "Cohort Study on Developmental Characteristics, Influences, and Outcomes of Children and Adolescents' Use of Modern Information Communication Technology (ICT)" project»
- **ai_system: mixed** — Methods, Procedure — «Specific examples include personal assistants (such as Siri, Xiaoai, Xiaodu, Tmall Genie, etc.), intelligent auxiliary equipment, chat robots (such as ChatGPT, ERNIE Bot, etc.), social robots (such as service robot) etc»

**Остальные поля:**
- country: CHN — Methods, Participants — «They came from the northern (2.1%), central (52.3%), and southwestern (45.6%) regions of China.»
- data_years: 2022 — Methods, Participants — «5057 adolescents (male = 2514) in wave 1 (spring semester 2022) and 3843 adolescents (male =1848) in wave 2 (autumn semester 2022)»
- design: panel — Methods, Participants — «A two-wave cohort program with 3843 adolescents»
- clinical_group: NA — NA — «NA»
- age_mean: 13.21 — Methods, Participants — «3843 adolescents (male = 1848, Mage = 13.21 ± 2.55)»
- age_sd: 2.55 — Methods, Participants — «Mage = 13.21 ± 2.55»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 51.9 (computed: (3843-1848)/3843) — Methods, Participants — «3843 adolescents (male = 1848, Mage = 13.21 ± 2.55)»
- mode: paper — Methods, Procedure — «All responses were provided in a paper-pencil format.»
- attention_checks: NR — Methods — «NR»
- pub_status: journal — Header — «Psychology research and behavior management»
- language: English — Full text — «AI Technology panic—is AI Dependence Bad for Mental Health?»
- funding_coi: NR (no funding or COI statement in the supplied text) — NA — «NR»
- notes: School-based cohort; questionnaires distributed in classes by volunteer teachers. Wave-2 same-occasion correlations extracted as wave 2 for the longitudinal narrative. Cross-occasion (T1-T2) correlations not extracted because same-occasion correlations exist. AI social, instrumental and entertainment motivations are not dictionary constructs and were not extracted.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — Participants came from a school-based cohort project, but the way schools or students were selected is not described (it looks like convenience recruitment through volunteer teachers). — Methods, Participants; Procedure — «Volunteer teachers from the school assisted the researchers with data collection.»
2. отклик: **yes** — 76% were retained (3843 of 5057). Dropouts were compared with completers on the T1 variables, and the differences were small. The initial participation rate is not reported. — Methods, Participants — «T test revealed that at T2, the adolescents who responded and those who dropped out differed at T1 for anxiety (t = 2.91, p = 0.004, Cohen's d = 0.095)»
3. валидная шкала зависимости от ИИ: **yes** — The 5 items were adapted from the Smartphone Addiction Scale, and a CFA validation is reported in this paper. — Methods, AI Dependence — «the AI Dependence Scale showed good reliability (αT1 = 0.881, αT2 = 0.953) and construct validity (CFIT1 = 0.955, TLIT1 = 0.987, RMSEAT1 = 0.059»
4. надёжность шкалы ИИ в выборке: **yes** — Alpha was .881 at T1 and .953 at T2. — Methods, AI Dependence — «αT1 = 0.881, αT2 = 0.953»
5. валидные шкалы коррелятов: **yes** — PHQ-9 and GAD-7 are published instruments. Escape motivation comes from a revised version of a published AI Speaker Use Motivation Scale (ref 85), with a CFA reported here. — Methods, Measurement — «The AI Use Motivation Scale was revised from the Artificial Intelligence Speaker Use Motivation Scale.85»
6. качество данных: **unclear** — No attention checks or rules for invalid responses are reported. — Methods — «NR»

Правки:
- 

Проверено: да

---

## ST115 · Liu 2024 · arXiv (Cornell University)

Основной отчёт R4677: [текст](../../fulltext/text/R4677.txt) · [PDF](../../fulltext/pdf/R4677.pdf) — «Chatbot Companionship: A Mixed-Methods Study of Companion Chatbot Usage Patterns and Their Relationship to Loneliness in Active Users» — [DOI](https://doi.org/10.48550/arxiv.2410.21596)
Приложен R3792: [текст](../../fulltext/text/R3792.txt) · [PDF](../../fulltext/pdf/R3792.pdf) — «The Heterogeneous Effects of AI Companionship: An Empirical Model of Chatbot Usage and Loneliness and a Typology of Use…»
Связь отчётов: Companion-chatbot users (N = 404, CloudResearch Connect, adapted GPIUS2): arXiv 2410.21596 v3 (R4677, with the appendix correlation matrix) and the journal version R3792
Расхождения в тексте: (1) GPIUS-2 vs. session length: the main text (R4677 p.7; R3792 p.1590) gives r = 0.303, but the Appendix D list gives r = 0.2549. GPIUS-2 vs. frequency agrees (0.337 vs. 0.3374). (2) Agreeableness vs. loneliness: the text gives r = −0.333, but Appendix D gives +0.3332, an apparent sign error in the appendix. This is not an exposure pair. (3) Gender: the text (both reports) says 36.6% women, but the Figure 11 table gives Woman 39.6% (n = 160/404). The table value is used. (4) Social attraction towards chatbot: Figure 3A gives coef = 0.043, but the Figure 3B table gives 0.080. This is not extracted. (5) R3792 (journal version) has the same methods and results text, has no appendix correlation list (it points to arXiv), and reports no different exposure-correlate values. (6) GPIUS-2 correlations with BFI-10 traits, MSPSS social support and B-RSES self-esteem appear only as colours in the …
Заметка ИИ: One effect extracted: GPIUS-2 (adapted for chatbots) × ULS-8 loneliness, Spearman 0.3649, n = 404. No sample-specific reliability is reported for the exposure.

### ST115-1 · Companion-chatbot users, CloudResearch Connect, mainly USA, n=404
Отчёты: R4677 (main); R3792

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4677_1 · total (T4) | **loneliness** · UCLA Loneliness Scale (ULS-8) | spearman | **0.3649** | **404** | 1 | Page 22, Appendix D (Significant correlations wit… | «Significant correlations with Loneliness (ULS-8): • Problematic Use of Chatbot (GPIUS-2): r = 0.3649, p < 0.001» |

- E1: заметка: Spearman correlation with Benjamini-Hochberg correction (labelled r in the list). The Figure 6 matrix is a colour-only heatmap; this value comes from the Appendix D text list. A ULS-8 α = .84 is reported, but it seems to describe the scale's psychometric properties rather than this sample, so corre…

**Ключевые поля выборки:**
- **n_analysed: 404** — Page 4, Section 3 — «After filtering incomplete responses, our final sample consisted of 404 participants.»
- **population: general_adults** — Page 4, Section 3 — «Participants were 18+ years old, English-fluent, and regular chatbot users (weekly use for at least one month).»
- **sampling: quota or online panel** — Page 4, Section 3 — «We surveyed companion chatbot users recruited from CloudResearch Connect [47]»
- **ai_system: ai_companion** — Page 8, Section 4.3.1 — «Most participants utilize Snapchat MyAI (31.6%), Character.ai (30.4%), or Replika (22.6%) and tend to spend 15 and 30 minutes in each session with a companion chatbot»

**Остальные поля:**
- country: MULTI: USA, GBR, CAN, AUS — Page 29, Figure 11 (Country Of Residence) — «United States 93.6 378 ... United Kingdom 3.2 13 ... Canada 3.0 12 ... Australia 0.3 1»
- data_years: NR — Page 4, Section 3 — «We surveyed companion chatbot users recruited from CloudResearch Connect [47]»
- design: cross-sectional — Page 13, Section 5.4 — «Our cross-sectional design limits causal inferences.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 8, Section 4.3.1 — «Participants ranged in age from 18 to 73, primarily 30-35.»
- age_sd: NR — Page 8, Section 4.3.1 — «Participants ranged in age from 18 to 73, primarily 30-35.»
- age_min: 18 — Page 8, Section 4.3.1 — «Participants ranged in age from 18 to 73, primarily 30-35.»
- age_max: 73 — Page 8, Section 4.3.1 — «Participants ranged in age from 18 to 73, primarily 30-35.»
- pct_female: 39.6 — Page 29, Figure 11 (Gender) — «Woman 39.6 160»
- mode: online — Page 4, Section 3 — «We surveyed companion chatbot users recruited from CloudResearch Connect [47], administering psychological scales»
- attention_checks: NR — Page 4, Section 3 — «After filtering incomplete responses, our final sample consisted of 404 participants.»
- pub_status: preprint — Page 1 — «arXiv:2410.21596v3 [cs.HC] 11 Aug 2025»
- language: English — Page 1 — «CHATBOT COMPANIONSHIP: A MIXED-METHODS STUDY OF COMPANION CHATBOT USAGE PATTERNS»
- funding_coi: Funding NR; conflicts of interest NR; acknowledgment of statistical support only — Page 13, Section 7 — «Statistical support was provided by data science specialist Jinjie Liu, at IQSS, Harvard University.»
- notes: Exposure is an adapted GPIUS2 measuring problematic chatbot use; the reliability given (α = .91) is for the original scale, not this sample. Correlations are Spearman with Benjamini-Hochberg correction. Appendix D lists numeric coefficients only for correlates of usage frequency, session length and loneliness. Correlations of GPIUS-2 with neuroticism, extraversion, agreeableness, conscientiousness, openness, social support (MSPSS) and self-esteem appear only as colours in the Figure 6 / Figure 1 heatmaps, so they are not extracted. Only incomplete responses were filtered; no attention checks …

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Participants were recruited through the CloudResearch Connect online crowdsourcing panel — Page 4, Section 3 — «We surveyed companion chatbot users recruited from CloudResearch Connect [47]»
2. отклик: **unclear** — No response rate is reported; only a target n and the final n after filtering are given — Page 4, Section 3 — «The study was IRB-approved with a target sample of 385 participants (95% confidence level, 5% margin of error).»
3. валидная шкала зависимости от ИИ: **no** — GPIUS2 was adapted to chatbots (and scales may have been shortened) without psychometric evidence for the adapted version; the reliability cited is for the original scale, and the authors note that adaptation may affect… — Page 4, Section 3.2.1; Page 13, Section 5.4 — «Adapted Generalized Problematic Internet Use Scale (GPIUS2) [54], measuring problematic chatbot use (α = .91 for original scale)»
4. надёжность шкалы ИИ в выборке: **unclear** — No alpha or omega is reported for the adapted GPIUS2 in this sample; the .91 refers to the original scale — Page 4, Section 3.2.1 — «measuring problematic chatbot use (α = .91 for original scale)»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, loneliness, was measured with the published ULS-8 — Page 4, Section 3.2.1 — «Our primary dependent variable was measured with the UCLA Loneliness Scale (ULS-8) [48]»
6. качество данных: **unclear** — Only incomplete responses were filtered; no attention checks or careless-responding screening are reported — Page 4, Section 3 — «After filtering incomplete responses, our final sample consisted of 404 participants.»

Правки:
- 

Проверено: да

---

## ST116 · Prayoga 2024 · Journal of Accounting and Investment

Основной отчёт R4748: [текст](../../fulltext/text/R4748.txt) — «AI chatbot distractions and academic triumphs: a mediation approach with self-control and coping skills» — [DOI](https://doi.org/10.18196/jai.v25i2.20755)
Не выписано ИИ: No separate samples. 15 first-semester respondents (of 168) were dropped because they had no GPA; they are not a separate sample.
Расхождения в тексте: Table 4 is titled 'Goodness-of-Fit' (the same title as Table 5) and the text calls it a 'cross-loading analysis', but its layout is a Fornell-Larcker matrix: sqrt(AVE) on the diagonal (0.862, 0.795, 0.948), matching the 'Discriminant Validity' column of Table 3, and latent correlations off the diagonal. The abstract says academic performance is 'moderated by AI Chatbot addiction', while the title and methods describe mediation. In Table 6, H3b is printed as 'CS → CS → AP' (probably CS → CA → AP). The latent correlation of coping skill with CAI is -0.104 (Table 4), while the CS→CA path is +0.043 (Table 6); this is not a contradiction, since the path is adjusted for self-control. The text says higher self-control scores mean better self-control, but the 13 listed items are mostly negatively worded, and no reverse-scoring is described. Self-control loadings and alpha are unusually high (al…
Заметка ИИ: Single sample with one eligible effect: a latent correlation between AI Chatbot Addiction and self-control (r = -0.340, n = 153). No observed Pearson matrix is reported.

### ST116-1 · Accounting students, Faculty of Economics and Business (Universitas Gadjah Mada authors), Indonesia, n=153
Отчёты: R4748 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4748_1 · total (T4) | **self_control** · Self-Control (Tangney et al., 2004), 13 items | latent | **-0.340** | **153** | 1 | p. 683, Table 4 (labelled 'Goodness-of-Fit'; Forn… | «Self-Control 0.067 -0.340 0.410 0.948 [columns: Academic Performance / Chatbot Addiction / Coping Skill / Self-Control]» |

- E1: α ИИ 0.912, α коррелята 0.991; заметка: PLS latent-construct correlation; the diagonal holds sqrt(AVE) (0.862 for CAI, 0.948 for SC). The report says higher scores mean better self-control, although the listed items are mostly negatively worded, so reverse-scoring is assumed. The SEM path SC→CA = -0.358 (Table 6) is not extracted.

**Ключевые поля выборки:**
- **n_analysed: 153** — p. 682, Table 3 notes; p. 681 — «Notes: N = 153 for all the variables»
- **population: university_students** — p. 681, Descriptive Statistics — «the researchers acquired 168 respondents, reflecting the behaviors, characteristics, and academic performance of accounting students.»
- **sampling: convenience** — p. 679, Research Method — «Participants selected for this study were students from the Department of Accounting at the Faculty of Economics and Business who voluntarily followed the prescribed procedures.»
- **ai_system: general_chatbot** — p. 687, Table 7 (AI Chatbot Addiction item 1) — «I intend to continue using AI Chatbots (such as ChatGPT, Google Bard, Bing Chat, and others) to complete academic tasks.»

**Остальные поля:**
- country: IDN — p. 673, Affiliation — «Master of Science in Accounting, Faculty of Economics and Business, Universitas Gadjah Mada, Special Region of Yogyakarta, Indonesia»
- data_years: NR — p. 681, Descriptive Statistics; p. 673 Article history — «This research collected responses over one month and conducted cumulative data checks»
- design: cross-sectional — p. 679, Research Method — «This research employed a quantitative research design with a survey and archival method.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — p. 681, Table 1 — «< 20 years old 12 8 20-25 years old 113 74 26-30 years old 17 11 > 30 years old 11 7»
- age_sd: NR — p. 681, Table 1 — «Age < 20 years old 12 8»
- age_min: NR — p. 681, Table 1 — «< 20 years old 12 8»
- age_max: NR — p. 681, Table 1 — «> 30 years old 11 7»
- pct_female: 56 — p. 681, Table 1 — «Female 85 56»
- mode: online — p. 679, Research Method — «the researchers administered a questionnaire through Google Forms.»
- attention_checks: NR — p. 681, Descriptive Statistics — «The researchers excluded 15 responses, specifically from first-semester students who had not yet obtained GPA results.»
- pub_status: journal — p. 673, header/citation — «Prayoga, H., & Wakhid, Z. N. (2024). AI chatbot distractions and academic triumphs: a mediation approach with self-control and coping skills. Journal of Accoun…»
- language: English — Full text — «Article Type: Research Paper»
- funding_coi: No funding source named; authors declare no conflict of interest. — p. 691, Conflicts of Interest — «The authors declare no conflict of interest. The funders had no role in the design of the study»
- notes: The 15 excluded first-semester students were removed for having no GPA (eligibility), not for data quality. The AI-dependence measure is a 5-item 'AI Chatbot Addiction (CAI)' scale said to be adopted from X. Chen et al. (2020), which is a review of AI in education, not a scale-development paper. Some items cover use or intention (e.g., 'I intend to continue using AI Chatbots'). Analysis was PLS-SEM in Smart-PLS 3.0. No Pearson correlation matrix is given; the only zero-order association is the latent correlation in the Fornell-Larcker-type table (Table 4).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of volunteer accounting students recruited online. — p. 679, Research Method — «students from the Department of Accounting at the Faculty of Economics and Business who voluntarily followed the prescribed procedures»
2. отклик: **unclear** — 168 respondents obtained, but the number invited and the response rate are not reported. — p. 681 — «Absolutely, the researchers acquired 168 respondents»
3. валидная шкала зависимости от ИИ: **yes** — The cited source (X. Chen et al., 2020) is not a scale-development study, but this report gives measurement-model evidence (loadings 0.752-0.916, AVE 0.743, CR 0.935, Fornell-Larcker). This counts as in-report validatio… — p. 680, Research Method; p. 682, Table 3 — «To measure AI Chatbot addiction, the researchers adopted the measurement developed by X. Chen et al. (2020).»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha of 0.912 for AI Chatbot Addiction in this sample. — p. 682, Table 3 — «AI Chatbot Addiction CAI1 0.896 0.743 0.862 0.912 0.935»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate, self-control, is measured with items from Tangney et al. (2004), a published scale. — p. 679, Research Method; p. 686, Table 7 — «The measurement of self-control was dependent on Tangney et al. (2004), where a higher score indicates better self-control.»
6. качество данных: **unclear** — No attention checks or careless-responding screening are reported. The only exclusion was first-semester students without a GPA. — p. 681 — «The researchers excluded 15 responses, specifically from first-semester students who had not yet obtained GPA results.»

Правки:
- 

Проверено: да

---

## ST117 · Uppal 2024 · European Journal of Educational Research

Основной отчёт R4825: [текст](../../fulltext/text/R4825.txt) · [PDF](../../fulltext/pdf/R4825.pdf) — «Students’ Perceptions of ChatGPT in Higher Education: A Study of Academic Enhancement, Procrastination, and Ethical Concerns» — [DOI](https://doi.org/10.12973/eu-jer.14.1.199)
Расхождения в тексте: The means differ slightly between the text and Table 5, apparently from rounding. GPT Dependence is M = 2.863 in the Findings section, M = 2.860 in the Bivariate section and 2.861 in Table 5. Procrastination is 2.953 in the Findings section and Table 5 but 2.950 in the Bivariate section. Plagiarism Risk is 3.821 and 3.820 in the text but 3.822 in Table 5. The correlation of .546 is the same in the text and Table 6. Figure 1 (canonical correlation diagram) does not include dependence, so no figure-only coefficients are relevant.
Заметка ИИ: One effect was extracted: single-item ChatGPT dependence with single-item procrastination attributed to ChatGPT use. Its eligibility under the procrastination key needs the reviewer's judgement.

### ST117-1 · Psychology undergraduates, Kwantlen Polytechnic University, Canada, n=44
Отчёты: R4825 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4825_1 · total (T4) | **procrastination** · Procrastination (single ad hoc Likert item; 'Procrastinatio… | pearson | **.546** | **44** | 1 | Page 7, Table 6 | «1. GPT Dependence 1.000 / 2. Procrastination .546** 1.000» |

- E1: заметка: Both measures are single items. The procrastination item asks about procrastination caused by ChatGPT use, not trait procrastination, so the reviewer should confirm it is eligible. The text gives the same value (r = .546, p < .001).

**Ключевые поля выборки:**
- **n_analysed: 44** — Page 7, Table 5 — «GPT Dependence 2.861 1.167 44»
- **population: university_students** — Page 4, Research Participants and Procedure — «undergraduate students in the Psychology Department at Kwantlen Polytechnic University»
- **sampling: convenience** — Page 4, Research Participants and Procedure — «A total of 44 participants completed the survey, which was accessed through a link posted on the psychology lab website. To encourage participation and increase response rates, students were offered bonus points and course credit»
- **ai_system: general_chatbot** — Page 4, Survey Design — «followed by an initial screening question on ChatGPT use; those who responded affirmatively were directed to the rest of the questionnaire.»

**Остальные поля:**
- country: CAN — Page 4, Research Participants and Procedure — «we administered an online survey to undergraduate students in the Psychology Department at Kwantlen Polytechnic University»
- data_years: NR — Page 9, Ethics Statements; Page 1 — «approved by the Institutional Review Board of Kwantlen Polytechnic University (protocol code 2024-09, approved on April 29, 2024)»
- design: cross-sectional — Page 1, Abstract — «we conducted a correlational study with a sample of 44 students»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NA — «NR»
- age_sd: NR — NA — «NR»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: NR — NA — «NR»
- mode: online — Page 4, Research Participants and Procedure — «The survey, conducted using the Qualtrics platform»
- attention_checks: yes — Page 5, Exclusion Criteria — «Students who responded neutrally to all questions or completed the survey in less than one minute were excluded from the analysis.»
- pub_status: journal — Page 1, header — «European Journal of Educational Research Volume 14, Issue 1, 199 - 211.»
- language: English — Full text — «Students' Perceptions of ChatGPT in Higher Education: A Study of Academic Enhancement, Procrastination, and Ethical Concerns»
- funding_coi: Funded by Kwantlen Polytechnic University Student Research and Innovation Grant (KPU SRIG 2024-10); authors declare no conflicts of interest — Page 10, Conflict of Interest; Funding — «The authors declare no conflicts of interest. ... This research was funded by Kwantlen Polytechnic University through the Student Research and Innovation Grant…»
- notes: The researchers wrote the survey themselves; GPT Dependence and Procrastination are each a single 5-point Likert item, and the item wording is not reported. The procrastination item measures procrastination attributed to ChatGPT use ('Procrastination caused by ChatGPT use'), not trait procrastination. Data years are not stated: IRB approval was on 29 April 2024 and the paper was received on 12 September 2024, so collection was probably in 2024, but this is not reported. The paper does not say whether n=44 is the count before or after the stated exclusions. Plagiarism Risk (r=.108 with depende…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample: a survey link posted on the psychology lab website, with course credit offered. — Page 4, Research Participants and Procedure — «accessed through a link posted on the psychology lab website. To encourage participation and increase response rates, students were offered bonus points and co…»
2. отклик: **unclear** — No response rate is reported and non-responders are not described. — Page 4, Research Participants and Procedure — «A total of 44 participants completed the survey»
3. валидная шкала зависимости от ИИ: **no** — Dependence is a single item written by the researchers, with no psychometric evidence. — Page 4, Survey Design — «The researchers independently designed the survey for this study, without reliance on external resources»
4. надёжность шкалы ИИ в выборке: **unclear** — Single item, so no alpha or omega is reported. — Page 4, Survey Design — «The core of the survey featured ten questions on a 5-point Likert scale»
5. валидные шкалы коррелятов: **no** — Procrastination is a single ad hoc item from the researcher-designed survey. — Page 4, Survey Design — «the behavioural outcomes of the study included dependence on the tool, procrastination, and risk of plagiarism»
6. качество данных: **yes** — A rule for invalid responses is stated: all-neutral responders and completions under one minute were excluded. — Page 5, Exclusion Criteria — «Students who responded neutrally to all questions or completed the survey in less than one minute were excluded from the analysis.»

Правки:
- 

Проверено: да

---

## ST118 · Yuan 2024 · Frontiers in psychology

Основной отчёт R4868: [текст](../../fulltext/text/R4868.txt) — «Impact of media dependence: how emotional interactions between users and chat robots affect human socialization?» — [DOI](https://doi.org/10.3389/fpsyg.2024.1388860)
Расхождения в тексте: The correlations between media dependence and emotional interaction are reported both by subscale (Table 9: degree 0.686, behavior 0.581, effect 0.705, satisfaction 0.530) and as a total (Table 10: 0.674). Emotional interaction is not a dictionary construct, so neither is extracted. The media dependence × interpersonal communication value (0.741) agrees across Tables 9 and 10. Table 11's 'DW inspection' row (0.110/0.588/0.665) appears to repeat adjusted R², while the text gives DW = 1.970/1.908/2.011. The text calls gender significant (β = 0.063, p = 0.000) although its t = 1.283. The behavioral-effect SD is 0.89416 in Table 6 but 0.89316 in the text. The SPSS version is given as 27.0 (reliability) and 26.0 (PROCESS). The direct-effect CI in the text is garbled ('95% CI (0.47, 95% CI)'); Table 12 gives 0.47–0.65.
Заметка ИИ: No effects extracted. The only zero-order correlate of the AI-dependence score is 'Users' real-life interpersonal communication': an ad hoc 5-item composite adapted from the ICDS (Zheng 1999) and the SADS (Watson & Friend 1969), alpha 0.815. It covers interaction with acquaintances, social comfort, hiding feelings, emotional expression and loneliness, with higher scores meaning worse interpersonal communication. I judged it a mixed interpersonal-difficulty measure that fits no dictionary key; social_anxiety or loneliness are possible but uncertain. Reviewer should decide. If coded: r = 0.741,…

### ST118-1 · Replika users recruited via Chinese social media platforms, China, n=428
Отчёты: R4868 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 428** — Table 10 — «Users' media dependence on Replika | Pearson correlation | 1 | 0.741** | 0.674** ... N | 428 | 428 | 428»
- **population: mixed** — Table 1 — «Age | Under 18 years old | 29 | 6.80% | 18–25 years old | 264 | 61.70%»
- **sampling: convenience** — Methods, Data collection and sample description — «The study constructed the formal questionnaire of the survey through the Wenjuanxing platform... distributed and collected through the Douban's "Man–Machine Love" group (9,602 members)... and other platforms.»
- **ai_system: ai_companion** — Methods, Data collection and sample description — «Considering that Replika is an emotional chatbot... this paper takes users who have used Replika as the research object.»

**Остальные поля:**
- country: CHN — Conclusion (limitations) — «this paper only focuses on the interaction between Chinese users and chatbots, and does not conduct relevant investigations on users outside China.»
- data_years: 2023 — Methods, Data collection and sample description — «From October 22 to November 11, 2023, the questionnaires were distributed and collected through the Douban's "Man–Machine Love" group»
- design: cross-sectional — Methods; Conclusion (limitations) — «this paper lacks a periodic surveys of the problem. The main research method in this paper is questionnaire»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «Age | Under 18 years old | 29 | 6.80% ... Over 30 years old | 49 | 11.50%»
- age_sd: NR — Table 1 — «Age reported only in categories»
- age_min: NR — Table 1 — «Under 18 years old | 29 | 6.80%»
- age_max: NR — Table 1 — «Over 30 years old | 49 | 11.50%»
- pct_female: 71.5 — Table 1 — «Gender | Male | 122 | 28.50% | Female | 306 | 71.50%»
- mode: online — Methods, Data collection and sample description — «The study constructed the formal questionnaire of the survey through the Wenjuanxing platform»
- attention_checks: yes — Methods, Data collection and sample description — «Invalid questionnaires mainly included those that took less than 60 s to answer (3 questionnaires)... those whose answers to all questionnaires were the same (…»
- pub_status: journal — Header (Frontiers in psychology, 2024) — «Frontiers in psychology; DOI: 10.3389/fpsyg.2024.1388860»
- language: English — Full text — «Impact of media dependence: how emotional interactions between users and chat robots affect human socialization?»
- funding_coi: NR (no funding or conflict-of-interest statement in the supplied text) — NA — «NR»
- notes: 496 questionnaires were collected and 68 excluded (48 had never used Replika, 14 duplicate IDs, 3 under 60 s, 3 straight-lined). 6.8% of respondents were under 18. The media dependence scale is coded 1 = strongly agree to 5 = strongly disagree, yet the text says higher scores mean more dependence, so the scoring direction is unclear. No eligible correlate was extracted (see note).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online via Wenjuanxing and Replika-related groups and private messages on Chinese social media. — Methods, Data collection and sample description — «The study also used the private messaging functions of Douban, Xiaohongshu, Weibo, Xianyu, and Douyin platforms to conduct a one-to-one questionnaire survey»
2. отклик: **unclear** — No response rate reported. 86.29% is the share of valid questionnaires among those collected, not a response rate. — Methods, Data collection and sample description — «A total of 428 valid questionnaires were obtained, with an effective rate of 86.29%.»
3. валидная шкала зависимости от ИИ: **no** — Ad hoc 6-item scale adapted from the SAS (Kwon) and the CIAS (Chen) by changing the target to Replika. Only alpha and KMO/Bartlett are reported; no factor structure or validity evidence. — Methods, Questionnaire design (3); Table 4 — «this paper adjusted and modified the scale in combination with the specific research objects of this paper, and finally formed the media dependence scale of th…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.923 in this sample. — Table 3 — «Users' media dependence on Replika | 6 | 0.923»
5. валидные шкалы коррелятов: **no** — No correlate extracted. The only candidate correlate (real-life interpersonal communication) is an ad hoc 5-item composite adapted from the ICDS and SADS. — Methods, Questionnaire design (4) — «this paper adjusted and modified the scale in combination with the specific research objects of this paper, and finally formed the user's real interpersonal co…»
6. качество данных: **yes** — Stated rules for invalid responses: completion time under 60 s, straight-lining, duplicate IDs, never used Replika. — Methods, Data collection and sample description — «those whose answers to all questionnaires were the same (3 questionnaires), and those with the same ID were filled in multiple times (14 questionnaires)»

Правки:
- 

Проверено: да

---

## ST119 · Zhang 2024 · International Journal of Educational Technology in Higher Education

Основной отчёт R4876: [текст](../../fulltext/text/R4876.txt) · [PDF](../../fulltext/pdf/R4876.pdf) — «Do you have AI dependency? The roles of academic self-efficacy, academic stress, and performance expectations on problematic AI usage behavior» — [DOI](https://doi.org/10.1186/s41239-024-00467-0)
Расхождения в тексте: The coefficients in the text and in Table 2 agree. The Table 2 note marks ** as p < 0.001, but r = 0.164 (AS-PE) with n = 300 would have p of about .004, so the significance labels look inconsistent. In the Discussion, 84% of students use ChatGPT for academic help, but Table 1 gives 83% (251/300). The abstract and conclusion promise 'top five' negative effects but name only four. The word-cloud results (Fig. 2) are qualitative and contain no coefficients.
Заметка ИИ: Two effects were extracted: AI dependency with academic self-efficacy and with academic stress. Performance expectations was not extracted because it is an AI-specific cognition and out of scope. The PROCESS mediation betas are not zero-order correlations and were not extracted.

### ST119-1 · University students in Seoul, Korea, ChatGPT users, Embrain online survey (n=300)
Отчёты: R4876 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **self_efficacy** · Academic self-efficacy questionnaire (Nielsen et al., 2018;… | pearson | **-0.116** | **300** | 1 | Page 7, Table 2 | «AID / -0.116* / 1» |
| E2 | BERGEN_ADAPTED · total (T1) | **academic_stress** · Academic stress scale (You, 2018), 7 items | pearson | **0.242** | **300** | 1 | Page 7, Table 2 | «AS / -0.217** / 0.242** / 1» |

- E1: α ИИ 0.852, α коррелята 0.885; заметка: Row AID, column ASF. Text also reports r = -0.116.
- E2: α ИИ 0.852, α коррелята 0.702; заметка: Row AS, column AID. Text also reports r = 0.242.

**Ключевые поля выборки:**
- **n_analysed: 300** — Page 5, Participants — «A total of 300 participants were included in this study.»
- **population: university_students** — Page 5, Participants — «University students in Seoul, South Korea, were invited to participate in this study.»
- **sampling: quota or online panel** — Page 5, Participants — «The survey was conducted using a reputable online survey platform offered by Embrain, a prominent South Korean company specializing in online questionnaires.»
- **ai_system: general_chatbot** — Page 5, Participants; Page 1, Abstract — «Participants were selected by asking them if they had any experience using ChatGPT.»

**Остальные поля:**
- country: KOR — Page 5, Participants — «we conducted an online survey in August 2023 in South Korea»
- data_years: 2023 — Page 5, Participants — «we conducted an online survey in August 2023 in South Korea»
- design: cross-sectional — Page 11, Limitations — «First, data collection was cross-sectional; therefore, causal relationships between the variables could not be confirmed.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 5, Table 1 — «Age <= 18 39 13% 19–29 255 85% >= 30 6 2%»
- age_sd: NR — Page 5, Table 1 — «Age <= 18 39 13% 19–29 255 85% >= 30 6 2%»
- age_min: NR — Page 5, Table 1 — «Age <= 18 39 13%»
- age_max: NR — Page 5, Table 1 — «>= 30 6 2%»
- pct_female: 50 — Page 5, Table 1 — «Gender Male 150 50% Female 150 50%»
- mode: online — Page 5, Participants — «we conducted an online survey in August 2023 in South Korea»
- attention_checks: NR — Pages 5-6, Methods — «A total of 300 participants were included in this study.»
- pub_status: journal — Page 1 — «International Journal of Educational Technology in Higher Education (2024) 21:34»
- language: English — Full text — «Do you have AI dependency? The roles of academic self-efficacy, academic stress, and performance expectations on problematic AI usage behavior»
- funding_coi: National Research Foundation of Korea grant (RS-2023-00208278); authors declare no competing interests — Pages 11-12, Funding; Declarations — «This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korean Government (RS-2023-00208278). ... The authors declare th…»
- notes: Only ChatGPT users included. 13% aged <=18 even though all are university students; population coded university_students. Performance expectations (AI-specific) was also correlated with AI dependency (r = 0.575) but is out of scope and not extracted. The AI dependency scale is six Bergen-type items adapted to ChatGPT.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Participants came from a commercial online survey panel (Embrain) and were screened for ChatGPT experience; not a probability sample. — Page 5, Participants — «The survey was conducted using a reputable online survey platform offered by Embrain»
2. отклик: **unclear** — No response rate is reported and non-responders are not compared. — Page 5, Participants — «A total of 300 participants were included in this study.»
3. валидная шкала зависимости от ИИ: **yes** — Six items adapted from the published Bergen Facebook Addiction Scale (Andreassen et al., 2012), which was validated in its original form. The AI-adapted wording was not validated in this report (no CFA), so the reviewer… — Page 6, Measurements — «AI dependency was measured using six items developed by Andreassen et al. (2012) and has been validated in previous studies (Hu et al., 2023; Lee-Won et al., 2…»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.852 in this sample. — Page 6, Measurements — «AI dependency (Cronbach’s α = 0.852)»
5. валидные шкалы коррелятов: **yes** — Academic self-efficacy was measured with a published scale (Nielsen et al., 2018, GASE), and academic stress with seven items from a published study (You, 2018). — Page 6, Measurements — «the academic self-efficacy questionnaire was used (Nielsen et al., 2018) ... Students’ academic stress was measured using seven items (You, 2018)»
6. качество данных: **unclear** — The report mentions no attention checks or screening of invalid responses. — Pages 5-6, Methods — «A total of 300 participants were included in this study.»

Правки:
- 

Проверено: да

---

## ST120 · Zhong 2024 · PloS one

Основной отчёт R4882: [текст](../../fulltext/text/R4882.txt) — «How Do Personal Attributes Shape AI Dependency in Chinese Higher Education Context? Insights from Needs Frustration Perspective.» — [DOI](https://doi.org/10.1371/journal.pone.0313314)
Расхождения в тексте: The text says S1 Table gives the Pearson correlations among all constructs, all significant at p < .01. S1 Table was not in the supplied text, so the zero-order correlations of ChatGPT dependency with neuroticism and impulsivity could not be extracted; a reviewer should get them from S1 Table or from the OSF data (https://osf.io/rys9q/). Table 4 gives HTMT ratios (e.g., ChatGPT Dependency with Neuroticism .281 and with Impulsivity .191), which are not extracted by rule. Table 5 SEM paths are not extracted. Table 3 lists Impulsivity AVE = .908 and CR = .967 from composite indicators. The Discussion says 40.6% use ChatGPT 'very often', but Table 1 labels this category 'Always'.
Заметка ИИ: No effects were extracted. The zero-order correlation matrix is only in S1 Table, which was not provided; check the supplement or the OSF dataset.

### ST120-1 · Chinese university students with ChatGPT experience, Sojump online survey, CHN, n=958
Отчёты: R4882 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | ИИ не нашёл ни одного эффекта для этой выборки | | | | | | | |


**Ключевые поля выборки:**
- **n_analysed: 958** — Materials and methods, Participants and procedure; Table 1 — «Of the 1,000 students invited, 958 provided valid responses.»
- **population: university_students** — Materials and methods, Participants and procedure — «Full-time undergraduate and postgraduate students with experience using ChatGPT for academic work were targeted.»
- **sampling: convenience** — Materials and methods, Participants and procedure — «Participants were recruited online through a reputable survey platform named "Sojump,"»
- **ai_system: general_chatbot** — Materials and methods, Participants and procedure — «Full-time undergraduate and postgraduate students with experience using ChatGPT for academic work were targeted.»

**Остальные поля:**
- country: CHN — Materials and methods, Participants and procedure — «Participants were recruited online through a reputable survey platform named "Sojump," a prominent platform in China specializing in online questionnaires.»
- data_years: 2024 — Materials and methods, Participants and procedure — «The recruitment started on 5th June 2024 and ended on 12th June 2024.»
- design: cross-sectional — Limitations and future directions — «This study's cross-sectional design limits the ability to draw causal inferences»
- clinical_group: NA — NA — «NA»
- age_mean: 21.67 — Materials and methods, Participants and procedure — «Participants ranged from 18 to 28 years old (M = 21.67, SD = 2.46).»
- age_sd: 2.46 — Materials and methods, Participants and procedure — «Participants ranged from 18 to 28 years old (M = 21.67, SD = 2.46).»
- age_min: 18 — Materials and methods, Participants and procedure — «Participants ranged from 18 to 28 years old»
- age_max: 28 — Materials and methods, Participants and procedure — «Participants ranged from 18 to 28 years old»
- pct_female: 48.4 — Table 1 — «Female | 464 | 48.4%»
- mode: online — Materials and methods, Participants and procedure — «Participants were recruited online through a reputable survey platform named "Sojump,"»
- attention_checks: yes — Materials and methods, Participants and procedure — «To ensure data quality, duplicate submissions (identified by IP address) were excluded.»
- pub_status: journal — Header (venue) — «venue: PloS one; DOI: 10.1371/journal.pone.0313314»
- language: English — Full text — «How Do Personal Attributes Shape AI Dependency in Chinese Higher Education Context?»
- funding_coi: Funded by the Key Project of the National Social Science Fund of China (ACA210010); conflicts of interest NR in the supplied text. — Funding Statement — «This work was supported by the Key Project of the National Social Science Fund of China [grant number ACA210010].»
- notes: The only screening was excluding duplicate submissions by IP; there were no attention-check items. The AI-dependence measure is 6 ad hoc items adapted from prior studies [12, 44], omega = .863, with item-level CFA, CR and AVE reported here. The zero-order Pearson correlations are only in S1 Table, which was not supplied, so no effects could be extracted. Eligible correlates measured: neuroticism (NEO-FFI, omega .94) and impulsivity (BIS-15 total, omega .967). Negative academic emotion (AEQ-S composite) and needs frustration fit no dictionary key.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online convenience recruitment through the Sojump (Wenjuanxing) crowdsourcing platform. — Materials and methods, Participants and procedure — «Participants were recruited online through a reputable survey platform named "Sojump,"»
2. отклик: **yes** — 958 of 1,000 invited students gave valid responses (95.8%). — Materials and methods, Participants and procedure — «Of the 1,000 students invited, 958 provided valid responses.»
3. валидная шкала зависимости от ИИ: **yes** — Ad hoc adapted items, but this report gives a validation: item-level CFA fit, loadings > .70, CR = .863, AVE = .512. The reviewer should confirm this counts as a validation. — Measurements; Table 2; Table 3 — «ChatGPT Dependency | .778 | 1.00 | .998 | 1.00 | .00[.00-.03] | .009»
4. надёжность шкалы ИИ в выборке: **yes** — McDonald's omega = 0.863 in this sample. — Measurements — «The reliability index indicated acceptable internal consistency (McDonald's omega = 0.863).»
5. валидные шкалы коррелятов: **yes** — The eligible correlates use published instruments: NEO-FFI neuroticism and BIS-15. No effects could be extracted, though. — Measurements — «Neuroticism was assessed using the 12-item subscale of the NEO Five-Factor Inventory (NEO-FFI) [38]. ... Impulsivity was measured by the Barratt Impulsiveness …»
6. качество данных: **yes** — States a rule for invalid responses: duplicate submissions excluded by IP address. — Materials and methods, Participants and procedure — «To ensure data quality, duplicate submissions (identified by IP address) were excluded.»

Правки:
- 

Проверено: да

