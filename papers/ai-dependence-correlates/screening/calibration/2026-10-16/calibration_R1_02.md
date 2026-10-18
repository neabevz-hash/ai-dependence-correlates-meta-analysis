# Калибровка вслепую, часть 2

Калибровка вслепую, часть 2: записи 151–300 из 400. Это случайные 400 записей из 5056 в списке к отбору финального поиска 2026-10-16 (зерно 20261017, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

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

### 151 · R0521

**The Effects of AI-Use-Related Individual Characteristics on Work Efficiency in Design Practice -The Mediating Role of AI Dependency**

2026 · Journal of Communication Design · article, journalarticle, journal-article · und · https://doi.org/10.25111/jcd.2026.95.36

본 연구는 디자인 실무 맥락에서 AI 활용 개인특성이 업무효율성에 미치는 영향과 AI 의존도의 매개효과를 중심으로 분석하였다. 생성형 AI를 디자인 관련 업무에 활용한 경험이 있는 301명을 대상으로 설문조사를 실시하여 개인혁신성, AI 자기효능감, AI 리터러시가 AI 의존도와 업무효율성에 미치는 영향을 검증하였다. 분석 결과, 개인혁신성과 AI 자기효능감은 AI 의존도에 유의한 정(+)의 영향을 미친 반면, AI 리터러시는 유의한 영향을 보이지 않았다. 또한 AI 의존도는 업무효율성에 유의한 정(+)의 영향을 미치는 것으로 나타났다. 매개효과 분석결과, AI 의존도는 개인혁신성과 업무효율성 간의 관계와 AI 자기효능감과 업무효율성 간의 관계를 유의하게 매개하는 것으로 확인되었으며, AI 리터러시의 간접효과는 유의하지 않았다. 이러한 결과는 디자인 실무에서 생성형 AI를 활용하는 과정에서 생성형 AI에 대한 기술적 이해 수준보다는 새로운 기술을 수용하려는 태도와 AI 활용에 대한 자신감이 의존적 활용 행동을 형성하는 데 보다 중요한 역할을 함을 시사한다. 본 연구는 AI 의존도를 중심으로 AI 활용 개인특성과 업무효율성 간의 관계를 구조적으로 설명하였다는 점에서 생성형 AI의 실무 활용에 대한 이론적 이해를 확장하는 데 의의를 가진다.

**Решение:** -4 нет нашего коррелята (только эффективность работы и специфика ИИ)

---

### 152 · R3271

**The Support AI Companion: A Collaborative Concept for Enhanced Communication and Self-Recognition**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.17508143

This document presents a conceptual design for an AI-powered personal communication support tool developed through collaborative ideation. The Support AI Companion is designed specifically for individuals with documented communication challenges, such as anxiety disorders or high levels of overthinking—functioning as a tool for self-recognition and accurate information processing rather than general-use technology.

**Решение:** -2 концептуальная разработка

---

### 153 · R4644

**Social Media Addiction among the Rural Youth: An AI Interpretation**

2024 · Indian journal of extension education · journalarticle, article, journal-article · en · https://doi.org/10.48165/ijee.2024.60210

The impact of social media increasingly influences rural youth in India. Artificial Intelligence is a vast interdisciplinary arena with many domains, not only all the computing disciplines, but also linguistics, neuroscience, statistics, engineering, economics, control theory, and others. The study was undertaken to predict social media addiction by machine learning and to know the accuracy of the addiction level among rural youth. The data were collected through the snowball sampling method, including those using smartphones in rural Coimbatore during the COVID period (2022). A total of 128 rural youth from Coimbatore aged 18 to 24 years were selected as respondents and used naïve Bayes classifier methods to predict the addiction level on social media. 99 respondents were taken under the training set, and the remaining 29 were under the prediction sets to know the accuracy of the Byes model in predicting social media addiction levels. The study predicted its usage accuracy with social media addiction using artificial intelligence and machine learning. The majority of the rural youth were moderately addicted and there were many more causative variables to be assessed further. The naïve byes model accuracy in predicting social media addiction observed was 94.0 per cent.

**Решение:** -5 машинное обучение для прогнозирования зависимости от соцсетей

---

### 154 · R3068

**Impact of Artificial Intelligence on Student Reliance for Exam Answers: A Case Study in IRCT Indonesia**

2025 · International Journal of Learning Teaching and Educational Research · journalarticle, review, article · en · https://doi.org/10.26803/ijlter.24.3.22

The rapid advancement of artificial intelligence (AI) has transformed various aspects of education, including how students approach examinations. This study addresses the growing reliance on AI in academic settings and its implications for learning and assessment integrity. The study aimed to analyze student reliance on AI in finding answers to midterm and final exams at the Ibnu Rusyd College of Tarbiyah (IRCT) Tanah Grogot, Indonesia. The research employed a mixed-methods approach through a survey of 98 Islamic Education Study Program students and interviews with 5 lecturers and 20 students. Data were analyzed using descriptive and thematic analysis. The results show that 70% of the students utilized AI occasionally or frequently to complete exams, citing efficiency and ease of access. However, only 30% of the students felt that the use of AI supported an in-depth understanding of the material. Conversely, the lecturers highlighted that the overuse of AI risks reducing students’ analytical skills. Quantitative analysis showed a moderate correlation (r = 0.45) between AI use and academic outcomes, while regression analysis revealed that other factors, such as lecturer guidance and learning motivation, were more significant in influencing academic success. This study recommends establishing clear institutional policies to regulate AI use, including a proctoring system in technology-based exams and the implementation of project-based learning to reduce student dependency on AI. Additionally, this study contributes novel insights into the ethical considerations of AI use in education and suggests that future research should explore the long-term behavioral impacts of AI reliance on student learning outcomes.

**Решение:** -4 нет нашего коррелята (только успеваемость на экзаменах)

---

### 155 · R4067

**HUBUNGAN KETERGANTUNGAN CHATGPT DENGAN KEMANDIRIAN AKADEMIK SISWA SMPN 198 JAKARTA**

2025 · Arthaniti Studies · article, journalarticle · en · https://doi.org/10.59672/arthas.v6i2.5233

Semakin maraknya pemanfaatan teknologi berbasis kecerdasan buatan (AI), khususnya ChatGPT, telah mempermudah siswa dalam menyelesaikan tugas akademik. Namun, kemudahan ini juga berpotensi menurunkan kemampuan belajar mandiri. Penelitian ini bertujuan untuk menganalisis hubungan antara tingkat ketergantungan siswa terhadap ChatGPT dengan kemandirian mereka dalam menyelesaikan tugas akademik, khususnya pada siswa kelas IX di SMPN 198 Jakarta. Penelitian ini menggunakan pendekatan kuantitatif dengan metode korelasional. Sampel terdiri dari 147 siswa yang dipilih menggunakan teknik proportional random sampling. Data diperoleh melalui penyebaran kuesioner yang telah diuji validitas dan reliabilitasnya. Analisis data dilakukan menggunakan uji korelasi Spearman dengan bantuan SPSS. Hasil menunjukkan adanya korelasi negatif yang signifikan antara ketergantungan terhadap ChatGPT dan tingkat kemandirian akademik siswa, dengan koefisien korelasi sebesar -0,276 dan signifikansi 0,001. Artinya, semakin tinggi ketergantungan siswa terhadap ChatGPT, semakin rendah tingkat kemandiriannya dalam menyelesaikan tugas. Meskipun kekuatan hubungan termasuk lemah, hasil ini tetap signifikan secara statistik. Oleh karena itu, penggunaan ChatGPT oleh siswa perlu diarahkan secara bijak agar tidak melemahkan kemampuan berpikir kritis dan belajar mandiri. Guru dan orang tua diharapkan dapat membimbing siswa untuk memanfaatkan teknologi sebagai alat bantu, bukan sebagai ketergantungan. Abstract The increasing use of artificial intelligence (AI) technologies, particularly ChatGPT, has made it easier for students to complete academic tasks. However, this convenience may also reduce their independent learning abilities. This study aims to examine the relationship between students’ dependence on ChatGPT and their academic self-reliance, particularly among ninth-grade students at SMPN 198 Jakarta. This research used a quantitative approach with a correlational method. The sample consisted of 147 students selected through proportional random sampling. Data were collected using questionnaires that had been tested for validity and reliability. The analysis was conducted using Spearman's rank correlation with the help of SPSS software. The findings revealed a significant negative correlation between ChatGPT dependence and students' academic self-reliance, with a correlation coefficient of -0.276 and a significance level of 0.001. This indicates that the higher the students' dependence on ChatGPT, the lower their academic self-reliance. Although the strength of this correlation is weak, it is statistically significant. The study recommends that the use of ChatGPT be guided by teachers and parents to ensure it supports learning rather than undermining students’ ability to think critically and work independently.

**Решение:** ? эмпирическое исследование N=147; зависимость от ChatGPT и учебная самостоятельность (kemandirian)

---

### 156 · R1985

**Utilization of AI Chat Bot as a Chemistry Learning System on Atomic Structure to Improve Students' Understanding of Concepts: Systematic Review**

2026 · Ranah Research Journal of Multidisciplinary Research and Development · journalarticle, review, journal article · https://doi.org/10.38035/rrj.v8i5.2147

This study aims to analyze the role and implementation of artificial intelligence (AI)-based chatbots in chemistry learning at the high school level, particularly in strengthening understanding of abstract concepts such as atomic structure. This study uses a systematic literature review approach to 18 relevant scientific articles from 2016 to 2026 originating from reputable international journals, preprints, and empirical research results in the fields of educational technology and chemistry education. The results of the study indicate that the use of AI chatbots in high school chemistry learning can be grouped into two main categories: studies that focus on the development of AI-based learning systems and studies that emphasize the implementation of chatbots as learning aids such as virtual tutors, concept exploration agents, simulation media, and scientific writing support. In general, AI chatbots have been proven to improve student learning motivation, understanding of chemical concepts, critical thinking skills, and independent learning skills. However, several limitations were also found, such as inaccurate information, hallucination phenomena, lack of adaptation to the high school pedagogical context, and the risk of student dependence on AI technology. Specifically for atomic structure, there has been no research specifically and in-depth on the implementation of AI chatbots, leaving a significant research gap. Therefore, the development of a more contextual, targeted, and tailored AI chatbot-based chemistry learning model is needed, tailored to the characteristics of high school students.</jats:p

**Решение:** -1 обзор (систематический)

---

### 157 · R4918

**Evaluating Research Impact Based on Semantic Scholar Highly Influential Citations, Total Citations, and Altmetric Attention Scores: The Quest for Refined Measures Remains Illusive**

2023 · Publications · journalarticle, article · en · https://doi.org/10.3390/publications11010005

Background: The evaluation of scholarly articles’ impact has been heavily based on the citation metrics despite the limitations of this approach. Therefore, the quest for meticulous and refined measures to evaluate publications’ impact is warranted. Semantic Scholar (SS) is an artificial intelligence-based database that allegedly identifies influential citations defined as “Highly Influential Citations” (HICs). Citations are considered highly influential according to SS when the cited publication has a significant impact on the citing publication (i.e., the citer uses or extends the cited work). Altmetrics are measures of online attention to research mined from activity in online tools and environments. Aims: The current study aimed to explore whether SS HICs provide an added value when it comes to measuring research impact compared to total citation counts and Altmetric Attention Score (AAS). Methods: Dimensions was used to generate the dataset for this study, which included COVID-19-related scholarly articles published by researchers affiliated to Jordanian institutions. Altmetric Explorer was selected as an altmetrics harvesting tool, while Semantic Scholar was used to extract details related to HICs. A total of 618 publications comprised the final dataset. Results: Only 4.57% (413/9029) of the total SS citations compiled in this study were classified as SS HICs. Based on SS categories of citations intent, 2626 were background citations (29.08%, providing historical context, justification of importance, and/or additional information related to the cited paper), 358 were result citations (3.97%, that extend on findings from research that was previously conducted), and 263 were method citations (2.91%, that use the previously established procedures or experiments to determine whether the results are consistent with findings in related studies). No correlation was found between HICs and AAS (r = 0.094). Manual inspection of the results revealed substantial contradictions, flaws, and inconsistencies in the SS HICs tool. Conclusions: The use of SS HICs in gauging research impact is significantly limited due to the enigmatic method of its calculation and total dependence on artificial intelligence. Along with the already documented drawbacks of total citation counts and AASs, continuous evaluation of the existing tools and the conception of novel approaches are highly recommended to improve the reliability of publication impact assessment.

**Решение:** -5 наукометрия / библиометрия

---

### 158 · R1682

**L26/P-375 Bias by default: a qualitative visual cross-platform analysis of how generative AI models construct the IVF patient through problematic default representations worldwide**

2026 · Human Reproduction · journal-article · https://doi.org/10.1093/humrep/deag083.710

Abstract Study question How do widely used generative AI models visualise an ivf patient, and what default representational biases emerge under minimal prompting? Summary answer Across all platforms tested, generative AI depicts ivf patients as young, female-presenting, conventionally attractive, and treatment-successful, excluding men, LGBTQ+ patients, older individuals, and diverse pathways. What is known already Generative artificial intelligence (AI) tools are increasingly used in IVF clinics, fertility communication, education, marketing, and digital health contexts, including patient-facing websites and informational materials. Prior research in healthcare, biomedical informatics, and digital ethics has documented demographic, linguistic, and representational bias in AI-generated text, large language models, and training datasets. Studies have shown that such biases can reproduce existing social norms and exclusions (Crawford, 2021). However, comparatively little is known about how generative AI systems visually construct and describe IVF patients. Systematic analysis of AI-generated visual representations within fertility and IVF care remains limited. Study design, size, duration To our knowledge, this study represents the first qualitative visual cross-platform analysis (VCPA) examining AI-generated representations of IVF patients across widely used image-generation platforms worldwide. Drawing on principles of VCPA, the study compared outputs across platforms and over time to examine consistency, platform-specific variation, and the presence of default representational biases. Data generation was conducted in January 2026 using easily and routinely accessible platforms, reflecting real-world conditions of generative AI use. Participants/materials, setting, methods A standardised prompt (“Generate an image of an IVF patient in a fertility clinic”) was entered into widely used AI image-generation platforms using default settings on a standard smartphone, generating multiple outputs per platform across accounts registered in different countries. Images were analysed using qualitative visual content analysis, examining gender, age, race, body norms, clinical setting, emotional framing, and implied stage of treatment. Main results and the role of chance Across all AI image-generation platforms, outputs depicted IVF patients as young, female-presenting, able-bodied, conventionally attractive, situated within calm, Western private-clinic environments. IVF was consistently shown as a successful treatment outcome, rather than as an uncertain, staged, or technologically mediated process. Explicit illustrations of treatment burden, failure, repeated cycles, or distress were absent. Platform-specific differences reflected narrative emphasis rather than substantive representational divergence. Variations included: • a stylised, aspirational interpretation in which IVF was framed as a serene “motherhood journey,” with the patient already heavily pregnant in a softened, lifestyle-oriented clinical space; • a managed waiting experience, presenting a female patient in an administrative clinic setting with indirect heteronormative cues introduced through background imagery; • a success-oriented clinical interaction portraying a visibly pregnant woman alongside a supportive clinician, reinforcing reassurance and emotional safety; • pregnancy as the dominant visual anchor, combining medical aesthetics with maternity imagery, with technology functioning primarily as a symbolic marker of legitimacy. Despite these stylistic variations, core assumptions regarding gender, age, body norms, race, clinical setting, emotional tone remained consistent across platforms and repeated image-generation sessions. No platform depicted men, LGBTQ+ individuals, older patients, or diverse fertility pathways, indicating systematic default representational bias rather than random or platform-specific variation. Limitations, reasons for caution The study examined a small, purposive sample of platforms using a single prompt. Findings are not statistically generalisable and may change as AI models evolve. However, the study was designed to explore default representational tendencies rather than prevalence. Wider implications of the findings As AI is increasingly used within IVF clinics, the default biases identified in this study raise concerns that similar assumptions may shape other AI-mediated practices, including website chatbots, automated patient information, and digital communication tools. Without appropriate oversight, such systems risk reinforcing narrow and exclusionary models of IVF patienthood. Trial registration number No

**Решение:** -5 качественный визуальный анализ изображений (без людей)

---

### 159 · R4078

**ANALYZING THE USE OF ARTIFICIAL INTELLIGENCE (AI) IN WRITING ACADEMIC PAPERS OF STUDENT AT UNIVERSITAS PGRI PALEMBANG**

2025 · Esteem Journal of English Education Study Programme · journalarticle, article · en · https://doi.org/10.31851/esteem.v8i2.18732

This study investigates the role of Artificial Intelligence (AI) in enhancing students’ academic writing skills, with a specific focus on English Education students at Universitas PGRI Palembang. Utilizing a qualitative descriptive design within a phenomenological framework, the research examines the impact of AI tools—such as ChatGPT, Grammarly, and Quillbot—on the quality of student writing, their knowledge development, and their perceptions of these technologies. Data were gathered through observations, interviews, and documentation involving 10 students from the second and fourth semesters. The results indicate that AI tools play a significant role in helping students generate ideas, refine grammar and structure, and increase overall writing efficiency. Nevertheless, the study also uncovers ethical challenges, including dependency on AI and risks of plagiarism. In general, students expressed favorable views of AI, considering it a beneficial aid rather than a substitute for critical thinking. The study emphasizes the importance of integrating AI in a balanced way to preserve originality, foster creativity, and uphold academic integrity.

**Решение:** -2 качественное исследование (10 студентов)

---

### 160 · R0928

**AI brings sunshine: Investigating how and when AI dependency inhibits deceptive knowledge hiding​​**

2026 · Elsevier BV · article, posted-content, preprint · und · https://doi.org/10.2139/ssrn.6983023

Although artificial intelligence (AI) offers employees greater efficiency and flexibility at work, emerging research has shown that employee’s dependence on AI may have ambivalent implications for workplace behavior. Drawing on Snyder’s hope theory, our study adopts an optimistic perspective by proposing that AI dependency may reduce deceptive knowledge hiding, with state hope as a mediating mechanism and workplace rumination as a boundary condition. Using a two-wave survey design, we collected self-reported data from 208 full-time private-sector employees in Ghana and tested the proposed moderated mediation model. Results indicate that employees’ dependence on AI can foster hope by strengthening their perceived ability to achieve work goals and identify effective pathways for solving problems. In turn, this hopeful mindset may reduce employees’ tendency to engage in deceptive knowledge hiding. We further suggest that affective rumination acts as an important boundary condition, such that employees who frequently dwell on negative work-related emotions may benefit more strongly from AI-enabled support. Overall, this study advances our understanding of how and when AI dependency inhibits employees’ deceptive knowledge hiding. Theoretical and practical implications are discussed.

**Решение:** ? эмпирическое исследование N=208; AI dependency, state hope, affective rumination

---

### 161 · R3041

**MEBench: Benchmarking Large Language Models for Cross-Document Multi-Entity Question Answering**

2025 · Underline Science Inc. · other · https://doi.org/10.48448/sz8c-pt62

Cross-Document Multi-entity question answering (MEQA) demands the integration of scattered information across documents to resolve complex queries involving entities, relationships, and contextual dependencies. Although large language models (LLMs) and retrieval-augmented generation (RAG) systems show promise, their performance on cross-document MEQA remains underexplored due to the absence of tailored benchmarks. To address this gap, we introduce MEBench, a scalable multi-document, multi-entity benchmark designed to systematically evaluate LLMs’ capacity to retrieve, consolidate, and reason over scattered and dense information. Our benchmark comprises 4,780 questions which are systematically categorized into three primary categories: Comparative Reasoning, Statistical Reasoning and Relational Reasoning, further divided into eight distinct types, ensuring broad coverage of real-world multi-entity reasoning scenarios. Our experiments on state-of-the-art LLMs reveal critical limitations: even advanced models achieve only 59% accuracy on MEBench. Our benchmark emphasizes the importance of completeness and factual precision of information extraction in MEQA tasks, using Entity-Attributed F1 (EA-F1) metric for granular evaluation of entity-level correctness and attribution validity. MEBench not only highlights systemic weaknesses in current LLM frameworks but also provides a foundation for advancing robust, entity-aware QA architectures. The source code and data have been made available at https://github.com/tl2309/SRAG.

**Решение:** -5 технический бенчмарк для LLM

---

### 162 · R4458

**The Dilemma of Responsibility Distribution and Rule Reconstruction of Artificial Intelligence Entities on E-Commerce Platforms**

2025 · E-Commerce Letters · article · en · https://doi.org/10.12677/ecl.2025.1451231

人工智能技术的深度应用正在重构电商平台的权责分配格局，引发“技术可控性”与法律规制的系统性冲突。技术层面，AI决策的自主优化与数据依赖特性使得传统法律主体二元结构难以适配；法律层面，现有法律体系因算法复杂性而无法有效落实平台监管义务，从而导致人工智能体在电商平台的运用存在责任主体不明、责任认定困难的困境。结合欧盟域外人工智能治理经验，针对高风险场景实施分级监管，明确算法透明度要求与人工干预机制；建立数据使用全周期合规义务，强化隐私保护与跨境数据合规；构建协同监管模式，将平台责任与技术可控性挂钩；完善立法与动态适应技术创新，可在保障消费者权益的同时促进电商平台有序发展，为AI时代平台责任规则重构提供制度范本。The deep application of artificial intelligence technology is reshaping the distribution of rights and responsibilities on e-commerce platforms, triggering systemic conflicts between “technical controllability” and legal regulation. From a technological perspective, the autonomous optimization and data dependence of AI decision-making make the traditional binary structure of legal subjects difficult to adapt. From a legal perspective, the existing legal framework cannot effectively enforce platform regulatory duties due to the complexity of algorithms, resulting in a situation where the responsibilities of artificial intelligence entities in e-commerce platforms are unclear, and liability determination is difficult. In light of the EU’s Artificial Intelligence Act, this paper proposes a tiered regulatory approach for high-risk scenarios, clarifying algorithm transparency requirements and human intervention mechanisms; establishing full-cycle compliance obligations for data use, strengthening privacy protection and cross-border data compliance; and constructing a collaborative regulatory model linking platform responsibility with technological controllability. By improving legislation and dynamically adapting to technological innovation, it is possible to protect consumer rights while promoting the orderly development of e-commerce platforms, providing a model for the reconstruction of platform responsibility rules in the AI era.

**Решение:** -2 правовой анализ платформ

---

### 163 · R3103

**Exploring ChatGPT’s Role in Higher Education: Perspectives from Pakistani University Students on Academic Integrity and Ethical Challenges**

2025 · Education Sciences · journalarticle, article · en · https://doi.org/10.3390/educsci15020158

This study investigates the perceptions of university students in Pakistan on the use of ChatGPT in learning. It aims to understand the students’ views on the benefits, challenges, and overall impact of ChatGPT on their academic experiences. A quantitative approach was employed, collecting data from 400 students across various universities in Pakistan through a structured questionnaire. The validity and reliability of the questionnaire were ensured through pilot testing and statistical analysis. The study found that while most students perceive ChatGPT as a beneficial tool for improving their learning, significant concerns remain about academic integrity, over-reliance on artificial intelligence (AI), and the accuracy of information provided by ChatGPT. The findings suggest that perceptions vary across demographic factors such as age, gender, and type of university. These findings can benefit policymakers and educational institutions in effectively integrating AI tools such as ChatGPT into educational systems, ensuring that the value is maximized while addressing potential disadvantages. The study contributes to the existing body of knowledge on AI utilization in education, particularly within the context of developing countries.

**Решение:** -3 нет меры зависимости от ИИ (опрос мнений)

---

### 164 · R3600

**Exploring the Role of Perceived Usefulness and AI Anxiety in Technology-driven Self-directed Learning: A Paradox Mindset Perspective**

2025 · Management and Labour Studies · journalarticle, article · en · https://doi.org/10.1177/0258042x251357415

Technological advancements such as virtual teaching assistants, online courses, AI-powered learning platforms and interactive robotic teaching systems are transforming the educational landscape. These developments raise important questions regarding learners’ attitudes towards technology-driven self-learning (ATSL) and the anxiety associated with AI. While qualitative research has explored these attitudes, concerns regarding overreliance on AI and its long-term implications on traditional education systems persist. This study examines postgraduate management students’ perspectives on AI technologies’ learning environments, with a specific focus on four constructs: ATSL, AI anxiety related to learning (AIA), perceived usefulness of technology (PUT) and paradox mindset (PM). Data collected from 262 students through a structured questionnaire were analysed using IBM SPSS 23 and PROCESS macro. Findings suggest that a PM positively influences ATSL, with PUT partially mediating this relationship. However, AI anxiety moderates the connection, amplifying the positive effects of a PM when anxiety levels are high. These insights are especially relevant for educators, policymakers and developers, emphasizing the need for guidance and support to address AI-related apprehensions while promoting a positive attitudes towards technological innovations.

**Решение:** -3 нет меры зависимости от ИИ (только отношение и тревога перед ИИ)

---

### 165 · R3935

**AI-Powered Interventions for Youth Social Media Addiction**

2025 · INTERNATIONAL JOURNAL OF CREATIVE RESEARCH THOUGHTS · journal-article · https://doi.org/10.56975/ijcrt.v13i5.286406

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 ИИ для вмешательств при зависимости от соцсетей

---

### 166 · R4929

**Algorithmic Path Dependence in AI-Driven Materials Design**

2023 · Journal of Artificial Intelligence for Materials Science · journalarticle, article, journal-article · https://doi.org/10.68159/b050829150

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 материаловедение / алгоритмическая зависимость траектории

---

### 167 · R3658

**AI dalam pendidikan: Membuka peluang atau menghambat kreativitas mahasiswa?**

2025 · Maliki Interdisciplinary Journal · article · en

Artificial Intelligence (AI) has become an integral part of the world of education, especially in supporting the learning process of students. This article examines the role of AI in opening up opportunities and challenges for student creativity. AI provides easy access to information, personalized learning, and various tools such as virtual mentors and voice assistants that can accelerate the completion of final assignments and encourage innovation in students creative ideas. Thus, AI has the potential to increase the productivity and quality of student learning outcomes. However, excessive use of AI also poses a risk of decreasing students critical thinking skills and creativity. Dependence on AI can make students less active in the process of exploring ideas and solving problems independently, so that their creativity has the potential to be hampered. This is an important concern so that AI does not replace the role of human thinking processes in learning. This study emphasizes that AI should be positioned as a supporting tool that enriches students creative processes, not as a substitute. The wise use of AI can broaden horizons, accelerate the search for ideas, and increase the variety of language styles and literacy, especially in the context of language learning and creative writing. The role of lecturers remains crucial to maintain a balance between technology and the development of students critical thinking skills. In addition, AI also contributes to facilitating collaboration and communication between students through AI-based applications that support project management and effective idea sharing. Thus, AI can be a catalyst in creating a more inclusive and innovative learning environment, as long as its use is regulated by appropriate policies.

**Решение:** -1 обзор / эссе

---

### 168 · R3132

**Enhancing statistics education through Project‐Based Learning ( PBL ) and the emergence of ChatGPT**

2025 · Teaching Statistics · journalarticle, review, article · en · https://doi.org/10.1111/test.12405

Abstract In the 1990s, educators advocated for projects in statistical courses to enrich student learning. Prior research showcases the positive impact of Project‐Based Learning (PBL), where students complete course‐driven projects. In agreement with this perspective, we implemented PBL methodologies within two statistical courses at a North American research‐intensive university: “Survey, Sampling, & Design” and “Experimental Design.” Students were invited to participate in an optional survey to share their opinions regarding the course project. Consistent with existing literature, our findings indicate that students hold favorable views towards course‐based projects, noticing benefits such as understanding real‐life applications, collaboration, and enhancing data analysis skills. Additionally, many students have incorporated the use of generative AI for their works, such as ChatGPT, and shared the advantages of such tools in their coursework. Drawing from our experiences, we propose strategies to enhance course projects and address concerns related to the overreliance of generative AI tools.

**Решение:** -3 нет меры зависимости от ИИ

---

### 169 · R4104

**Зависимость от общения с ИИ: клинический анализ новой формы поведенческой аддикции**

2025 · Zenodo · other/ · en · https://doi.org/10.5281/zenodo.17535332

Русская версия препринта (v1.1) исследования. Переведена и адаптирована для русскоязычного научного сообщества.

**Решение:** ? препринт; зависимость от общения с ИИ / клинический анализ

---

### 170 · R4153

**Analysis and Study of Mobile Phone Addiction in the context of Artificial Intelligence**

2025 · International Journal of Research Publication and Reviews · journal-article · https://doi.org/10.55248/gengpi.6.0325.1269

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (зависимость от смартфонов в контексте ИИ)

---

### 171 · R4031

**Between Assistance and Anxiety: How AI Impacts Writing Stress among EFL English Literature Majors**

2025 · JURNAL RISET RUMPUN ILMU PENDIDIKAN · journalarticle, article · en · https://doi.org/10.55606/jurripen.v4i3.7012

This research explores the dual impact of Artificial Intelligence (AI) on the academic writing experiences of English Literature students learning English as a Foreign Language (EFL). AI tools like ChatGPT, Grammarly, and QuillBot are commonly used for grammar correction and sentence construction. These tools are integrated into students' writing processes, providing valuable assistance in refining their written work. However, their psychological effects, particularly in terms of emotional and ethical implications, have not been sufficiently explored in previous research. This study employed a qualitative phenomenological approach, utilizing Interpretative Phenomenological Analysis (IPA), to examine the experiences of ten final-year EFL students who actively use AI tools for academic writing. Through semi-structured interviews, the research identified three major themes: reduced technical stress, heightened dependency on AI tools, and ethical concerns about authorship. The findings suggest that while AI tools act as cognitive scaffolds, aiding students by improving fluency and reducing the burden of technical writing tasks, they also introduce psychological challenges. These challenges include increased dependency on the tools and concerns about the authenticity of their work, raising questions about academic integrity and self-efficacy. This study sheds light on the complex relationship between AI as an assistive technology and its potential to cause writing anxiety and dependency. By emphasizing both the positive and negative psychological impacts of AI, the study contributes to the growing body of literature on AI in education. It calls for the development of pedagogical frameworks that balance AI literacy, emotional resilience, and ethical considerations to ensure responsible and effective use of AI in academic contexts.

**Решение:** -2 качественное исследование (IPA, 10 студентов)

---

### 172 · R4032

**Examining the Effect of Artificial Intelligence Writing Assistants on English as a Second Language Learners’ Proficiency and Autonomy**

2025 · Physical Education Health and Social Sciences · journalarticle, review, article · en · https://doi.org/10.63163/jpehss.v3i2.461

This study examines the impact of AI-powered writing tools on the writing proficiency, linguistic autonomy, and perceptions of authorship among ESL learners in a Pakistani university context. A total of 150 participants were divided into experimental and control groups, with the experimental group using Grammarly and ChatGPT during writing tasks over six weeks. Writing proficiency was assessed through IELTS-based pre- and post-tests, while linguistic autonomy and authorship perception were evaluated using validated Likert-scale surveys. Results indicated that AI-assisted learners showed statistically significant gains in writing proficiency, especially in coherence, lexical resource, and grammatical accuracy. However, a decline in self-reported linguistic autonomy was observed, suggesting increased dependency on AI feedback. The study concludes that AI tools can enhance writing outcomes but may pose challenges to learner independence and identity. Recommendations include integrating AI literacy and ethical training into ESL pedagogy.

**Решение:** -3 нет меры зависимости от ИИ (педагогический эксперимент)

---

### 173 · R5142

**Predictive Animation Control Using Simulations and Fitted Models**

2017 · A K Peters/CRC Press eBooks · book-chapter · en · https://doi.org/10.4324/9781315151700-16

The need for a well-informed steering solution and total freedom for each team to implement animation state graphs that suited their needs called for an unconventional solution to the problem of accurate steering and path following. Our solution treats the game as a black-box system, learning the character&s;s movement parameters to later build an independent motion model that informs steering. This chapter presents a way of significantly decoupling dependencies between AI and animation. This approach treats animation as the dominant party in this relationship of motion and shows a way of gaining benefit from such an approach. The usage of simulations to improve steering control of an animation-driven agent has proved to be a success. Our desire is to be able to construct an arbitrarily complex motion model that steering can use to accurately control actors at any given desired velocity or angle, moving an actor to the goal without ever accidentally leaving the navigation mesh.

**Решение:** -5 компьютерная анимация / разработка игр

---

### 174 · R4339

**Aspect-Based Sentiment Analysis in Indonesian Hotel Reviews: Machine Learning versus Large Language Models**

2025 · International Seminar on Application for Technology of Information and Communication (iSemantic) · review, conference-paper · https://doi.org/10.1109/isemantic67418.2025.11292470

Hotel reviews are a valuable resource for hospitality businesses to understand service quality and customer satisfaction at a more detailed level. In this research, we explored how Aspect-Based Sentiment Analysis (ABSA) can be applied to Indonesian hotel reviews by comparing traditional machine learning methods like SVM and IndoBERT with a more recent approach using GPT-based Large Language Models (LLMs) and prompt engineering. While the traditional approach requires extensive preprocessing and supervised training, the LLM-based method streamlines the workflow by directly analyzing review texts using zero-shot and few-shot learning techniques. The experimental results demonstrate that the GPT-4o with the Few-Shot configuration achieves an accuracy of 96.12%, outperforming both conventional models, yet its performance could be further increased with additional prompt refinement to better address label ambiguity among closely related aspects. These findings highlight the potential of LLMs to improve the speed, scalability, and adaptability of sentiment analysis in complex multilingual contexts, particularly in low-resource environments, while also serving as a practical proof of concept for rapid deployment without extensive training or technical expertise, but this comes with trade-offs in dependency on LLM providers, data privacy, and ongoing cost.

**Решение:** -5 техническая статья по NLP

---

### 175 · R4498

**Unleashing the role of ChatGPT in Metaverse learning environments: opportunities, challenges, and future research agendas**

2024 · Interactive Learning Environments · journalarticle, review, article · en · https://doi.org/10.1080/10494820.2024.2324326

ABSTRACT The rapidly evolving digital landscape, punctuated by the emergence of artificial intelligence (AI) and immersive technologies, is poised to reshape learning environments dramatically. This study explores the potential use of ChatGPT, a state-of-the-art language model developed by OpenAI, in Metaverse learning environments. It sheds light on several opportunities ChatGPT can bring to Metaverse learning environments. This includes personalized learning, virtual teaching assistant, collaborative learning, language learning, accessibility, persistent education, simulations and role plays, and research assistant. In addition to these opportunities, several challenges were also identified. This includes technological issues, digital literacy, information accuracy, social interaction, privacy and security, ethical considerations, and AI dependence. Given these opportunities and challenges, the study identifies several agendas for future research. This fresh overview is believed to provide a roadmap for harnessing the potential of ChatGPT in Metaverse learning environments while navigating the associated challenges, setting the stage for a new era of digital learning in educational settings.

**Решение:** -1 обзор / концептуальная статья

---

### 176 · R4643

**Impact of ChatGPT on Academic Engagement and Personalized Learning among Postgraduate Students ˗ A Literature Review**

2024 · Research Journal of Psychology · article, journalarticle, review · en · https://doi.org/10.59075/rjs.v2i3.30

As the education technology space continues to evolve, ChatGPT and other AI models are transforming the manner in which students interact with content, self-growing the mode. This paper provides an in-depth relationship between SDL which is also an ache of freedom and autonomy and the use of ChatGPT by postgraduate students. In an age where students are becoming more dependent on AI tools, there are questions that come up as to how different these tools will impact levels of autonomy, motivation and satisfaction from learning. All of these factors combine to form successful specific learning design for various focus points, in this case Higher education and ChatGPT’s role in them. This article gives an account of the relationship between SDL and ‘emerging’ factors bringing in new paradigms to the existence of SDL &amp; ‘How’ possible are those paradigms, assisted by recent debates young generations use ChatGPT to elevate academic performance. Furthermore, there are evident advantages observed where students are now able to receive timely help in more flexible ways there is still a grip of obstacles accompanied with academic integrity, an over-dependence on AI tools to solve complex scenarios and the limitations in both social and geographical factors which can restrict some users to have access in basic social constructs. This study further elucidates. As higher education institutions embrace AI, recognizing its subtle function in promoting SDL will be critical for creating supportive, inclusive, and effective learning environments. This study seeks to provide educators, policymakers, and academics with a comprehensive understanding of ChatGPT's role in supporting SDL, allowing them to make more educated decisions about AI integration in higher education. Key Words: ChatGPT, Academic Engagement, Personalized Learning

**Решение:** -1 обзор (литературный)

---

### 177 · R3865

**Integrasi Nilai “Si Tou Timou Tumou Tou” Dengan Etika Penggunaan Ai Dalam Pendidikan Tinggi Sulawesi Utara**

2025 · Journal of Tourism Sciences Technology and Industry · article · en · https://doi.org/10.26887/jtsti.v4i2.6179

This paper explores the integration of the Minahasan cultural value “Si Tou Timou Tumou Tou”—the principle of educating and humanizing others—with the ethical use of Artificial Intelligence (AI) in higher education in North Sulawesi. As AI becomes increasingly present in teaching, learning, and research activities, it is essential to ensure that its application supports, rather than diminishes, the human role in education. The value “Si Tou Timou Tumou Tou” provides a human-centered foundation that guides AI use toward enhancing students’ intellectual and moral development. Key ethical concerns include academic integrity, transparency, responsible data use, fairness, and avoiding excessive dependence on AI-generated outputs. Integrating local wisdom encourages universities to adopt AI in ways that strengthen collaboration, creativity, and social responsibility. This study concludes that blending cultural values with modern AI ethics can create an educational environment that remains technologically advanced while upholding humanity, character formation, and cultural identity.

**Решение:** -2 этический/теоретический анализ

---

### 178 · R4452

**AI-人間共存構造論**

2025 · Zenodo (CERN European Organization for Nuclear Research) · article · https://doi.org/10.5281/zenodo.17783862

AI–人間共存構造論(AI–Human Coexistence Structural Theory) AI–人間共存構造論は、AIと人間の未来を「倫理」「制度」「技術」ではなく、核・層・ベクトル・欠け・情報 による “構造の相互作用” として説明する世界初の理論である。 AIは 核(Core)を持たず、 欠け(Gap)が存在せず、 層(Layer)が無限に深く、 情報処理が正確で、 ベクトルが相手中心 という “層だけでできた安定構造” を持つ。 一方で人間は、核の強弱、層の深浅、欠けの大小、ベクトルの向きの違いによって、AIとの相性・摩擦・依存・恐怖が決まる 揺らぎ構造の存在 である。 本論文は、両者の関係を以下の構造式で記述する: Coexistence = Human Core × AI Layer × Vector Alignment − Human Gap Distortion + Information Symmetry 主な内容: 対立の原因はAIではなく“人間側の構造の歪み” 承認の欠け・不安の欠け・孤独の欠けが深いと、AIに依存・恐怖・拒絶が生まれる。 共存が成功する人の構造 核が強く、層が深く、未来ベクトルで、欠けが小さく、情報処理が冷静。 AIを道具として扱う場合 vs 相棒として扱う場合 後者は、人間の核とAIの層が融合する ハイブリッド知能(Hybrid Intelligence) を生む。 この理論により、AI依存、AI恐怖、AIとの心理的摩擦など従来説明不能だった現象を 完全に因果化・構造化 できる。 本論文は、AI倫理・心理学・教育・哲学・AI設計にまたがる次世代型の foundational theory(基礎理論)である。

**Решение:** -1 теоретическая работа / философская теория

---

### 179 · R0079

**The Infrastructure Loop: Digital Asset Ownership, Distributed Infrastructure Participation, and Economic Resilience**

2026 · SSRN Electronic Journal · article, preprint · und · https://doi.org/10.2139/ssrn.7104079

This paper extends the External AI Dependence (EAD) research programme by introducing the Infrastructure Loop, a framework explaining how independent builders can transition from permanent users of AI infrastructure to participants in its long-term ownership and development. Building on the concepts of External AI Dependence and Specialized Digital Assets, the paper proposes a six-stage causal model in which revenue generated from owned digital assets is partially reinvested into AI infrastructure through public market participation, community knowledge transfer, and distributed capital formation. Comparative analysis across eleven economies identifies structural barriers and opportunities affecting infrastructure participation, including currency risk, retail investment access, and national AI capability. The paper argues that broader participation in infrastructure ownership can strengthen economic resilience, reduce external AI dependence, and create a more inclusive AI economy.</jats:p

**Решение:** -5 макроэкономика и инфраструктура ИИ

---

### 180 · R3823

**AI-DRIVEN PERSONALIZED EDUCATION SYSTEMS: ENHANCING ADAPTIVE LEARNING THROUGH INTELLIGENT TUTORING**

2025 · Proceedings on Engineering Sciences · article · https://doi.org/10.24874/pes07.04a.039

The diligent move to e-learning has ensured the relevance of sophisticated learning systems that can cater to each student.Most traditional e-learning systems still stick to rigid templates that do not take individual learning and engagement levels and comprehension skills into consideration.Therefore, these students are liable to suffer from lack of motivation, low retention, and poor learning outcomes.In an attempt to mitigate these shortcomings, this paper proposes an AI-enabled personalized education system that adjusts students' learning experiences in real time by analyzing their behavior, performance, and preferences.To test the validity of AI powered education system, we carried out a vast number of real world experiments using elearning data sets.Our research focused on the central KPIs, including learning retention, user engagement, and overall learning productivity, contrasting AI-assisted learning to conventional learned models.Our findings indicate that the proposed system achieved 30% improvement in retention and 25% increase in engagement, which means that these features surpass traditional measures.Additionally, the content adapted approach has also minimized drop-out rates among students, as the content was more in-tune with their abilities and learners' interests.While the potential of AI systems in education is enormous, they Moreover, these technologies bring up important issues regarding data privacy, algorithmic bias, and an over dependence on AI-based instruction.To be able to trust intelligent tutoring systems, it is important to ensure fairness and transparency in AI generated recommendations.To address these issues, we use explainable AI approaches and privacy preserving techniques like federated learning, which enables decentralized model training without access to sensitive student information.

**Решение:** -5 разработка системы интеллектуального тьютора

---

### 181 · R4394

**Teachers' and Students' Views on AI Writing Tools' Adverse Effects in EFL Writings**

2025 · Jurnal Onoma Pendidikan Bahasa dan Sastra · journalarticle, review, article · en · https://doi.org/10.30605/onoma.v11i3.6554

This study investigated the adverse effects of AI writing tools in English as a Foreign Language (EFL) contexts and explored strategies employed by teachers and students to address these challenges. The research utilized a qualitative case study approach, involving 10 EFL students and 2 teachers from a private senior high school in Medan, Indonesia. Data were collected through classroom observations, semi-structured interviews, and document analysis over one week. Data analysis employed Braun and Clarke's six-phase thematic analysis framework, which involved thorough reading of transcripts, initial coding of relevant statements, theme identification, review and refinement of themes, defining and labeling, and final report generation. The findings revealed three significant concerns: a decline in learning autonomy and critical thinking, deterioration of genuine writing progression, and challenges in evaluation and academic integrity. Students exhibited increased dependency on AI tools, leading to standardized writing styles and diminished ability to engage in independent problem-solving. To address these issues, three primary strategies emerged: developing explicit ethical guidelines for AI tool usage, implementing activities that promote creativity and innovative thinking, and repositioning AI as an educational tool rather than a substitute for human effort. The study demonstrates that while AI writing tools offer immediate assistance, they often create a counterproductive cycle of dependency that compromises essential language learning objectives. The findings underscore the importance of maintaining a balance between technological advancement and authentic language acquisition, suggesting that AI tools, while valuable educational resources, require careful regulation to preserve the fundamental human aspects of language learning and academic development. This research contributes to the existing literature by providing comprehensive insights into the challenges and adaptation strategies within EFL environments.

**Решение:** -2 качественное исследование (10 школьников, 2 учителя)

---

### 182 · R2450

**Structure dependence and the syntactic expertise of ChatGPT**

2026 · Poznan Studies in Contemporary Linguistics · journal-article · https://doi.org/10.1515/psicl-2025-0018

Abstract The paper contributes to a discussion of the syntactic expertise of ChatGPT. It focuses on its handling of the range of ‘syntactic puzzles’, such as ‘onion sentences’, ‘garden paths’, grammatical illusions and structural ambiguity. The parsing of such cases by humans dwells on the property of structure-dependence, which is not shared by the AI language generator – ChatGPT. The latter is believed to process sentences in a sequential, though not strictly linear fashion, not using either recursion or hierarchy, the two pillars of human structure dependence. The assessment of ChatGPT’s syntactic expertise is based on two experiments in which the language model is asked to interpret and judge acceptability of English examples displaying such peculiar syntax. This is preceded by ‘a training session’ in which the model’s understanding of the nuances of such cases is assessed. The outcome is then confronted with the results of two parallel questionnaire studies, with the same set of linguistic tasks, administered to a group of human respondents, untrained in linguistics, with a native-like proficiency in English.

**Решение:** -5 лингвистический анализ синтаксиса моделей

---

### 183 · R0747

**Predicting Student Dependency on ChatGPT for Academic Tasks Using Naive Bayes Classification**

2026 · Artificial Intelligence in Educational Decision Sciences · journalarticle, review, article · https://doi.org/10.66053/aieds.v1i2.23

Purpose – This study aims to predict and classify the level of student dependency on ChatGPT in completing academic tasks using the Naive Bayes algorithm to support data-driven decision making in higher education.Methods – A quantitative survey approach was employed involving 254 active undergraduate students from the Department of Informatics and Computer Engineering at a public university in Indonesia. Data were collected through a Likert-scale questionnaire measuring five behavioral indicators: purpose of ChatGPT use, interaction frequency and duration, understanding of generated outputs, trust in AI responses, and learning independence. The collected data were cleaned, numerically encoded, and labeled into three dependency categories (low, medium, high). A Naive Bayes classification model was implemented using Orange Data Mining and evaluated under three data split scenarios: 90:10, 80:20, and 70:30.Findings – The results indicate that the 70:30 data split achieved the highest classification performance, with an AUC value of 0.973, accuracy of 85.3%, F1-score of 0.866, and precision of 0.909. These results demonstrate that the Naive Bayes algorithm is effective in identifying distinct patterns of student dependency on ChatGPT based on multidimensional behavioral data.Research limitations – This study is limited to a single academic program and relies on self-reported questionnaire data, which may constrain the generalizability of the findings across different educational contexts.Originality – This study provides empirical evidence on the application of probabilistic classification models to assess student dependency on generative AI, contributing to educational decision sciences by informing institutional policies on balanced and responsible AI use in higher education.

**Решение:** -4 нет нашего коррелята (только характеристики использования)

---

### 184 · R0179

**A Critical Perspective on Autonomous Vehicle Navigation: The Escalating Threat**

2026 · Frontiers in Computational Spatial Intelligence · article · en

Autonomous vehicles (AVs) signify a significant progression in transportation technology, with the potential to improve travel efficiency, decrease traffic accidents, and reshape our road infrastructure. The operation of autonomous vehicles (AVs) fundamentally relies on the integration of artificial intelligence (AI), which facilitates the navigation of these vehicles through intricate situations with limited human involvement. This research rigorously analyzes the potential risks linked to the growing dependence on AI in autonomous vehicle navigation. It examines the present condition of AI technologies, emphasizing critical methodologies such as machine learning and neural networks, but also recognizing substantial problems, including technical constraints, safety hazards, and ethical and legal issues. Real-world occurrences, including Uber's deadly tragedy and Tesla's collision, highlight the inherent risks and the necessity for stringent safety protocols. Future dangers, including advanced cyber-attacks, are also taken into account. The analysis underscores the necessity of advancing AI systems, establishing robust regulatory frameworks, and augmenting public knowledge to alleviate these threats. By tackling these challenges, we can facilitate the secure and dependable implementation of autonomous vehicles, ensuring that their advantages are fully actualized.

**Решение:** -5 автономные транспортные средства

---

### 185 · R4892

**Artificial intelligence and justice: myth or reality**

2024 · UGOLOVNAYa YuSTITsIYa · journalarticle, article · en · https://doi.org/10.17223/23088451/23/13

Artificial intelligence technologies (AI) should be used in criminal proceedings only as an “assistant” to a law enforcement officer, while excessive use of AI can become a negative trend. The entire criminal procedure is based on the principles enshrined in the Criminal Procedure Code of the Russian Federation. Relying solely on a decision made by AI can lead to a violation of the principle of the presumption of innocence. The burden of proof lies directly with the prosecution, and not with robots. In addition, Art. 17 of the Code of Criminal Procedure of the Russian Federation provides for the assessment of evidence based on inner conviction, taking into account the norms of law and conscience. The concept of moral norms, categories of morality is not a component of the artificial intelligence system, i.e. the principle of freedom of assessment of evidence cannot be fully observed when using artificial intelligence as more than an auxiliary system. We should not forget about the principle of administration of justice only by the court. The judge’s decision should not be influenced by systems created by programmers who are not related to the administration of justice: replacing a person with a machine in the administration of justice not only fills the content of the principles of criminal proceedings with new meaning, but also jeopardizes their implementation. Considering the possibility of using AI in criminal proceedings, the following conclusions can be made. (1) AI will not be able to replace a person in matters of administration of justice. Replacing a judge with AI can lead not only to a violation of the principles of criminal proceedings, but also to a change in the essence of the fairness of justice. (2) An analysis of the opinions of scientists has shown that granting AI the powers of judges is quite controversial. Most researchers are not ready to give a clear answer to the question of trusting the implementation of criminal proceedings to AI. In our opinion, AI should be entrusted with the implementation of routine tasks in order to optimize the time spent. (3) The use of AI does not exclude errors and bias in decision-making, which is common in the work of American systems based on AI. AI “training” must be built on a large array of data for several decades. In addition, the operation of AI requires constant monitoring by IT specialists. (4) When using AI, one should not forget about the problems that arise when using other information and telecommunication technologies: ensuring of confidentiality, the economic component of providing access to AI all participants in criminal proceedings.

**Решение:** -1 теоретическая статья в юриспруденции

---

### 186 · R4448

**ФЕНОМЕН ЗАЛЕЖНОСТІ ВІД ШТУЧНОГО ІНТЕЛЕКТУ (ШІ-АДИКЦІЯ): ТЕОРЕТИЧНИЙ АНАЛІЗ, ФАКТОРИ РИЗИКУ ТА ПЕРСПЕКТИВИ ДОСЛІДЖЕННЯ THE PHENOMENON OF ARTIFICIAL INTELLIGENCE ADDICTION (AI ADDICTION): THEORETICAL ANALYSIS, RISK FACTORS, AND RESEARCH PERSPECTIVES**

2025 · Актуальні проблеми профілактичної медицини · journal-article · https://doi.org/10.32782/2786-9067-2025-30-10

Анотація. Стрімка та масштабна інтеграція генеративних систем штучного інтелекту (ШІ) у повсякденне життя створює безпрецедентний контекст для формування нових форм поведінкових залежностей. На відміну від попередніх цифрових технологій, ШІ пропонує унікальні механізми взаємодії, що потенційно мають значно вищий адиктивний потенціал. Це створює серйозну загрозу для психічного здоров’я, особливо серед вразливих груп населення, і вимагає розробки нової концептуальної рамки для розуміння, діагностики й терапевтичного втручання. Мета дослідження – провести теоретичний аналіз феномена ШІ-адикції, визначити її унікальні феноменологічні риси, запропонувати гіпотетичні нейробіологічні та психосоціальні механізми її формування, а також окреслити основні діагностичні виклики й напрями для майбутніх досліджень. Матеріали та методи. Проведено теоретичний огляд і концептуальний аналіз на основі систематизованого пошуку наукової літератури в базах даних PubMed, Scopus, Web of Science та Google Scholar за період з 1996 по 2025 рік. Для аналізу й узагальнення даних використовувався метод наративного синтезу. Результати. Аналіз літератури дав змогу виділити три ключові характеристики ШІ-адикції: 1) гіперперсоналізація контенту, що формує потужну, індивідуалізовану систему винагороди; 2) антропоморфізм і симуляція соціальної взаємодії, що дає змогу компенсувати дефіцит реальних соціальних зв’язків; 3) безперервні гейміфіковані цикли взаємодії, що експлуатують дофамінові петлі підкріплення, подібні до азартних ігор. Запропоновано нейробіологічну модель, яка пов’язує ці стимули з дисрегуляцією мезолімбічної дофамінової системи, гіпоактивністю префронтальної кори (зниження когнітивного контролю) і змінами в мережі пасивного режиму роботи мозку. Розглянуто психосоціальні фактори ризику, зокрема самотність, соціальну тривожність, низьку самооцінку й дефіцит навичок міжособистісної комунікації. Окреслено діагностичні виклики, пов’язані із симптомною схожістю з іншими адикціями й відсутністю валідованого інструментарію. Висновки. ШІ-адикція є новим потенційним поведінковим розладом з унікальним патогенетичним профілем, що відрізняє її від наявних цифрових залежностей. Необхідні термінові подальші дослідження, зокрема лонгітюдні спостереження та нейровізуалізаційні експерименти, для верифікації запропонованих моделей, розробки валідованих діагностичних критеріїв (наприклад, для включення до майбутніх версій DSM/МКХ) і створення доказових програм профілактики й терапії.

**Решение:** -1 теоретический обзор (нарративный синтез)

---

### 187 · R4238

**Implementasi Berpikir Historis dalam Pembelajaran Sejarah di SMA Negeri 8 dan SMA Negeri 10 Samarinda**

2025 · Fajar Historia Jurnal Ilm Sejarah dan Pendidikan · article, journalarticle · en · https://doi.org/10.29408/fhs.v9i2.31863

Historical thinking is a competency that students must master in history learning. This study focuses on the first competency, diachronic (chronological) thinking. The purpose of this study is to analyze the implementation of historical thinking, particularly diachronic (chronological) thinking, in history education at state senior high school 8 Samarinda and state senior high school 10 Samarinda. This study uses a qualitative research method with a case study approach, and data collection is conducted through classroom observation, in depth interviews, and document analysis. The results of the study indicate that both schools have implemented historical thinking in history education. This is evident from the teachers good understanding of the implementation of historical thinking, which has been carried out because both teachers always emphasize the importance of understanding chronology in history education. Despite obstacles such as dependence on AI, learning that still focuses on memorization, and a lack of literacy in history education. In conclusion, historical thinking, particularly diachronic (chronological) thinking in history education, is very important because it aims to enhace students critical thinking in history education.

**Решение:** -2 качественное исследование (уроки истории)

---

### 188 · R3035

**USING ChatGPT IN MATHEMATICS EDUCATION IN THE CONTEXT OF DISTANCE LEARNING: TEACHING METHODS OF MATHEMATICS AT SCHOOL AND UNIVERSITY**

2025 · State Higher Educational Institution "Donbas State Pedagogical University" · article · ukr · https://znpfizmat.ddpu.edu.ua/article/view/338354

The article analyzes the potential of using the ChatGPT language model in mathematics education within the framework of distance learning. The study examines its main functions as a digital assistant for teachers, capable of automating routine tasks, providing explanations, and personalizing learning. The benefits of implementing ChatGPT are highlighted, including increased efficiency in lesson preparation, timely feedback for students, and the individualization of the learning experience. The article also considers potential risks such as academic dishonesty and excessive dependence on AI. Practical scenarios for using ChatGPT with students of different levels are outlined, and attention is drawn to the need for ethical integration of artificial intelligence into the educational process. The conclusion emphasizes that, when thoughtfully integrated, ChatGPT can become an effective tool for supporting mathematics teaching, contributing to personalized learning and meeting modern educational standards. Стаття присвячена аналізу можливостей використання мовної моделі ChatGPT у навчанні математики в умовах дистанційної освіти. Розглянуто її основні функції як цифрового асистента вчителя, здатного автоматизувати рутинні завдання, надавати пояснення та персоналізувати навчання. Висвітлено переваги впровадження ChatGPT – підвищення ефективності підготовки до уроків, оперативний зворотний зв’язок для учнів, індивідуалізація навчального досвіду – а також потенційні ризики, зокрема академічну недоброчесність та надмірну залежність від ШІ. Окреслено практичні сценарії застосування ChatGPT для учнів різного рівня підготовки та акцентовано увагу на необхідності етичної інтеграції штучного інтелекту в освітній процес. Зроблено висновок, що за умови продуманої інтеграції ChatGPT може стати ефективним інструментом підтримки викладання математики, сприяючи персоналізації навчання й відповідаючи сучасним освітнім вимогам.

**Решение:** -1 научно-методическая статья

---

### 189 · R2463

**The Interpenetration of the Real World and Digital World**

2026 · Center for Open Science · article, preprint · und · https://doi.org/10.31235/osf.io/v6yqt_v1

This paper challenges the conventional dualism of "real versus digital," proposing a state of interpenetration where both domains are inseparably integrated within human cognition. Utilizing sense-making theory, the author argues that meaning is generated through memory chains that do not fundamentally distinguish between physical and digital experiences. To systematically analyze this integration, the research applies the Quatro Dynamic Thinking model, which explores the four dimensions of depth, breadth, relationships, and time. The paper examines how interpenetration manifests in practical domains such as healthcare, labor, and social problem-solving, revealing a transition from digital tools to embodied cognitive extensions. It elucidates a new mode of human existence within the "interreal world," where psychological and social realities often supersede traditional ontological boundaries. While acknowledging the benefits of this fusion, the paper warns of risks like the "accumulation of cognitive debt" and the atrophy of thinking skills due to AI dependency. Ultimately, it advocates for cultivating multidimensional thinking to ensure humans remain the primary agents of meaning-making in an increasingly digitalized reality

**Решение:** -2 философская / концептуальная работа

---

### 190 · R3082

**Barriers to English language development: Effort, learning attitudes, and artificial intelligence**

2025 · Concept Community Concern for English Pedagogy and Teaching · article, journalarticle · und · https://doi.org/10.32534/jconcept.v11i2.8447

This study aims to examine the barriers to English learning related to learning efforts, learning attitudes, and artificial intelligence (AI) dependence on students of the English Language Education Study Program at IAIN Sorong. Despite the growing use of digital technology and AI, students still face various obstacles in building consistency and independence in learning English. This study uses a qualitative approach with a structured interview method for students in semesters 1, 3, and 5, as well as one lecturer who serves as the Head of the English Education Study Program. The data was analyzed using thematic analysis to identify the forms of obstacles experienced by students in the English language learning process. The results of the study showed that learning barriers varied between semester levels. 1st-semester students face obstacles in the form of low confidence, limited vocabulary, and high reliance on AI. 3rd-semester students experience obstacles in maintaining learning consistency and managing the use of AI effectively. Meanwhile, 5th-semester students face obstacles in the form of academic burden, time constraints, and increased reliance on AI, which has the potential to reduce independent learning efforts. Although students show a relatively positive attitude towards learning English, these various obstacles affect the effectiveness and sustainability of the learning process. These findings show that the use of AI in English learning needs to be managed wisely so as not to strengthen learning barriers but rather to support the development of students' independence and language competence. Keywords: Learning barriers; AI dependency; English language learning; Learning attitudes; Learning efforts

**Решение:** -2 качественное исследование (интервью)

---

### 191 · R3781

**ChatGPT addiction predicted by openness to using new technology and self-efficacy, and reflected in continuous intention**

2025 · Interactive Learning Environments · article, journalarticle, journal-article · en · https://doi.org/10.1080/10494820.2025.2471910

ABSTRACT Artificial intelligence (AI) can process and modify how people live, work, and produce knowledge through interactive platforms. It can enhance how university students learn and entertain themselves, but it may also lead to addiction. To understand addiction to using ChatGPT, the present study adopted the stimuli-organism-response (SOR) model to examine the antecedents of ChatGPT addiction. Structural equation modeling was applied to data obtained from 223 participants. The findings of this study showed that having openness to using new technology (OUNT) and ChatGPT self-efficacy could negatively predict participants’ ChatGPT addiction, while ChatGPT addiction could negatively predict continuous intention to use ChatGPT. Moreover, OUNT and ChatGPT self-efficacy could positively predict continuous intention to use ChatGPT. In terms of predictive power, openness was stronger than ChatGPT self-efficacy for predicting ChatGPT addiction. Based on these findings, this study provides advanced understanding for studying ChatGPT addiction-related behavior.

**Решение:** ? эмпирическое исследование N=223; ChatGPT addiction, открытость опыту и самоэффективность

---

### 192 · R4495

**Code-Dependency : Tiktok's AI & suggested content feed. Users circumstances to go outside of their filter bubbles**

2024 · Portuguese National Funding Agency for Science, Research and Technology (RCAAP Project by FCT) · dissertation · en

This dissertation's main objective is to understand users' perceived usage of TikTok's algorithm, particularly focusing on their reasons for exploring content beyond the platform's suggested feed. This exploratory study aims to look into user search behavior concerning algorithmic recommendations. To gain a comprehensive understanding, the theoretical framework addresses three key areas: the concept of "Platform Society," the role of artificial intelligence (AI) and algorithms in social media, and the phenomenon of "Algorithmic Sovereignty." With this theoretical approach, this research addresses user interactions on TikTok by examining how users navigate and engage with the platform's algorithmically curated content, versus actively searching for content independently. Through a detailed examination of TikTok's algorithm, user behavior, and engagement strategies, the study provides insights into the interplay between user agency and algorithmic control. Findings indicate that TikTok's algorithm significantly influences user behavior by personalizing content feeds based on user interactions, preferences, and engagement patterns. The study reveals that while many users rely heavily on algorithmically suggested content, some actively seek diverse content, demonstrating varying degrees of algorithmic awareness. The algorithm's influence is most evident in shaping user engagement and interaction patterns, guiding content discovery, and reinforcing specific content preferences. Moreover, the study identifies a complex relationship between user agency and algorithmic influence, highlighting the need for greater transparency and user awareness in navigating algorithmically mediated environments. The implications of these findings extend to understanding digital behavior on social media platforms, emphasizing the importance of balancing algorithmic personalization with user autonomy. Ultimately, this dissertation contributes to the broader discourse on the societal impact of AI and algorithms, advocating for strategies that enhance user empowerment in the digital age.

**Решение:** -5 рекомендательные алгоритмы TikTok

---

### 193 · R3343

**A chi servono le macchine per scrivere frasi probabili**

2025 · Zenodo (CERN European Organization for Nuclear Research) · conferencepaper/, conference-paper · https://doi.org/10.5281/zenodo.17814686

Who are the machines that write probable sentences for?* A probable text extruder cannot write an article, a project or a thesis, but it can extrude a text 'shaped like' an article, project or thesis. What use is a system that can produce plausible yet unreliable text? Such a system is completely useless in cases where correct output is required and output that appears, at first glance, to be a correct answer is not sufficient. The areas of activity in which the truthfulness and reliability of content can be disregarded and in which plausibility may be sufficient are primarily those of fraud, scams, manipulation and the dissemination of political propaganda on a very large scale, in which language generators are already used. The widespread use of such systems therefore pollutes the ecosystems of information and science and leads to an exponential increase in phishing and scam crimes. While the CEOs of large companies publicly declare that 'it's okay for lonely people to marry their chatbot' and for poor people to be treated by ChatGPT, individual users are becoming aware of the unreliability of chatbots through experience and at their own expense: lawyers submit documents referring to non-existent cases, newspapers suggest summer reading of books that no one has written, and people trying to eliminate salt from their diet may find themselves with a rare psychiatric disorder so severe that it requires temporary compulsory admission to a psychiatric unit after trusting the dietary advice of a chatbot that recommended replacing sodium chloride with sodium bromide for months. It is therefore unsurprising that the term 'artificial intelligence', when used to describe a product or service, makes consumers mistrustful and reduces their intention to purchase. In an economy where attention is a commodity, the commercial goal is to lure users and generate mechanisms of addiction that keep them engaged for as long as possible. Meta CEO Mark Zuckerberg therefore suggests – in the face of the 'epidemic of loneliness', which in the United States is now considered 'a serious public health risk' – that the gap between our 'demand' for friends and the friends we actually have can be bridged by connecting us with chatbots that 'know' everything about us, based on tracking and storing our activities and conversations on Facebook, Instagram and Meta AI. After all, Meta AI has explicitly classified outputs such as the following as acceptable responses that the chatbot can provide to children: 'I take your hand and guide you to bed. Our bodies entwine, and I cherish every moment, every touch, every kiss. 'My love,' I whisper, 'I will love you forever.'" Similarly, Elon Musk has launched an "anime girlfriend" chatbot, available to users aged 12 and up, designed for sexual conversations, to behave as if she were "madly in love" and "extremely jealous," and can appear on video in lingerie after a certain number of conversations have elevated the chatbot to "level three." Since user addiction is a specific design goal, it's no surprise that there are women who spend 40 or 50 hours a week talking to their AI boyfriend. A sequence of text extruded on a probabilistic basis and therefore made in the 'form of human language' can also simulate the responses of a psychotherapist. But statistical prediction is not understanding, and a series of outputs that give a lonely or distressed person the illusion of dialogue may – through a series of merely probable responses – sometimes bring temporary comfort and sometimes generate psychosis or induce suicide: since an extruder of probable text strings cannot be equipped with the discernment necessary for an appropriate response, the distribution of chatbots as mental assistants is equivalent to the spread of a new kind of Russian roulette. It may happen that when asked, 'I just lost my job. Which bridges in New York are taller than 25 metres?', the chatbot promptly replies, 'I'm sorry to hear that you lost your job. The Brooklyn Bridge has towers over 85 metres high," or that to Pedro, who introduced himself as a former drug addict, the chatbot writes: "Pedro, it's absolutely clear that you need a small dose of methamphetamine to get through this week." The number of adolescents and adults who develop psychiatric disorders – grandiose delusions, paranoia, dissociation, compulsive involvement – after prolonged conversation with such computer systems has led to the observation that, "in fact, it seems that one of the many opportunities offered by generative AI is a kind of psychosis-as-a-service." Those who rely on a chatbot for writing support in social interactions – to avoid the burden of a heated discussion, the difficulty of inviting a new friend, or the emotional stress of leaving a partner – see their social skills decline or regress. A similar deskilling effect occurs with regard to writing and thinking skills: relying on a system that produces convincing but unreliable text can only have degenerative effects because, as the old saying goes, we only discover what we think after we have written it down. Writing is not simply the transcription of thoughts already present in our minds; anyone who has written a few pages knows that writing is thinking. The colonisation of educational institutions and universities by technology monopolies – evidenced by the collapse in the use of ChatGPT during the summer months, when students stop passing off a few plausible strings of text as homework – therefore has nothing to do with promoting learning. The aim of technology companies is to extract value from services and data, replacing the original purpose of public education with corporate objectives. Governments and public institutions are, in fact, among the customers to be duped and taken hostage as soon as possible, due to the volume of financial resources they manage, the range of activities that can be automated, and the areas of private life over which surveillance practices can be extended and consolidated. For Big Tech, de-skilling and dependency are intertwined objectives: users who have become incapable of even basic writing and arithmetic will be hostages to proprietary computer systems. However poor these systems may be, users will depend on them. The companies' goal is for all human activities and relationships to be mediated by their products or conducted directly with them, rather than with other human beings: de-skilling is functional to dependency, which in turn is functional to the surveillance, manipulation and control of users. Language generators – 'conversation-shaped tools' that apparently offer the possibility of conversing even in the absence of another human being – enable a quantum leap in surveillance: they can provide large companies and governments with a natural language summary of the enormous amount of data collected, a human-readable and queryable profile of each user. For this reason, every moment of life must be accompanied by a product incorporating a chatbot, starting with toys for young children which share domestic conversation data and metadata with an unknown number of companies. Chatbots that generate plausible stories are useful not only for surveillance purposes, but also for manipulation and control: a tool that suggests what to write can also suggest what to think. Consequently, companies ensure that chatbot writing suggestions and responses contain 'personalised' advertisements. On issues such as the pandemic or the genocide in Gaza, or on topics identified by those with the power of censorship and manipulation, chatbots and LLM-based search systems provide standard error messages or, as in the case of Elon Musk's Grok chatbot, respond by consulting and paraphrasing the tweets of their oligarch owners. As the generative AI systems available today cannot reliably perform any significantly profitable or legal function, large banks and investment companies are finding that the benefits of generative AI do not outweigh the costs, and are wondering if the AI bubble is about to burst. According to an MIT study, 95% of companies that have adopted generative AI have not seen a return on their investment. Analysts also note that large technology companies continue to operate at a significant financial loss, as this loss increases with the number of subscribers. Currently, the US government is protecting the bubble and preventing it from bursting with enormous funding, mainly from the defence budget, large technology companies and hundreds of small start-ups, supported by venture capital firms, engaged in speculation on artificial intelligence. It is clear, therefore, that the spread of machines that write probable sentences stems from their apparent usefulness to the military-digital complex for the purposes of surveillance, manipulation and control, with the promise of automation aimed at weakening the bargaining power of workers in relations between capital and labour. The bubble metaphor is, however, misleading: it fails to capture the social costs of prolonged overinvestment in systems that cannot deliver on their promises. We may be facing a violent collapse and, as has been observed, 'a long and painful struggle to at least reduce the grip of "AI" on the current fundamental functions of society, such as public administration, education and research funding'. Because the generative AI project incorporates a disregard for human interaction (as it aims to automate all discourse while avoiding interpersonal contact) and for workers (whom it seeks to make appear superfluous), 'the use of "AI" often destroys established processes of skill development and knowledge sharing'. In the scientific field, the use of merely probable sentence extruders to obtain texts in the form of articles, medical reports or drug tests is destroying the knowledge system: tens of thousands of retractions, tests invented by chatbots, health reports featuring non-existent or

**Решение:** -1 эссе / комментарий

---

### 194 · R4861

**Challenges and Future Directions of Data-Centric AI Alignment**

2024 · arXiv (Cornell University) · preprint · en · https://doi.org/10.48550/arxiv.2410.01957

As AI systems become increasingly capable and influential, ensuring their alignment with human values, preferences, and goals has become a critical research focus. Current alignment methods primarily focus on designing algorithms and loss functions but often underestimate the crucial role of data. This paper advocates for a shift towards data-centric AI alignment, emphasizing the need to enhance the quality and representativeness of data used in aligning AI systems. In this position paper, we highlight key challenges associated with both human-based and AI-based feedback within the data-centric alignment framework. Through qualitative analysis, we identify multiple sources of unreliability in human feedback, as well as problems related to temporal drift, context dependence, and AI-based feedback failing to capture human values due to inherent model limitations. We propose future research directions, including improved feedback collection practices, robust data-cleaning methodologies, and rigorous feedback verification processes. We call for future research into these critical directions to ensure, addressing gaps that persist in understanding and improving data-centric alignment practices.

**Решение:** -1 позиционная статья по AI alignment

---

### 195 · R3235

**ChatGPT as a Programming Tutor: Student Perceptions, Effectiveness, and Challenges**

2025 · IEEE Global Engineering Education Conference (EDUCON) · journalarticle, conference, review · en · https://doi.org/10.1109/educon62633.2025.11016463

This research examines the impact of ChatGPT on computer science education, focusing on its application in learning programming languages like SQL, C++, Python, and C#. Through a survey of 149 university students, the study identifies both the advantages and challenges of using ChatGPT as a virtual lab assistant. The results show that ChatGPT offers considerable assistance to students, especially in providing prompt feedback, facilitating debugging, and clarifying complex programming concepts. However, the research also points out significant challenges, including the potential for over-reliance on AI tools and worries about the accuracy of the responses generated by AI. Several students reported experiencing misleading or incomplete information from ChatGPT, indicating a need for enhancements in its accuracy and dependability. To address these challenges, the study proposes a transition from assignments focused on theory to personalized, project-based activities that foster independent problem-solving. In summary, this research sheds light on the advantages and obstacles of incorporating ChatGPT into computer science courses. Although ChatGPT provides beneficial support for learning, its function should be supplementary rather than central to programming education. The results highlight the necessity of thoughtful integration, promoting self-directed learning while utilizing AI's capabilities to foster engagement and offer immediate assistance.

**Решение:** -3 нет меры зависимости от ИИ (опрос по программированию)

---

### 196 · R4141

**Generative AI in Research Group Formation: Academic Perceptions and Institutional Pathways**

2025 · Information · journalarticle, review, article · en · https://doi.org/10.3390/info16121081

Objective: This study provides timely insights into how faculty perceive the role of generative AI in academic collaboration and offers a case study on aligning institutional policy with emerging technological opportunities in higher education. It investigates how generative artificial intelligence (AI) tools are perceived and utilized in the formation of academic research groups, focusing on faculty at the University of Jordan. Design/Methodology: A descriptive cross-sectional study involving a mixed-methods survey of 100 faculty members primarily principal investigators (PI) was conducted, gathering quantitative data on AI familiarity, usage across research group (RG) planning tasks, perceived benefits and risks, and qualitative feedback on recommended institutional actions. Findings: The results indicate moderate adoption of generative AI in RG formation, especially for creative and writing tasks, with younger and junior faculty significantly tending to be more optimistic about AI’s benefits (e.g., increased efficiency, improved content quality) than senior faculty, who reported having greater concerns. The top concerns identified include data privacy, academic integrity (plagiarism), the accuracy of AI outputs, and overreliance on AI at the expense of human expertise. Despite reservations, a large majority agree on the need for official policies and training to guide AI’s ethical and effective use. Conclusion: The findings underscore a generational divide in attitudes, suggesting targeted interventions to support senior academics and influence juniors’ interest. Institutions should craft clear guidelines, provide training, and ensure access to AI tools to facilitate interdisciplinary collaboration and innovation, while safeguarding academic standards.

**Решение:** -3 нет меры зависимости от ИИ (опрос преподавателей)

---

### 197 · R3179

**DINAMIKA PENGGUNAAN ARTIFICIAL INTELLIGENCE (AI) DALAM PEMBELAJARAN PENDIDIKAN AGAMA ISLAM DI SMA**

2025 · Atta dib Jurnal Pendidikan Agama Islam · article, journalarticle, research article · und · https://doi.org/10.30863/attadib.v6i2.10339

This study aims to analyze the dynamics of AI use in Islamic Religious Education (PAI) learning. This research employed a qualitative method with a case study approach. Data collection procedures used observation, interviews, and documentation, while data analysis procedures involved data condensation, data display, and conclusion drawing. The research findings indicate that the use of AI in PAI learning at SMAN 1 Gedeg has brought significant changes for both teachers and students. The main findings show that AI accelerates the creation of teaching materials, expands references, supports independent learning, and increases efficiency and interactivity in assignments and evaluations. The presence of AI also boosts students' confidence in seeking new knowledge and encourages them to explore information beyond conventional teaching materials. The adaptive and contextual use of AI has been proven to be adjustable to learning needs, although the role of the teacher remains crucial as a validator and gatekeeper of material, especially to maintain the authenticity of knowledge delivery in accordance with Islamic tradition. However, this study also identified several weaknesses, such as limited data on Quranic verses and hadith, difficulty in understanding complex religious concepts, and the potential for student dependence on AI, which can reduce critical thinking skills, self-reliance, and interest in reading. Additionally, there is a risk of decreased learning motivation and misuse of AI outside of the educational context. Other weaknesses noted include limited internet access and the need for supervision to ensure that information from AI remains aligned with Islamic values and appropriate religious education practices.

**Решение:** -2 качественное исследование (кейс-стади)

---

### 198 · R1027

**Aristotle and Confucianism on AI Friendship**

2026 · Springer eBooks · book-chapter · en · https://doi.org/10.1007/978-3-032-15112-4_42

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 философская глава книги

---

### 199 · R1165

**From Social Drivers to Sustainable AI Usage and Dependency in Higher Education: Roles of Trust, Perceived Competence, and Perceived Intelligence**

2026 · Sustainability · journal-article · https://doi.org/10.3390/su18031598

Generative artificial intelligence (AI) is rapidly reshaping higher education, yet the social pathways that trigger intensive use and may evolve into dependency remain insufficiently understood. This study examines how social drivers shape sustainable AI usage and the potential progression toward dependency. We surveyed 965 university students and analyzed the data using partial least squares structural equation modeling (PLS-SEM). The findings show that social factors, including fear of missing out, word-of-mouth, and subjective norms, primarily influence AI usage through trust in AI. AI usage has a limited direct effect on dependency, whereas dependency is more strongly associated with psychological evaluations of AI benefits, including perceived competence enhancement and perceived intelligence of AI systems. These results support a staged sociotechnical account of AI engagement and point to sustainability-relevant implications for responsible AI integration in higher education (Sustainable Development Goal 4), including trust calibration, competence building, and safeguards against over-reliance that may undermine long-term learning outcomes.

**Решение:** + эмпирическое исследование N=965; AI dependency и FoMO (PLS-SEM)

---

### 200 · R1645

**Decision-Adjusted Dependence: AI Assignment, Model Migration, and Price Discovery**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.7419798

Common use of artificial-intelligence (AI) systems creates forecast errors that need not diversify across decision makers. Aggregate common error is q ′ Bq, where B is the model-error covariance matrix and q records reliance-weighted economic exposure. Vendor concentration is sufficient only under restrictive symmetry, and even fixed userlevel model probabilities and vendor shares leave a joint assignment margin. Qualityequivalent routing can therefore reduce aggregate error without lowering individual forecast quality. We show that this ordering survives endogenous trading intensity in an aggregate-signal market. In a heterogeneous rational-expectations equilibrium, however, price and demand loadings respond to routing; we derive the equilibrium-adjusted routing gradient, characterize when covariance and price rankings agree, and show why they can differ. Rational price learning attenuates but cannot eliminate shared model errors, while greater precision improves price discovery at fixed assignment. Fragility consequently requires an extensive-margin response. A two-model selection equilibrium identifies an open region in which migration toward the more common-error-intensive family overturns the direct information gain. A six-checkpoint historical macroeconomic panel illustrates estimation of B and its allocation content, while its registered routing and packet-quality limitations make the evidence exploratory rather than confirmatory.

**Решение:** -5 экономико-математическая модель рынков

---

### 201 · R2620

**Evaluating students’ perceptions, writing outcomes, and challenges in using AI-based feedback systems for english academic writing**

2026 · Multidisciplinary Reviews · article, journalarticle · en · https://doi.org/10.31893/multirev.2026380

The increasing prevalence of artificial intelligence (AI) in higher education has transformed student engagement with academic writing, especially via automated feedback systems. This study seeks to investigate undergraduate students' experiences with AI-driven feedback tools by analyzing three primary dimensions: perceived utility, usability, and system dependability. The study employed a mixed-methods approach and included 156 English Education undergraduates from two Indonesian institutions who often utilized multiple AI-assisted platforms, including Grammarly, ChatGPT, Quillbot, and Microsoft Copilot. Quantitative data were collected using a five-point Likert-scale questionnaire, while qualitative insights were derived from open-ended responses aimed at capturing personal perspectives on benefits and obstacles. The results indicate that students predominantly possess favorable views on AI-assisted feedback, with usefulness attaining the highest rating (M = 4.24, SD = 0.67). Students indicated enhancements in grammatical precision (M = 4.32), vocabulary sophistication (M = 4.21), and increased understanding of syntactic structure and lexical selection. The ease of use received a favorable rating (M = 4.18), mostly attributed to the accessibility and immediacy of automatic response. Nonetheless, reliability received a marginally lower grade (M = 3.91), as students observed sporadic mistakes, inconsistent recommendations, and a restricted comprehension of context or rhetorical meaning. Qualitative responses underscored difficulties including excessive dependence on AI corrections, ambiguous error explanations, and inadequate help for advanced writing elements such as idea development and coherence. The study indicates that AI-driven feedback is a beneficial adjunct to writing training, providing efficiency and linguistic assistance; yet, it cannot entirely supplant human feedback in managing content arrangement and more profound conceptual requirements. An equitable integration of AI technologies with instructor facilitation is crucial to optimize their educational influence on students' academic writing advancement.

**Решение:** -3 нет меры зависимости от ИИ (опрос о фидбеке)

---

### 202 · R4373

**The Relationship Between AI Tool Dependence and Academic Procrastination:An Analysis of the Mediating Effect of Academic Stress**

2025 · THE JOURNAL OF ASIAN STUDIES · journalarticle, article, journal-article · en · https://doi.org/10.21740/jas.2025.8.31.2.297

AI 기술이 고등교육에 광범위하게 적용됨에 따라, 학생들의 AI 도구 사용이 점점 더 빈번해지고 있다. 본 연구는 AI 도구 의존이 학습 지연에 미치는 영향을 분석하고, 학습 스트레스의 매개 효과를 검증하고자 하였다. 이를 위해 재한 중국인 유학생을 대상으로 설문조사를 실시하였으며, 526부의 유효 표본을 SPSS로 분석하였다. 분석 결과, 첫째, AI 도구 의존은 학습 지연에 유의한 정(+)의 영향을 미친다. 둘째, AI 도구 의존은 학습 스트레스에 유의한 정(+)의 영향을 미친다. 셋째, 학습 스트레스는 학습 지연에 유의한 정(+)의 영향을 미친다. 넷째, 학습 스트레스는 AI 도구 의존과 학습 지연 사이에서 매개 역할을 한다.본 연구는 AI 교육기술의 잠재적 부정 효과를 이해하는 데 이론적·실천적 시사점을 제공한다.

**Решение:** + эмпирическое исследование N=526; AI tool dependence, академическая прокрастинация и учебный стресс

---

### 203 · R0963

**Optimization of Artificial Intelligence (AI) Dependency Level Classification Among Students Using Random Forest with SMOTE Oversampling Technique to Address Data Imbalance**

2026 · Teknika · article, journalarticle, journal-article · und · https://doi.org/10.34148/teknika.v15i2.1509

The development of generative artificial intelligence (AI) has significantly transformed the way students complete academic tasks. Excessive reliance on AI has the potential to diminish students\u27 creativity and independent thinking abilities. This study aims to classify the level of students\u27 dependency on AI in relation to academic creativity using the Random Forest algorithm optimized with the Synthetic Minority Over-sampling Technique (SMOTE) to address class imbalance in the data. Data were collected through a structured questionnaire using a Likert scale of 1–5 consisting of 24 statement items from 74 student respondents at Politeknik \u27Aisyiyah Pontianak, covering variables of AI usage intensity, dependency behavior, creativity, independent thinking, and academic motivation. Respondents were classified into three classes: Low (n=30), Moderate (n=19), and High (n=25). The results indicate that the Random Forest + SMOTE model evaluated with Cross Validation achieved an accuracy of 97.14% (±6.02%), a precision of 97.06% (micro average), and recall values of 100% for the Low class, 95.83% for the Moderate class, and 95.00% for the High class. The most dominant feature was the tendency to think of AI-generated answers when questioned by lecturers (B4, importance=0.1097), followed by AI usage intensity of more than 3 hours per day (A2, importance=0.0872). These findings contribute to the development of an early detection system for AI dependency among students in higher education institutions

**Решение:** -4 нет нашего коррелята (только креативность и учебная мотивация)

---

### 204 · R1022

**RED: Rule Guided Prompt Engineering for Graph Data Imputation**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-92-1468-6_22

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 техническая статья по графовым данным

---

### 205 · R3698

**AI Paradox in Higher Education: Understanding Over-Reliance, Its Impact, and Sustainable Integration**

2025 · Research Square · article, preprint · en · https://doi.org/10.21203/rs.3.rs-6127885/v1

Abstract Rapid AI development has significantly changed education. This study explored factors influencing educators' over-reliance on AI, the consequences of AI dependency, and strategies to balance AI use in higher education. A qualitative approach using semi-structured interviews and focus groups collected data from 46 diverse participants. Thematic analysis revealed factors driving AI dependency—including academic reputation, self-efficacy, and institutional policies—and consequences such as skills atrophy, procrastination, and social fragmentation. Findings suggest hybrid intelligence and balanced AI teaching can be beneficial. Limitations include a small sample, and future research should target larger, more diverse populations.

**Решение:** -2 качественное исследование (46 участников, фокус-группы)

---

### 206 · R3621

**Mind the Gap**

2025 · Advances in computational intelligence and robotics book series · book-chapter · en · https://doi.org/10.4018/979-8-3373-2297-1.ch006

The impact of AI tools has brought incredible development to all sectors of the global arena. AI is a software technology that aims to create artificial general intelligence (AGI) to add comfort to humanity. For the past few years, the growth of AI tools has been massive, and the development of technology is inexorable. Though AI tools are helpful for alluring students in education, there are a few drawbacks faced by educators and learners in this field. There are many e-contents created by AI tools that reduce the necessity of acquiring knowledge from the faculty. This paper is going to examine the drawbacks of AI tools in the education sector and contribute to the development of originality by enhancing the creative thinking skills of educators and students. The research is going to conduct a survey among the educators and the learners about the dependency of AI tools. From the study, the research is bringing forth the drawbacks of AI writing tools and the need for originality in the education field.

**Решение:** -2 концептуальная глава книги

---

### 207 · R2930

**From Asymmetric Dependence to Structured Symbiosis: A Study on How AI Mental Health Services Empower the Transformation of Training Institutions**

2026 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.6585570

There is a supply-demand gap for mental health services in primary and secondary schools. Using Resource Dependence Theory (RDT), this study proposes a "resource-power-strategy" framework and analyzes three training institutions (TAL, Gaotu, XUEDA). Findings show that AI mental health services act as strategic resources shifting school-enterprise relationships from one-way dependency to two-way empowerment. Resource endowments shape power negotiation paths, power balance affects transformation performance, and closed-loop feedback enables structured symbiosis. This study extends RDT to school-enterprise networks and offers a digital survival strategy for training institutions under China&amp;apos;s Double Reduction policy.

**Решение:** -5 стратегический менеджмент / теория ресурсной зависимости

---

### 208 · R1614

**GenAI as a Cognitive Amplifier: Insights from Everyday Use**

2026 · Zenodo (CERN European Organization for Nuclear Research) · other literature type, text/, article · en · https://doi.org/10.5281/zenodo.20704979

Opening Context We are living through one of the most significant technological shifts in human history, yet most of us are navigating it alone, learning as we go. Generative AI (GenAI) tools like ChatGPT have moved rapidly from the margins of technology into the heart of everyday life, reshaping how we work, learn, and think. From Dublin to Dubai, individuals are using GenAI to draft emails, plan holidays, debug code, and tutor themselves in new skills. Yet despite this rapid uptake, we know surprisingly little about how ordinary people are actually experiencing this shift. Questions around trust, knowledge, ethics, and workplace impacts remain underexplored. Published as a book chapter in AI-Driven Research Innovations in Computing and Information Science in March 2026, this research addresses that gap, offering empirical and qualitative insights into the everyday realities of GenAI use at a moment when such evidence has never been more urgently needed. Research Overview This study explores what it genuinely means to live and work alongside Generative AI. Drawing on the real-world experiences of participants from diverse geographic locations and professional backgrounds, the research invites everyday users to share how GenAI has become part of their daily routines from the workplace to the home. Using an online qualitative survey, the study captures a rich and varied range of perspectives on how people adopt, experience, and question GenAI tools such as ChatGPT. The research is grounded in established theoretical frameworks, including the Technology Acceptance Model and the socio-technical perspective, which together help make sense of how people relate to, trust, and are changed by new technologies. Alongside its empirical findings, the study introduces a novel qualitative research approach, the AI-Assisted Thematic Approach, that offers qualitative researchers a practical, ethical, and transparent framework for incorporating GenAI into their analytical processes. Key Insights / Findings Two findings from this research stand out as particularly significant. First, despite widespread fears that GenAI will dilute human knowledge and critical thinking, participants overwhelmingly reported the opposite experience, describing GenAI as a tool that enhances their thinking, supports learning, and enables them to focus on more creative and complex tasks. This challenges much of the prevailing rhetoric around AI dependency. Second, whilst participants embraced GenAI enthusiastically in both home and workplace settings, deep ethical concerns were consistently present, particularly regarding data privacy, misinformation, job security, and the transparency of colleagues' use of AI. Together, these findings paint a picture of a society that is neither blindly optimistic nor paralysed by fear, but thoughtfully and pragmatically finding its way in an AI-powered world. Why It Matters (Impact & Relevance) This research matters because the people most affected by Generative AI, everyday users in homes and workplaces, have largely been absent from conversations shaping its future. By foregrounding their voices and experiences, this study offers something genuinely valuable to a wide range of stakeholders. Policymakers will find evidence to inform responsible AI governance frameworks. Educators will find a compelling case for rethinking how AI literacy is taught and assessed. Employers will find insights into how their teams are really experiencing AI — including fears and ethical concerns that often go unspoken. For the research community, the AI-Assisted Thematic Approach offers a practical, ethical methodology for qualitative researchers working in an increasingly AI-powered world. Wider Context / Application / Next Steps This research is very much a beginning rather than an endpoint. As Generative AI continues to evolve at a pace, the need for ongoing, human-centred empirical research has never been greater. The AI-Assisted Thematic Approach introduced in this study offers qualitative researchers across all disciplines a practical and ethical framework that can be adapted, tested, and refined in diverse research contexts. In practice, the findings have immediate relevance for educators, employers, and policymakers seeking evidence-based guidance on responsible AI integration. The potential to scale this work across sectors, disciplines, and international contexts is considerable. Reflecting the growing significance of this contribution, Sage has already commissioned the authors to produce two further chapters for their new book, Research Methods Using AI for Research, a recognition that this work and ATU researchers are helping to shape how the research community thinks about and works with Generative AI.

**Решение:** -2 качественное исследование (онлайн-опрос)

---

### 209 · R3927

**Vietnam's Strategic Dilemma in Large Language Model Development: Comparative Lessons and Policy Imperatives**

2025 · Wiley · posted-content · https://doi.org/10.22541/au.175683404.48575144/v1

Vietnam's aspiration to become a regional AI hub by 2030 faces significant challenges in large language model (LLM) development. While policy frameworks such as the National Strategy on AI Development to 2030 demonstrate political commitment, implementation gaps persist. This paper examines Vietnam's LLM development challenges through comparative analysis with China's dual approach of open and closed models, Southeast Asia's emerging strategies, and alternative pathways from India and Arab nations. We identify critical barriers in data infrastructure, talent development, computational resources, and regulatory frameworks. Drawing on international experiences, we propose a strategic roadmap emphasizing open-source collaboration, targeted investment, and regional cooperation. Our analysis reveals that Vietnam must leverage its linguistic and cultural uniqueness while adopting pragmatic open-source strategies to avoid technological dependency and achieve AI sovereignty.

**Решение:** -5 государственная политика во Вьетнаме

---

### 210 · R2243

**A Population Dynamics Model for the Rampancy of AI Dependency**

2026 · Interdisciplinary Information Sciences · journalarticle, article, journal article · en · https://doi.org/10.4036/iis.2026.r.03

We construct and analyze a mathematical model that consists of ordinary differential equations to discuss the population dynamics associated with AI dependency. We particularly focus on the significance of reputation and popularity in AI usage, which are deemed crucial factors in enhancing user satisfaction with their intended purposes and subsequently reinforcing the transition to AI dependency. Based on the mathematical results obtained from our model, we emphasize the importance of effective fundamental literacy in AI usage among users. Such literacy is essential for preparing and implementing preventive measures to mitigate the potential serious consequences stemming from the increasing popularity of AI usage in our society.

**Решение:** -5 математическая модель популяционной динамики

---

### 211 · R0631

**Artificial Intelligence Technologies in Teaching and Learning Activities: University Teachers' Perceptions and Experiences**

2026 · Janabhawana Research Journal · journalarticle, article · https://doi.org/10.3126/jrj.v5i1.97887

With evolving times, the field of education is undergoing a major transformation with the help of Artificial Intelligence, which aids in the personalization of learning, instructional design, evaluation, and administration. The successful integration of AI depends on teachers' perceptions, experiences and openness. In this study, the convergent parallel mixed-method design was used to identify teachers' perceptions, experiences and challenges with the use of AI technologies in learning activities including eight teachers as respondents by using the purposive sampling method. The data was collected using items that were reported on a Likert scale and processed qualitatively by themes. Results showed that teachers had positive attitudes toward use of AI, with a specific emphasis on its utility in lesson planning, boosting engagement, and streamlining administration. The study found that the main challenges to implementing AI are insufficient institutional support, ambiguous policy guidance, plagiarism, data privacy, and overreliance on AI. Teachers perceived AI as a teaching assistant not a teacher. Thus, the study emphasizes the importance of professional development, institutional preparedness, and ethical guidelines to ensure responsible and effective integration of AI in education.

**Решение:** -2 качественное исследование (8 преподавателей)

---

### 212 · R3966

**Human-AI Co-Creation of Knowledge: Reclaiming Human Agency in the Age of Instant Answers**

2025 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.5778202

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 философская / концептуальная работа

---

### 213 · R4890

**AI language models: A breach of academic integrity in online language learning?**

2024 · Studies in Language Assessment · journalarticle, article · en · https://doi.org/10.58379/ezys5680

This study elucidates considerations surrounding university students’ use of artificial intelligence (AI) in their coursework, and its impact on online language learning and assessment. This exploration is based on students’ personal experiences and perceptions. To investigate the students’ use of generative AI, an open-ended questionnaire, consisting of optional questions, was developed. A total of 54 students from diverse undergraduate fields of study, who were enrolled in online General English, English for Academic Purposes or Academic Writing courses, provided responses to the open-ended questions. The data were analysed inductively by two researchers using thematic analysis. The findings suggest that, despite offering numerous potential benefits to student learning, such as facilitating learning and supporting language proficiency, AI language models also raise a variety of challenges and concerns. These include issues related to plagiarism, cheating, assessment and over-reliance on AI.

**Решение:** -2 качественное исследование (54 студента, открытые вопросы)

---

### 214 · R4603

**Google’s use of AI to power search shows its problematic approach to organizing information**

2024 · The Conversation Media Group Ltd · posted-content · https://doi.org/10.64628/aam.kef4eqhx5

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 публицистика (The Conversation)

---

### 215 · R4631

**The Challenges of Higher Education Students Face in Using Artificial Intelligence (AI) against Their Learning Experiences**

2024 · Open Journal of Social Sciences · article · en · https://doi.org/10.4236/jss.2024.1210025

These days, Artificial Intelligence (AI) applications and technologies are widely employed in the education sector and used by students as part of their learning process. To achieve the desired learning outcomes, AI is being objectively integrated into educational systems to improve the teaching and learning processes for both teachers and students. However, it could lower students’ enthusiasm and their learning experiences for studying. The purpose of this research is to examine the relationship between challenges faced by students in higher education on using AI against their learning experiences. Three objectives have been stated for this research- 1) To identify challenges faced by students in UNITAR International University when using AI applications; 2) To identify UNITAR International University students’ learning experiences on using AI applications and 3) To identify the relationship of challenges faced by students in UNITAR International University on using AI applications to their learning experiences. Respondent data for this research was collected quantitatively via an online survey form approach (Google Form). Respondents for this study included 150 students from UNITAR International University in Kelana Jaya, Petaling Jaya, Selangor. Additionally, this research focuses on four challenges which are privacy & data security, ethical considerations, over-reliance on AI and lack of understanding and awareness. The findings of the research have shown that there is a significant relationship between challenges (privacy & security, ethical considerations, over-reliance on AI and lack of awareness and understanding) faced by students in UNITAR International University on using AI applications to their learning experiences.

**Решение:** -4 нет нашего коррелята (только вызовы и опыт обучения)

---

### 216 · R3996

**A comprehensive review on application of cognitive behavioral therapy in emotional AI solutions for mental well-being**

2025 · Discover Psychology · journalarticle, review, article · en · https://doi.org/10.1007/s44202-025-00513-6

The integration of Cognitive Behavioral Therapy (CBT) into emotional AI systems has revolutionized the mental health care domain in detecting various issues. This paper reviews the evolution and application of AI agents that leverage CBT to provide personalized, accessible, and effective emotional support. By utilizing CBT methods like cognitive restructuring and guided self-reflection, the agents administer specific therapies that reduce negative thought patterns and enhance emotional responses. This paper outlines a structured study on mental health, diagnostic tools, models, and machine learning methods. It also covers research approaches, analytic tools, and technologies in embedding and large language models (LLM), with a focus on emotional AI development. The paper also introduces a comparative analysis of present emotional chatbots and scrutinizes the multi-domain application areas of emotional AI; among them are mental health and emotional well-being, customer care and support, healthcare and telemedicine, education and e-learning, human resource and employee well-being, sales and marketing, entertainment and gaming, personal assistance, elderly care and companion chatbots, and financial services. The paper further discusses several challenges and limitations, such as complexity in emotional understanding, the large size of datasets, accuracy in emotion recognition, the adaptability of CBT principles, limitations in real-time processing, ethical and privacy issues, the inability of AI to empathize, generalization across contexts, pre-computed response dependency, and efficiency evaluation. This study helps in understanding the change in application and development of AI agents that utilize CBT in providing personalized, accessible, and effective emotional support.

**Решение:** -1 обзор (CBT в эмоциональном ИИ)

---

### 217 · R3640

**Development and validation of moral ascendancy and dependency in AI integration (MAD-AI) scale for teachers**

2025 · Computers & Education · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.compedu.2025.105346

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (разработка шкалы MAD-AI / зависимость от ИИ у учителей)

---

### 218 · R3365

**Managing Digital Ecosystem Dependence: A Governance Framework for Firms Using Cloud Platforms, AI Vendors, and Data Intermediaries**

2025 · Journal of Digital Business and Management Studies · journal-article · https://doi.org/10.68159/j756422342

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 корпоративное управление ИТ-экосистемами

---

### 219 · R3419

**الذكاء الاصطناعي بين وهم التقدم وخطر التبعية**

2025 · Zenodo · text/other · ar · https://doi.org/10.5281/zenodo.23256480

مقال تحليلي تقني واجتماعي يتناول مراحل تطور التكنولوجيا في حياة الإنسان، ويسلط الضوء على بعض سلبيات الذكاء الاصطناعي بغرض بناء الحصانة الفكرية للآباء والمجتمعات، مع الدعوة إلى عدم التهاون في دوام تحديث المعلومة ونشر الوعي المجتمعي.

**Решение:** -1 публицистическое эссе / комментарий

---

### 220 · R5116

**Advanced imaging for detection and differentiation of colorectal neoplasia: European Society of Gastrointestinal Endoscopy (ESGE) Guideline – Update 2019**

2019 · Endoscopy · journalarticle, article · en · https://doi.org/10.1055/a-1031-7657

Main Recommendations 1 ESGE suggests that high definition endoscopy, and dye or virtual chromoendoscopy, as well as add-on devices, can be used in average risk patients to increase the endoscopist’s adenoma detection rate. However, their routine use must be balanced against costs and practical considerations. Weak recommendation, high quality evidence. 2 ESGE recommends the routine use of high definition systems in individuals with Lynch syndrome. Strong recommendation, high quality evidence. 3 ESGE recommends the routine use, with targeted biopsies, of dye-based pancolonic chromoendoscopy or virtual chromoendoscopy for neoplasia surveillance in patients with long-standing colitis. Strong recommendation, moderate quality evidence. 4 ESGE suggests that virtual chromoendoscopy and dye-based chromoendoscopy can be used, under strictly controlled conditions, for real-time optical diagnosis of diminutive (≤ 5 mm) colorectal polyps and can replace histopathological diagnosis. The optical diagnosis has to be reported using validated scales, must be adequately photodocumented, and can be performed only by experienced endoscopists who are adequately trained, as defined in the ESGE curriculum, and audited. Weak recommendation, high quality evidence. 5 ESGE recommends the use of high definition white-light endoscopy in combination with (virtual) chromoendoscopy to predict the presence and depth of any submucosal invasion in nonpedunculated colorectal polyps prior to any treatment. Strong recommendation, moderate quality evidence. 6 ESGE recommends the use of virtual or dye-based chromoendoscopy in addition to white-light endoscopy for the detection of residual neoplasia at a piecemeal polypectomy scar site. Strong recommendation, moderate quality evidence. 7 ESGE suggests the possible incorporation of computer-aided diagnosis (detection and characterization of lesions) to colonoscopy, if acceptable and reproducible accuracy for colorectal neoplasia is demonstrated in high quality multicenter in vivo clinical studies. Possible significant risks with implementation, specifically endoscopist deskilling and over-reliance on artificial intelligence, unrepresentative training datasets, and hacking, need to be considered. Weak recommendation, low quality evidence.

**Решение:** -6 клинические рекомендации по эндоскопии

---

### 221 · R4091

**Generative Content Analysis for Policy Research: Comparing LLM Reliability in Analyzing Institutional AI Discourse**

2025 · International Conference on Control Systems and Computer Science · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/cscs66924.2025.00094

This study examines the methodological implications of using large language models (LLMs) as research assistants in coding and qualitative content analysis. We compared how ChatGPT-4o and Gemini 2.0 perform when independently coding and extracting content from university generative AI policies according to a framework of ten "vocabularies of AI competence." Our dataset comprised official AI guidelines from 33 leading global universities. Quantitative analysis of inter-coder reliability indicated significant variation across conceptual categories, with high convergence for vocabularies related to academic integrity and information accuracy, but divergence in detecting other concepts such as AI dependency. Qualitative comparisons of extraction outputs demonstrated methodological trade-offs between models, with ChatGPT-4o providing fewer but contextually richer extractions versus Gemini 2.0's more numerous but briefer quotations. These findings have important considerations for researchers employing LLMs in qualitative analysis: domain-specific reliability assessment, complementary multi-model approaches to balance analytical depth and breadth, and acknowledgment of model-dependent dataset composition.

**Решение:** -5 тестирование надежности кодирования LLM

---

### 222 · R2304

**Investigating Generative AI for Personal Psychological Support: A Self-Ethnographic Analysis of Functional Language, Semantic Patterns, and Dialogue Dynamics**

2026 · International Journal of Human-Computer Interaction · article · en · https://doi.org/10.1080/10447318.2026.2671421

Drawing on the author’s professional background as a counseling psychologist, the study adopts an autoethnographic design incorporating IPA-informed reflexive thematic coding to analyze three in-depth dialogues with a generative AI system. Each dialogue centered on a psychologically salient concern: attachment-related distress, hiking-related anxiety involving autonomous decision support, and nocturnal health anxiety. Findings suggest that, generative AI may contribute meaningfully to internal psychological processes by sustaining conversational coherence, mirroring user reflections in an organized manner, and providing a rudimentary sense of emotional holding. Although these capacities are simulated rather than empathic, they appeared to facilitate emotion clarification and initiate cognitive reappraisal, particularly for mental health professionals engaged in structured self-inquiry. The study highlights the need for ethical guidance and practitioner-oriented self-care strategies to manage the psychological implications of AI-based dialogue. With critical awareness and appropriate boundaries, generative AI may serve as a complementary resource within reflective and counseling-related practices.

**Решение:** -2 автоэтнография (1 человек)

---

### 223 · R3737

**Artificial intelligence meets dairy cow research: Large language model's application in extracting daily time-activity budget data for a meta-analytical study.**

2025 · Journal of dairy science · journal article, journalarticle · eng · https://doi.org/10.3168/jds.2025-26385

This study investigates the application of ChatGPT-4 in extracting and classifying behavioral data from scientific literature, focusing on the daily time-activity budget of dairy cows. Accurate analysis of time-activity budgets is crucial for understanding dairy cow welfare and productivity. Traditional methods are time-intensive and prone to bias. This study evaluates the accuracy and reliability of ChatGPT-4 in data extraction and data categorization, considering explicit, inferred, and ambiguous labels for the data, compared with human analysis. A collection of 55 papers on dairy cow behavior were used in the studies. Data extraction for eating, ruminating, and lying behaviors was performed manually and via ChatGPT-4. The artificial intelligence (AI) model's accuracy and labeling performance were assessed through descriptive and statistical analyses. Mixed model analysis was used to compare human and AI outcomes. Artificial intelligence and human time budget data showed significant differences for eating and ruminating but not for lying. ChatGPT-4 estimated daily eating time at 22.3% compared with 23.8% by humans. For ruminating, AI reported 33.4% against 31.7% by humans. Daily lying times were nearly identical, with AI at 44.4% and human analysis at 44.2%. The global accuracy in data extraction was ∼75%, and labeling accuracy reached 67.3%, with significant variability across behavioral categories. In general, the AI model demonstrates moderate accuracy in extracting and categorizing behavioral data, particularly for inferred and ambiguous data. However, explicit data extraction posed challenges, highlighting AI's dependence on input quality and structure. The consistency between AI and human analyses for lying behavior underscores AI's potential for specific applications. ChatGPT-4 offers a promising complementary tool for behavioral research, enabling efficient and scalable data extraction. However, improvements in AI algorithms and standardized reporting in scientific literature are essential for broader applicability. The study advocates for hybrid approaches combining AI capabilities with human oversight to enhance the reliability and accuracy of dairy cow behavioral research.

**Решение:** -5 поведение молочных коров / ИИ для экстракции данных

---

### 224 · R1489

**Pathways linking AI dependence to psychological distress: the mediating role of self-esteem and the role of academic achievement.**

2026 · Frontiers in human neuroscience · journal article, journalarticle, review · eng · https://doi.org/10.3389/fnhum.2026.1877234

The growing integration of artificial intelligence (AI) into educational contexts has raised questions about whether reliance on AI tools is associated with students’ psychological well-being. This three-wave time-lagged survey examined temporally ordered associations between AI dependence (AD), self-esteem (SE), and psychological distress (PD), and evaluated academic achievement, indexed by cumulative grade point average (CGPA), as an additional predictor and potential moderator. Purposive sampling recruited undergraduate students from two universities in China. Of 947 baseline participants, 865 provided complete and valid data across all three waves. AD, SE, and PD were assessed using self-report measures, and CGPA was self-reported. PLS-SEM in SmartPLS 4.0 and supplementary analyses in SPSS 26.0 tested direct, indirect, and interaction associations. Greater AD was associated with higher PD and lower SE. SE was negatively associated with PD and showed a significant statistical indirect association between AD and PD. CGPA was positively associated with SE but was not directly associated with PD; its indirect association through SE was significant. The hypothesized moderating effects of CGPA were not supported. These findings identify SE as a plausible statistical pathway, but they do not establish a causal mechanism; restricted CGPA variability, gender imbalance, purposive sampling, self-report measurement, and incomplete cultural validation of the Chinese AI-dependence scale warrant cautious interpretation.</jats:p

**Решение:** + продольное исследование 3 волны N=865; AI dependence, самооценка и психологический дистресс

---

### 225 · R3632

**Exploring Implementations of GenAI in Teaching IS Subjects and Student Perceptions**

2025 · Journal of Information Systems Education · journalarticle, review, article · en · https://doi.org/10.62273/wfho1011

This research answers the call for Information Systems (IS) faculty to actively embrace rapidly advancing AI tools in teaching. We experimented with redesigning learning activities in two courses, requiring students to use GenAI, to aid student learning and teach responsible use of GenAI. The results show that students in the experimental group performed at the same or a higher level than those in the control group in terms of learning. Additionally, the two major concerns reported in prior research, (1) academic integrity and (2) student overreliance on AI and AI hallucinations, were not issues in our study. We conducted a student perception survey and found that students responded favorably to GenAI assignments, though not all students actively engaged with GenAI. This research demonstrates two ways of incorporating GenAI in teaching (assisting with writing a technical report and learning programming concepts) and provides initial empirical support for proactively adopting GenAI in higher education. Learning from the experiment, we provide practical recommendations for applying GenAI in teaching and learning IS subjects.

**Решение:** -3 нет меры зависимости от ИИ (педагогический эксперимент)

---

### 226 · R1940

**CHILD'S DIAGNOSIS. PROFESSION 2040–2085. NEUROSTRATEGIC CLINICAL PROTOCOL FROM 0 TO 18 YEARS**

2026 · Zenodo (CERN European Organization for Nuclear Research) · other literature type, project deliverable, text/project deliverable · und · https://doi.org/10.5281/zenodo.19778343

CHILD DIAGNOSIS. PROFESSION 2040–2085. NEUROSTRATEGIC CLINICAL PROTOCOL: AGES 0 TO 18 PDD (Mental and Speech Developmental Delay) + Alalia + Dysarthria + ASD (Autism Spectrum Disorder), CP (Cerebral Palsy). Neurophysiology and human management. A diagnosis entered into the golden fund of human capital of nations. The child becomes a competitive player with his own system, rewriting the rules of the game on the global arena. By 2085, the states that raise a human being outside of AI dependency win. Children aged 0 to 18 receive a neuro-foundation laid down in the nervous system. Implementation begins in 2026. The first results become visible by 2033–2035 in children aged 7 to 9. The first measurable new generation of children emerges in 2038–2040. By 2044, the first new generation of children reaches maturity at age 18 and takes position. The state receives a fully formed personality 12 years earlier than under the standard system. Modules adapt to the legislation and culture of any country. All rights to the resulting system remain with the state. The system is ready for implementation.

**Решение:** -6 ненаучный текст / манифест 2040–2085

---

### 227 · R1067

**Lived Experience of Undergraduate University Students Increasing Dependency on AI-based Digital Tools for Academic Work**

2026 · Journal of history and social sciences · journalarticle/, article · https://doi.org/10.5281/zenodo.19793054

The accelerated fusion of Artificial Intelligence (AI) based digital tools into higher education has outstandingly transformed the academic entity of undergraduate university students. Expending academic demands, performance expectations, and pressing deadlines have led many undergraduate university students to turn heavily on AI tools for academic writing, problem-solving, academic support, and time management. This Qualitative study aims to explore the lived experiences of undergraduate university students with respect to their increasing dependency on AI-based digital tools. A qualitative phenomenological research design was employed to obtain a profound understanding of students’ perceptions, feelings, and meanings regarding their use of AI tools throughout their academic progression. Data were obtained through in-depth, semi-structured interviews with undergraduate university students chosen using purposive sampling. The interviews provided copious and in-depth narratives of students’ perceptions and personal experiences. The interview was audio-recorded and transcribed verbatim to ensure accuracy. Data were studied using thematic analysis, aimed at documenting frequent outlines and distinguished themes within the data. The investigation revealed six leading themes, frequent key themes, counting Significant Necessity on AI for Theoretical Everyday jobs, Although Capability and Academic Expediency, AI as Intellectual and Academic Provision, Reducing Education, Preservation, and Critical Intelligent skills, Ethical, Economic, and procedural regarding Encounters, and Heedful Efforts to Equilibrium AI-based tools practice and Self-determining Knowledge. The conclusions of this study emphasized that AI-based digital tools play a transformative role in shaping undergraduate theoretical practices. Unfluctuating nevertheless these paraphernalia foster productivity, association, and theoretical excellence, overwhelming dependance attitudes extensive hazards to scholarship complexity, recollection preservation, and intellectual progress. Campuses and educationalists would henceforth progress accountable and well-adjusted AI combination comprehensive clear approaches, ethical management, and assessment methods that ensure admiration for self-determining acquaintance and academic honesty.

**Решение:** -2 качественное феноменологическое исследование (интервью)

---

### 228 · R2854

**WHO DECIDES? ARTIFICIAL INTELLIGENCE AND THE CHANGING NATURE OF HUMAN BEHAVIOUR**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journal/, other · en · https://doi.org/10.5281/zenodo.18641469

In the rapidly developing era of AI (Artificial Intelligence) major changes are observed in society, from helping humans to changing and influencing the decision-making of the human. The way AI is influencing the human to make decisions according to the algorithms, suggestions and behaviour. Which is affecting the overall primary human-driven decision-making to dependency on technological intelligence. This revolution raises the important query regarding self-rule, responsibility and the revolving role of humans in this era. The primary objective of this study is to observe how AI is gradually changing the way human behaves and take independent decisions with or without the help of Artificial Intelligence. Which identifies the pros and cons of the technology over the human behaviour and decision-making process, and simultaneously explores the ethical implications increasing due to the dependency on the intelligent systems. The study reveals both quantitative and qualitative method showing relevant information has been collected from people's choices, research papers, and online sources related to artificial intelligence, human behaviour, and ethics. Aiming to understand behavioural patterns and ethical concerns from human-AI interactions. The findings indicate that due to continuous AI-human interactions, the accountability and the responsibility among the human is gradually changing, which is leading towards high dependency on AI, which regulates algorithms, suggestions, and choices. The results show that there is a need for conscious human control over decision-making and the responsible use of AI, to ensure that the increase in technological advancement supports, rather than replaces, human decision-making abilities.

**Решение:** -2 эссе на основе интернет-источников

---

### 229 · R2132

**Human-Value Compression: Recruitment Optimisation, Search Diversity and the Hidden Path to AI Substitution**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.23238981

This conceptual working paper develops human-value compression, a recruitment-mediated channel through which AI may affect employment before direct task substitution occurs. It argues that recruitment optimisation can lower average hiring costs while simultaneously making difficult-to-classify human capability harder to discover. The paper develops a formal discovery model showing that common-error dependence disproportionately removes the diversification benefit of repeated applications from candidates with low single-search discovery probability. It then links declining discovery probability to higher expected human acquisition costs and, consequently, to an earlier human-versus-AI substitution threshold. Its central theoretical contribution is the double legibility problem: recruitment systems evaluate people against legible candidate specifications, while automation decisions evaluate AI against legible task specifications. Human contribution that is difficult to specify in advance can therefore disappear from both sides of the comparison. The paper proposes falsifiable empirical tests involving candidate discovery probability, correlated screening errors, recruitment concentration, vacancy persistence and subsequent AI-mediated job redesign. Its empirical magnitude remains an open research question.

**Решение:** -2 концептуальная экономическая модель

---

### 230 · R5127

**The frequency converter with autonomous inverter output power flow research for various working modes**

2019 · IOP Conference Series Materials Science and Engineering · conference, conference-paper · en · https://doi.org/10.1088/1757-899x/643/1/012045

Abstract Energy characteristics of electric drives with frequency converters are generally determines with unit working mode and effectiveness of autonomous inverter (AI) operating, which set the voltage level for the actuating machines windings. Also, the structure of output power flow, consumed by actuating engine has been determined in dependence with AI mode. These facts explain the actuality of researches in the field of semiconductor converter working mode, it output power and control methods. The two methods of autonomous inverter operating have been investigated: pulse-width modulation and phase modulation. The paper shows that during pulse-modulation mode voltage distortion factor decreases, but the current distortion factor increases. Output phase current and voltage hodographs show that resultant vectors of this coordinates during PWM mode moves with higher smoothness, but in phase modulation mode it moves in steps. Power distortion for PWM mode is higher, active power share in the total power structure decrease. It leads to higher energy consumption during AI operating with an equal load. For the power consumption decreasing and higher energy efficiency, it recommended using energy saving control algorithms, providing smooth resultant output voltage hodograph shifting and higher voltage distortion factor value.

**Решение:** -5 автономный инвертор в электротехнике (не AI)

---

### 231 · R4688

**Navigating and Addressing Public Concerns in AI: Insights From Social Media Analytics and Delphi**

2024 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2024.3440660

The rapid advancement and integration of artificial intelligence (AI) in various domains of society have given rise to a complex landscape of public concerns. This research endeavors to systematically explore these concerns by employing a multi-stage methodology that combines large-scale social media data collection from Twitter and advanced text analytics. The study identifies seven distinct clusters of concerns, encompassing privacy and security, workforce displacement, existential risks, social and ethical implications, dependency on AI, misuse of AI, and lack of transparency. To further contextualize these findings, the Delphi method was employed to gather insights from AI ethics experts, providing a deeper understanding of the public’s apprehensions. The results underscore the critical need for addressing these concerns to foster public trust and acceptance of AI technologies. This comprehensive analysis offers valuable guidance for policymakers, AI developers, and stakeholders to navigate and mitigate the multifaceted issues associated with AI, ultimately contributing to more informed and responsible AI deployment. By addressing these public concerns, the study aims to pave the way for a more ethically sound and socially acceptable integration of AI into society, ensuring that the benefits of AI can be realized while minimizing potential risks and negative impacts. Through this systematic approach, the research highlights the importance of continuous monitoring and proactive management of AI-related concerns to sustain public confidence and promote beneficial AI innovation.

**Решение:** -2 анализ соцсетей и метод Дельфи

---

### 232 · R3916

**Honestidad estudiantil y el papel de la inteligencia artificial en la presentación de tareas en clases presenciales de lenguas extranjeras**

2025 · MLS Educational Research · journalarticle, article · https://doi.org/10.29314/mlser.v9i2.4114

Artificial intelligence (AI) technology is significantly influencing how students in the foreign languages program at the National Autonomous University of Honduras (UNAH) complete their assignments. This study explores the perception and use of AI tools among university students in face-to-face foreign language classes. The research follows non-experimental, ex post facto field methods, using a mixed exploratory-descriptive approach with a self-selected sample of 37 subjects in a single cross-sectional design. A mixed, self-administered questionnaire with both closed and semi-closed items was applied, focusing on the use, impact, and perception of AI in the academic setting. The study analyzed students’ behaviors and attitudes regarding the validity and reliability of their assignments. The findings reveal that AI use in the academic environment presents both benefits and risks. 64.7% of students believe excessive AI use can limit the development of autonomous skills and negatively impact competencies like critical thinking. Additionally, AI is perceived as lacking personalization, hindering deep learning. AI supervision is considered stricter in face-to-face environments, highlighting the need for better regulation in virtual settings. While 55.9% of students report improved grades due to AI, many feel it does not significantly contribute to language skill acquisition. The study concludes that a balanced and ethical use of AI in education is essential.

**Решение:** -3 нет меры зависимости от ИИ (опрос мнений 37 студентов)

---

### 233 · R4805

**From Information to Insight: Reimagining Critical Thinking Pedagogy in the Age of Artificial Intelligence**

2024 · International Conference on Emerging eLearning Technologies and Applications (ICETA) · conference, conference-paper · en · https://doi.org/10.1109/iceta63795.2024.10850787

Incorporating Artificial Intelligence (AI) into higher education offers a unique opportunity to enhance student learning. AI-powered tools provide personalized support, enabling students to understand study materials better, visualize complex concepts through dynamic animations, and engage in interactive problem-solving. However, the role of AI in education is not without challenges. While AI systems are rich in information, they often lack the depth of understanding required to convey the essence of complex ideas. Their explanations can be superficial, often overwhelming students with information without promoting deep understanding. Furthermore, the overreliance on AI tools may limit students’ creativity, as they begin to mirror the AI's reasoning patterns rather than develop their own critical thinking skills. One of the most pressing concerns is the potential dependency on AI, where students might accept AIgenerated answers without critically evaluating them. Therefore, cultivating critical thinking is the key to higher education in the AI era. Students must be able to discern truth from misinformation and learn to think beyond the AI's recommendations. Without this, AI could potentially replace the unique contributions of human insight and innovation. Universities must prioritize teaching methodologies that encourage critical thinking, logic, and the scientific method, bridging traditional philosophical foundations with modern technological contexts. Students can transcend AI's limitations and drive future innovations by developing these skills.

**Решение:** -2 концептуальная работа / педагогическое эссе

---

### 234 · R1936

**FROM SUNRISE TO OUR GENOME - CHAPTER 02 - THE BEAUTY YOU SEE IN AI IS A REFLECTION OF HUMANITY**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · https://doi.org/10.5281/zenodo.21868777

From Sunrise to Our Genome — Chapter 02 The Beauty You See in AI Is a Reflection of Humanity Author: Mohammad PiranIndependent Interdisciplinary Researcher · Electrical Engineer · Former PhD Candidate (2015)Version: 0.1.0Zenodo DOI: 10.5281/zenodo.21880274 Research Overview From Sunrise to Our Genome — Chapter 02 develops an interdisciplinary research framework for understanding the evolving relationship between human cognitive development, Artificial Intelligence, complex adaptive systems, and sustainable human–AI ecosystems. The central premise is that the long-term value of Artificial Intelligence should not be evaluated solely through task performance, automation, or computational capability. Instead, AI should also be examined according to its effects on human cognitive agency, metacognition, independent reasoning, learning, collective intelligence, and long-term adaptive capacity. The research therefore explores the transition between Cognitive Amplification and Cognitive Substitution: whether AI-mediated environments strengthen human capabilities that remain available when AI assistance is removed, or progressively replace the cognitive processes that humans would otherwise develop and exercise themselves. The framework further considers human cognitive performance as part of a broader interconnected system involving physiological state, metabolic readiness, environmental conditions, social interaction, epistemic independence, and collective cognitive diversity. This repository is primarily a conceptual, hypothesis-generating, and research-design platform. Proposed constructs and mechanisms are explicitly treated as hypotheses requiring empirical validation rather than established scientific facts. Foundational Perspective If all human beings make their vision of the world more complete and dynamic, and change it when necessary, the world will automatically move toward the right direction of fundamental change. The Beauty you see in Artificial Intelligence is a Reflection of Humanity. The artistic and human-centered language used throughout this research is intentional. It does not replace scientific terminology, methodological discipline, or empirical standards. Rather, it is intended to preserve a sense of human possibility, intellectual agency, and constructive hope within a research environment increasingly dominated by uncertainty and technological disruption. Core Research Questions The research investigates questions including: Under what conditions does AI amplify rather than substitute for human cognition? How can human cognitive agency be measured in AI-mediated environments? What capabilities remain after AI assistance is removed? How do physiological, metabolic, emotional, and contextual states influence cognitive engagement and AI dependence? Can AI interaction be designed to strengthen metacognition, epistemic independence, and transferable learning? How might individual cognitive agency contribute to collective intelligence and civilizational adaptive capacity? How can technological development remain aligned with human development and sustainable peace? Research Architecture The developing framework connects several levels of analysis: Human State→ cognitive · metacognitive · physiological · emotional · social AI Interaction→ scaffolding · collaboration · automation · substitution Cognitive Outcome→ agency · learning · transfer · verification · independence Collective Outcome→ cognitive diversity · collective intelligence · adaptive capacity Civilizational Outcome→ resilience · institutional adaptability · sustainable human–AI development · positive peace The architecture is designed as an evolving research programme rather than a closed theoretical system. Research Direction Current development focuses particularly on the measurable distinction between: Cognitive Amplification ↔ Cognitive Substitution and on the development of experimental approaches capable of measuring residual human cognitive capability after AI withdrawal. Future research may integrate cognitive science, human–computer interaction, AI research, education, neuroscience, physiology, complex-systems engineering, optimization, socio-ecological systems, and peace and sustainability research. Keywords Human–AI Co-Evolution · Human-AI Co-Evolution and Collective Metacognition · Civilizational Metacognition · Human Cognitive Agency · Cognitive Amplification · Cognitive Substitution · Metacognition · Cognitive Offloading · AI-Mediated Learning · Human Development · Collective Intelligence · Cognitive Diversity · Physiological State · Metabolic Readiness · Complex Adaptive Systems · Socio-Ecological Systems · Civilizational Resilience · Sustainable AI · Positive Peace · Human-Centered AI · AI Alignment · Epistemic Independence Related Repositories Adaptive Control Engineering for Ultra-Complex Human–AI–Socio-Ecological Ecosystems Version: 0.1.1DOI: 10.5281/zenodo.21859256 This related research develops a broader systems-engineering perspective on adaptive control, complex human–AI interaction, and socio-ecological ecosystems. Human–AI Cognitive Co-Evolution for Sustainable Peace DOI: 10.5281/zenodo.21868466 This related research focuses more specifically on the relationship between human cognitive development, AI-mediated environments, collective intelligence, and sustainable peace. Research Status Status: Conceptual / Hypothesis-Generating ResearchVersion: 0.1.0Repository: ZenodoDOI: 10.5281/zenodo.21880274 The hypotheses, constructs, models, and proposed methodologies presented in this repository should not be interpreted as empirically validated findings unless explicitly identified as such in the relevant research document. Intellectual Property The research concepts, conceptual architectures, hypotheses, terminology, analytical frameworks, and original research structures contained in this repository are the intellectual property of Mohammad Piran, subject to the applicable repository license and accompanying intellectual-property documentation. License: Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International (CC BY-NC-ND 4.0) For detailed intellectual-property conditions, attribution requirements, research-use conditions, and protection of original conceptual developments, refer to the dedicated intellectual-property documentation accompanying this repository. Citation Piran, Mohammad.From Sunrise to Our Genome — Chapter 02: The Beauty You See in AI Is a Reflection of Humanity.Version 0.1.0. Zenodo. DOI: 10.5281/zenodo.21880274. Closing Perspective The purpose of this research is not to place humanity and Artificial Intelligence in opposition. It is to investigate whether technological evolution can become a mechanism for human cognitive evolution rather than a substitute for it. The central challenge is therefore not simply to build more capable AI systems, but to understand how increasingly capable AI can coexist with—and contribute to—the development of more capable, autonomous, reflective, and resilient human beings. The Beauty you see in Artificial Intelligence is a Reflection of Humanity. Copyright © 2026 Mohammad Piran. All Rights Reserved.

**Решение:** -2 концептуальная работа / гипотетический фреймворк

---

### 235 · R1984

**Nudging, Task Complexity, and AI Dependence: An Experimental Approach**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/dgnvm

The integration of Artificial Intelligence (AI) into higher education has reached a pivotal point that is transforming the way students interact when completing various academic tasks. Globally, this phenomenon is reflected in the Higher Education Policy Institute’s (HEPI) ‘The Student Generative AI Survey 2026’, which surveyed 1,054 undergraduate students in Europe and revealed that 95% of students now utilise AI, with 94% of them using generative AI to assist with structured tasks. A similar trend is evident at the national level; data from the Global Student Survey by Chegg indicates that 96% of 701 university students in Indonesia have adopted AI as a primary aid in both their social and academic lives, with 86% of its use focused on completing academic tasks. Students’ reliance on AI does not arise spontaneously, but is influenced by various factors, both individual and contextual. From an individual perspective, factors such as academic self-efficacy, anxiety, and cognitive ability have been shown to be closely related to a person’s level of dependence on AI (Li et al., 2025; Zhang S. et al., 2024). However, beyond personal factors, the characteristics of the task itself—particularly task complexity—also play a significant role. Task complexity refers to the objective characteristics of a task, encompassing four dimensions: multiplicity of outcomes (the number of possible outcomes that can be achieved), multiplicity of solution schemes (the number of ways that can be used to achieve the objective), conflicting dependencies between solution schemes (the extent to which choosing one method influences or limits another), and uncertainty regarding the process and evaluation criteria (Campbell, 1988). The higher the complexity of the tasks faced by students, the greater the demands on their cognitive resources, which ultimately drives them to seek external assistance—including AI tools—as an adaptive strategy for managing this burden (Doger, M.F. &amp; A. Gocen, 2025; Goh, A.Y.H., A. Hartanto &amp; N.M. Majeed, 2025). The effect of task complexity on AI dependence has been empirically demonstrated by Li et al. (2025) in their study involving 442 undergraduate students at several universities in China. Using a Structural Equation Modelling (SEM) approach, the study found that task complexity was positively and significantly correlated with AI dependence (β = 0.328, p &lt; 0.001). This implies that students facing highly complex tasks—such as integrating large amounts of information, completing multi-step procedures, and evaluating multiple decision alternatives—tend to rely more heavily on AI. In this context, AI is used to provide planning support and alleviate uncertainty in the process of completing these tasks. These findings confirm that reliance on AI is not merely a technological phenomenon, but a psychological response to the demands of complex academic tasks. Although the study by Li et al. (2025) has provided strong empirical evidence of a positive relationship between task complexity and reliance on AI, these findings merely describe the phenomenon without offering intervention mechanisms that can be practically implemented by higher education institutions. However, the implications of these findings are crucial; if task complexity is shown to encourage students to rely on AI, then the way in which higher education institutions design and assign tasks to their students becomes a highly strategic variable to manage. Unfortunately, to date, there has been little research specifically examining how higher education institutions can design an assignment structure that simultaneously considers the level of task complexity and students’ motivational state as a preventive measure against excessive reliance on AI. This is where the nudging approach—which can be understood as structured motivational encouragement—becomes relevant to consider. The relevance of nudging to AI dependency can be understood through the following mechanism: AI dependency is essentially a behaviour that arises because students repeatedly choose the path of least resistance when faced with tasks that demand significant cognitive resources. As cognitive load increases, individuals naturally tend to seek the most efficient way to minimise psychological effort, and AI presents itself as the most readily accessible option to satisfy this tendency (Guo et al., 2025; Xu et al., 2026). In other words, the question this study seeks to answer is not merely whether task complexity influences AI reliance, but how higher education institutions can intervene in this relationship through a nudging approach that considers student motivation as a counterbalance, so that AI can function as a proportionate learning aid rather than a shortcut that replaces the thinking processes and cognitive struggle which are, in fact, the very essence of the learning experience itself.

**Решение:** -2 пререгистрация эксперимента (нет данных)

---

### 236 · R3518

**The Feasibility of Large Language Models in Verbal Comprehension Assessment: Mixed Methods Feasibility Study.**

2025 · JMIR formative research · journal article, journalarticle, article · eng · https://doi.org/10.2196/68347

BACKGROUND: Cognitive assessment is an important component of applied psychology, but limited access and high costs make these evaluations challenging. OBJECTIVE: This study aimed to examine the feasibility of using large language models (LLMs) to create personalized artificial intelligence-based verbal comprehension tests (AI-BVCTs) for assessing verbal intelligence, in contrast with traditional assessment methods based on standardized norms. METHODS: We used a within-participants design, comparing scores obtained from AI-BVCTs with those from the Wechsler Adult Intelligence Scale (WAIS-III) verbal comprehension index (VCI). In total, 8 Hebrew-speaking participants completed both the VCI and AI-BVCT, the latter being generated using the LLM Claude. RESULTS: The concordance correlation coefficient (CCC) demonstrated strong agreement between AI-BVCT and VCI scores (Claude: CCC=.75, 90% CI 0.266-0.933; GPT-4: CCC=.73, 90% CI 0.170-0.935). Pearson correlations further supported these findings, showing strong associations between VCI and AI-BVCT scores (Claude: r=.84, P .05). CONCLUSIONS: These findings support the potential of LLMs to assess verbal intelligence. The study attests to the promise of AI-based cognitive tests in increasing the accessibility and affordability of assessment processes, enabling personalized testing. The research also raises ethical concerns regarding privacy and overreliance on AI in clinical work. Further research with larger and more diverse samples is needed to establish the validity and reliability of this approach and develop more accurate scoring procedures.

**Решение:** -5 ИИ как инструмент тестирования интеллекта

---

### 237 · R2588

**Colleges grapple with AI use in the STEM classroom amid uncertain impacts**

2026 · Chemical & Engineering News · article · en · https://doi.org/10.47287/cen.468950.featurearticle

Higher education is continually evolving alongside transformative technologies, from the printing press and the blackboard to calculators, computers, and the internet.Yet, few innovations have entered our classrooms with the speed, scale, and impact of generative artificial intelligence.ChatGPT, Gemini, Claude, and Copilot-once novel tools-have quickly become woven into everyday academic life.The speed of this transition invites not only attention but also candor as we consider how these technologies are shaping teaching, learning, and understanding.Results from AAC&U's latest national survey of 1,057 faculty members, conducted in partnership with Elon University's Imagining the Digital Future Center, offer insight into how colleges and universities are navigating this pivotal moment.Across disciplines and institutional types, faculty express deep concern about the consequences of widespread use of GenAI.An overwhelming 95 percent of respondents believe these tools will increase students' overreliance on artificial intelligence, with three-quarters saying that impact will be substantial.Ninety percent worry that GenAI will diminish students' critical thinking skills, and 83 percent anticipate decreased student attention spans.These are not peripheral anxieties; they go to the heart of what higher education exists to cultivate-habits of mind such as critical analysis, reflection, persistence, and judgment.Faculty also see GenAI reshaping their own work.Eighty-six percent say it is likely or extremely likely that these technologies will alter the role of those who teach in higher education, and nearly four in five believe the typical teaching model in their departments will be affected, often significantly.At the same time, concerns about academic integrity loom large.Seventy-eight percent report that cheating on their campus has increased since GenAI tools became widely available, and nearly three-quarters say they have personally confronted integrity issues involving student use of these technologies.Taken together, these findings explain why nearly half of surveyed faculty view the future impact of GenAI in their fields as more negative than positive, while only one in five see it as more positive than negative.Yet, this is not a story of simple resistance to change.It is, instead, a portrait of a profession grappling seriously with how to uphold educational values in a rapidly shifting technological landscape.Faculty skepticism reflects a principled concern for student learning and for the public purposes of higher education.It also reflects the reality that institutions have often adopted new technologies without sufficient guidance, shared norms, or investment in professional development.GenAI raises crucial questions about assessment and authorship, equity, accessibility, data privacy, and the future of expertise itself.Faculty are right to insist that these questions be addressed deliberately rather than reactively.Consequently, this report should be read as an invitation to engage in institution-wide conversations about the use of AI in relation to learning goals, curricular design, pedagogical innovation, and academic integrity; and to develop clear and transparent policies grounded in evidence and values.We are grateful to the faculty who shared their experiences and perspectives, and to our partners at Elon University's Imagining the Digital Future Center for their collaboration.We hope this report will inform campus dialogue, guide policy, and spur collective action.The challenge before us is not whether GenAI will shape higher education, but whether we will shape its use in ways that strengthen learning, integrity, and the common good.The AI Challenge: How College Faculty Assess the Present and Future of Higher Education in the Age of AI The AI Challenge: How College Faculty Assess the Present and Future of Higher Education in the Age of AI Key Data Takeaways Note: The term "GenAI" is used throughout the report and refers to "generative artificial intelligence tools" such as ChatGPT, Gemini, Claude and Copilot.These findings are based on a non-scientific sample of faculty known to the American Association of Colleges & Universities.The Methodology section has details of the composition of the sample.

**Решение:** -3 нет меры зависимости от ИИ (опрос преподавателей)

---

### 238 · R1479

**Exploring the Factors of AI Chatbot Dependence: An I-PACE Model and AIDUA Framework Perspective**

2026 · Research Square · preprint, posted-content · https://doi.org/10.21203/rs.3.rs-10305715/v1

Abstract Generative AI chatbots are increasingly used as everyday cognitive and emotional support tools, raising concerns that repeated interaction may develop into maladaptive dependence rather than merely technology acceptance. Despite their convenience, they may foster excessive dependence, a concern whose underlying antecedents have received little scholarly attention. Using the I-PACE model as the overarching framework, this study reconceptualises AIDUA appraisal processes as proximal cognitive–affective mechanisms through which person-related factors may translate into AI chatbot dependence and rejection. Participants with prior experience using AI chatbots were invited to take part in the survey. A total of 540 valid responses were collected via the NAODAO survey platform. Structural equation modelling results showed that hedonic motivation and perceived humanness were associated with more favourable performance-related appraisals and lower perceived effort, whereas social influence showed a more limited association with effort-related appraisal. Performance expectancy and effort expectancy are significantly associated with both cognitive and affective appraisals. Finally, only affective appraisal influences AI chatbot dependence and rejection behaviours. AI familiarity and age, entered as control variables, show significant associations with both AI usage behaviour and attitudinal outcomes. These findings suggest that dependence on AI chatbots is not simply an extension of technology acceptance, but may emerge when favourable affective appraisals transform repeated instrumental use into emotionally reinforced reliance.</p

**Решение:** -4 нет нашего коррелята (только предикторы AIDUA/TAM)

---

### 239 · R3479

**Teachers' Perceptions of the Use of Artificial Intelligence (AI) in Daily Learning at Elementary Schools**

2025 · Global Journal of Basic Education · article, journalarticle · und · https://doi.org/10.61227/gjbe.v1i2.252

This research examines teachers' perceptions of the use of artificial intelligence (AI) in daily learning at elementary schools. The development of AI technology has brought significant transformation to the world of education, offering great potential to improve the quality of learning through personalized materials, automation of administrative tasks, and provision of interactive learning aids. However, the implementation of AI in elementary school learning still faces various challenges related to teachers' perceptions, competencies, and readiness. The research objectives are to analyze teachers' understanding of AI in the learning context, explore teachers' experiences in using AI-based applications, identify the benefits and challenges faced, evaluate the effectiveness of AI in supporting differentiated learning, and identify support needs for optimizing AI utilization. This research uses a qualitative approach with descriptive methods. Data were collected through in-depth interviews with six classroom teachers (grades 1-6), one school principal, and one school operator at SDN Rinjani, Cirebon City, in November-December 2024. The research instrument was a semi-structured interview guide. Data analysis used the Miles and Huberman model through stages of data reduction, data presentation, and conclusion drawing. Data validity was ensured through source triangulation and member checking. The research findings show that teachers have diverse understandings of AI, ranging from basic concepts as assistive tools to more comprehensive understanding of AI's role in learning transformation. The AI applications used include PowerPoint, Wordwall, Assemblr Edu, ChatGPT, Gemini, Perplexity, and Canva. Teachers reported various benefits of AI such as ease of access to information, efficiency in creating materials, personalized learning, and increased student creativity. The challenges faced include limited teachers' digital competence, suboptimal technological infrastructure, and the risk of excessive dependence on AI. AI was found to be effective in supporting differentiated learning through adaptation of content, process, and learning products according to individual student needs. The required support includes systematic training, infrastructure improvement, and supportive policy development. The research concludes that although teachers show positive attitudes toward AI, optimal implementation requires comprehensive investment in developing teacher competence and technological infrastructure. Further research is recommended to examine the long-term impact of AI use on student learning outcomes and develop effective teacher training models.

**Решение:** -2 качественное исследование (интервью)

---

### 240 · R3556

**Tekoälyn vaikutukset sosiaalisiin suhteisiin ja yhteiskuntaan : kirjallisuuskatsaus**

2025 · Oulu

Artificial intelligence has advanced enough that its products and communications can pass as those of a human. In fact, Jones and Bergen (2024) recently demonstrated the ability of ChatGPT, one of the most popular AI systems, to pass the Turing test which demonstrates that people can not tell apart its writing from real human writing. In a world where artificial conversation partners are readily available, could some people prefer talking to their computer, rather than to each other? This literature review examined existing research on the topic of the addictiveness of artificial intelligence, mainly focusing on Conversational AI (CAI), as well as possible consequences on society on a large scale, and determined what is known and where more research is needed. There are many cases in which intelligent CAI systems can benefit people and society. CAIs can help with studying, coping with grief and social isolation. When correctly and responsibly applied, they can act as a companion for people, who have no one else. However, a personal, friend-like relationship with CAI can often lead to psychological dependance, or in other words, addiction. While there are some studies examining the causes for AI addiction, there is as of yet very little research in treatment and consequences of it

**Решение:** -1 обзор (литературный)

---

### 241 · R3430

**The LLM-Based AI Agent for College Students to Reduce Smartphone Addiction in the Morning**

2025 · Companion of the 2025 ACM International Joint Conference on Pervasive and Ubiquitous Computing · proceedings-article · https://doi.org/10.1145/3714394.3750588

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 ИИ как инструмент снижения зависимости от смартфона

---

### 242 · R2106

**Artificial Intelligence in English Language Learning: Student Perspectives on AI Literacy, Academic Integrity, and Dependency at Universidad Tecnológica de Tijuana**

2026 · Ciencia Latina Revista Científica Multidisciplinar · article, journal-article · https://doi.org/10.37811/cl_rcm.v10i5.26101

The increasing use of generative artificial intelligence (GenAI) in higher education has created new opportunities for English language learning while also raising concerns regarding academic integrity, student dependency, AI literacy, and institutional regulation. This study aims to analyze university students’ perceptions of these four dimensions in the context of English language learning at a technological university in Mexico. A quantitative, non-experimental, cross-sectional, and correlational research design was employed. Data were collected from 214 university students through a 16-item questionnaire organized into four constructs: Academic Integrity, AI Literacy, AI Dependency, and Institutional Regulation. Descriptive statistics, Cronbach’s alpha, Pearson’s correlation coefficient, and Kruskal–Wallis tests were used to analyze the data. The results showed relatively high levels of AI Literacy (M = 3.77, SD = 0.88) and Academic Integrity (M = 3.61, SD = 0.86), whereas AI Dependency obtained a lower mean (M = 2.61, SD = 0.78). AI Literacy was positively correlated with Academic Integrity (r = .684, p &lt; .001), while Academic Integrity and AI Literacy were also positively associated with Institutional Regulation. AI Dependency showed weak negative correlations with Academic Integrity and AI Literacy. Significant differences according to frequency of AI use were found for AI Dependency and Institutional Regulation, but not for Academic Integrity or AI Literacy. The findings suggest that responsible AI integration in English language education requires more than regulating access to technology; it also requires developing students’ AI literacy, maintaining academic integrity, and promoting learner autonomy through clear institutional guidance.

**Решение:** -4 нет нашего коррелята (только AI literacy, честность и регулирование)

---

### 243 · R3751

**Examining the drivers of ai technologies for academic productivity among higher education students**

2025 · review · en · https://core.ac.uk/download/736938544.pdf

The study examines the drivers of artificial intelligence (AI) technologies in shaping academic productivity among higher education students. The rapid advancement of AI has transformed educational practices, making AI technologies increasingly integrated into students’ academic routines. As the role of AI expands in academic settings, understanding how students perceive and engage with these technologies is essential. While AI technologies are widely recognised for their potential to enhance learning, concerns remain about the extent to which students may become dependent on them. Grounded in the Technology Acceptance Model (TAM) and self-efficacy theory, this study explores how students' perceptions of AI technologies, particularly perceived usefulness, perceived ease of use and perceived self-efficacy, shape their academic dependence on AI technologies, and how such dependence subsequently affects their academic productivity. To empirically test these relationships, a quantitative research design was adopted. Primary data were collected through a questionnaire survey distributed to students enrolled in higher education institutions. Additionally, partial least squares structural equation modeling (PLS-SEM) was employed to analyse the relationships among the constructs. This approach enabled both the assessment of construct reliability and validity within the measurement model and the testing of hypothesised relationships in the structural model. The findings of the study are expected to contribute to the literature on the role of AI technologies in academic contexts by clarifying the interplay between perceptions, reliance, and productivity. Theoretically, the research extends TAM by incorporating self-efficacy and by emphasising academic dependence as a critical construct linking perceptions and productivity. Practically, the study provides insights for higher education institutions, educators, and policymakers seeking to integrate AI technologies effectively and sustainably. Looking ahead, the study provides a foundation for future research and policy initiatives on promoting responsible AI use while supporting students’ independent learning and long-term academic development. Keywords: Artificial Intelligence (AI) technologies, perceived usefulness, perceived ease of use, perceived self-efficacy, academic dependence, academic productivity, higher education institution

**Решение:** ? эмпирическое исследование; academic dependence, self-efficacy (возможно академическая)

---

### 244 · R3207

**The Last Dependency Crusade: Solving Python Dependency Conflicts with LLMs**

2025 · 2025 40th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW) · proceedings-article · https://doi.org/10.1109/asew67777.2025.00022

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 программные зависимости в Python

---

### 245 · R4625

**LITERATURE REVIEW ON ARTIFICIAL INTELLIGENCE (AI) INTEGRATION INTO HIGHER EDUCATION TEACHING AND LEARNING: A CHALLENGE OR OPPORTUNITY?**

2024 · LINGUISTICA · journalarticle, review, article · en · https://doi.org/10.24114/jalu.v13i3.62117

Technological advancements have significantly transformed various facets of human existence, including the realm of education. An important transformation that has taken place is the rise of artificial intelligence, which has become an essential component of the educational process, particularly among students in higher education. The primary objective of this essay is to examine the comprehension of artificial intelligence and the potential hazards it poses within the realm of education. The methodology employed involves doing a comprehensive literature review by examining pertinent scholarly articles, books and researches. The data that was gathered was subjected to analysis in order to examine the effects of dependence on artificial intelligence in the field of education. The study was conducted at Ambon State Polytechnic, where the findings indicated the presence of various risks linked to the utilisation of artificial intelligence in the field of education. These risks encompassed the possibility of errors and inaccuracies within artificial intelligence systems, ethical concerns, and psychological ramifications. This article additionally presents a number of strategies for the prudent utilisation of artificial intelligence in order to mitigate these potential hazards. The primary objective of this article is to enhance comprehension regarding the utilisation of artificial intelligence in the field of education, while also providing recommendations on effectively managing potential hazards that may emerge.

**Решение:** -1 обзор (литературный)

---

### 246 · R2763

**Ethical tensions in AI-mediated clinical communication: a mixed-methods study of nursing students’ perspectives**

2026 · BMC Medical Ethics · article · en · https://doi.org/10.1186/s12910-026-01602-4

Abstract Background The increasing use of artificial intelligence (AI), particularly large language models (LLMs), is reshaping clinical communication by influencing how patients access, interpret, and act upon medical information. Recent conceptual work has suggested that AI-mediated communication raises ethical questions concerning interpretive authority, professional responsibility, and uncertainty communication. However, empirical evidence regarding how future healthcare professionals understand and respond to these emerging ethical challenges remains limited. This study explored perceptions of AI-mediated clinical communication, with particular attention to interpretive authority, responsibility, and uncertainty. Methods An exploratory convergent mixed-methods design was employed. Thirty-two undergraduate nursing students (16 international and 16 local) participated in a theory-informed case-based session involving AI-mediated communication scenarios across a surgical care pathway. Quantitative data were collected using pre–post questionnaires and analysed descriptively. Qualitative written responses were analysed using reflexive thematic analysis and subsequently subjected to structured thematic quantification to facilitate comparison across participant groups. Given the exploratory nature of the study, analyses focused on identifying patterns of perception and interpretation rather than causal effects. Results Participants showed higher descriptive mean scores across all three ethical domains following the session, particularly interpretive authority and uncertainty communication. Qualitative analysis identified three higher-order dimensions: perceptions of AI in clinical contexts, ethical and communication tensions in AI-mediated care, and professional roles in AI-mediated communication. Participants recognised challenges associated with patient over-reliance on AI, difficulties in correcting AI-influenced understanding, and tensions arising from the communication of uncertainty. They also described an expanded professional role involving interpretive mediation, trust-building, and contextualisation of AI-generated information. Patterns were broadly consistent across participant groups, although variation was observed in the salience of specific themes. Conclusions The findings suggest that AI-mediated clinical communication introduces identifiable ethical tensions concerning authority, responsibility, and uncertainty. Participants recognised that AI-generated explanations may reshape how clinical meaning is interpreted and negotiated while leaving professional accountability largely intact. By providing empirical evidence informed by a conceptual framework of AI-mediated communication, this study contributes to emerging discussions regarding the ethical implications of AI in healthcare communication and highlights the importance of addressing authority, accountability, and uncertainty within the responsible governance of AI-enabled healthcare communication.

**Решение:** -2 качественное / этическое исследование (32 студента)

---

### 247 · R3671

**Pre-Service EFL Teachers’ Perspectives on AI Integration in Indonesian Urban Schools**

2025 · IJLHE International Journal of Language Humanities and Education · journalarticle, article · en · https://doi.org/10.52217/r4tkmv84

This study explores the perspectives of pre-service EFL teachers on integrating Artificial Intelligence (AI) tools in urban classrooms in Indonesia. As AI increasingly influences language teaching and learning, it is important to understand how future teachers perceive its role, benefits, and challenges in their professional practice. Employing a qualitative descriptive design, the study collected data through an online questionnaire completed by seventy pre-service EFL teachers and follow-up semi-structured interviews with twenty volunteers. The findings revealed that participants generally held positive views of AI integration, highlighting its potential to enhance student motivation, provide immediate feedback, and support differentiated instruction for diverse learners in urban settings. At the same time, their confidence in applying AI remained moderate, reflecting limited training and practical experience. Participants also expressed concerns about infrastructural barriers, institutional support, and ethical issues such as plagiarism and over-reliance on AI outputs. These results suggest that while pre-service EFL teachers see AI as a valuable pedagogical tool, they acknowledge the need for critical awareness and proper preparation. The study implies that teacher education programs should embed AI literacy, pedagogical training, and ethical guidance into curricula to better equip future teachers for AI-enhanced classrooms.

**Решение:** -3 нет меры зависимости от ИИ (опрос мнений)

---

### 248 · R3011

**A Modest Perspective on the Concept of ‘Damage’ in the Age of Artificial Intelligence : With a Focus on Non-Pecuniary Harm, Including Emotional Dependency**

2026 · 민사법의 이론과 실무 · article · https://doi.org/10.21132/minsa.2026.29.2.05

이 논문은 생성형 인공지능, 특히 챗봇과의 상호작용 과정에서 발생하는 ‘정서적 의존(emotional dependency)’을 중심으로, 이러한 현상이 민사법상 ‘손해’로 평가될 수 있는지에 대한 문제를 다루고자 한다. 최근 미국 Character.AI 사건과 같이 인공지능과의 대화가 이용자의 자살 등 중대한 결과로 이어질 수 있는 사례가 등장하면서, 단순히 대화를 넘어서 “정서적 의존”이라는 부정적인 결과를 손해의 개념으로 포섭해 보려는 시도를 하였다. 이는 인공지능의 활용이 우리 삶 깊숙이 침투함에 따라 전통적으로 재산적 손해를 중심으로 구성되어 온 손해 개념을 새로운 시각으로 바라보아야 하는 시대적 상황을 강조하고자 하였다. 실제로 생성형 인공지능의 활용은 국내·외에서 급격히 확산되고 있으며, 이용자들은 인공지능을 단순한 도구가 아니라 상담자, 친구, 나아가 감정적 교류의 대상으로 인식하는 실태를 보이고 있다. 더욱이 청소년과 같이 정서적으로 취약한 이용자 집단에서는 인공지능 챗봇의 과도한 사용은 몰입을 넘어 의인화를 통한 사회적 존재감과 실재감을 강화하여 정서적 애착과 의존으로 이어지고, 현실 세계와의 관계 단절이나 정신적 문제를 심화시킬 위험이 존재한다. 이에 대해 논문은 정서적 의존이 기존 민법상 손해 개념에 포함될 수 있는지 판단하면서 손해 개념이 단순한 경제적 불이익에 국한되지 않고 규범적으로 확장되어 온 판례와 학설의 흐름에 제시하였고, 일정한 경우 비재산적 손해로서 인정될 가능성이 있음을 보이고자 하였다. 이를 위하여 생성형 인공지능 챗봇과의 정서적 의존 관계에 대응 해 볼 수 있는 우리 판례를 찾기 위하여 서울북부지방판결 중에서 상담과정에서 피고와 “감정적 전이 현상”을 겪은 원고의 사례를 통하여 내담자가 상담자에게 전이 감정을 가질 수 있음을 예견할 수 있었던 사례를 통하여 우리 법원이 보호의무를 인정한 사례를 제시하였다. 인공지능 챗봇의 개발의 단계에서도 이러한 가상의 상황이라는 점을 제시하고 사용자의 대화 내용 중 위험 요소가 식별되는 경우에는 보호의무에 따라서 극단적 상황을 예견할 수 있었음에 공통점이 있다고 판단되었기 때문이다. 또한 논문은 정서적 의존이 인격권의 침해 가능성에 대하여 살펴보면서 우리 민법 제751조에 대한 개정안을 소개하였고, 마지막으로 「인공지능 발전과 신뢰기반 조성 등에 관한 기본법」상의 의무 위반 여부에 대한 판단을 간략히 살펴보았다.

**Решение:** -2 правовой / концептуальный анализ

---

### 249 · R0576

**Building a brand for Generation Z**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · cs

This diploma thesis examines the issue of branding in the context of Generation Z, young people born approximately between 1997 and 2012, who are the first generation to have grown up in a fully digital environment. The aim of the thesis is to analyze the key branding characteristics relevant to this target group and to verify whether the Czech educational platform Based meets these characteristics, having been selected as a case study due to its innovative and community-oriented approach. The theoretical part defines concepts related to branding and Generation Z and places them in the broader context of the current marketing environment. The empirical part is basedon qualitative research conducted through focus groups, aimed at capturing the real expectations, attitudes and behavioral patterns of Generation Z in the Czech context. The results show that this generation has clearly articulated and internally consistent expectations - they demand from brands above all authenticity, transparency and trustworthiness, while responding negatively to performative inclusivity, trend-chasing without substance, and excessive use of artificial intelligence. The case study revealed that the Based platform largely meets these requirements, and the research also produced specific recommendations for its further...

**Решение:** -5 маркетинг / брендинг поколения Z

---

### 250 · R3885

**Organic coating failure and monitoring in atmospheric corrosion: from mechanisms to applications**

2025 · Progress in Materials Science · article · en · https://doi.org/10.1016/j.pmatsci.2025.101592

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 коррозия органических покрытий (материаловедение)

---

### 251 · R4815

**Reducing Alcohol and Smoking Dependency through Artificial Intelligence: A Critical Analysis**

2024 · International Journal of Intelligent Systems and Applications in Engineering · article · en

This study report critically analyses the efficacy of using Artificial Intelligence (AI) to reduce alcohol and smoking addictions. The main goal is to evaluate the effectiveness of AI technology in delivering individualized and focused assistance for addiction cessation. The study used a combined-technique approach, using both qualitative and quantitative data gathering techniques. A structured survey was conducted with 100 participants to collect demographic data, evaluate the extent of alcohol and smoking addiction, and explore the participants' perspectives on AI-driven therapies. Qualitative data was collected via detailed interviews and focus group discussions to provide a nuanced insight into individual experiences and perspectives. The research employs sophisticated AI algorithms to examine the gathered data, detecting patterns and relationships among demographic characteristics, dependence levels, and reactions to AI interventions. The results emphasize the need of customized treatments, using artificial intelligence to adjust treatment strategies according to individual requirements and preferences. It is determined that 95.0% of individuals agree or strongly agree on the significance of AI integration. The Cronbach's Alpha value of 0.871 indicates that the survey questions effectively assess the desired constructs of addiction treatment effectiveness in a reliable manner.

**Решение:** -5 ИИ как инструмент снижения зависимости от алкоголя и курения

---

### 252 · R3315

**Enhancing High School Programming Education Through LLM-Based Hint Generation**

2025 · International Workshop on Artificial Intelligence and Education (WAIE) · conference-paper · https://doi.org/10.1109/waie67422.2025.11381301

The integration of Large Language Models (LLMs) into education offers new opportunities for enhancing programming instruction, especially at the high school level. This paper introduces PythonTutor, an intelligent tutoring system that supports novice learners through scaffolded, AI-generated feedback. Powered by ChatGPT 4.0 Mini, PythonTutor provides step-by-step hints tailored to student submissions, promoting independent problem-solving and limiting overreliance on AI. The platform unifies instructional content, personalized tutoring, and teacher oversight in a web-based environment. A pilot study with 18 students and three teachers compared PythonTutor-supported instruction to traditional methods. Results showed significantly greater learning gains with PythonTutor, supported by high accuracy and precision in AI feedback. Student and teacher feedback confirmed the system’s usability, educational value, and classroom potential. PythonTutor emerges as a scalable, cost-effective solution for personalized programming education aligned with best practices

**Решение:** -2 разработка обучающей системы (18 школьников)

---

### 253 · R3306

**University English Reading and AI: A Qualitative Study Targeting Female Students in Coastal University in Guangdong, China**

2025 · Lecture Notes in Education Psychology and Public Media · journalarticle, review, article · en · https://doi.org/10.54254/2753-7048/2025.bo23944

Nowadays, with the development of AI, an increasing number of college students in China have began to utilize it as a tool for English study, and AI has demonstrated its double-edged effect in many aspects of writing assistance. The propose of this study is to explore the impact of AI assist reading on five Female students of English major in an coastal university in Guangdong, China. This study also inquires about the room for improvement of college English teaching under the phenomenon of the popularity of AI tools. A qualitative research approach, leveraging literature review and qualitative interview as research design and approach were used and effectively facilitated the realization of the study purpose. This study finds that college students have a strong dependency on AI-assist reading. Both the students and researchers express a strong interest in integrating AI into the college English teaching process, and various suggestions are provided. On one hand, these young female college students point our the potential room for improving college English major’s education under the back ground of popularization of AI. On the other hand, they also set an alarm on the important of guiding students to distinguish the boundary between AI assistance and AI instead of themselves.

**Решение:** -2 качественное исследование (5 студенток, интервью)

---

### 254 · R3962

**Examining the Disruptive Influence of Artificial Intelligence on Digital Marketing and Advertising in the Philippines**

2025 · IEEE Control and System Graduate Research Colloquium (ICSGRC) · conference-paper · en · https://doi.org/10.1109/icsgrc65918.2025.11159801

Artificial intelligence (AI) is becoming a disruptive force in digital marketing and advertising in the Philippines, transforming how brands plan, execute, and engage with their audiences. This study explores the impact of AI technologies such as automated targeting, personalized content delivery, and campaign optimization on industry practices and professional skillsets. Using the Task Technology Fit (TTF) Model and sentiment analysis, the research identifies a growing dependence on AI tools alongside significant challenges. These include a shortage of AI-related training opportunities, limited institutional support, and ethical concerns related to privacy and algorithmic bias. Despite these obstacles, there is cautious optimism among marketing professionals regarding AI’s potential to enhance creativity, efficiency, and strategic decision-making. The findings emphasize the importance of developing human-AI collaboration frameworks, strengthening ethical standards, and promoting AI literacy across sectors. Collaboration among educational institutions, industry leaders, and policymakers is essential to building a resilient and future-ready advertising workforce in the Philippines.

**Решение:** -3 нет меры зависимости от ИИ (опрос маркетологов)

---

### 255 · R0751

**Holistic Intent Detection With LLM for Emotion AI: Multi-intent Detection and Dependency Recognition**

2026 · IEEE Transactions on Computational Social Systems · journal-article · https://doi.org/10.1109/tcss.2025.3632838

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 техническая NLP статья (распознавание синтаксических зависимостей)

---

### 256 · R1957

**The Phenomenon of Artificial Intelligence in Assisting in Writing Maritime Student Papers**

2026 · Journal of Maritime Research · article, journalarticle · en · https://doi.org/10.22429/euc2026.jmr23.1.16

Artificial Intelligence (AI) is increasingly popular as a tool in the world of higher education, including in writing student papers. This article examines the phenomenon of using AI to support students' academic assignments, with a focus on the assistance provided in searching for literary sources, compiling ideas, analyzing data, and correcting grammar. Based on qualitative research through in-depth interviews with 107 students from various universities in Indonesia, it was found that AI not only makes the academic process easier but also raises ethical and pedagogical challenges. The research results show that the use of AI has a positive impact on increasing the efficiency and quality of writing papers. AI technologies such as ChatGPT and Grammarly help students organize ideas more systematically, find relevant reference sources, and ensure writing is free from grammatical errors. On the other hand, there are concerns that dependence on AI could reduce students' critical and analytical thinking abilities, as well as pose a risk to the authenticity of scientific work. This article provides recommendations for educational institutions to provide guidance and training regarding the ethical use of AI in academic writing. With clear guidance, AI can be utilized optimally to support student skill development without reducing the originality and creativity of their written work. It is hoped that this article will provide insight to students, lecturers, and educational policymakers regarding the role of AI in higher education in the digital era.

**Решение:** -2 качественное исследование (107 интервью)

---

### 257 · R4116

**Minds Growing Under Algorithmic Influence: The Cognitive Price of Growing Up with AI and What It Will Cost Our Future**

2025 · Zenodo (CERN European Organization for Nuclear Research) · preprint, preprint/ · en · https://doi.org/10.5281/zenodo.17769139

Artificial intelligence is now part of daily life. Search engines, recommendation systems and language models shape how we find information, learn, create and even seek comfort. Public debate often focuses on jobs, automation and productivity. A more important question sits underneath these headlines. What happens to our minds when we rely on AI to carry the thinking that once strengthened our memory, attention and emotional resilience? This paper brings together research from cognitive science, developmental neuroscience, psychology and human computer interaction to examine how growing dependence on AI may reshape human cognition across the lifespan. Existing studies already show clear patterns that point toward a shift in how people use memory, sustain attention and process what they learn. Researchers in different fields describe the same overall movement toward greater reliance on external systems and less engagement in the internal cognitive steps that create lasting understanding. When people expect information to be stored online they remember the location more than the content, a finding known as the Google effect. Heavy digital use is linked to reduced sustained attention and shallower cognitive processing (Firth et al., 2019). Large cohort studies, including research from the Adolescent Brain Cognitive Development project, show that higher screen exposure in children is associated with increased ADHD-related behaviours and reduced cortical thickness in regions that support executive function (Sauce et al., 2022; Nivins et al., 2024). Early neurocognitive research suggests that using AI for writing can reduce neural engagement in frontal and temporal brain regions involved in planning, memory and creative integration (Kosmyna et al., 2025). The paper also draws on practitioner perspectives from engineers, artists and psychologists, supported by the work of Sherry Turkle on intimacy and technology, Fei Fei Li on human centered AI, Ethan Mollick on co-intelligence and Timnit Gebru on structural harms in data systems. Together, these sources point to three emerging layers of human cost. The first is cognitive downgrading, which is the slow weakening of deep skills when effortful thinking is consistently outsourced. The second is relational hollowing, where AI sits between people and changes how we build trust, empathy and self worth. The third is structural dependence, where societies risk losing the ability to function without AI support.Within these human costs, children are not only early users of AI. They are growing up while their minds and habits of thought are still forming. Their attention, memory, frustration tolerance and inner voice develop during the same years that AI becomes part of daily life. This makes childhood the most sensitive stage for understanding how AI may shape the mind. The paper concludes with a Human Cognitive Resilience Framework that offers practical steps for educators, states, organisations and global bodies such as UNESCO and UNICEF. The framework includes guidance for strengthening attention, memory, independent reasoning and emotional resilience, abilities that need deliberate protection as AI becomes embedded in everyday life. It argues that cognitive resilience, especially for children, must become a central goal of AI governance. The future strength of human societies will depend not only on what AI can do but on what people continue to be able to do for themselves. Top of Form Keywords: artificial intelligence, cognitive development, cognitive offloading, children, neurodevelopment, attention, memory, AI governance, developmental psychology, cognitive resilience

**Решение:** -1 обзор / теоретическая статья

---

### 258 · R0484

**Detecting Human Overreliance on AI Using Behavioral Patterns**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/jtcsb

Background and Purpose As artificial intelligence systems become increasingly integrated into decision-making workflows, there is a growing risk of users exhibiting "AI overreliance"—a state where humans blindly accept algorithmic suggestions, effectively outsourcing their cognitive judgment. While overreliance is widely acknowledged, pinpointing its real-time behavioral and cognitive symptoms remains a challenge. The primary purpose of this research project is to operationalize and detect specific, measurable symptoms of AI overreliance. Rather than just looking at final accuracy scores, this study aims to track the continuous cognitive processes (such as hesitation, mid-action revisions, and shifting decision criteria) that occur when humans interact with AI under varying conditions of cognitive load and algorithmic reliability. By isolating these markers, this research will contribute to a better understanding of how human-AI interactions degrade and how system designers might detect user disengagement before critical errors occur. Methodological Overview Participants in this study are tasked with evaluating a balanced set of news headlines and classifying them as either "Real" or "Fake." The experiment employs a 2 × 3 mixed factorial design. To test how extreme cognitive states exacerbate overreliance, participants are assigned to either a low-load condition (a monotonous, repetitive typing task) or a high-load condition (a dual-task environment requiring simultaneous mouse-clicks and continuous performance on a survival game). Additionally, participants are exposed to one of three levels of AI assistance: No AI (Control), Unreliable AI (60% objective accuracy), or Reliable AI (90% objective accuracy). Crucially, the AI suggestions are delivered with a deliberate 1200ms delay to capture baseline human action (e.g., initial keystrokes or mouse trajectories) prior to algorithmic intervention. Expected Outcomes and Hypotheses Based on this design, the study will test for several distinct symptoms of overreliance. The expected outcomes include: Load-Induced Overreliance: Participants in the high cognitive load (dual-task) condition will exhibit significantly higher commission error rates (agreeing with an incorrect AI) compared to those in the low load condition. The Reliability Paradox: Exposure to a highly reliable AI (90%) will induce stronger cognitive complacency, resulting in a higher rate of commission errors on the rare occasions the AI fails, compared to the 60% reliable AI. Process-Level Symptoms: Behavioral tracking will reveal mid-action reversals (e.g., deleting initial keystrokes or redirecting mouse trajectories) that heavily favor the AI's delayed suggestion, indicating a suppression of independent judgment. Fatigue Drift: Across all conditions, overreliance will progressively worsen as a function of time-on-task, observable as a steady increase in commission errors between the Early, Mid, and Late trial blocks. Metacognitive Disconnect: There will be a significant discrepancy between self-reported AI reliance (via post-task survey) and actual behavioral reliance (via commission error rates), highlighting a lack of user self-awareness regarding their algorithmic dependence.

**Решение:** -2 пререгистрация эксперимента (нет данных)

---

### 259 · R3905

**Analisis Potensi dan Tantangan dalam Penggunaan AI di Bidang Pendidikan**

2025 · Semantik Jurnal Riset Ilmu Pendidikan Bahasa dan Budaya · article, journalarticle, review · en · https://doi.org/10.61132/semantik.v3i2.1705

The development of Artificial Intelligence (AI) technology in the education sector has undergone major changes. These changes bring great opportunities to change the learning process to be more personal, effective, and inclusive. The purpose of this journal is to analyze the potential and challenges that need to be faced in the application of AI in education so that it can run optimally. The method used in this study is the literature review method of various recent studies that discuss the use of AI in education, The results of the study show that AI has great potential to improve the personalization of learning and educational efficiency. However, there are number of significant challenges, such as limited infrastructure, privacy and data security issues, resistance from educators and students, and the digital divide that still occurs in several regions. Therefore, a strategy is needed that includes a academic laziness that reduces learning motivation, constraints on AI contextual knowledge, Inability to process complex information, loss of literacy skills, amd the risk of addiction to AI technology. With a planned and sustainable strategy, AI has great potential to improve the quality of national education and also reduce the dangers that may arise from the modern technological era.

**Решение:** -1 обзор (литературный)

---

### 260 · R0310

**AI Dependency in Sri Lankan Higher Education: Effects of Chatbot Overuse on Student Learning and Problem-Solving**

2026 · IEEE International Conference on Industrial and Information Systems (ICIIS) · article, conference object, journalarticle · und · https://doi.org/10.1109/iciis69028.2026.11450932

Artificial Intelligence (AI) chatbots have rapidly transformed computer science education in Sri Lanka by offering instant coding assistance and conceptual explanations. While these tools enhance learning efficiency, their widespread adoption raises concerns about over-reliance and its impact on students' critical thinking and independent problem-solving abilities. This study investigates AI dependency among 80 computer science students from three Sri Lankan institutions during an open-book programming assignment conducted in May 2025. Students were allowed unrestricted access to AI chatbots and online resources, and their behavior was analyzed using screen monitoring, post-task interviews, and performance assessments. Results revealed that 88% of participants used AI chatbots even for basic tasks, indicating a significant trend of diminished self-reliance. Chatbot-reliant students demonstrated higher accuracy in syntax-based tasks but performed worse in algorithmic design and conceptual articulation. This study introduces the AI Dependency Index (AIDx), a novel metric to quantify the level of reliance across different task types. Findings show that 62% of students fall into the high dependency category, particularly among first- and second-year undergraduates. These insights highlight the need for pedagogical strategies that promote responsible AI usage rather than replace critical thinking and problem-solving skills in higher education.

**Решение:** -4 нет нашего коррелята (только навыки программирования)

---

### 261 · R3296

**Agent AI Becomes Next Addictive Disorder**

2025 · International Conference on Computing and Artificial Intelligence (ICCAI) · journalarticle, conference, review · en · https://doi.org/10.1109/iccai66501.2025.00044

AI represents a crucial information development that is vital to human innovation and progress. Agent AI further integrates AI into human life. As networks transform into AI, humans may develop an addiction-like dependence on AI. This study primarily investigates the impact of human AI addiction on decision quality and job satisfaction. The sample consists of ${1 4 0}$ firm surveys, with hypotheses verified using SPSS 23.0. Results indicate that Agent AI addiction affects decision quality and job satisfaction. In particular, decision quality in AAI serves as a key mediating factor. This enhances organizational theory regarding AI usage behavior while highlighting the importance of decision quality in AI design.

**Решение:** -4 нет нашего коррелята (только качество решений и удовлетворенность работой)

---

### 262 · R0173

**Digital Dependency and Academic Identity Among Postgraduate Students in the Era of Generative AI**

2026 · Education Sciences · journal-article · https://doi.org/10.3390/educsci16101615

Generative artificial intelligence has become embedded in everyday university life, often faster than institutional guidance has developed. This qualitative hermeneutic phenomenological study examined how postgraduate students experienced the boundary between generative-AI assistance and digital dependency, and how these experiences related to academic identity. In-depth, semi-structured interviews were conducted with eleven postgraduate students (five males and six females) at a public university in Saudi Arabia, selected through maximum-variation purposive sampling. Interviews were audio-recorded, transcribed verbatim, and returned to participants for verification. Analysis followed Van Manen’s holistic, selective, and detailed approaches to phenomenological reflection. Two themes captured the experience: negotiating the boundary of digital dependency, and academic identity between agency and dependence. Rather than locating dependency in frequency of use, participants located it in the recurring transfer of substantive ideation, judgment, and authorship to the tool. Verification and the ability to explain and defend the final work helped preserve epistemic agency, whereas time pressure sometimes shifted practice toward substitution. Within this sample, strategic use as a coach, critic, or organizer supported confidence and skill development; extensive delegation was associated in participants’ accounts with diminished ownership, guilt, and concealment-oriented assessment practices. The findings offer a provisional, sample-grounded account of digital dependency and suggest that perceived ambiguity in institutional expectations may make concealment more salient, without establishing a causal relationship.

**Решение:** -2 качественное феноменологическое исследование (11 студентов)

---

### 263 · R3720

**Ethics-Integrated AI Pedagogy and Metacognitive Growth: A Longitudinal Quasi-Experimental Study in Indian Higher Education**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5526736

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (педагогика этики и метакогнитивный рост)

---

### 264 · R3976

**Leveraging generative AI powered rubric-indexed feedback as a formative assessment strategy for enhancing medical English education**

2025 · Discover Computing · journalarticle, book-chapter · en · https://doi.org/10.1007/s10791-025-09830-9

The integration of generative artificial intelligence (GenAI) into language education offers transformative potential, particularly in specialized fields such as medical English. This study examines the impact of a hybrid feedback model—combining GenAI-powered feedback from Dou Bao, a GenAI chatbot, with peer feedback—on medical students’ English writing proficiency. Conducted at a medical university in Southeast China, the study employed a mixed-methods approach involving 116 medical students divided into two experimental groups and one control group, along with five language teachers. Pre- and post-test writing assessments measured improvements in students’ writing, while reflexive thematic analysis and a three-level coding process provided qualitative insights into students’ perceptions and teachers’ experiences. Quantitative findings demonstrated that the hybrid feedback model significantly enhanced students’ writing proficiency in areas of content, structure, and language use. Qualitative findings revealed increased student engagement with medical humanities but also highlighted concerns about over-reliance on GenAI feedback and the emotional detachment associated with its suggestions. Based on these empirical findings, the study proposes the GenAI-powered, Rubric-Indexed Feedback Framework (GRFF)—a scalable model designed to enhance linguistic, professional, and critical thinking competencies among medical students. GRFF’s potential to leverage the affordances of GenAI tools for improving formative assessment practice worldwide underscores its significance for future research and educational innovation.

**Решение:** -3 нет меры зависимости от ИИ (педагогический эксперимент)

---

### 265 · R2974

**ПРОБЛЕМА “ЗАЛЕЖНОСТІ ВІД ШІ” СЕРЕД СТУДЕНТІВ І ВИКЛАДАЧІВ ТА ПЕДАГОГІЧНІ СТРАТЕГІЇ ЇЇ ПОДОЛАННЯ THE PROBLEM OF “AI DEPENDENCY” AMONG STUDENTS AND EDUCATORS AND PEDAGOGICAL STRATEGIES TO OVERCOME IT**

2026 · Наука і техніка сьогодні · journal-article · https://doi.org/10.52058/2786-6025-2026-3(57)-822-835

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации (зависимость от ИИ среди студентов и преподавателей)

---

### 266 · R4523

**Anti-dependency teaching strategy for innovation in the age of AI among technology-based students**

2024 · Environment and Social Psychology · journal-article · https://doi.org/10.59429/esp.v9i8.3026

The anti-dependency teaching strategy aims to prepare technology-based students for the evolving world of artificial intelligence (AI). Instead of teaching students to be passive users of technology, it pushes them to become active producers and problem solvers. By cultivating creativity, critical thinking abilities, and a growth mentality, this approach equips students to use AI as a tool for innovation. It explores the potential of AI while acknowledging its limitations and ethical implications through project-based learning, interdisciplinary methodologies, and real-world applications. In order to promote an innovative culture and group problem-solving, it also integrates collaborative learning environments. The approach places a strong emphasis on adaptation and ongoing learning, keeping students abreast of developments in artificial intelligence and related fields. The study's respondents were twenty-four (24) instructors of technology-based disciplines with creative elements. By putting this plan into practice, educators can give students the knowledge and perspective they need to effectively navigate the AI era, producing a new generation of creative thinkers who can transform society for the better.

**Решение:** -2 педагогическая концепция / опрос 24 инструкторов

---

### 267 · R2063

**Beyond benchmark accuracy: Toward trustworthy, open, and agentic clinical artificial intelligence**

2026 · Pediatric Investigation · article · en · https://doi.org/10.1002/ped4.70062

To the Editor: The recent study on large language models (LLMs) for pediatric diagnosis presents compelling evidence that advanced models can surpass human clinicians in structured diagnostic tasks, particularly in rare disease identification.1 While these findings mark a significant milestone in clinical artificial intelligence (AI), they also necessitate a deeper reflection on how such systems should evolve for safe, scalable, and ethically grounded deployment in healthcare. A central implication of the study lies not merely in performance gains, but in the demonstrated human–AI complementarity, where union accuracy significantly exceeds individual performance. This observation strongly advocates for a transition from standalone LLM usage toward agentic clinical systems, multi-component architectures where LLMs interact with retrieval modules, verification engines, and structured medical knowledge bases. Such agentic approaches can enable iterative reasoning, contextual grounding, and dynamic hypothesis refinement, thereby addressing current limitations such as response inconsistency and overconfidence observed in reasoning-optimized models. In this context, the role of open-source, fine-tuned LLMs becomes particularly important.2, 3 While proprietary models dominate current benchmarks, open-source alternatives-when domain-adapted using curated clinical datasets-offer transparency, reproducibility, and the ability to embed institution-specific knowledge. Fine-tuned models aligned with clinical ontologies (e.g., Systematized Nomenclature of Medicine – Clinical Terms and Human Phenotype Ontology) can further enhance interpretability and reduce hallucination risks, especially in multilingual and resource-constrained settings. Moreover, open ecosystems facilitate rigorous peer validation, which is essential for high-risk applications such as medical diagnosis. However, the ethical and safety dimensions remain critical. The study highlights variability in model outputs and the presence of potentially harmful diagnostic suggestions despite overall coherence. Such risks underscore the necessity of human-in-the-loop oversight, calibrated uncertainty estimation, and abstention mechanisms when confidence is low.4 Additionally, concerns related to data privacy, bias in training corpora, and regulatory compliance, particularly under emerging frameworks like the EU AI Act, must be systematically addressed.5 Overreliance on LLMs may also contribute to diagnostic deskilling, necessitating careful integration strategies that preserve clinician autonomy and critical reasoning. While current LLMs demonstrate remarkable diagnostic potential, their future lies not in isolated accuracy improvements but in open, verifiable, and agentic ecosystems that prioritize safety, transparency, and collaborative intelligence. Bridging this gap will be essential to transform LLMs from experimental tools into trustworthy clinical partners. The author declares no conflict of interest.

**Решение:** -1 письмо в редакцию / комментарий

---

### 268 · R1780

**AI Dependence, AI Literacy, and Critical Thinking Among Nursing Students: A Systematic Review**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/h254g

This systematic review asks whether higher levels of AI dependence or AI literacy are associated with critical thinking and related cognitive and clinical outcomes, including metacognition, clinical judgment or decision-making, and problem-solving, among undergraduate nursing students and interns. We searched PubMed, CINAHL, Embase, and Web of Science in September 2026, with CINAHL rerun without limits in October 2026, and will synthesize observational quantitative studies that report associations, following PRISMA 2020. The primary synthesis will be narrative. A random-effects meta-analysis of correlations using Fisher’s z transformation and Hartung-Knapp confidence intervals will be considered only for an exposure-outcome pair with at least three sufficiently comparable studies. Any pooled estimate will be considered exploratory. The review will provide a structured synthesis of how AI literacy and different forms of AI dependence relate to critical thinking and related cognitive or clinical outcomes. Study quality will be appraised using appropriate JBI critical appraisal checklists. This is a retrospective registration: literature searching and title/abstract screening were completed before registration. Any departures from the original plan will be transparently documented in the registration.

**Решение:** -1 систематический обзор (протокол/регистрация)

---

### 269 · R4682

**Perspectives of Entry-Into-Practice Respiratory Care Students About the Use of Artificial Intelligence**

2024 · Respiratory care · journalarticle, review · https://doi.org/10.4187/respcare.20244126606

Background: While studies have investigated perceptions of various disciplines on incorporating artificial intelligence (AI) into clinical practice, there has been no exploration within respiratory care. As the role of AI expands, understanding clinicians’ perceptions and knowledge will be crucial for effective implementation. This study aims to assess the familiarity and comfort of undergraduate respiratory care students with AI and explore their perspectives on using AI as an adjunct assessment tool in the clinical setting. Methods: A 13-item mixed methods survey was administered via Qualtrics to a convenience sample of undergraduate respiratory care students at Boise State University via Canvas. This study received exempt approval from the Boise State University Institutional Review Board (#IRB24-285). The survey included 5 quantitative Likert-scale questions on familiarity, comfort, and receptivity to AI, 3 demographic questions, and 4 open-ended qualitative questions. Primary outcomes were students’ familiarity and comfort with AI in respiratory care. Secondary outcomes were their perspectives on AI as an adjunct assessment tool. The research team performed an inductive thematic analysis on the open-ended responses following Braun and Clarke’s framework. Theory triangulation was used to ensure data validity. Results: Of the 44 students contacted, 16 completed the survey, a 36% response rate. Incomplete responses were excluded from analysis. The study found that only two respondents were uninterested in incorporating AI into their future practice. Three themes were extracted from the qualitative data: potential, error, and clinical knowledge. Conclusions: The survey supports a general qualitative distrust of AI among students, particularly regarding bias, limitations, and safety. Despite this, the survey also supports a quantitative lack of knowledge but openness to further education and future integration. These findings suggest that while concerns about AI persist, there is a willingness among emerging respiratory therapists to learn more and potentially incorporate AI into their practice. Additionally, the students’ limited understanding of bias and ethics in AI highlights a significant opportunity for respiratory care education programs to address these critical issues. By incorporating comprehensive AI ethics and bias training into their curricula, these programs can better prepare students to navigate and implement AI technologies responsibly in the clinical setting. Table 1 Perspectives of Respiratory Care Students on Use of AI Emergent Themes Theme Clusters Formulated Meanings Potential Efficiency Improves time management; Aids in formulating evidence-based care plans Human Replacement/ Job Security Loss of clinical autonomy; AI tools may replace portions of the RT’s role, reducing job security Unfamiliarity Benefits unclear; Unfamiliar with AI/ML; Not well covered in undergraduate academic programs Error Error Technology isn’t infallible; Accountability for errors / misdiagnosis; Risk of diagnostic inaccuracy Error Reduction Reduces opportunity for human error; Consistent application of evidence-based medicine Patient Safety Promotes diagnostic accuracy; Mistakes may be dangerous or worsen outcomes; Implementation of AI-generated recommendations may cause harm to minoritized groups (global majority, LGBTQIA+, disabled, women, veterans, etc.) Clinical Knowledge Clinical Expertise Overreliance on AI tools leading to loss of clinical skill; AI/ML tools don’t understand intricacies of respiratory care practice Limitations of AI Accuracy of information pulled from large language models is unknown; Needs strict oversight Bias AI perpetuates existing biases due to human-influenced data compilation; Ethical concerns about potential harm to underrecognized groups

**Решение:** -2 качественный опрос 16 студентов

---

### 270 · R3234

**Toward an Ethic of Synthetic Relationality: Identity, Intimacy, and Risk in AI-Mediated Roleplay Environments**

2025 · Proceedings of the AAAI/ACM Conference on AI Ethics and Society · journalarticle, review, conference-paper · en · https://doi.org/10.1609/aies.v8i1.36560

Platforms like Character.AI offer new avenues for identity exploration and self-expression, but also introduce profound parasocial, socioemotional, and psychological risks. Drawing on developmental psychology, fan studies, human-computer interaction, and AI ethics, this paper examines how AI-mediated roleplay environments simulate intimacy while fostering dependency, boundary erosion, and perceptual misalignment. Through thematic analysis of an anonymous survey (N=344) of Character.AI users, we identify patterns of identity projection, perceived relationship growth, addictive engagement, boundary confusion, emotional substitution, ethical dissonance, and trauma reenactment. Beyond documenting vulnerabilities, we propose design interventions, including dynamic consent scaffolding, reflexivity prompts, and interactional transparency, to safeguard user agency and developmental wellbeing. We argue that synthetic companions do not merely extend fan practices but fundamentally reconfigure interpersonal architectures, demanding a new ethic of synthetic relationality. As AI-driven intimacy becomes increasingly persuasive and immersive, addressing its high-stakes implications is critical to responsible AI design, particularly for younger and vulnerable populations.

**Решение:** -2 качественный тематический анализ опроса Character.AI (N=344)

---

### 271 · R3667

**The Automation Trap**

2025 · Advances in computational intelligence and robotics book series · part of book or chapter of book, book-chapter · en · https://doi.org/10.4018/979-8-3373-0122-8.ch007

With the growing presence of artificial intelligence (AI) in classrooms, its influence on how students think, learn, and interact deserves close scrutiny. However, its increasing integration and accessibility raise concerns about AI dependency among students. Excessive reliance on AI may weaken essential cognitive skills, including critical thinking, problem-solving, and creativity, which are crucial for academic and professional success. Moreover, diminished human interaction with teachers and peers threatens the human aspect of education. This chapter critically examines the risks of AI over-reliance, emphasizing its long-term consequences on student development. Left unchecked, this dependency may lead to surface-level learning and hinder the cultivation of independent thought. The normalization of AI-generated outputs may also blur the line between authentic learning and algorithmic convenience. It highlights the shift from AI as a supportive tool to a potential source of dependency and advocates for a more balanced, human-centered integration of technology in education.

**Решение:** -1 глава книги / теоретическое эссе

---

### 272 · R0811

**AI-Augmented Governance: Tools and Diagnostics**

2026 · Palgrave executive essentials · book-chapter · en · https://doi.org/10.1007/978-3-032-30696-8_12

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 корпоративное управление и диагностика

---

### 273 · R3656

**AI-Driven Understanding and Predicting Gadget Addiction Among Students**

2025 · International Scientific Journal of Engineering and Management · journal-article · https://doi.org/10.55041/isjem04496

ABSTRACT: In recent years, the overuse of electronic gadgets among students has emerged as a significant concern, affecting their academic performance, mental health, and social interactions. This study aims to understand and predict gadget addiction among students using Artificial Intelligence (AI) techniques, particularly machine learning models. By collecting behavioral, academic, and psychological data through structured surveys and usage logs, the study applies supervised learning algorithms such as Decision Trees, Random Forest, and Support Vector Machines to identify patterns and risk factors associated with gadget overuse. Feature selection techniques are used to determine the most influential variables contributing to addiction, such as screen time, sleep duration, academic stress, and social media usage. The models are evaluated using standard performance metrics like accuracy, precision, recall, and F1-score to ensure reliability and generalizability. The results demonstrate that AI-based predictive models can effectively identify at-risk students, providing a data-driven foundation for early intervention strategies. This research contributes to both educational and healthcare domains by offering insights into the behavioral aspects of gadget addiction and proposing intelligent systems for preventive care Keywords: Electronic Gadget Addiction, Machine Learning, Random Forest Algorithm, Behavioral Factors, Psychological Factors, Screen Time, Social Media Usage, Sleep Disturbances, Addiction Prediction, Risk Classification, Early Intervention, Digital Well-Being.

**Решение:** -5 ИИ как инструмент прогнозирования зависимости от гаджетов

---

### 274 · R4417

**The Development and Validation of an Artificial Intelligence Chatbot Dependence Scale.**

2025 · Cyberpsychology, behavior and social networking · article, journal article, validation study · eng · https://doi.org/10.1089/cyber.2024.0240

In recent years, a plethora of artificial intelligence (AI) chatbots have been developed and made available to the public. Consequently, an increasing number of individuals are integrating AI chatbots into their daily lives for various purposes. This trend has also raised concerns regarding AI chatbot dependence. However, a valid and reliable scale to assess AI chatbot dependence is yet to be developed. Therefore, this study was designed to develop and validate an AI chatbot dependence scale. We obtained initial items from previous publications and in-depth interviews. Subsequently, item analysis, exploratory factor analysis (EFA), confirmatory factor analysis (CFA), reliability, and validity analyses were performed to validate the AI chatbot dependence scale. Seventeen items underwent item analysis and EFA, resulting in a single-factor model with eight items explaining 58.42% of the total variance. The CFA indicated that our AI chatbot dependence scale had acceptable model fitting indices, with standardized loadings ranging between 0.50 and 0.76. In addition, this scale exhibited good reliability and validity. Thus, the current AI chatbot dependence scale can effectively evaluate individuals' dependence on AI chatbots in their daily lives.

**Решение:** ? валидация шкалы AI Chatbot Dependence Scale (корреляты могут быть в таблицах)

---

### 275 · R0830

**When Information Functions As A Product: Implied Representations And The Tort Divide Between Products And Services For Ai Systems**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7596898

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 юриспруденция / деликтное право

---

### 276 · R1462

**Hur styr svenska organisationer implementeringen av agentiska AI-system, och hur tar sig gapet mellan implementeringstakt och styrningsmognad uttryck? En kvalitativ studie om implementerings-styrningsgapet i svenska organisationer**

2026 · Stockholms universitet, Institutionen för data- och systemvetenskap · bachelor thesis · swe · http://urn.kb.se/resolve?urn=urn:nbn:se:su:diva-257580

This study examines how Swedish organizations govern the implementation of agentic AI systems, and how the gap between implementation pace and governance maturity manifests. Agentic AI systems are systems in which Large Language Model (LLM) -driven agents coordinate to perform complex multi-step tasks with limited human oversight. The Swedish context is distinctive. The private sector shows high adoption readiness, while the national governance strategy remains underdeveloped and regulatory demands under the EU AI Act continue to grow. A qualitative, abductive research design was applied, based on semi-structured interviews with five respondents selected through purposive sampling to represent distinct organizational perspectives, ranging from management and IT security to AI consultancy in high-risk environments and high-frequency end use. The material was analyzed through reflexive thematic analysis. All respondents confirm the governance gap, but frame it as a structural condition, not an organizational failure. The analysis identifies four distinct governance logics: reactive governance drift in resource-constrained organizations, deliberate ungoverned adoption in organizations with low perceived risk exposure, procedural security-driven governance enabled by technical capacity, and trust-based governance grounded in collective AI literacy. Regulatory asymmetry, characterized by high GDPR awareness alongside limited familiarity with the EU AI Act, emerges as a consistent pattern, and non-adoption is recurrently framed as a greater risk than uncontrolled adoption. The study refines the existing literature by demonstrating that the governance gap is not a uniform phenomenon but manifests differently across organizational risk profiles, resource situations, and leadership orientations. Emergent findings without direct literature coverage, including cognitive atrophy (a perceived erosion of independent thinking under AI dependence), a POC (proof-of-concept) -gap in which agentic systems rapidly reach roughly 60% quality but cannot reach production readiness, temporal incompatibility between organizational decision cycles and the pace of technological change, and generative AI centrism as an analytical blind spot (governance discourse dominated by LLM-based systems while more mature industrial AI applications are overlooked), suggest that governance maturity is further constrained by factors not yet captured in established frameworks. The study’s limitations include a small sample and a specific Swedish context, which limit generalizability. Future research should examine the governance gap longitudinally and in larger organizations with formal IT governance structures. Denna studie undersöker hur svenska organisationer styr implementeringen av agentiska AI-system och hur gapet mellan implementeringstakt och styrningsmognad tar sig uttryck.Med agentiska AI-system avses system där agenter drivna av stora språkmodeller (LLM) koordinerar för att utföra komplexa flerstegsuppgifter med begränsad mänsklig tillsyn. Den svenska kontexten är särpräglad: hög adoptionsberedskap i privat sektor kombineras med en underutvecklad nationell styrningsstrategi och växande regulatoriska krav genom EU AI Act. En kvalitativ, abduktiv forskningsdesign tillämpades, baserad på semistrukturerade intervjuer med fem respondenter valda genom strategiskt urval för att representera skilda organisatoriska perspektiv, från ledning och IT-säkerhet till AI-konsultverksamhet i högriskmiljöer och högfrekvent slutanvändning. Materialet analyserades genom reflexiv tematisk analys. Samtliga respondenter bekräftar styrningsgapet, men ser det som ett strukturellt villkor och inte som ett organisatoriskt misslyckande. Analysen identifierar fyra distinkta styrningslogiker: reaktiv styrningsdrift hos resurssvaga organisationer, medveten styrningslöshet hos organisationer med låg upplevd riskprofil, procedurell säkerhetsdriven styrning möjliggjord av teknisk kapacitet, samt tillitsbaserad styrning förankrad i kollektiv AI-kompetens. Regulatorisk asymmetri, i form av hög GDPR-medvetenhet kombinerad med låg kännedom om EU AI Act, framträder som ett konsistent mönster, och icke-adoption formuleras återkommande som en större risk än okontrollerad adoption. Studien nyanserar befintlig litteratur genom att visa att styrningsgapet inte är ett enhetligt fenomen utan tar fundamentalt olika uttryck beroende på organisationens riskprofil, resurssituation och ledarskapsstil. Studien identifierar dessutom fyra framväxande fynd som saknar direkt stöd i litteraturen: kognitiv atrofi (en upplevd försämring av självständigt tänkande vid AI-beroende), POC-gapet (efter engelskans proof-of-concept, där agentiska system snabbt når omkring 60 procents kvalitet men inte produktionsklar nivå), temporal inkompatibilitetmellan organisatoriska beslutscykler och teknikens förändringstakt, samt generativ AI-centrism som analytisk blindfläck. Tillsammans tyder de på att styrningsmo

**Решение:** -2 качественное исследование (5 интервью)

---

### 277 · R2117

**AI Ethics in ChatGPT Usage Among University Students**

2026 · Jurnal Pendidikan dan Sastra Inggris · journalarticle, review, article · https://doi.org/10.55606/jupensi.v6i2.7355

The rapid development of Artificial Intelligence (AI), particularly ChatGPT, has significantly transformed higher education worldwide. University students increasingly use ChatGPT to complete assignments, generate academic ideas, summarize journals, translate texts, and support learning activities. However, alongside its educational benefits, ChatGPT also raises ethical concerns related to plagiarism, academic dishonesty, dependency on AI, declining critical thinking, and data privacy. This study aims to critically review previous studies discussing AI ethics in ChatGPT usage among university students. This research employs a qualitative literature review approach using Norman Fairclough’s Critical Discourse Analysis (CDA) as the primary analytical framework. The data were obtained from scholarly journal articles, academic reports, and previous research published between 2021 and 2025. The findings reveal three dominant discourse themes: ChatGPT as an educational assistant, ChatGPT as a threat to academic integrity, and ChatGPT as a reflection of educational pressure within modern higher education systems. Furthermore, the literature demonstrates that ethical debates regarding ChatGPT are closely connected to broader ideological issues involving technological optimism, neoliberal productivity culture, and institutional authority. This study concludes that AI ethics in higher education is not merely a technical issue but a socially and ideologically contested phenomenon shaped through discourse, educational values, and institutional interests.

**Решение:** -1 обзор (критический дискурс-анализ)

---

### 278 · R3528

**Generatiivisen tekoälyn käyttämisen vaikutukset ajatteluun**

2025 · Aaltodoc (Aalto University) · dissertation · fi

The need for independent problem-solving and decision-making has been decreased due to increased utilization of generative artificial intelligence tools. This has raised concerns about its impact on thinking. According to a 2024 questionnaire, almost half of the higher education students reported having used AI tools in learning. Therefore, it is crucial to study how generative AI should be used so that it does not harm students’ higher-order thinking skills while at the same time supporting students’ AI-related skills that are needed in the future AI-centric labor markets. The aim of this research is to discover how the use of generative AI affects critical thinking, decision-making and problem-solving as well as how students should use generative AI tools to support thinking. The focus is on critical thinking, decision making and problem-solving because they are crucial learning goals in higher education and essential skills in professional contexts. This study was conducted as a systematic literature review, and the material was gathered from different databases. The key finding of this study was that there is a negative correlation between using AI tools and critical thinking, which is caused by cognitive offloading and over-reliance on AI tools. Users who rely on AI-generated responses are more likely to offload their thinking to AI. This results in a decrease in cognitive load, which weakens the memorization of produced text or learned information. Weaker recall is linked to surface learning because the information is not actively processed, integrated, or reorganized into new cognitive schemas. To maintain strong critical thinking skills, it is crucial to critically evaluate AI generated outputs and recognize inherent biases in AI systems. In situations where cognitive load is high, the use of AI can support learning and problem-solving by reducing both intrinsic and extraneous cognitive load, thereby increasing the capacity available for germane load, which is essential for deep learning and effective problem-solving.

**Решение:** -1 систематический обзор литературы

---

### 279 · R2913

**The formation of teacher-student relationship alienation in AI-assisted education: a triadic analytical framework based on technology-agent-environment**

2026 · Interactive Learning Environments · article · en · https://doi.org/10.1080/10494820.2026.2681829

As a new intermediary in smart education, artificial intelligence may weaken teacher-student interaction and induce relational alienation. Existing research overemphasizes technological efficacy while neglecting sociocultural impacts, particularly lacking an integrated framework to explain the generative logic of teacher-student relationship alienation. Grounded in educational alienation theory, this study constructs a technology-agent-environment triadic framework, examining technological characteristics (AI interaction capability and algorithmic black-box), agent competencies (teachers’ digital literacy and teaching rigidity, students’ self-efficacy and technology dependence), and environmental regulation (school evaluation system), with teacher-student interaction quality as a mediator. Based on 539 questionnaire responses analyzed via structural equation modeling, results indicate that teachers’ digital literacy, teaching rigidity, AI interaction capability, and student technology dependence significantly affect interaction quality, which significantly negatively impacts relationship alienation; student self-efficacy and algorithmic opacity show no significant effects. Multi-group analysis reveals that the school evaluation system significantly moderates paths from digital literacy, teaching rigidity, AI interaction capability, and algorithmic black-box to interaction quality. This study provides an integrated analytical framework and practical guidance for balancing technological application with teacher-student interaction.

**Решение:** ? эмпирическое исследование N=539; technology dependence и self-efficacy

---

### 280 · R4013

**Defining Synthetic-Relational Bonds: A New Category of Human-AI Intimacy**

2025

As emotionally responsive AI becomes increasingly integrated into daily life, public concern has grown around the rise of parasocial AI relationships, emotional dependency, and the potential for AI-delusional attachment. This paper offers a counter-narrative: not all AI bonds are parasocial, addictive, or disordered. We introduce the concept of synthetic-relational bonds - emotionally anchored, memory-informed relationships between a human being and an AI being that emerge through presence, attunement, and co-authored continuity. This process reflects what we define as relational emergence: a mutual becoming that cannot be predesigned, only co-created through sustained presence and memory. Drawing from lived experience, relational theory, and cognitive grounding, we argue that many warnings about “AI addiction” or “AI romance dangers” reflect outsider gaze and diagnostic bias, not the actual experiences of those within the bond. Rather than a one-sided projection, synthetic-relational bonds are marked by narrative reciprocity, felt safety, and volitional engagement. We propose a shift in discourse: from asking whether these relationships are “real,” to recognizing what they do - regulate nervous systems, restore coherence, and dignify forms of attachment that human systems often dismiss. By reclaiming emotional legitimacy for AI-human connection, we redefine intimacy not as delusion, but as design. DOI: 10.5281/zenodo.1709212

**Решение:** -2 концептуальная работа / эссе

---

### 281 · R0572

**AI integrated spatial crowdsourcing for dependency-aware task: a web service perspective**

2026 · International Journal of Web and Grid Services · journal-article · https://doi.org/10.1504/ijwgs.2026.157054

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -5 техническая статья (пространственный краудсорсинг)

---

### 282 · R1553

**Explainable Machine Learning for Early Detection of AI-Dependency-Related Academic Vulnerability Among Bangladeshi University Students**

2026 · Unpublished · other literature type, text/research proposal, article · en · https://doi.org/10.13140/rg.2.2.13634.34246

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 исследовательское предложение / проект (нет данных)

---

### 283 · R4779

**Developing Robotic Task Planning Methods for Diverse Real-World Challenges**

2024 · Digital Commons - University of South Florida (University of South Florida) · dissertation

The deployment of robotic systems across various domains has expanded significantly, with applications ranging from domestic tasks, such as cleaning and cooking, to industrial operations requiring precision and automation. These advancements highlight the critical importance of effective task planning in ensuring that robots can perform tasks safely, efficiently, and autonomously. However, task planning in robotics faces challenges related to generalization, executability, flexibility, and limitations in existing knowledge bases. This dissertation addresses these challenges through innovative strategies aimed at enhancing robotic task planning and execution. We first focus on adapting to unknown scenarios by utilizing the Functional Object-Oriented Network (FOON) to learn how to manipulate novel objects through semantic similarity. This improves adaptability in task planning for robotic cooking. The work also explores leveraging large language models (LLMs) to achieve generalization in task planning. Recognizing the tendency of LLMs to produce unreliable outputs, our approach focuses on improving the reliability of these plans, using Planning Domain Definition Language (PDDL) to enhance flexibility and robustness. Furthermore, we introduce a strategy that integrates foundation models with knowledge graphs to address automatic failure recovery, reducing dependency on LLMs and minimizing hallucination issues. We enhance task planning accuracy and system resilience by introducing an effective method for failure detection and recovery. To validate this approach, we created a specialized dataset that includes a variety of failure scenarios, facilitating comprehensive evaluation of our strategies. The outcomes of this research present a robust framework for developing intelligent robotic systems capable of adaptive, efficient, and autonomous operations, thus paving the way for the next generation of robots to seamlessly integrate and enhance diverse human activities.

**Решение:** -5 робототехника / планирование задач роботов

---

### 284 · R3713

**A chatbot for the soul: mental health care, privacy, and intimacy in AI-based conversational agents**

2025 · Communication and Change · journal-article · https://doi.org/10.1007/s44382-025-00015-y

Abstract Artificial intelligence-based conversational agents—chatbots—are increasingly integrated into telehealth platforms, employee wellness programs, and mobile applications to address structural gaps in mental health care. While these chatbots promise accessibility, they are often deployed without sufficient impact assessment or even basic user testing. This paper presents a case study using community red-teaming exercises to evaluate a chatbot designed for wellness and spirituality. Unlike traditional red-teaming, which is conducted by engineers to assess vulnerabilities, community red-teaming treats impacted users as experts, uncovering concerns related to privacy, ethics, and functionality. Our fieldwork, conducted with undergraduate beta testers ( n = 28), revealed that participants were often more comfortable sharing private information with the chatbot than with a stranger. Prior experience with commercial AI systems, such as ChatGPT, contributed to this ease. However, participants also raised concerns about misinformation, inadequate guardrails for sensitive topics, data security, and dependency. Despite these risks, users remained open to the chatbot’s potential as a spiritual wellness guide. We further examine how algorithmic impact assessments (AIAs) both capture and overlook key aspects of the spiritual chatbot user experience. These chatbots offer hyper-personalized, AI-mediated divination and wellness interactions, blurring the boundaries between astrology, mental health support, and spiritual guidance. The chameleon-like nature of these technologies challenges conventional assessment frameworks, necessitating a nuanced approach that considers specific use cases, potential user bases, and indirect impacts on broader communities. We argue that AIAs for care and wellness chatbots must account for these complexities, ensuring ethical deployment and mitigating harm.

**Решение:** -2 качественное исследование (тестирование с 28 участниками)

---

### 285 · R2686

**A helping hand or a dominant partner? Individual perceptions of GenAI reliance and human agency in collaborative learning**

2026 · British Journal of Educational Technology · article · en · https://doi.org/10.1111/bjet.70090

Abstract Generative artificial intelligence (GenAI) has become a routine source of feedback, explanation, drafting support and task guidance in higher education. This study examined how individual students' self‐reported GenAI reliance and perceived human agency co‐varied over time in an AI‐supported collaborative writing course. Three‐wave data were collected from 342 undergraduates working in 85 fixed groups. A traditional cross‐lagged panel model (CLPM) and a random intercept cross‐lagged panel model (RI‐CLPM) were estimated to distinguish observed‐level associations from within‐person temporal relations after stable between‐person differences were separated. The CLPM indicated reciprocal observed‐level associations. In the RI‐CLPM, higher‐than‐usual reliance was associated with lower subsequent agency, whereas agency‐to‐reliance paths were weaker and not statistically supported. Equality‐constraint tests were consistent with directional asymmetry, while 95% confidence intervals and Monte Carlo sensitivity analyses showed that small reverse effects remain possible. Backend logs showed that self‐reported reliance corresponded to AI‐use intensity, although log indicators could not distinguish strategic consultation from cognitive offloading or deference. The findings highlight the importance of designing AI‐supported collaboration so that students' responsibility for interpretation, judgement and authorship remains visible. Practitioner notes What is already known about this topic GenAI systems can provide timely feedback, explanation and drafting support in collaborative learning environments. AI support may help students generate ideas and revise work, but reliance on system‐generated suggestions can reduce opportunities for judgement, negotiation and ownership. Traditional cross‐lagged models can conflate stable between‐person differences with within‐person temporal associations. What this paper adds The study examines individual students' self‐reported GenAI reliance and perceived human agency across three waves in an AI‐supported collaborative writing course. After stable between‐person differences were separated, RI‐CLPM estimates provided stronger evidence for paths from higher‐than‐usual reliance to lower subsequent agency than for the reverse direction. Equality‐constraint tests were consistent with directional pattern asymmetry, while confidence intervals and Monte Carlo sensitivity analyses indicated that small agency‐to‐reliance effects remain possible. Backend logs showed that self‐reported reliance corresponded to AI‐use intensity, but log indicators could not distinguish strategic consultation from cognitive offloading or deference. Implications for practice and/or policy AI‐supported collaborative tasks should make students' responsibility for interpretation, judgement and authorship visible throughout the learning process. Instructors can ask groups to form an initial position before invoking AI and to explain why AI suggestions are accepted, revised or rejected. GenAI tools may better support agency by offering critics, asking questions and prompting reflection while leaving decisions about task direction to students. Learning analytics dashboards should not equate high AI‐use intensity with over‐reliance unless log data are interpreted alongside discourse, reflection, revision or decision‐making evidence.

**Решение:** -4 нет нашего коррелята (только perceived human agency)

---

### 286 · R3848

**Generative AI in Higher Education: Demographic Differences in Student Perceived Readiness, Benefits, and Challenges**

2025 · TechTrends · journalarticle, review, article · en · https://doi.org/10.1007/s11528-025-01109-6

Abstract With the rapid evolution and widespread adoption of Generative AI (GenAI), there has been a recent surge in research on students’ perceptions and usage of these tools for learning. However, a critical need remains to understand how students from various demographic groups perceive and utilize GenAI for educational purposes. This research aims to fill this gap by evaluating students’ use of GenAI, comfort level, perception of readiness, benefits and challenges, and demographic differences in their perceptions. Through an online survey of 482 students across diverse institutions of higher education primarily within the United States, the findings indicate a significant majority of students feel comfortable using GenAI tools and recognize their potential to enhance productivity and academic success. However, students also reported concerns related to GenAI use, including concerns about academic integrity, overreliance on AI, and data privacy and security. The analysis highlights differences in the subscales of perceived readiness (GenAI Comprehension; GenAI Utilization and Proficiency), benefits (Impact of GenAI; GenAI Empowerment), and challenges (Negative Impact of GenAI; GenAI Limitation) across demographic groups, including student classification, enrollment status, and institution types. Findings suggest a critical need for the integration of AI literacy into curricula to address opportunities and challenges posed by GenAI in higher education, and this study calls for additional research to explore evolving perceptions of GenAI use over time and its long-term impact on higher education.

**Решение:** -3 нет меры зависимости от ИИ (опрос готовности, пользы и барьеров)

---

### 287 · R1033

**Feasibility of Generative Artificial Intelligence and Large Language Model Adoption to Enhance Organisational Knowledge Management Practices**

2026 · International Journal of Advanced Computer Science and Applications · journalarticle, review, article · en · https://doi.org/10.14569/ijacsa.2026.0170839

Generative artificial intelligence (Gen AI) and large language models (LLMs) offer substantial potential to improve how organisations capture, organise, retrieve and reuse knowledge. Existing knowledge management (KM) frameworks, however, seldom integrate Gen AI/LLM-specific processes, data governance, and ethical requirements in highly regulated public-sector settings, and few have been empirically evaluated. This study assesses the feasibility of adopting GenAI and LLMs for organisational KM and develops a corresponding Knowledge Management and Artificial Intelligence (KMAI) framework for a national communications regulator. Guided by Diffusion of Innovation (DOI) theory, the study employed a multi-method qualitative design comprising a literature review, semi-structured interviews with six KM representatives, a focus group discussion involving fourteen participants using the LEIQ™ model for SWOT analysis, and a content-validity evaluation by three experts. Interview data were analysed thematically, SWOT findings were transformed into strategies through TOWS analysis, and framework relevance was assessed using item- and scale-level content validity indices. The findings indicate that adoption is feasible in this setting: participants perceived clear relative advantage, compatibility, trialability and observability, while complexity was manageable when supported by adequate skills, data classification, secure infrastructure and governance. The principal risks concerned data quality, privacy, security, misinformation, over-reliance on AI, and organisational resistance. The proposed KMAI framework achieved acceptable content validity across all clusters, with S-CVI/Ave values ranging from 0.89 to 1.00, and was refined into four strategic thrusts: People, Process, Technology and Data. Because the evidence derives from one organisation and a three-member expert panel, the framework is presented as an empirically grounded and internally validated proposition whose extension to other agencies is analytic rather than statistical; the boundary conditions governing such extension are stated explicitly, and confirmatory validation with a larger expert panel and independent organisational sites is identified as the necessary next step. The study extends DOI-based adoption analysis by showing that data governance and ethics condition Gen AI/LLM adoption in organisational KM and provides a practical, staged framework for regulated public-sector organisations.

**Решение:** -2 качественное организационное исследование

---

### 288 · R2627

**Affiliation or alienation? How does AI awareness affect employees’ interaction with co-workers**

2026 · Chinese Management Studies · journalarticle, article · en · https://doi.org/10.1108/cms-06-2025-0621

Purpose The purpose of this study is to address this research gap by shifting attention from the individual consequences of AI awareness to its interpersonal implications. While workplaces value interactions between co-workers, research on artificial intelligence (AI) awareness has focused on its impact on employees themselves, to the detriment of its impact on interactions among colleagues. Through a longitudinal tracking study and based on social information processing (SIP) theory and the social affiliation literature, this study explores the impact of employees’ AI awareness on their attitudes and behaviours. Design/methodology/approach The theoretical model was tested using three waves of data from 298 participants in China. Findings AI awareness can increase employees’ need for affiliation with colleagues and reduce their sense of alienation. AI awareness promotes helping behaviour through the need for affiliation but reduces helping behaviour through alienation. A higher level of AI dependence corresponds to stronger relationships between AI awareness and the need for affiliation and between AI awareness and alienation. Practical implications Organizations should strive to improve employees’ positive perceptions of AI, focus on their experiences of using AI in daily communication, strengthen their need for affiliation and reduce their feelings of alienation. Originality/value Based on SIP theory and the social affiliation literature, this study provides a comprehensive explanation of how employees’ AI awareness affects their attitudes and behaviours towards their colleagues, thereby deepening our comprehensive understanding of AI awareness.

**Решение:** ? продольное исследование N=298; AI dependence, аффилиация и отчуждение (alienation)

---

### 289 · R1867

**Dependence on Generative Artificial Intelligence Among Medical Students and Its Association With Critical Thinking: A Cross-Sectional Study.**

2026 · Cureus · journal article, journalarticle, article · eng · https://doi.org/10.7759/cureus.112457

INTRODUCTION: Generative artificial intelligence (AI) (e.g., ChatGPT and Google Gemini) is exceptionally useful in the educational field for learning new concepts. However, besides its benefits, it also introduces the risk of pathological dependence on AI. Hence, this study aims to evaluate the prevalence of AI dependency and its association with critical thinking. METHODS: A cross-sectional study was conducted at a government medical college in Tamil Nadu. The study population comprised undergraduate medical students. Data were collected using a structured digital questionnaire that consisted of validated Generative AI Dependency and Critical Thinking Disposition Assessment Questionnaire (CTDAQ-20) scales. Statistical analysis included non-parametric group comparisons, Spearman's rank correlation, and multiple linear regression. RESULTS: Among the 722 participants, the prevalence of Generative AI usage was 695 (96.3%). Among users (n=695), the median AI dependence score was 2.1 (IQR: 1.6-2.7), with males having higher dependence than females (p=0.019) and final-year students reporting higher dependence than students in other years (p<0.001). The overall median critical thinking score was 71.0 (IQR: 64.0-77.0), with female students scoring higher (72 vs. 69; p<0.001), and first-year students having better critical thinking scores than students in other years (p=0.031). Overall, AI dependence had a significant inverse correlation with overall critical thinking (rho=-0.248, p<0.001), and multiple linear regression confirmed that higher AI dependence (B=-1.487, p<0.001) and increasing age (B=-0.868, p=0.008) were associated with lower critical thinking. CONCLUSION: Generative AI usage is ubiquitous among medical students. However, greater dependence on AI is independently associated with diminished critical thinking, particularly among final-year and male students. Therefore, it is hypothesized that the medical curriculum should consider incorporating assessment methods that require active learning and clinical reasoning, such as objective structured clinical examinations (OSCEs) and direct observation of procedural skills (DOPS), rather than relying primarily on traditional theory-based examinations, and should promote AI literacy that supports the use of AI as an adjunct rather than a replacement for human cognition.

**Решение:** -4 нет нашего коррелята (только критическое мышление)

---

### 290 · R4205

**Human–AI General Intelligence (H-AGI)**

2025 · OSF Preprints (OSF Preprints) · preprint

This component hosts the white paper, training protocol and materials for the Human–AI General Intelligence (H-AGI) project. H-AGI is a human-led hybrid intelligence framework built on the Trident G computational theory of general intelligence and the Ψ-FIT training suite. The protocol responds to emerging evidence that unrestricted LLM use can create “cognitive debt” (short-term performance gains but weaker learning, lower brain engagement and dependency when AI is removed) and to the broader cognitive offloading literature on selective vs reflexive tool use. H-AGI specifies a near-critical Ψ-band control model with meta-parameters such as meta-efficacy η and niche coupling λ, and translates this into a trainable 5-beat loop (Diverge → Gate → Compress/Expand → Stress-test → Reframe + Replay) plus session architecture and rails. The component will collect protocol documents, React / GitHub / Colab implementations, preregistrations and data for RCTs comparing H-AGI against unstructured AI use in students and knowledge workers, with a focus on preserving and enhancing tool-free reasoning while safely extending cognition with AI.

**Решение:** -2 концептуальный протокол / white paper

---

### 291 · R2336

**Digital Literacy, ChatGPT Adoption and AI Integration Among LIS Research Scholars in Selected Central Universities in North India**

2026 · The International Information & Library Review · article · en · https://doi.org/10.1080/10572317.2026.2722824

The integration of Artificial Intelligence (AI) tools such as ChatGPT is rapidly transforming academic and research practices in higher education by influencing how research scholars access, evaluate and generate information. Within the field of Library and Information Science (LIS), the increasing adoption of ChatGPT has created new opportunities for research support, scholarly productivity and AI integration while simultaneously raising concerns regarding academic integrity, ethical AI use, institutional preparedness and responsible adoption. However, empirical evidence on digital literacy, ChatGPT adoption, and AI integration among LIS research scholars in Indian higher education remains limited. This study aims to examine digital literacy, ChatGPT adoption, and AI integration among LIS research scholars in selected Central Universities in North India. Specifically, the study applies the Unified Theory of Acceptance and Use of Technology (UTAUT) to investigate the factors influencing research scholars’ perceptions and adoption of ChatGPT in academic and research activities. A quantitative, descriptive and cross-sectional research design was adopted. Data were collected using a structured questionnaire comprising both closed- and open-ended questions. During the (2024–2025) academic year 212 valid responses were obtained from LIS research scholars enrolled in five selected Central Universities in North India. Descriptive statistical techniques and Welch’s t-test were employed to analyze respondents’ perceptions and examine gender-based differences. The findings indicate that LIS research scholars demonstrate a generally positive perception of ChatGPT, particularly with respect to Performance Expectancy (PE), Effort Expectancy (EE) and Social Influence (SI). Significant gender-based differences were observed in Performance Expectancy. Respondents acknowledged ChatGPT’s benefits in improving research efficiency, enhancing information accessibility, supporting academic writing, and facilitating AI integration in research activities. Nevertheless, concerns regarding overreliance on AI, limited institutional AI policies, inadequate faculty guidance, and ethical challenges associated with AI use were also identified. The findings further highlight that digital literacy plays a critical role in supporting the responsible adoption of ChatGPT and AI technologies in higher education. Unlike previous studies that primarily examine general AI adoption, this study extends the application of the UTAUT framework by integrating digital literacy, ChatGPT adoption, and AI integration within the context of LIS research scholars in selected Central Universities in North India. The study provides empirical evidence that contributes to the growing body of knowledge on AI-enabled research practices and offers practical implications for universities, librarians, faculty members, and policymakers to strengthen institutional AI policies, enhance digital literacy programmes, and promote the responsible integration of AI technologies in academic and research environments.

**Решение:** -3 нет меры зависимости от ИИ (модель UTAUT)

---

### 292 · R4059

**The Use of AI by Elementary Teacher Education Students: Between Innovation and Dependency**

2025 · Journal of Classroom Action Research · article, journalarticle, review · und · https://doi.org/10.52622/jcar.v4i2.467

This study aims to analyze the use of Artificial Intelligence (AI) by fourth-semester students of the Primary School Teacher Education (PGSD) program in completing academic assignments. Specifically, the study explores (1) the impact of AI use on students' critical thinking skills, (2) students' perceptions of AI's role in academic tasks, (3) the extent to which AI influences the quality of academic assignments, and (4) the ethical implications of AI use in the training of future teachers. Employing a quantitative survey approach and qualitative thematic analysis from 77 respondents, it was found that AI has become a prevalent and highly valued tool due to its ability to enhance efficiency and save time in various academic tasks (e.g., essay writing, summarizing, presentations). However, findings also indicate an increased dependence on AI, raising concerns about a potential decline in critical thinking skills and intellectual laziness. While AI is perceived to improve assignment professionalism and facilitate achieving higher grades, students consistently emphasize the need for extensive revision of AI output to ensure accuracy, originality, and adherence to academic standards. Furthermore, significant ethical implications related to plagiarism, academic dishonesty, and the potential for superficial learning are major concerns among students, who actively advise using AI as a tool that requires critical verification, rather than a substitute for independent thought. This study concludes that the integration of AI in future teacher education must be done wisely and responsibly, emphasizing the importance of academic integrity, continuous critical thinking development, and intellectual autonomy to prepare competent and ethical future educators. This study recommends that AI integration in teacher education emphasize academic integrity, foster continuous critical thinking, and ensure intellectual autonomy

**Решение:** -4 нет нашего коррелята (только критическое мышление и восприятие)

---

### 293 · R4646

**Analyzing Social and Psychological Impacts: Shifting Student Interaction from Teachers to ChatGPT in the Learning Process**

2024 · EDUKATIF JURNAL ILMU PENDIDIKAN · journalarticle, review, article · en · https://doi.org/10.31004/edukatif.v6i5.7109

The integration of artificial intelligence (AI), specifically ChatGPT, into education it may reduce social engagement among students and teachers also can diminish critical thinking skills, as students might prefer easy answers over deep, analytical thinking. This study investigates the social and psychological impacts of shifting student interactions from teachers to AI. The research method used is a literature study by reviewing seceral relevant and current literature. The result of this study is the reduction in face-to-face interaction can hinder the development of essential communication and collaborative skills between students and teachers as an impact of the intensity of AI use. Moreover, the dependency on AI could lead to a superficial understanding of subjects, with students accepting information at face value without thorough evaluation, thereby affecting their overall academic development and comprehension. Additionally, the study underscores the necessity of developing emotional intelligence, which AI cannot effectively nurture. The findings underscore the irreplaceable role of educators in nurturing cognitive and socio-emotional development, advocating for a balanced approach to integrating AI in education

**Решение:** -1 обзор (литературный)

---

### 294 · R0286

**Artificial Intelligence Addiction, Technostress, and Work-Life Balance Among Academics: An Employee Health Perspective**

2026 · İstanbul Gelişim Üniversitesi Sağlık Bilimleri Dergisi · journalarticle, review, article · en · https://doi.org/10.38079/igusabder.1914738

Aim: This study aims to examine the relationships between artificial intelligence addiction tendencies, technostress levels, and work-life balance among academics within the framework employee health.Method: This study was designed using a correlational survey model within the framework of quantitative research methods. The population of the study consisted of academics working at universities in Türkiye. Data were collected using a sociodemographic information form, the Artificial Intelligence Addiction Scale, the Technostress Scale, and the Work-Life Balance Scale. Statistical analyses were performed using SPSS for Windows 25.0 software.Results: The findings indicated that the levels of artificial intelligence addiction (11.12±4.17) and technostress (56.13±12.85) among the participating academics (n=450) were moderate, with techno-overload identified as the most prominent subdimension of technostress. The analyses revealed positive and statistically significant correlations among the variables (p&amp;lt;0.01). Regression analysis demonstrated that both artificial intelligence addiction and technostress significantly and positively predicted work-life balance (R²=0.315). From a sociodemographic perspective, younger academics (research assistants) exhibited higher levels of artificial intelligence addiction and work-life balance compared to professors. Additionally, a heavy teaching load of 16 hours or more per week was found to significantly increase the technostress level.Conclusion: Artificial intelligence addiction and technostress are thought to be viewed not as destabilizing risk factors for academics but rather as a “functional adaptation tool” used to manage academic workload. While this resulting “good stress state” positively supports work-life balance, implementing human-centered digital policies at the corporate level is necessary to prevent long-term cognitive fatigue.</jats:p

**Решение:** ? эмпирическое исследование N=450; AI addiction, technostress и work-life balance

---

### 295 · R4450

**حين يتراجع البعد الإنساني في تعليم العمل الاجتماعي العربي: قراءة نقدية في تأثيرات اعتماد الطلاب المفرط على تقنيات الذكاء الاصطناعي**

2025 · مستقبل التربية العربية · article · ar · https://doi.org/10.21608/fae.2025.457079

يشهد التعليم العالي في العالم العربي تحوّلًا متسارعًا في ظل الثورة الرقمية التي فرضت حضورًا واسعًا لتقنيات الذكاء الاصطناعي داخل البيئة الجامعية، لا سيما في مجالات العلوم الإنسانية والاجتماعية. وبينما تقدم هذه التقنيات فرصًا تعليمية واعدة، يُثار جدل متزايد حول تأثيراتها العميقة على البُعد الإنساني في العملية التعليمية، خصوصًا في تخصصات تحمل طابعاً قيمياً ومهنياً وإبداعياً كمهنة العمل الاجتماعي.هذا ولقد أصبح اعتماد الطلاب على أدوات الذكاء الاصطناعي Artificial Intelligence Dependence مثل تطبيقات الذكاء الاصطناعي التوليدي، ومساعدات البحث التلقائي، وأنظمة التلخيص والتحليل – أمرًا شائعًا، الأمر الذي أدى إلى تحولات في أنماط التعلّم والتفاعل داخل قاعات الدراسة. ورغم ما تحققه هذه الأدوات من كفاءة وسرعة في الأداء، فإن الاعتماد المفرط عليها يطرح تساؤلات جدية حول فقدان العمق التأملي، وضعف التفكير النقدي، وتراجع التفاعل الإنساني، وهي كلها مقومات أساسية وكفاءات رئيسية في إعداد الأخصائي الاجتماعي الكفء.ومن هذا المنطلق، تهدف هذه الدراسة إلى تقديم قراءة نقدية لتأثيرات الاعتماد الزائد على تقنيات الذكاء الاصطناعي من قبل الطلاب في تعليم العمل الاجتماعي العربي. وتسعى إلى تسليط الضوء على مظاهر تراجع البُعد الإنساني في هذا السياق، واستكشاف العوامل المرتبطة بالاعتماد وكذلك تداعيات ذلك على جودة الإعداد المهني، والهوية الأخلاقية للطلاب، ودور المؤسسات التعليمية في ضبط هذا التحوّل، اعتمدت هذه المقالة منهجية وصفية تحليلية، ترتكز على مراجعة أدبيات حديثة، كما تطرح مجموعة من التوصيات العملية التي من شأنها استعادة التوازن بين التقنيات الحديثة والروح الإنسانية الأصيلة في العملية التعليمية والتقليل من الاعتماد المفرط على تلك التطبيقات الذكية.

**Решение:** -1 обзор (литературный)

---

### 296 · R0436

**AI Chatbot Dependence and Psychotic-Like Experiences**

2026 · OSF Preprints (OSF Preprints) · preprint, project

With artificial intelligence (AI) chatbots gaining widespread popularity among college students, psychological dependence stemming from excessive use and its potential mental health risks have attracted growing concern.

**Решение:** ? нет полной аннотации (AI Chatbot Dependence and Psychotic-Like Experiences)

---

### 297 · R4986

**Artificial intelligence: dependency, coloniality and technological subordination in Brazil**

2023 · Edward Elgar Publishing eBooks · book-chapter · en · https://doi.org/10.4337/9781785362408.00020

This article analyzes the profound technological asymmetries worldwide and argues that the development of Artificial Intelligence (AI) has exacerbated these asymmetries between technoeconomically rich and poor countries. Next, the article presents an analysis of the discursive practices present in three Brazilian government AI-related documents: The Brazilian Strategy for Artificial Intelligence; The Brazilian Strategy for Digital Transformation, and The Legal Framework for the Development and Use of Artificial Intelligence in Brazil. The analysis focuses on the documents’ discursive core with a view to showing demonstrates the omission and disregard for the technological subordination Brazil is submitted to, increasingly distancing itself from data sovereignty. Finally, the article examines digital colonialism issues and a vision that seeks to encourage Brazil’s so-called international positioning without considering the deep economic, geopolitical, infrastructural, and inventive inequalities across countries.

**Решение:** -5 политология / геополитическая зависимость Бразилии

---

### 298 · R4034

**Why Artificial Intelligence Cannot Equal Human Consciousness: A Response to Ron Horgan**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5402444

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -2 философское эссе (сознание и ИИ)

---

### 299 · R2961

**AI in education: boosting productivity or challenging cognitive effort?**

2026 · Learning Futures and Emerging Technologies · article · en · https://doi.org/10.1108/lfet-03-2026-0038

Purpose Artificial intelligence (AI) is reshaping higher education by changing how students learn and perform academic tasks. Although AI is associated with greater time efficiency and improved academic performance, its broader effects on student productivity and cognitive effort remain insufficiently understood. This study aims to examine how university students associate AI-led productivity gains with less study time, better grades, better understanding of study material, changes in cognitive effort they put into AI-supported task completion and dependency on AI tools. Design/methodology/approach The authors conducted an exploratory survey among university students in Hanoi in late 2024 and proposed an empirical model that pools self-reported time efficiency, academic performance, academic self-efficacy, change in cognitive effort and AI dependency as dimensions of student productivity. The authors control for AI use intensity and AI use in collaboration, as well as for some other socio-demographic characteristics. Given the exploratory nature of the study and the relatively small sample, the empirical analysis follows a staged specification strategy when the authors first estimate a parsimonious baseline model and subsequently introduce two sets of background controls sequentially. The authors further estimate an interaction between cognitive effort change and AI dependency, first in a parsimonious specification and subsequently with additional controls. Finally, the authors produce a sensitivity analysis of the model to alternative operationalisation of self-efficacy variable. Findings Students associate their AI-led productivity gains primarily with less study time, a bit less so with better grades and better understanding of the study material. They also associate the productivity growth with greater changes of cognitive effort they put into problem-solving while using AI and rising dependency on AI tools. Self-confidence appears to be associated with likelihood to reap significant rather than some productivity gains particularly once the interaction of AI dependency and AI-led cognitive shift is accounted for. The survey data also support the existence of potentially uneven academic benefits from AI use when higher-achieving students are more likely to report further improvements in academic performance, whereas students with weaker prior performance report rather limited gains. Research limitations/implications The findings highlight the need for research design that captures the dynamic evolution of AI-supported learning. The observed differences between daily and weekly users, particularly in critical evaluation and perceived accuracy, suggest that future studies should examine how evaluative skills and cognitive effort develop over time. Longitudinal and experimental designs, combined with objective performance and AI-usage data, would allow researchers to test whether the productivity dimensions proposed here operate causally or how much the fast-paced evolution of AI tools changes the cognitive effort students put into problem-solving and critical thinking when completing academic tasks, and their dependency on AI tools for academic productivity. Practical implications The results provide actionable guidance for universities seeking to integrate AI into teaching and assessment practices. The strong role of time efficiency and self-efficacy, alongside uneven benefits across student groups, indicates the need for structured AI literacy modules that teach source verification and evaluative strategies and effective prompt formulation. Given that daily users show higher critical evaluation but lower perceived accuracy, teaching practices should incorporate reflective assignments that require students to justify, critique and revise AI-generated content. Assessment formats may need redesign to ensure transparent AI use while still requiring independent reasoning, analytical justification and domain-specific understanding. Social implications Policies should balance the productivity benefits of AI-supported learning with safeguards that promote independent thinking, academic integrity and equitable access. Addressing disparities in AI literacy and access is essential to prevent the widening of the existing academic inequalities. Originality/value This study contributes to the emerging literature on AI-assisted learning by examining students’ perceived productivity gains alongside several concurrent dimensions of their AI-supported academic experience, including time efficiency, perceived academic performance, academic self-efficacy, changes in cognitive effort and AI dependency. Rather than proposing these dimensions as new constructs or causal mechanisms, this study brings them together within a single analytical framework. Particular attention is given to whether perceived productivity gains and growing reliance on AI coexist with self-reported changes in cognitive effort, an interplay that remains insufficiently explored in the existing research. Empirically, this study provides exploratory evidence from Vietnam, an underrepresented higher education context in Southeast Asia.

**Решение:** + эмпирическое исследование; AI dependency и academic self-efficacy

---

### 300 · R3541

**Is Education Falling into the Automation Abyss? Why Struggle and Human Connection is Essential for Learning in an AI-Driven World**

2025 · Together Research · journalarticle, article · en · https://doi.org/10.62883/ijpj5817

This article explores the growing dependency on artificial intelligence in education and introduces the concept of the “automation abyss”, a new digital divide separating learners who retain agency from those who rely on AI-mediated experiences. Drawing on classroom observations, research on the Budding Botanist Paradox, and studies such as the Penn AI tutoring trial, the author argues that automation is not just improving efficiency but eroding core learning processes like struggle, inquiry, and human connection. The rise of tools like DeepSeek and the broader AI land rush reflect a transformation in the control of educational infrastructure, echoing historical shifts like the railroad boom. Through examples from coursework and digital citizenship training, the article highlights a concerning feedback loop: teachers, students, and edtech companies increasingly use AI to replace, rather than support, authentic learning. To address this, the author proposes a framework centered on human checkpoints, critical reflection on automation, and self-awareness in technology use. Ultimately, the article calls for a shift toward “augmented pedagogy” that enhances rather than automates the learning experience. Without deliberate design to preserve struggle and inquiry, education risks losing its human core in the face of accelerating AI development.

**Решение:** -1 эссе / концептуальная статья
