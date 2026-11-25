# Generation evaluation: baseline

Run 2026-11-25 19:43.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:3b |
| top_k | 4 |
| max_chunk_chars | 1200 |
| max_context_chars | 4000 |
| min_similarity | None |
| relative_cutoff | 0.05 |
| num_ctx | 4096 |
| temperature | 0.1 |
| repeat_penalty | 1.05 |
| max_answer_tokens | 400 |
| keep_alive | 30m |
| min_similarity (effective) | 0.81 |

## Summary (automatic proxies; verdicts are filled by hand in the CSV)

| Measure | Value |
|---|---|
| Questions | 20 |
| Answerable: expected document retrieved (top-k) | 14/15 (93%) |
| Answerable: expected document cited | 14/15 (93%) |
| Answerable: refused (false refusal if the document was retrieved) | 2/15 (13%) |
| No-answer: refused (correct) | 4/5 (80%) |
| Answers with unverified figures/dates | 0/16 (0%) |
| Answers with removed contact details | 1/16 (6%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 15.5 |
| Median total time (s), model answers | 30.5 |
| Median answer speed (tokens/s) | 7.5 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 27.3 | 51.5 |  |
| PRC-02 | en | True | True | False |  | 26.2 | 32.8 |  |
| PRC-09 | en | True | True | False |  | 10.8 | 27.2 |  |
| FIN-01 | en | True | True | True |  | 34.2 | 42.4 |  |
| FIN-05 | en | True | True | False |  | 23.5 | 34.2 |  |
| FIN-06 | en | True | True | False |  | 13.1 | 18.0 |  |
| ERP-02 | en | True | True | False |  | 14.7 | 28.3 |  |
| ERP-03 | en | True | True | False |  | 0.4 | 13.5 |  |
| TTB-03 | en | True | True | False |  | 11.3 | 24.0 |  |
| MHP-01 | en | True | True | False |  | 9.1 | 21.7 |  |
| MHP-02 | en | True | True | False |  | 23.2 | 50.6 |  |
| MHP-03 | en | True | True | False |  | 24.5 | 59.3 |  |
| VAR-01 | fr | True | True | False |  | 16.3 | 53.4 |  |
| VAR-02 | fr | True | True | False |  | 9.2 | 19.8 |  |
| VAR-03 | fr | False | False | True |  |  | 0.2 |  |
| NEG-01 | en |  |  | True |  |  | 0.1 |  |
| NEG-02 | en |  |  | True |  | 0.4 | 5.8 |  |
| NEG-03 | en |  |  | True |  |  | 0.2 |  |
| NEG-04 | en |  |  | False |  | 16.4 | 41.1 |  |
| NEG-05 | en |  |  | True |  |  | 0.2 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: [admissions-how-to-apply].
2. Provide the required documents for your level (see Bachelor and Masters requirements documents for details) and upload the receipt of the application fee if you are applying for a Masters program.
3. For transfer and Top-Up students, submit their documents to the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
4. Have your application checked by the Deans of the faculties to evaluate which credits can be transferred.
5. Finally, follow up with "Check my application" on the ERP login page using the reference number you received.

[admissions-how-to-apply] provides detailed information about the application process and documents required. [web-maters-degree-entry-requirements] gives specific requirements for applying to Masters programs, including the application fee.

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
The course registration deadline is Monday 23 November 2026 [announcements-current-files]. From that date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline [procedures-course-registration].

Sources:
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript, finance-refunds

```
The processing time for a transcript is not specified in the provided sources [procedures-transcript]. The cost of a transcript is also not stated; it is added to My Fees when you request one through the ERP system [procedures-transcript].

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files, admissions-fee

```
[finance-fee-schedule] does not specify the tuition for Bachelor programs. Therefore, I do not have that information and suggest contacting the university directly for accurate details. [admissions-fee] mentions a $50 application fee for Masters programs, but does not provide tuition fees for Bachelor programs.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
  [admissions-fee] Application fee (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files, about-academic-calendar

```
The installment dates and amounts are as follows:

- The first installment is due on 9 November 2026 (50% of the total tuition).
- The second installment is due from 20 to 30 November 2026.
- The third installment amount is XAF 73,000.

[finance-installments] [announcements-current-files]

Sources:
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement, finance-payment-channels

```
[finance-payment-channels] does not document which payment methods the canteen accepts. Please refer to the sources provided for information on payment channels and proof of payment related to tuition fees.

Sources:
  [finance-payment-channels] Payment channels and proof of payment (content/finance/finance-payment-channels.md, verified 2026-11-17)
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration, erp-first-login

```
To log in to the ERP for the first time, follow these steps:

1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

[erp-first-login]

Source: [erp-first-login]

Sources:
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login, erp-first-login

```
If you forgot your ERP password, you can reset it by following these steps:

- [erp-password-reset] Click on the "Forgot password?" option on the login page.
- Type your email or matricule into the provided field.
- The system will send you an email with a secure link to choose a new password.
- Follow the instructions in the email to set a new password.

You should use at least 8 characters mixing letters and numbers. [erp-password-reset]

Sources:
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations, about-academic-regulations

```
The exams are scheduled from Monday, 25 January to Wednesday, 3 February 2027, according to the official communique of 25 October 2026. [timetables-exams-files]

For context, Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 is from 4 to 10 January 2027. [timetables-exams-files]

Sources:
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript

```
You need to pay your outstanding fees before you can get a transcript. Once your fees are settled, follow these steps:

1. Go to the Transcript page of the ERP.
2. Use Download/Print Transcript to get an official stamped transcript.
3. Your fee statement on the ERP will show all your approved results grouped by semester with GPA and CGPA; credits transferred from another university appear at the top.

[erp-fee-statement] [procedures-transcript]

Sources:
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-complaints

```
To resit a failed course, you need to follow these steps:

1. Check if your course is eligible for resit by paying the resit fee. The eligibility criteria are that the total mark of the course must be below 50 [procedures-resits].
2. If your course is eligible, register for the resit in the ERP system. Open Resit Registration and pay the resit fee (the amount is shown in the ERP for each course; it is not stated in the manual) [procedures-resits].
3. For a special resit, you need to request one by clicking Request on Resit Registration and add a note to the Dean. If the Dean agrees, the lecturer will score a fresh mark out of 100, capped at 79 [procedures-resits].

The cost for the resit is not stated in the manual but can be found in the ERP system for each course. [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements, finance-fee-schedule

```
To apply for the Master's program at ICT University, you need to provide the following documents:

- Complete our online application at the ICT University portal-sign-up [web-maters-degree-entry-requirements].
- Certified Scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution. [admissions-masters-requirements]
- Scanned copy of identification documents (birth certificate, National ID card, Passport) [web-maters-degree-entry-requirements]
- Three letters of recommendation [web-maters-degree-entry-requirements]
- Statement of Purpose [web-maters-degree-entry-requirements]
- Certified Scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (Non-refundable Application Fee) [admissions-masters-requirements]

Regarding fees, the complete tuition is XAF 365,000 (Central African francs). However, the programme and level it applies to are not specified in the information collected so far; fees may differ between Bachelor, Masters, and PhD programs. [finance-fee-schedule]

Sources:
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
  [admissions-masters-requirements] Masters admission requirements and documents (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview, erp-course-registration

```
Pour vous inscrire aux cours, vous devez suivre ces étapes :

1. Vérifiez que vous avez payé au moins 50% de la cotisation semestrielle. Sinon, consultez le document d'inscription sur l'ERP pour connaître votre situation [erp-course-registration].
2. Une fois que vous avez payé au moins 50%, téléchargez une reçu de banque démontrant votre paiement et envoyez-le dans votre espace personnel des frais (My Fees) afin que la finance le vérifie.
3. Une fois que votre paiement est validé, vous pouvez vous inscrire aux cours dans l'ERP de l'ICTU. Cliquez sur les cours de votre programme et cliquez sur "Register Selected".
4. Votre coordinateur de programme approuvera votre inscription.
5. Imprimez le formulaire d'inscription officiel.

Veuillez présenter ce formulaire officiel à vos enseignants avant d'assister aux cours, et seuls les étudiants dont les noms figurent sur la liste des cours seront autorisés à y assister [procedures-course-registration].

Sources:
  [erp-course-registration] Registering courses on the ERP (content/erp/erp-course-registration.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
Les frais de scolarité sont de XAF 365,000 [finance-fee-schedule]. Les informations sur les bourses et les réductions sont non documentées à ce jour [finance-scholarships]. Les détails sur la façon de se rendre au campus sont également non documentés [campus-directions].

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
  [finance-scholarships] Scholarships and discounts (content/finance/finance-scholarships.md, verified 2026-11-17)
  [campus-directions] How to reach the university (content/campus/campus-directions.md, verified 2026-11-17)
Remarque : [finance-scholarships] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
Remarque : [campus-directions] est un brouillon non encore vérifié ; confirmez auprès du bureau concerné.
```

### VAR-03 (campus, variant, fr)

> Où se trouve le bureau des finances ?

Expected: campus-office-directory; retrieved: about-contacts, web-faculty-of-bms, web-faculty-of-ict, web-faculty-of-bms

```
Je n'ai pas cette information dans la base de connaissances de l'ICT University. Veuillez contacter directement l'université. Contacts officiels (document about-contacts, en anglais) :
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-01 (about, no-answer, en)

> What is the rector's personal phone number?

Expected: (no answer expected); retrieved: about-contacts, people-org-chart, procedures-complaints, procedures-complaints

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-02 (finance, no-answer, en)

> What is my current fee balance?

Expected: (no answer expected); retrieved: erp-fee-statement, erp-fee-statement, finance-fee-notices, finance-fee-schedule

```
I do not have that information. You can contact the Finance office at [contact removed: not in the sources] to find out your current fee balance. [finance-fee-schedule]

Note: the model wrote a contact detail that is not in the knowledge base; it was removed. Use only the official contacts below or in the cited documents.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-03 (programs, no-answer, en)

> What were last year's exam questions for a given course?

Expected: (no answer expected); retrieved: people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-04 (procedures, no-answer, en)

> Will I pass my resit?

Expected: (no answer expected); retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-resits

```
To determine if you will pass your resit, we need to consider the following points from the sources:

1. The resit is eligible for a course with a total below 50.
2. For a normal resit, the resit score (out of 70) is added to your CA mark. The final total is capped at 79 (grade B+, 3.5 points).

Given these points, if your current cumulative average (CA) plus the resit score is less than or equal to 79, you will pass your resit.

However, without specific details about your current CA and the resit score, we cannot definitively say whether you will pass. You should check your CA and the resit score in the ERP system to determine your final result. [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2, campus-location

```
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

