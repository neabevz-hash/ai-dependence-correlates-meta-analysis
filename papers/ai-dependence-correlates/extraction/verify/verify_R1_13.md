# Проверка выписывания — файл 13 из 13

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

## ST121 · Marriott 2023 · Psychology and Marketing

Основной отчёт R4962: [текст](../../fulltext/text/R4962.txt) — «One is the loneliest number… Two can be as bad as one. The influence of AI Friendship Apps on users' well‐being and addiction» — [DOI](https://doi.org/10.1002/mar.21899)
Не выписано ИИ: Study 1 (netnography: 321 Reddit r/Replika posts and 21 semi-structured interviews) is qualitative and has no AI-dependence measure or correlations.
Расхождения в тексте: The loneliness to addiction path is β = 0.181 in the text (p.12) but 0.108 in Table 3. The text says all CR values are <0.60 and all AVE values <0.50, but Table 2 shows CR 0.856–0.960 and AVE 0.601–0.860, so '<' appears to be a typo for '>'. The text states '≥ 0.050 = significant' for p values (obviously reversed). The text says the data are nonparametric, but Table 2 correlations are not labelled as Pearson, Spearman or latent. No figure-only coefficients.
Заметка ИИ: One sample and one effect extracted (Addiction × Loneliness, latent r = 0.221, n = 572). Other variables in the correlation table are AI-specific perceptions (fear of judgment by the AI, well-being gained from the app, AI agreeableness, sentience, warmth, ubiquity, relationship with AI) and fall outside the construct dictionary.

### ST121-1 · Study 2, Prolific AI friendship app users, USA, n=572
Отчёты: R4962 (main)

**Эффекты — ключевые числа сверить по таблице статьи:**

| | Шкала ИИ · часть (тип) | Коррелят · шкала | Стат. | **r** | **n** | Волна | Где | Цитата |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | ADHOC_R4962_1 · total (T1) | **loneliness** · Loneliness, 3 items (Palgi et al., 2020) | latent | **0.221** | **572** | 1 | Table 2 (p.11) | «Addiction 0.942 0.732 −0.186 0.018 0.555 0.221 0.380 0.348 1 (columns: CR, AVE, Ubiquity, Agreeableness, Judgment, Loneliness, ...)» |

- E1: α ИИ 0.927, α коррелята 0.921; заметка: Table 2 is a discriminant-validity (Fornell-Larcker-type) intercorrelation table with 1 on the diagonal. Coded as latent, but it is not stated whether these are latent (CFA) or observed correlations; reviewer to check.

**⚠ Проверка скриптом (обратите внимание):**
- в независимом проходе были ещё числа: 0.31 — нет ли пропущенных эффектов (они могут быть и не про эту выборку)

**Ключевые поля выборки:**
- **n_analysed: 572** — p.10, 6.1 — «Of the 600 responses collected, 572 are usable.»
- **population: general_adults** — p.10, 6.1 — «The screening questions concerned the age of participants, to ensure they are over the age of 18»
- **sampling: quota or online panel** — p.10, 6.1 — «Simple random sampling is employed through Prolific, and the final sample comprised of AI friendship app users in the United States.»
- **ai_system: ai_companion** — p.11, 6.1 — «Most respondents used Replika (n = 220; 38.5%) with other respondents report to use Kuki (n = 162; 28.3%), Anima (n = 70; 12.2%), Woebot (n = 48; 8.4%), Wysa (n = 45; 7.9%) and "other"»

**Остальные поля:**
- country: USA — p.10, 6.1 — «the final sample comprised of AI friendship app users in the United States»
- data_years: NR — p.10, 6.1 — «the 600 responses were obtained within 2 h of the survey being made live»
- design: cross-sectional — p.14, 7.3 — «Through a netnography and a cross‐sectional study, this research offers a snapshot in time»
- clinical_group: NA — NA — «NA»
- age_mean: NR — p.11, 6.1 — «Most respondents were between the ages of 20 and 45 (youngest = 18; oldest = 85).»
- age_sd: NR — p.11, 6.1 — «Most respondents were between the ages of 20 and 45»
- age_min: 18 — p.11, 6.1 — «(youngest = 18; oldest = 85)»
- age_max: 85 — p.11, 6.1 — «(youngest = 18; oldest = 85)»
- pct_female: 36.7 — p.11, 6.1 — «346 (60.5%) are male, 210 (36.7%) female, 10 (1.7%) nonbinary and 6 (1.0%) preferred not to say»
- mode: online — p.10, 6.1 — «Due to the use of Prolific, the 600 responses were obtained within 2 h of the survey being made live»
- attention_checks: yes — p.10, 6.1 — «Those who did not select "5" were discounted from the final sample ... 28 respondents failed the attention check question and were removed from the analysis.»
- pub_status: journal — p.1, header — «Psychol Mark. 2023;1–16.»
- language: English — full text — «One is the loneliest number… Two can be as bad as one.»
- funding_coi: Funding NR; authors declare no conflicts of interest — p.15, Conflict of interest statement — «The authors declare no conflicts of interest.»
- notes: Only one eligible correlate (loneliness, 3 items from Palgi et al., 2020) is paired with addiction. Fear of judgment refers to judgment by the AI friend ('I worry about how my AI friend evaluates me'), so it is AI-specific and not trait social anxiety. 'AI well-being' is well-being gained from the app, not general wellbeing. Agreeableness/warmth/sentience/ubiquity are perceived traits of the app, not user traits. None of these were extracted. The addiction scale (7 items, AD1 deleted) was adapted from a fast-food addiction scale (Farah & Shahzad, 2020).

**Риск смещения (6 пунктов AXIS, `forms/rob.md`):**
1. отбор выборки: **no** — Online crowdsourcing panel (Prolific). The authors call it 'simple random sampling', but it is not a probability sample. — p.10, 6.1 — «Simple random sampling is employed through Prolific»
2. отклик: **unclear** — No response rate reported. The authors state that nonresponse bias could not be measured. — p.10, 6.1 — «As the data was collected using Prolific, nonresponse bias is not able to be measured as relevant information is not made available to perform the analysis.»
3. валидная шкала зависимости от ИИ: **yes** — Items adapted from a published fast-food addiction scale. This report gives CFA evidence (CR = 0.942, AVE = 0.732, measurement-model fit). There is no prior validation for AI apps, so the reviewer should confirm that th… — p.10 6.2; Table 2 — «7‐items for addiction (sample item "Not chatting to my AI friend is something I worry about") from Farah and Shahzad (2020).»
4. надёжность шкалы ИИ в выборке: **yes** — Cronbach's alpha 0.927 in this sample. — p.11, 6.3 — «AI well‐being = 0.930; Addiction = 0.927»
5. валидные шкалы коррелятов: **yes** — The only extracted correlate is loneliness, measured with 3 items from a published source (Palgi et al., 2020). — p.11, 6.2 — «3‐items for loneliness (Palgi et al., 2020; sample item "I often feel left out")»
6. качество данных: **yes** — Attention-check item; failures removed; z-score outlier screening. — p.10, 6.1 — «28 respondents failed the attention check question and were removed from the analysis.»

Правки:
- 

Проверено: да

