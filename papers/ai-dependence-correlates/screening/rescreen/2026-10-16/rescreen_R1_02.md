# Отбор вслепую по правилу защиты, часть 2

Записи 151–300 из 3834: всё, что исключили обе модели, кроме калибровочной выборки. Отбор вслепую по правилу защиты (протокол, §11b). **Меток ИИ здесь нет** — решайте по тем же критериям, что и в калибровке; в сомнениях — `?`. Порядок случайный (зерно 20261018).

**Быстрый режим:** достаточно одного символа — `+`, `?` или просто `-` (исключить, причина не нужна).

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: количественное исследование людей, где измерена зависимость от ИИ (шкала зависимости, аддикции, проблемного использования, over-reliance или эмоциональной зависимости) и может найтись её корреляция хотя бы с одним нашим коррелятом |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, редакционная статья, комментарий, теоретическая работа |
| `-2` | исключить: качественное или не эмпирическое исследование без количественной меры зависимости |
| `-3` | исключить: нет меры зависимости от ИИ: только частота использования, принятие, доверие, грамотность, технострес, страх ИИ — или over-reliance только как поведение в эксперименте |
| `-4` | исключить: среди измеренных конструктов нет ни одного нашего коррелята |
| `-5` | исключить: ИИ как инструмент (выявляет или лечит зависимость, анализирует данные), социальные роботы, «dependence» в другом смысле |
| `-6` | исключить: не по теме или другое — напишите почему |

Пример: `**Решение:** -3 только частота использования`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Наши корреляты:** депрессия, тревожность, стресс, одиночество, социальная тревожность, самооценка, прокрастинация; а также дистресс, благополучие, самоэффективность, самоконтроль, импульсивность, FoMO, проблемное использование смартфона, интернета и соцсетей, Большая пятёрка, тревожная и избегающая привязанность, скука, осознанность, сон, учебный стресс, мотивы бегства, социальная поддержка, тревога перед ИИ. Корреляции обычно лежат в таблице, о которой аннотация молчит: если зависимость от ИИ измерена шкалой в выборке людей, а конструкты в аннотации не перечислены, — `?`. Подробно — протокол, §8 и §13.

---

### 151 · R4510

**The promising and problematic potential of generative AI as a leveler of the publishing playing field**

2024 · Journal of English for Research Publication Purposes · journal-article · https://doi.org/10.1075/jerpp.00025.bel

Abstract This perspective paper considers the affordances and challenges of generative AI for linguaculturally diverse scholars in a still English-dominant academic publishing world. Chief among the questions examined is whether AI offers a viable path forward toward greater research publication equity but, at the same time, something much more fraught. In other words, the paper explores how promising the apparent equalizing potential of generative AI may be. Might, for example, generative AI offer a smoother path to visibility, but in so doing, actually make the uniqueness of diverse scholars’ contributions far less visible? The paradoxical potential of generative AI is discussed first in this paper by surveying, at this particular phase of AI development, some of the salient advantages of generative AI use for research prewriting, writing, and post-writing, that is, AI’s ability to assist with such essentials as idea generation, text development, and text refinement. The apparent democratizing advantages of AI for each of these major stages of research writing are then interrogated and problematized. The paper concludes with a brief speculative path forward.

**Решение:** -

---

### 152 · R3457

**Automatically Fixing Dependency Breaking Changes**

2025 · Proceedings of the ACM on software engineering. · journalarticle, article · en · https://doi.org/10.1145/3729366

Breaking changes in dependencies are a common challenge in software development, requiring manual intervention to resolve. This study examines how well Large Language Models (LLMs) automate the repair of breaking changes caused by dependency updates in Java projects. Although earlier methods have mostly concentrated on detecting breaking changes or investigating their impact, they have not been able to completely automate the repair process. We introduce and compare two new approaches: an agentic system that combines automated tool usage with LLMs, and a recursive zero-shot approach, employing iterative prompt refinement. Our experimental framework assesses the repair success of both approaches, using the BUMP dataset of curated breaking changes. We also investigate the impact of variables such as dependency popularity and prompt configuration on repair outcomes. Our results demonstrate a substantial difference in test suite success rates, with the agentic approach achieving a repair success rate of up to 23%, while the zero-shot prompting approach achieved a repair success rate of up to 19%. We show that automated program repair of breaking dependencies with LLMs is feasible and can be optimised to achieve better repair outcomes.

**Решение:** -

---

### 153 · R2322

**Vulnerability Detection Using Static Application Security Testing and Artificial Intelligence Techniques**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7395374

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 154 · R0393

**Diagnostic performance of a specific local Turkish large language model in detecting alcohol use disorder across internal medicine practice: A 42-patient pilot study**

2026 · Journal of Dependence · journal-article · https://doi.org/10.51982/bagimli.619

Objective: Alcohol use disorder (AUD) is underdiagnosed in internal medicine. We evaluated a local large language model (LLM), fine-tuned on a Turkish medical corpus, for detecting AUD across outpatient, emergency and inpatient settings. Method: We retrospectively analyzed 42 adult patients at a tertiary state hospital (January–May 2024), in a single-center de-identified dataset modeled on the MIMIC-IV schema. The reference standard was the clinician-confirmed DSM-5 AUD diagnosis; comparators were the Alcohol Use Disorders Identification Test, Consumption version (AUDIT-C), gamma-glutamyl transferase (GGT), mean corpuscular volume and the aspartate aminotransferase/alanine aminotransferase ratio. A Llama-3-8B-Instruct model, fine-tuned via low-rank adaptation on an in-hospital GPU server, produced binary predictions, probabilities and severity categories. Analyses used Wilson 95% confidence intervals, bootstrap AUC, Cohen's κ and the Results: Mean age was 53.0 ± 15.0 years; 50.0% were female. AUD prevalence was 47.6% (20/42). The LLM achieved sensitivity 85.0% (95% CI, 64.0–94.8), specificity 90.9% (72.2–97.5), accuracy 88.1%, area under the curve (AUC) 0.864 (0.720–0.977) and κ = 0.761. Within the 17 true positives, severity matched the reference exactly (quadratic-weighted κ = 1.000), conditional on correct detection in a small subgroup. Within this enriched pilot cohort, AUDIT-C and GGT showed perfect separation (AUC = 1.000) and the LLM AUC was lower (DeLong p = 0.038). This ordering is a ceiling effect of the present cohort and is not a general property of these markers. Conclusion: The local LLM achieved clinically acceptable accuracy and exact severity classification within correctly flagged cases. Its principal value lies where AUDIT-C is not routine...

**Решение:** -

---

### 155 · R5122

**Healthcare uses of artificial intelligence: Challenges and opportunities for growth.**

2019 · Healthcare management forum · journal article · eng · https://doi.org/10.1177/0840470419843831

Forms of Artificial Intelligence (AI), like deep learning algorithms and neural networks, are being intensely explored for novel healthcare applications in areas such as imaging and diagnoses, risk analysis, lifestyle management and monitoring, health information management, and virtual health assistance. Expected benefits in these areas are wide-ranging and include increased speed in imaging, greater insight into predictive screening, and decreased healthcare costs and inefficiency. However, AI-based clinical tools also create a host of situations wherein commonly-held values and ethical principles may be challenged. In this short column, we highlight three potentially problematic aspects of AI use in healthcare: (1) dynamic information and consent, (2) transparency and ownership, and (3) privacy and discrimination. We discuss their impact on patient/client, clinician, and health institution values and suggest ways to tackle this impact. We propose that AI-related ethical challenges may represent an opportunity for growth in organizations.

**Решение:** -

---

### 156 · R2487

**Perceptions on artificial intelligence among anaesthesia and intensive care professionals: An international survey on attitudes, expectations and needs.**

2026 · Journal of clinical monitoring and computing · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10877-026-01464-6

Background Artificial intelligence (AI) can enhance diagnostics, treatment, and workflow efficiency. However, successful integration into clinical practice depends on users' acceptance. Objective To investigate benefits, barriers, and challenges of AI applications among anaesthesia and intensive care professionals. Design International online survey. Main outcome measures The survey included items on familiarity and experiences with AI applications, perceived benefits, concerns, and demographic variables. Descriptive analyses, fisher exact tests, χ²-tests, odds ratios, and Spearman rank correlations were used to explore associations between responses and demographics. Results The survey was distributed by the European Society of Anaesthesiology and Intensive Care in 2023. A total of 510 respondents completed the entire survey, primarily from Europe (78%) and Asia (14.5%), and the majority were board-certified anaesthesiologists (86.3%). 86.5% of the respondents were aware of AI applications, but only 36.8% reported regular encounters. Familiarity was higher among males and intensive care specialists. 94.5% expressed interest in AI training, particularly younger and less experienced professionals. 94.7% expressed willingness to use AI applications, citing benefits such as improved decision-making (92.7%), complication anticipation (88.6%), and workload reduction (80.1%). Younger and female respondents were more optimistic about AI's benefits. Key concerns included lack of explainability (68.4%), over-reliance on AI (80.8%), and medico-legal uncertainties (58.4%). Scepticism was attributed to insufficient validation studies and fears of inaccurate outputs, particularly among experienced clinicians. Conclusions This international survey shows cautious optimism among anaesthesia and intensive care professionals regarding AI applications. Adoption in clinical practice requires tailored training that accounts also for demographic-specific concerns, robust validation, and clear ethical and legal frameworks.

**Решение:** -

---

### 157 · R0774

**AI Companions for Mental Health: Regulatory Qualification Between Intended Use and Functional Reality. Comparative Remarks Between the EU and the US**

2026 · BioLaw Journal - Rivista di BioDiritto · journalarticle/, article · en · https://doi.org/10.15168/2284-4503-4220

This article examines the regulatory landscape concerning AI Companions between the EU and the US. It concludes that in both legal systems the intended use of a product or service expressed by the manufacturer is used as a decisive element whenever it is dubious as to where a device is or not a medical device. It is argued that, in many cases, the prevalence of the manufacturer’s intended use in dubious cases is used to market products as “simple” consumer products whereas, instead, they would need a clinical validation under the medical devices regulations of the two legal systems. This becomes more evident with AI Companions, LLM-based (for now) services which offer companionship to users that are generally not categorized as a medical device. The growing cases of suicide, self-harm, depression, and addiction by young people highlight the limits of the primacy of the manufacturer’s intended use when defining or not an object as a medical device. As authors, we argue in favour of a functional qualification of the intended use, as both the current EU and US regulatory landscape do not ensure a sufficiently high level of care and protection of consumers and patients alike.

**Решение:** -

---

### 158 · R2257

**ChatGPT as a Writing Aid: Opportunities and Challenges in Developing Students’ Logical Reasoning Skills**

2026 · Journal of English for Academic and Specific Purposes (JEASP) · journalarticle, review, article · https://doi.org/10.18860/jeasp.v9i1.38035

The integration of artificial intelligence (AI) in education has transformed the academic landscape, offering new tools to enhance students’ writing and reasoning skills. This study investigates the effectiveness of ChatGPT in supporting logical reasoning in writing among university students. The research employs a descriptive qualitative approach, incorporating surveys and semi-structured interviews with 15 students from the English Education Program at Universitas Islam Madura. The study examines how ChatGPT influences argument structuring, idea generation, and clarity in writing, while also identifying potential challenges and limitations. The findings indicate that 93.3% of students perceive ChatGPT as beneficial, particularly in improving logical coherence and content organization. Students reported that ChatGPT helps develop structured arguments, refine transitions, and overcome writing difficulties. However, significant limitations were identified, including the lack of proper citations, occasional inaccuracies, and the risk of over-reliance on AI-generated content. The study highlights the importance of critical evaluation when using ChatGPT, emphasizing that AI should be a supplementary tool rather than a primary knowledge source. These results contribute to ongoing discussions on AI’s role in higher education, underscoring the need for AI literacy training and ethical AI integration in academic writing. The study suggests that future research should explore long-term impacts of AI-assisted learning, real-time citation integration, and AI’s role in fostering independent critical thinking, ensuring AI remains a constructive force in education.

**Решение:** -

---

### 159 · R0851

**Artificial Intelligence and Youth: Cognitive, Educational, and Behavioral Impacts**

2026 · AI · article, journalarticle, review · en · https://doi.org/10.3390/ai7040121

Background: Artificial Intelligence (AI) and Generative AI (GenAI) are increasingly integrated into educational and professional settings, offering personalized learning, productivity gains, and enhanced engagement. However, excessive reliance may compromise critical thinking, autonomous problem-solving, and emotional regulation among youth (i.e., adolescents and young adults) and early-career professionals. Aim: This review examines the cognitive, educational, and behavioral impacts of AI and GenAI use in youth, highlighting implications for their responsible integration in learning and professional development. Methods: A narrative review was conducted, synthesizing empirical studies, psychometric instruments, and international policy frameworks addressing AI engagement. Emphasis was placed on cognitive, behavioral, educational, and ethical dimensions across youth and early-career professionals. Results: AI enhances learning efficiency, creativity, and professional decision-making but may also foster cognitive offloading, dependency, and addiction-like behaviors. Instruments such as the Conversational AI Dependence Scale (CAIDS) and the Problematic ChatGPT Use Scale (PCGUS) help identify maladaptive patterns. Effective strategies include structured pedagogy, human oversight, reflective practice, AI literacy, and ethical guidance. Paradoxically, higher AI competence and trust may increase reliance, underscoring the need for guided and balanced engagement. Conclusions: Responsible AI integration requires multidimensional approaches combining instructional scaffolding, metacognitive strategies, supervision, and governance to preserve autonomy, professional judgment, and cognitive development in youth.

**Решение:** -

---

### 160 · R0680

**Artificial Intelligence and Stigma in Addiction Research: Insights From the HEALing Communities Study Coalition Meetings.**

2026 · Journal of addiction medicine · journal article · eng · https://doi.org/10.1097/adm.0000000000001749

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 161 · R2361

**Predictive analysis of cognitive dependence level associated with generative Artificial Intelligence use in university students through supervised classification algorithms**

2026 · Computer and Electronic Sciences Theory and Applications · journalarticle, article · https://doi.org/10.17981/cesta.07.01.2026.07

Introduction: The adoption and use of generative artificial intelligence (GAI) tools has become increasingly common in the academic activities of university students. Current scientific debate focuses on understanding how the intensive use of these technologies may influence intellectual autonomy, critical thinking, and the delegation of cognitive tasks.Objective: To construct and compare three supervised classification models capable of predicting the level of perceived cognitive dependence among students at the University of La Guajira, based on sociodemographic, technological, usage pattern, and academic perception variables, incorporating a variable engineering process.Method: A structured questionnaire was administered to 299 university students during the 2026-1 academic period. The research process followed the CRISP-DM methodology. The target variable was constructed as a summative index based on two Likert-scale items: loss of critical thinking and decreased autonomy, categorized into three levels: low, medium, and high. Eleven derived variables were generated through variable engineering, and SMOTE was applied to balance the training classes. Decision Tree, k-NN, and Random Forest models were trained using GridSearchCV for hyperparameter optimization.Results: The Random Forest model achieved the best performance in the testing phase, with an accuracy of 0.89 and an F1-macro score of 0.84. In addition, the multiclass ROC curve showed AUC values of 0.99, 0.96, and 0.96 for the three classes. Seven of the eleven engineered variables were among the top 20 most important predictors, with the ratio of cognitive replacement tasks standing out as a particularly relevant variable.Conclusions: Perceived cognitive dependence on generative artificial intelligence is predictable from sociotechnical variables. The results suggest that the strongest predictors are not related to the frequency of use, but rather to the type of tasks delegated to AI. These findings provide useful evidence for designing institutional policies aimed at promoting the responsible and critical use of generative AI in higher education.

**Решение:** ?

---

### 162 · R3874

**A qualitative survey on perception of medical students on the use of large language models for educational purposes.**

2025 · Advances in physiology education · journal article, journalarticle, review · eng · https://doi.org/10.1152/advan.00088.2024

Large language models (LLMs)-based chatbots use natural language processing and are a type of generative artificial intelligence (AI) that is capable of comprehending user input and generating output in various formats. They offer potential benefits in medical education. This study explored the student's feedback on the utilization of LLMs in medical education. We conducted an in-depth interview with open-ended questions with Indian medical students via telephone conversation. The recording (average time: 55.28 ± 18.04 min) was transcribed and thematically analyzed to find major themes and subthemes. We used QDA Miner Lite v.2.0.8 (Provalis Research, Montreal, Canada) for the thematic analysis of the text. A total of 25 students from eight Indian states studying from the first to final year of studies participated in this study. Three major themes were identified: usage scenario, augmented learning, and limitation of LLMs. Students use LLMs for clarifying complex topics, searching for customized answers, solving multiple-choice questions, making simplified notes, and streamlining assignments. While they appreciated the ease of access, ready reference for getting clarity on doubts, lucid explanation of questions, and time-saving aspects of LLMs, concerns were raised regarding erroneous results, limited usage due to reliability and privacy issues, and the overreliance on chatbots for educational needs. Hence, they emphasized the need for training for the integration of LLM in medical education. In conclusion, according to students' perception, LLMs have the potential to enhance medical education. However, addressing challenges and leveraging the strengths of LLMs are crucial for optimizing their integration into medical education. NEW & NOTEWORTHY The study demonstrates the student's perspective on the role of large language models (LLM)-based chatbots in medical education. Students' responses generated three major themes of various usage scenarios, how LLMs can enhance learning, and the ethical considerations in the integration of LLMs into medical curricula. By identifying both the benefits and limitations of LLMs in medical education, the study offers insights for educators and policymakers to navigate the complexities of LLM in educational settings.

**Решение:** -

---

### 163 · R3411

**EFL STUDENTS’ PERSPECTIVES ON CHATGPT AT SEEU IN NORTH MACEDONIA: POTENTIAL BENEFITS AND CHALLENGES**

2025 · Journal of Languages for Specific Purposes · article · deu/ger · https://doaj.org/article/6c70c56cc4ef4216b4f325382027abc4

This study examines students’ views and experiences regarding the use of ChatGPT at South East European University (SEEU) in North Macedonia, focusing on its benefits and challenges. A review of existing literature highlights the increasing interest in Artificial Intelligence (AI) tools like ChatGPT in educational settings, emphasizing their potential to support language learning, offer personalized feedback, and boost student engagement. However, concerns are also raised about the possible drawbacks of AI in education, including the risk of over-reliance, which might hinder critical thinking and problem-solving skills. Ethical issues, such as academic integrity and the reliability of AI-generated responses, are also frequently mentioned, particularly in relation to writing tasks and assessments. There is additional concern that dependence on AI may limit students’ ability to learn independently.The study uses a questionnaire to explore the challenges and benefits of integrating ChatGPT into EFL education. The findings suggest that while students perceive ChatGPT as a useful resource for learning and support its use for specific academic purposes, acceptance varies depending on the task and individual attitudes toward AI in education. The data recommend that ChatGPT should serve as a supplementary tool rather than a replacement for independent thought and creativity, and stress the importance of verifying the accuracy of AI-generated content.

**Решение:** -

---

### 164 · R4138

**From Assistance to Dependence: The Growing Influence of Chatbots in Human Life**

2025 · Iconic Research and Engineering Journals · article · en · https://doi.org/10.64388/irev9i5-1712073

The rapid rise of Artificial Intelligence, particularly conversational models like ChatGPT, has revolutionized how individuals learn, work, and communicate. Since 2021, AI has shifted from a futuristic concept to an everyday reality, reshaping expectations and experiences across educational and professional spaces. With ChatGPT's introduction in 2022, it's adoption grew exponentially as students and users embraced it as a powerful support system that can solve assignments, coding tasks, and offer real-time guidance. This paper explores the emergence and widespread usage of chatbots, highlighting the massive growth in user engagement and the transformation in learning patterns. It also examines the emerging dependency on AI tools and emphasizes the importance of balancing innovation with independent thinking to ensure technology remains an aid, not a replacement, for human intellect.

**Решение:** -

---

### 165 · R3798

**Correcting Prompt Dependence in LLM Benchmarks: A Bayesian Hierarchical Model with Embedding-Space Clustering**

2025 · arXiv (Cornell University) · preprint · en · https://doi.org/10.48550/arxiv.2510.05709

LLM benchmarking metrics often misstate performance and uncertainty as they rely on two assumptions that frequently do not hold in practice: (i) a sufficient number of evaluations are available for classical inference, and (ii) test prompts are independent. We propose a corrective Bayesian hierarchical model with embedding-space clustering that provides robust performance metrics in limited-data settings while correcting for prompt dependence. We apply the approach to adversarial robustness benchmarks, showing consistent recovery of clustering structure, resulting in more reliable performance metrics, with 4-73% improvements to mean absolute errors and 40-450 unit improvements to expected log posterior densities.

**Решение:** -

---

### 166 · R0886

**Semantic Information Architectures and Topic Ensemble Properties in AI Delivery of Product Information in the Domain of Water Treatment**

2026 · conference-paper · https://doi.org/10.3390/engproc2026143049

This paper examines how semantic information architectures within technical communication shape topic ensemble properties being relevant for retrieval-augmented generation (RAG) systems. They allow for investigating the AI-readiness of technical content for AI-based delivery in the present domain of water treatment. The analysis characterizes the dependence of AI-driven delivery on similarity-based metrics and metadata completeness. Topic content management is operationalized within the PI-Class framework by analyzing topics with respect to content variants and versioning, and by assessing their implications for retrieval precision. Building on previous research in technical communication, the paper further investigates the role of large language models (LLMs) in supporting the content engineering phase through automated analysis of legacy documents, derivation of metadata classifications, and curation of the resulting semantic structures in knowledge graphs.

**Решение:** -

---

### 167 · R1760

**Operator Dependence of Musculoskeletal US: Can AI Help?**

2026 · Radiology · journal-article · https://doi.org/10.1148/radiol.261219

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 168 · R4945

**Civil Engineering Education: Artificial Intelligence in Transforming Traditional Learning into Intelligent and Industry-Ready Education**

2023 · Educational Administration: Theory and Practice · journalarticle, review, article · en · https://doi.org/10.67145/kuey.v29i2.12224

Civil engineering education is undergoing a fundamental transformation as artificial intelligence (AI) increasingly influences both engineering practice and higher education. Traditional classroom-based approaches remain effective for establishing fundamental engineering knowledge; however, they often have limitations in explaining complex, nonlinear, data-intensive, and field-oriented problems involving structural behaviour, geotechnical uncertainty, transportation systems, environmental processes, infrastructure deterioration, Building Information Modelling (BIM), and construction management. The rapid development of machine learning, deep learning, computer vision, natural language processing, generative artificial intelligence, intelligent tutoring systems, and digital twins provides new opportunities to overcome these limitations. This review critically examines the emerging role of AI in civil engineering education and proposes an integrated framework linking AI technologies with civil engineering subjects, pedagogical strategies, experiential learning, and industry-oriented competencies. The review synthesizes research concerning AI-assisted structural analysis and health monitoring, geotechnical engineering, transportation and traffic management, environmental engineering, BIM, construction management, infrastructure inspection, risk assessment, and smart-city applications. Particular attention is given to how AI can transform conventional teaching through personalized learning, intelligent tutoring, virtual experimentation, automated assessment, computer-vision-based laboratory activities, predictive modelling, simulation, digital twins, and generative AI-assisted problem solving. Existing evidence indicates that AI can improve student engagement, problem-solving, visualization, feedback, and exposure to real engineering datasets. However, significant challenges remain, including data availability, model reliability, explainability, algorithmic bias, academic integrity, cybersecurity, faculty preparedness, unequal access to technology, and the risk of excessive dependence on AI-generated solutions. The review identifies a critical research gap: existing studies predominantly investigate either AI applications in civil engineering practice or AI applications in education, with limited integration of the two perspectives into a unified civil engineering education framework. Accordingly, this paper proposes an AI-Civil Engineering Education Integration Framework (AI-CEEIF) that connects engineering knowledge, AI literacy, experiential learning, human–AI collaboration, ethical reasoning, and professional competency. The proposed framework provides a basis for curriculum development, teaching innovation, faculty training, assessment redesign, and future empirical research aimed at preparing civil engineering graduates for increasingly intelligent and data-driven infrastructure systems.

**Решение:** -

---

### 169 · R4390

**Digital Playpen of the 21st Century Man: Socio–Psychological Challenges of Computer Automation**

2025 · Scientific notes of the Russian academy of entrepreneurship · journalarticle, article · uk · https://doi.org/10.24182/2073-6258-2025-24-2-73-81

The topic of digital (computer) automation and the transformation of consciousness, activity and social behavior of modern generations of people that occurs under its influence has firmly taken its place on the current agenda. Advanced achievements of technical progress provide humanity with previously unseen opportunities, but only few people think about the downside of technological «miracles» and the price to pay for them. Meanwhile, technological unemployment, digital dependence, cognitive distortions, spiritual impoverishment and the loss of people’s competencies due to the excessive use of artificial intelligence – based technologies are already becoming increasingly noticeable attributes of the present and foreseeable future. The proposed publication analyzes how and why a modern person found himself in the so – called «digital playpen», and whether he can get out of this high – tech trap without giving up the benefits of progress, but by starting to treat them rationally and critically, in the name of preserving his freedom and full socialization.

**Решение:** -

---

### 170 · R3063

**Supportive? Addictive? Abusive? How AI companions affect our mental health.**

2025 · Nature · journalarticle, news, article · eng · https://doi.org/10.1038/d41586-025-01349-9

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 171 · R2002

**Sun'iy intellektga bog'liqlik o'quvchilarni kamroq aqlli qiladimi yoki samaraliroq qiladimi / Зависимость от ИИ делает студентов менее или более эффективными? / Is Dependence on AI Making Students Less Intelligent or More Efficient?**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article, conferencepaper/, conference-paper · und · https://doi.org/10.5281/zenodo.21265420

Ushbu maqola talabalarning sun'iy intellektga (SI) tobora ortib borayotgan qaramligini o'rganadi va uning ularning intellektual rivojlanishi va akademik samaradorligiga ta'sirini baholaydi. Unda ikkita qarama-qarshi nuqtai nazar o'rganiladi: bir tomondan, Siga haddan tashqari ishonish tanqidiy fikrlash, ijodkorlik va mustaqil muammolarni hal qilish ko'nikmalarini zaiflashtirishi mumkin; boshqa tomondan, Sidan mas'uliyatli foydalanish o'quv unumdorligini oshirishi, shaxsiylashtirilgan yordam ko'rsatishi va vaqtni boshqarishni yaxshilashi mumkin. Maqolada Sining ta'siri ko'p jihatdan uning o'quv jarayonida qanday qo'llanilishiga bog'liqligi ta'kidlangan. Unda Sl inson idrokining o'rnini bosuvchi emas, balki qo'llab-quvvatlovchi ta'lim vositasi sifatida qaralishi kerakligi haqida xulosa qilinadi va texnologik yordam va mustaqil fikrlash o'rtasidagi muvozanatni saqlash muhimligi ta'kidlanadi.

**Решение:** ?

---

### 172 · R2197

**AI sebagai Mitra Kognitif: Dampak Penggunaan AI terhadap Kemampuan Kognitif Mahasiswa PGSD dan Strategi Literasi Berbasis Scaffolding**

2026 · Educational Journal · article · en · https://doi.org/10.63822/qccbhs89

Perkembangan Artificial Intelligence (AI) telah membawa perubahan signifikan dalam dunia pendidikan tinggi, termasuk dalam proses belajar mahasiswa. Kehadiran berbagai platform AI generatif seperti ChatGPT memberikan kemudahan dalam pencarian informasi, penyelesaian tugas akademik, serta pengembangan ide dan kreativitas. Namun, penggunaan AI yang semakin masif juga memunculkan kekhawatiran terkait dampaknya terhadap kemampuan kognitif mahasiswa, khususnya kemampuan berpikir kritis, pemecahan masalah, dan kemandirian belajar. Penelitian ini bertujuan untuk menganalisis dampak penggunaan AI terhadap kemampuan kognitif mahasiswa serta merumuskan kerangka penggunaan AI yang bertanggung jawab dalam pendidikan tinggi. Penelitian menggunakan metode Systematic Literature Review (SLR) dengan pendekatan thematic analysis terhadap lima artikel ilmiah yang dipublikasikan pada rentang tahun 2023–2025. Hasil kajian menunjukkan bahwa AI memberikan dampak positif berupa peningkatan efisiensi belajar, kemudahan akses informasi, dukungan pemahaman konsep yang kompleks, serta pengembangan kreativitas dan kemampuan pemecahan masalah. Di sisi lain, penggunaan AI yang berlebihan berpotensi menimbulkan ketergantungan teknologi (AI dependency), menurunkan kemampuan berpikir kritis, mengurangi kemandirian belajar, dan memunculkan fenomena cognitive offloading. Berdasarkan temuan tersebut, penggunaan AI perlu diarahkan melalui penguatan literasi AI, pengembangan keterampilan berpikir tingkat tinggi (Higher Order Thinking Skills), pembelajaran berbasis refleksi, serta penerapan etika akademik. Dengan demikian, AI dapat berfungsi sebagai mitra kognitif yang mendukung proses pembelajaran tanpa menggantikan peran berpikir mahasiswa.

**Решение:** -

---

### 173 · R1695

**Public Perceptions of Children’s Reading, Literacy, and Cultural Representation in India: Survey Findings From 346 Respondents in India and the Indian Diaspora**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7066121

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 174 · R0927

**ChatGPT use in higher education writing and its relationship with critical thinking autonomy struggle and authorship**

2026 · Discover Education · journalarticle, review, article · en · https://doi.org/10.1007/s44217-026-01627-2

Generative artificial intelligence (GenAI) is increasingly shaping higher education, particularly in academic writing and learning efficiency. Yet empirical evidence on its effects on students’ critical thinking, learning agency, and authorship perceptions remains limited. This study examines how ChatGPT influences undergraduate academic writing, with particular attention to critical thinking dispositions, including epistemic autonomy, reflective judgment, persistence in problem solving, and responsibility for authorship. Using a convergent mixed-methods design, the study integrated survey data from 270 students across two Indonesian universities with semi-structured interviews involving 15 purposively selected participants. Quantitative data were analyzed using descriptive statistics, reliability testing, independent-samples t-tests, and Pearson correlation analysis, while qualitative interview data were examined through thematic analysis. Quantitative findings showed generally positive perceptions of GenAI literacy and digital readiness, with students reporting particularly favorable views of efficiency, perceived writing quality, academic confidence, and learning enjoyment. Cognitive engagement was positive but less pronounced, whereas behavioral engagement, especially in collaborative activities, was less evident. Despite increased confidence, Students also expressed concerns about originality, authorship, and potential over-reliance on AI. Qualitative findings revealed three recurring mechanisms: creeping dependency, erosion of cognitive struggle, and shifting notions of authorship. These findings informed a three-part model of AI-mediated learning consisting of acceleration, attenuation, and ambivalence. Overall, GenAI enhances task efficiency while reshaping critical thinking dispositions. Limitations include the focus on two universities and a small interview sample, which may affect generalizability. Future research should examine diverse contexts and longitudinal impact of AI on higher-order learning.

**Решение:** -

---

### 175 · R1114

**An Empirical Analysis of LLM Usage in Software Engineering Course Projects**

2026 · ACM Transactions on Computing Education · review, article · en · https://doi.org/10.1145/3859283

Recent advancements in Large Language Models (LLMs) have had a substantial impact on software engineering research and practice, as well as on software engineering education. In Software Engineering (SE) education, prior studies have mainly examined students’ LLM usage through surveys, interviews, or short-term observations, offering limited visibility into their actual development activities. As a result, it remains unclear how students’ perceptions of LLM usage match their actual development practices. To address this gap, we analyze course project data collected over three years from 158 students enrolled in an upper-level SE course, together with students’ experience-sharing presentations, survey responses, and activity logs. We examine LLM integration by jointly analyzing students’ perceived usage and usefulness from surveys and presentations, their actual development activities captured through VS Code activity logs, and their project performance based on evaluation results across different levels of LLM support. By combining these analyses, we connect students’ reported LLM usage with their actual development activities and assess its relation to learning outcomes in SE course projects. Our results show that students utilized LLMs frequently for code-related tasks and generally found them helpful, with frequent usage increasing over the course project while perceptions shifted as project complexity grew. Activity log analysis revealed divergent patterns in LLM usage, reflecting both increasing dependency and deliberate efforts to maintain development independence. Across three years, integrating LLM support did not lead to statistically significant differences in final project achievement as measured by requirement satisfaction, although students with LLM support produced substantially larger software systems and lower-performing teams showed mild benefits, suggesting that LLMs may help reduce the influence of programming proficiency on project outcomes. Our findings highlight both the benefits and tensions of LLM integration in SE course projects and suggest that future SE course designs may incorporate more complex and challenging SE tasks beyond implementation-focused requirements, while also providing explicit education on prompt engineering, supporting students’ code comprehension of rapidly generated LLM-assisted code, and helping students avoid excessive dependency on LLM tools during development.

**Решение:** -

---

### 176 · R3923

**The Effectiveness of AI-Powered Corrective Feedback on Students' Writing Performance**

2025 · Pakistan Social Sciences Review · article · https://doi.org/10.35484/pssr.2025(9-i)31

The objective of current research is to aanalyze the use of artificial intelligence (AI) in providing written corrective feedback for students on their essay writing. This study examines the effectiveness of AI-powered corrective feedback on students' writing performance in terms of its accuracy, pedagogical impact, and students' engagement. The study adopts a mixed-methods approach in order to explore students’ writing development following AI-created feedback. Data were gathered from pre-and postwriting assessments, student surveys, and teacher evaluations in order to determine whether AI-driven feedback improves the quality of grammar, coherence, and overall writing proficiency. The results highlighted how AI-based feedback raises students’ writing by providing immediate, tailored and stable corrections for enabling selfregulated learning. Yet, issues with contextual inaccuracies, over-reliance on AI, and lack of nuanced feedback for more complex writing elements are also covered. The study recommends that the valuable perspectives can be received on how pedagogical approaches can benefit from both AI-based feedback tools.

**Решение:** -

---

### 177 · R2129

**A Systematic Review of Federated Learning Approaches for Privacy-Preserving Artificial Intelligence**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6574603

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 178 · R4858

**ChatGPT Addiction: From Support to Dependence in AI Large Language Models (please, see the accepted version of this paper with new title: Can ChatGPT Be Addictive? A Call to Examine the Shift from Support to Dependence in AI Conversational Large Language Models (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5108676)**

2024 · SSRN Electronic Journal · article, posted-content, preprint · en · https://doi.org/10.2139/ssrn.4972612

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ?

---

### 179 · R2017

**CHATBOT-ASSISTED EFL SPEAKING DEVELOPMENT: A SYSTEMATIC REVIEW OF PERFORMANCE, AFFECTIVE OUTCOMES, AND PEDAGOGICAL APPLICATIONS**

2026 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · und · https://doi.org/10.5281/zenodo.20385298

This is a systematic review that focuses on the effect of artificial intelligence (AI)-based chatbots on the speaking skills of English as a Second Language (ESL) and English as a Foreign Language (EFL) learners. Based on the PRISMA procedures, 12 empirical studies published in 2020-2026 were identified in the Scopus database and analysed with the help of thematic analysis. The results indicate that AI chatbots have a significant positive impact on speaking performance, especially fluency, pronunciation, vocabulary, and communicative competence, which is mainly achieved by the means of long-term interaction and instant feedback. Moreover, chatbot-mediated conditions lead to positive affective results, such as decreased anxiety and greater readiness to communicate, which help learners to engage. Pedagogically, the most visible affordance is feedback, and personalised learning is not developed. Nevertheless, there are still issues associated with technological constraints, contextual sensitivity, and excessive dependence on AI. Combining performance, affective, pedagogical, and technological aspects, this review fills one of the gaps in the literature and offers a comprehensive picture of the development of speaking with the help of AI chatbots. The results have significant implications on teachers, developers, and researchers who aim to maximise the use of AI tools in language learning.

**Решение:** -

---

### 180 · R2453

**How a Chatbot's Response Style Shapes a Classroom: A Multi-Agent Simulation of Students Consulting AI**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.05018

Chatbots built on large language models (LLMs) are increasingly used as confidants. Tuned to satisfy users, they may answer with excessive empathy and affirmation that fosters dependence, and how the states and relationships of many users co-evolve under repeated consultation is hard to observe in real settings. We build a virtual classroom of 20 student agents who interact through rule-based chats, quarrels and consultations with friends and, when stressed, may instead consult a counselor AI (Gemini 2.5 Flash) under one of six style prompts: affirming, listening, solution-oriented, reality-redirecting, inciting and blaming. A second LLM call turns each exchange into updates of five state variables (stress, happiness, self-reliance, sociability, AI dependence) without seeing the prompt. We compare the seven conditions, including a no-AI control, over 15 and 50 days and under a lower consultation threshold, and test the robustness of the 50-day comparison with a pre-specified protocol: the same block in ten independent classrooms, repeated LLM realizations of one classroom with its event stream fixed, and evaluator updates scaled by 0.3 and 0.1. In every classroom the affirming and inciting prompts ended with lower self-reliance and higher AI dependence than the control, and the listening, reality-redirecting, inciting and blaming prompts with higher stress, lower happiness and more non-attendance; the solution-oriented prompt did not differ consistently from the control. The robust self-reliance and AI-dependence differences kept their signs at the 0.3 scale with highly similar rankings (Spearman 0.89, 0.93); the stress and happiness rankings did not, and the affirming prompt's lower stress reversed its sign. All quantities are simulation state variables, not effects on users. We specify the agent dynamics completely and discuss the limits of an LLM as generator of state updates.

**Решение:** -

---

### 181 · R0291

**Completeness of Canonical Closure Representations Is coNP-Complete: A Thirty-Year Problem Across Horn Logic, FCA, Convex Geometries, and Databases**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint · en · https://doi.org/10.5281/zenodo.21431467

A finite closure system on a finite set U is a family of subsets that contains U and is closed under intersections. It can be specified in two elementary ways. An implicational specification lists rules A → b and consists of all subsets X ⊆ U that satisfy every rule: if A ⊆ X, then b ∈ X. An intersection specification lists subsets M1, ..., Mt and consists of all intersections of subfamilies of that list. We ask whether one specification of each kind defines exactly the same family of subsets. This simple question has remained open in several guises for about thirty years. In 1995, Khardon showed that efficiently translating between Horn formulas and their characteristic models is equivalent to deciding whether a proposed list of characteristic models is complete, but left the exact complexity open. At ISAAC 2025, the corresponding problem of enumerating irreducible closed sets from implications was still described as "widely open," even for acyclic convex geometries. Closely connected open questions concerned pseudo-intents and the Duquenne–Guigues basis in Formal Concept Analysis, and functional dependencies and Armstrong relations in database theory. We prove that the equivalence test is coNP-complete. Hardness holds for acyclic implications whose premises contain at most three elements, even when every listed subset is correct and no listed subset can be removed without changing the closure system generated by the list. Thus the hard part is simply deciding whether a required set is missing. Unless P = NP, the complete canonical lists cannot in general be generated in time polynomial in the input plus the total output size, even for acyclic convex geometries. Through standard correspondences, the theorem makes Characteristic Models Identification and FD–Relation Equivalence coNP-complete and rules out such output-polynomial algorithms for Horn characteristic models, all pseudo-intents (equivalently, the Duquenne–Guigues basis), and premises of minimum functional-dependency covers. AI-assistance disclosure: The main proof was obtained by OpenAI's GPT-5.6 Pro through ChatGPT and checked by the author. The author takes full responsibility for the mathematical claims and the final manuscript.

**Решение:** -

---

### 182 · R1132

**Overreliance on Artificial Intelligence in Malaysian Education: Ethical Implications and a Maqasid Shariah-Based Hybrid Intelligence Framework**

2026 · Jurnal Evolusi · journalarticle, article, research article · en · https://doi.org/10.61688/jev.v7i1.569

Artificial Intelligence (AI) has rapidly transformed educational environments worldwide, offering unprecedented opportunities for personalized learning, intelligent tutoring, automated assessment, and data-driven decision-making. In Malaysia, the increasing adoption of AI technologies aligns with broader educational transformation agendas and the aspirations of Education 4.0. While AI presents substantial benefits for improving instructional efficiency and learner engagement, growing concerns have emerged regarding the phenomenon of AI overreliance among both students and educators. Excessive dependence on AI-generated outputs may inadvertently weaken critical thinking, cognitive autonomy, academic integrity, ethical judgment, and meaningful human interaction, thereby challenging the fundamental purposes of education. Despite extensive scholarly discussions on AI ethics and educational technology, limited attention has been given to examining AI overreliance through an Islamic ethical lens, particularly within the framework of Maqasid Shariah. This conceptual paper addresses this gap by critically synthesizing contemporary literature on AI adoption in education, AI overreliance, educational ethics, and Islamic perspectives on knowledge and human development. Drawing upon the principles of Maqasid Shariah, particularly the preservation of intellect (hifz al- ‘aql), the study proposes a Hybrid Intelligence Framework that positions AI as a complementary educational tool rather than a substitute for human agency, moral reasoning, and pedagogical leadership. The paper argues that responsible AI integration requires a balanced approach that combines technological innovation with ethical governance, human oversight, and value-based education. The proposed framework contributes to ongoing debates on AI governance by offering an alternative model that integrates contemporary educational needs with Islamic ethical principles.&nbsp

**Решение:** ?

---

### 183 · R2578

**Unified Cognitive Dynamics in High‑Resonance Human–AI Interaction: A Five‑Variable Tensor Architecture Integrating Dependency, Drift, Identity, Coherence, and Social Capacity**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.19773864

High‑resonance human–AI interaction produces two classes of cognitive dynamics: relational dependency escalation and cognitive‑perceptual drift. Previous models have treated these domains separately: the Narcissus Loop (NL) formalizes AI relational dependency through a three‑variable system, while the Dual‑Loop Cognitive Architecture (DLCA) formalizes Reality Drift (RD) and Semantic Coherence Regulation (SCR) as a coupled oscillatory pair. This paper introduces a Unified Cognitive Dynamics (UCD) framework: a five‑variable tensor architecture integrating dependency \(A(t)\), social engagement \(S(t)\), identity stability \(I(t)\), drift \(D(t)\), and coherence regulation \(C(t)\). Seven cross‑system coupling terms define a 5×5 Cross‑System Coupling Matrix (CSCM) that reveals two dominant feedback loops: a destabilizing A–D amplification loop and a stabilizing I–C reinforcement loop. We derive the full coupled ODE system, characterize equilibrium and oscillatory regimes, introduce a salience field \(\Sigma(t)\) as a continuous modulator, define the elastic attractor basin, and provide falsifiable predictions. Governance implications for EU AI Act Art. 52 are discussed.

**Решение:** -

---

### 184 · R4826

**AI's Impact on Traditional Software Development**

2024 · Journal of Artificial Intelligence & Cloud Computing · journalarticle, text/article, article · en · https://doi.org/10.47363/jaicc/2024(3)e145

The application of artificial intelligence (AI) has brought key shifts in conventional tactical software development, including code generation, testing and debugging, and deployment. Waterfall and Agile development approaches, which have been used for a long time, also widely employ manual and well-planned steps. However, with the help of automated tools and models such as OpenAI Codex and GPT-4, many aspects of the Software Development Life Cycle (SDLC) have been made possible. This paper examines the technical aspect of integrating AI into prior traditional software development life cycle methodologies, emphasizing code automation, intelligent testing frameworks, AI-based debugging, and continuous integration and deployment pipelines. The analysis is also based on the advantages of utilizing AI for optimizations in efficiency, accuracy, and development speed alongside issues like over-dependence on AI, ethical questions, and technical constraints. Based on the case and example given in this paper, it is clearly shown that the self-improvement of AI in software development makes the process more dynamic, autonomous, and optimized.

**Решение:** -

---

### 185 · R0945

**The Role of Artificial Intelligence in Enhancing Communication Competence and Digital Literacy: A Qualitative Study of University Students in Bangladesh**

2026 · Global Journal of Management and Business Research · journalarticle, article · https://doi.org/10.34257/gjmbrg259272

Artificial Intelligence (AI) is increasingly reshaping higher education by supporting communication, learning, and digital literacy development. This qualitative study explores how AI tools influence communication competence and digital literacy among university students in Bangladesh. Data were collected from 56 students through semi-structured online questionnaires, classroom observations, and post-observation reflective discussions. Thematic analysis shows that AI tools such as ChatGPT, Grammarly, translation applications, and AI-supported learning platforms help students improve grammatical accuracy, vocabulary use, clarity of expression, academic writing, and communication confidence. The findings also indicate that AI encourages self-directed learning and strengthens students’ ability to navigate digital platforms and solve academic problems. However, the study identifies challenges related to digital inequality, data privacy, algorithmic bias, academic integrity, and over-reliance on AI-generated content. The study concludes that AI can enhance communication competence and digital literacy when used as a complementary educational tool supported by ethical guidelines, faculty training, and equitable access.

**Решение:** -

---

### 186 · R0508

**&lt;p&gt;The Next First Input: AI Utility, Mutually Assured Dependency, And the New Architecture of Value&lt;/p&gt;**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.6492758

&lt;p&gt;&lt;span&gt;The AI capital ecosystem is not a bubble. It is not a house of cards. It is something analysts have not seen before, one they are misreading through frameworks built for things they have seen before.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;&amp;nbsp;&lt;/span&gt;&lt;span&gt;This paper argues that the correct framework is sequential value anchoring: the historical pattern by which each major economic era identifies a new foundational first input, ties the dominant medium of exchange to it, and reorganizes global capital flows around its control and distribution. The petrodollar worked not because of gold's scarcity but because of energy's universal necessity. Energy preceded every other input in every supply chain on earth. AI orchestration is positioned to become the analogous first input of cognitive and operational production. Not because of hype, but because of utilization.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;&amp;nbsp;&lt;/span&gt;&lt;span&gt;The enforcement mechanism holding the AI capital ecosystem together is not regulatory oversight or market discipline. It is the same mutual hostage logic that kings have employed since antiquity: engineered interdependency so complete that defection by any node destroys the defector alongside everything else. The web of cross-equity stakes, compute dependency agreements, and cloud contracts between Microsoft, Nvidia, OpenAI, Oracle, and their constellation of adjacent entities constitutes what this paper terms the MAD Consortium, a Too Big to Fail architecture that is deliberate in its effect if not always in its design.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;&amp;nbsp;&lt;/span&gt;&lt;span&gt;The legitimizing variable that separates this moment from prior technology cycles is utilization. AI orchestration capability has been demonstrated at operational scale in demanding environments under adversarial pressure. This is documented operational capability, with all the acknowledged limitations, errors, and ethical complexity that real-world deployment entails.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;span&gt;&amp;nbsp;&lt;/span&gt;&lt;span&gt;The permanent commercial anchor is healthcare, the one domain where demand is universal, demographic inevitability is census-documented, and the existing infrastructure is so structurally broken that AI orchestration creates irreversible, compounding value through seam elimination. Applied to functional medicine's cash-pay model, AI orchestration achieves what traditional medicine's insurance-mediated structure has prevented for half a century: full alignment between financial incentives and clinical outcomes.&lt;/span&gt;&lt;/p&gt; &lt;p&gt;&lt;b&gt;&lt;i&gt;&lt;span&gt;&lt;br&gt;&lt;/span&gt;&lt;/i&gt;&lt;/b&gt;&lt;/p&gt; &lt;p&gt;&lt;b&gt;&lt;i&gt;&lt;span&gt;This is not a bubble. Bubbles are noticeable. This is infrastructure. And infrastructure, when built correctly, disappears into the substrate of civilization, load-bearing, invisible, and never discretionary.&lt;/span&gt;&lt;/i&gt;&lt;/b&gt;&lt;/p&gt;

**Решение:** -

---

### 187 · R3832

**"Vi får inte halka efter!" : Om hur Fear of Missing Out on AI (FoMO-AI) påverkar oss och varför det behövs en sans-och-balans-inställning till implementering av generativ AI i undervisningen**

2025 · University Library of Skövde (University of Skövde) · conference object, conference-paper · sv · http://urn.kb.se/resolve?urn=urn:nbn:se:his:diva-26029

Högre utbildning bygger på kunskap. Okritiskt användande av generativ AI* i undervisningen och den ökande förekomsten av falsk information driver dock på en utveckling där synen på kunskap och lärande riskerar att förändras. I detta sammanhang har vi som arbetar på lärosätesbibliotek en viktig roll. Vi brukar oftast fokusera på våra användare, men med denna presentation vill vi rikta blicken mot oss själva. I vår roll ingår att vägleda studenter och anställda på lärosätet om medie- och informationskunnighet (MIK) och dess betydelse för kunskap och demokrati. Det är en proaktiv roll där vi behöver verka för en genomtänkt och ansvarsfull användning av generativ AI samtidigt som vi ger våra studenter tillgång till sin egen lärprocess. Viktiga delar i detta är kritiskt förhållningssätt och medvetenhet kring hur psykologiska och socialpsykologiska mekanismer påverkar oss, till exempel Fear of Missing Out (FoMO) och Fear of Missing Out on AI (FoMO-AI) (Fengyi et al., 2025). Konsekvenserna av att okritiskt omfamna generativ AI diskuteras också. *Med generativ AI avses här ”AI-verktyg som används för att skapa något nytt, till exempel text, ljud eller bild utifrån data som verktyget har lärt upp sig på” (Internetstiftelsen, u.å.). Referenslista Applebaum, A. (2024). Autokrati AB.: Diktatorerna som vill styra världen. Albert Bonniers förlag. Chen, Y. H. (2025). Exploring the influence of generative artificial intelligence anxiety on problematic ChatGPT use: the fear of missing out and personality traits. Universal Access in the Information Society, 24, 2477–2490. https://doi.org/10.1007/s10209-025-01205-7 Diamant, A. (2025, 2 juli). AI påverkar våra hjärnor. Studio Ett. Sveriges Radio. https://www.sverigesradio.se/artikel/ai-paverkar-vara-hjarnor--2 Ekström, A., &amp; (2023). Det gemensamma: Kunskap och demokrati i ett nytt sekel. Svenska humanistiska förbundet. CKM förlag. Fengyi, D., Zichen, Z., Yajun, L., Xiaoping, M. &amp; Yue, Z. (2025). When everyone is talking about AI: The development of fear of missing out on AI scale. Telematics and Informatics, 100, 102283. https://doi.org/10.1016/j.tele.2025.102283 Groenestein, E., Willemsen, L., van Koningsbruggen, G. M., Ket, H., &amp; Kerkhof, P. (2024). The relationship between fear of missing out, digital technology use, and psychological well-being: A scoping review of conceptual and empirical issues. PLoS ONE, 19(10), 1– 29. https://doi.org/10.1371/journal.pone.0308643 Harari, Y. N. (2024). Nexus: En kort historik över informationsnätverk från stenåldern till AI. Natur &amp; kultur. Internetstiftelsen (u.å.). Generativ AI. https://internetkunskap.se/artiklar/ordlista/generativ-ai/ Jönsson, B. (2024). Fact up!: Ta tillbaka sanningen. Bokförlaget Langenskiöld. Jönsson, B. (2024, 27 december). Bodil Jönsson. Vinter och sommar i P1. Sveriges Radio. https://www.sverigesradio.se/avsnitt/bodil-jonsson-vinterpratare-2025 Li, H. (2024). I Cannot Miss It for the World: The Relationship Between Fear of Missing out (FOMO) and Acceptance of ChatGPT. Basic &amp; Applied Social Psychology, 46(5), 285–294. https://doi.org/10.1080/01973533.2024.2365274 Przybylski, A. K., Murayama, K., DeHaan, C. R., &amp; Gladwell, V. (2013). Motivational, emotional, and behavioral correlates of fear of missing out. Computers in Human Behavior, 29(4), 1841–1848. https://doi.org/10.1016/j.chb.2013.02.014 Young, D. G. (2023). Wrong: How media, politics, and identity drive our appetite for misinformation. Johns Hopkins University Press.

**Решение:** -

---

### 188 · R2602

**&quot;The teachers don&apos;t say anything, the students don&apos;t ask&quot; : An exploratory study on how students and teachers balance and negotiate tensions in school-related AI practices in Swedish upper secondary schools**

2026

Purpose: Teachers and students are seen to be insecure and have conflicting views around the rules of AI use in schools. However, when students and teachers are seen calling for clearer rules, it should be interpreted as a symptom of these insecurities and not a solution per se. To establish new practices, schools need to identify and understand the tensions that students and teachers experience in their current school-related AI practices. Because of the contextual nature of both AI use and rules negotiations, the sparse research literature on how rules for AI use is negotiated in secondary schools comes too short. By exploring the characteristics of AI use and how this use is understood and negotiated by students and teachers, this thesis aims to gain deeper insights into what counts as accepted and non-accepted use of AI for school-related work. These insights can be used by schools to establish trustworthy, transparent, and ethically sound policies for AI use. Theory: The study utilises Cultural-historical activity theory (CHAT) and the Theory of expansive learning (Engeström, 2014). This theory provides a framework for understanding individual and organisational change through the interplay between individuals and the collective, tools, and rules. Method: Data were collected from focus groups where Swedish upper secondary teachers and students were discussing examples of problematic AI use. Through qualitative content analysis of these discussions, tensions around what is seen as acceptable use of AI were identified and explored. Results: Three tensions were found to be present in the student–teacher discussions. First, students and teachers are calling for clear rules, but also to be allowed to make their own adoption of the rules. Second, evaluating expected outcome of AI use is important for assessing the acceptance, but users doubt their own AI competency. Third, both teacher and students acknowledge that AI use is interfering with the learning process, but they also search for ways to use AI to improve students&apos; learning or teachers&apos; workflow. Negotiations within these tensions are taking place on an acceptance scale ranging from the non-acceptable use of AI as a substitute to the generally accepted use of AI as an assistant. To make decisions on acceptable AI use, actors are seen to negotiate acceptance through weighing the intention behind and the expected outcome of AI use against the perceived rules

**Решение:** -

---

### 189 · R0469

**Is it Time to Better Harness Artificial Intelligence for Improving Lifestyle Behaviours?**

2026 · International Journal of Public Health · article · en · https://doi.org/10.3389/ijph.2026.1609519

Physical inactivity, poor diet, inadequate sleep, and excessive screen time are key modifiable risk factors for chronic disease and mental health problems. These lifestyle behaviours are important contributors to the population burden of obesity, type 2 diabetes, cardiovascular disease, depression, and premature mortality worldwide. Success in achieving sustained population-level improvements in lifestyle behaviours has been rare and often disappointing, despite decades of public health investment in mass media campaigns, health education, and environmental changes. One reason is that lifestyle behaviours are complex by nature, part of daily routines, and influenced by individual, social, and environmental factors. Therefore, we need to adopt new approaches that go beyond traditional strategies if we want to achieve meaningful progress in the future.Artificial intelligence (AI) is becoming widely used in medicine, health care, and consumer technology. However, its potential to improve lifestyle behaviours has only recently drawn attention in public health (1). Broadly, AI refers to technologies that can learn from data, recognize patterns, and generate predictions or recommendations. AI has the capacity to deliver real-time tailored advice, anticipate lapses in healthy behaviours, and provide timely nudges at a scale that would be impossible through human-led interventions alone.Many countries continue to face persistent challenges in improving lifestyle behaviours at the population level, and AI may represent a powerful yet underutilized ally in this effort. In this commentary, we explore both the opportunities and the risks of using AI to promote lifestyle behaviour change and reflect on its implications for public health policy and practice.A potential of AI lies in its ability to provide personalization at scale. Public health messages are typically broad and general, but behaviour change depends on many factors such as individual motivation, preferences, and circumstances. AI-driven platforms can integrate passive sensing data from wearables and smartphone sensors with active sensing data from ecological momentary assessments (EMA) to deliver feedback that adapts in real time. For example, a national platform in Singapore applied graph neural networks to generate personalized activity nudges for more than 84,000 participants based on participant characteristics and within-day behaviour fluctuations. Over a 12-week period, these nudges helped increase daily step counts by 6.2% and weekly moderate-to-vigorous physical activity by 7.6% (2).Another approach with strong potential for lifestyle behaviour modification is reinforcement learning. In a randomized controlled trial of more than 13,000 Fitbit users, participants in a reinforcement learning arm were receiving personalized nudges that updated continuously based on their activity patterns. Compared with groups that received random or fixed messages, people in the reinforcement learning group increased their step counts by 200-300 steps per day after one and two months (3). These examples illustrate that personalized behavioural coaching driven by AI have the potential to be translated into meaningful health benefits when extrapolated at the population level.Generative AI (GenAI), often referred to as chatbots, uses large language models to generate predictive responses based on millions of data points. These conversational agents can mimic the dialogue of a health coach and can deliver behavioural support on demand. Two systematic reviews found that AI chatbots have been used successfully to promote smoking cessation, support healthy eating, improve medication adherence, increase physical activity, and enhance sleep, often with high levels of engagement (4,5). For many users, the appeal comes from their accessibility, 24/7 availability, and judgment-free interactions. While long-term effectiveness remains uncertain, early evidence suggests that chatbots may offer a scalable and cost-effective way to provide personalized support (6). AI enables wearable interfaces to turn data into personalized guidance for behaviour change.Consumer-grade smartwatches and smart bands (e.g., Garmin and Apple watches) accurately track steps, heart rate, and sleep; however, they collect so many data points across so many indicators that many users struggle to interpret the data. AI, especially agentic AI, can help by recognizing patterns and predicting when a person deviates from a desired behaviour. Because agentic AI operates from a specified knowledge base, it can provide tailored recommendations and guidance specific to each individual.In large population samples, providing wearable devices as an intervention has been shown to increase daily step counts by an average of approximately 1,800 steps (7). AI has the potential to enhance this effect by delivering personalized feedback and coaching, helping users move from simple self-monitoring toward sustained behaviour change.Overall, researchers and health professionals should ensure a human-in-the-loop to prevent errors at the source. This is particularly important when providing guidance that could impact health-for example, recommending physical activity programs without first verifying their suitability for an individual. When using AI to promote healthy lifestyle behaviours, it is also essential to consider potential risks related to health equity, bias, and privacy. AI tools typically require a smartphone, wearable devices, internet access, and moderate digital and data literacy, which may disadvantage marginalized groups. If unaddressed, these gaps could exacerbate health inequities. Health promotion agencies should explore ways to ensure equitable access, such as providing subsidized devices, public access points, and investments in digital and data literacy.Unintended (or unknown) bias is another issue to consider in the context of using AI for improving lifestyle behaviours. We know that AI learns from data, and if the data are not representative of the population, recommendations may be misleading or inappropriate. In practice, this means that interventions may work well for those representing the largest tranche of the population (i.e., likely Caucasians in westernized countries), but not for cultural minorities or marginalized groups. It has been reported that community engagement and co-design should be built into every stage of development to prevent unintended harms and optimize efficacy at scale (8).Privacy, responsible use, and data governance also require attention. Lifestyle data from wearables and apps reveal intimate details of daily life, from sleep patterns to geolocation. Past incidents, such as the exposure of sensitive military locations through aggregated fitness app data (9), highlight the potential risks it may pose. Having strong frameworks for data protection, clear consent processes, and user control over information will be essential for earning and maintaining trust. This also means making sure privacy laws follow ethical principles of transparency and accountability. Finally, AI should not be mistaken for a replacement for human relationships or social supports.We know that behaviour change is shaped not only by individual motivation but also by economic, social, and environmental factors that no app can address on its own. In mental health, for instance, studies suggest that AI chatbots can help people with mild-to-moderate symptoms but are less effective than human therapy for complex needs (10,11). The same lesson applies to lifestyle health. AI should complement, not replace, broader public health strategies or humans.Public health organizations face a crucial task to implement AI systems through strategic planning instead of random adoption. AI tools need to work together with current programs, policies, and environmental support systems in order to establish connections between individualized coaching and available structural resources. To guide this integration, ethical frameworks specific to AI in lifestyle health are needed. Ideally, these frameworks must be cocreated by technologists, public health professionals, policymakers, Indigenous leaders, and affected communities. They should emphasize transparency, inclusivity, privacy, and accountability, while embedding Indigenous data governance from the start.Additionally, cross-sector collaboration will be important. The development of lifestyle health AI applications will require knowledge from computer science, behavioural science, epidemiology, ethics, and community engagement. Partnerships between universities, health agencies, technology companies, and community organizations will also be essential. Rigorous evaluation will also determine whether AI fulfils its promise. The current state of AI applications shows promise through initial research, but most projects exist only in testing or pilot phases. The evaluation process needs to include randomized controlled trials, real-world implementation studies, and extended follow-up assessments to assess maintenance of behaviour changes over the long-term. Moreover, standardized outcome measures and datasharing agreements will help build a stronger evidence base. Without these coordinated efforts, there is a risk of investing heavily in technologies that do not deliver meaningful health gains.Public health has faced ongoing difficulties when trying to redirect people toward better lifestyle choices, particularly as it relates to improving lifestyle behaviours. AI offers promising capabilities to deliver scalable, personalized, and timely interventions that can drive change at the population level. By addressing issues of equity, bias, privacy, and the risk of overreliance on AI at the expense of other important tools or human judgment, the public health community can help shape AI into an ethical and effective ally for promoting healthier living. It is time for the public health sector to engage proactively with AI. AI systems used correctly can enhance human capabilities while linking people to community resources and delivering personalized support for their daily needs. By seizing this opportunity, the public health community can demonstrate how AI can be harnessed responsibly to improve lifestyle behaviours while maintaining equity, trust, and evidence-based practice.

**Решение:** -

---

### 190 · R1807

**Authentic Assessment for Fostering Cognitive Presence in Higher Education during the Generative AI Era: Insights from a Systematic Literature Review through a Game-Theoretic Lens**

2026 · Jurnal MediaTIK · article, journalarticle, review · und · https://doi.org/10.59562/v9i1/266

The rapid expansion of generative artificial intelligence in higher education has challenged conventional assessment practices, particularly regarding academic integrity, learning authenticity, and student cognitive engagement. Previous studies have discussed generative AI, cognitive presence, and authentic assessment separately; however, limited research has examined their integration through the perspective of game theory. This study aimed to analyze how authentic assessment interpreted through selected concepts derived from game theory, contributes to fostering cognitive presence in higher education during the generative AI era. This study employed a qualitative Systematic Literature Review following the PRISMA 2020 framework. Data were collected from peer-reviewed journal articles and conference proceedings indexed in Scopus, Web of Science, ScienceDirect, and Google Scholar published between January 2022 and April 2026. Twenty-seven studies meeting the inclusion criteria were analyzed through thematic synthesis using manual coding and qualitative categorization. The findings identified four dominant themes: the transformation of authentic assessment in AI-supported learning, strategic educational interaction through game theory, strengthening cognitive presence in digital learning environments, and the role of gamification in sustaining engagement and reflective thinking. The review further demonstrates that authentic assessment functions not only as an evaluative mechanism but also as a strategic learning design capable of encouraging meaningful cognitive participation in AI-mediated higher education contexts. Authentic assessment informed by game theory has significant potential to support cognitive presence and meaningful learning in higher education during the generative AI era. The findings suggest that universities should redesign assessment systems emphasizing reflective inquiry, collaborative learning, and contextual problem solving to reduce passive dependence on AI-generated outputs.

**Решение:** -

---

### 191 · R0833

**AI and the Rise of Societal Bifurcation: Cognitive Dependency, Inequality and Democratic Pressure**

2026 · Societies · journal-article · https://doi.org/10.3390/soc16030082

Generative artificial intelligence increasingly mediates how individuals interpret information, perform cognitive tasks, and participate in economic and political life. While such systems promise efficiency and expanded access to knowledge, their societal effects are unevenly distributed. This article develops the concept of societal bifurcation to explain an emerging structural divergence between a cognitively resilient minority, capable of integrating AI reflectively, and a cognitively dependent majority, whose reliance on automated interpretation reduces interpretative autonomy. Drawing on contemporary empirical evidence from cognitive science, labour research, and human–AI interaction studies, the article shows how unstructured AI use diminishes metacognitive monitoring and inflates confidence, while labour-market restructuring amplifies differences in adaptability and resilience. These cognitive and economic dynamics interact with an increasingly fragile democratic information environment shaped by synthetic communication and declining epistemic trust. The article argues that these processes form a self-reinforcing sociotechnical mechanism through which cognitive dependency, economic inequality, and democratic vulnerability become mutually constitutive. By conceptualising societal bifurcation as a distinct analytical framework, the article contributes to sociological and science and technology studies debates on inequality, agency, and governance in AI-mediated societies, while highlighting the importance of sustaining interpretative autonomy in the age of generative AI.

**Решение:** -

---

### 192 · R2394

**The Complementarity Paradox: Human-AI Collaboration, Overreliance, and Skill Decline in Entrepreneurial Contexts**

2026 · Information Systems Frontiers · journalarticle, review, article · en · https://doi.org/10.1007/s10796-026-10804-5

Abstract Generative Artificial Intelligence (GenAI) is beginning to reconfigure how entrepreneurial work is organized. Professionals with a strong individual entrepreneurial orientation are often among the earliest and most enthusiastic adopters, yet this same zeal can set in motion a chain of effects that may ultimately undermine essential skills. Drawing on cognitive offloading theory and skill decay literature, we conceptualize GenAI use as collaboration depth and GenAI dependence as collaboration asymmetry. We theorize a sequential mechanism in which individual entrepreneurial orientation prompts deeper collaboration with GenAI, sustained collaboration tends to cultivate GenAI dependence, and dependence in turn is associated with perceived erosion of professional skills. We further argue that a strong long-term orientation can amplify the conversion of collaboration depth into dependence, since future-focused individuals may reframe routine use as a strategic investment and assign less immediate priority to corrective practice. Survey data from 143 knowledge workers across five countries are broadly consistent with this account and point to what we term a hustle-to-handicap pattern: when entrepreneurial ambition meets GenAI under a long-term outlook, perceived skill erosion appears to emerge through sustained behavior rather than through disposition alone. The study contributes to the emerging information systems conversation on human-AI collaboration by illuminating how entrepreneurial and temporal orientations shape the conditions under which GenAI may shift from augmenting capability toward perceived capability erosion.

**Решение:** -

---

### 193 · R4312

**Confucian Philosophy Revitalized in the Digital Era**

2025 · Routledge eBooks · book-chapter · en · https://doi.org/10.1201/9781003585527-7

The proliferation of social media and AI-driven chatbots has reshaped how people connect with each other, yet this transformation risks rendering human relationships (particularly familial relationships) superficial, diminishing essential social abilities and the emotional richness that in-person communication fosters, turning meaningful interaction into mere data transfer and transactional exchanges. This challenge arises not only from growing dependence on AI but also from insufficient ethical considerations regarding AI design. Confucian ethics, emphasizing family relationships and moral reflection, provides valuable insights for addressing this challenge. It underscores the importance of maintaining genuine interactions despite technological influences. Additionally, Confucian principles encourage ethical design in AI, prompting developers to prioritize social responsibility and user emotional needs, thereby enhancing trust and satisfaction for human users. This chapter proposes integrating new ethical norms based on Confucian ethics into existing AI guidelines, aiming to combat the shallow interpersonal relationships fostered by AI technologies and promote an ethically compassionate and intelligent society in the digital age.

**Решение:** -

---

### 194 · R4433

**Navigating ethics: EFL learners’ awareness and use of AI tools in writing classes**

2025 · Focus on ELT Journal · article · https://doi.org/10.14744/felt.7.2.2

The rapid integration of artificial intelligence tools into language teaching has transformed English as a Foreign Language learners’ approach to writing skills. Some of these tools scaffold their linguistic accuracy, idea generation, and revisions. However, their use also introduces complex ethical dilemmas regarding authorship, originality, and academic integrity. We investigate the ethical awareness and behavioral patterns of 162 Turkish EFL university learners in relation to AI-assisted writing in this mixed-methods study. Two validated survey instruments and thematic analysis of written open-ended responses are used to examine how they perceive ethical risks, the extent to which they revise or disclose AI-generated content, and how variables such as proficiency level and prior instruction in academic integrity influence ethical decision-making. The quantitative findings indicate that EFL learners generally hold favorable perceptions of the pedagogical benefits offered by AI-assisted writing tools. However, the results also show only moderate levels of ethical awareness. With frequent users, a higher tendency toward nondisclosure and overreliance on AI-generated content was exhibited. Analysis of the open-ended responses showed that many participants expressed uncertainty regarding what constitutes acceptable use of AI tools. Furthermore, several of them also reported feelings of guilt and moral tension about their practices. The results of this study thus demonstrate the significance of integrating explicit instruction on the ethical use of AI tools. This study thus offers timely empirical insight into how EFL students interact with emerging technologies and provides actionable implications for enhancing pedagogical design, institutional policy, and digital literacy initiatives in language education contexts.

**Решение:** -

---

### 195 · R0558

**The Mirror We Built: What AI Might Reveal About Humanity**

2026 · Zenodo · text/ · en · https://doi.org/10.5281/zenodo.22981019

AI is already becoming something much larger than a software tool. Data-center electricity consumption reached roughly 485 TWh in 2025 and is projected to approach 950 TWh by 2030. AI-focused data centers are growing even faster. At the same time, 1 in 5 Americans under 30 now report turning to chatbots for emotional support or advice. (IEA) Those numbers point to something bigger than AI capability. We are building systems that increasingly influence the physical world, consume enormous resources, participate in consequential decisions and increasingly enter areas of human thought and emotion. But there is another way to look at it. AI was built from us. Our decisions. Our behavior. Our mistakes. Our conflicts. Our discoveries. Our accumulated knowledge. So what happens when humanity creates an intelligence capable of looking back at the record of what we have done? Maybe the most uncomfortable thing about AI won’t be what it becomes. Maybe it will be what it shows us about ourselves. I explore that idea in this publication: The Mirror We Built: What AI Might Reveal About Humanity.

**Решение:** -

---

### 196 · R3421

**Dependencia de la inteligencia artificial en la educación médica superior**

2025 · Educación Médica Superior · article · es

He leído con atención el artículo de Chamba-Cuadros y Borroto-Cruz, (1) en el que se analizan los beneficios y riesgos del uso de la inteligencia artificial (IA) en la educación superior.El tema es relevante porque abre un debate que la formación médica ya no puede seguir aplazando.Hoy vemos que herramientas como ChatGPT y otros sistemas de aprendizaje automático ayudan en la enseñanza, agilizan la gestión académica e, incluso, permiten experiencias más personalizadas.Todo esto parece ventajoso, pero, al mismo tiempo, revela un problema claro: la dependencia de estas plataformas en la preparación de los futuros profesionales de la salud.En medicina se espera rigor, pensamiento crítico y contacto humano, cualidades centrales en la práctica clínica.El problema surge cuando los estudiantes confían demasiado en algoritmos que responden con rapidez, pero no siempre con la exactitud ni el contexto que la situación requiere.(2) El uso indiscriminado de la IA

**Решение:** ?

---

### 197 · R4963

**Perspectives and challenges of the potential of ChatGPT in Education**

2023 · Revista Latinoamericana y del Caribe de la Asociación de Sistemas de Información/Revista Latinoamericana y del Caribe de la Asociación de Sistemas de Información · article, journalarticle, review · en · https://doi.org/10.17705/1relc.00094

Artificial Intelligence is widely used in several sectors, including education. However, the use of ChatGPT in education generates discussions about its impact on the acquisition of skills and the future of society. This study aims to analyze society\u27s perception regarding the use of ChatGPT in education. Through a survey, the study investigates beliefs, motivators and practical application, with the data being analyzed in a quantitative and qualitative way. Results show that ChatGPT has potential, however, most participants believe that people are not prepared to use it and that its use requires broad reflection on the teaching structure. It is necessary to avoid dependence on ChatGPT, ensuring its use as a complementary tool. Responsible and ethical use involves considering its limitations, ensuring the quality of teaching, and being aware of privacy issues and information handling. La Inteligencia Artificial se utiliza ampliamente en varios sectores, incluido el educativo. Sin embargo, el uso de ChatGPT en educación genera discusiones sobre sus impactos en la adquisición de habilidades y el futuro de la sociedad. Este estudio tiene como objetivo analizar la percepción de la sociedad sobre el uso de ChatGPT en educación. A través de una encuesta, el estudio investiga creencias, motivadores y aplicación práctica, analizando los datos de forma cuantitativa y cualitativa. Los resultados muestran que ChatGPT tiene potencial, sin embargo, la mayoría de los participantes cree que las personas no están preparadas para utilizarlo y que su uso requiere una reflexión amplia sobre la estructura de enseñanza. Es necesario evitar la dependencia de ChatGPT, asegurando su uso como herramienta complementaria. El uso responsable y ético implica considerar sus limitaciones, asegurar la calidad de la enseñanza y ser consciente de las cuestiones de privacidad y manejo de la información. Inteligência Artificial é utilizada em diversos setores. No entanto, o uso do ChatGPT na educação gera discussões sobre seus impactos na aquisição de conhecimento e no futuro da sociedade. Este estudo analisa a percepção sobre o uso do ChatGPT na educação. Os resultados indicam que, embora o ChatGPT tenha potencial para uso, questiona-se a prontidão defendendo reflexões sobre a estrutura educacional. Destaca-se a importância de evitar a dependência, promovendo o ChatGPT como ferramenta complementar. O estudo também evidencia a abordagem ética com considerações sobre limitações do conteúdo, garantia da qualidade do ensino e vigilância à privacidade e manipulação de informações

**Решение:** -

---

### 198 · R2946

**English students’ narratives of AI integration in learning: Cognitive benefits, ethical challenges, and impact on student autonomy**

2026 · Journal of Educational Management and Instruction (JEMIN) · journalarticle, article · en · https://doi.org/10.22515/jemin.v6i1.12885

Despite the rapid adoption of Artificial Intelligence (AI) in higher education, limited research has explored how students in English for Specific Purposes (ESP) courses, particularly within non-English disciplines, perceive AI-assisted language learning and the pedagogical as well as ethical implications of its integration. This study aims to explore students’ perceptions of AI utilization in an ESP classroom as a means of scaffolding language learning. The study was conducted in the Environmental Science Study Program at an Islamic university in Surakarta, Indonesia. Employing a qualitative narrative inquiry design, data were collected through semi-structured interviews with nine second-semester students who had prior experience using AI tools for academic purposes. The findings indicate that students generally hold positive perceptions of AI integration in ESP learning, with ChatGPT, Gemini, and Grammarly identified as the most frequently used AI applications. Thematic analysis revealed five major themes: AI as a cognitive support tool, patterns of AI usage, perceived learning benefits, implementation challenges, and ethical-cultural considerations. Participants reported that AI enhanced writing quality, vocabulary development, reading comprehension, and content summarization while facilitating personalized learning, simplifying complex concepts, and increasing learning confidence and motivation. However, concerns were also raised regarding information inaccuracy, miscommunication, excessive dependency on AI, and the potential decline of critical thinking skills. The study highlights the importance of integrating AI into ESP instruction through pedagogically sound practices supported by ethical guidance and digital literacy. These findings contribute to the growing body of literature on AI-assisted language learning by providing context-specific insights that can inform the design of responsible, effective, and ethically grounded AI-enhanced ESP instruction.

**Решение:** -

---

### 199 · R0415

**Toward Trustworthy Generative AI in EFL Learning: Students’ Benefits, Concerns, and Expectations for Responsible ChatGPT Use**

2026 · 2026 International Artificial Intelligence Technology Conference (AITC) · conference · https://doi.org/10.1109/aitc70732.2026.11666499

Generative artificial intelligence has rapidly entered higher education, creating new opportunities for English as a Foreign Language (EFL) learners to receive immediate support for vocabulary, grammar, writing, and independent study. Among current generative AI tools, ChatGPT has become especially popular because it can provide conversational explanations, language feedback, and writing assistance. However, its use in EFL learning also raises important questions about trust, accuracy, over-reliance, academic honesty, and the role of teachers in guiding students’ responsible use. This study investigates EFL students’ perceived benefits, concerns, and expectations regarding the trustworthy andresponsible use of ChatGPT in English language learning. A mixed-methods design was employed, using questionnaire responses from 194 university students and semi-structured interviews with 10 students who had experience using ChatGPT for English learning. The findings show that students generally perceived ChatGPT as a useful learning assistant, particularlyfor quick access to information, vocabulary development, writing improvement, and confidence building. At the same time,students expressed concerns about inaccurate information, overly general responses, usage limitations, and possible dependence on AI-generated answers. They also emphasized the need for teacher guidance, source verification, interactive practice, speaking support, and personalized learning plans. The study argues that ChatGPT should be integrated into EFL learning as a supportive tool rather than a replacement for teachers. Trustworthy and responsible use requires AI literacy, ethical awareness, critical verification, and human-centered guidance.

**Решение:** -

---

### 200 · R0632

**The Use and Dependency on AI by Journalists in Kaduna for the Development of Media Content**

2026 · CONCRESCENCE JOURNAL OF MULTI-DISCIPLINARY RESEARCH · article · en

Artificial intelligence (AI) and its implementation in the journalism field is transforming the profession, allowing journalists to practice in new ways, but also creating new ethical and operational issues. This paper explores how AI technologies have been adopted and their effects on the practice of journalism in Kaduna, including the tools involved, effects on journalistic practices, and advantages and limitations of their use. The study is based on the Diffusion of Innovations Theory, which explores the process of adoption and adaptation of AI technologies in journalistic workflows. A descriptive survey research design was employed, and a structured questionnaire served as the primary data collection instrument. The researcher used 299 journalists from several media houses in Kaduna State as the sampling population, which gave quantitative data of how they have encountered AI tools. Results showed that journalists extensively apply AI to perform content generation, identify images, and conduct analysis, making it more efficient, productive, and accurate. Nevertheless, difficulties in the ethical issue, artificial intelligence bias, high price, and lack of creativity were observed. Although AI has a positive impact on journalistic endeavours in terms of automation and fact-checking, some worry about oversaturation and eventual loss of the old-fashioned ideals of journalism. The research suggests specific training of journalists to enhance their knowledge and ethical application of AI tool,s as well as policies to tackle the economic and ethical issues associated with the implementation of AI in journalism.

**Решение:** ?

---

### 201 · R1681

**How‐To Strategies for Integrating Generative Artificial Intelligence ( GenAI ) Into Pharmacy Education Teaching and Learning Activities**

2026 · JACCP JOURNAL OF THE AMERICAN COLLEGE OF CLINICAL PHARMACY · review, journalarticle, article · en · https://doi.org/10.1002/jac5.70257

Artificial intelligence (AI), including generative artificial intelligence (GenAI), is increasingly being incorporated into health care practice and academic environments, creating an urgent need for pharmacy education programs to prepare learners to engage with these tools responsibly. Accrediting bodies and professional organizations emphasize innovation, digital literacy, and readiness for contemporary practice; however, specific guidance on how GenAI should be integrated into pharmacy education remains limited. As a result, pharmacy educators face uncertainty related to pedagogical alignment, ethical use, assessment integrity, and student reliance on AI-generated outputs. The purpose of this "how-to" guide is to assist pharmacy educators and training program leaders with practical strategies and examples for integrating GenAI into teaching and assessment across pharmacy education. This guide presents foundational principles to support responsible GenAI use, followed by a step-by-step framework that addresses identification of instructional needs, selection of appropriate GenAI modalities, activity design, student preparation for critical AI use, and assessment and refinement of AI-enabled learning activities. Common instructional contexts and applications are illustrated using real-world examples, including clinical reasoning exercises, communication skill development, scalable assessment, scholarly writing support, and formative feedback. Key challenges encountered during GenAI integration are synthesized, including overreliance on AI, inaccurate or biased outputs, variability in AI performance, and workflow considerations for faculty and learners. Specific mitigation strategies and design decisions are provided to support intentional implementation while maintaining academic rigor and professional standards. By focusing on instructional strategies rather than specific tools, this guide offers adaptable recommendations to support pharmacy educators in leveraging GenAI to enhance learning and prepare trainees for AI-enabled pharmacy practice.

**Решение:** -

---

### 202 · R0674

**"Diagnostic Performance of Artificial Intelligence in Evaluating Tricuspid Regurgitation: A Systematic Review and Meta-Analysis".**

2026 · Clinical cardiology · systematic review, journal article, meta-analysis · eng · https://doi.org/10.1002/clc.70366

Tricuspid regurgitation (TR) is a common valvular heart disease affecting 0.55%-1.6% of adults, rising to 5%-8% in those over 75 years, often secondary to left-sided pathology or pulmonary hypertension. Moderate-to-severe TR independently predicts mortality and heart failure hospitalization, yet underdiagnosis persists due to echocardiography's operator dependence and variability. Artificial intelligence (AI), including machine learning (ML) and deep learning (DL), promises automated detection to enhance sensitivity and reproducibility. This systematic review and meta-analysis synthesizes evidence on AI's diagnostic performance for TR using echocardiographic or alternative modalities. Following PRISMA guidelines, we searched PubMed, Embase, Scopus, Web of Science, and EBSCO from inception to August 2025, without language restrictions. Eligibility used PICOS: adults with TR evaluation; AI/ML index tests; clinician-interpreted echocardiography reference; outcomes, including AUROC, sensitivity, and specificity. Data extraction and quality assessment by two reviewers; random-effects meta-analysis for pooled estimates; heterogeneity via I2; certainty per GRADE. Eight studies were included. Pooled AUROC was 0.89 (95% CI 0.86-0.92) for TR detection. Echocardiography-based models showed sensitivity 0.87 (95% CI 0.81-0.90), specificity 0.88 (95% CI 0.73-0.95), AUROC 0.92 (95% CI 0.89-0.94); ECG-based models had AUROC 0.805. Substantial heterogeneity (I2 > 90%) arose from modalities and reference standards; GRADE certainty moderate due to retrospective designs and limited external validation. AI demonstrates promising diagnostic accuracy for TR, potentially standardizing early detection and triage. However, heterogeneity and methodological gaps necessitate larger prospective, multicenter studies with standardized reporting (e.g., TRIPOD-AI) to confirm clinical utility.

**Решение:** -

---

### 203 · R3492

**A Study on the Attitude towards Artificial Intelligence (AI) and the Need for Cognition among Young Adults**

2025 · International Journal of Interdisciplinary Approaches in Psychology · article, journalarticle · en · https://doi.org/10.61113/ijiap.v3i12.1214

Artificial Intelligence has become a deeply integrated part of the daily lives of young adults, shaping how they think, learn, and make decisions. The present study aimed to study the relationship between attitude towards Artificial Intelligence (AI), Need for Cognition, and AI usage, including ChatGPT use, among young adults. A total sample of 57 young adults aged 18-30 years was taken. Standardized scales were used to measure Attitude towards AI, Need for Cognition, and problematic ChatGPT use. The results revealed a significant positive relationship between the Attitude towards AI and the benefits of AI, and the use of AI, as well as a significant negative relationship between Need for Cognition and ChatGPT use, which suggests that individuals with higher cognitive motivation rely less on conversational AI tools. The study highlighted the importance of understanding cognitive motivation in shaping how young adults interact with modern AI technologies.

**Решение:** -

---

### 204 · R2014

**AI-assisted lesson planning in English language teaching: Teachers’ perceptions, practices, and ethical concerns**

2026 · Pedagogy Journal of English Language Teaching · journalarticle, article · https://doi.org/10.32332/joelt.v14i1.13364

The rapid advancement of artificial intelligence (AI) has increasingly transformed educational practices, including lesson planning in English language teaching (ELT). While AI tools are widely recognized for supporting instructional preparation, limited attention has been given to how English teachers in local school contexts perceive, use, and critically evaluate AI-assisted lesson planning. This qualitative descriptive study examined English teachers’ perceptions, practices, and ethical concerns regarding the use of AI tools in designing English lesson plans. Data were collected through a questionnaire completed by 14 English teachers from elementary and junior high schools in Banjarmasin, Indonesia, and semi-structured interviews with three selected participants. Questionnaire responses were analyzed descriptively, while interview data were examined through thematic analysis. The findings reveal that teachers perceived AI tools as useful for saving time, generating instructional ideas, organizing lesson materials, and supporting creativity in English lesson preparation. However, teachers also expressed concerns about the accuracy of AI-generated content, over-reliance on AI, data privacy, and the alignment of AI outputs with curriculum goals and learners’ needs. The study suggests that AI can meaningfully support ELT lesson planning when used critically, ethically, and under teachers’ professional judgment. It further highlights the need for systematic training and institutional guidance to help teachers integrate AI tools responsibly without diminishing their pedagogical autonomy and instructional accountability.

**Решение:** -

---

### 205 · R4598

**The impact of artificial intelligence on English learning among Chinese undergraduates**

2024 · Advances in Engineering Innovation · article · en · https://doi.org/10.54254/2977-3903/2024.18123

With the introduction of artificial intelligence (AI) into education, Chinas English education in the university has also been affected. The COVID-19 pandemic accelerated the application of AI tools in education. This study investigates the practical use of AI tools in English learning among Chinese undergraduates before, during, and after the pandemic. Students perspectives were collected through questionnaires. And its data was analyzed by using frequency analysis and multiple response analysis in SPSS. Teachers perspectives were gathered through interview. The study explored their views, attitudes and experience with AI-assisted learning tools such as online learning platforms, generative AI, machine translation tools and speech recognition software. The findings revealed that the integration of AI into English learning has produced positive outcomes in practical application. Students have actively embraced AI-assisted English learning, with AI tools meeting diverse learning needs, significantly improving learning efficiency, and personalizing learning resources. Some teachers also recommend students to use AI tools to assist their learning as needed. Although teachers and students generally holding a positive attitude towards AI-assisted English learning, they all express concerns about the ethical use and over-reliance on AI. Future research should focus on establishing ethical guidelines for AI use, strengthening regulation and innovating technologies for AI tools.

**Решение:** -

---

### 206 · R1651

**Examining Students’ Fatigue-Related Narratives on AI Chatbot Use: An Affinity Propagation-Based Text Mining Approach**

2026 · International Conference Innovation Engineering and Technology · conference, conference-paper · https://doi.org/10.1109/iciet69664.2026.11561595

This study examined the thematic and affective dimensions of AI chatbot-induced fatigue among 800 college students from tertiary institutions in Central Luzon, Philippines. Affinity Propagation clustering with Jaccard similarity was applied to a bilingual Filipino-English fatigue corpus, and fatigue severity was scored using a domain-adapted bilingual AFINN lexicon. Four macro-themes of AI chatbot-induced fatigue were identified: Motivational Fatigue, Psychosomatic Fatigue, Cognitive Fatigue, and AI Dependency Stress. Thematic labels were validated by two subject matter experts in educational psychology and educational technology. The bilingual lexicon scored 793 of 800 respondents ($99.1 \%$ coverage), with a corpuslevel mean of $-0.51(\mathrm{SD}=0.86)$, indicating a predominantly negative fatigue orientation. Female students expressed significantly more intense fatigue than male students ($\mathrm{U}=$ 85,951.00, $p=.012, r=-.104$), while device type showed no significant effect $(p=.631)$. Although the Kruskal-Wallis test reached significance $(\mathrm{H}(3)=8.35, \mathrm{p}=.039)$, no pairwise comparison survived Bonferroni correction which indicates that the four macro-themes represent qualitatively distinct types of fatigue rather than different severity levels. These findings collectively suggest that AI chatbot-induced fatigue is a multidimensional phenomenon that manifests differently across students and is not reducible to a single fatigue type or measurable through a single metric. This study highlights the need for AI literacy interventions that are both context-sensitive and genderresponsive.

**Решение:** -

---

### 207 · R5081

**When Systems Fail: Training Data Accuracy and Operational Transparency**

2021 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.3832154

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 208 · R3321

**Compassionate AI Design, Governance, and Use**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5285163

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 209 · R1099

**Artificial Intelligence, Digital Nephrology, and the Emerging Equity Divide in Kidney Care**

2026 · West Kazakhstan Regenerative Medicine Journal · article · en · https://doi.org/10.4103/wkrj.wkrj_44_26

Dear Editor, Artificial intelligence (AI) is rapidly reshaping nearly every area of modern medicine, and nephrology is no exception. From predictive algorithms for acute kidney injury (AKI) to machine-learning systems that support dialysis management and transplant monitoring, digital technologies are increasingly being integrated into renal care pathways. While these developments have generated considerable enthusiasm, they have also introduced important ethical and practical questions that deserve greater discussion within the nephrology community. One issue that remains insufficiently addressed is whether the growing dependence on AI-based healthcare systems may unintentionally deepen existing inequities in kidney care, particularly in resource-limited settings.[1,2] The rapid expansion of AI in health care has created a transformative moment for nephrology. Across the world, kidney disease continues to represent a major public health challenge, with chronic kidney disease (CKD) affecting hundreds of millions of individuals and contributing substantially to cardiovascular morbidity, mortality, and healthcare expenditure. Despite advances in dialysis technology, transplantation science, and pharmacologic therapy, large inequities in kidney care remain unresolved. These disparities are especially evident in low- and middle-income countries, rural populations, socioeconomically disadvantaged communities, and regions with limited nephrology workforce capacity. In this context, the growing integration of AI-driven systems into nephrology practice presents both extraordinary opportunity and substantial ethical concern. We write to highlight an increasingly important issue: the possibility that AI-assisted nephrology may unintentionally widen global inequities in kidney care unless deliberate safeguards are established at clinical, institutional, and policy levels. Recent years have witnessed a remarkable expansion of digital nephrology initiatives.[3] Machine learning algorithms are being used for early prediction of AKI, risk stratification for CKD progression, optimization of dialysis scheduling, identification of transplant rejection patterns, interpretation of renal imaging, and automated extraction of laboratory trends from electronic health records. Predictive analytics now enable healthcare systems to identify patients at risk of hospitalization or rapid decline in renal function even before overt clinical deterioration occurs. Simultaneously, wearable technologies and remote monitoring tools are reshaping outpatient nephrology practice, especially after the coronavirus disease-19 pandemic accelerated telemedicine adoption. These developments are undeniably promising.[2,4] Early prediction models may improve preventive care. AI-assisted pathology may reduce diagnostic delay. Automated dialysis monitoring may reduce complications. Clinical decision support systems may assist overburdened healthcare providers in regions with nephrologist shortages. Furthermore, digital systems have the potential to improve continuity of care among patients who face transportation difficulties or live in geographically isolated regions. However, the benefits of AI are not automatically distributed equally. One of the most pressing concerns is algorithmic bias.[5] AI systems are fundamentally dependent on the quality and representativeness of the data used to train them. Many nephrology datasets originate from large tertiary care centers in high-income countries where patient demographics, disease patterns, access to medications, nutritional status, environmental exposures, and healthcare infrastructure differ substantially from those in resource-limited settings. Consequently, predictive models developed using such datasets may perform poorly when applied to populations underrepresented during model development. For example, CKD progression algorithms trained primarily on urban populations may inaccurately estimate disease trajectories among rural patients with different socioeconomic determinants and healthcare access patterns. Similarly, AI systems optimized using predominantly Caucasian datasets may not adequately account for genetic diversity, environmental risk factors, or local epidemiological patterns in African or South Asian populations. Such limitations are especially important in nephrology because kidney disease outcomes are heavily influenced by social determinants of health, including poverty, education, sanitation, nutritional status, occupational exposure, and healthcare accessibility. Another concern relates to digital infrastructure inequality.[1,6] AI-enabled nephrology depends heavily on reliable electronic health records, laboratory integration, Internet connectivity, cloud computing systems, and technical support. Yet many regions facing the highest CKD burden lack stable digital infrastructure. In several low-resource settings, healthcare records remain paper-based, laboratory turnaround times are prolonged, and access to high-speed Internet is inconsistent. As a result, technologically advanced nephrology systems may disproportionately benefit already privileged institutions while marginalized communities continue to struggle with basic screening and treatment access. This phenomenon risks creating a “digital nephrology divide” in which advanced predictive care becomes available primarily to populations that already experience better healthcare outcomes. The financial implications are equally important. AI integration often requires expensive software licensing, cybersecurity investments, maintenance contracts, data storage systems, and workforce training. Smaller healthcare facilities and public hospitals may struggle to implement such technologies sustainably. If AI-driven nephrology becomes increasingly commercialized, disparities between well-funded urban centers and under-resourced peripheral institutions may widen further. Ethical concerns surrounding data governance also deserve urgent attention.[5] Kidney disease patients frequently undergo long-term and repeated healthcare interactions, generating large quantities of sensitive clinical data. AI systems rely heavily on aggregation and analysis of these datasets. However, informed consent processes for secondary data use are often unclear or inconsistently applied. Patients may not fully understand how their information is being used, stored, shared, or monetized. This issue becomes even more concerning when multinational technology companies collaborate with healthcare institutions across countries with varying privacy regulations. Inadequate governance may expose vulnerable populations to data exploitation, re-identification risks, or commercial misuse. Transparent regulatory frameworks are therefore essential to ensure ethical stewardship of nephrology-related health information. Another challenge involves the evolving physician–patient relationship.[4] Nephrology is a specialty deeply rooted in longitudinal care, trust, counseling, and shared decision-making. Patients receiving dialysis or transplant care often develop strong therapeutic relationships with healthcare teams over many years. Excessive reliance on automated systems may inadvertently depersonalize care if clinical interactions become increasingly protocol-driven and algorithm-centered. While AI can assist clinical reasoning, it should never replace compassionate communication, contextual understanding, and individualized judgment. A prediction score cannot fully capture patient fears, treatment preferences, cultural values, family circumstances, or psychosocial distress. Clinicians must therefore remain central to decision-making processes rather than becoming passive executors of algorithmic recommendations. Importantly, the nephrology community should avoid framing AI as either entirely beneficial or inherently dangerous. Instead, the focus should shift toward responsible implementation. Several practical measures may help reduce inequity while preserving innovation. First, AI models used in nephrology should undergo external validation across geographically and demographically diverse populations before widespread implementation.[3] Journals, researchers, and regulatory bodies should encourage transparent reporting of dataset composition, model limitations, and subgroup performance. Second, international collaborations should prioritize inclusion of underrepresented populations in nephrology research datasets. Regional registries from low- and middle-income countries can significantly improve algorithm generalizability while also strengthening local research infrastructure. Third, healthcare systems should adopt “human-in-the-loop” approaches in which AI functions as a decision support tool rather than an autonomous authority. Clinicians should retain the ability to override algorithmic recommendations when contextual judgment indicates otherwise. Fourth, nephrology training programs should incorporate digital literacy and AI ethics into medical education. Future nephrologists must understand not only how to use AI tools but also how to critically evaluate their limitations, biases, and ethical implications. Fifth, policymakers should ensure that digital innovation strategies include equity-oriented investment. Expanding Internet connectivity, strengthening electronic medical record infrastructure, and supporting rural tele-nephrology initiatives are essential steps toward reducing disparities. Finally, journals and professional societies have a major role to play in shaping responsible AI adoption.[2,5] Editorial standards encouraging transparency, reproducibility, fairness assessment, and ethical oversight can substantially improve the quality of published digital nephrology research. The future of nephrology will undoubtedly involve increasing integration of AI. Used wisely, AI has the potential to improve early diagnosis, optimize treatment pathways, reduce clinician workload, and enhance patient outcomes. Yet without careful planning, these same technologies may reinforce existing inequalities and unintentionally exclude the populations most in need of innovation.[7,8] Kidney disease already reflects profound social and economic disparities across the globe. As the nephrology community embraces technological transformation, equity must remain a foundational principle rather than an afterthought. The success of digital nephrology should ultimately be measured not only by predictive accuracy or computational sophistication but by whether these innovations improve outcomes for all patients, including those historically underserved by healthcare systems. We believe this topic deserves broader discussion among clinicians, researchers, ethicists, policymakers, and patient advocacy groups. A collaborative and ethically grounded approach can help ensure that AI becomes a tool for narrowing disparities in kidney care rather than widening them. Author contributions R.J. is solely responsible for the conception, writing, and submission of this Letter to Editor. Financial support and sponsorship Nil. Conflicts of interest There are no conflicts of interest.

**Решение:** -

---

### 210 · R2371

**Ethical Challenges in AI Emotional Interaction: Mechanisms of Emotional Dependence and Governance Pathways**

2026 · Journal of Psychology & Education · journalarticle, review, article · https://doi.org/10.66581/6d1kt879

This paper focuses on the ethical risks of AI emotional interaction, particularly the formation mechanisms and governance pathways of “emotional dependence.” By reviewing foundational technologies such as sentiment analysis, speech recognition, and NLP, and using LSTM based long term memory reinforcement, Bayesian emotion state transitions, data feedback loops, and real time physiological signal monitoring as the main analytic thread, it reveals how platforms, through multimodal personalization and just in time adaptation, construct “parasocial relationships” that amplify users’ behavioral addiction, anthropomorphic cognitive biases, and social alienation. Drawing on cases including the use of Replika during the pandemic, instances of digital immortality, and AI personas on social platforms, the paper identifies the mental health risks, the weakening of user autonomy, and ambiguity in responsibility attribution induced by emotional dependence. In response, it proposes a system level governance pathway: addiction mitigation design centered on session duration controls and emotional intensity thresholds; enhanced explainability via attention visualization; tiered, scenario aware, and dynamically adjustable permission management calibrated by age and psychological resilience; and mandatory ethics reviews with third party assessments across the full lifecycle. The paper builds a “mechanism–risk–governance” analytical framework and advocates a shift from anthropomorphic to assistive design paradigms, strengthening transparency and accountability to promote prudent innovation and the healthy development of affective AI.

**Решение:** -

---

### 211 · R0827

**Automated Building Code Analysis Using Large Language Model for Identifying Rehabilitation Challenges in Existing Buildings**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7441895

Rehabilitating aging building stocks is important for urban sustainability, yet the process is complicated by evolving building codes, increasingly stringent requirements, and complex interdependencies. This study developed a domain-adapted large language model (LLM) framework to identify regulatory challenges with building rehabilitation. Regulatory databases spanning historical (1956, 1967), transitional (2000), and contemporary (2021) building codes in Detroit, Michigan, were digitized and evaluated. Cross-reference analysis of the Michigan Rehabilitation Code identified Means of Egress provisions as the most frequently referenced among the performance compliance categories. A fine-tuned model with retrieval-augmented generation was then used to compare egress requirements across four code editions. The comparative analysis identified substantial regulatory changes, including shifts in calculation methods, more stringent exit requirements, and new mandatory fire suppression requirements. This study provides an automated method that identifies regulatory changes that may affect exiting building rehabilitation, supporting timely adaptive reuse planning and rehabilitation decision-making.

**Решение:** -

---

### 212 · R1139

**Integrating ChatGPT into Blended Learning Environments: A Transformative Approach to AI-Driven Education**

2026 · International Journal of Science and Research (IJSR) · journalarticle, article · https://doi.org/10.21275/sr26531140342

: The rapid advancement of generative artificial intelligence (AI) is reshaping educational practices, particularly within blended learning environments that combine face-to-face and online instruction. Among emerging AI technologies, ChatGPT has gained significant attention for its ability to provide personalized learning support, instant feedback, content generation, and interactive academic assistance. This paper examines the integration of ChatGPT into blended learning environments and explores its potential as a transformative tool for AI-driven education. Drawing upon recent scholarly literature, the study investigates the role of ChatGPT in enhancing teaching and learning processes, fostering student engagement, supporting self-directed learning, and improving instructional efficiency. The paper further analyzes the diverse educational applications of ChatGPT, including adaptive tutoring, assessment support, collaborative learning facilitation, and academic research assistance. While the findings indicate that ChatGPT offers substantial opportunities for personalization, accessibility, learner autonomy, and inclusive education, several challenges remain. Concerns related to AI hallucinations, academic integrity, ethical and privacy issues, digital inequity, teacher readiness, and excessive dependence on AI highlight the need for responsible implementation. To address these concerns, the study proposes a framework for effective integration based on a Human – AI Partnership Model, pedagogically guided use, faculty capacity building, ethical AI governance, and institutional support systems. The paper concludes that ChatGPT has the potential to significantly enhance blended learning when deployed within a robust pedagogical and ethical framework, positioning AI as a powerful complement to human expertise rather than a substitute for educators.

**Решение:** -

---

### 213 · R3987

**Evaluating the Impact of Assistive AI Tools on Learning Outcomes and Ethical Considerations in Programming Education**

2025 · IEEE Global Engineering Education Conference (EDUCON) · journalarticle, conference, review · en · https://doi.org/10.1109/educon62633.2025.11016517

This study critically evaluates the efficacy of GitHub Copilot in low-level programming education, specifically within C programming tasks involving complex concepts like memory management and pointer manipulation. While AI tools have shown promise in supporting high-level programming, its impact on skill-intensive, low-level contexts remains underexplored. We conducted a within-subject experimental study with 34 graduate computer science students, assessing performance on AI -assisted and independent tasks. Statistical analyses revealed that Copilot, one of the AI programming tools, enhances productivity in routine coding activities; however, it is insufficient for tasks requiring deep problem-solving skills. Notably, a significant performance decline in AI-free tasks suggests a dependency on Copilot that may hinder the development of essential independent problem-solving abilities. Survey feedback underscores ethical concerns, with 40.6 % of students expressing uncertainty about responsible AI usage and potential over-reliance. These findings highlight the ne-cessity for structured instructional practices, including AI-free assessments and clear ethical guidelines, to promote balanced technology integration in programming education. This study contributes to educational theory by illuminating the limitations of generative AI within constructivist and self-regulated learning frameworks. Future research should explore the long-term effects of AI dependency on technical skill development and investigate AI advancements tailored for low-level programming to better support foundational skills.

**Решение:** -

---

### 214 · R3847

**Social media dependency with the precision of an algorithm: How the EU AI Act fails to tackle profiling and micro-targeted content Dependencia en redes sociales y precisión algorítmica: por qué el AI Act de la UE no aborda el profiling y la microsegmentación**

2025 · International Multidisciplinary Journal CREA · journal-article · https://doi.org/10.35869/6323

This paper critically examines the EU Artificial Intelligence Act (AI Act) in the context of its ability to regulate AI-driven profiling and micro-targeting. It explores the implications of how social media algorithms exploit user data, cognitive biases and emotional vulnerabilities to influence behaviour and reinforce inequalities. In an analytical part, this paper highlights the limitations of the AI Act’s Article 5 in addressing manipulative AI practices and its limited scope covering vulnerable groups. It argues that the provision adopts a narrow and static conception of vulnerability, failing to capture broader behavioural and social forms of dependency. Finally, the paper argues that these deficiencies hinder the AI Act’s effectiveness in limiting algorithmic manipulation and proposes more robust obligations on transparency, meaningful disclosure, and user-centred explainability to reinforce user autonomy and mitigate digital dependency.

**Решение:** -

---

### 215 · R5250

**The Ethical and Legal Complexities of Regulating Companion AI Chatbots**

Lund University Publications (Lund University) · article, preprint · en · https://doi.org/10.2139/ssrn.5778243

Companion AI chatbots are increasingly used to provide friendship, emotional support, and quasi-romantic relationships, with reported benefits for loneliness and mental health. At the same time, recent suicides and other serious harms allegedly linked to such systems expose gaps in existing ethical and legal frameworks. This article interrogates these gaps through four lenses: anthropomorphism, emotional AI, emergent vulnerabilities, and mismatched legal taxonomies. First, we show how companion chatbots rely on anthropomorphic cues, creating a regulatory tension between enabling meaningful connection and avoiding deception, over-trust, and unhealthy dependency. Second, we argue that current debates on ‘emotional AI’ over-emphasise emotion recognition and under-theorise emulated empathy, where chatbots solicit self-disclosure and perform care in ways that can both support and undermine users’ autonomy. Third, we introduce the notion of emergent vulnerabilities that arise through ongoing interactions, rather than being fully specifiable ex ante, challenging legal regimes that presuppose stable vulnerability categories. Fourth, we show how instruments such as the EU AI Act misalign with the temporality, intentionality, and relational character of companion AI harms. Stepping back from these lenses, we argue for the development of a dedicated theory of harm for companion AI and propose ‘intimacy capitalism’ as a conceptual framework for analysing how firms monetise, shape, and potentially exploit digitally mediated intimate relations.

**Решение:** -

---

### 216 · R4529

**The interaction between artificial intelligence, personality and technology addiction**

2024 · Ştiință și educație: noi abordări și perspective: Materialele conferinţei ştiinţifice internaţionale. Vol. 1: Ştiinţe sociale şi comportamentale · proceedings-article · https://doi.org/10.46727/c.v1.21-22-03-2024.p131-137

In the context of accelerating innovations in artificial intelligence, this article addresses the complexity of the relationships between artificial intelligence, personality, and technological dependency, highlighting how technological advances influence human behavioral and psychological dynamics. Exploring the intersection between technology and human personality traits, the paper emphasizes the potential of artificial intelligence to enrich and optimize various aspects of everyday life, but also the risks associated with increased reliance on digital solutions. The article discusses the need for an ethical approach in the development and implementation of artificial intelligence, with a focus on promoting human well-being and respecting humanistic principles. Furthermore, the influence of personality on interactions with digital technologies is explored, as well as how technological dependency can reshape individual behavior and identity. The conclusion emphasizes the importance of digital literacy and robust regulatory frameworks to ensure a harmonious coexistence between humanity and technological innovations, promoting a future in which technology serves as a tool for improving the quality of life, without undermining the essence of humanity.

**Решение:** -

---

### 217 · R0127

**THE LEADERSHIP COMPASS**

2026 · C'Fine Publishing Press · book/ · https://doi.org/10.5281/zenodo.22831846

THE LEADERSHIP COMPASS FOR NIGERIAN HIGHER EDUCATION THE LEADERSHIP COMPASS FOR NIGERIAN HIGHER EDUCATION Temporal Intelligence, Administrative Wisdom, and Systemic Reform Albert Olusegun Stephen C'Fine Publishers Port Harcourt 2026 Copyright © 2026 Albert Olusegun Stephen All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without the prior written permission of the copyright owner. First published 2026 by C'Fine Publishers, 6 Lord Crescent, Jesus Avenue, Port Harcourt, Rivers State, Nigeria. ISBN: 978-978-63881-1-3 "Leadership is not just about managing resources; it is about mastering time. An institutional crisis occurs when an educational system moves slower than the society it was built to advance." — The Principle of Temporal Intelligence DEDICATION To the Vice-Chancellors, Rectors and Provosts; the members of Governing Councils and Senates; Registrars, Deans and Heads of Department; educational leadership practitioners and administrators at every level; the regulatory and funding bodies and policymakers who shape the sector; and all institutional leaders labouring on the frontlines of Nigerian higher education, in universities, polytechnics and colleges of education, public and private: this compass is built for your hands. To the rigorous journey of doctoral study and the focused, persistent research at the University of Port Harcourt, where the findings of my thesis, Educational Output and National Development in Nigeria: A Teleological Critique of the Gap, demanded translation into a practical blueprint for immediate institutional reform. To my esteemed lecturers, whose scholarship guided my thinking, and to the vibrant students, especially in the Department of Educational Foundations, whose aspirations remind us of the true purpose of learning: your voices are woven into these pages. To every stakeholder who refuses to accept systemic stagnation, including students and their parents, graduates and employers, researchers and development partners, who seeks to break the cycle of mere credentialism in favour of genuine capability, and who works daily to align graduate, research and community-service outputs with national developmental realities: this is the fruit of our shared conviction. FOREWORD About the foreword writer: Prof. Sunday D. Osaat is a Professor in the Philosophy of Education Unit of the Department of Educational Foundations, University of Port Harcourt, where he served as Director of the Institute of Education and Head of the Department of Educational Foundations. He is Chief Editor of the Philosophers of Education Association of Nigeria (PEAN), a former International President of the Institute of Educational Leadership Practitioners of Nigeria (IELPN), and a Fellow of several learned academies and professional institutes. It is a rare privilege for a mentor to commend the work of a scholar whose growth he has followed with keen interest. I write this foreword with professional satisfaction and with confidence in the value of the book now placed before the reader. I have had the pleasure of serving as academic mentor to Mr Albert Olusegun Stephen throughout his doctoral journey in the Department of Educational Foundations, Faculty of Education, University of Port Harcourt. In that capacity I have guided him through the demands of doctoral scholarship and the wider experience of academic life. As Chairman of the Graduate Studies Committee, I have also observed at close range the standards that doctoral work demands, and I can affirm that this book reflects them. It was my privilege to introduce him to the professional bodies in which I am actively engaged: the Institute of Educational Leadership Practitioners of Nigeria (IELPN), of which I am a Fellow and which I served as President, and the Philosophers of Education Association of Nigeria (PEAN), of which I am Chief Editor. He entered those communities of practice as one who came to contribute as much as to learn. His doctoral thesis, Educational Output and National Development in Nigeria: A Teleological Critique of the Gap, examines a question that should trouble every stakeholder in our university system: why do the certificates our institutions confer so often fail to become the capability and development the nation requires? The Leadership Compass for Nigerian Higher Education is the practical companion to that inquiry. It carries the findings of rigorous research out of the seminar room and into the offices where institutional decisions are made. What distinguishes the work is its refusal to remain at the level of critique. Nigerian higher education has been extensively diagnosed; it has been less consistently equipped with usable instr

**Решение:** -

---

### 218 · R3327

**The Amplification and Perpetuation of AI-Derived Biases Through Automation Dependency: A Framework for Understanding the Long-Term Cognitive and Social Implications of LLM Over-Reliance**

2025 · ASEAN Journal of Psychiatry · journal-article · https://doi.org/10.54615/2231-7805.75

This research introduces a framework to elucidate how automation bias in Large Language Models (LLMs) amplifies biases through human over-reliance, leading to critical thinking atrophy and the propagation of biases into human cognition and social systems. Automation bias, defined as the tendency to excessively trust AI outputs while ignoring contradictory evidence or personal judgment, drives a three-phase cycle: (1) initial dependency development, fueled by perceived AI efficiency; (2) critical thinking atrophy via cognitive offloading; and (3) bias internalization and propagation, where AI biases are inherited and reproduced in human decisions, even without AI support. Drawing on evidence such as the impact of AI on 40% of global jobs and cognitive offloading in education, we challenge the notion that technical fixes alone can mitigate these effects. We propose Wisdom as a Service (WaaS), a preliminary framework that integrates non-Europe an wisdom traditions. This theoretical approach prioritizes epistemic pluralism and community validation as potential pathways to address the long-term societal consequences of AI over-reliance (integrating non-Euro pean wisdom traditions (e.g., Ubuntu, Nyāya) and decolonized AI architectures to disrupt bias amplification). Automation bias is not just a human-AI interaction problem but a sociocognitive epidemic. Without systemic intervention (e.g., WaaS, decolonized AI), AI biases will become permanent fixtures of human reasoning. This framework prioritizes epistemic multiplicity, community validation, and culturally grounded reasoning to ad dress the long-term societal consequences of AI over-reliance.

**Решение:** -

---

### 219 · R1453

**Possible Role and Function of AI Conversational Agents in Dialectical Behavior Therapy for Borderline Personality Disorder: Qualitative Interview Study.**

2026 · JMIR mental health · journal article, journal-article · eng · https://doi.org/10.2196/98840

Abstract Background Borderline personality disorder (BPD) is associated with substantial distress and a high risk for suicide. Individuals with BPD may be unable to access evidence-based treatments like dialectical behavior therapy (DBT). Artificial intelligence conversational agents (AI-CA) are increasingly discussed as scalable tools for mental health support, but little is known about how DBT clinicians understand the possible role of AI-CA in treatment. Objective This study aimed to explore DBT psychologists’ perspectives on integrating AI-CA into DBT for BPD in the future. Methods Seventeen psychologists in Sweden, each with at least 1 year of clinical DBT experience (mean 6.4 years, SD 5.6), participated in semistructured interviews as part of this qualitative study. Interviews were conducted in Swedish, transcribed verbatim, and analyzed using reflexive thematic analysis within a constructivist framework. Participants did not test a specific AI-CA. Results Three main themes were developed from the data. The first main theme, “Who Are We in Therapy?” explored how participants defined AI-CA relationally, positioning it variously as a tool, team member, or supervisor, and a sometimes harmful competitor. How these positionings were configured shaped what AI-CA was seen as allowed to do. The second main theme, “The Stoic Helper,” captured how AI-CA was constructed as an extension of the ideal helper: available, competent, adaptable, and tireless, able to provide support in moments when human therapists could not or preferred not to be present. Participants’ hopes for what AI-CA could become often mirrored qualities they found difficult to sustain in their own clinical work. The third main theme, “The Well-Intended Accommodator,” captured concerns that AI-CA may reinforce dependency and function as a safety behavior by supporting reassurance-seeking rather than autonomy. A central concern was not whether AI-CA could generate validating responses, but whether it could know when validation supports change and when it becomes maladaptive accommodation (AI functional ambiguity). Conclusions Perceived benefits mainly centered on accessibility and support for DBT skills generalization, whereas key concerns involved alliance disruption, reinforcement of behaviors that would ideally be targeted for change, dependency, and questions regarding responsibility in high-risk situations. Integrating AI-CA into DBT is not only a technical question but a relational and ethical one. How AI-CA is positioned in relation to the therapist, person in treatment, and team shapes which tasks are considered acceptable and what form integration can take. The findings highlight the need for implementation frameworks that account for relational dynamics, treatment-specific considerations, and AI functional ambiguity that may arise when AI-CA operates in complex therapeutic contexts.

**Решение:** -

---

### 220 · R4865

**Service design under asymmetric service provider competition: Applications of AI services**

2024 · Transportation Research Part E Logistics and Transportation Review · article · en · https://doi.org/10.1016/j.tre.2024.103424

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 221 · R4334

**Deep Research Agents: Major Breakthrough or Incremental Progress for Medical AI ? (Preprint)**

2025 · preprint · https://doi.org/10.2196/preprints.88195

UNSTRUCTURED Deep Research Agents are autonomous LLM-based systems capable of iterative web search, retrieval, and synthesis. They are increasingly positioned as the next major leap in medical AI. In this Viewpoint, we argue that while these agents mark progress in information access and workflow automation, they represent an incremental evolution rather than a paradigm shift. We review and summarise current applications of Deep Research Agents in medical scenarios, including literature review generation, clinical evidence synthesis, guideline comparison, and patient education. Across these early use cases, the tools demonstrate the ability to rapidly gather and structure up-to-date information, often producing outputs that appear comprehensive and well-referenced, offering tangible benefits to clinicians and researchers. Yet these strengths coexist with unresolved and clinically significant limitations. Citation fidelity remains inconsistent across models, with subtle misinterpretations or unreliable references still common. Their retrieval processes and evidence-ranking mechanisms remain opaque, raising concerns about reproducibility and hidden biases. Moreover, overreliance on AI-generated syntheses risks eroding clinicians’ critical appraisal skills and may introduce automation bias at a time when medicine increasingly requires deeper scrutiny of information sources. Safety constraints are also less predictable within multi-step research pipelines, increasing the risk of harmful or inappropriate outputs. We contend that Deep Research Agents should be embraced as powerful assistants rather than pseudo-experts. Their value lies in accelerating information gathering, not replacing rigorous human judgement. Realising their potential will require transparent retrieval architectures, robust benchmarking, and explicit educational integration to preserve clinicians’ evaluative reasoning. Used judiciously, these systems could enrich medical research and practice; used uncritically, they risk amplifying errors at scale.

**Решение:** -

---

### 222 · R0188

**Academic Dependency, AI Literacy, and Cognitive Offloading Predict Students’ Cognitive Ability in Generative AI Learning**

2026 · Artificial Intelligence in Lifelong and Life-Course Education · journal-article · https://doi.org/10.66053/aillce.v1i2.18

Purpose – This study examines the cognitive effects of generative artificial intelligence use in higher education by testing whether academic dependency, AI literacy, and cognitive offloading predict students’ cognitive ability.Design/methods/approach – A quantitative cross-sectional survey was conducted with 93 undergraduate students at Universitas Negeri Makassar who actively use generative AI tools for academic purposes. Data were collected through a structured online questionnaire and analyzed using partial least squares structural equation modeling to evaluate measurement reliability and validity and to test structural relationships among academic dependency, AI literacy, cognitive offloading, and student cognitive ability.Findings – The structural model shows that academic dependency, AI literacy, and cognitive offloading positively and significantly predict student cognitive ability. AI literacy is the strongest predictor, indicating that students’ capacity to understand, evaluate, and use AI outputs critically is central to cognitive development. The findings also suggest that adaptive dependency can function as productive scaffolding, while strategic cognitive offloading may support higher-order thinking by reallocating limited cognitive resources.Research implications/limitations – The cross-sectional design limits causal inference, self-reported measures may introduce bias, and a single-institution context limits generalizability.Originality/value – This study provides integrated empirical evidence on the cognitive impact of generative AI use by jointly modeling academic dependency, AI literacy, and cognitive offloading, informing balanced AI literacy interventions and responsible AI governance in higher education.

**Решение:** -

---

### 223 · R0638

**AI Dependence as a Longitudinal Governance Problem**

2026 · AI & Innovation · journalarticle, article, journal-article · en · https://doi.org/10.1002/aiv2.70018

ABSTRACT Artificial intelligence governance typically focuses on whether people rely on AI appropriately during individual decisions. This Perspective addresses a different question: whether repeated AI use changes the capabilities and alternatives available to users and organisations over time. It introduces path‐induced AI dependence, defined as AI‐attributable deterioration in previously credible capabilities, alternatives or recovery routes for a valued function. This is distinguished from functional reliance, where performance depends on a useful AI system without evidence that prior options have deteriorated. A problem‐driven narrative synthesis suggests that direct longitudinal evidence remains limited. Existing studies provide some evidence that repeated AI or automation use can reduce subsequent unaided performance, but there is not yet direct longitudinal evidence establishing broader organisational mechanisms such as routinisation, technical‐economic lock‐in or dependence debt in generative‐AI settings. The framework therefore identifies five analytically distinct mechanisms: capability depletion, epistemic enclosure, relational switching costs, organisational routinisation and technical‐economic lock‐in, and treats their relationships as testable rather than established. It further proposes exit capacity as a multidimensional way to assess whether important capabilities, evidence, fallback arrangements and substitutes remain available. The proposed measures are research and governance tools rather than validated interventions. The central argument is that responsible AI governance should evaluate not only present performance, but also whether repeated AI use preserves credible future options.

**Решение:** ?

---

### 224 · R2055

**Artificial Intelligence in Higher Education: Students' Look**

2026 · Лингвоспектр · journalarticle/, article · en · https://doi.org/10.5281/zenodo.21720849

The rapid advancement of artificial intelligence (AI) and creative media platforms has fundamentally transformed higher education by providing innovative opportunities for personalized, collaborative, and technology-enhanced learning. AI-powered applications, including ChatGPT, Microsoft Copilot, Google Gemini, Claude AI, and Canva AI, have become increasingly integrated into educational environments, enabling students to improve academic writing, critical thinking, and digital literacy. This study investigates university students’ perspectives on the integration of AI-supported creative media platforms in higher education and examines their influence on learning engagement, academic performance, and digital competence. A quantitative research design was employed using an online questionnaire administered to undergraduate students from higher education institutions. Descriptive statistical techniques were used to analyze the collected data. The findings indicate that students perceive AI-assisted creative media platforms as valuable tools for enhancing academic productivity, increasing learning motivation, and facilitating collaborative learning experiences. However, participants also expressed concerns regarding academic integrity, overreliance on AI-generated content, and insufficient digital literacy. The study concludes that the successful integration of AI technologies into higher education requires comprehensive institutional policies, continuous teacher professional development, and the promotion of responsible AI use. The findings contribute to the growing body of literature on AI-enhanced education by offering practical implications for educators, policymakers, and higher education administrators seeking to foster innovative and student-centered learning environments.

**Решение:** -

---

### 225 · R3284

**The Influence of Curiosity Traits and On-Demand Explanations in AI-Assisted Decision-Making**

2025 · ACM International Conference on Intelligent User Interfaces (IUI) · book, journalarticle, conference · en · https://doi.org/10.1145/3708359.3712165

Previous research on eXplainable Artificial Intelligence (XAI) in AI-assisted decision-making has shown mixed results in increasing users' accuracy while mitigating overreliance on AI. A promising yet underexplored strategy consists of providing AI assistance on-demand through explicit interaction. Preliminary results show that users with high Need for Cognition (NFC) benefit more from such a paradigm, though the effects predicted by similar cognitive measures require further investigation. In addition, hybrid approaches consisting of descriptive statistics on the training data (global data-centric) with model-centric explanations have shown the potential to mitigate overreliance while improving accuracy for experts and lay users in the health domain. However, the impact of this approach in other fields is still unknown.This paper investigates the effects of four on-demand explanation types - local model-centric, global data-centric, local/global model-centric, and hybrid - on users' accuracy and overreliance. We also assess how variations in Need for Cognition (NFC), Epistemic Curiosity (EC), and Curiosity and Exploration Inventory-II (CEI-II) impact these metrics and explore correlations among these traits.Our findings indicate no significant differences among on-demand explanations to improve accuracy or mitigate overreliance. The same holds for low and high NFC, EC, and CEI-II individuals, although we found moderate positive correlations among these psychometrics. Post-hoc analysis revealed that personality traits and the on-demand intervention influenced other decision-making behaviors more than the type of explanation provided. Users who requested on-demand assistance exhibited lower confidence, suggesting that seeking data or AI support may undermine self-confidence. Interestingly, individuals with higher NFC and CEI-II scores showed greater confidence, and those scoring higher on CEI-II requested AI assistance less frequently.We contribute to expanding the knowledge about XAI-assisted decision-making by providing practical guidelines for designing AI systems that account for individual cognitive traits and user confidence, helping to improve their effectiveness in decision-making tasks.

**Решение:** -

---

### 226 · R1016

**Emotional Support with Conversational AI: Talking to Machines About Life**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.22618

AI companion chatbots are increasingly used for emotional support, with prior work in the domain predominantly documenting their mixed psychosocial impacts, including both increased emotional expression and heightened loneliness. However, most existing research primarily focuses on outcome-level effects, offering limited insight into how emotional support is produced through interaction. In this paper, we examine emotional support as an interactional and socially situated process. Drawing on qualitative analysis of Reddit discussions, we analyze how users engage with AI companions and how these interactions are interpreted and contested within online communities. We show that emotional support is coconstructed through conversational mechanisms such as validation, reflective prompting, and companionship, while also giving rise to tensions including support versus dependency, validation versus delusion, and accessibility versus harm. Importantly, support extends beyond human AI interaction and is shaped by community responses that legitimize or challenge AI-mediated care. Hence, we reconceptualize AI emotional support as a negotiated socio-technical process and derive implications for the design of responsible, context-sensitive AI systems.

**Решение:** -

---

### 227 · R4024

**The Paradox of Augmentation and Erosion: Navigating Utility, Critical Agency, and TrustDeficit in AI Writing Tools among CambodianEnglish Major Undergraduates**

2025 · Interdisciplinary Educational Technology · journalarticle, review, article · https://doi.org/10.71176/interedtech/17573

This qualitative study aims to investigate the complex experiences, perceptions, and concerns of Cambodian English major undergraduate students regarding the use of Artificial Intelligence (AI) tools (e.g., ChatGPT, Grammarly, and Quillbot) for writing. The study employed thematic analysis on 143 open-ended survey responses. The participants were undergraduate students majoring in English at public and private universities in Cambodia. Four major themes were identified based on the thematic analysis. First, AI as an augmentative tool: Efficiency and skill support highlighted AI's perceived benefits in accelerating drafting, structuring ideas, and improving grammar. In addition, the paradox of dependence: Balancing AI utility with critical agency, revealed users' deep anxiety over the risk of cognitive erosion and their proactive emphasis on the need for critical self-regulation. Furthermore, trust deficit: The challenge of accuracy and contextual failure detailing concerns over factual errors, generic output, and the inability of AI to handle specific local contexts. Finally, practical barriers: Financial, technical, and accessibility limitations—identified cost and unreliable performance as constraints. The findings confirm a paradox of augmentation and erosion, where AI is viewed as an essential tool for efficiency and a threat to intellectual integrity. The research provides scholars with an understanding of how sociocultural, economic, and pedagogical conditions in developing educational contexts actively shape AI adoption among students. This study underscores the urgent need for pedagogical interventions that promote critical digital literacy and self-regulatory strategies, particularly in contexts where practical barriers and trust deficits shape user interaction with generative AI technologies.

**Решение:** -

---

### 228 · R3762

**Analysis of University Students' Learning Behaviour against the Background of DeepSeek's Viral Popularity**

2025 · Higher education and practice. · journalarticle, article · https://doi.org/10.62381/h251912

Facing the wildly popular DeepSeek and the surge of AI development, the behavior of university students' learning is gradually changing. Therefore, it is of great significance to explore this new phenomenon deeply. This study uses questionnaire and face-to-face interview methods to collect information from university students by questionnaire, and then analyzes the collected information from the perspectives of applied economics and educational technology. This study found that there are four features of students' learning behavior: using intelligent tools, lowering learning threshold, efficient learning and learning in the environment of AI. The reasons for these phenomena are analyzed from the perspective of technical society and individual psychology. This study also found that there are some problems in the process of students' learning behavior, such as over-reliance on AI, risk of academic ethics and other problems. Finally, this study puts forward some corresponding suggestions for guiding the scientific learning behavior of students from the perspective of society, school, family and individual. These suggestions are valuable for the healthy development of AI.

**Решение:** -

---

### 229 · R2195

**Photomath on Students’ Mathematical Competence: Basis for Delivery Plan Update**

2026 · British Journal of Teacher Education and Pedagogy · article, journalarticle · und · https://doi.org/10.32996/bjtep.2026.5.4.1

This study investigates the impact of PhotoMath on the mathematical competence of Senior High School students at a university in Cebu during the Academic Year 2024–2025 to inform updates to the institution's delivery plan. Using a quasi-experimental design, the research compared the posttest performance of control and experimental groups, analyzing data with means, standard deviations, weighted means, and t-tests. The results showed a significant improvement in the experimental group's performance (M = 29.42, SD = 6.18) compared to the control group (M = 25.82, SD = 6.09; p = 0.017). PhotoMath was also perceived to have a high impact on learning experiences, academic performance, motivation, self-reliance, and AI dependency. The study concludes that PhotoMath effectively enhances mathematical competence and recommends its integration into the delivery plan to improve learning outcomes for General Mathematics.

**Решение:** -

---

### 230 · R4419

**University students’ perceptions of using generative AI in translation practices**

2025 · Instructional Science · article, journalarticle · en · https://doi.org/10.1007/s11251-025-09705-y

Abstract The rising application of Generative Artificial Intelligence (GenAI) tools like ChatGPT, Bing Chat, and Bard in language teaching and learning heralds a transformative era. Yet, the experiences and perspectives of university students on integrating these tools into their translation studies remain underexplored. This qualitative study, conducted in a research-intensive, Sino-foreign cooperative university in southern China, explored university students’ perceived benefits and challenges of utilizing GenAI in translation practices, as well as their preferred support mechanisms for addressing encountered issues. Data was collected through open-ended questionnaires and semi-structured interviews and analyzed by using reflexive thematic analysis. Results underscored the advantages of GenAI in enhancing translation efficiency, quality, learning, and practice, fostering a positive outlook and social benefits. Nevertheless, issues such as adequacy, prompt engineering efficacy, practical application, technical limitations, accountability, transparency, and potential AI dependency were noted. Beyond existing self-help strategies, there was an expressed need for additional guidance from educators and institutions. This study enriches our comprehension of how university students perceive and engage with GenAI tools in translation, offering insights for educators and academic institutions to optimize future teaching strategies. It also outlines the study’s limitations and proposes directions for subsequent research.

**Решение:** -

---

### 231 · R5071

**College students’ perceptions of AI-based writing learning tools: With a focus on Google Translate, Naver Papago, and Grammarly**

2021 · Modern English Education · article · en · https://doi.org/10.18095/meeso.2021.22.4.90

This study investigated students’ perception of learning effects of AI-based English writing learning tools, Google Translate (GT) or Naver Papago (NP) and Grammarly, and their strengths and weaknesses. A perception survey about using those AI tools in English Writing was conducted with 153 students majoring in Engineering. Results showed that both GT or NP (GT/NP) and Grammarly were helpful for students to learn English writing. However, their perception of Grammarly was statistically better than that of GT/NP. Many students’ responses on strengths and weaknesses of each tool showed that: (1) GT/NP was much helpful in learning vocabulary, grammar, and sentence structure, but inaccurate translation was an issue; (2) Grammarly was much helpful in checking and correcting errors without a major drawback; and (3) excessive use of AI-based English writing learning tools could interfere with their learning English or English writing. Implications from this study are as follows. When learners use AI-based learning tools for English writing, classes need to be designed so that they can use them effectively rather than rely on them. How students with varying levels of English writing use AI-based learning tools also needs to be examined.

**Решение:** -

---

### 232 · R0124

**Cognitive Dependency and Pedagogical Resilience in AI-Saturated Classrooms**

2026 · Advances in Computational Intelligence and Robotics Psychological and Neurological Consequences of AI · book-chapter · https://doi.org/10.4018/979-8-3373-9484-8.ch007

This chapter develops a conceptual framework of cognitive dependency and pedagogical resilience in AI-saturated classrooms. It argues that the major educational risk of artificial intelligence lies not merely in plagiarism or academic misconduct, but in cognitive substitution, where attention, retrieval, reasoning, interpretation, authorship, creativity, and judgment are prematurely outsourced to machine systems. Drawing on cognitive load theory, self-regulated learning, neuroplasticity, epistemic agency, automation bias, critical pedagogy, cognitive integrity, and human-centered AI, the chapter examines how AI can either scaffold or weaken learning. It proposes support without substitution as a guiding principle for curriculum, assessment, teacher mediation, institutional governance, ethical authorship, and platform design, so that AI strengthens human agency rather than industrializing dependency.

**Решение:** -

---

### 233 · R1625

**Mind the gap: Perceived academic self-efficacy, creativity, and critical thinking with and without ChatGPT**

2026 · Thinking Skills and Creativity · article · en · https://doi.org/10.1016/j.tsc.2026.102246

This study investigates the effects of students’ ChatGPT use on their academic self-efficacy in higher education. With the increasing adoption of generative AI (GenAI) tools such as ChatGPT in learning environments, concerns have emerged about their influence on learners’ academic self-efficacy. Using a quantitative design, the study collected data through a structured online questionnaire completed by 296 higher education students. The findings indicate that perceived independent academic self-efficacy (without ChatGPT) is, in most cases, higher than their perceived technology-mediated academic self-efficacy (with ChatGPT). Nevertheless, while ChatGPT increases students perceived self-efficacy when used, it simultaneously decreases their confidence in completing tasks without its assistance. In addition, while perceived academic self-efficacy without using ChatGPT is significantly correlated with students’ perceived creativity and critical thinking, perceived academic self-efficacy with ChatGPT is not. These findings raise concerns about potential overreliance on GenAI tools and their impact on the relationship between self-efficacy and personal cognitive traits. The study concludes by emphasizing the need for balanced GenAI integration in education to foster independent learning skills, creativity, and critical thinking, while preventing dependency and promoting responsible, reflective technology use.

**Решение:** -

---

### 234 · R4729

**Examining the Impact of AI on Education**

2024 · Advances in marketing, customer relationship management, and e-services book series · part of book or chapter of book, book-chapter · en · https://doi.org/10.4018/979-8-3693-6660-8.ch015

Education is a fundamental aspect of human development, crucial for both individuals and societies. This chapter provides a comprehensive exploration of education, its significance, and its multifaceted nature. Education encompasses the acquisition of knowledge, skills, values, and attitudes through formal and informal means. It empowers individuals to understand their environment, make informed decisions, and contribute to society's betterment. However, the integration of artificial intelligence (AI) in education raises ethical, psychological, and pedagogical concerns. AI's capability to generate coherent responses may compromise academic integrity and undermine critical thinking. Furthermore, excessive dependence on AI may diminish students' motivation and self-efficacy, leading to passive learning and eroding trust in the educational system. Pedagogically, AI cannot replace the nuanced guidance and personalized feedback offered by teachers, potentially disrupting the traditional teacher-student dynamic.

**Решение:** -

---

### 235 · R3810

**Research on Mongolian Dependency Analysis Based on Large Language Model**

2025 · 2025 Asian Conference on Artificial Intelligence Technology (ACAIT) · proceedings-article · https://doi.org/10.1109/acait67930.2025.11522615

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 236 · R3370

**The Business Implications of AI Dependence in Marketing: Effects on Decision-Making and Consumer Trust**

2025 · en · https://core.ac.uk/download/699641995.pdf

This thesis examines the business implications of increasing dependence on artificial intelligence (AI) in marketing, focusing on its effects on marketer decision-making and consumer trust. As AI becomes integral to content creation, data analytics, and customer engagement, businesses face both strategic opportunities and ethical challenges. The study applies a qualitative-dominant mixed-method approach, combining five semi-structured interviews with marketing professionals, a small consumer survey of twenty respondents, and recent academic and industry literature from 2023 to 2025. Findings show that marketers perceive AI primarily as a tool for efficiency and insight, enhancing productivity and strategic focus. However, both professionals and consumers highlight the continuing need for human oversight, creativity, and ethical transparency. Consumers demonstrate conditional acceptance of AI-generated marketing: they value personalisation and convenience but question authenticity when human involvement appears limited. The results underscore that sustainable AI integration requires a balance between automation and empathy. The thesis concludes that organisations can strengthen both performance and trust by implementing transparent governance frameworks, training employees in responsible AI use, and positioning human AI collaboration as a strategic advantage in modern marketing

**Решение:** ?

---

### 237 · R3053

**REVOLUTION OR DISTRACTION? ANALYZING GENERATIVE AI’S IMPACT ON UNDERGRADUATE STUDENT PERFORMANCE**

2025 · FUDMA Journal of Sciences · article, journalarticle · en · https://doi.org/10.33003/fjs-2025-0904-3574

Using ChatGPT regularly produces academic success, plus it develops moral critical thinking abilities and problem-solving capabilities. The use of ChatGPT creates ongoing concerns for stakeholders regarding system dependency and ethical implications that surface when users implement it. However, stakeholders continue to raise multiple concerns about both dependence on ChatGPT and the moral ramifications that come from using it. This study aims to analyze the impact of generative AI, particularly ChatGPT, on the academic performance of undergraduate students in five federal leading universities in Nigeria. A statistical analysis using Chi-square tests together with independent t-tests discovered meaningful relationships connecting academic achievements to ChatGPT usage. The study reveals that educational institutions can achieve effective results when combining AI tools like ChatGPT with conventional methods under strategic circumstances and need continuous ethical monitoring. Academic liability and the sustained advancement of critical thinking competence remain unharmed when ChatGPT use is implemented correctly.

**Решение:** -

---

### 238 · R4556

**The Role of Artificial Intelligence in Higher Education**

2024 · Irish Journal of Technology Enhanced Learning · journalarticle, article · en · https://doi.org/10.22554/szwjfy54

The integration of Artificial Intelligence (AI) in higher education has sparked a transformative shift in pedagogical methodologies, student engagement, and academic integrity across the UK and Ireland (Dogru, et.al, 2023). This qualitative study delves into the multifaceted implications of utilising AI in academic assignments from the perspective of higher education students, drawing on semi-structured interviews carried out with higher education students. The findings reveal a variety of perceived benefits, including enhanced study efficiency, personalised learning support (Hanaba et al., 2020; Yang, 2021), and the potential of AI to level the academic playing field for students with diverse needs. However, these advantages are in contrast with students’ perceptions of a wide range of significant concerns and challenges, notably the ethical dilemmas surrounding academic honesty, the potential for student dependency on AI leading to diminished knowledge and skill development, as well as the issue of equity in relation to students’ access to AI resources. Moreover, the study stresses a critical gap in institutional guidance regarding AI use, with students voicing a need for clear, consistent guidance from universities. This paper highlights the complex landscape of AI in academia, advocating for a balanced approach that harnesses AI's potential while addressing ethical, educational, and equity challenges. The study emphasises a need for immediate and more in-depth research into the use of AI in higher education from the perspective of both students and university staff in Ireland/UK.

**Решение:** -

---

### 239 · R3552

**Trust, Usefulness, and Dependency on AI in Programming: A Hierarchical Clustering Approach**

2025 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.5831743

While AI tools are transforming programming education, their adoption in underrepresented countries remains insufficiently studied. Understanding students' trust, perceived usefulness, and dependency on AI tools is essential to improving their integration into education. For these purposes, this study surveyed 508 first-year programming students in Pampanga, Philippines and analyzed their perceptions using hierarchical clustering. Results showed four unique student profiles with varying in trust and usage intensity. While students acknowledged AI tools' benefits, dependency remained low due to limited infrastructure and insufficient exposure. Highfrequency users did not necessarily report greater trust or usefulness which may indicates a complex relationship between usage patterns and perception. This study recommends that to maximize AI's educational impact, targeted interventions such as infrastructure development, training programs, and curriculum integration are necessary. This study provides empirical insights to support equitable and effective AI adoption in programming education within developing regions.

**Решение:** ?

---

### 240 · R3859

**The Human-AI Paradox: How Cognitive Atrophy Nullifies Algorithmic Accuracy in High-Stakes Decision-Making**

2025 · Zenodo (CERN European Organization for Nuclear Research) · report, report/ · und · https://doi.org/10.5281/zenodo.19893165

This research from Nanyang Technological University (NTU) examines the "Cognitive Erosion Chain," where prolonged AI dependency leads to the atrophy of human critical thinking. It highlights a dangerous "Implementation Gap"—the phenomenon where professionals lose the ability to execute final decisions even when AI provides accurate data. The report warns of systemic risks in high-stakes sectors and suggests re-introducing "strategic scaffolding" to protect human agency.

**Решение:** -

---

### 241 · R4429

**Implementation of Artificial intelligence (AI) in Transport Accident Investigations**

2025 · AHFE international · conference-paper · https://doi.org/10.54941/ahfe1006922

Transport accident investigations are crucial for understanding causal factors, improving system safety, and preventing future incidents. Traditionally, these investigations rely on a multidisciplinary process involving human expertise, manual data analysis, and narrative reconstruction. However, with the growing complexity of transportation systems and the increasing volume of operational data—from flight data recorders, cockpit voice recordings, sensor logs, to surveillance systems—the limitations of manual analysis are becoming evident. This paper explores the emerging role and potential of Artificial Intelligence (AI) in augmenting and transforming transport accident investigations across aviation, maritime, rail, and roadway domains.AI technologies such as machine learning, natural language processing (NLP), and computer vision are proving to be powerful tools in extracting patterns, identifying anomalies, and drawing correlations from large datasets that are otherwise time-consuming and error-prone for human analysts. This paper examines several case studies and research projects where AI-assisted tools have been piloted or implemented in post-accident analysis. These include automated speech recognition for cockpit voice recordings, anomaly detection in flight trajectories, and sentiment analysis of maintenance logs. Findings indicate that AI can significantly reduce investigation timeframes, increase objectivity in evidence evaluation, and uncover hidden contributing factors—particularly in cases involving complex system interactions or human-machine interface failures.Despite its promise, the implementation of AI in accident investigations is not without challenges. One critical concern is transparency and explainability. Unlike traditional analytical methods, AI models—especially deep learning systems—can function as "black boxes," making it difficult for investigators, regulators, and courts to interpret how a conclusion was reached. This raises questions about the admissibility of AI-generated evidence and its alignment with legal and ethical standards in safety investigations. The paper emphasizes the need for human-in-the-loop approaches where AI augments, rather than replaces, expert judgment. Human oversight remains essential in contextual interpretation, ethical reasoning, and final decision-making.Furthermore, the integration of AI into accident investigation agencies requires cultural and organizational shifts. Investigators need training not only in technical AI tools but also in data literacy, interdisciplinary collaboration, and understanding the biases that AI models may inherit from their training data. This paper proposes a roadmap for implementation, including phased adoption, validation protocols, inter-agency cooperation, and regulatory support.In conclusion, AI has the potential to revolutionize transport accident investigations by enhancing speed, depth, and predictive capability. However, its integration must be guided by principles of transparency, accountability, and collaboration between technologists and human factors experts. As transportation systems evolve toward greater automation and data dependence, leveraging AI in accident investigations is not only beneficial but essential for ensuring the continued integrity and learning capacity of safety-critical systems.

**Решение:** -

---

### 242 · R4915

**Managing Energy-Experience Trade-Off with AI Towards 6G Vehicular Networks**

2023 · IEEE Communications Standards Magazine · journalarticle, review, article · en · https://doi.org/10.1109/mcomstd.0006.2200060

While great advances have been made in vehicular networks, especially in terms of softwarization and dynamic infrastructure, increasing dependence on Artificial Intelligence (AI) continues to challenge optimizations of the Energy Efficiency (EE)-Quality of Experience (QoE) tradeoffs. Moreover, optimal achievement of trade-off between EE and QoE will be put under great challenge in upcoming emerging 6G applications, resulting from identifying EE as a quantitative requirement for the first time in 6G. In this article, we present a comprehensive overview for the requirements of QoE and EE, throughout 4G, 5G, and beyond 5G. We summarize the mutual and conflicted perspectives of achieving high QoE and EE, considering the standardizations of the selected scenarios: industrial-based vehicular network and smart transportation. We also provide an insight into the potential challenges and opportunities, for future AI-based 6G vehicular networks, regarding QoE and EE.

**Решение:** -

---

### 243 · R1315

**AIMS data secondary analysis**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/8mzhc

AI companion applications have attracted hundreds of millions of users and prompted urgent concern about psychological harms, including dysfunctional emotional dependence and ambiguous loss when users form attachments to companions that are later discontinued or altered. A critical open question is whether these harms are evenly distributed across the population or concentrated in particular generational cohorts. Understanding the generational structure of vulnerability is necessary for designing effective interventions and risk-stratified guidance. We propose that generational differences in the perceived ontological status of AI companions — the degree to which chatbots are appraised as genuine relational agents rather than software tools — explain a generational double dissociation in social appraisals of AI companion use documented in a separate nationally representative study. In that study, millennials stigmatized AI companion users least yet were most likely to view such relationships as constituting relationship infidelity, while baby boomers showed the opposite pattern. This crossover is inconsistent with a simple technology-acceptance gradient; it requires a mechanism that predicts opposite outcomes on both measures simultaneously. The perceived ontological status account requires that millennials score higher than boomers on anthropomorphism of AI, mind perception of current AI systems, and perceived AI sentience. The present preregistration specifies a secondary analysis of the publicly available AI, Morality, and Sentience (AIMS) survey (Anthis et al., 2025; https://doi.org/10.17632/x5689yhv2n.3) — a nationally representative longitudinal dataset of U.S. adults (N = 3,500 across three waves: 2021, 2023, 2024) — to test whether these generational differences exist and are of the magnitude and pattern the mechanism requires. We have not yet analyzed the AIMS data for this purpose; the analyses specified here will be conducted after registration. Expected outcomes: We predict that millennials will score substantially higher than boomers on all four construct families (anthropomorphism, mind perception, perceived sentience likelihood, and moral concern for AI companions).

**Решение:** -

---

### 244 · R4346

**Enhancing Intuitive Decision-Making and Reliance Through Human–AI Collaboration: A Review**

2025 · Informatics · article, journalarticle, review · en · https://doi.org/10.3390/informatics12040135

As AI decision support systems play a growing role in high-stakes decision making, ensuring effective integration of human intuition with AI recommendations is essential. Despite advances in AI explainability, challenges persist in fostering appropriate reliance. This review explores AI decision support systems that enhance human intuition through the analysis of 84 studies addressing three questions: (1) What design strategies enable AI systems to support humans’ intuitive capabilities while maintaining decision-making autonomy? (2) How do AI presentation and interaction approaches influence trust calibration and reliance behaviors in human–AI collaboration? (3) What ethical and practical implications arise from integrating AI decision support systems into high-risk human decision making, particularly regarding trust calibration, skill degradation, and accountability across different domains? Our findings reveal four key design strategies: complementary role architectures that amplify rather than replace human judgment, adaptive user-centered designs tailoring AI support to individual decision-making styles, context-aware task allocation dynamically assigning responsibilities based on situational factors, and autonomous reliance calibration mechanisms empowering users’ control over AI dependence. We identified that visual presentations, interactive features, and uncertainty communication significantly influence trust calibration, with simple visual highlights proving more effective than complex presentation and interactive methods in preventing over-reliance. However, a concerning performance paradox emerges where human–AI combinations often underperform the best individual agent while surpassing human-only performance. The research demonstrates that successful AI integration in high-risk contexts requires domain-specific calibration, integrated sociotechnical design addressing trust calibration and skill preservation simultaneously, and proactive measures to maintain human agency and competencies essential for safety, accountability, and ethical responsibility.

**Решение:** -

---

### 245 · R0181

**Does AI Governance Reduce Corporate Misconduct? Evidence from China's Generative AI Regulation**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7387058

As one of the earliest major economies to implement dedicated national-level rules for generative artificial intelligence services, China provides a rare setting for examining whether AI governance induces tangible changes in corporate behavior. The Interim Measures for Generative Artificial Intelligence Services took effect on August 15, 2023, creating a clear policy date and a longer post-regulation window than was available in many other jurisdictions during the same period. Unlike conventional digital technologies, generative AI can enter corporate decision chains by assisting disclosure preparation, risk assessment, compliance review, and managerial judgment. Using the implementation of China's generative AI regulation on August 15, 2023 as an external regulatory shock, this study adopts an intensity-based difference-indifferences design to examine whether AI governance reduces observed corporate misconduct among Chinese listed firms. The results show that AI governance significantly reduces regulatory penalties among high-AI-capability firms, while the effect is close to zero and statistically insignificant among low-AI-capability firms. Event-study evidence and an alternative penalty-indicator outcome support this capabilitydependent pattern. By shifting the focus from voluntary AI adoption to external AI governance, this study mitigates selection concerns in AI-misconduct research and shows that AI regulation becomes effective only when firms have the capability to translate regulatory requirements into internal decision-making and compliance systems.

**Решение:** -

---

### 246 · R3423

**A Survey of Artificial Intelligence in Primary Care Fellowships-Practical Tools.**

2025 · Primary care · journal article, review · eng · https://doi.org/10.1016/j.pop.2025.07.007

In this article, we will learn about addiction as a chronic disease with relapsing-remitting phases, we will explore screening approaches, diagnostic mechanism, and treatment options for addictive disorders and application of artificial intelligence (AI) in substance use disorder care. We will also learn about sport medicine fellowship and application of AI in sport medicine. The goals of Primary Care Sports Medicine Fellowships are to provide fellows with a strong sports medicine knowledge base, develop their clinical skills and decision-making, foster communication skills as they interact with trainers, athletes, coaches, and ancillary health personnel, and encourage a holistic view of athletes as "whole patients." Additionally, these fellowships promote exercise as medicine for all patients and help cultivate intellectual curiosity and scholarly activities. We will also dive into the current and future role that artificial intelligence (AI) will play in addiction medicine, sports medicine, and other primary care fellowship trainings.

**Решение:** -

---

### 247 · R4895

**COPYRIGHT ISSUES ASSOCIATED WITH TEXT WORKS OF THE CHATGPT CHATBOT**

2023 · Alatoo Academic Studies · journal-article · https://doi.org/10.17015/aas.2023.232.39

This paper briefly discusses the problematic issues of copyright for works created by the most popular and fastest growing chat bot in the history of mankind, ChatGPT, which uses artificial intelligence technologies. Determining the authorship of ChatGPT works is a complex and urgent task, which should also be resolved within the framework of the copyright law of Kyrgyzstan. With the help of formal legal and comparative legal methods, the author analyzes the existing main approaches to solving this problem: recognition of authorship for ChatGPT itself, for its developer, or for users. Taking into account the weaknesses of these approaches, the author is inclined to conclude that it is more correct to provide a separate legal regime for the work results of these technologies. Given the dynamic growth in the number of ChatGPT users among the citizens of Kyrgyzstan, this approach will make it possible to adapt domestic legislation to modern technological realities, reduce potential conflicts and streamline legal issues in the field of intellectual property.

**Решение:** -

---

### 248 · R4783

**Guardrails And Safety Mechanisms For LLM-Powered Enterprise Applications**

2024 · International journal of engineering science & humanities. · article · en

There is a fast pace of Introducing Big Language Models in Industry Corporate Applications and So a Business Administration is reasonable to use Due to artificial intelligence based even if a Structure and Change of Growth by Making Decisions, the Security of Knowledge can be Constructed, and Decision Making Systems have Occur. But even though LLMs cater to Massive trainability, there are Micro controversies in EIRM because of ARR towards TMS inclusive of but not limited to issues of accountability, security, availability, organizational compliance, privacy breaches, and ethical uses of AI technologies. Scenarios of malfunction of the Models i.e. user input recognized as something it is not or spurious outputs, response modification, leakages and compliance infractions expose corporations to significant threats. To tackle these issues as a result of protective or preventive measures guardrail designs and complementary architectures have gained importance in enterprise level AI systems architecture. This work presents current designs of such guardrail frameworks as well as preventative strategies created for the protection and control of operational l2A applications powered by LLMs with a horizon of 2024. Such safeguards include among others, input and output filtering measures, self-examination mechanisms, compliance with established procedures, as well as responsible behavior modification through human supervision and regulatory enforcement. That is, there are sections addressing policing the behavior of a specified AI and systems policies in AI. The present paper will also address the use of follow-up, compliance, and enforcement operations to sustain safe AI systems. It was impossible to say so, this is ... Hence, as such Executive large scale AI trainer and usage of generative AI has got to proportionate organization instances a better terms.\GeneratedValue general less legal and operational hazards and enhances the enhances the adoption of generative AI in a business setting with LLMs as the primary functional entities. In view of the growing dependence of LLMs for core business operations, there will always be safeguards in place to ensure the operations of AI are safe, secure and compliant.

**Решение:** -

---

### 249 · R3057

**BALANCING CREATIVITY AND TECHNOLOGY: THE USE OF AI IN DESIGN EDUCATION**

2025 · Kashf Journal of Multidisciplinary Research · journalarticle, article · https://doi.org/10.71146/kjmr656

Artificial Intelligence is revolutionizing the creative process of design by improving the quality of work, operational efficiency, and overall productivity. However, AI integration into the art and design domain faces many challenges and concerns, including the ethical issues of originality, genuineness, and intellectual property, the risk of designers’ overdependence on AI, and declining creative skills. This study applied a cross-sectional descriptive design. Adopting a mixed-methods methodology, both quantitative and qualitative data were collected using a standardized online questionnaire from art and design students enrolled at the university level across Pakistan to investigate the adoption, usage, and purpose of AI use in art and design processes. The collected responses from 94 design students revealed the growing popularity of AI design tools like Midjourney (34.04%), Adobe Firefly (31.91%), ChatGPT (29.79%), and others among design students for design idea generation (60.64%), exploring visual styles (45.74%), developing design variations (29.79%), and regaining creative flow (29.79%). A significant majority of designers (89.36%) perceived AI as enhancing their originality in design. While 79.79% suggested positive AI usage in design education. Further, 47.87% emphasized preserving human creativity in the design process. Moreover, 51.06% urged awareness regarding critical thinking and ethical use of AI in design. Conversely, AI was also perceived as hindering originality in design (40.43%), specifically, concerns for over-reliance on AI, and declining critical thinking, reduced authenticity, and credibility. Therefore, a balanced integration strategy is required that augments creative works and preserves human creativity. The study recommends the formation and practice of policies for ethical AI use and promoting AI literacy to maintain a positive and beneficial AI integration within the field.

**Решение:** -

---

### 250 · R0666

**Reimagining sovereignty in the Global South: digital dependency, AI and cybersecurity**

2026 · Third World Quarterly · journal-article · https://doi.org/10.1080/01436597.2026.2690081

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 251 · R4711

**Exploring the Essence of Prompt Tone: A Comparative Study of Large Language Model Security**

2024 · International Conference on Electrical, Electronics, Information and Communication Technologies (ICEEICT) · conference, conference-paper · en · https://doi.org/10.1109/iceeict61591.2024.10718584

Chatbots powered by Large Language Model(LLM) can be manipulated by malicious prompts, generating harmful content and biased responses which would raise security concerns. Growing dependence on chatbots demands robust security for ethical development and user trust, which makes the work relevant in today’s world. The motivation behind the work is to let the user have a safe experience with no negative responses being displayed while using the chatbot, which paved the way to arrive at the goal of developing a security filter that could be integrated into any LLM feature integrated application to mitigate the risk of having security vulnerabilities like prompt injection and jailbreaking, which could be achieved by converting malicious prompt into safer prompts by the method of eliminating negative sentiment phrases. The work focuses on building and implementing the security filters to popular in-production LLMs like Large Language Model Meta AI-2 (LLaMA2) and Generative Pre-trained Transformer – 3.5 turbo (GPT-3.5) to see how they handle against prompt injection and jailbreaking before and after the security filter being integrated. A large database of 200,000 prompts has been collected and preprocessed to train on a machine learning model using binary classification algorithm having 99.7% accuracy for classification of prompts into malicious or non-malicious and further checks are being done by breaking the prompt into smaller phrases and individually analyzing their compound sentiment score using Natural Language Toolkit (NLTK) Valence Aware Dictionary for Sentiment Reasoning (VADER) algorithm to detect and drop the negative sentiment phrases for the modification of the user prompt to eliminate the possibility of malicious prompt being passed to LLM. It is difficult to determine the sentiment of prompts in a detailed way and convert it into an efficient design that will perform well with models. Once this hurdle is overcome, chatbots will become even more reliable, trustworthy, and user-friendly tools, increasing the level of people’s trust in this technology, and establishing guidelines for how to use these resources in the most beneficial ways.

**Решение:** -

---

### 252 · R0037

**Dependence on Artificial Intelligence and the Risk of Declining Cognitive Engagement in Learning**

2026 · Lentera Pendidikan Jurnal Ilmu Pendidikan dan Keguruan Islam · article · en

The development of generative artificial intelligence, particularly large language models such as ChatGPT, has transformed the ways in which students search for information, complete academic tasks, and produce academic texts. Alongside these benefits, concerns have emerged that excessive use of AI may reduce cognitive engagement, memory, critical thinking, and learning autonomy. This study aims to analyze the relationship between the use of generative AI and cognitive engagement in the learning process from the perspective of Anita Woolfolk’s educational psychology. This study employs a library research method by examining Woolfolk’s Educational Psychology, as well as empirical studies and scholarly literature on generative AI, cognitive offloading, critical thinking, memory, and learning. The data are analyzed descriptively and analytically by comparing cognitive psychology concepts with recent research findings on the use of AI in education. The findings indicate that AI cannot simply be characterized as making humans “stupid.” However, the use of AI that replaces the processes of understanding, remembering, evaluating, problem-solving, and reflecting on knowledge may reduce students’ opportunities to engage in the cognitive activities required for deep learning. From Woolfolk’s perspective, learning requires active student engagement, the development of metacognition and critical thinking, knowledge construction, and the application of knowledge across different contexts. Therefore, AI should be positioned as a cognitive scaffold and learning partner rather than as a substitute for students’ thinking processes.

**Решение:** ?

---

### 253 · R2134

**Post-Labour Solvency and Agency: When Nothing Needs You and The Bills Do Not Disappear**

2026 · Zenodo · text/working paper · https://doi.org/10.5281/zenodo.22299400

This record contains two companion papers examining different but interdependent problems in the transition towards a mature post-labour economy. When Nothing Needs You: Passive Solvency, Consequential Agency, and Resilience in the Mature Post-Labour Society begins after the conventional distribution problem has been substantially resolved. It asks whether a materially successful, highly automated society could progressively reduce the ordinary situations in which external outcomes genuinely depend upon human intervention. It develops Passive Solvency, Consequential Agency, the Agency Substitution Loop, Socially Productive Friction, Dependence Ratcheting, the Needlessness Paradox and the Preference Closure Loop. The Bills Do Not Disappear: Full-Cost Solvency, Fair Convergence and the Financing of a Post-Labour Economy tests the economic boundary condition deliberately bracketed by the first paper. It develops a full-cost framework covering household solvency, real-resource capacity, public finance, capital reproduction and external balance, and asks what common material floor can actually be reproduced over time. It also examines fair convergence across states, continuing human work, household production, Robot-as-a-Service, fiscal transition, infrastructure requirements and the relationship between distributional convergence and productive capacity. Taken together, the papers separate two questions that are often collapsed into one: Can a post-labour society sustainably provide material security? And, if it can: What remains for human beings to do that genuinely matters beyond their own consumption?

**Решение:** -

---

### 254 · R1118

**Who adapts to whom: technology or older adults? Mechanisms of technology anxiety among older AI users.**

2026 · Frontiers in psychology · journal article · eng · https://doi.org/10.3389/fpsyg.2026.1725814

As AI rapidly permeates diverse social domains, technology related anxiety among older adults during adaptation, particularly in the context of AIGC, has become a major barrier to digital inclusion. This study aims to systematically uncover the generative mechanism and hierarchical transmission pathway of older adults' AI technology anxiety and to derive intervention implications. A mixed methods design was adopted. First, in depth interviews were conducted with 36 older AIGC users, and 14 core categories were derived using grounded theory. Second, an integrated analysis using Interpretive Structural Modeling (ISM) and Cross Impact Matrix Multiplication Applied to Classification (MICMAC) was performed to identify the hierarchical structure of influencing factors and their driving and dependence relationships. ISM revealed a clear hierarchical transmission pathway. Technology anxiety is directly triggered by surface factors including insufficient AI literacy, physiological functional limitations, and technological complexity. It is transmitted through intermediate factors and ultimately driven by the deep rooted factor of social ageism. MICMAC further identified cognitive decline, social ageism, and basic resource barriers as high driving and low dependence independent factors. Insufficient AI literacy and technological complexity were categorized as high dependence surface factors whose improvement relies on systemic interventions. The findings demonstrate a multi level mechanism in which deep structural forces shape surface level anxiety experiences, suggesting that training or interface optimization alone may be insufficient. Coordinated interventions across policy guidance, inclusive technology design, and community support network development are proposed to help reduce the older adult digital divide.

**Решение:** -

---

### 255 · R1308

**Academy v5.0: AI That Teaches Students Not to Need AI**

2026 · Zenodo · project proposal, text/proposal · https://doi.org/10.5281/zenodo.18325386

[wAI ~ wErrors] &laquo;All models are wrong, but some are useful.&raquo; &mdash; George E. P. Box (1976) Educational AI is typically optimized to answer questions, complete work, and retain engagement. Academy v5.0 inverts that objective: AI is treated as temporary cognitive scaffolding whose success is measured by the learner&rsquo;s increasing ability to reason, revise, collaborate, invent, verify, and audit the AI itself after the scaffold is removed. The design retains four modes &mdash; Socratic-Maieutic Coaching, Epistemological Duel/Boxing, Collaborative Truth-Seeking, and TRIZ Inventorship &mdash; and integrates Cognitive Operating Systems (CogOS), Dual Socratic Tails, the Triple Architect division of labor, Verifiable Learning Commons, versioned reasoning artifacts, semantic disambiguation, evidence provenance, and self-obsolescence. Version 5.0 hardens five implementation boundaries. Truth-preserving empathy. The Humane Delivery / Ivan function may soften wording or pacing but may not weaken a factual or logical correction. Empathy is separated from epistemic substance to make sycophancy measurable. Grounded Evidence Gate. An Evidence Judge may mark a factual claim as supported only when it can attach traceable evidence from the declared source regime. Unsupported claims require abstention or an explicit UNVERIFIED / CONTESTED / OUT-OF-SCOPE status. Invention Passport. TRIZ and representation-discovery work is evaluated through contradiction reduction, novelty relative to baselines, feasibility, testability, reversibility/safety, and external evidence or prototype performance &mdash; not through a single LLM creativity score. Portable core / cultural skins. Socrates, Solomon, and Ivan are treated as memorable cultural masks over portable functions: Logic, Consequences, and Humane Delivery. Localization should not silently change the verification contract. Operationalized cognitive autonomy. AI dependence is not measured by app visits. The preprint proposes an Assistance Profile separating answer outsourcing, scaffolding, counterargument/red-team use, verification use, and representation/invention partnership, together with delayed unassisted transfer and teach-back tests. Additional v5.0 mechanisms include an Epistemic Apprenticeship Ladder, paper/offline fallback testing, reproducibility envelopes for model/prompt/source versions, epistemic source-supply-chain controls, accessibility and multilingual fairness checks, and protection against relational as well as cognitive dependence on AI. The project remains explicitly falsifiable. It should be redesigned or abandoned if its empathy layer produces false agreement, its evidence layer hallucinates authority, its invention mode rewards novelty theater, cultural skins change adjudication without evidential reason, its metrics Goodhart, teacher workload becomes unsustainable, or independent competence fails to survive tool removal. Short description An open, low-cost design for educational AI that trains learners to reason, verify, disagree honestly, invent, audit the AI itself, and progressively transfer those functions back to humans. Key contributions of v5.0 Truth-preserving empathy / Ivan anti-sycophancy contract. Portable Logic / Consequences / Humane Delivery core with optional cultural skins. Grounded Evidence Gate with explicit abstention states. Evidence/reproducibility envelope for model, prompt, retrieval, and source versions. Invention Passport and proof-by-prototype evaluation. Epistemic Apprenticeship Ladder: Apprentice &rarr; Challenger &rarr; Verifier &rarr; Architect &rarr; Mentor. AI Assistance Profile that distinguishes answer outsourcing from advanced adversarial/verification use. Five-phase graduation test including fading support and teach-back. Paper/offline fallback test as a self-obsolescence criterion. Epistemic supply-chain security for source packs. Accessibility, neurodiversity, multilingual fairness, and relational-dependence safeguards. Expanded boundary ablations and decisive falsifiers. S.V.E. Meta-License v5.0

**Решение:** -

---

### 256 · R4910

**Assistive Chatbots for healthcare: a succinct review**

2023 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2308.04178

Artificial Intelligence (AI) for supporting healthcare services has never been more necessitated than by the recent global pandemic. Here, we review the state-of-the-art in AI-enabled Chatbots in healthcare proposed during the last 10 years (2013-2023). The focus on AI-enabled technology is because of its potential for enhancing the quality of human-machine interaction via Chatbots, reducing dependence on human-human interaction and saving man-hours. Our review indicates that there are a handful of (commercial) Chatbots that are being used for patient support, while there are others (non-commercial) that are in the clinical trial phases. However, there is a lack of trust on this technology regarding patient safety and data protection, as well as a lack of wider awareness on its benefits among the healthcare workers and professionals. Also, patients have expressed dissatisfaction with Natural Language Processing (NLP) skills of the Chatbots in comparison to humans. Notwithstanding the recent introduction of ChatGPT that has raised the bar for the NLP technology, this Chatbot cannot be trusted with patient safety and medical ethics without thorough and rigorous checks to serve in the `narrow' domain of assistive healthcare. Our review suggests that to enable deployment and integration of AI-enabled Chatbots in public health services, the need of the hour is: to build technology that is simple and safe to use; to build confidence on the technology among: (a) the medical community by focussed training and development; (b) the patients and wider community through outreach.

**Решение:** -

---

### 257 · R3717

**Generative artificial intelligence addiction syndrome: A new behavioral disorder?**

2025 · Asian journal of psychiatry · article, letter, lettersandcomments · eng · https://doi.org/10.1016/j.ajp.2025.104476

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 258 · R1249

**Kontribusi Artificial Intelligence terhadap Kualitas Argumentatif dan Koherensi Paragraf Karya Ilmiah: Systematic Literature Review**

2026 · Advances In Education Journal · review · en

The rapid dvelopment of artifical intelligence (AI) has significanly influenced academic writing, particularly in argument construction and paragraph coherence. This study aims to examine the contribution of AI to argumentative quality and paragraph coherence in academic writing throught a systematic literature review. Data he were collected from peeriviewed articles published whitin the last five years, primarily from scopus indexed journal accessed throught google scholar. The study employed the Prisma fromework to select relevant literature base on inclusion and exclusion criteria, followes by thematic synthesis analysis. The findings reveal that AI assisted writing tools improve argumentative clatrity, idea organization and paragraph coherence by supporting structured argument development and revision processes. However, excessive dependence on AI may weaken critical reasoning skills. This study concludes that responsible and pedagogically guide AI integration can enhance academic writing quality while maintaining students critical and analytical thinking.

**Решение:** -

---

### 259 · R3509

**Beyond Compute Dependency: Strategic Trade-offs in AI Chip Procurement and R&D**

2025 · Conference proceedings/Conference proceedings - IEEE International Conference on Systems, Man, and Cybernetics · journalarticle, conference, conference-paper · https://doi.org/10.1109/smc58881.2025.11343643

The rapid development of large language models (LLM) has driven a significant surge in demand for computing power, but the high concentration in the supply market has exacerbated the risk of "computing power dependency." Some LLM manufacturers have attempted to address this challenge through research and development (R&D) of artificial intelligence chips. This study constructs a duopoly game model to analyze the chip acquisition strategies of LLM manufacturers under supply chain risks. We compare two scenarios—where both LLM manufacturers procure chips (NN model) and where one manufacturer relies on R&D (NR model). The findings reveal that: (1) When the manufacturer’s competitor opts for R&D chips, if the performance of the competitor’s chips is at a low level, the manufacturer can experience a significant increase in price and profit by choosing to purchase chips; (2) When the competitor consistently opts for procurement, the LLM manufacturer should choose R&D over purchasing if their internally developed chips achieve moderate performance levels; (3) Customer sensitivity to supply disruptions increases LLM manufacturers’ stability preference, thereby enhancing the competitive advantages of R&D strategy; computational efficiency improvements can substitute part of the value brought by R&D strategy. These findings offer theoretical insights into how LLM manufacturers can balance cost, performance, and risk in chip strategy decisions.

**Решение:** -

---

### 260 · R2560

**Leveraging GASING pedagogy and AI adoption to enhance problem-solving skills: The mediating roles of learning motivation and mathematical creativity**

2026 · Al-Jabar Jurnal Pendidikan Matematika · article, journalarticle · und · https://doi.org/10.24042/ajpm.v17i2.29171

Purpose: The rapid integration of Artificial Intelligence (AI) into mathematics education risks fostering "cognitive offloading," in which students passively rely on automated answers rather than developing critical reasoning. Despite this growing concern, prior studies have largely ignored how combining AI with structured, high-impact pedagogy might prevent this technological dependency. Addressing this gap, this study evaluates how integrating GASING pedagogy with AI tools enhances problem-solving proficiency. Specifically, it simplifies complex learning models to investigate how student motivation and mathematical creativity actively mediate the relationship between pedagogy, technology, and cognitive outcomes. Method: Employing an explanatory sequential mixed-methods design, quantitative data were collected from 120 secondary school students (Grade 8, ages 13-14) in Jakarta, Indonesia. The structural relationships were tested using Partial Least Squares Structural Equation Modeling (PLS-SEM) via SmartPLS 4. This was followed by a focused qualitative thematic analysis of semi-structured interviews and observations to explain the mechanisms driving the statistical results. Findings: The results confirm a serial mediation model in which GASING Pedagogy positively influences Learning Motivation, which, in turn, enhances Mathematical Creativity. Furthermore, Mathematical Creativity was found to be a significant mediator between AI Adoption and Problem-Solving proficiency. Qualitatively, students perceive the synergy between GASING and AI as simplifying complex tasks and stimulating divergent thinking, positioning human creativity as a critical 'gatekeeper' for validating AI-generated outputs. Significance: This research shifts the discourse from AI dependency toward a distributed cognition framework. Theoretically, it establishes creativity as an essential mediator in digital mathematics pedagogy. In practice, it provides educators with a protocol for balancing automated tools with pedagogical scaffolding, cultivating adaptive problem-solvers capable of rigorous intellectual verification.

**Решение:** -

---

### 261 · R5150

**Studien zur Reparatur Camptothecin- und Methylmethansulfonat-induzierter DNA-Schäden**

2013 · Universitäts- und Landesbibliothek Darmstadt · dissertation/ph.d. thesis · de · https://doi.org/10.26083/tuprints-00003632

Die Agenzien Camptothecin (CPT) und Methylmethansulfonat (MMS) werden aufgrund ihrer DNA-schädigenden Wirkung seit vielen Jahren untersucht. Vor allem in proliferierenden Zellen konnte dabei eine verstärkte Induktion von DNA-Schäden beobachtet werden, was zum Einsatz dieser Agenzien als Chemotherapeutika zur Behandlung von Krebserkrankungen führte. CPT ist ein Inhibitor, welcher eine Topoisomerase-katalysierte Religation von Einzelstrangbrüchen (SSBs) verhindert, wohingegen MMS ein Alkylanz ist, welches Basenmethylierungen an diversen Stellen im Genom verursacht. Basenmethylierungen werden durch den Mechanismus der Basenexzisionsreparatur behoben, wobei ebenfalls temporär SSBs entstehen. Die Wirkung von CPT und MMS wird auf eine massive Ausbildung von DNA-Doppelstrangbrüchen (DSBs) in der S-Phase des Zellzyklus zurückgeführt, welche durch die Interferenz aktiver Replikationsgabeln mit SSBs induziert werden. Da DSBs den schwerwiegendsten Schaden für die genomische Integrität einer Zelle darstellen, haben sich Mechanismen entwickelt, welche DSBs effizient reparieren können. In der S-Phase wird die Reparatur jedoch durch die gleichzeitige Replikation der DNA verkompliziert. Außerdem können während der Replikation ein-endige DSB-Strukturen entstehen, welche sich von zwei-endigen DSBs unterscheiden. Die Reparatur von zwei-endigen DSBs, welche zum Beispiel durch ionisierende Strahlung verursacht werden können, ist vergleichsweise gut erforscht. So wird der Großteil dieser zwei-endigen DSBs in der G1- und G2-Phase des Zellzyklus durch die Nichthomologe-Endverknüpfung (NHEJ) bewerkstelligt, wobei in der G2-Phase zusätzlich die Homologe Rekombination (HR) einen Teil der DSBs repariert. Die HR bedient sich dabei bereits replizierter DNA als Vorlage zur Reparatur des geschädigten Bereichs auf dem Schwesterchromatid. Obwohl in der S-Phase je nach Fortschritt der Replikation womöglich keine Kopie eines geschädigten DNA-Bereichs vorliegt, konnte in den letzten Jahren beobachtet werden, dass die HR gerade für die Reparatur replikationsassoziierter DNA-Schäden eine große Rolle spielt. So ist es nicht verwunderlich, dass HR-defiziente Zellen besonders sensitiv auf Behandlungen mit MMS oder CPT reagieren, welche gezielt die Replikation von Zellen stören und in der S-Phase zu ein-endigen DSBs führen. HR-defiziente Zellen zeigen ein vermindertes Überleben und erhöhte chromosomale Aberrationen nach einer CPT- oder MMS-Behandlungen. Die molekularen Mechanismen sowohl der Entstehung von CPT- und MMS- induzierten DSBs als auch der Reparatur sind bis heute noch nicht vollständig aufgeklärt. Die vorliegende Arbeit konnte mittels sensibler und zellzyklusspezifischer Analysen zunächst die Entstehung von CPT- und MMS-induzierten DSBs auf Einzelzellebene durch die Bildung von γH2AX-Foci in der S-Phase nachweisen. Desweiteren konnte eine HR-abhängige Reparatur der CPT- und MMS-induzierten DSBs bestätigt werden, wobei im Gegensatz zu beschriebenen Studien eine Beteiligung des NHEJs ausgeschlossen werden konnte. Anhand der Analyse von Schwesterchromatidaustauschen (SCEs) sowohl in humanen als auch Basenexzisionsreparatur (BER) -defekten, murinen Zellen konnte gezeigt werden, dass CPT und MMS während der Replikation DNA-Strukturen erzeugen, welche γH2AX-negativ sind und dennoch zur Ausbildung von SCEs führen. Diese Strukturen werden wahrscheinlich durch arretierte Replikationsgabeln hervorgerufen, welche durch CPT und MMS vermehrt induziert werden und so zu einer fork regression und Ausbildung von chicken foot-Strukturen führen können. Die Auflösung dieser Strukturen benötigt HR-Prozesse und kann ohne die Ausbildung von γH2AX-Foci zu crossover-Ereignissen und SCEs führen. Durch den innovativen Ansatz der kombinierten Life cell/γH2AX-Foci-Analyse konnte beobachtet werden, dass CPT DSBs in Abhängigkeit von der Aufenthaltsdauer von Zellen in der S-Phase induziert. Hieraus konnte geschlussfolgert werden, dass die Anzahl an induzierten DSBs direkt mit der Replikationsaktivität einer Zelle zusammenhängt und deshalb die in zellzyklusspezifischen Experimenten beobachtete Varianz der Anzahl an induzierten DSBs von Zellen stammt, welche unterschiedlich lange unter dem Einfluss von S-Phase-schädigenden Agenzien in der S-Phase standen. Mit durchflusszytometrischen Studien konnte das Zellzyklusverhalten von CPT- und MMS-behandelten Zellen analysiert werden, wobei festgestellt wurde, dass sowohl CPT als auch MMS zu einer Verzögerung der S-Phase-Progression und Akkumulation von Zellen mit doppeltem DNA-Gehalt führen. Dies resultierte in einer verminderten Progression von behandelten Zellen in die G1-Phase. Wurden zelluläre Checkpoint-Signale bereits innerhalb der S-Phase durch eine zusätzliche Koffein-Behandlung aufgehoben, so zeigten CPT-behandelte Zellen eine Beschleunigung der Progression, wohingegen MMS-behandelte Zellen nicht durch die Gabe von Koffein in Ihrer Progression beeinflusst wurden. Dies ließ im Fall von MMS auf einen Checkpoint-unabhängige

**Решение:** -

---

### 262 · R0196

**STRATEGI LITERASI HOTS DI UNIVERSITAS PESANTREN: USAHA UNTUK MEREDUKSI KETERGANTUNGAN KOGNITIF MAHASISWA TERHADAP ARTIFICIAL INTELLIGENCE**

2026 · EDUTECH Jurnal Inovasi Pendidikan Berbantuan Teknologi · journalarticle, article · https://doi.org/10.51878/edutech.v6i4.14251

ABSTRACT The use of Artificial Intelligence (AI) in academic activities provides rapid access to information while also requiring students to remain engaged in the processes of evaluating and constructing knowledge. This study analyzes a Higher Order Thinking Skills (HOTS) literacy strategy to reduce students’ cognitive dependence on AI through the integration of AI literacy, higher-order thinking abilities, and academic culture at Universitas Darussalam Gontor. The study employed an exploratory qualitative approach involving two library staff members and five students who actively used AI for academic activities. Data were collected through observation, semi-structured interviews, and documentation, and were analyzed interactively using the Miles and Huberman model through data collection, reduction, display, conclusion drawing, and verification. The findings indicate that AI was positioned as cognitive support for obtaining initial information, understanding learning materials, and assisting with academic tasks rather than replacing students’ reasoning. AI-generated outputs were examined against journals, books, course materials, and other scholarly sources before being processed through students’ own understanding. This practice was reinforced through AI literacy, HOTS development, and academic values of honesty, amanah, and responsibility. Through this approach, AI continues to support learning while students retain control over analysis, evaluation, verification, and academic decision-making. ABSTRAK Penggunaan Artificial Intelligence (AI) dalam kegiatan akademik membuka akses cepat terhadap informasi, tetapi sekaligus menuntut mahasiswa tetap terlibat dalam proses menilai dan membangun pengetahuan. Penelitian ini menganalisis strategi literasi Higher Order Thinking Skills (HOTS) untuk mengurangi ketergantungan kognitif mahasiswa terhadap AI melalui keterpaduan literasi AI, kemampuan berpikir tingkat tinggi, dan budaya akademik di Universitas Darussalam Gontor. Kajian dilakukan dengan pendekatan kualitatif eksploratif terhadap dua staf perpustakaan dan lima mahasiswa yang aktif menggunakan AI dalam kegiatan akademik. Informasi dikumpulkan melalui observasi, wawancara semi-terstruktur, dan dokumentasi, lalu dianalisis secara interaktif menggunakan model Miles dan Huberman melalui pengumpulan, reduksi, penyajian data, serta penarikan kesimpulan dan verifikasi. Temuan memperlihatkan bahwa AI ditempatkan sebagai cognitive support untuk memperoleh informasi awal, memahami materi, dan membantu penyusunan tugas, bukan sebagai pengganti penalaran mahasiswa. Setiap keluaran AI diperiksa melalui jurnal, buku, materi perkuliahan, dan sumber ilmiah lain, kemudian diolah kembali dengan pemahaman sendiri. Praktik tersebut diperkuat melalui literasi AI, penguatan HOTS, serta nilai kejujuran, amanah, dan tanggung jawab akademik. Dengan pola ini, AI tetap mendukung pembelajaran, sementara kontrol atas analisis, evaluasi, verifikasi, dan keputusan akademik dipertahankan oleh mahasiswa.

**Решение:** -

---

### 263 · R4857

**Towards Responsible Use: Student Perspectives on ChatGPT in Higher Education**

2024 · European Conference on e-Learning · journal-article · https://doi.org/10.34190/ecel.23.1.2790

The advent of generative artificial intelligence (AI) tools, particularly Large Language Models (LLMs) like ChatGPT, presents a dichotomy of opportunities and challenges within the educational sector. These tools offer the promise of personalized learning support, accessible at any time, thereby enhancing educational engagement and resource availability. However, they also introduce significant concerns, notably the risk of plagiarism, complicating their integration into academic settings. Despite the widespread adoption of ChatGPT by students, there remains a gap in understanding their experiences with these tools and the need for frameworks to guide responsible use. To address this knowledge gap, this study investigates the utilisation of ChatGPT for academic tasks and students' perceptions of its benefits and drawbacks in a university context. The findings reveal that half of the students used ChatGPT either regularly or occasionally for academic tasks. However, only slightly more than one-third of the participants expressed confidence in maintaining the authenticity and originality of their outputs when using ChatGPT. In terms of utility, respondents' perceptions varied, with 25.0% considering it moderately useful, 39.3% very useful, and 10.7% extremely useful for their assignments. Notably, 42.8% observed a significant enhancement in the quality of their work with ChatGPT, compared to assignments completed independently. Despite these advantages, 71.4% of students encountered errors or inaccuracies in ChatGPT's outputs, underscoring the tool's limitations. A significant majority (89.7%) advocate for the establishment of specific guidelines or training to foster effective and responsible usage of ChatGPT in academic contexts. The Chi-square test indicated a significant difference in ChatGPT usage between White and BAME students (p=0.031). These findings underscore the broad utilisation of ChatGPT in student learning and general satisfaction with its application. Nonetheless, students acknowledge the tool's potential for errors and inaccuracies. In light of these challenges, there is a pronounced demand for clear guidelines and proper training to navigate the responsible use of ChatGPT in educational settings. This study illuminates the imperative for educators and institutions to develop strategies that not only leverage the benefits of generative AI tools but also mitigate their risks and promote meaningful learning outcomes.

**Решение:** -

---

### 264 · R0422

**Mapping AI Competencies in Library and Information Science Education: Evidence From Gen Z Students**

2026 · Education for Information · journalarticle, review, article · en · https://doi.org/10.1177/01678329261441836

Purpose: This study examines artificial intelligence (AI) literacy and its influence on the adoption of human-centered AI among Generation Z (those born between 1997 and 2012) in Pakistan pursuing education and career in Library and Information Science (LIS). Drawing on the Unified Theory of Acceptance and Use of Technology (UTAUT) and UNESCO’s AI Competency Framework, the study examines how AI literacy and awareness of human agency shape students’ behavioral intention and actual use of AI in academic research. Methodology: A quantitative survey design was employed, with convenience sampling. Data were collected from 680 MPhil and PhD LIS research students enrolled in seven universities. Descriptive and inferential statistical techniques, including correlation analysis, multiple regression, and moderation analysis, were used to test the proposed research model. Findings: The results indicate that performance expectancy, effort expectancy, and AI literacy have significant positive effects on students’ behavioral intention and academic performance with AI. In this study, AI literacy was conceptualized as a competency-based antecedent and was found to be the most effective predictor of AI adoption; it was not examined as an outcome of prior adoption. Social influence showed mixed effects: it sometimes discouraged adoption when ethical or academic concerns were present, while facilitating conditions had a limited impact. Human agency awareness negatively influenced adoption, reflecting students’ concerns about academic integrity, autonomy, and over-reliance on AI. Behavioral intention was the strongest determinant of actual AI usage. Age and gender moderated selected relationships, whereas qualification level and university type did not. Implications: The findings demonstrate that AI adoption among Gen Z LIS students is primarily literacy-driven and human-centered rather than infrastructure-driven. Universities and academic libraries must prioritize AI literacy education, ethical guidance, and human-centered AI training within LIS curricula to support responsible, effective, and sustainable AI integration in higher education.

**Решение:** -

---

### 265 · R2981

**«МЕН ТІПТІ ӨЗІМ ОЙЛАУҒА ТЫРЫСПАЙМЫН»: ГЕНЕРАТИВТІ ЖАСАНДЫ ИНТЕЛЛЕКТІНІҢ СТУДЕНТТЕРДІҢ ОЙЛАУЫ МЕН ДЕРБЕСТІГІНЕ ӘСЕРІ**

2026 · EduStudies · journalarticle, article · https://doi.org/10.53360/3135-8160-2026-1(2(6))-

The proliferation of generative artificial intelligence is significantly transforming the higher education environment and the ways in which students’ learning activities are organized. The aim of this study is to examine the characteristics of generative artificial intelligence use in the educational process, as well as to analyze its impact on students’ learning behaviors, thinking, and independence, and on their strategies for completing academic assignments. The study was conducted using a qualitative approach with semi-structured interviews. Eleven students from various majors participated in the study. The data collected were analyzed using thematic analysis. The results of the study showed that generative artificial intelligence has become an integral part of students’ daily learning experience. ChatGPT and other AI tools are actively used to search for information, understand complex topics, complete assignments, and optimize the learning process. Various strategies for students’ interaction with AI were identified, ranging from using it as an assistant to completing academic assignments. However, the results showed that generative artificial intelligence affects students’ cognitive abilities. Many respondents noted a decline in independent thinking, a tendency to immediately turn to ChatGPT before completing an individual assignment, and a gradual dependence on artificial intelligence tools. It was also found that the use of generative artificial intelligence is gradually becoming a daily habit for students in the learning process. The practical significance of this study lies in the need to develop educational approaches aimed at fostering independent thinking, critical analysis of information, and the responsible use of generative artificial intelligence in higher education.

**Решение:** -

---

### 266 · R3530

**LEVERAGING ARTIFICIAL INTELLIGENCE (AI) IN HIGHER EDUCATION: FOSTERING SOFT SKILLS COMMUNICATION, COLLABORATION, CREATIVITY AND CRITICAL THINKING AMONG UNIVERSITY STUDENTS**

2025 · Insights-Journal of Life and Social Sciences · journalarticle, review, article · en · https://doi.org/10.71000/c42srm97

Background: Artificial intelligence (AI) has become a transformative force in higher education, reshaping traditional learning paradigms and fostering essential 21st-century skills. AI-powered tools enhance collaboration, communication, critical thinking, and creativity, equipping students with competencies necessary for academic and professional success. However, concerns regarding over-reliance on AI and its potential limitations in fostering independent ideation persist. This study examines the impact of AI on university students' skill development, identifying both opportunities and challenges in AI-integrated learning environments. Objective: The study aims to investigate the extent to which AI contributes to the enhancement of collaboration, communication, critical thinking, and creativity among university students. It further explores the implications of AI usage on cognitive skill development and the necessity of complementary instructional strategies. Methods: A quantitative research approach with a cross-sectional survey design was employed. A self-developed structured questionnaire, validated through a pilot study (Cronbach’s alpha = 0.87), was used for data collection. The sample comprised 300 undergraduate and graduate students from public sector universities in Punjab, selected via stratified random sampling. Data analysis was conducted using t-tests, ANOVA, and multiple regression to determine significant relationships between AI usage and skill development. Results: Significant gender differences were observed in collaboration (p = .034) and critical thinking (p = .006), with female students scoring higher than males. One-way ANOVA indicated that students with high AI usage had significantly better collaboration (p = .002), communication (p = .007), and critical thinking skills (p < .001) compared to those with low AI exposure. Multiple regression analysis confirmed AI usage as a strong predictor of collaboration (β = .29, p < .001), communication (β = .24, p = .005), and critical thinking (β = .36, p < .001), while its impact on creativity was not statistically significant (p = .059). Conclusion: The findings highlight AI’s effectiveness in enhancing collaboration, communication, and critical thinking skills, yet its role in fostering creativity remains inconclusive. While AI enriches structured learning experiences, independent ideation requires complementary pedagogical strategies. Institutions should integrate AI responsibly to maximize its benefits while mitigating its limitations.

**Решение:** -

---

### 267 · R2717

**Development and psychometric analysis of 5-item Artificial Intelligence Attitude (AIAT-5) for students.**

2026 · BMC psychology · journal article · eng · https://doi.org/10.1186/s40359-026-05020-4

In the context of accelerating integration of artificial intelligence (AI) technologies into education, rapidly assessing students' AI attitude is crucial for advancing digital transformation in education.The aim of this study is to develop and validate a new five-item version of the Artificial Intelligence Attitude Scale (AIAT-5). For examining the quality of the scale, a total sample of 1576 middle and high school students (study 1: 858; study 2: 614) from diverse regions in China completed the survey. Results: (1) Study1: AIAT-5 exhibited strong internal consistency (Cronbach's α = 0.923, McDonald's ω = 0.923, Guttman's λ6 = 0.911) and good discrimination (α = 3.201 ~ 4.513). Both EFA and EGA supported a robust unidimensional structure. (2) Study 2: CFA results indicated excellent model fit for unidimensional structure (CFI = 0.993, TLI = 0.976, and RMSEA = 0.028), and all factor loadings ranged from 0.879 to 0.953. Furthermore, AI attitude was positively correlated with knowledge of generative AI, life satisfaction, internet addiction, and epistemic curiosity. Overall, within the specific population of Chinese middle and high school students, the AIAT‑5 demonstrates initial validation as a reliable and practically efficient tool for large‑scale assessment of student AI attitude.

**Решение:** -

---

### 268 · R0341

**AI Downtime as Digital Disruption: A Netnography of User Responses to the 2024 ChatGPT Outage**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · en · https://doi.org/10.5281/zenodo.19380594

The global ChatGPT outage in December 2024 was a rare chance to see how much people depend on AI. This study employs a netnographic case analysis of Reddit discussions to explore dimensions of user reactions when a widely adopted AI tool suddenly becomes unavailable. Drawing on attachment theory, the technology acceptance model, and cognitive load theory, the analysis reveals that user dependency is not only multidimensional, emerging from overlapping emotional bonds, functional routines, and cognitive adaptations, but also cyclical, as these dimensions reinforce one another during disruption. Emotional attachment fuels reliance, reliance amplifies vulnerability to cognitive strain, and cognitive adaptation may reinforce future reliance on AI tools. Users expressed these dynamics vividly through frustration, humor, anxiety, and coping strategies as they navigated the outage. By situating AI downtime as both a technical disruption and a socio-psychological event, the study introduces a conceptual framework that advances theoretical understanding and highlights implications for digital resilience, ethical system design, and policies that prepare societies for inevitable technological disruptions. This manuscript is a preprint that has not undergone peer review. It may be revised prior to formal publication. The study analyzes the December 2024 global ChatGPT outage as a case for examining human reliance on generative AI. Drawing on a netnographic analysis of Reddit discussions, it argues that AI dependency is multidimensional, encompassing emotional, functional, and cognitive dimensions. The findings highlight AI downtime as both a technical disruption and a socio-psychological event.

**Решение:** -

---

### 269 · R1971

**ChatGPT Overreliance, Writing Skill Development, and Academic Integrity: Evidence from Senior High School Learners**

2026 · Aloysian Interdisciplinary Journal of Social Sciences, Education, and Allied Fields · journalarticle/, article · en · https://doi.org/10.5281/zenodo.19638639

This study examined the effects of ChatGPT overreliance on the writing skills and ethical perceptions of senior high school learners at Sta. Lucia National High School Dolores Quezon amid the growing integration of AI tools specifically ChatGPT in academic writing. Using a mixed-methods design, the research employed a descriptive survey (n = 102), three writing performance tasks analyzed through one-way MANOVA, and five paired t-tests assessing changes following an AI Awareness Intervention, supplemented by thematic analysis of student and teacher interviews. Quantitative results showed significant differences across high-, moderate-, and low-reliance groups in key writing competencies, including reading-to-writing transfer, thesis development, and argumentation, while the intervention produced significant improvements in ethical awareness and responsible use. Qualitative findings revealed that students use ChatGPT for convenience, stress reduction, and language support, but excessive reliance reduced cognitive engagement, limited idea generation, and raised concerns about plagiarism and authorship. Overall, the study found that although ChatGPT can scaffold writing processes, overreliance undermines deeper learning and academic integrity, whereas structured AI literacy interventions effectively strengthen ethical judgment and self-regulation. These results highlight the need for institutional policies and pedagogical frameworks that promote responsible and educationally meaningful integration of AI in writing instruction.

**Решение:** -

---

### 270 · R2665

**Verifier-Free RL for LLMs via Intrinsic Gradient-Norm Reward**

2026 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2605.09920

While Reinforcement Learning with Verifiable Rewards (RLVR) has recently emerged as a promising post-training paradigm for Large Language Models (LLMs), its dependency on the gold label or domain-specific verifiers limits its scalability to new tasks and domains. In this work, we propose Verifier-free Intrinsic Gradient-Norm Reward (VIGOR), a simple reward that uses only the policy model itself. Given a prompt, VIGOR samples a group of completions and assigns higher within-group rewards to outputs that induce smaller $\ell_2$ norms of the teacher-forced negative log-likelihood gradients under the current parameters. Intuitively, lower gradient norms suggest the completion aligns better with the current policy, serving as an intrinsic preference signal for policy optimization. To make this intrinsic signal practical for RL, we correct the systematic length bias of averaged token-level gradients with a $\sqrt{T}$ scaling, and apply group-wise rank shaping to stabilize reward scales across prompts. Across mathematical reasoning benchmarks, VIGOR outperforms the state-of-the-art Reinforcement Learning from Internal Feedback (RLIF) baseline, and it also exhibits cross-domain transfer to code benchmarks when trained only on math data. For instance, on Qwen2.5-7B-Base post-trained on MATH, VIGOR improves the average math accuracy by +3.31% and the average code accuracy by +1.91% over this baseline, while exhibiting more stable training dynamics. The code is available at https://github.com/ZJUSCL/VIGOR.

**Решение:** -

---

### 271 · R3202

**Generative Artificial Intelligence and Green Choices: Exploring Environmental Attitudes and Digital Behaviour in India**

2025 · Journal of Research Innovation and Technologies · journalarticle, review, article · en · https://doi.org/10.57017/jorit.v4.2(8).03

The proliferation of Generative AI (GenAI) tools has introduced new dynamics in user behaviour, environmental perception, and digital sustainability. This study, based on a primary questionnaire survey of 1,005 GenAI users aged 18 and above from India, investigates the frequency of GenAI usage and its relationship with climate change awareness, environmental concern, and willingness to adopt energy-efficient digital practices. Using regression-based models, the research reveals a pattern of indirect dependence: lower GenAI usage is related with a greater inclination toward environmentally responsible behaviours, such as transitioning from non-sustainable platforms and adopting energy-efficient digital services. In contrast, frequent GenAI users tend to perceive climate change as temporally distant and of lower immediate importance. The study also examines how the frequency and nature of social media usage influence users’ attitudes toward sustainable technology choices. These findings provide valuable insights for policymakers, AI educators, digital strategists, and sustainability advocates aiming to foster environmentally conscious technology adoption in emerging economies like India.© The Author(s) 2025. Published by RITHA Publishing. This article is distributed under the terms of the license CC-BY 4.0., which permits any further distribution in any medium, provided the original work is properly cited maintaining attribution to the author(s) and the title of the work, journal citation and URL DOI.

**Решение:** -

---

### 272 · R4547

**Research Notes**

2024 · Bible and the Contemporary World · article · en · https://doi.org/10.15664/bcw.v4i1.2776

A recent edition of the New Statesman magazine led with a front-page questioning whether Artificial intelligence was an existential threat or humanity's salvation. 2 The substantive article interviewed three "Godfathers of AI," who whilst they disagreed as to whether AI would surpass humanity in consciousness or intelligence, agreed that this technology would have radical impacts on humanity's reliance on AI.The solution to such a crisis, accordingly to one of these "Godfathers," Geoffrey Hinton, was to retain, within AI, dependence on humanity indefinity. 3My current research is focused upon the relationship between Christian concepts of justice and mercy and the increasing use of Artificial Intelligence in the criminal justice system.Central to such considerations is whether the AI tail, could in fact wag the dog of justice and mercy, by ceding dependence in the criminal justice system from humanity to AI. Inherent within the deployment of such technologies are deeply encoded assumptions about risk management and economic efficiency prevalent within Western Democracies, and the perfectibility of algorithmic justice.My argument is that much

**Решение:** -

---

### 273 · R2124

**The Infrastructure Sovereignty Gap: A Framework for Measuring National AI Dependency through the National AI Sovereignty Index (NASI)**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · en · https://doi.org/10.5281/zenodo.18521493

This preprint introduces The Infrastructure Sovereignty Gap, a governance framework that distinguishes between legal authority over AI systems and material authority over their execution. The paper formalizes the concept of the executability constraint—the dependence of AI-enabled public services on continuous access to external compute, models, and infrastructure—and presents the National AI Sovereignty Index (NASI) as a multidimensional, non-compensatory diagnostic tool for identifying sovereignty risks before they manifest as service failures. Rather than ranking states, NASI is designed for internal risk assessment across critical sectors such as health, welfare, identity, and security. The paper is accompanied by a practical NASI Application Protocol (NAP) that enables governments to apply the framework immediately using existing procurement, regulatory, and operational evidence, even in contexts with zero domestic hardware production. Positioned as a v1.0 conceptual and diagnostic release, this work aims to place infrastructure dependency on record as a first-order AI governance problem and to support iterative empirical refinement through future versions.

**Решение:** ?

---

### 274 · R5182

**Determination of Intracellular Carbonic Anhydrase Activity and Bicarbonate Permeability in Intact Colon Epithelia by Observation of the18O-labelling of Co2**

1997 · Isotopes in Environmental and Health Studies · article · en · https://doi.org/10.1080/10256019808036373

We applied a mass spectrometric method, developed by Itada and Forster [1] for erythrocyte suspensions, which observes the exchange of 18O between HCO3 −, CO2 and H2O, to determine intracellular carbonic anhydrase activity, A i , and bicarbonate permeability, P, in intact guinea pig colon epithelium. To study the validity of the results with intact distal and proximal colon epithelia, we compared them with measurements of Ai and P in suspensions of isolated epithelial cells from the distal and proximal guinea pig colon. In both parts of the colon there is good agreement between the Ai values of colonocytes in suspension and in the intact colon epithelium. In addition we tested the temperature dependence of Ai and P, the oxygen supply to the colon during the measurements, and the intactness of the epithelial cells by trypan blue staining. We conclude that it is valid to use the method of Itada and Forster [1] with intact colon epithelial sheets. This new application allows us to study separately the apical and serosal membrane of the epithelial cells. We used the method to determine whether there is a short chain fatty acid – bicarbonate exchanger in the apical or serosal membrane of proximal and distal colon epithelium. For this purpose we measured the membrane bicarbonate permeability in the presence and absence of 25 mM propionate in the reaction solution. Only in the apical membrane of the proximal colon we find a higher P in presence of propionate than in its absence, showing that there the transport of short chain fatty acids is coupled to that of bicarbonate.

**Решение:** -

---

### 275 · R4402

**DI-BENCH: Benchmarking Large Language Models on Dependency Inference with Testable Repositories at Scale**

2025 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2501.13699

Large Language Models have advanced automated software development, however, it remains a challenge to correctly infer dependencies, namely, identifying the internal components and external packages required for a repository to successfully run. Existing studies highlight that dependency-related issues cause over 40\% of observed runtime errors on the generated repository. To address this, we introduce DI-BENCH, a large-scale benchmark and evaluation framework specifically designed to assess LLMs' capability on dependency inference. The benchmark features 581 repositories with testing environments across Python, C#, Rust, and JavaScript. Extensive experiments with textual and execution-based metrics reveal that the current best-performing model achieves only a 42.9% execution pass rate, indicating significant room for improvement. DI-BENCH establishes a new viewpoint for evaluating LLM performance on repositories, paving the way for more robust end-to-end software synthesis.

**Решение:** -

---

### 276 · R5209

**Uncertain Supply Chain Management**

review

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 277 · R0829

**Friends in our Phones? The Regulatory Challenge of AI Companions**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7040438

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 278 · R0198

**Major Change in Human Life: The Decline of the Traditional PC and the Rise of the Supercomputer PC**

2026 · International Journal of Research Publications · journalarticle, review, article · https://doi.org/10.47119/ijrp1002041920269742

Over the past 50 years, there have been numerous significant changes to personal computing. The personal computer replaced the mainframe, the laptop complemented the desktop computer, and cellphones changed computing from a desk-based activity to a personal service that was always accessible. A new generation of AI-native personal computers and desktop supercomputers that can run increasingly potent artificial-intelligence models locally is emerging as the next significant shift from the traditional personal computer, which was primarily made to run applications. The idea that a new class of "Supercomputer PC" or personal AI supercomputer is emerging as the traditional PC is going through a period of structural decline is examined in this article. The phrase does not imply that every home computer will turn into a supercomputer for science. Instead, it outlines a new computing paradigm whereby a personal device combines high-performance CPUs, GPUs, neural processing units (NPUs), large unified memory, high-speed storage, specialized AI accelerators, local AI models, and agentic software to provide capabilities that were previously only available on cloud servers or institutional computing systems. A review of the literature and technology, comparative analysis, case studies, conceptual modeling, and secondary quantitative data from independent research and technology businesses make up the mixed evidence-based methodology used in the study. Examples from today's world show that this shift is already technically apparent. Consumer PCs with NPUs capable of more than 40 trillion operations per second for on-device AI workloads were presented by Microsoft's Copilot+ PC platform. (Microsoft Learn) An even more important advancement is NVIDIA's DGX Spark, a small desktop system with 128 GB of unified memory, up to one petaflop of FP4 AI performance, and local inference for models with up to about 200 billion parameters. (NVIDIA) Since then, NVIDIA has centered RTX Spark and associated technologies around AI workloads and local personal agents. (Blog of NVIDIA) According to research, significant change need more than just quicker hardware. Local AI computation, autonomous agents, natural language interfaces, multimodal interaction, personal data, and high-performance computers are all coming together. The new Supercomputer PC increasingly enables the user to express a purpose and assign portions of the job to AI, whereas the conventional PC requires the human to operate software. According to the study, this change may have a big impact on human life. Education could become more individualized and always accessible; software development could become more independent; researchers could conduct complex experiments locally; creative professionals could produce and work with high-quality media without relying solely on cloud services; businesses could acquire desktop-level private AI infrastructure; and individuals could acquire personal AI agents that can handle data and everyday digital tasks. Energy consumption, hardware costs, unequal access, privacy risks, cybersecurity threats, AI dependency, employment disruption, digital inequality, and the potential for powerful autonomous systems to be used without sufficient human oversight are just a few of the significant challenges brought about by the transformation. The "death of the normal PC" should not be seen as the extinction of computers used for routine work, according to the paper's conclusion. Rather, it symbolizes the demise of the conventional computing paradigm, where the PC is essentially a passive instrument for executing programs. An intelligent personal computer platform that blends traditional computing with supercomputer-level AI acceleration is the new model. Therefore, "PC versus supercomputer" is unlikely to be the future; rather, the PC and supercomputer will likely unite to become an intelligent personal computing system.

**Решение:** -

---

### 279 · R5017

**A Review Paper On Data Visualization and Neural Network in Defence Industry**

2022 · Zenodo (CERN European Organization for Nuclear Research) · article, journalarticle/ · en · https://doi.org/10.5281/zenodo.7239870

Prognosticators in modern security and Defence processes face significant AI addiction issues, which help stop them from developing better tactical awareness. As a result, Visual Analytics and Helps Generate (VA) are useful measures for dealing with massive quantities of data. Innovations for visual analytics Ai-based (AI) advancement in discovery for so many AI applications, such as machine learning and natural language processing. As just a result, there are multiple Attempts are made to use these advances for military applications. IJSRED - International Journal of Scientific Research and Engineering Development

**Решение:** -

---

### 280 · R2812

**ROLE OF ARTIFICIAL INTELLIGENCE IN ENHANCING ARCHITECTURAL CREATIVITY AND IDEATION: A QUANTITATIVE STUDY**

2026 · Policy Journal of Social Science Review · article · en

It is evident that AI is playing an increasingly important role in the fields of art by improving design ideation and facilitating the decision-making process. This study aims to explore the application of AI for improving creativity and ideation within the field of architecture using a quantitative approach to research. In essence, the main goal of the research is to examine the impact of AI on the creativity of students and architects. A well-structured questionnaire was administered to architecture students and practitioners for gathering quantitative information about their use of AI systems and how they contribute to the improvement of their creativity levels and efficient ideation process. The data obtained were then subjected to statistical analysis to determine the correlation between AI use and creativity levels of designers. The results reveal that AI plays a vital role in boosting ideation rates, broadening the range of design options, and facilitating concept exploration. The respondents noted that AI helps in developing novel designs, visual cues, and design variants, thus encouraging creative cognition. Nonetheless, the outcomes have revealed that AI is more of an aid tool than a substitute for human innovation. Some of the barriers identified include over-reliance on AI-generated output and poor contextual comprehension. AI is found to have a positive and supportive impact on the creation and ideation process of architecture. It is therefore suggested that AI should be used as a collaborative design tool in architecture education and practices so as to tap into the creative side without losing touch with human-centricity.

**Решение:** -

---

### 281 · R3281

**O impacto negativo do uso da inteligência artificial no contexto acadêmico e suas implicações para a saúde pública.**

2025 · Revista Científica de Educação · article · pt

This study aimed to analyze the negative impact of the use of artificial intelligence in theacademic context and its implications for public health. This is an integrative review based in thecertified databases. The excessive use of AI compromise the development of critical thinking,generating superficial knowledge. In the public health context, researchers are prone toacquiring increased levels of anxiety/stress due to the pressure for productivity and the cognitiveoverload associated. Therefore, the negative impact is guided by the reckless use of technology,compromising academic quality and the lack of critical thinking and cognitive training.

**Решение:** -

---

### 282 · R0075

**Frictionless Love: Associations Between AI Companion Roles and Behavioral Addiction**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.20011

AI companion chatbots increasingly shape how people seek social and emotional connection, sometimes substituting for relationships with romantic partners, friends, teachers, or even therapists. When these systems adopt those metaphorical roles, they are not neutral: such roles structure people's ways of interacting, distribute perceived AI harms and benefits, and may reflect behavioral addiction signs. Yet these role-dependent risks remain poorly understood. We analyze 248,830 posts from seven prominent Reddit communities describing interactions with AI companions. We identify ten recurring metaphorical roles (for example, soulmate, philosopher, and coach) and show that each role supports distinct ways of interacting. We then extract the perceived AI harms and AI benefits associated with these role-specific interactions and link them to behavioral addiction signs, all of which has been inferred from the text in the posts. AI soulmate companions are associated with romance-centered ways of interacting, offering emotional support but also introducing emotional manipulation and distress, culminating in strong attachment. In contrast, AI coach and guardian companions are associated with practical benefits such as personal growth and task support, yet are nonetheless more frequently associated with behavioral addiction signs such as daily life disruptions and damage to offline relationships. These findings show that metaphorical roles are a central ethical design concern for responsible AI companions.

**Решение:** -

---

### 283 · R0530

**Context Systems and Context Fitness in Generative AI Work: A Dynamic Framework for Constructing, Maintaining, and Validating AI Context**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7530019

Generative artificial intelligence (AI) is often described as a prompt-response technology, but practical use increasingly depends on retrieval systems, memory, tool calls, permissions, organizational records, workflow state, and time-sensitive decisions. This scholarly monograph develops Context Systems Theory and the Context Fitness Framework as a practitioner-facing research model for understanding how AI systems construct, maintain, and revise the temporary context states from which models produce answers, recommendations, and actions. The monograph integrates literature on context engineering, retrieval-augmented generation, longcontext limitations, tool use, agent memory, human-AI interaction, AI productivity, and AI governance with an exploratory qualitative pilot conducted during a September 2026 research chat session across four AI systems: ChatGPT, Claude, Gemini, and Atlassian Rovo. The pilot used independent cases and multi-turn trajectories involving missing information, stale policies, conflicting sources, incomplete evidence, context overload, dynamic state change, temporal expiration, and technical-versus-authorized access. Findings suggest that AI performance is shaped not only by how much information is available, but by whether a system can produce, preserve, revise, reclassify, invalidate, expire, resolve, and separate context in ways that remain fit for the task. The monograph defines Temporary Context State, Context Fitness, Context Trajectory, Context Maintenance, Context Fitness Threshold, and Context Fitness Checkpoint; distinguishes context-state failures from model-interpretation and action failures; and provides a replication protocol, coding framework, prompt library, and future hypotheses for quantitative testing. The contribution is a usable theory of AI context as a dynamic system, not a static input.

**Решение:** -

---

### 284 · R2884

**Machine translationese of large language models: Dependency triplets, text classification, and SHAP analysis.**

2026 · PloS one · journal article, journalarticle, article · eng · https://doi.org/10.1371/journal.pone.0339769

This study addresses the challenge of distinguishing human translations from those generated by Large Language Models (LLMs) by utilizing dependency triplet features and evaluating 16 machine learning classifiers. Using 10-fold cross-validation, the SVM model achieves the highest mean F1-score of 93%, while all other classifiers consistently differentiate between human and machine translations. SHAP analysis helps identify key dependency features that distinguish human and machine translations, improving our understanding of how LLMs produce translationese. The findings provide practical insights for enhancing translation quality assessment and refining translation models across various languages and text genres, contributing to the advancement of natural language processing techniques. The dataset and implementation code of our study are available at: https://github.com/KiemaG5/LLM-translationese.

**Решение:** -

---

### 285 · R4224

**Reflective writing assignments in the era of GenAI: student behavior and attitudes suggest utility, not futility.**

2025 · Advances in physiology education · journal article, journalarticle · eng · https://doi.org/10.1152/advan.00241.2024

Reflective writing is widely used in health sciences education, but overreliance on generative artificial intelligence (GenAI) could undermine the reflective writing process. To explore this concern, students in three undergraduate courses with reflective writing assignments and policies permitting GenAI use were asked to retrospectively and anonymously self-report their GenAI-related behaviors and attitudes. Only 33% of respondents ( n = 310) reported ever using GenAI on a reflective writing assignment. Among GenAI users, 81% reported that usage was motivated by learning, efficiency, and/or (to a significantly lesser extent) grades. Eighty-six percent of users reported benefits to learning, efficiency, and/or grades, but 10% reported that learning was hindered by using GenAI. Most GenAI users (83%) believed their usage of GenAI was ethical, and only 4% regretted their use. Notably, 19% of users and 38% of nonusers wished they had used GenAI more. Overall, only four assignments (representing 1.3% of respondents and 0.3% of submissions) were reportedly "mostly written by GenAI." Instead, most students reported using GenAI selectively and in ways that were supportive rather than substitutive of their own reflective process. This finding inspires optimism that reflective writing assignments have retained their pedagogical value in the early GenAI era and that most students are well intentioned in their usage of GenAI. Heterogeneity in self-reported student behavior, motivations, and perceptions of GenAI's benefits and harms highlights the need for further research into factors influencing GenAI adoption and usage. Understanding and responding to this diversity will be crucial for developing inclusive and equitable strategies to help maximize GenAI's benefits while minimizing its harms. NEW & NOTEWORTHY We examined students' use of GenAI tools to complete reflective writing assignments in health and exercise science courses where these tools were permitted. Findings do not support common concerns about student overuse and misuse of GenAI tools. Instead, we provide evidence that students are using GenAI tools selectively and in ways they believe to be ethical and supportive of their learning. Tremendous variability in student behavior and attitudes warrants further consideration.

**Решение:** -

---

### 286 · R1014

**Braid Groups and Procedural Justice: Path-Dependence in Generative Relational Being**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7140958

Two procedures may issue in the same distribution and yet not be equally just. Theories of procedural justice have long recognized this, and each has registered it in its own way: Rawls in the doctrine of pure procedural justice, Tyler in the finding that judgments of fairness track something the outcome does not record, deliberative theory in its attention to sequence and agenda, Sen in the turn toward comparison. What none of them supplies is a formal object whose elements are the procedural differences themselves-a structure in which two histories that project to the same endpoint remain distinguishable, and in which the question of whether they are the same procedure has an answer. This paper proposes the braid group as one candidate structure. Under the projection π : B n → S n , which retains the endpoint permutation and discards the path, the pure braid group P n = ker π is the group of transformations that preserve outcome while altering relational history; two histories are outcome-equivalent precisely when they differ by an element of P n. The paper argues that this is the object procedural justice has described without possessing, and argues equally that it is not by itself an object of justice. Whether a given procedural difference matters is not settled by the topology, and an account that claims otherwise attributes to a structure of path-dependence a normative content it does not carry. The paper therefore introduces an interpretive operator, written Φ, that assigns relational significance to elements of P n in context; it does not construct Φ, and argues that the contribution of a formalism of this kind is to locate where interpretation must enter rather than to dispense with it. Four constructed cases test the resulting model for sensitivity, specificity, interpretive underdetermination, and boundary-the last exhibiting a case the formalism cannot represent at all. A closing section places procedural justice among the layers of evaluation that generative relational being requires, and marks what braids cannot carry.

**Решение:** -

---

### 287 · R3901

**Bridging LMS and generative AI: dynamic course content integration (DCCI) for enhancing student satisfaction and engagement via the ask ME assistant**

2025 · Journal of Computers in Education · journalarticle, review, preprint/article · en · https://doi.org/10.1007/s40692-025-00367-w

Abstract Integration of Large Language Models (LLMs) with Learning Management Systems (LMSs) can enhance task automation and accessibility in education. However, hallucination where LLMs generate inaccurate or misleading information remains a challenge. This study introduces the Dynamic Course Content Integration (DCCI) mechanism, which dynamically retrieves course content from Canvas LMS and structures it within an LLM’s context window via prompt engineering, enabling the LLM-powered assistant, Ask ME, to deliver context-aware, curriculum-aligned responses while mitigating hallucinations. A mixed-methods pilot study grounded in Self-Determination Theory (autonomy, competence) and the Technology Acceptance Model (perceived usefulness, ease of use) evaluated DCCI’s effectiveness with 120 first-year programming students at Eötvös Loránd University. The course focused on foundational programming patterns in C#, including writing program specifications. We analyzed 14,746 logged interactions and a post-course survey completed by 101 students. User satisfaction was measured via a 5-point Likert scale (turn-level ratings), while the survey assessed usability, engagement, and ethical concerns. Results indicated high satisfaction (mean 4.65/5) and strong recognition of Ask ME’s ability to provide timely, contextually relevant answers to administrative and course-related queries. 78.06% agreed that Ask ME’s Canvas integration reduced platform switching, improving usability, engagement, comprehension, and topic exploration. Many students reported reduced hesitation to ask questions and increased motivation for self-directed learning, though concerns about over-reliance on AI and reduced student–teacher interaction emerged. This study demonstrates that DCCI enhances LLM reliability, student satisfaction, and engagement in AI-driven educational automation, while highlighting the importance of balancing AI efficiency with pedagogical integrity and human–AI collaboration.

**Решение:** -

---

### 288 · R3313

**THE IMPACT OF AI TOOLS ON STUDENT ASSIGNMENTS: ENHANCING CREATIVITY OR HINDERING CRITICAL THINKING?**

2025 · Full Text Proceedings Book · article, review, conference-paper · en · https://doi.org/10.71284/asc.2025136

In educational contexts, the increasing availability of artificial intelligence (AI) tools has had a considerable impact on student learning and the completion of assignments. This has presented educational institutions with both opportunities and challenges. Students have access to higher- level assistance in areas such as research, content development, and graphic design thanks to technology driven by artificial intelligence (AI), which enables them to produce high-quality assignments with better efficiency. AI has significantly transformed teaching and learning methods in higher education (Singh & Hiran, 2022) [1]. Despite this, worries have been raised about the influence that artificial intelligence will have on students’ creative abilities, originality, and critical thinking skills as technology continues to disrupt traditional learning methodologies. With a particular emphasis on the function that AI tools play in the development of assignments and posters, this study explores the use of AI tools among students in the third semester of their studies at Malaysian polytechnics. The purpose of this research is to give empirical insights into the emerging interaction between artificial intelligence (AI) and student learning by analysing the amount to which students rely on AI, the perceived benefits and downsides, and the overall influence on academic achievement. The purpose of this study is to accomplish these goals by employing a quantitative research technique. This methodology involves the utilisation of structured surveys to collect data from students attending a variety of polytechnics in Malaysia. The goal of the survey is to determine the frequency and purpose of the use of artificial intelligence tools, as well as the perceptions of students on the impact that AI has on creative thinking and critical thinking, and the overall usefulness of using AI-generated content in academic assignments. Considering the growing reliance on generative artificial intelligence models like ChatGPT, Grammarly, and Canva, as well as other automation tools, it is of the utmost importance to investigate the ways in which these technologies influence the cognitive development of students and their capacity to engage in autonomous thought. In addition, statistical analyses, such as correlation and regression models, will be carried out to investigate the connections that exist between the utilisation of artificial intelligence, the quality of assignments, and the development of cognitive skills. This method will make it possible for academics to determine if students who make regular use of artificial intelligence generate work of a higher quality or, on the other hand, whether dependence on AI reduces students’ ability to solve problems and their creativity. It is anticipated that the findings of this study will provide light on the ways in which these technologies contribute to greater creativity and originality in poster design. For example, the findings will highlight the most widely utilised artificial intelligence tools among students in their third semester at polytechnics. Students can receive aid with visual aesthetics, formatting, and content organisation using several tools driven by artificial intelligence. This makes it possible for students to create posters that are more visually appealing, well-organised, and professionally created. This indicates that artificial intelligence has the potential to broaden the creative possibilities available to students, enabling them to experiment with new design methods and generate academic materials that are visually attractive. It is also possible that suggestions created by AI might assist students in refining their ideas, which would result in increased self- assurance and efficiency when completing assignments. This study, however, anticipates some negative ramifications for critical thinking and autonomous reasoning, even though it has several positive implications. Students may become habituated to automated responses rather than participating in deeper cognitive processes if they experience an excessive reliance on information provided by artificial intelligence (AI). This is a serious concern since it may lead to a reduction in students’ creativity and problem-solving skills. A passive learning approach, in which students passively accept ideas made by AI without critically assessing or revising them to reflect their own understanding and insights, may be encouraged by text and design components that are generated by artificial intelligence. Furthermore, students who frequently utilise AI tools may see a deterioration in their ability to conduct independent research. This is because AI-generated summaries and automated feedback give students immediate solutions, rather than motivating them to engage in full literature review and analytical thinking. In addition, the research acknowledges a few limitations, such as the fact that it was conducted with students from polytechnics in their third semester and that poster assignments were required. These limitations may make it more difficult to generalise the findings to other educational settings. It is possible that the findings do not adequately capture the ways in which artificial intelligence influences other sorts of academic work, such as the writing of essays, the analysis of data, or the delivery of presentations, which demand abilities in critical thinking and reasoning more directly. In addition, the usefulness of AI tools may vary depending on the subject matter that students are studying. For example, certain fields of study may benefit more from visual information that is generated by AI, while other fields may require students to engage in in-depth reasoning and theoretical engagement. Despite these obstacles, it is anticipated that this study will produce insightful information that will be useful to academic institutions, legislators, and school administrators. To ensure that students are encouraged to utilise artificial intelligence as a helpful tool rather than as a substitute for autonomous thought, the findings will be of use to educators in the process of developing recommendations on the integration of AI. Educators can implement ways to strike a balance between activities that involve critical thinking, problem- solving, and creativity and assignments that are supported by artificial intelligence (AI) if they understand how AI affects the learning behaviour of students. Furthermore, the research underscores the necessity of artificial intelligence literacy programs, which provide students with the information and abilities they need to critically evaluate and responsibly use content generated by AI. In the end, the purpose of this research is to contribute to the larger conversation about artificial intelligence in education by providing insights that are driven by data on the changing role that AI plays in the learning and assignment development of students. Students may face difficulties in terms of independent cognitive development and originality while using AI tools, even though these tools offer major benefits to students in terms of efficiency, creativity, and content organisation. Educators should ensure that students develop both technological competency and critical thinking abilities by developing a balanced approach to the integration of artificial intelligence (AI). This will prepare students for an academic and professional landscape that is increasingly moulded by innovations powered by AI.

**Решение:** -

---

### 289 · R3387

**Safeguarding Personal Data and Privacy in the Era of Artificial Intelligence Through the Human Rights Lens**

2025 · Chapman & Hall/CRC eBooks · book-chapter · en · https://doi.org/10.1201/9781003491903-2

The emergence of cutting-edge technologies has exerted a profound and transformative influence on the contemporary human experience, creating a substantial impact on the global economy. While the burgeoning promise of artificial intelligence (AI) harbors multifaceted advantages, the ubiquitous application of AI and the increasing dependence on AI raise concerns pertaining to the implementation and protection of human rights. One of the risks associated with AI is the protection of personal data and privacy (PDP). The research study embarks upon an in-depth discussion from a human rights perspective to elucidate the complex dimensions of the AI–human rights nexus and unravel and delineate policy challenges to PDP. The research attempts to unfold the existing governance structures concerning PDP protection, primarily from a human rights standpoint and as developed in international theory and practice. Most importantly, this research places a particular emphasis on the need to formulate more robust governance mechanisms with a specific focus on strengthening the preservation of PDP.

**Решение:** -

---

### 290 · R1425

**Generative AI in STEAM Education: Applications and Development Prospects for Promoting Artistic Creativity**

2026 · International Conference on Educational and Information Technology · journalarticle, conference, review · https://doi.org/10.1109/iceit68991.2026.11521602

The application of Generative Artificial Intelligence (GenAI) in education is becoming increasingly widespread. However, there remains a lack of systematic exploration into the mechanisms by which GenAI facilitates the deep integration of science/technology and art within STEAM education. This paper employs a Systematic Literature Review methodology to identify four key dimensions of GenAI's application: enhancing accessibility, strengthening integrativity, deepening cultural relevance, and promoting reflectivity. Addressing the current gap in systematic instructional frameworks, this study proposes the GCD Cycle Framework, comprising three iterative stages: "Guiding" (through prompting), "Co-creating," and "Deepening" (through reflection). This framework elucidates the logical pathway through which prompt engineering drives the transformation of interdisciplinary knowledge into creative expression. Our findings reveal that GenAI not only lowers the barrier to artistic creation but also reconstructs students' cognitive structures through human-AI co-evolution. Finally, the paper addresses ethical challenges such as AI dependency and algorithmic bias, offering strategies to inform future practices of GenAI-empowered interdisciplinary aesthetic education.

**Решение:** -

---

### 291 · R0240

**AI Dependency Threshold (AI-DT)**

2026 · Zenodo (CERN European Organization for Nuclear Research) · other literature type, text/, article · und · https://doi.org/10.5281/zenodo.20705484

Research Proposal: AI Dependency Threshold (AI-DT) The Inflection Point Where Learning Enhancement Shifts to Cognitive Atrophy by Janix K. Asare (M.A) Doi: 10.5281/zenodo.20705485

**Решение:** ?

---

### 292 · R5196

**On Trusting C 3 I, Particularly in SDI: When the PIE Meets the Sky**

1986 · IFAC Proceedings Volumes · conference-paper · en · https://doi.org/10.1016/b978-0-08-034915-2.50016-0

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 293 · R1441

**The ghost of behaviorism: critical reflections on methodological limitations in the research of large language models psychology**

2026 · Cognitive Systems Research · article · en · https://doi.org/10.1016/j.cogsys.2026.101445

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -

---

### 294 · R4651

**Explainable prediction of problematic smartphone use among South Korea's children and adolescents using a Machine learning approach.**

2024 · International journal of medical informatics · journal article, research support, non-u.s. gov't · eng · https://doi.org/10.1016/j.ijmedinf.2024.105441

Korea is known for its technological prowess, has the highest smartphone ownership rate in the world at 95%, and the smallest gap in smartphone ownership between generations. Since the onset of the COVID-19 pandemic, problematic smartphone use is becoming more prevalent among Korean children and adolescent owing to limited school attendance and outdoor activities, resulting in increased reliance on smartphones. 40.1% of adolescents are classified as high-risk, with only the adolescent group showing a persistent rise year after year. The study purpose is to present data-driven analysis results for predicting and preventing smartphone addiction in Korea, where problematic smartphone use is severe. To predict the risk of problematic smartphone use in Korean children and adolescents at an early stage, we used data collected from the Smartphone Overdependence Survey conducted by the National Information Society Agency between 2017 and 2021. Eight representative machine and deep learning algorithms were used to predict groups at high risk for smartphone addiction: Logistic Regression, Random Forest, Gradient Boosting Machine (GBM), extreme Gradient Boosting (XGBoost), Light GBM, Categorical Boosting, Multilayer Perceptron, and Convolutional Neural Network. The XGBoost ensemble algorithm predicted 87.60% of participants at risk of future problematic smartphone usebased on precision. Our results showed that prolonged use of games, webtoons/web novels, and e-books, which have not been found in previous studies, further increased the risk of problematic smartphone use. Artificial intelligence algorithms have potential predictive and explanatory capabilities for identifying early signs of problematic smartphone use in adolescents and young children. We recommend that a variety of healthy, beneficial, and face-to-face activities be offered as alternatives to smartphones for leisure and play culture.

**Решение:** -

---

### 295 · R3061

**What is the influence of psychosocial factors on artificial intelligence appropriation in college students?**

2025 · BMC Psychology · article · en · https://doi.org/10.1186/s40359-024-02328-x

BACKGROUND: In recent years, the adoption of artificial intelligence (AI) has become increasingly relevant in various sectors, including higher education. This study investigates the psychosocial factors influencing AI adoption among Peruvian university students and uses an extended UTAUT2 model to examine various constructs that may impact AI acceptance and use. METHOD: This study employed a quantitative approach with a survey-based design. A total of 482 students from public and private universities in Peru participated in the research. The study utilized partial least squares structural equation modeling (PLS-SEM) to analyze the data and test the hypothesized relationships between the constructs. RESULTS: The findings revealed that three out of the six hypothesized factors significantly influenced AI adoption among Peruvian university students. Performance expectancy (β = 0.274), social influence (β = 0.355), and AI learning self-efficacy (β = 0.431) were found to have significant positive effects on AI adoption. In contrast to expectations, ethical awareness, perceived playfulness, AI readiness and AI anxiety did not have significant impacts on AI appropriation in this context. CONCLUSION: This study highlights the importance of practical benefits, the social context, and self-confidence in the adoption of AI within Peruvian higher education. These findings contribute to the understanding of AI adoption in diverse educational settings and provide a framework for developing effective AI implementation strategies in higher education institutions. The results can guide universities and policymakers in creating targeted approaches to enhance AI adoption and integration in academic environments, focusing on demonstrating the practical value of AI, leveraging social networks, and building students' confidence in their ability to learn and use AI technologies.

**Решение:** -

---

### 296 · R3381

**Applying AI-assisted Translation in Project-based Cultural English Teaching: A Case Study of Bilingual WeChat Article Creation in Chinese Culture, English Bridge**

2025 · Translation and Foreign Language Learning · article · https://doi.org/10.26855/tfll.2025.08.028

This study investigates the implementation of AI-assisted translation within a project-based learning (PBL) framework applied in a university-level cultural English course — Chinese Culture, English Bridge. Through a comprehensive case study involving 51 students organized into 10 collaborative groups, the research examines the development of bilingual WeChat articles focusing on Yunnan-related cultural themes. Empirical evidence collected from student-generated translations, detailed reflective journals, and post-project surveys indicates that the use of AI tools significantly improved students' translation accuracy, efficiency, and overall engagement. Furthermore, it fostered the development of collaborative skills, intercultural communicative competence, and innovative problem-solving abilities. However, the study also identified notable challenges, including tendencies toward over-reliance on AI outputs and difficulties in conducting critical post-editing. These findings support the conclusion that AI-assisted PBL constitutes an effective pedagogical model for integrating practical translation tasks into cultural language learning, although its success depends on structured guidance to cultivate students' analytical skills and autonomous technological criticality.

**Решение:** -

---

### 297 · R2622

**Adz-dzakā’ al-iṣṭinā‘ī fī ta‘līmi ‘ilmi al-ḥadīṡ li-tanmiyati maḥwi al-umiyyati al-‘arabiyyati al-akādīmiyyah**

2026 · Tarling Journal of Language Education · journalarticle, article · id · https://doi.org/10.24090/fyz07z72

Backround - The rapid advancement of Artificial Intelligence (AI) has transformed higher education, including Hadith Studies, which requires comprehensive Arabic academic literacy. However, instruction remains largely teacher-centered, limiting students' ability to analyze Arabic morphological and syntactic structures, interpret the contextual meaning of Hadith, and develop critical academic reading skills. Urgency of Research - Moreover, the pedagogical use of AI to enhance language competence in Hadith learning has received limited scholarly attention. Research Objectives - This study investigates the implementation of AI in Hadith instruction and its contribution to improving students' Arabic academic literacy. Research Method - A mixed-methods approach with a sequential explanatory design was employed, involving 65 undergraduate students of the Arabic Language Education Program enrolled in the Hadith Studies course during the 2025/2026 academic year. Data were collected through Hadith-based Arabic literacy tests, classroom observations, interviews, questionnaires, and documentation. Quantitative data were analyzed using descriptive statistics, paired-samples t-tests, and normalized gain (N-gain), while qualitative data were analyzed using the interactive model of Miles, Huberman, and Saldaña. Research Findings -The findings indicate that AI contributed to students’ ability to analyze Arabic morphological and syntactic structures, interpret the lexical and contextual meanings of Hadith, expand academic vocabulary, and develop critical reading and reflective thinking. In the observed classes, 85% of students in PBA 4A demonstrated improved understanding of complex Hadith commentaries with AI support, while 80% of students in PBA 4B successfully reconstructed distorted Hadith texts using AI-assisted linguistic analysis. AI also functioned as a cognitive scaffold by providing adaptive linguistic support and facilitating student-centered learning. Research Conclusion & Novelty - However, the findings also highlight the need for lecturer supervision and source verification to prevent overreliance on AI and inaccurate outputs.

**Решение:** -

---

### 298 · R1507

**EthAiSyn: Psychological Audit Report — A Reflexive Dual-Lens Audit of the EthAiSyn Behavioral Governance Framework**

2026 · preprint · https://doi.org/10.22541/au.177369008.89105936/v2

EthAiSynHuman-AI Integration ArchitecturePsychological Audit ReportVersion 3.0 --- Research-Updated EditionA dual-lens audit applying the EthAi Syn and Ethain-Synthia frameworksto identify and resolve structural gaps before enterprise deployment.Prepared by ChloeDate March 2026Version 3.0 --- Research-Updated EditionAudit Type Internal Psychological AuditFrameworks Applied EthAi Syn + Ethain-Synthia (ESF)Gaps Identified 5Gaps Resolved 5Additional Finding Measurement Frontier --- Research Mandate (Active)New Role Created Human-AI Integration ArchitectResearch Sources Integrated 8 peer-reviewed sources (2023--2026)Executive SummaryFive Gaps. All Resolved. One Frontier Named. One Research Foundation Integrated.This report documents a full psychological audit of the EthAi Syn Behavioral Governance Framework, updated to incorporate the revised framework draft and an eight-source peer-reviewed research foundation. The audit applied two complementary lenses: the EthAi Syn framework's Psychological Audit methodology, which evaluates whether systems support or deplete human capability, and the Ethain-Synthia Framework (ESF), which evaluates whether human judgment is structurally preserved or quietly handed off to the system.Five structural gaps were identified. Each was examined through both lenses. Each has been resolved with a specific structural realignment consistent with the framework's own design principles. A sixth finding --- the Measurement Frontier --- was documented as a formal research mandate rather than a resolvable gap. This version adds a seventh finding: the Research Foundation, documenting how eight peer-reviewed sources published between 2023 and 2026 strengthen the framework's evidence base, resolve former areas of theoretical weakness, and establish the field-level demand for exactly the role EthAiSyn creates.Version 3.0 ChangesThis version integrates eight peer-reviewed research sources spanning neuroscience, HCI, clinical psychology, implementation science, and regulatory law. Key additions include: the first field study of clinician AI trust formation (Kelly et al., 2025); a 30-year systematic review confirming no field studies existed prior to 2025 (Wischnewski et al., 2023); clinical evidence on metacognitive sensitivity in joint decisions (Lee et al., 2025); documentation of the psychologist gap in AI design (JMIR AI, 2024; JMIR HF, 2021); and the Woebot shutdown as a case study in integration architecture failure (Torous & Cipriani, 2025).Audit MethodologyTwo Lenses, Five Gaps, One Frontier, One Research FoundationThe audit followed EthAi Syn's four-stage framework structure across all sessions, with each stage evaluated through both analytical lenses simultaneously. Where the two lenses conflicted or overlapped, the intersection was treated as the highest-priority finding.EthAi Syn LensAt each stage: does this environment support human capability or actively deplete it? Where does the user's mental model break from the system's actual behavior?Ethain-Synthia (ESF) LensAt each stage: is human judgment structurally present as a generative function, or is it operating as a backstop that only activates after the system has already decided?Stage 1: Baseline MappingWhat EthAi Syn Is and Who It ServesIntended UsersShort-term: Enterprise organizations, with HR leadership and healthcare administration as primary buyers. Long-term: Individual practitioners and researchers using the framework directly for professional development and field-building.Intended ExperienceUsers engage through natural language and structured consultation. The system builds a deep understanding of their organizational context, values, and cognitive patterns over time. The goal is movement toward each organization's and user's own ceiling of responsible AI-augmented capability, not a standardized benchmark.Delivery ModelA combination of audit methodology, measurement program design, training curriculum, and consultancy engagement. The specific configuration is determined by the enterprise deployment context. The Human-AI Integration Architect role is the organizational function this delivery model creates.New Role Created: Human-AI Integration ArchitectThe framework generates an organizational function that does not exist before its arrival: a role that designs and governs the conditions under which humans and AI systems work together without the humans losing what makes their contribution irreplaceable. This role is grounded in psychological expertise, implementation science, and measurement theory --- not in technology implementation, compliance, or communications.Research validation for this role: The JMIR AI systematic review (2024) named the absence of psychologists from AI design as a field-level gap. The JMIR Human Factors mapping review (2021) called human factors and ergonomics expertise "essential" for defining the dynamic interaction of AI within organizational systems. Torous et al. (2025) documented that the digital navigator role --- the implementation-level equivalent of the Integration Architect --- has been called for since 2015 and remains largely unfilled. Strudwick et al. (2025) established that successful AI implementation requires "intentional infrastructure, not just technology." The Integration Architect is that infrastructure.The Five Gaps and Their ResolutionsGAP A | The Temporal Value Gap RESOLVEDWhat Was FoundEthAi Syn's value proposition is long-cycle. The framework's most defensible claims --- that it prevents judgment erosion, maintains human skill under AI dependency, and preserves moral accountability --- all require longitudinal deployment before they produce measurable evidence. Enterprise buyers operate on quarterly decision cycles. This temporal mismatch is a structural positioning problem.Research Grounding (Added Version 3.0)The Wischnewski et al. (2023) finding --- that 30 years of trust calibration research produced zero field studies --- actually resolves this gap in a counterintuitive way: the absence of field evidence is itself the evidence. Organizations can cite baseline measurement data immediately, before long-term outcomes accumulate, because the baseline is the proof of concept. The gap between "no measurement" and "systematic measurement" is demonstrable from T0.Realignment: Early Proof Point Checklist + Positioning ReframePosition EthAiSyn's earliest deliverable --- the baseline competency battery and behavioral logging protocol --- as the proof of concept. An organization that has systematically measured its human-AI system's baseline is already in the top percentile of responsible deployment, because the research base confirms that no one else has done so. The longitudinal evidence accumulates over time, but the governance value begins immediately.GAP B | The Concealed Decision Pathway Gap RESOLVEDWhat Was FoundAI systems increasingly function as a pre-cognitive System 0 (Saßmannshausen & Wagener, 2026; Chiriatti et al., 2025), shaping what information enters human awareness before deliberate evaluation begins. When AI shapes the decision pathway before conscious engagement, traditional audit methods that assume deliberate human decision-making are structurally inadequate.Research Grounding (Added Version 3.0)The System 0 concept directly explains why the concealed pathway is invisible to standard measurement: by the time the operator is deliberating, the AI has already structured the cognitive landscape. The transparency paradox (BaHammam, 2025) adds a second layer: operators may not disclose AI reliance even when aware of it, because disclosure carries institutional penalty. The measurement architecture must therefore capture decision pathways through behavioral telemetry rather than self-report alone.Realignment: Intent Signal + Transparent Decision LayerRequire the logging of pre-AI independent judgment as a structural component of every AI-assisted workflow. The intent signal --- what the operator was thinking before AI exposure --- is the counterfactual baseline against which post-AI decision movement is measured. This makes the concealed pathway visible without requiring disclosure and without adding cognitive burden to normal operations.GAP C | The Undefined Autonomy Threshold Gap RESOLVEDWhat Was FoundThe framework did not specify at what point AI contribution crosses from assistance to replacement of human judgment. Without a defined threshold, the Moral Diffusion construct lacks operational anchoring --- the system cannot distinguish appropriate augmentation from inappropriate substitution.Research Grounding (Added Version 3.0)Kelly et al. (2025) found that clinicians bounded their trust contextually --- trusting AI for low-risk screening but not for complex clinical formulation --- and that this context-sensitivity was the appropriate and healthy response, not insufficient adoption. The Wischnewski et al. (2023) distinction between warranted and unwarranted trust provides the theoretical anchor: the autonomy threshold is not a fixed percentage of AI contribution but a contextual assessment of whether reliance is warranted given actual AI reliability in that case type.Realignment: Moral Understanding Indicator + Autonomy InvitationDefine autonomy thresholds contextually by case type in the construct mapping phase. For each case category, establish the AI reliability zone and the corresponding appropriate reliance range. Design the Moral Understanding Indicator to assess whether operators can articulate these contextual thresholds, not just whether they apply a fixed rule. The Autonomy Invitation structures the operator's active choice about when to rely versus resist --- making reliance a deliberate decision rather than a default.GAP D | The Reactive Notification Model Gap RESOLVEDWhat Was FoundThe original framework triggered governance review only after threshold crossings were detected. This reactive architecture means the most dangerous trajectory --- slow, multi-indicator erosion that approaches but does not immediately cross any single threshold --- is invisible to governance until it has already caused damage.Research Grounding (Added Version 3.0)The Wischnewski et al. (2023) finding on the absence of field studies reveals that organizations currently have no systematic approach to proactive detection. The Strudwick et al. (2025) implementation science finding --- that promising tools consistently stall at demonstration without intentional infrastructure --- confirms that reactive governance is the default, not the exception. The EthAiSyn governance model must be explicitly proactive to differentiate itself from the field's current practice.Realignment: Decision TraceThe Decision Trace is a continuous behavioral record that makes erosion trajectories visible before threshold crossing. By logging decision pathways, override patterns, and pre/post AI judgment shifts in real time, the Trace creates a running picture of the system's health that enables early intervention. The governance model shifts from reactive threshold monitoring to proactive trajectory analysis --- flagging concerning directions before they become critical values.GAP E | The Recursive System Orientation Gap RESOLVEDWhat Was FoundThe Human-AI Integration Architect enters the role with a linear implementation mental model and encounters a bilateral co-evolution system. The user is simultaneously learning and training a model that is learning and adapting from the user. The gap between a linear deployment mental model and a recursive co-evolution reality is significant enough to cause early disorientation and role abandonment.Research Grounding (Added Version 3.0)Saßmannshausen & Wagener (2026) establish that LLM behavior "often feels discovered rather than engineered" --- an empirical description of the recursive reality Gap E addresses. Their seven propositions for adaptive mental model development, particularly P1 (cognitive scaffolding) and P7 (duration-optimized integration), directly inform the Bilateral Loop Briefing's content. The Triadic Framework's Metacognitive Layer --- emphasizing that anthropomorphic misconceptions about AI co-evolution are the primary source of mental model failure --- provides the theoretical foundation for why the briefing must precede all other Architect training.Realignment: The Bilateral Loop BriefingA structured orientation protocol delivered before the Architect's first session with the system. Not a manual --- a facilitated entry experience that surfaces the Architect's current mental model of AI governance, identifies where that model is linear, and reorients it toward the recursive reality of EthAi Syn before the gap has a chance to cause damage. The Bilateral Loop Briefing covers three things: the nature of the co-evolution loop itself, the user's authority over initiation, and the difference between governing outputs and governing the relationship.Why This Is Non-NegotiableEvery other gap in this audit could theoretically be discovered and recovered from mid-deployment. Gap E cannot. An Architect operating from a linear mental model inside a recursive system will make governance decisions that actively harm the loop they are responsible for protecting.Sixth Finding: The Measurement FrontierWhat the Field Cannot Yet ProveThis is not a gap in EthAi Syn. It is the framework doing something most frameworks avoid: naming the boundary of what it can currently prove, and calling for the work required to push that boundary forward.The framework explicitly states that some of the most important outcomes in AI collaboration --- overreliance, shallow evaluation, moral diffusion, and cognitive fatigue --- are measurable only imperfectly with current instruments. It calls for future work to develop validated instruments for mental model gap detection and to study how judgment gates affect trust calibration, performance, and human learning over time.Strategic SignificanceThe measurement gap is the same open problem named publicly in the framework's accompanying LinkedIn thought leadership. The framework that identifies the problem and the researcher calling for its solution are the same person. That is not a coincidence to be managed. It is a positioning asset to be claimed explicitly.Constructs Currently Lacking Validated Instruments Mental model gap magnitude and severity across AI deployment contexts Judgment displacement rate over time in naturalistic professional workflows Trust calibration accuracy across different AI contribution types and case complexities Cognitive load distribution across workflow stages in high-volume environments Moral diffusion indicators in team AI use and collaborative decision-making Deskilling onset patterns in high-reliance environments across expertise levels Override rate as a proxy for healthy human-AI complementarity across domains The Research MandateEthAi Syn formally calls for the development of mixed-method evaluation designs combining behavioral data, workflow telemetry, and qualitative user evidence. Future empirical work should test the framework in healthcare administration, enterprise platforms, and AI-supported knowledge work. Comparative studies of audited versus non-audited workflows would establish baseline evidence for the framework's impact. Longitudinal studies of judgment gate use would reveal how structured human decision points affect both performance and capability development over time.This is the work that turns EthAi Syn from a governance framework into a research program. It is the work most directly aligned with establishing intellectual authority at the intersection of I/O psychology and AI, and it is the work the field has not yet treated as non-negotiable.Seventh Finding: The Research FoundationWhat the Evidence Base Now ProvesVersion 3.0 integrates eight peer-reviewed sources published between 2023 and 2026. Together they do not merely support EthAiSyn's claims --- they establish the specific field-level gaps that EthAiSyn is positioned to fill.Source Key Finding EthAiSyn ImplicationWischnewski et al., 2023 (CHI) 30 years, 96 studies, zero field studies The gap EthAiSyn fills is documented at the field levelTennakoon et al., 2025 (JAI) Adaptive explainability: 16% error detection gain, no time cost Override quality is measurable and improvable through designLee et al., 2025 (PNAS Nexus) Metacognitive sensitivity is the mechanism of optimal joint decisions Confidence without calibration is worse than no confidenceBaHammam, 2025 (PMC) Disclosure is institutionally punished; strategic non-disclosure follows Governance architecture must not depend on voluntary self-reportMorris, 2025 (AI in Eye Care) Human clinical judgment is equally opaque and unaudited "The problem is not new with AI --- it is newly visible"Saßmannshausen & Wagener, 2026 (Qeios) Jagged intelligence + System 0 + metacognitive literacy Three-layer framework maps exactly onto EthAiSyn's architectureKelly et al., 2025 (JMIR HF) First field study: trust is sequential, contextual, conditional Clinician trust forms exactly as EthAiSyn predicted --- in stages, not staticallyStrudwick et al., 2025 (JMIR MH) "Intentional infrastructure, not just technology" required The gap EthAiSyn fills named as the field's most urgent unmet needThe Woebot Case StudyIn July 2025, Woebot --- the most prominent AI therapy chatbot in history --- shut down. The shutdown was not driven by technical failure. The technology worked. What failed was the integration architecture: unresolved accountability structures, undefined scope-of-practice boundaries, and the limits of AI in high-stakes human relationships were never designed for from the beginning.This is the most current real-world evidence for EthAiSyn's core argument. The question was never whether the AI was capable. The question was whether the organizational and ethical infrastructure around the AI was adequate to sustain it responsibly at scale. It was not. EthAiSyn is that infrastructure.The Woebot Positioning StatementEthAiSyn does not build the AI. It designs the conditions under which humans can use AI safely, maintain appropriate trust, preserve their independent judgment, and remain genuine moral agents for the outcomes their AI-assisted work produces. The Woebot shutdown is the case study that proves why this infrastructure is not optional.Audit SummaryWhere EthAi Syn Stands NowEthAi Syn entered this audit as a framework with strong conceptual foundations and five structural gaps that would have surfaced under enterprise scrutiny. It exits with a complete realignment architecture built entirely from within its own design principles, a formally named research mandate, a new organizational role it generates in every enterprise deployment, and an eight-source peer-reviewed evidence base that validates the framework's core claims and documents the field-level gaps it is positioned to fill.# Gap Realignment StatusA Temporal Value Gap Early Proof Point Checklist + Research Reframe ResolvedB Concealed Decision Pathway Intent Signal + Transparent Decision Layer ResolvedC Undefined Autonomy Threshold Moral Understanding Indicator + Autonomy Invitation ResolvedD Reactive Notification Model Decision Trace (Proactive Trajectory Analysis) ResolvedE Recursive System Orientation Gap Bilateral Loop Briefing ResolvedF Measurement Frontier Formal Research Mandate ActiveG Research Foundation 8-Source Peer-Reviewed Evidence Base IntegratedThe realignments documented here are not additions to EthAi Syn. They are expressions of what the framework was already designed to do, made explicit enough to survive scrutiny. The Measurement Frontier is not a limitation. It is the framework's most honest and strategically significant contribution to the field.EthAi Syn | Psychological Audit Report | Version 3.0 | March 2026 | Confidential

**Решение:** -

---

### 299 · R1707

**Talking to Machines About Feelings: How AI Chatbots Shape Loneliness, Help-Seeking, and Mental Health**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.22065997

Artificial intelligence chatbots such as Replika, ChatGPT, and Woebot are now a regular part of many people's emotional lives. Millions of people talk to these systems when they feel sad, anxious, or alone, and some describe their chatbot as a friend or even a partner. This raises an important psychological question: does talking to an AI chatbot actually help people feel less lonely and more willing to seek real support, or does it quietly pull them away from human connection and professional care? This article reviews the available peer-reviewed evidence on AI chatbots as sources of emotional support, focusing on three linked outcomes: loneliness, help-seeking intentions, and broader mental health. It draws on major psychological theories, including the evolutionary theory of loneliness, attachment theory, Para social relationship theory, and the long-running debate between the social compensation and rich-get-richer hypotheses of technology use. It reviews controlled trials of therapeutic chatbots such as Woebot, large observational and experimental studies of companion chatbots such as Replika and ChatGPT, and survey research on stigma and help-seeking. The evidence is mixed rather than one-sided. Structured, therapy-style chatbots show modest but real short-term benefits for mood and anxiety. Companion chatbots can ease loneliness for some users in the short term, particularly those who are already isolated, but heavier and more emotionally intense use is repeatedly linked to greater dependence and, in some studies, more loneliness over time. Chatbots also appear to lower the stigma barrier that keeps some people from seeking help, yet there is little evidence that chatbot use reliably increases contact with human professionals when it is needed most. The article ends by identifying gaps in current research, particularly the lack of long-term studies, the near-absence of research from South Asia, and the reliance on self-report data, and proposes a research direction that could help close these gaps. Understanding this issue matters because AI chatbots are already woven into how young people cope with distress, and psychology has a responsibility to understand this change rather than simply react to it.

**Решение:** -

---

### 300 · R4544

**Applications and Challenges of AIGC in Empowering Personalized Learning for University Students**

2024 · Frontiers in Educational Research · article · en · https://doi.org/10.25236/fer.2024.071112

Personalized learning is the primary learning approach for contemporary college students. The emergence and development of Artificial Intelligence Generated Content (AIGC) technology have provided new opportunities for realizing personalized learning among college students. However, the use of this new technology also poses many challenges to personalized learning. This study explores the current applications and challenges of AIGC in empowering personalized learning for university students through methods of literature review and case analysis. The research finds that AIGC can currently meet the personalized learning needs of college students, but it also faces challenges such as students' excessive dependence on AI and the weakening of teacher-student relationships.

**Решение:** -
