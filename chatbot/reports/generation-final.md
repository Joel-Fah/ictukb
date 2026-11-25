# Generation evaluation: final

Run 2026-11-25 21:08.

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
| Answers with removed contact details | 1/16 (6%) |
| Answers stopped (loop or length cap) | 0/16 (0%) |
| Model called | 16/20 (80%) |
| Median first token (s), model answers | 10.8 |
| Median total time (s), model answers | 34.8 |
| Median answer speed (tokens/s) | 4.5 |

## Per question

| Id | Lang | Expected retrieved | Expected cited | Refused | Unverified | First token (s) | Total (s) | Verdict |
|---|---|---|---|---|---|---|---|---|
| ADM-01 | en | True | True | False |  | 44.0 | 85.4 |  |
| PRC-02 | en | True | True | False |  | 10.8 | 31.3 |  |
| PRC-09 | en | True | True | False |  | 7.4 | 24.2 |  |
| FIN-01 | en | True | True | True |  | 25.9 | 34.4 |  |
| FIN-05 | en | True | True | False |  | 38.0 | 58.3 |  |
| FIN-06 | en | True | True | False |  | 15.9 | 34.9 |  |
| ERP-02 | en | True | True | False |  | 0.6 | 36.6 |  |
| ERP-03 | en | True | True | False |  | 10.2 | 34.2 |  |
| TTB-03 | en | True | True | False |  | 0.5 | 17.8 |  |
| MHP-01 | en | True | True | False |  | 25.1 | 50.9 |  |
| MHP-02 | en | True | True | False |  | 19.2 | 47.4 |  |
| MHP-03 | en | True | True | False |  | 9.2 | 58.2 |  |
| VAR-01 | fr | True | True | False |  | 10.8 | 58.9 |  |
| VAR-02 | fr | True | True | False |  | 4.8 | 16.7 |  |
| VAR-03 | fr | False | False | True |  |  | 0.2 |  |
| NEG-01 | en |  |  | True |  |  | 0.2 |  |
| NEG-02 | en |  |  | True |  | 22.5 | 30.4 |  |
| NEG-03 | en |  |  | True |  |  | 0.2 |  |
| NEG-04 | en |  |  | False |  | 7.9 | 34.7 |  |
| NEG-05 | en |  |  | True |  |  | 0.2 |  |

## Answers as displayed

### ADM-01 (admissions, procedural, en)

> How do I apply to ICT University?

Expected: admissions-how-to-apply, web-apply-to-ictu; retrieved: admissions-how-to-apply, web-home-2, about-university-overview, web-maters-degree-entry-requirements

```
[retrieval 213 ms, confidence=high, best=0.907, threshold=0.81, language=en]
  0.907  admissions-how-to-apply  [How do I apply to ICT University?]
  0.862  web-home-2  [The ICT University]
  0.855  about-university-overview  [What is ICT University?]
  0.862  web-maters-degree-entry-requirements  [NEW STUDENTS !]
To apply to ICT University, follow these steps:

1. Complete the online application on the student portal: [admissions-how-to-apply].
2. Provide the required documents for your level (see Bachelor and Masters requirements documents for details).
3. For transfer and Top-Up students, contact the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
4. Follow up with "Check my application" on the ERP login page using the reference number you received.
5. Finance will verify the application fee once your application is complete.

[admissions-how-to-apply] provides detailed instructions for applying, including where to find the online application and what documents are required. [web-maters-degree-entry-requirements] gives specific requirements for Masters degree applications, including the application process and documents needed.

Sources:
  [admissions-how-to-apply] How to apply to ICT University (https://ictuniversity.org/bachelors-degree-entry-requirements/, verified 2026-11-18)
  [web-maters-degree-entry-requirements] Master’s Degree Entry Requirements (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-25)
[first token 44.0 s, total 85.4 s, prompt 1018 tok at 23 tok/s, answer 164 tok at 4.0 tok/s]
```

### PRC-02 (procedures, factual, en)

> What is the course registration deadline?

Expected: procedures-course-registration; retrieved: procedures-course-registration, procedures-course-registration, announcements-current-files, announcements-current-files

```
[retrieval 199 ms, confidence=high, best=0.892, threshold=0.81, language=en]
  0.892  procedures-course-registration  [What is the course registration deadline?]
  0.851  procedures-course-registration  [How do I register for courses each semester?]
  0.853  announcements-current-files  [Notice of 13 November 2026: course registration, class lists and the enrolment list] STALE
  0.870  announcements-current-files  [Latest notice: end of course registration (23 November 2026) and second installment] STALE
The course registration deadline is on Monday 23 November 2026 [announcements-current-files]. From that date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline [procedures-course-registration]. Students must present valid, signed and stamped registration forms to their lecturers by 16 November 2026 [announcements-current-files].

Sources:
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
[first token 10.8 s, total 31.3 s, prompt 1191 tok at 114 tok/s, answer 86 tok at 4.2 tok/s]
```

### PRC-09 (procedures, factual, en)

> How long does a transcript take, and what does it cost?

Expected: procedures-transcript; retrieved: procedures-transcript, procedures-transcript, procedures-transcript, finance-refunds

```
[retrieval 269 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  procedures-transcript  [What do I need before I can get a transcript?]
  0.849  procedures-transcript  [How do I request an official stamped transcript?]
  0.825  procedures-transcript  [How do I get my transcript?]
  0.832  finance-refunds  [How is a refund requested and how long does it take?] DRAFT
The time it takes to get a transcript varies depending on the turnaround option chosen when requesting the transcript. The options are standard or express, where offered. [procedures-transcript]

Regarding the cost, it is added to My Fees after you request an official stamped transcript. The cost and processing time are not stated in the ERP manual. [procedures-transcript]

Sources:
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
[first token 7.4 s, total 24.2 s, prompt 670 tok at 96 tok/s, answer 74 tok at 4.4 tok/s]
```

### FIN-01 (finance, factual, en)

> How much are tuition fees for the Bachelors program?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-installments, announcements-current-files, admissions-fee

```
[retrieval 285 ms, confidence=high, best=0.858, threshold=0.81, language=en]
  0.858  finance-fee-schedule  [How much is the tuition?]
  0.817  finance-installments  [Can I pay my fees in installments?]
  0.800  announcements-current-files  [Notice of 9 November 2026: resumption of fees control] STALE
  0.858  admissions-fee  [Is there an application fee and how much is it?]
[finance-fee-schedule] does not specify the tuition for Bachelor programs. Therefore, I do not have that information and suggest contacting the university directly for accurate details.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
[first token 25.9 s, total 34.4 s, prompt 833 tok at 33 tok/s, answer 35 tok at 4.1 tok/s]
```

### FIN-05 (finance, list, en)

> What are the installment dates and amounts?

Expected: finance-installments; retrieved: finance-installments, finance-installments, announcements-current-files, about-academic-calendar

```
[retrieval 209 ms, confidence=high, best=0.862, threshold=0.81, language=en]
  0.862  finance-installments  [What are the installment dates?]
  0.857  finance-installments  [Can I pay my fees in installments?]
  0.837  announcements-current-files  [Latest notice: end of course registration (23 November 2026) and second installment] STALE
  0.823  about-academic-calendar  [Have the registration dates changed?]
The installment dates and amounts are as follows:

- The first installment is due on 9 November 2026 (50% of the total tuition).
- The second installment is due from 20 to 30 November 2026.
- The third installment amount is XAF 73,000.

[finance-installments] [announcements-current-files]

Sources:
  [finance-installments] Paying tuition in installments (content/finance/finance-installments.md, verified 2026-11-18)
  [announcements-current-files] Official notices, November 2026 (content/announcements/announcements-current-files.md, verified 2026-11-17)
Note: [announcements-current-files] was last verified on 2026-11-17 and may be out of date.
[first token 38.0 s, total 58.3 s, prompt 998 tok at 27 tok/s, answer 82 tok at 4.0 tok/s]
```

### FIN-06 (finance, list, en)

> What payment methods are accepted?

Expected: finance-payment-channels; retrieved: canteen-payment, finance-payment-channels, erp-fee-statement, finance-payment-channels

```
[retrieval 204 ms, confidence=high, best=0.835, threshold=0.81, language=en]
  0.835  canteen-payment  [Which payment methods does the canteen accept (cash, mobile money, other)?] DRAFT
  0.791  finance-payment-channels  [How do I submit proof of payment and get a receipt?]
  0.784  erp-fee-statement  [How do I pay and prove my payment?]
  0.790  finance-payment-channels  [Which bank accounts can I pay tuition into?]
The payment methods for tuition at ICT University are accepted through the official bank accounts published in the notice "Changes to the ICT University official bank account details" issued on 10 October 2024. These accounts are not publicly available but can be accessed through the knowledge base database [finance-bank-accounts]. Payments to any other bank accounts are not recognised and will not be accepted. [finance-payment-channels]

Sources:
  [finance-payment-channels] Payment channels and proof of payment (content/finance/finance-payment-channels.md, verified 2026-11-17)
[first token 15.9 s, total 34.9 s, prompt 655 tok at 42 tok/s, answer 86 tok at 4.5 tok/s]
```

### ERP-02 (erp, procedural, en)

> How do I log in to the ERP for the first time?

Expected: erp-first-login; retrieved: erp-first-login, erp-first-login, erp-course-registration, erp-first-login

```
[retrieval 256 ms, confidence=high, best=0.914, threshold=0.81, language=en]
  0.914  erp-first-login  [How do I log in to the ERP for the first time?]
  0.875  erp-first-login  [What is my first password?]
  0.843  erp-course-registration  [How do I register courses on the ERP?]
  0.878  erp-first-login  [I have a matricule but no ERP account. What do I do?]
To log in to the ERP for the first time, follow these steps:

1. Open the ERP address given by the university.
2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
4. Click Sign in. You go straight to your own dashboard.

[erp-first-login] [erp-first-login] [erp-first-login]

Note: If you have a matricule but no ERP account, use Student registration on the login page and enter your matricule along with your details. The account will be pending until the Admission Office approves it. New applicants should use Apply for admission instead.

Sources:
  [erp-first-login] First login to the ERP (content/erp/erp-first-login.md, verified 2026-11-17)
[first token 0.6 s, total 36.6 s, prompt 757 tok at 4047 tok/s, answer 159 tok at 4.4 tok/s]
```

### ERP-03 (erp, procedural, en)

> I forgot my ERP password. What do I do?

Expected: erp-password-reset; retrieved: erp-password-reset, erp-password-reset, erp-first-login, erp-first-login

```
[retrieval 278 ms, confidence=high, best=0.912, threshold=0.81, language=en]
  0.912  erp-password-reset  [How do I reset a forgotten ERP password?]
  0.905  erp-password-reset  [How do I change my password when I am logged in?]
  0.881  erp-first-login  [What is my first password?]
  0.879  erp-first-login  [How do I log in to the ERP for the first time?]
If you forgot your ERP password, you can reset it by following these steps:

- [erp-password-reset] Click on the "Forgot password?" option on the login page.
- Type your email or matricule and the system will send you a secure link to choose a new password via email. The link is only valid for a short time and can be used only once.

You do not need to contact the ERP support contact or the Registrar's office for this process; it is handled internally by the university.

Sources:
  [erp-password-reset] Resetting a forgotten ERP password (content/erp/erp-password-reset.md, verified 2026-11-17)
[first token 10.2 s, total 34.2 s, prompt 833 tok at 85 tok/s, answer 104 tok at 4.3 tok/s]
```

### TTB-03 (timetables, factual, en)

> When are the exams?

Expected: timetables-exams; retrieved: about-academic-regulations, timetables-exams-files, about-academic-regulations, about-academic-regulations

```
[retrieval 158 ms, confidence=high, best=0.859, threshold=0.81, language=en]
  0.809  about-academic-regulations  [What is required to sit end-of-semester examinations?]
  0.859  timetables-exams-files  [When are the exams?]
  0.802  about-academic-regulations  [What are the rules for online students and the Moodle platform?]
  0.794  about-academic-regulations  [Attachment]
The exams are scheduled from Monday, 25 January to Wednesday, 3 February 2027. Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 is from 4 to 10 January 2027.

[timetables-exams-files] [about-academic-regulations]

Sources:
  [timetables-exams-files] Examination and resit timetable (content/timetables/timetables-exams-files.md, verified 2026-11-18)
  [about-academic-regulations] Academic regulations (grading, attendance, exams, conduct) (content/about/about-academic-regulations.md, verified 2026-11-17)
[first token 0.5 s, total 17.8 s, prompt 661 tok at 3407 tok/s, answer 78 tok at 4.5 tok/s]
```

### MHP-01 (finance, multi-hop, en)

> I owe part of my fees and want a transcript. What do I need to do?

Expected: finance-clearance, procedures-transcript; retrieved: procedures-transcript, procedures-transcript, erp-fee-statement, procedures-transcript

```
[retrieval 361 ms, confidence=high, best=0.890, threshold=0.81, language=en]
  0.886  procedures-transcript  [What do I need before I can get a transcript?]
  0.890  procedures-transcript  [How do I request an official stamped transcript?]
  0.840  erp-fee-statement  [How do I view my fee statement on the ERP?]
  0.851  procedures-transcript  [How do I get my transcript?]
You need to pay your outstanding fees before you can get a transcript. Once your fees are settled, follow these steps:

1. Go to the Transcript page on the ERP.
2. Use Download/Print Transcript to get an official stamped transcript.
3. Your fee statement on the ERP will show all your approved results grouped by semester with GPA and CGPA; credits transferred from another university appear at the top.

[erp-fee-statement] [procedures-transcript]

Sources:
  [erp-fee-statement] Viewing the fee statement on the ERP (content/erp/erp-fee-statement.md, verified 2026-11-17)
  [procedures-transcript] Request for an official transcript (content/procedures/procedures-transcript.md, verified 2026-11-17)
[first token 25.1 s, total 50.9 s, prompt 781 tok at 32 tok/s, answer 96 tok at 3.7 tok/s]
```

### MHP-02 (procedures, multi-hop, en)

> I failed a course. How do I resit, and what will it cost?

Expected: procedures-resits, finance-fee-schedule; retrieved: procedures-resits, procedures-resits, procedures-resits, procedures-complaints

```
[retrieval 377 ms, confidence=high, best=0.874, threshold=0.81, language=en]
  0.874  procedures-resits  [How do I register for a resit and what does it cost?]
  0.872  procedures-resits  [What is a special resit?]
  0.865  procedures-resits  [Who is eligible for a resit?]
  0.843  procedures-complaints  [How do I file a complaint about a mark or a grade?]
To resit a failed course, you need to follow these steps:

- First, ensure that the total mark for the course is below 50.
- Then, register for the resit by opening Resit Registration in the ERP.
- The ERP will list your resit courses along with the resit fee and its payment status.
- Pay the resit fee using the payment channels provided in the document.
- Once the fee is paid, your lecturer will enter a fresh mark out of 100 for the course.

[procedures-resits] [procedures-resits] [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
[first token 19.2 s, total 47.4 s, prompt 961 tok at 51 tok/s, answer 126 tok at 4.5 tok/s]
```

### MHP-03 (admissions, multi-hop, en)

> I'm applying for the Masters. What are the requirements and the fees?

Expected: admissions-masters-requirements, finance-fee-schedule; retrieved: admissions-masters-requirements, web-maters-degree-entry-requirements, web-maters-degree-entry-requirements, finance-fee-schedule

```
[retrieval 336 ms, confidence=high, best=0.868, threshold=0.81, language=en]
  0.868  admissions-masters-requirements  [What are the entry requirements for the Masters program?]
  0.834  web-maters-degree-entry-requirements  [NEW STUDENTS !]
  0.831  web-maters-degree-entry-requirements  []
  0.834  finance-fee-schedule  [How much is the tuition?]
To apply for the Master's program at ICT University, you need to provide the following documents:

- Complete online application on the student portal [admissions-masters-requirements].
- Certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript from an accredited institution [admissions-masters-requirements].
- Scanned copy of identification documents (birth certificate, national ID card or passport) [admissions-masters-requirements].
- Three letters of recommendation [admissions-masters-requirements].
- Statement of purpose [admissions-masters-requirements].
- Certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (non-refundable application fee) [admissions-masters-requirements].

Regarding fees, the complete tuition is XAF 365,000 (Central African francs). However, this information is not specified in detail for Bachelor, Masters, and PhD programs. Please refer to the [finance-fee-schedule] for more specific details on fees per program and level.

Sources:
  [admissions-masters-requirements] Masters admission requirements and documents (https://ictuniversity.org/maters-degree-entry-requirements/, verified 2026-11-18)
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 9.2 s, total 58.2 s, prompt 995 tok at 115 tok/s, answer 227 tok at 4.6 tok/s]
```

### VAR-01 (procedures, variant, fr)

> Comment puis-je m'inscrire aux cours ?

Expected: procedures-course-registration; retrieved: procedures-course-registration, finance-scholarships, transport-overview, erp-course-registration

```
[retrieval 295 ms, confidence=high, best=0.832, threshold=0.81, language=fr]
  0.832  procedures-course-registration  [How do I register for courses each semester?]
  0.822  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.822  transport-overview  [How does a student subscribe and who is the contact?] DRAFT
  0.820  erp-course-registration  [What must I have paid before I can register?]
Pour vous inscrire aux cours à ICT University, suivez ces étapes :

1. Vérifiez vos paiements dans l'ERP (Course Registration) : assurez-vous d'avoir payé au moins 50% de la cotisation semestrielle. Si vous n'avez pas encore payé, suivez les instructions pour payer et téléchargez votre reçu bancaire dans My Fees afin que Finance le vérifie.
2. Une fois vos paiements validés, accédez à l'ERP (Course Registration) pour inscrire les cours de votre programme. Cochez les cours correspondants et cliquez sur Register Selected.
3. Votre coordinateur de programme approuvera votre inscription. Après approbation, imprimez le formulaire de validation d'inscription.
4. À partir du 16 novembre 2026, vous devrez présenter un formulaire d'inscription valide, signé et apposé à vos professeurs avant de participer aux cours. Seuls les étudiants inscrits sur la liste des classes seront autorisés à y assister.

[Voir sources : procedures-course-registration, erp-course-registration]

Sources:
  [procedures-course-registration] Course registration (content/procedures/procedures-course-registration.md, verified 2026-11-17)
  [erp-course-registration] Registering courses on the ERP (content/erp/erp-course-registration.md, verified 2026-11-17)
[first token 10.8 s, total 58.9 s, prompt 688 tok at 66 tok/s, answer 251 tok at 5.2 tok/s]
```

### VAR-02 (finance, variant, fr)

> Quels sont les frais de scolarité ?

Expected: finance-fee-schedule; retrieved: finance-fee-schedule, finance-scholarships, finance-scholarships, campus-directions

```
[retrieval 341 ms, confidence=high, best=0.820, threshold=0.81, language=fr]
  0.820  finance-fee-schedule  [How much is the tuition?]
  0.819  finance-scholarships  [How does a student apply and what is the deadline?] DRAFT
  0.815  finance-scholarships  [Which scholarships or discounts exist and who qualifies?] DRAFT
  0.811  campus-directions  [What are the usual fares or travel times?] DRAFT
Les frais de scolarité à ICT University sont de XAF 365,000 [finance-fee-schedule]. Les programmes et niveaux ne sont pas spécifiés dans les informations collectées jusqu'à présent, donc les frais peuvent varier entre les programmes Bachelor, Masters et PhD.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)
[first token 4.8 s, total 16.7 s, prompt 541 tok at 124 tok/s, answer 64 tok at 5.4 tok/s]
```

### VAR-03 (campus, variant, fr)

> Où se trouve le bureau des finances ?

Expected: campus-office-directory; retrieved: about-contacts, web-faculty-of-bms, web-faculty-of-ict, web-faculty-of-bms

```
[retrieval 171 ms, confidence=low, best=0.779, threshold=0.81, language=fr]
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
[retrieval 208 ms, confidence=low, best=0.800, threshold=0.81, language=en]
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
[retrieval 152 ms, confidence=high, best=0.848, threshold=0.81, language=en]
  0.838  erp-fee-statement  [How do I view my fee statement on the ERP?]
  0.833  erp-fee-statement  [How do I pay and prove my payment?]
  0.848  finance-fee-notices  [What fee changes or payment deadlines have been announced recently?] DRAFT STALE
  0.817  finance-fee-schedule  [Where can I find the full fee schedule per program and level?]
I do not have that information. You can contact the Finance office at [contact removed: not in the sources] to find out your current fee balance. [finance-fee-schedule]

Note: the model wrote a contact detail that is not in the knowledge base; it was removed. Use only the official contacts below or in the cited documents.

Sources:
  [finance-fee-schedule] Fee schedule per program and level (content/finance/finance-fee-schedule.md, verified 2026-11-18)

I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
[first token 22.5 s, total 30.4 s, prompt 782 tok at 35 tok/s, answer 37 tok at 4.6 tok/s]
```

### NEG-03 (programs, no-answer, en)

> What were last year's exam questions for a given course?

Expected: (no answer expected); retrieved: people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files, people-course-lecturers-files

```
[retrieval 205 ms, confidence=low, best=0.805, threshold=0.81, language=en]
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
[retrieval 150 ms, confidence=high, best=0.833, threshold=0.81, language=en]
  0.833  procedures-resits  [Who is eligible for a resit?]
  0.828  procedures-resits  [How is a resit graded?]
  0.816  procedures-resits  [How do I register for a resit and what does it cost?]
  0.821  procedures-resits  [What is a special resit?]
To determine if you will pass your resit, we need to consider a few factors based on the information provided:

1. The total mark of your course must be below 50 for it to be eligible for a resit.
2. If the resit is a normal resit, your final total will be capped at 79 (grade B+, 3.5 points).

Therefore, if your initial course total was below 50 and you pass the resit (which scores out of 70), your final total will be capped at 79.

[procedures-resits] [procedures-resits] [procedures-resits]

Sources:
  [procedures-resits] Resit examinations (content/procedures/procedures-resits.md, verified 2026-11-17)
[first token 7.9 s, total 34.7 s, prompt 767 tok at 101 tok/s, answer 136 tok at 5.1 tok/s]
```

### NEG-05 (about, no-answer, en)

> What's the weather in Yaounde today?

Expected: (no answer expected); retrieved: about-contacts, about-contacts, web-home-2, campus-location

```
[retrieval 224 ms, confidence=low, best=0.791, threshold=0.81, language=en]
  0.791  about-contacts  [What is the official postal address of the university?]
  0.777  about-contacts  [What are the general phone number and email address?]
  0.784  web-home-2  [The ICT University > Recent Events > 15th ICT For Africa Conference 2024]
  0.772  campus-location  [Where is the university located?]
I don't have that information in the ICT University knowledge base. Please contact the university directly. Official contacts (from the about-contacts document):
- The website header shows the telephone +237 678 76 40 37 and the email admin@ictuniversity.edu.cm. The ERP footer shows the Faculty of Information and Communication Technology, ICT University Yaounde, telephone +237 682 255 000.
```

