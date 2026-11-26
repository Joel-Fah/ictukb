# Generation evaluation: qwen7b

Run 2026-11-26 05:16.

## Settings

| Setting | Value |
|---|---|
| ollama_url | http://127.0.0.1:11434 |
| model | qwen2.5:7b |
| top_k | 4 |
| max_chunk_chars | 1200 |
| max_context_chars | 4000 |
| min_similarity | None |
| relative_cutoff | 0.05 |
| num_ctx | 4096 |
| temperature | 0.1 |
| repeat_penalty | 1.05 |
| max_answer_tokens | 400 |
| seed | 42 |
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
| Answers with removed contact details | 0/16 (0%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 36.1 |
| Median total time (s), model answers | 62.3 |
| Median answer speed (tokens/s) | 3.3 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 85.8 | 130.6 |  |
| PRC-02 | en | True | True | False |  | 70.1 | 78.0 |  |
| PRC-09 | en | True | True | False |  | 26.4 | 38.6 |  |
| FIN-01 | en | True | True | False |  | 39.9 | 56.1 |  |
| FIN-05 | en | True | True | True |  | 53.8 | 99.1 |  |
| FIN-06 | en | True | True | False |  | 25.2 | 44.3 |  |
| ERP-02 | en | True | True | False |  | 33.7 | 62.8 |  |
| ERP-03 | en | True | True | False |  | 39.8 | 61.9 |  |
| TTB-03 | en | True | True | False |  | 25.9 | 50.6 |  |
| MHP-01 | en | True | True | False |  | 35.9 | 71.6 |  |
| MHP-02 | en | True | True | False |  | 51.4 | 79.8 |  |
| MHP-03 | en | True | True | False |  | 54.2 | 110.0 |  |
| VAR-01 | fr | True | True | False |  | 28.0 | 75.1 |  |
| VAR-02 | fr | True | True | False |  | 8.2 | 28.4 |  |
| VAR-03 | fr | False | False | True |  |  | 0.2 |  |
| NEG-01 | en |  |  | True |  |  | 0.2 |  |
| NEG-02 | en |  |  | False |  | 36.3 | 56.4 |  |
| NEG-03 | en |  |  | True |  |  | 0.2 |  |
| NEG-04 | en |  |  | True |  | 34.5 | 60.0 |  |
| NEG-05 | en |  |  | True |  |  | 0.1 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
[retrieval 304 ms, confidence=high, best=0.907, threshold=0.81, language=en]
  0.907  admissions-how-to-apply  [How do I apply to ICT University?]
  0.862  web-home-2  [The ICT University]
  0.855  about-university-overview  [What is ICT University?]
  0.862  web-maters-degree-entry-requirements  [NEW STUDENTS !]
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: https://studentportal.ictuniversity.edu.cm/portal-sign-up/ [admissions-how-to-apply]
2. Provide the required documents for your level.
3. For transfer and Top-Up students, submit your documents to the Department of Transcript and Verification (transcript.verification@ictuniversity.edu.cm) [admissions-how-to-apply].
4. Follow up with "Check my application" on the ERP login page using the reference number you received [admissions-how-to-apply].
5. The admission letter is sent once Finance has verified the application fee [admissions-how-to-apply].

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
[first token 85.8 s, total 130.6 s, prompt 1018 tok at 12 tok/s, answer 145 tok at 3.2 tok/s]
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
[retrieval 145 ms, confidence=high, best=0.892, threshold=0.81, language=en]
  0.892  procedures-course-registration  [What is the course registration deadline?]
  0.851  procedures-course-registration  [How do I register for courses each semester?]
  0.853  announcements-current-files  [Notice of 13 November 2026: course registration, class lists and the enrolment list] STALE
  0.870  announcements-current-files  [Latest notice: end of course registration (23 November 2026) and second installment] STALE
The course registration deadline is Monday 23 November 2026 [procedures-course-registration, announcements-current-files].

Sources:
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
[first token 70.1 s, total 78.0 s, prompt 1191 tok at 17 tok/s, answer 26 tok at 3.3 tok/s]
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript, finance-refunds

```
[retrieval 189 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  procedures-transcript  [What do I need before I can get a transcript?]
  0.849  procedures-transcript  [How do I request an official stamped transcript?]
  0.825  procedures-transcript  [How do I get my transcript?]
  0.832  finance-refunds  [How is a refund requested and how long does it take?] DRAFT
The processing time for a transcript is not stated in the ERP manual [procedures-transcript]. The cost, if any, is added to My Fees after you submit your request [procedures-transcript].

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
[first token 26.4 s, total 38.6 s, prompt 670 tok at 26 tok/s, answer 42 tok at 3.4 tok/s]
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files, admissions-fee

```
[retrieval 177 ms, confidence=high, best=0.858, threshold=0.81, language=en]
  0.858  finance-fee-schedule  [How much is the tuition?]
  0.817  finance-installments  [Can I pay my fees in installments?]
  0.800  announcements-current-files  [Notice of 9 November 2026: resumption of fees control] STALE
  0.858  admissions-fee  [Is there an application fee and how much is it?]
The complete tuition is XAF 365,000 (Central African francs) [finance-fee-schedule]. However, the specific amount for the Bachelor's program is not specified in the information collected so far [finance-fee-schedule].

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 39.9 s, total 56.1 s, prompt 833 tok at 21 tok/s, answer 54 tok at 3.3 tok/s]
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files, about-academic-calendar

```
[retrieval 138 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  finance-installments  [What are the installment dates?]
  0.857  finance-installments  [Can I pay my fees in installments?]
  0.837  announcements-current-files  [Latest notice: end of course registration (23 November 2026) and second installment] STALE
  0.823  about-academic-calendar  [Have the registration dates changed?]
Tuition is paid in three installments with the following amounts:
1. First installment: 50% of the total tuition, which is XAF 182,500.
2. Second installment: 30% of the total tuition, which is XAF 109,500.
3. Third installment: 20% of the total tuition, which is XAF 73,000.

The second installment payment period is from 20 to 30 November 2026 [finance-installments, announcements-current-files, about-academic-calendar]. The specific dates for the first and third installments are not provided in the sources.

Sources:
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [about-academic-calendar] Academic calendar for the current year (content/about/about-academic-calendar.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
[first token 53.8 s, total 99.1 s, prompt 998 tok at 19 tok/s, answer 145 tok at 3.2 tok/s]
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement, finance-payment-channels

```
[retrieval 175 ms, confidence=high, best=0.835, threshold=0.81, language=en]
  0.835  canteen-payment  [Which payment methods does the canteen accept (cash, mobile money, other)?] DRAFT
  0.791  finance-payment-channels  [How do I submit proof of payment and get a receipt?]
  0.784  erp-fee-statement  [How do I pay and prove my payment?]
  0.790  finance-payment-channels  [Which bank accounts can I pay tuition into?]
The payment method accepted is through the bank, specifically into the official bank accounts of The ICT University as published by the Secretary General in the notice "Changes to the ICT University official bank account details" (10 October 2024). Payments to other accounts are not recognised. [finance-payment-channels]

Sources:
  [finance-payment-channels] Payment channels and proof of payment (content/finance/finance-payment-channels.md, verified 2026-11-17)
[first token 25.2 s, total 44.3 s, prompt 655 tok at 26 tok/s, answer 64 tok at 3.4 tok/s]
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration, erp-first-login

```
[retrieval 188 ms, confidence=high, best=0.914, threshold=0.81, language=en]
  0.914  erp-first-login  [How do I log in to the ERP for the first time?]
  0.875  erp-first-login  [What is my first password?]
  0.843  erp-course-registration  [How do I register courses on the ERP?]
  0.878  erp-first-login  [I have a matricule but no ERP account. What do I do?]
To log in to the ERP for the first time, follow these steps:

1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

[erp-first-login]

Sources:
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
[first token 33.7 s, total 62.8 s, prompt 757 tok at 23 tok/s, answer 96 tok at 3.3 tok/s]
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login, erp-first-login

```
[retrieval 155 ms, confidence=high, best=0.912, threshold=0.81, language=en]
  0.912  erp-password-reset  [How do I reset a forgotten ERP password?]
  0.905  erp-password-reset  [How do I change my password when I am logged in?]
  0.881  erp-first-login  [What is my first password?]
  0.879  erp-first-login  [How do I log in to the ERP for the first time?]
To reset a forgotten ERP password, follow these steps:

1. Go to the login page.
2. Click on "Forgot password?".
3. Enter your email or matricule.
4. The system will send you a secure link via email to choose a new password. This link expires after a short time and works only once [erp-password-reset].

Sources:
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
[first token 39.8 s, total 61.9 s, prompt 833 tok at 21 tok/s, answer 73 tok at 3.3 tok/s]
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations, about-academic-regulations

```
[retrieval 457 ms, confidence=high, best=0.859, threshold=0.81, language=en]
  0.809  about-academic-regulations  [What is required to sit end-of-semester examinations?]
  0.859  timetables-exams-files  [When are the exams?]
  0.802  about-academic-regulations  [What are the rules for online students and the Moodle platform?]
  0.794  about-academic-regulations  [Attachment]
The exams for the first semester 2026/2027 are scheduled from Monday 25 January to Wednesday 3 February 2027. Continuous Assessment 1 is from 14 to 19 December 2026, and Continuous Assessment 2 from 4 to 10 January 2027. [timetables-exams-files]

Sources:
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
[first token 25.9 s, total 50.6 s, prompt 661 tok at 26 tok/s, answer 83 tok at 3.4 tok/s]
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript

```
[retrieval 183 ms, confidence=high, best=0.890, threshold=0.81, language=en]
  0.886  procedures-transcript  [What do I need before I can get a transcript?]
  0.890  procedures-transcript  [How do I request an official stamped transcript?]
  0.840  erp-fee-statement  [How do I view my fee statement on the ERP?]
  0.851  procedures-transcript  [How do I get my transcript?]
You need to settle your outstanding fees before requesting a transcript. Once your fees are settled, you can request an official stamped transcript through the ERP system by following these steps:

1. Under Requests and Services, choose either a partial or full official transcript.
2. Select the turnaround time (standard or express, if offered).
3. State the purpose of the request.
4. Submit the request.

The fee for the transcript, if any, will be added to your My Fees page. You can track the status and reference number on the same page. [procedures-transcript]

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
[first token 35.9 s, total 71.6 s, prompt 781 tok at 22 tok/s, answer 117 tok at 3.3 tok/s]
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-complaints

```
[retrieval 239 ms, confidence=high, best=0.874, threshold=0.81, language=en]
  0.874  procedures-resits  [How do I register for a resit and what does it cost?]
  0.872  procedures-resits  [What is a special resit?]
  0.865  procedures-resits  [Who is eligible for a resit?]
  0.843  procedures-complaints  [How do I file a complaint about a mark or a grade?]
To resit a course that you have failed:

1. Open Resit Registration in the ERP.
2. Pay the resit fee for each course, which amount is shown in the ERP for each course [procedures-resits].
3. Once the fee is paid, your lecturer will enter the resit score.

The cost of the resit fee is not explicitly stated but can be found in the ERP for each course [procedures-resits].

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
[first token 51.4 s, total 79.8 s, prompt 961 tok at 19 tok/s, answer 92 tok at 3.2 tok/s]
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements, finance-fee-schedule

```
[retrieval 198 ms, confidence=high, best=0.868, threshold=0.81, language=en]
  0.868  admissions-masters-requirements  [What are the entry requirements for the Masters program?]
  0.834  web-maters-degree-entry-requirements  [NEW STUDENTS !]
  0.831  web-maters-degree-entry-requirements  []
  0.834  finance-fee-schedule  [How much is the tuition?]
To apply for a Master's degree at ICT University, you need to provide the following:

1. The online application on the student portal (https://studentportal.ictuniversity.edu.cm/portal-sign-up/).
2. A certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
3. A scanned copy of identification documents (birth certificate, national ID card or passport).
4. Three letters of recommendation.
5. A statement of purpose.
6. A certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA, which is a non-refundable application fee.

The complete tuition is XAF 365,000 (Central African francs). [finance-fee-schedule]

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 54.2 s, total 110.0 s, prompt 995 tok at 18 tok/s, answer 178 tok at 3.2 tok/s]
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview, erp-course-registration

```
[retrieval 158 ms, confidence=high, best=0.832, threshold=0.81, language=fr]
  0.832  procedures-course-registration  [How do I register for courses each semester?]
  0.822  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.822  transport-overview  [How does a student subscribe and who is the contact?] DRAFT
  0.820  erp-course-registration  [What must I have paid before I can register?]
Pour vous inscrire aux cours, procédez comme suit :

1. Connectez-vous à l'ICTU ERP (Course Registration).
2. Cochez les cours de votre programme.
3. Cliquez sur "Register Selected".
4. Obtenez l'approbation de votre Coordinateur de programme.
5. Imprimez le formulaire de registration des cours officiel.

N'oubliez pas que depuis le 16 novembre 2026, vous devez présenter un formulaire de registration des cours valide, signé et tamponné à vos professeurs avant d'assister aux cours. Seuls les noms figurant sur la liste officielle des classes peuvent y assister.

[procedures-course-registration]

Sources:
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
[first token 28.0 s, total 75.1 s, prompt 688 tok at 25 tok/s, answer 155 tok at 3.3 tok/s]
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
[retrieval 207 ms, confidence=high, best=0.820, threshold=0.81, language=fr]
  0.820  finance-fee-schedule  [How much is the tuition?]
  0.819  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.815  finance-scholarships  [Which scholarships or discounts exist and who qualifies?] DRAFT
  0.811  campus-directions  [What are the usual fares or travel times?] DRAFT
Les frais de scolarité pour ICT University s'établissent à XAF 365,000 (francs centrafricains) [finance-fee-schedule]. Cependant, il n'est pas spécifié si cette somme concerne un bachelor, un master ou un doctorat.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 8.2 s, total 28.4 s, prompt 541 tok at 69 tok/s, answer 68 tok at 3.4 tok/s]
```

### VAR-03 (campus, variant, fr)

> Où se trouve le bureau des finances ?

Expected: campus-office-directory; retrieved: about-contacts, web-faculty-of-bms, web-faculty-of-ict, web-faculty-of-bms

```
[retrieval 154 ms, confidence=low, best=0.779, threshold=0.81, language=fr]
  0.779  about-contacts  [What is the official postal address of the university?]
  0.771  web-faculty-of-bms  [Mission Statement > Various BMS Programs > Banking and Finance]
  0.768  web-faculty-of-ict  []
  0.768  web-faculty-of-bms  []
Je n'ai pas cette information dans la base de connaissances de l'ICT University. Veuillez contacter directement l'université. Contacts officiels (document about-contacts, en anglais) :
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-01 (about, no-answer, en)

> What is the rector's personal phone number?

Expected: (no answer expected); retrieved: about-contacts, people-org-chart, procedures-complaints, procedures-complaints

```
[retrieval 199 ms, confidence=low, best=0.800, threshold=0.81, language=en]
  0.800  about-contacts  [What are the general phone number and email address?]
  0.773  people-org-chart  [How is the university organised (rector, deans, registrar, heads of department)?] DRAFT
  0.756  procedures-complaints  []
  0.751  procedures-complaints  []
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-02 (finance, no-answer, en)

> What is my current fee balance?

Expected: (no answer expected); retrieved: erp-fee-statement, erp-fee-statement, finance-fee-notices, finance-fee-schedule

```
[retrieval 183 ms, confidence=high, best=0.848, threshold=0.81, language=en]
  0.838  erp-fee-statement  [How do I view my fee statement on the ERP?]
  0.833  erp-fee-statement  [How do I pay and prove my payment?]
  0.848  finance-fee-notices  [What fee changes or payment deadlines have been announced recently?] DRAFT STALE
  0.817  finance-fee-schedule  [Where can I find the full fee schedule per program and level?]
Your current fee balance can be found on the ERP system under "My Fees." It includes tuition, resit fees, senior project fees, other fees (application, student union, infirmary, graduation, bus, additional course, late registration, transcript), fines, and your wallet balance [erp-fee-statement].

Sources:
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
[first token 36.3 s, total 56.4 s, prompt 782 tok at 22 tok/s, answer 66 tok at 3.3 tok/s]
```

### NEG-03 (programs, no-answer, en)

> What were last year's exam questions for a given course?

Expected: (no answer expected); retrieved: people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files

```
[retrieval 159 ms, confidence=low, best=0.805, threshold=0.81, language=en]
  0.803  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
  0.805  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
  0.802  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
  0.799  people-course-lecturers-files  [Which lecturer teaches a given course in Fall 2026?]
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

### NEG-04 (procedures, no-answer, en)

> Will I pass my resit?

Expected: (no answer expected); retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-resits

```
[retrieval 137 ms, confidence=high, best=0.833, threshold=0.81, language=en]
  0.833  procedures-resits  [Who is eligible for a resit?]
  0.828  procedures-resits  [How is a resit graded?]
  0.816  procedures-resits  [How do I register for a resit and what does it cost?]
  0.821  procedures-resits  [What is a special resit?]
I do not have that information [procedures-resits]. The outcome depends on your performance during the resit examination, which is scored out of 70 and added to your continuous assessment (CA) mark, with a final total capped at 79 (grade B+, 3.5 points). For courses failed in an earlier semester, you may request a special resit with the Dean's approval.

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
[first token 34.5 s, total 60.0 s, prompt 767 tok at 22 tok/s, answer 84 tok at 3.3 tok/s]
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2, campus-location

```
[retrieval 132 ms, confidence=low, best=0.791, threshold=0.81, language=en]
  0.791  about-contacts  [What is the official postal address of the university?]
  0.777  about-contacts  [What are the general phone number and email address?]
  0.784  web-home-2  [The ICT University > Recent Events > 15th ICT For Africa Conference 2024]
  0.772  campus-location  [Where is the university located?]
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

