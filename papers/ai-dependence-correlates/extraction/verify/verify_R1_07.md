# Проверка выписывания — файл 7 из 13

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

## ST061 · Siddqiue 2026 · Journal of excellence in social sciences.

Основной отчёт R2325: [текст](../../fulltext/text/R2325.txt) · [PDF](../../fulltext/pdf/R2325.pdf) — «When AI Helps but Humans Feel Less Capable: The Impact of Generative AI Reliance on Professional Self-Efficacy and Meaningful Work» — [DOI](https://doi.org/10.69565/jess.v5i1.395)
Лонгитюд (для описания): This is a three-wave time-lagged design, not a cross-lagged panel. Each construct was measured only once: GenAI reliance and AI literacy at T1, professional self-efficacy at T2 (4 weeks later), and meaningful work at T3 (4 more weeks later). The OLS model (PROCESS Model 7) gives GAR(T1) → PSE(T2) β = −.277 (95% CI [−.377, −.178]), GAR(T1) → MW(T3) β = −.123, PSE(T2) → MW(T3) β = .479, and GAR × AIL → PSE β = .138. Indirect effect −.133 [−.191, −.081]. No cross-lagged or autoregressive paths can be estimated, and the authors say reverse causality cannot be ruled out.
Расхождения в тексте: (1) Indirect-effect CI: Table 5 gives [−.191, −.081], but the Table 6 baseline gives [−.193, −.081]. Index of moderated mediation CI: [.016, .116] in Table 5 vs [.017, .118] in Table 6. The Table 6 note is cut off ("baseline intervals differ from."). (2) The marker-adjusted GAR–PSE r = −.371 (text, p. 8) is larger in magnitude than the unadjusted Table 3 value of −.253. (3) The discussion (p. 10) says "81.4% of respondents who were high level in AI literacy were still harmed", but the results say the effect was significant for 81.4% of all respondents. The discussion also says "meaningful work was the most robust predictor of self-efficacy", which reverses the tested path (PSE → MW). (4) The Figure 2 path diagram is not extracted. (5) The ethics approval statement contains placeholders ("[name of institution]", "[approval reference]"). (6) Data collection years are not reported. Female …
Заметка ИИ: I extracted one sample with one effect (GAR–professional self-efficacy, latent/Fornell-Larcker, lagged T1–T2). Professional (occupational) self-efficacy is mapped to self_efficacy; the reviewer should confirm that occupational self-efficacy fits this key.

### ST061-1 · Knowledge workers, Pakistan, three-wave time-lagged survey (n=350)
Отчёты: R2325 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2325_1 · total (T2) | **self_efficacy** · Short Occupational Self-Efficacy Scale (Rigotti et al., 200… | latent | **−.253** | **350** | lagged: T1-T2 | Page 8, Table 3 (below diagonal) | «PSE / −.253 / .184 / .821 / .558» |

- E1: α ИИ .887, α коррелята .903; заметка: From the Fornell-Larcker discriminant-validity table (below diagonal = correlations; composites from confirmatory composite analysis), so coded latent. These may equal Pearson correlations of the unit-weighted composites, but the report does not say so. GAR measured at T1, PSE at T2; no same-occasi…

**⚠ Проверка скриптом (обратите внимание):**
- E1: корреляция между разными замерами (lagged): идёт в анализ, только если нет корреляции одного замера

**Ключевые поля выборки:**
- **n_analysed: 350** — Page 1, Abstract; Page 13, Conclusion — «The three-wave time-lagged survey of 350 knowledge workers in Pakistan»
- **population: employees** — Page 6, 4.2 — «Purposive sampling targeted full-time employees with at least one year in their occupation who used GenAI for work at least weekly»
- **sampling: convenience** — Page 6, 4.2 — «Purposive sampling targeted full-time employees ... Access was obtained through HR departments of participating organisations and supplemented by professional networks and snowball referrals.»
- **ai_system: general_chatbot** — Page 6, 4.3; Appendix A — «Items referred to work tasks and named common tools (e.g. ChatGPT, Copilot, Gemini, Claude)»

**Остальные поля:**
- country: PAK — Page 6, 4.2 Sample and procedure — «Participants were knowledge workers in Pakistan’s IT/software, banking and finance, telecommunications, consulting, marketing, media and higher-education secto…»
- data_years: NR — NR — «NR»
- design: panel — Page 5-6, 4.1 Research design — «we used a three-wave time-lagged survey. GenAI reliance, AI literacy and controls were measured at Time 1 (T1), professional self-efficacy four weeks later (T2…»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 6, 4.2 — «Respondents (54.6% male) were mostly aged 25–34 (50.0%)»
- age_sd: NR — NR — «NR»
- age_min: NR — Page 6, 4.2 — «were mostly aged 25–34 (50.0%)»
- age_max: NR — NR — «NR»
- pct_female: 45.4 (computed as 100 − 54.6% male; female % not printed) — Page 6, 4.2 — «Respondents (54.6% male)»
- mode: NR — NR — «NR»
- attention_checks: yes — Page 7, 4.4 Analytical strategy — «Data were screened for missing values, outliers and straight-lining; no missing data remained in the matched sample»
- pub_status: journal — Page 1 — «Journal of Excellence in Social Sciences (2026) 5(1): 01–16»
- language: English — Full text — «When AI Helps but Humans Feel Less Capable: The Impact of Generative AI Reliance on Professional Self-Efficacy and Meaningful Work»
- funding_coi: No specific funding; authors declare no conflict of interest — Page 13, Declarations — «This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.»
- notes: Participants: full-time knowledge workers with ≥1 year in their occupation who used GenAI for work at least weekly. Mean work experience 8.94 years (SD 6.09); 78.6% used GenAI daily or several times a week. GAR (7 items) was adapted from Morales-García et al. (2024) and extended. Mode of administration and initial n / attrition are not reported.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Purposive sampling via HR departments, professional networks and snowball referrals. — Page 6, 4.2 — «Purposive sampling targeted full-time employees ... supplemented by professional networks and snowball referrals.»
2. отклик: **unclear** — The report gives no number invited, no response rate and no attrition across the three waves; only the matched n=350. — Page 7, 4.4 — «no missing data remained in the matched sample»
3. валидная шкала зависимости от ИИ: **yes** — Adapted and extended from the published Morales-García et al. (2024) AI dependence scale; confirmatory composite analysis in this report (loadings .698–.814, CR .912, AVE .597). Caveat: the authors say it still needs va… — Page 6, 4.3; Page 7, Table 2; Page 12, 6.3 — «seven items were adapted from Morales-García et al.’s (2024) unidimensional AI dependence scale and extended»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .887 in this sample. — Page 7, Table 2 — «GenAI reliance (GAR) | 3.011 | .912 | .017 | −.788 | .887 | .912 | .597»
5. валидные шкалы коррелятов: **yes** — The extracted correlate (professional self-efficacy) was measured with the published Rigotti et al. (2008) short occupational self-efficacy scale. — Page 6, 4.3 — «Professional self-efficacy used Rigotti et al.’s (2008) six-item short occupational self-efficacy scale»
6. качество данных: **yes** — Responses were screened for straight-lining and outliers. — Page 7, 4.4 — «Data were screened for missing values, outliers and straight-lining»

Правки:
- 

Проверено: да

---

## ST062 · Tan 2026 · Frontiers in Education

Основной отчёт R2459: [текст](../../fulltext/text/R2459.txt) — «Prevalence of AI chatbot usage and factors associated with AI dependency among medical faculty undergraduate students» — [DOI](https://doi.org/10.3389/feduc.2026.1750324)
Расхождения в тексте: (1) Weekly usage–AI dependency: Section 3.5 and the Discussion give r = 0.402, but Table 8 gives 0.346 (Spearman). The Discussion also gives a bivariable R2 of 0.383, while Table 9 gives .127. These values are not extracted. (2) The Discussion (4.3.1) calls the age 'correlation coefficient' −4.1. That number is the unstandardized B from Table 9; Table 8 gives r = −0.143. Table 9 gives a bivariable β of −.153 for age and .356 for weekly usage, which differ from the Table 8 values (−0.143, 0.346). (3) In the t-test text, weekly usage has p = 0.012, but Table 7 gives p < 0.001. (4) Section 4.3.5 says the study 'was unable to establish a direct correlation between academic self-efficacy and AI dependency', yet Table 8 shows a significant r = −0.123 (p = .033). Section 4.3 says age, course of study and self-efficacy were significant in the multiple regression, but Table 9 shows they were not…
Заметка ИИ: This draft covers one sample with two effects. Both correlates are short study-specific scales (2 and 3 items). Rating rob_3 as 'yes' rests only on the EFA reported in this paper, so a reviewer should check it.

### ST062-1 · FPER UKM undergraduate medical, nursing and emergency medicine students, Malaysia, n=300
Отчёты: R2459 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | BERGEN_ADAPTED · total (T1) | **academic_stress** · Academic stress (2 items, Section C; adapted from Bouzar et… | pearson | **0.244** | **300** | 1 | Table 8; Section 3.5 | «Academic stress / 0.244 / <0.001» |
| E2 | BERGEN_ADAPTED · total (T1) | **self_efficacy** · Academic self-efficacy (3 items, Section C; adapted from Bo… | pearson | **−0.123** | **300** | 1 | Table 8; Section 3.5 | «Academic self-efficacy / −0.123 / 0.033» |

- E1: α ИИ 0.864, α коррелята 0.705; заметка: Pearson per text ('Pearson correlation was employed for course of study, academic stress, and academic self-efficacy'). 2-item ad hoc scale.
- E2: α ИИ 0.864, α коррелята 0.66; заметка: Pearson per text. 3-item ad hoc scale with alpha below .70.

**Ключевые поля выборки:**
- **n_analysed: 300** — Table 5 — «AI dependency | 0.864 | 300 | 72.13 (0.74)»
- **population: university_students** — Section 2.2 — «The inclusion criteria were FPER UKM students who are willing to participate»
- **sampling: snowball** — Section 2.2 — «The sampling method utilized in this study is in the form of snowball sampling through dissemination of the survey to representatives of each undergraduate course in FPER UKM.»
- **ai_system: general_chatbot** — Abstract; Section 2.5 — «explore the behavioral and psychological factors associated with AI Chatbot use and dependency ... “For me, life without AI chatbots would be inconvenient”»

**Остальные поля:**
- country: MYS — Section 2.2 — «undergraduate students in the Faculty of Medicine, Universiti Kebangsaan Malaysia (FPER UKM)»
- data_years: NR — Section 2.2 — «Ethical approval has been obtained from UKM Research Ethics Secretariat with the ethics reference number JEP-2025–021.»
- design: cross-sectional — Section 2.2 — «A cross-sectional study design was implemented to investigate the prevalence of AI chatbot usage and the determinants of AI dependency»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 3 — «Agea | 18-21 | 109 | 36% ... 22-25 | 169 | 56% ... 26 and above | 22 | 8%»
- age_sd: NR — Table 3 — «Agea | 18-21 | 109 | 36%»
- age_min: NR (youngest age category 18-21) — Table 3 — «Agea | 18-21 | 109 | 36%»
- age_max: NR (oldest category '26 and above') — Table 3 — «26 and above | 22 | 8%»
- pct_female: 63 — Table 3; Section 3.1 — «The majority of the 300 respondents were female (190, 63%).»
- mode: online — Section 2.2 — «The online questionnaire was disseminated to FPER UKM undergraduate students via social media platforms, including but not limited to WhatsApp.»
- attention_checks: NR — Methods — «NR»
- pub_status: journal — Header — «ORIGINAL RESEARCH articleFront. Educ., 01 July 2026»
- language: English — Full text — «Prevalence of AI chatbot usage and factors associated with AI dependency among medical faculty undergraduate students»
- funding_coi: Funded by UKM Faculty of Medicine Fundamental Grants (FF-2025-103); authors declare no conflict of interest. — Funding; Conflict of interest — «This research received the grant from UKM Faculty of Medicine Fundamental Grants (FF-2025-103). ... conducted in the absence of any commercial or financial rel…»
- notes: AI dependency: 24 study-specific items (Sections D and E) adapted from BFAS and other literature, 5-point Likert, alpha .864. Three AID items loaded <.298 in EFA; unclear whether they were dropped from the total score. Table 5 'S.D.' values (e.g., 0.74 for AI dependency) appear to be standard errors (Table 7 group SDs ~12-13). Correlates: academic stress (2 items) and academic self-efficacy (3 items) adapted from Bouzar et al. 2024 / Zhang S. et al. 2024. Sample: 71% medicine, 18% nursing, 11% emergency medicine; 100% had used AI chatbots.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Snowball sampling via social media dissemination to course representatives. — Section 2.2 — «The sampling method utilized in this study is in the form of snowball sampling»
2. отклик: **unclear** — Population of 1300 and minimum sample of 300 stated, but no response rate and no comparison of non-responders reported. — Section 2.2 — «the population size of undergraduate students in FPER UKM was determined at 1300 and the minimum sample size calculated ... is 300.»
3. валидная шкала зависимости от ИИ: **yes** — Study-specific 24-item composite adapted from BFAS and other scales; the report includes its own EFA (single-factor loadings, KMO .862, discriminant EFA). Weak evidence: 3 items loaded <.298 and AS items did not separat… — Table 6; Section 3.3 — «between 0.388 and 0.659 for 21 out of the 24 AI Dependency (AID) items»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .864 in this sample. — Table 5 — «AI dependency | 0.864 | 300»
5. валидные шкалы коррелятов: **no** — Academic stress (2 items) and academic self-efficacy (3 items) are short item subsets adapted from prior studies, not complete published instruments; self-efficacy alpha .66. — Section 2.4; Table 1 — «This section comprised 5 questions to assess two main factors associated with AI dependency ... namely academic stress and academic self-efficacy.»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rules reported. — Methods — «NR»

Правки:
- 

Проверено: да

---

## ST063 · Totan 2026 · Journal of Psychometric Research

Основной отчёт R2518: [текст](../../fulltext/text/R2518.txt) · [PDF](../../fulltext/pdf/R2518.pdf) — «Yapay Zekâya Bağımlı Davranışlar: Davranışsal Kontrolsüzlük, Duygusal Bağlanma ve Bilişsel Zayıflama» — [DOI](https://doi.org/10.62425/jopres.1880071)
Не выписано ИИ: Pilot sample (n=44 university students, p.5): used only for item analysis of the draft form; no correlations reported. The EFA (n=307) and CFA (n=361) samples are independent groups, but Table 3 does not say which one (or whether both pooled) gave the correlations. Only one sample record was made, so whichever of the two did not provide Table 3 has no extractable effects. The DAI (YZBÖ) was administered, but no correlations with it are reported.
Расхождения в тексте: 1) Table 3 marks Cognitive Impairment x Internet addiction ",55*" (p<.05), but the text says all correlations are significant at p<.001. 2) The abstract says the final scale has 25 items, but the factor structure has 21 items (10+6+5; Table 1; Bartlett df=210 matches 21 items). 3) Item lists disagree: Table 1 puts item 2 under factor 2 (Emotional Attachment), while Table 2 lists item 12 under both Emotional Attachment and Cognitive Impairment and leaves out item 2. 4) Software versions differ: Mplus 8.1 (p.6) vs Mplus 8.3 (p.8). 5) The text says Behavioural Dyscontrol CFA loadings range .25-.43 while calling them high; this looks internally inconsistent. 6) The sample behind the Table 3 correlations is not identified, and alphas are given only as a range (.82-.95) across scale scores, not per subscale or per sample. 7) The text says the Kaiser criterion supports three factors, but the t…
Заметка ИИ: Turkish-language scale-development paper. I extracted 8 correlations from Table 3: the AI-Dependent Behaviours Scale total and its three subscales, each with internet addiction (YIAT-SF) and with the social network subscale of the Technology Addiction Scale. Three things need checking: n (the sample for Table 3 is not stated), whether the social-network subscale fits problematic_social_media_use, and the assumption that the coefficients are Pearson.

### ST063-1 · Aydın Adnan Menderes University students, TUR (criterion-validity analysis; sample unspecified: EFA n=307 or CFA n=361)
Отчёты: R2518 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2518_1 · total (T4) | **problematic_internet_use** · Young Internet Addiction Test-Short Form (YİBT-KF, Turkish) | pearson | **,57** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «İnternet bağımlılığı / ,51** / ,43** / ,55* / ,57**» |
| E2 | ADHOC_R2518_1 · Davranışsal Kontrolsüzlük / Behavioural Dyscontro… (T1) | **problematic_internet_use** · Young Internet Addiction Test-Short Form (YİBT-KF, Turkish) | pearson | **,51** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «İnternet bağımlılığı / ,51** / ,43** / ,55* / ,57**» |
| E3 | ADHOC_R2518_1 · Duygusal Bağlanma / Emotional Attachment (6 items) (T4) | **problematic_internet_use** · Young Internet Addiction Test-Short Form (YİBT-KF, Turkish) | pearson | **,43** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «İnternet bağımlılığı / ,51** / ,43** / ,55* / ,57**» |
| E4 | ADHOC_R2518_1 · Bilişsel Zayıflama / Cognitive Impairment (5 item… (T2) | **problematic_internet_use** · Young Internet Addiction Test-Short Form (YİBT-KF, Turkish) | pearson | **,55** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «İnternet bağımlılığı / ,51** / ,43** / ,55* / ,57**» |
| E5 | ADHOC_R2518_1 · total (T4) | **problematic_social_media_use** · Technology Addiction Scale (TBÖ; Aydın, 2017), Social Netwo… | pearson | **,50** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «Sosyal ağ kullanma / ,42** / ,37** / ,57** / ,50**» |
| E6 | ADHOC_R2518_1 · Davranışsal Kontrolsüzlük / Behavioural Dyscontro… (T1) | **problematic_social_media_use** · Technology Addiction Scale (TBÖ; Aydın, 2017), Social Netwo… | pearson | **,42** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «Sosyal ağ kullanma / ,42** / ,37** / ,57** / ,50**» |
| E7 | ADHOC_R2518_1 · Duygusal Bağlanma / Emotional Attachment (6 items) (T4) | **problematic_social_media_use** · Technology Addiction Scale (TBÖ; Aydın, 2017), Social Netwo… | pearson | **,37** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «Sosyal ağ kullanma / ,42** / ,37** / ,57** / ,50**» |
| E8 | ADHOC_R2518_1 · Bilişsel Zayıflama / Cognitive Impairment (5 item… (T2) | **problematic_social_media_use** · Technology Addiction Scale (TBÖ; Aydın, 2017), Social Netwo… | pearson | **,57** | **NR (307 or 361)** | 1 | p.10, Tablo 3 | «Sosyal ağ kullanma / ,42** / ,37** / ,57** / ,50**» |

- E1: α ИИ NR (range .82-.95 across scores), α коррелята .92; заметка: Correlation type not stated; assumed Pearson. Sample n not stated. The alpha range .82-.95 comes from the abstract.
- E2: α ИИ NR (range .82-.95 across scores), α коррелята .92; заметка: Correlation type not stated; assumed Pearson.
- E3: α ИИ NR (range .82-.95 across scores), α коррелята .92; заметка: Correlation type not stated; assumed Pearson.
- E4: α ИИ NR (range .82-.95 across scores), α коррелята .92; заметка: Marked with a single star (p<.05) in the table, while the text says all are p<.001.
- E5: α ИИ NR (range .82-.95 across scores), α коррелята NR; заметка: Subscale alpha in this sample NR (TBÖ total alpha .94). Mapping this subscale to problematic_social_media_use needs reviewer check.
- E6: α ИИ NR (range .82-.95 across scores), α коррелята NR; заметка: Mapping this subscale to the construct needs reviewer check.
- E7: α ИИ NR (range .82-.95 across scores), α коррелята NR; заметка: Mapping this subscale to the construct needs reviewer check.
- E8: α ИИ NR (range .82-.95 across scores), α коррелята NR; заметка: Mapping this subscale to the construct needs reviewer check.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.38, 0.45, 0.49, 0.56, 0.59 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: NR (Table 3 n not stated; either EFA sample n=307 or CFA sample n=361)** — p.4, Katılımcılar; p.10, Tablo 3 — «açımlayıcı faktör analizi (AFA) aşamasında, toplam 307 katılımcıdan ... doğrulayıcı faktör analizi (DFA) toplam 361 genç yetişkin öğrenci oluşturmuştur»
- **population: university_students** — p.4, Katılımcılar — «Aydın Adnan Menderes Üniversitesi'nde öğrenim görmekte olan ve kolayda örnekleme yöntemiyle seçilen üniversite öğrencileridir»
- **sampling: convenience** — p.4, Katılımcılar — «kolayda örnekleme yöntemiyle seçilen üniversite öğrencileridir [university students selected by convenience sampling]»
- **ai_system: ai_unspecified** — p.4, Araştırmanın Amacı; p.8 example item — «genç yetişkinlerin YZ kullanım aşırılığına ilişkin eğilimlerini ölçmeyi [to measure young adults' tendencies toward excessive AI use]; Örnek madde 2: Yapay zekâ uygulamalarını kullanmak beni güçlü hissettirir [using AI applications makes me feel powerful]»

**Остальные поля:**
- country: TUR — p.4, Katılımcılar — «Ege Bölgesi'nde yer alan Aydın Adnan Menderes Üniversitesi'nde öğrenim görmekte olan [studying at Aydın Adnan Menderes University in the Aegean Region]»
- data_years: 2025 — p.4, Katılımcılar; p.6 — «2025 yılı bahar döneminde [in the spring semester of 2025]; 2024-2025 öğretim yılı bahar döneminde, yaklaşık bir ay süresince»
- design: validation study — p.1, Abstract — «The aim of this study is to develop a valid and reliable measurement tool to assess young adults' dependency tendencies toward the use of artificial intelligen…»
- clinical_group: NA — NA — «NA»
- age_mean: NR — p.4, Katılımcılar — «en yoğun yaş grubu 20 yaş (%23,8) ve 21 yaş (%19,5) aralığındadır [most frequent ages 20 and 21]»
- age_sd: NR — NR — «NR»
- age_min: 17 — p.4, Katılımcılar — «yaşları 17 ile 47 arasında değişmektedir (EFA); Yaş dağılımı 17 ile 47 arasında değişmekte olup (CFA)»
- age_max: 47 — p.4, Katılımcılar — «yaşları 17 ile 47 arasında değişmektedir (EFA); Yaş dağılımı 17 ile 47 arasında değişmekte olup (CFA)»
- pct_female: NR for the correlation sample (EFA sample 67.8; CFA sample 68.4) — p.4, Katılımcılar — «Katılımcıların %67,8'i kadın (n = 208) ... [CFA] Katılımcıların %68,4'ü kadın (n = 247)»
- mode: online — p.6, Veri Toplama Süreci — «çevrim içi ortamda Google Forms aracılığıyla uygulanmıştır [administered online via Google Forms]»
- attention_checks: yes — p.6, Veri Analizi — «Eksik, hatalı ya da tutarsız veriler veri kümesinden çıkarılmış, yalnızca geçerli yanıtlar analiz kapsamına alınmıştır. [Missing, erroneous or inconsistent dat…»
- pub_status: journal — p.1 — «Journal of Psychometric Research ... Araştırma Makalesi Research Article DOI: 10.62425/jopres.1880071»
- language: Turkish (English abstract) — p.1-15 — «Yapay Zekâya Bağımlı Davranışlar: Davranışsal Kontrolsüzlük, Duygusal Bağlanma ve Bilişsel Zayıflama»
- funding_coi: No financial support; no conflicts of interest declared — p.12, declarations — «Conflict of Interest: The authors have no conflicts of interest to declare. Financial Disclosure: The authors declared that this study has received no financia…»
- notes: Scale-development study with two independent samples (EFA n=307; CFA n=361) from the same university, both collected online in spring 2025. Table 3 (criterion validity) does not state which sample (or whether pooled) the correlations come from, so a single sample record is used and n is NR. The DAI (YZBÖ, Savaş 2024 Turkish adaptation) was administered for criterion validity, but no correlations with it are reported. Not extracted from Table 3 because they fit no dictionary key: Technology Addiction Scale total and its instant messaging, online gaming and websites subscales.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample of students at one university, recruited online — p.4, Katılımcılar; p.12 — «kolayda örnekleme yöntemiyle seçilen üniversite öğrencileridir»
2. отклик: **unclear** — No response rate reported — p.6 — «Ölçek formu ... yaklaşık bir ay süresince çevrim içi ortamda Google Forms aracılığıyla uygulanmıştır.»
3. валидная шкала зависимости от ИИ: **yes** — The AI-Dependent Behaviours Scale is developed and validated in this report (EFA, CFA, item analysis) — p.7-9 — «ikinci düzey DFA sonucunda modelin uyum indeksleri χ²(183) = 746.824, p < ,001, CFI = ,90, TLI = ,89, RMSEA = ,09»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha .82-.95 reported for the scale scores in this study (values per score and sample not given separately) — p.1, Abstract — «Internal consistency analyses indicated high reliability, with Cronbach's α coefficients ranging from .82 to .95.»
5. валидные шкалы коррелятов: **yes** — Internet addiction measured with the published YIAT-SF (Turkish adaptation by Kutlu et al., 2016); Technology Addiction Scale published by Aydın (2017, thesis) — p.4-5, Veri Toplama Araçları — «Young (1998) tarafından geliştirilen ölçek Pawlikowski vd. (2013) tarafından kısaltılmıştır. Türkçe uyarlaması Kutlu vd. (2016)...; Teknoloji Bağımlılığı Ölçeğ…»
6. качество данных: **yes** — States a rule that missing, erroneous or inconsistent responses were removed (the criteria are not specified) — p.6, Veri Analizi — «Eksik, hatalı ya da tutarsız veriler veri kümesinden çıkarılmış, yalnızca geçerli yanıtlar analiz kapsamına alınmıştır.»

Правки:
- 

Проверено: да

---

## ST064 · Unión 2026 · REVISTA EUGENIO ESPEJO

Основной отчёт R2562: [текст](../../fulltext/text/R2562.txt) · [PDF](../../fulltext/pdf/R2562.pdf) — «Relación entre dependencia a la inteligencia artificial, rendimiento académico y procrastinación académica en universitarios» — [DOI](https://doi.org/10.37135/ee.04.25.08)
Расхождения в тексте: 1. Sex: the abstract says 53% male, but the Results text and Table 1 give 53.9% male (265) and 46.1% female (227). The table value was used. 2. Age: the participants section gives 18-35 years, while Table 1 has an open top category ('31 o más'). 3. Reliabilities: the reported α/ω for DAI (0.87/0.87), RAU (0.843/0.865) and the EPA subscales (0.821, 0.752; ω 0.829, 0.794) are given in the instrument descriptions. Their wording (e.g., EPA values with 95% CIs) suggests they may come from the original validation studies rather than this sample. 4. Discussion vs Table 4: the Discussion reports DAI–Postergación as r = 0.02, p < 0.647; Table 4 gives 0,021, p = 0,647. These agree. 5. Text vs Table 4: the text says 'Falta de organización' (an academic-performance dimension, not extracted) is negatively related to DAI (r = -0.225), but the Discussion reads this as less organisation going with more…
Заметка ИИ: Single cross-sectional Peruvian sample. Three DAI–procrastination Pearson correlations were extracted: the EPA total and its two subscales. The academic performance (RAU) correlations were not extracted because the construct is not in the dictionary. Language: Spanish; quotes from the methods are given in Spanish with English translations.

### ST064-1 · University students, Puno region, Peru (n=492)
Отчёты: R2562 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **procrastination** · Escala de Procrastinación Académica (EPA), total | pearson | **0,022** | **492** | 1 | Page 8, Tabla 3 | «Dependencia a la IA 1 -0,122** 0,022 / 0,007 0,627» |
| E2 | DAI · total (T4) | **procrastination** · EPA subscale: Autorregulación académica | pearson | **0,018** | **492** | 1 | Page 9, Tabla 4 | «Autorregulación académica 0,018 -0,327** 0,952** 0,692 0,000 0,000» |
| E3 | DAI · total (T4) | **procrastination** · EPA subscale: Postergación de actividades | pearson | **0,021** | **492** | 1 | Page 9, Tabla 4 | «Postergación de actividades 0,021 -0,163** 0,576** 0,647 0,000 0,000» |

- E1: α ИИ 0.87 (source sample unclear), α коррелята NR; заметка: p = 0.627. Same value in the abstract and text.
- E2: **направление: unclear; correlates .952 with EPA total, so it appears scored as lack of self-regulation (more procrastination)**; α ИИ 0.87 (source sample unclear), α коррелята 0.821 (source sample unclear); заметка: p = 0.692. Subscale of the procrastination scale. The scoring direction is not stated, and the authors' interpretation (more self-control linked to more procrastination) suggests the items were reverse-keyed toward procrastination. Reviewer should check the scoring.
- E3: α ИИ 0.87 (source sample unclear), α коррелята 0.752 (source sample unclear); заметка: p = 0.647. The Discussion rounds this to r = 0.02.

**Ключевые поля выборки:**
- **n_analysed: 492** — Page 7, Tabla 2; Page 8, Tabla 3 — «Dependencia de la inteligencia artificial ... Total 492 100»
- **population: university_students** — Page 4, Participantes — «se seleccionó una muestra de 492 estudiantes universitarios de distintas carreras [a sample of 492 university students from different programmes was selected]»
- **sampling: convenience** — Page 4, Participantes — «Se emplearon criterios de muestreo no probabilístico por conveniencia intencional [Non-probabilistic purposive convenience sampling criteria were used]»
- **ai_system: ai_unspecified** — Page 5, Resultados; Page 4, Instrumentos — «tipos de IAs que más utilizan como apoyo para su jornada académica más relevantes fue: el ChatGPT con un 63,41 %, Canva (51,83 %), Meta.IA (40,65 %), Gemini (26.42%) y Mendeley (24,39 %) [types of AI used most for academic work: ChatGPT, Canva, Meta AI, Gemin…»

**Остальные поля:**
- country: PER — Page 4, Participantes — «Este estudio se realizó en la región Puno, Perú [This study was conducted in the Puno region, Peru]»
- data_years: 2024 — Page 4, Participantes — «matriculados en el segundo periodo académico del 2024 [enrolled in the second academic period of 2024]»
- design: cross-sectional — Page 3, Diseño y contexto — «diseño no experimental, de corte transeccional o transversal y de tipo correlacional [non-experimental, cross-sectional, correlational design]»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: 18 — Page 4, Participantes — «con edades comprendidas entre 18 y 35 años [aged between 18 and 35 years]»
- age_max: 35 — Page 4, Participantes — «con edades comprendidas entre 18 y 35 años [aged between 18 and 35 years]»
- pct_female: 46.1 — Page 6, Tabla 1 — «Género Masculino 265 53,9 Femenino 227 46,1»
- mode: NR — Page 5, Análisis de datos — «La recolección de datos se realizó mediante la aplicación de los instrumentos [Data were collected by administering the instruments]»
- attention_checks: NR — NR — «NR»
- pub_status: journal — Page 1 — «REE 20(1) Riobamba ene. - abr. 2026 ... ISSN-digital 2661-6742»
- language: Spanish — Page 1 — «Relación entre dependencia a la inteligencia artificial, rendimiento académico y procrastinación académica en universitarios»
- funding_coi: Self-funded by the authors; authors declare no competing interests. — Page 12 — «Financiamiento: Investigación financiada por los autores. ... Conflictos de intereses: Los autores no tienen intereses en competencia.»
- notes: DAI measures dependence on AI in general (not a specific system); participants reported using a mix of general chatbots (ChatGPT, Meta AI, Gemini) and task tools (Canva, Mendeley), so ai_system was coded ai_unspecified; the reviewer could code it as mixed instead. Mean age not reported; age groups were 18-25 (92.1%), 26-30 (6.9%) and 31+ (1.0%). The sample comes from several Puno universities (UNAP, UNAJ, UPEU, others), recruited together and analysed as one sample. Academic performance (RAU) and its dimensions, including 'Falta de organización', are not in the construct dictionary and were n…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probabilistic convenience sampling. — Page 4, Participantes — «Se emplearon criterios de muestreo no probabilístico por conveniencia intencional»
2. отклик: **unclear** — No response rate and no comparison of non-responders reported. — Page 4, Participantes — «seleccionando participantes con disponibilidad para formar parte de la muestra»
3. валидная шкала зависимости от ИИ: **yes** — DAI comes from a published development and validation study (Morales-García et al., 2024, ref. 24). — Page 4, Instrumentos; Page 15, ref. 24 — «Escala de Dependencia hacia la Inteligencia Artificial (DAI), desarrollada en Perú por Morales-García et al.(24)»
4. надёжность шкалы ИИ в выборке: **unclear** — α=0.87 and ω=0.87 are reported in the instrument description. The text does not say whether these come from this sample or from the original validation. — Page 4, Instrumentos — «Los valores de alfa de Cronbach y el coeficiente omega de McDonald muestran una adecuada consistencia interna (α= 0,87 y ω = 0,87).»
5. валидные шкалы коррелятов: **yes** — Academic procrastination was measured with the EPA (Busko), which has a published validation for Peru (Domínguez et al.). — Page 4, Instrumentos — «Escala de Procrastinación Académica (EPA), creada por Busko(27) y validada para Perú por Domínguez et al.(28)»
6. качество данных: **unclear** — No attention checks, careless-responding screening or invalid-response rule reported. — Page 5, Análisis de datos — «se estructuraron y procesaron utilizando Statistical Package for the Social Sciences (SPSS) versión 27 y Jamovi»

Правки:
- 

Проверено: да

---

## ST065 · Uğuz 2026 · BMC psychology

Основной отчёт R2571: [текст](../../fulltext/text/R2571.txt) — «Loneliness and AI chatbot dependence in young adults: the mediating role of perceived social support.» — [DOI](https://doi.org/10.1186/s40359-026-04916-5)
Расхождения в тексте: (1) Figure 2 shows the correlations among age, daily internet use, loneliness, AI chatbot dependence and perceived social support. The extracted coefficients come from the text, not the figure. (2) The text says data were collected 'over a two-month period', but the Data collection section says 'between September and December 2025'. Ethics approval is dated October 16, 2025, which is after the stated September start. (3) Table 2 gives loneliness kurtosis as -2.58, yet the text says all skewness and kurtosis values fell within ±2.0. (4) The Data analysis section says CMB was assessed with Harman's test. The Results section also reports Kock's full collinearity VIF test and cites refs [41] and [42], which are the same numbers used for the social support instrument papers. (5) The social support measure is called the 'Perceived Social Support Scale' in the abstract and the 'Perceived Socia…
Заметка ИИ: Population is coded general_adults because the sample is young adults aged 18-30 recruited through social media and university communities, not students only. Each coefficient comes from the Results text, which states the r value and its 95% CI.

### ST065-1 · Young adults aged 18-30 in Türkiye, online convenience sample, n=610
Отчёты: R2571 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | AICD · total (T4) | **loneliness** · UCLA Loneliness Scale–6 (Turkish adaptation, Sarıçam) | pearson | **0.71** | **610** | 1 | Results, Correlation check (also Figure 2) | «a strong positive correlation was observed between loneliness and AI chatbot dependence (r = 0.71, 95% CI [0.66, 0.74], p < 0.001)» |
| E2 | AICD · total (T4) | **social_support** · Perceived Social Support Questionnaire (Petersen et al.; Tu… | pearson | **-0.61** | **610** | 1 | Results, Correlation check (also Figure 2) | «Loneliness and AI chatbot dependence were moderately to strongly negatively correlated with perceived social support (r = − 0.55, 95% CI [− 0.60, − 0.49] and r = − 0.61, 95% CI [− 0.66, − 0.56], resp…» |

- E1: α ИИ 0.98, α коррелята 0.93; заметка: Value taken from the text; the report gives 95% CI [0.66, 0.74]. Figure 2 shows the correlation matrix, but its values are not reproduced in the text extraction.
- E2: α ИИ 0.98, α коррелята 0.91; заметка: Value taken from the text; the report gives 95% CI [-0.66, -0.56].

**Ключевые поля выборки:**
- **n_analysed: 610** — Method, Population and sample of the study — «The final analytical sample comprised 610 participants who met the inclusion criteria»
- **population: general_adults** — Results, Participants' characteristics — «most held an undergraduate degree (41.0%) or an associate degree (24.6%)»
- **sampling: convenience** — Method, Population and sample of the study — «Participants were recruited via a non-probability convenience sampling approach, based on voluntary online participation.»
- **ai_system: mixed** — Method, inclusion criteria — «Having used AI chatbots (e.g., ChatGPT, Replika, Gemini) at least once per week during the previous three months»

**Остальные поля:**
- country: TUR — Method, Population and sample of the study — «The target population comprised young adults residing in Türkiye.»
- data_years: 2025 — Method, Data collection — «Data were collected online between September and December 2025.»
- design: cross-sectional — Method, Research model — «Data were collected at a single time point, resulting in a cross-sectional research design.»
- clinical_group: NA — NA — «NA»
- age_mean: 23.84 — Results, Participants' characteristics — «The mean age of the participants was 23.84 ± 3.67 years»
- age_sd: 3.67 — Results, Participants' characteristics — «The mean age of the participants was 23.84 ± 3.67 years»
- age_min: 18 — Method, inclusion criteria — «Aged between 18 and 30 years»
- age_max: 30 — Method, inclusion criteria — «Aged between 18 and 30 years»
- pct_female: 54.6 — Results, Participants' characteristics — «54.6% of the participants were female and 45.4% were male»
- mode: online — Method, Data collection — «Interested individuals were invited to access the survey via a Google Forms link or by scanning a QR code»
- attention_checks: yes — Method, Population and sample; Data collection — «45 cases were excluded due to excessive missing responses (i.e., more than 50% incomplete)»
- pub_status: journal — Header — «BMC psychology; DOI: 10.1186/s40359-026-04916-5»
- language: English — Full text — «Loneliness and AI chatbot dependence in young adults: the mediating role of perceived social support»
- funding_coi: No specific funding; authors declare no competing interests — Funding; Competing interests — «This research did not receive any specific grant from funding agencies... The authors declare no competing interests.»
- notes: Usage purposes: 39.2% academic/educational, 23.8% emotional support. ai_system is coded mixed because the inclusion examples name ChatGPT, Gemini and Replika. attention_checks = yes rests only on the >50% missing-data exclusion rule and the duplicate-participation check; no attention-check items were used.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability convenience sample recruited online via social media and university student communities. — Method, Population and sample; Data collection — «Participants were recruited via a non-probability convenience sampling approach, based on voluntary online participation.»
2. отклик: **unclear** — No response rate; only number of people who completed the survey (655) is given, with no denominator of people invited. — Method, Population and sample of the study — «A total of 655 respondents initially completed the survey.»
3. валидная шкала зависимости от ИИ: **yes** — AI Chatbot Dependence Scale by Zhang et al., with a published Turkish adaptation (Yıldız Durak & Balıkçı). — Method, AI chatbot dependence scale — «The scale developed by Zhang et al. [39] and adapted into Turkish by Yıldız Durak and Balıkçı [40]»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = 0.98 in this sample. — Method, AI chatbot dependence scale — «In the present study, Cronbach's alpha was 0.98, indicating excellent internal consistency.»
5. валидные шкалы коррелятов: **yes** — Loneliness (UCLA-6, Turkish adaptation by Sarıçam) and perceived social support (Petersen et al., Turkish adaptation by Türk et al.) are both published instruments. — Method, Instruments — «data were collected using the UCLA Loneliness Scale–6, the AI Chatbot Dependence Scale, and the Perceived Social Support Questionnaire.»
6. качество данных: **yes** — Stated rule excluding cases with >50% missing responses, plus a check against duplicate participation; no attention-check items or careless-responding screening. Reviewer should check whether this counts. — Method, Population and sample; Data collection — «45 cases were excluded due to excessive missing responses (i.e., more than 50% incomplete)... To prevent duplicate participation, participants were asked to pr…»

Правки:
- 

Проверено: да

---

## ST066 · Vibanco 2026 · Ibero Ciencias - Revista Científica y Académica

Основной отчёт R2603: [текст](../../fulltext/text/R2603.txt) · [PDF](../../fulltext/pdf/R2603.pdf) — «Efectos de tres Modalidades de Tutoría con Inteligencia Artificial Generativa en el Desarrollo Cognitivo y Emocional de Adolescentes Mexicanos: Un Estudio Cuan…» — [DOI](https://doi.org/10.63371/ic.v5.n3.a1515)
Лонгитюд (для описания): Pre-post intervention (week 1 and week 14) with no control group. No cross-lagged paths are reported. Perceived AI dependence went up from pre to post (M 2.10 → 2.85; t = -10.35, df = 299, p < .001). Academic anxiety went down (3.89 → 2.31; t = 25.62, p < .001). The single correlation between the two (r = .412) has no stated measurement occasion.
Расхождения в тексте: The r = .412 for AI dependence and academic anxiety is the same in the abstract and the results. The conclusions say all three programmes produced significant 'mejoras' [improvements] in all six variables, but AI dependence increased, which the authors themselves treat as a risk. Subgroup means agree with the pooled post means. Integrity concerns for the reviewer: the in-text citation numbers [1]-[8] do not match the alphabetical reference list. One reference is an unfilled placeholder ('Raine v. OpenAI, No. [Incluir el número de caso si lo tienes]'). Some references look implausible (e.g., Klarin et al. 2024, Article 1345678). No correlation table is given; only coefficients in the text. No figures with coefficients.
Заметка ИИ: One sample, one effect extracted: AI dependence with academic anxiety, coded academic_stress. Not extracted because they fall outside the dictionary: cognitive planning, study habits, academic motivation, and emotional self-regulation (a possible self_control match, flagged for the reviewer). All measures are unnamed ad hoc Likert scales with no reliability reported.

### ST066-1 · Two technical schools (CBTIS 146 Tijuana + Secundaria Técnica #59 Tlajomulco), Mexico, adolescents in AI-tutoring intervention, n=300
Отчёты: R2603 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2603_1 · total (T4) | **academic_stress** · Ansiedad académica (study-specific Likert scale 1-5) [acade… | pearson | **.412** | **300** | NR | Page 6, Correlaciones (also abstract p. 2-3) | «La dependencia de IA percibida correlacionó positivamente con la ansiedad académica (r = .412, p < .01) [Perceived AI dependence correlated positively with academic anxiety]» |

- E1: заметка: The report does not say whether this uses pre, post or change scores. n for the correlation is not stated; assumed N=300 (total sample). Both measures are ad hoc scales.

**⚠ Проверка скриптом (обратите внимание):**
- E1: поздняя волна: в основной анализ не идёт, только в описание

**Ключевые поля выборки:**
- **n_analysed: 300** — Page 5, Cambios pre-post — «prueba t para muestras emparejadas, N = 300 [paired t-test, N = 300]»
- **population: adolescents** — Page 4, Diseño y participantes — «Participaron 300 adolescentes ... (nivel medio superior) ... (educación básica) [300 adolescents participated ... (upper secondary) ... (basic education)]»
- **sampling: NR** — Page 4, Diseño y participantes — «Participaron 300 adolescentes (52.0% mujeres, 48.0% hombres), 150 del CBTIS 146 de Tijuana... y 150 de la Secundaria Técnica #59 [300 adolescents participated]»
- **ai_system: general_chatbot** — Page 4, Diseño y participantes — «Estudio 1 (tutoría emocional con ChatGPT/Gemini), Estudio 2 (metacognición guiada con Copilot/Deepseek) y Estudio 3 (retroalimentación personalizada con Gemini/Copilot)»

**Остальные поля:**
- country: MEX — Page 4, Diseño y participantes — «150 del CBTIS 146 de Tijuana, Baja California (nivel medio superior), y 150 de la Secundaria Técnica #59 de Tlajomulco, Jalisco [150 from CBTIS 146 Tijuana and…»
- data_years: 2026 — Page 4, Procedimiento e intervención — «El trabajo de campo se desarrolló entre el 23 de febrero y el 14 de junio de 2026 en las dos sedes. [Fieldwork took place between 23 February and 14 June 2026 …»
- design: other — Page 4, Diseño y participantes — «Se empleó un diseño cuantitativo descriptivo de mediciones repetidas (pre-post), como componente complementario de un estudio mixto más amplio [A descriptive q…»
- clinical_group: NA — NA — «NA»
- age_mean: NR — NR — «NR»
- age_sd: NR — NR — «NR»
- age_min: NR — NR — «NR»
- age_max: NR — NR — «NR»
- pct_female: 52.0 — Page 4, Diseño y participantes — «Participaron 300 adolescentes (52.0% mujeres, 48.0% hombres) [52.0% female, 48.0% male]»
- mode: NR — Page 4, Instrumentos — «Se aplicaron escalas tipo Likert (1 a 5) para las seis variables de interés, administradas en la semana 1 (línea base) y en la semana 14 [Likert scales adminis…»
- attention_checks: NR — NR — «NR»
- pub_status: journal — Page 1-2; header — «Ibero Ciencias - Revista Científica y Académica; DOI: https://doi.org/10.63371/ic.v5.n3.a1515»
- language: Spanish (English abstract) — Page 2-3 — «RESUMEN Los tutores de inteligencia artificial (IA) generativa están cada vez más presentes...»
- funding_coi: NR (no funding or conflict-of-interest statement in the text) — NR — «NR»
- notes: Single pooled sample: the two schools were compared only on means, and the correlations are reported for the pooled group. Correlations come from a pre-post intervention study (14 weeks, three AI-tutoring programmes, no control group), and the report does not say whether they use pre, post or change scores. Institution means for AI dependence (2.98/2.73) average to the post mean (2.85). Emotional self-regulation (r = -.124), cognitive planning (r = -.185) and academic motivation (r = -.085) were also correlated with AI dependence but not extracted. Emotional self-regulation could arguably map…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **unclear** — The report does not say how the two schools or the students were selected. — Page 4, Diseño y participantes — «Participaron 300 adolescentes ... 150 del CBTIS 146 de Tijuana ... y 150 de la Secundaria Técnica #59 de Tlajomulco»
2. отклик: **unclear** — No response or attrition rate reported. — NR — «NR»
3. валидная шкала зависимости от ИИ: **no** — AI dependence measured with an unnamed study-specific Likert scale, with no psychometric evidence. — Page 4, Instrumentos — «Se aplicaron escalas tipo Likert (1 a 5) para las seis variables de interés [Likert scales (1 to 5) were applied for the six variables]»
4. надёжность шкалы ИИ в выборке: **unclear** — No reliability coefficient reported. — Page 4, Instrumentos — «Se aplicaron escalas tipo Likert (1 a 5) para las seis variables de interés»
5. валидные шкалы коррелятов: **no** — Academic anxiety measured with an unnamed ad hoc Likert scale. — Page 4, Instrumentos — «Se aplicaron escalas tipo Likert (1 a 5) para las seis variables de interés»
6. качество данных: **unclear** — No attention checks or invalid-response screening reported. — NR — «NR»

Правки:
- 

Проверено: да

---

## ST067 · Viet 2026 · Data in brief

Основной отчёт R2604: [текст](../../fulltext/text/R2604.txt) — «Survey on academic self-efficacy, academic stress, critical thinking, performance expectations, and students' AI dependency.» — [DOI](https://doi.org/10.1016/j.dib.2026.112952)
Расхождения в тексте: 1. The text says the correlations range from 0.356 to 0.720, which matches Table 3. 2. The Methods text says the item details are in Table 1, but they are in Table 2. Table 1 is the respondent profile. 3. In the inline text version of Table 1, the year 4 and year 5 counts run into neighbouring cells ('440(2.5%)', '527(1.7%)'). The structured table gives 40 (2.5%) and 27 (1.7%). 4. Sampling is described both as convenience and as 'probabilities based on the balanced male-female ratio'. It is coded as convenience. 5. The reported '100%' response rate cannot be interpreted because no denominator is given.
Заметка ИИ: There are two latent effects (AID with academic self-efficacy and with academic stress). No observed Pearson matrix is reported.

### ST067-1 · Vietnamese university students, online survey (n = 1580)
Отчёты: R2604 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ACOSTA5 · total (T4) | **self_efficacy** · Academic self-efficacy (6 items adapted from Zhang et al. [… | latent | **0.390** | **1580** | 1 | Table 3 (Fornell & Larcker) | «AID / 0.867 ... AS / 0.390 / 0.819» |
| E2 | ACOSTA5 · total (T4) | **academic_stress** · Academic stress (4 items adapted from Zhang et al. [4]) | latent | **0.499** | **1580** | 1 | Table 3 (Fornell & Larcker) | «AST / 0.499 / 0.437 / 0.849» |

- E1: α ИИ 0.918, α коррелята 0.902; заметка: Correlation between PLS latent variable scores (Fornell-Larcker table). HTMT 0.428 not extracted.
- E2: α ИИ 0.918, α коррелята 0.871; заметка: Correlation between PLS latent variable scores (Fornell-Larcker table). HTMT 0.553 not extracted. One stress item is about job worries after graduation.

**Ключевые поля выборки:**
- **n_analysed: 1580** — Data Description; Table 1 — «collected 1580 responses for analysis»
- **population: university_students** — Abstract — «Data were collected from 1580 university students in Vietnam.»
- **sampling: convenience** — Data Description — «A convenience sampling method and probabilities based on the balanced male-female ratio were used in this study.»
- **ai_system: ai_unspecified** — Table 2; Table 1 — «AID3 | Are you overly reliant on AI to complete your academic assignments? ... PE3 | AI tools increase your learning productivity.»

**Остальные поля:**
- country: VNM — Abstract — «Data were collected from 1580 university students in Vietnam.»
- data_years: 2025-2026 — Data Description — «The survey, conducted from December 2025 to February 2026 via an online Google Form, collected 1580 responses for analysis»
- design: cross-sectional — Data Description — «the questionnaire was distributed online to students studying at universities in Vietnam.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Table 1 — «NR»
- age_sd: NR — Table 1 — «NR»
- age_min: NR — Table 1 — «NR»
- age_max: NR — Table 1 — «NR»
- pct_female: 47.8 — Table 1 — «Female | 756(47.8%)»
- mode: online — Data Description — «via an online Google Form»
- attention_checks: NR — Experimental Design, Materials and Methods — «After being cleaned and coded in Excel, the data were imported into SmartPLS for analysis.»
- pub_status: journal — Venue metadata — «Data in brief; DOI: 10.1016/j.dib.2026.112952»
- language: English — Full text — «Survey on academic self-efficacy, academic stress, critical thinking, performance expectations, and students' AI dependency»
- funding_coi: Study commissioned/initiated by the Quantitative Analysis Center, QAglobal, Vietnam; no funding or conflict-of-interest statement in the text provided — Experimental Design, Materials and Methods; Ethics Statement — «This study was commissioned by the Quantitative Analysis Center of QAglobal, Vietnam, under Degree No. 022,026/QDNC-QAglobal.»
- notes: This is a Data in Brief data article. Correlations come only from the Fornell-Larcker table of a SmartPLS CFA (correlations of PLS latent variable scores), so they are coded as latent. Critical thinking and performance expectations (PE) are not in the construct dictionary and were not extracted. HTMT values were not extracted. Age is not reported. Raw data are posted on Mendeley Data (10.17632/2rrz65cxp9.1), which could be used to compute observed Pearson correlations.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Convenience sample recruited online through Google Form. — Data Description — «A convenience sampling method and probabilities based on the balanced male-female ratio were used in this study.»
2. отклик: **unclear** — The report gives a '100%' response rate, but it appears to mean complete responses among those who submitted the form (all items were mandatory). The number of students invited is not reported. — Data Description — «the response rate for online surveys reached 100%, and participants were required to answer all questions before submitting responses»
3. валидная шкала зависимости от ИИ: **yes** — The 5 items were adapted from Acosta-Enriquez et al. (ACOSTA5), and this report gives CFA evidence for them (loadings, CR, AVE, discriminant validity). — Table 2 — «AI dependency adapted from Acosta-Enriquez [5]; α = 0.918; CR = 0.938; AVE = 0.752»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha in this sample is 0.918. — Table 2 — «AI dependency adapted from Acosta-Enriquez [5]; α = 0.918»
5. валидные шкалы коррелятов: **yes** — Both extracted correlates (academic self-efficacy, academic stress) use items adapted from a published study (Zhang et al. [4]), with CFA support here. The reviewer should check whether Zhang et al. counts as a validate… — Experimental Design, Materials and Methods — «academic self-efficacy was measured using 6 items adapted from Zhang et al [4]... Academic stress was measured with 4 items adapted from Zhang et al [4].»
6. качество данных: **unclear** — The report says only that the data were 'cleaned'. It names no attention checks and no rule for invalid responses. — Experimental Design, Materials and Methods — «After being cleaned and coded in Excel, the data were imported into SmartPLS for analysis.»

Правки:
- 

Проверено: да

---

## ST068 · Waidyarathna 2026 · F1000Res

Основной отчёт R2621: [текст](../../fulltext/text/R2621.txt) · [PDF](../../fulltext/pdf/R2621.pdf) — «Productive and Unproductive AI Usage in Programming Education: Effects on Learning Behaviour, Creativity, and Performance with the Moderating Role of AI Litera…» — [DOI](https://doi.org/10.12688/f1000research.182898.1)
Расхождения в тексте: The sign of the UAIU correlation is uncertain. In Table 5 every UAIU correlation is printed as positive (LB 0.25, CPB 0.22, PP 0.28, MF 0.15), but the text calls them "weak to moderate negative correlations with Learning Behaviour (r = 0.25), Creative Programming Behaviour (r = 0.22), and Programming Performance (r = 0.28)". The text gives no direction for UAIU–Mindfulness. Minus signs may have been dropped throughout, so the UAIU–MF value (0.15 as printed) may also have the wrong sign. The same problem appears in the path coefficients: Table 7 and the text give UAIU→LB as 0.18 and UAIU→PP as 0.22 while calling them negative, and the abstract gives β = −0.18 and −0.22. The moderation results also conflict. In Table 9, Mindfulness × UAIU→LB is labelled "Weakens learning" and the text says lack of mindfulness intensifies harm, while the Figure 4(b) text says higher mindfulness gives a les…
Заметка ИИ: There is one sample. The only correlate in the construct dictionary is the study-specific Mindfulness composite, giving one effect: UAIU total × Mindfulness, r = 0.15 as printed, sign uncertain. The other correlates (AI literacy, learning behaviour, creativity, programming performance, AI interaction behaviour) are not in the dictionary and were not extracted.

### ST068-1 · SLIATE IT and Engineering undergraduate programming students, Sri Lanka (n=350)
Отчёты: R2621 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2621_1 · total (T2) | **mindfulness** · Mindfulness (study-specific: 14 general items + 4 programmi… | pearson | **0.15** | **350** | 1 | Page 20, Table 5 | «Mindfulness / 0.49 / 0.15 / 0.52 / 0.56 / 0.48 / 0.50 / 1» |

- E1: α ИИ 0.83, α коррелята 0.91; заметка: The correlation type is not stated (it could be SPSS composites or SmartPLS); coded Pearson provisionally. The sign is doubtful because the text calls the other UAIU correlations in Table 5 negative although they are printed as positive. The matrix gives two decimals only. The mindfulness composite…

**Ключевые поля выборки:**
- **n_analysed: 350** — Page 10, 4.3 — «From the relevant population of 7,779 students, 350 valid responses were retained for final analysis.»
- **population: university_students** — Page 17, Table 1 text — «The sample consists of 350 undergraduate students enrolled in programming-related disciplines»
- **sampling: convenience** — Page 10, 4.3 — «A multi-stage purposive sampling approach was employed.»
- **ai_system: ai_unspecified** — Page 11, 4.5; Page 4 — «Measured using five items capturing over-reliance on AI, copying without understanding, dependency, shortcut usage, and lack of critical evaluation. ... generative AI systems such as ChatGPT and GitHub Copilot»

**Остальные поля:**
- country: LKA — Page 10, 4.2 — «The study is conducted within the Sri Lanka Institute of Advanced Technological Education (SLIATE), which comprises multiple Advanced Technological Institutes …»
- data_years: NR — Page 10, 4.2 — «According to the official Students Intake and Enrollment Report (2025), the total student population in SLIATE is 26,406.»
- design: cross-sectional — Page 9, 4.1 — «This study adopts a quantitative, cross-sectional research design»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 17, Table 1 — «Age 18–20 110 31.4 21–23 205 58.6 24+ 35 10.0»
- age_sd: NR — Page 17, Table 1 — «Age 18–20 110 31.4 21–23 205 58.6 24+ 35 10.0»
- age_min: 18 (lower bound of youngest age category) — Page 17, Table 1 — «Age 18–20 110 31.4»
- age_max: NR (top category open: 24+) — Page 17, Table 1 — «24+ 35 10.0»
- pct_female: 43.4 — Page 17, Table 1 — «Female 152 43.4»
- mode: online — Page 12, 4.7 — «The questionnaire was administered either in online format across SLIATE institutes.»
- attention_checks: NR — Page 12, 4.8 — «Data cleaning and screening»
- pub_status: journal — Page 1 — «F1000Research 2026, 15:1212 ... [version 1; peer review: 1 approved]»
- language: English — Full text — «Productive and Unproductive AI Usage in Programming Education»
- funding_coi: No grants; no competing interests disclosed — Page 3 — «Competing interests: No competing interests were disclosed. Grant information: The author(s) declared that no grants were involved in supporting this work.»
- notes: UAIU is the study's measure of AI dependence: 5 ad hoc items covering over-reliance, copying without understanding, dependency, shortcut use and lack of critical evaluation. 'Ages' are reported only as categories. The sample consists of HND programme students (Year 2 51.4%, Year 3 48.6%) at SLIATE institutes.

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Multi-stage purposive (non-probability) sampling with voluntary participation. — Page 10, 4.3 — «A multi-stage purposive sampling approach was employed.»
2. отклик: **unclear** — No response rate reported; only that 350 valid responses were retained from an eligible population of 7,779. — Page 10, 4.3 — «From the relevant population of 7,779 students, 350 valid responses were retained for final analysis.»
3. валидная шкала зависимости от ИИ: **unclear** — UAIU is a 5-item ad hoc scale written for this study. Some psychometric evidence is given (alpha, CR, AVE, pilot test), but no loadings or HTMT values are reported. The reviewer should decide whether this counts as a va… — Page 10, 4.4; Page 19, Tables 3-4 — «Data were collected using a structured self-administered questionnaire specifically developed for this study. ... Unproductive AI Usage 0.87 0.59»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha for UAIU in this sample is 0.83. — Page 19, Table 3 — «Unproductive AI Usage 5 0.83»
5. валидные шкалы коррелятов: **no** — Mindfulness is a study-specific composite of 14 unnamed general items and 4 programming-specific items. No published instrument is cited. — Page 11, 4.5 — «General Mindfulness: 14 items assessing awareness and attention in everyday activities • Programming-Specific Mindfulness: 4 items assessing attention and focu…»
6. качество данных: **unclear** — Data cleaning and screening are mentioned and 'valid responses' were retained, but no attention checks or rule for invalid responses is described. — Page 12, 4.8 — «Data cleaning and screening»

Правки:
- 

Проверено: да

---

## ST069 · Wang 2026 · Scientific Reports

Основной отчёт R2637: [текст](../../fulltext/text/R2637.txt) · [PDF](../../fulltext/pdf/R2637.pdf) — «Empowerment or burden: promoting university students’ sense of gain in generative AI application based on the CAB-O framework» — [DOI](https://doi.org/10.1038/s41598-026-66780-y)
Не выписано ИИ: Pilot study of 80 frequent AI users (instrument pretest; no correlations reported). The STEM (n = 486) and Non-STEM (n = 255) subgroups are subsets of the same sample used in the multi-group analysis, not separately recruited samples.
Расхождения в тексте: 1) The text on p. 26 says the latent correlations between AI dependency and the gain dimensions are 'reported in Table 3', but they are in Table 4 (Table 3 gives CR/AVE). 2) Table 1 gives female 447 (52.5%) and male 403 (47.4%); 447/850 = 52.6%, so the printed percentage is used. 3) The text gives the latent correlation range as .007 to .903 and AD–CG = .763, AD–EG = .782; these match Table 4. 4) The CLF analysis (Supplementary Table S3, not available) reports that associations involving AI dependency were attenuated after controlling for common method variance. 5) Standardized path coefficients in Table 5 and Figure 2 are SEM paths and were not extracted.
Заметка ИИ: There is one eligible sample. Only one dictionary-eligible correlate (AI anxiety) is reported, and only as a latent correlation in the Fornell-Larcker/CFA matrix (Table 4). The other constructs in the matrix (AI literacy, AI usage shame, willingness to communicate with AI, content-based and experience-based sense of gain) fit no dictionary key. No construct-level Cronbach's alphas are reported; CR values were used as reliability.

### ST069-1 · University students with GenAI experience, 14 Chinese universities, Wenjuanxing survey (n = 850)
Отчёты: R2637 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R2637_1 · total (T4) | **ai_anxiety** · AI anxiety (AA) scale, study-adapted, not named | latent | **.062** | **850** | 1 | Page 24, Table 4 | «AA / .007 / .654 / .062 / 1.000» |

- E1: α ИИ CR = 0.809 (alpha NR), α коррелята CR = 0.880 (alpha NR); заметка: Standardized latent correlation (AD row/column x AA) from the CFA measurement model. No observed (Pearson) correlation is reported.

**Ключевые поля выборки:**
- **n_analysed: 850** — Page 24, Table 4 note — «Values represent standardized latent correlations estimated from the measurement model (N = 850).»
- **population: university_students** — Pages 16-17, 3.3 Data Collection — «targeting undergraduate and postgraduate students with prior exposure to GenAI»
- **sampling: convenience** — Pages 16-17, 3.3 Data Collection — «administered ... via the “Wenjuanxing” platform, targeting undergraduate and postgraduate students with prior exposure to GenAI»
- **ai_system: general_chatbot** — Page 3, Abstract; Pages 16-17, 3.3 — «A survey of 850 students with GenAI experience from 14 Chinese universities»

**Остальные поля:**
- country: CHN — Page 17, 3.3 Data Collection — «the sample covered 14 universities in China across provinces including Guangdong, Shandong, Sichuan, Guizhou, and Heilongjiang»
- data_years: 2025 — Page 16, 3.3 Data Collection — «The formal survey was administered between November and December, 2025, via the “Wenjuanxing” platform»
- design: cross-sectional — Page 38, 7. Limitations — «First, the cross-sectional design limits causal inference and does not establish temporal ordering among the variables»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Page 20, Table 1 — «NR»
- age_sd: NR — Page 20, Table 1 — «NR»
- age_min: NR — Page 20, Table 1 — «NR»
- age_max: NR — Page 20, Table 1 — «NR»
- pct_female: 52.5 — Page 20, Table 1 — «Gender Female 447 52.5%»
- mode: online — Page 16, 3.3 Data Collection — «via the “Wenjuanxing” platform»
- attention_checks: yes — Page 17, 3.3 Data Collection — «Following data cleaning—which involved purging invalid responses with excessively short completion times—a final dataset of 850 valid samples was retained.»
- pub_status: journal — Page 1 — «Scientific Reports Received: 13 June 2026 Accepted: 10 August 2026»
- language: English — Full text — «Empowerment or Burden: Promoting University Students’ Sense of Gain in Generative AI Application Based on the CAB-O Framework»
- funding_coi: Ministry of Education Youth Fund Project of Humanities and Social Sciences (24YJC880137); authors declare no competing interests — Pages 48-49, Competing Interests; Funding Declaration — «This study was supported by a Ministry of Education the Youth Fund Project of Humanities, Social Sciences and Social Sciences Research [Project approval number…»
- notes: The AI-dependency scale is study-specific (items adapted from unnamed established scales; listed in Supplementary Table S1, which was not available). Only reliability given per construct is composite reliability (CR = 0.809 for AD); alpha is reported only for the whole pilot instrument (0.908, n = 80). AI system is 'GenAI' with no specific tool named. Of the correlates, only AI anxiety (AA) fits the construct dictionary; AI literacy, AI usage shame, willingness to communicate with AI, content-based gain and experience-based gain are not dictionary constructs and were not extracted. The AI anx…

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online convenience survey via the Wenjuanxing crowdsourcing platform; no probability sampling. — Page 16, 3.3 Data Collection — «administered between November and December, 2025, via the “Wenjuanxing” platform, targeting undergraduate and postgraduate students with prior exposure to GenAI»
2. отклик: **unclear** — Response rate and the number invited or excluded are not reported; only the 850 valid responses are given. — Page 17, 3.3; Page 20, 4.1 — «A total of 850 valid responses were successfully retrieved and retained for the final analysis.»
3. валидная шкала зависимости от ИИ: **unclear** — The AI-dependency instrument is not named. Items were 'adapted from established international and domestic scales' and the sources are given only in Supplementary Table S1, which was not available. CFA (CR/AVE) is repor… — Page 16, 3.2 Measurement Instruments — «Items for each construct were adapted from established international and domestic scales and underwent contextual localization ... The measurement items and th…»
4. надёжность шкалы ИИ в выборке: **yes** — Composite reliability for AD = 0.809 (≥ .70), treated as an omega-type coefficient. No construct-level Cronbach's alpha is reported, so the reviewer should confirm that CR is acceptable here. — Page 22, Table 3 — «AD 0.809 0.520»
5. валидные шкалы коррелятов: **unclear** — The AI anxiety measure is not named. Items were adapted from unnamed scales and the sources appear only in the unavailable Supplementary Table S1. — Page 16, 3.2 Measurement Instruments — «Items for each construct were adapted from established international and domestic scales and underwent contextual localization»
6. качество данных: **yes** — States a rule for invalid responses: those with excessively short completion times were removed. — Page 17, 3.3 Data Collection — «purging invalid responses with excessively short completion times»

Правки:
- 

Проверено: да

---

## ST070 · Wang 2026 · Frontiers in psychology

Основной отчёт R2641: [текст](../../fulltext/text/R2641.txt) — «How academic stress leads to artificial intelligence-generated design dependency: the roles of academic procrastination and help-seeking behavior.» — [DOI](https://doi.org/10.3389/fpsyg.2026.1794730)
Расхождения в тексте: The zero-order correlations in the text (AS–AIGDD r = 0.368, AP–AIGDD r = 0.392) match the off-diagonal cells of the Fornell-Larcker Table 4 exactly. It is unclear whether the table values are latent correlations or the observed Pearson correlations repeated. Both rows were extracted as the form requires, but they are probably duplicates. The DAI family is listed as 5 items, but the report says the adaptation resulted in four items, and one item ('continuously follow the latest developments in AIGD') departs from the original content. The text says CR ranged from 0.852 to 0.86, but Table 3 gives a maximum CR of 0.868. Tables 2 and 4 give identical fit for the measurement and structural models. Academic help-seeking behavior (r = 0.481 with AIGDD) was not extracted because it matches no dictionary construct. Figure 2 (standardized SEM paths) and the PROCESS betas in Tables 5–6 are not ze…
Заметка ИИ: One sample, n = 492. Effects: AIGD dependency with academic stress and with academic procrastination, each extracted as both a Pearson row (from the text) and a latent row (from Table 4); the two pairs of values are identical and are probably duplicates. Age statistics were not reported. No funding or COI statement appears in the supplied text.

### ST070-1 · Chinese design undergraduates, 16 provinces, Wenjuanxing online survey (n = 492)
Отчёты: R2641 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | DAI · total (T4) | **academic_stress** · Academic stress scale (adapted from Jun & Choi, 2015; 4 ite… | pearson | **0.368** | **492** | 1 | Results, Descriptive statistics, correlations, an… | «academic stress demonstrated significant positive correlations with ... AIGD dependency (r = 0.368, p < 0.05)» |
| E2 | DAI · total (T4) | **academic_stress** · Academic stress scale (adapted from Jun & Choi, 2015; 4 ite… | latent | **0.368** | **492** | 1 | Table 4 | «AIGDD / 0.368 / 0.392 / 0.481 / 0.770» |
| E3 | DAI · total (T4) | **procrastination** · Academic Procrastination Scale (adapted from Solomon & Roth… | pearson | **0.392** | **492** | 1 | Results, Descriptive statistics, correlations, an… | «Both academic procrastination (r = 0.392, p < 0.05) and academic help-seeking behavior (r = 0.481, p < 0.05) were positively correlated with AIGD dependency.» |
| E4 | DAI · total (T4) | **procrastination** · Academic Procrastination Scale (adapted from Solomon & Roth… | latent | **0.392** | **492** | 1 | Table 4 | «AIGDD / 0.368 / 0.392 / 0.481 / 0.770» |

- E1: α ИИ 0.842, α коррелята 0.864; заметка: Same value as the Fornell-Larcker Table 4 entry. The two are probably the same coefficient reported twice, so do not double-count. The DAI was adapted to 4 AIGD items.
- E2: α ИИ 0.842, α коррелята 0.864; заметка: Off-diagonal value in the Fornell-Larcker table. It is identical to the text r, so it is likely the same coefficient and not a separate latent estimate. Reviewer to decide whether to keep only one row.
- E3: α ИИ 0.842, α коррелята 0.859; заметка: Same value as the Fornell-Larcker Table 4 entry. The two are probably the same coefficient reported twice, so do not double-count.
- E4: α ИИ 0.842, α коррелята 0.859; заметка: Off-diagonal value in the Fornell-Larcker table. It is identical to the text r, so it is likely the same coefficient and not a separate latent estimate. Reviewer to decide whether to keep only one row.

**Ключевые поля выборки:**
- **n_analysed: 492** — Methods, Sample and data collection; Table 1 — «The final sample includes 492 valid questionnaires for subsequent statistical analysis.»
- **population: university_students** — Methods, Sample and data collection — «The participants are design undergraduates from public universities from 16 provinces across the country.»
- **sampling: convenience** — Methods, Sample and data collection — «The survey adopts a non-probability purposive sampling strategy. We invited university students from various regions in China to participate in this survey, with the assistance of design university teachers.»
- **ai_system: task_assistant** — Introduction; Methods, Sample and data collection — «tools such as Midjourney, DALL-E, Stable Diffusion, and Canva serve as "collaborators," ... "Have you used AIGD tools to complete design tasks in the past six months?"»

**Остальные поля:**
- country: CHN — Methods, Sample and data collection — «we conducted an online survey to collect data from students in design majors at Chinese universities»
- data_years: 2025 — Methods, Sample and data collection — «In September 2025, after approval from our university's Institutional Review Board, we conducted an online survey»
- design: cross-sectional — Limitations and future work — «First, this study adopts a cross-sectional design.»
- clinical_group: NA — NA — «NA»
- age_mean: NR — Results, Frequency results — «Respondents aged 21 accounted for the largest proportion (21.7%)»
- age_sd: NR — NA — «NR»
- age_min: NR — NA — «NR»
- age_max: NR — NA — «NR»
- pct_female: 47.76 — Table 1 — «Gender | Female | 235 | 47.76»
- mode: online — Methods, Sample and data collection — «We used the "Wenjuanxing" questionnaire collection platform for data collection ... The questionnaire links were distributed via WeChat.»
- attention_checks: yes — Methods, Sample and data collection — «During data cleaning, we exclude the same answers and invalid questionnaires among all scale items. The final sample includes 492 valid questionnaires»
- pub_status: journal — Header (venue) — «Frontiers in psychology; DOI: 10.3389/fpsyg.2026.1794730»
- language: English — Full text — «How academic stress leads to artificial intelligence-generated design dependency»
- funding_coi: NR (no funding or conflict-of-interest statement in the supplied text); participants received a small incentive — Methods, Sample and data collection — «Participation was voluntary and anonymous, and each participant received a small incentive.»
- notes: Only students who had used AIGD tools in the past six months could take part (screening question). Of 570 questionnaires returned, 492 were valid. All scales are 7-point Likert, translated into Chinese. The AIGD dependency scale is a 4-item adaptation of Morales-García et al. (2024). Age is reported only as a modal age of 21 (21.7%).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Non-probability purposive sampling through teachers and WeChat, using the Wenjuanxing online platform — Methods, Sample and data collection — «The survey adopts a non-probability purposive sampling strategy.»
2. отклик: **unclear** — Only the number of questionnaires returned (570) and the number valid (492) are reported. The number invited and the response rate are not reported. — Methods, Sample and data collection — «The survey lasted for 2 weeks and yielded 570 online questionnaires.»
3. валидная шкала зависимости от ИИ: **yes** — Adapted from the published Morales-García et al. (2024) AI dependence scale (4 items here). CFA in this sample shows loadings from .692 to .912, CR .852 and AVE .593. — Methods, AIGD dependency; Table 3 — «The AIGD dependency scale was adapted from Morales-García et al. (2024) measure of AI dependency (Cronbach's α = 0.87).»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha = .842 in this sample — Methods, AIGD dependency; Table 3 — «In this study, the scale demonstrated adequate reliability (Cronbach's α = 0.842).»
5. валидные шкалы коррелятов: **yes** — Academic stress is adapted from Jun and Choi (2015) / Park et al. (2008). Academic procrastination is adapted from Solomon and Rothblum's PASS. Both are published instruments, shortened to 4 items each. — Methods, Academic stress; Academic procrastination — «The academic stress scale was adapted from Jun and Choi's (2015) work ... adapted from Solomon and Rothblum's (1984) Student Procrastination Assessment Scale»
6. качество данных: **yes** — Identical-response (straightlining) and invalid questionnaires were excluded, and abnormal response patterns were screened — Methods, Sample and data collection; Data analysis — «we exclude the same answers and invalid questionnaires among all scale items ... checked for missing values and abnormal response patterns.»

Правки:
- 

Проверено: да

