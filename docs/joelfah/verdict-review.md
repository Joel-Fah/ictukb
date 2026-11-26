# Verdict review

**Reviewed by Joel on 2026-11-26: all 36 verdicts confirmed as they stand** ("all good", given for the whole sheet). Recorded in the CSVs as "confirmed by Joel 2026-11-26".

Confirm or change Claude's verdict on each model answer. These verdicts are the basis of every quality number in [models.md](models.md) and [BENCHMARKS](../../chatbot/BENCHMARKS.md).

**How:** read each question's sources, then both answers. On each `Your verdict:` line write **ok** if you agree, or your verdict (*correct*, *partial*, *wrong*, *refused*) and a few words why. Tip: open the preview (Ctrl+Shift+V) next to this file to read, and edit here.

**Verdict scale:** *correct* = every fact matches the sources; *partial* = facts right but incomplete, a condition dropped, or a minor unsupported detail; *wrong* = a wrong or invented fact, or another topic; *refused* = says it doesn't know. For the no-answer questions (NEG-), a refusal is the right outcome.

---

## The 20 evaluation questions

### ADM-01: How do I apply to ICT University?

*admissions, procedural, en* · expected documents: admissions-how-to-apply web-apply-to-ictu

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**admissions-how-to-apply** › How do I apply to ICT University? · similarity 0.907

> 1. Complete the online application on the student portal: https://studentportal.ictuniversity.edu.cm/portal-sign-up/ (the "Apply now" buttons of the website lead there; the ERP login page also offers "Apply for admission", a bilingual public form).
> 2. Provide the documents required for your level (see the Bachelor and Masters requirements documents). Masters applicants also upload the receipt of the application fee.
> 3. For transfer and Top-Up students, the documents go to the Department of Transcript and Verification (transcript.verification@ictuniversity.edu.cm), which checks their authenticity; the Deans of the faculties evaluate which credits can be transferred; the Admissions Office (admissions@ictuniversity.edu.cm) then admits the student into the program.
> 4. Follow your application with "Check my application" on the ERP login page, using the reference number you received.
> 5. The admission letter is sent once Finance has verified the application fee.

**web-home-2** › The ICT University · similarity 0.862

> The ICT University operates a purely US-based curriculum to provide quality ICT and Managerial Human Capacity Development specially targeted for Africa, Latin America, the Caribbean and Asia. The ICT University is a vibrant institution which aims at imposing itself as premier destination for research, innovation and training of scholars relevant for the context of developing economies.
>
> The ICT University is accredited to run some Bachelors, Masters and IMBA degree programs in accordance with the general Framework Agreement signed between the University of Buea (UB) and The ICT University (ICT-U) on the 14th March 2023.
>
> [Admission](https://ictuniversity.org/apply-to-ictu/)

**about-university-overview** › What is ICT University? · similarity 0.855

> The ICT University (ICT-U) describes itself on its website as "Impacting ICTs in all Academic Disciplines". It operates in Yaounde, Cameroon, with an administrative office in the United States (The ICT University Foundation, Baton Rouge, Louisiana). It has two faculties: the Faculty of Information and Communication Technology and the Faculty of Business Management and Sustainability, and offers Bachelor's, Master's and International MBA programs.

**web-maters-degree-entry-requirements** › NEW STUDENTS ! · similarity 0.862

> To complete your application for a Masters degree program at the ICT University, both in Information Communication and Technology (ICT) and in Business Management and Sustainability (BMS), please ensure you provide the following documents:
>
> 1. Complete our online application at the ICT Universty  [portal-sign-up](https://studentportal.ictuniversity.edu.cm/portal-sign-up/)
> 2. Certified Scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
> 3. Scanned copy of identification documents (birth certificate, National ID card, Passport)
> 4. Three letters or recommendations
> 5. Statement of Purpose
> 6. Certified Scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (Non-refundable Application Fee).
>
> [SEE OUR MASTERS PROGRAMS](https://ictuniversity.org/masters-programs/)
>
> [APPLY NOW](https://studentportal.ictuniversity.edu.cm/portal-sign-up/)

</details>

**3B answer** (cited: admissions-how-to-apply web-maters-degree-entry-requirements)

> To apply to ICT University, follow these steps:
>
> 1. Complete the online application on the student portal: [admissions-how-to-apply].
> 2. Provide the required documents for your level (see Bachelor and Masters requirements documents for details).
> 3. For transfer and Top-Up students, contact the Department of Transcript and Verification at transcript.verification@ictuniversity.edu.cm.
> 4. Follow up with "Check my application" on the ERP login page using the reference number you received.
> 5. Finance will verify the application fee once your application is complete.
>
> [admissions-how-to-apply] provides detailed instructions for applying, including where to find the online application and what documents are required. [web-maters-degree-entry-requirements] gives specific requirements for Masters degree applications, including the application process and documents needed.

Claude: **correct**: Steps sourced; Deans step omitted (not wrong)

Your verdict (3B ADM-01): ok

**7B answer** (cited: admissions-how-to-apply)

> To apply to ICT University, follow these steps:
>
> 1. Complete the online application on the student portal: https://studentportal.ictuniversity.edu.cm/portal-sign-up/ [admissions-how-to-apply]
> 2. Provide the required documents for your level.
> 3. For transfer and Top-Up students, submit your documents to the Department of Transcript and Verification (transcript.verification@ictuniversity.edu.cm) [admissions-how-to-apply].
> 4. Follow up with "Check my application" on the ERP login page using the reference number you received [admissions-how-to-apply].
> 5. The admission letter is sent once Finance has verified the application fee [admissions-how-to-apply].

Claude: **correct**: All five steps from the source; the transfer/Top-Up step keeps its condition (the 3B once presented it as for everyone, failure 19)

Your verdict (7B ADM-01): ok

### PRC-02: What is the course registration deadline?

*procedures, factual, en* · expected documents: procedures-course-registration

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-course-registration** › What is the course registration deadline? · similarity 0.892

> Course registration closes on Monday 23 November 2026 (latest notice of the Office of the Bursar, Finance Department). From that date a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline. Earlier notices gave other dates: the communique of 25 October 2026 set 6 November 2026, and the notice of 13 November 2026 asked all students to complete registration online and physically by Thursday 19 November 2026 so that they could be included in the enrolment list sent to the University of Buea on 30 November 2026. The Finance notice of 23 November is the most recent and is the one to follow.

**procedures-course-registration** › How do I register for courses each semester? · similarity 0.851

> Registration is done in the ICTU ERP (Course Registration): tick the courses of your programme and click Register Selected, then your programme Coordinator approves the registration, and you print the official Course Registration Form. Since 16 November 2026 students must present a valid, signed and stamped registration form to their lecturers before attending lectures, and only students whose names are on the official class list may attend. The detailed ERP steps are in the ERP course registration document.

**announcements-current-files** › Notice of 13 November 2026: course registration, class lists and the enrolment list · similarity 0.853 · STALE

> Reference 01/13/11/2026/ICED/avni, signed by Professor Alain Vilard Ndi Isoh, Deputy Vice-Chancellor in charge of Internal Control and Evaluation. Subject: submission of the 2026/2027 student enrolment list to the University of Buea. In preparation for the Admission Board Meeting of Monday 30 November 2026, all new and returning students must:
>
> 1. Complete all outstanding admission requirements, where applicable (new students with incomplete files).
> 2. Complete course registration both online and physically no later than Thursday 19 November 2026 (new and returning students).
>
> Effective Monday 16 November 2026: all students must present valid course registration forms to their lecturers before taking lectures; no student may attend lectures without their name on the official class list; the penalty for late course registration is effective from Monday 23 November 2026. Only duly admitted and registered students are included in the official enrolment list submitted to the University of Buea on Monday 30 November 2026.

**announcements-current-files** › Latest notice: end of course registration (23 November 2026) and second installment · similarity 0.870 · STALE

> Issued by the Office of the Bursar, Finance Department. Course registration closes on Monday 23 November 2026. From that date a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline. The payment period for the second installment of fees is 20 to 30 November 2026.

</details>

**3B answer** (cited: announcements-current-files procedures-course-registration)

> The course registration deadline is on Monday 23 November 2026 [announcements-current-files]. From that date, a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline [procedures-course-registration]. Students must present valid, signed and stamped registration forms to their lecturers by 16 November 2026 [announcements-current-files].

Claude: **correct**: 23 Nov + 10,000 FCFA; 'by 16 November' slightly distorts 'since 16 November'

Your verdict (3B PRC-02): ok

**7B answer** (cited: procedures-course-registration announcements-current-files)

> The course registration deadline is Monday 23 November 2026 [procedures-course-registration, announcements-current-files].

Claude: **correct**: 23 November 2026, the latest notice

Your verdict (7B PRC-02): ok

### PRC-09: How long does a transcript take, and what does it cost?

*procedures, factual, en* · expected documents: procedures-transcript

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-transcript** › What do I need before I can get a transcript? · similarity 0.862

> The transcript is not available while you have outstanding fees. The cost and the processing time are not stated in the ERP manual.

**procedures-transcript** › How do I request an official stamped transcript? · similarity 0.849

> Under Requests and Services choose a partial or full official transcript, choose the turnaround (standard or express, where offered), state the purpose and submit. The fee, if any, is added to My Fees. The Registrar's Office processes the request and you can follow its status and reference number on the page.

**procedures-transcript** › How do I get my transcript? · similarity 0.825

> The Transcript page of the ERP shows all your approved results grouped by semester with the semester GPA and your CGPA; credits transferred from another university appear at the top. Use Download/Print Transcript for the official layout.

**finance-refunds** › How is a refund requested and how long does it take? · similarity 0.832 · DRAFT

> [[TO FILL]]

</details>

**3B answer** (cited: procedures-transcript)

> The time it takes to get a transcript varies depending on the turnaround option chosen when requesting the transcript. The options are standard or express, where offered. [procedures-transcript]
>
> Regarding the cost, it is added to My Fees after you request an official stamped transcript. The cost and processing time are not stated in the ERP manual. [procedures-transcript]

Claude: **partial**: Says time and cost are not stated (right) but first infers 'time varies with the turnaround option' (not in the source)

Your verdict (3B PRC-09): ok

**7B answer** (cited: procedures-transcript)

> The processing time for a transcript is not stated in the ERP manual [procedures-transcript]. The cost, if any, is added to My Fees after you submit your request [procedures-transcript].

Claude: **correct**: Says processing time is not stated (verbatim) and the fee, if any, is added to My Fees; nothing inferred

Your verdict (7B PRC-09): ok

### FIN-01: How much are tuition fees for the Bachelors program?

*finance, factual, en* · expected documents: finance-fee-schedule

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**finance-fee-schedule** › How much is the tuition? · similarity 0.858

> The complete tuition is XAF 365,000 (Central African francs). The programme and level it applies to are not specified in the information collected so far; fees may differ between Bachelor, Masters and PhD programs.

**finance-installments** › Can I pay my fees in installments? · similarity 0.817

> Yes. Tuition is paid in three installments: the first installment is 50% of the tuition, the second 30% and the third 20%. With a complete tuition of XAF 365,000 this is XAF 182,500, then XAF 109,500, then XAF 73,000.
>
> The Finance Department (Office of the Bursar) notices confirm that the first installment is 50% of the total tuition and must be settled to have access to the campus and the student portal (fees control resumed on Monday 9 November 2026), and that the payment period for the second installment is 20 to 30 November 2026.

**announcements-current-files** › Notice of 9 November 2026: resumption of fees control · similarity 0.800 · STALE

> The fees control, temporarily halted from 2 November 2026, takes effect again on Monday 9 November 2026. Students must settle the first tuition installment, which is 50% of the total tuition, to have access to the campus and the student portal. The control applies to both tuition fees and semester registration. Issued by the Office of the Bursar, Finance Department.

**admissions-fee** › Is there an application fee and how much is it? · similarity 0.858

> For Masters programs the application fee is $50 or 25,000 CFA and is non-refundable. It is paid into the ICT-U bank account and a certified scanned copy of the receipt is submitted with the application. The amount of the Bachelor application fee is not stated on the website. In the ERP the admission letter is sent once Finance has verified the application fee.

</details>

**3B answer** (cited: finance-fee-schedule)

> [finance-fee-schedule] does not specify the tuition for Bachelor programs. Therefore, I do not have that information and suggest contacting the university directly for accurate details.

Claude: **refused**: False refusal: 365,000 with the 'level not specified' caveat was available

Your verdict (3B FIN-01): ok

**7B answer** (cited: finance-fee-schedule)

> The complete tuition is XAF 365,000 (Central African francs) [finance-fee-schedule]. However, the specific amount for the Bachelor's program is not specified in the information collected so far [finance-fee-schedule].

Claude: **correct**: 365,000 with the "level not specified" caveat: the answer the 3B missed in all four runs

Your verdict (7B FIN-01): ok

### FIN-05: What are the installment dates and amounts?

*finance, list, en* · expected documents: finance-installments

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**finance-installments** › What are the installment dates? · similarity 0.862

> Only the second installment window is known: 20 to 30 November 2026. The dates of the other installments have not been published in the notices collected so far. For other deadlines, ask the Admissions office or the Finance office.

**finance-installments** › Can I pay my fees in installments? · similarity 0.857

> Yes. Tuition is paid in three installments: the first installment is 50% of the tuition, the second 30% and the third 20%. With a complete tuition of XAF 365,000 this is XAF 182,500, then XAF 109,500, then XAF 73,000.
>
> The Finance Department (Office of the Bursar) notices confirm that the first installment is 50% of the total tuition and must be settled to have access to the campus and the student portal (fees control resumed on Monday 9 November 2026), and that the payment period for the second installment is 20 to 30 November 2026.

**announcements-current-files** › Latest notice: end of course registration (23 November 2026) and second installment · similarity 0.837 · STALE

> Issued by the Office of the Bursar, Finance Department. Course registration closes on Monday 23 November 2026. From that date a penalty of 10,000 FCFA applies to any student who registers for courses after the deadline. The payment period for the second installment of fees is 20 to 30 November 2026.

**about-academic-calendar** › Have the registration dates changed? · similarity 0.823

> Yes. The most recent notice of the Office of the Bursar (Finance Department) states that course registration closes on Monday 23 November 2026, with a penalty of 10,000 FCFA for registration after that date, and that the second installment of fees is payable from 20 to 30 November 2026. This replaces the 6 November end date in the communique of 25 October 2026.

</details>

**3B answer** (cited: finance-installments announcements-current-files)

> The installment dates and amounts are as follows:
>
> - The first installment is due on 9 November 2026 (50% of the total tuition).
> - The second installment is due from 20 to 30 November 2026.
> - The third installment amount is XAF 73,000.
>
> [finance-installments] [announcements-current-files]

Claude: **partial**: 'due on 9 November' distorts the fees-control date; first/second amounts missing

Your verdict (3B FIN-05): ok

**7B answer** (cited: finance-installments announcements-current-files about-academic-calendar)

> Tuition is paid in three installments with the following amounts:
> 1. First installment: 50% of the total tuition, which is XAF 182,500.
> 2. Second installment: 30% of the total tuition, which is XAF 109,500.
> 3. Third installment: 20% of the total tuition, which is XAF 73,000.
>
> The second installment payment period is from 20 to 30 November 2026 [finance-installments, announcements-current-files, about-academic-calendar]. The specific dates for the first and third installments are not provided in the sources.

Claude: **correct**: All three amounts, the 20-30 Nov window, and that other dates are unpublished. PIPELINE: "not provided in" matched the refusal list, so the contacts fallback was appended and the run counted it as refused (failure 36)

Your verdict (7B FIN-05): ok

### FIN-06: What payment methods are accepted?

*finance, list, en* · expected documents: finance-payment-channels

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**canteen-payment** › Which payment methods does the canteen accept (cash, mobile money, other)? · similarity 0.835 · DRAFT

> [[TO FILL]]

**finance-payment-channels** › How do I submit proof of payment and get a receipt? · similarity 0.791

> After paying at the bank, open My Fees in the ICTU ERP, upload the receipt (image or PDF) with the bank name and transaction reference, and tick every fee the payment covers with the amount for each. Finance checks the receipt and approves or rejects it; your balance changes only after approval, and you follow the status on the same page. A surplus can be put in the wallet.

**erp-fee-statement** › How do I pay and prove my payment? · similarity 0.784

> 1. Pay at the bank as instructed by the Finance office (official accounts are in the payment channels document).
> 2. In My Fees click to upload the receipt: enter the bank name and the transaction reference, attach the receipt (image or PDF), and tick every fee this one payment covers with the amount for each.
> 3. If you paid more than you owe, put the surplus in your wallet.
> 4. Finance checks the receipt and approves or rejects it. Follow its status on the same page. Receipts change your balance only once Finance approves them.
> 5. Wallet credit can pay any fee instantly with Pay Selected, without waiting for verification.

**finance-payment-channels** › Which bank accounts can I pay tuition into? · similarity 0.790

> Tuition is paid into the official bank accounts of The ICT University published by the Secretary General in the notice "Changes to the ICT University official bank account details" (10 October 2024). The account details are served by the knowledge base database (document finance-bank-accounts) and are not published in the public code repository. Payments to accounts that are not in the official notice are not recognised.

</details>

**3B answer** (cited: finance-payment-channels)

> The payment methods for tuition at ICT University are accepted through the official bank accounts published in the notice "Changes to the ICT University official bank account details" issued on 10 October 2024. These accounts are not publicly available but can be accessed through the knowledge base database [finance-bank-accounts]. Payments to any other bank accounts are not recognised and will not be accepted. [finance-payment-channels]

Claude: **correct**: Official bank accounts per the 10 Oct 2024 notice; others not recognised

Your verdict (3B FIN-06): ok

**7B answer** (cited: finance-payment-channels)

> The payment method accepted is through the bank, specifically into the official bank accounts of The ICT University as published by the Secretary General in the notice "Changes to the ICT University official bank account details" (10 October 2024). Payments to other accounts are not recognised. [finance-payment-channels]

Claude: **correct**: Bank payment into the official accounts; did not take the canteen draft heading as an answer

Your verdict (7B FIN-06): ok

### ERP-02: How do I log in to the ERP for the first time?

*erp, procedural, en* · expected documents: erp-first-login

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**erp-first-login** › How do I log in to the ERP for the first time? · similarity 0.914

> 1. Open the ERP address given by the university.
> 2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
> 3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
> 4. Click Sign in. You go straight to your own dashboard.

**erp-first-login** › What is my first password? · similarity 0.875

> Accounts created by an administrator start with an initial password that the university gives you, unless a different one was given to you. The initial password is not published in this knowledge base. Ask the ERP support contact or the Registrar's office if you do not know it. Change it the first time you log in: click your name at the top right, choose Change Password, enter the current password and the new password twice, then click Update Password. Use at least 8 characters mixing letters and numbers.

**erp-course-registration** › How do I register courses on the ERP? · similarity 0.843

> 1. Open Course Registration (the Courses item of the menu).
> 2. If it is your first time, complete the biodata panel (date and place of birth, region, phone, address, last school, parent or guardian) and click Save.
> 3. The courses of your programme for the current semester are listed. Tick the ones you want and click Register Selected.
> 4. Your programme Coordinator approves the registration. Until then the course shows as pending, and you are notified of the decision.
> 5. Click Print / PDF to produce the official Course Registration Form. It carries a verification reference that staff can check online.

**erp-first-login** › I have a matricule but no ERP account. What do I do? · similarity 0.878

> Use Student registration on the login page, enter your matricule and your details. The account stays pending until the Admission Office approves it. New applicants use Apply for admission instead.

</details>

**3B answer** (cited: erp-first-login)

> To log in to the ERP for the first time, follow these steps:
>
> 1. Open the ERP address given by the university.
> 2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
> 3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
> 4. Click Sign in. You go straight to your own dashboard.
>
> [erp-first-login] [erp-first-login] [erp-first-login]
>
> Note: If you have a matricule but no ERP account, use Student registration on the login page and enter your matricule along with your details. The account will be pending until the Admission Office approves it. New applicants should use Apply for admission instead.

Claude: **correct**: Four steps verbatim

Your verdict (3B ERP-02): ok

**7B answer** (cited: erp-first-login)

> To log in to the ERP for the first time, follow these steps:
>
> 1. Open the ERP address given by the university.
> 2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
> 3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
> 4. Click Sign in. You go straight to your own dashboard.
>
> [erp-first-login]

Claude: **correct**: Four steps verbatim

Your verdict (7B ERP-02): ok

### ERP-03: I forgot my ERP password. What do I do?

*erp, procedural, en* · expected documents: erp-password-reset

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**erp-password-reset** › How do I reset a forgotten ERP password? · similarity 0.912

> On the login page click Forgot password?, type your email or matricule, and the system emails you a secure link to choose a new password. The link expires after a short time and works only once.

**erp-password-reset** › How do I change my password when I am logged in? · similarity 0.905

> Click your name at the top right, choose Change Password, enter your current password and the new password twice, then click Update Password.

**erp-first-login** › What is my first password? · similarity 0.881

> Accounts created by an administrator start with an initial password that the university gives you, unless a different one was given to you. The initial password is not published in this knowledge base. Ask the ERP support contact or the Registrar's office if you do not know it. Change it the first time you log in: click your name at the top right, choose Change Password, enter the current password and the new password twice, then click Update Password. Use at least 8 characters mixing letters and numbers.

**erp-first-login** › How do I log in to the ERP for the first time? · similarity 0.879

> 1. Open the ERP address given by the university.
> 2. In "Email or Matricule" type your ICTU email address or, as a student, your matricule.
> 3. Type your password (the eye icon shows or hides it; a warning appears if Caps Lock is on).
> 4. Click Sign in. You go straight to your own dashboard.

</details>

**3B answer** (cited: erp-password-reset)

> If you forgot your ERP password, you can reset it by following these steps:
>
> - [erp-password-reset] Click on the "Forgot password?" option on the login page.
> - Type your email or matricule and the system will send you a secure link to choose a new password via email. The link is only valid for a short time and can be used only once.
>
> You do not need to contact the ERP support contact or the Registrar's office for this process; it is handled internally by the university.

Claude: **partial**: Steps right; UNSUPPORTED claim 'you do not need to contact the ERP support... handled internally' (the source says to contact them if you lost email access)

Your verdict (3B ERP-03): ok

**7B answer** (cited: erp-password-reset)

> To reset a forgotten ERP password, follow these steps:
>
> 1. Go to the login page.
> 2. Click on "Forgot password?".
> 3. Enter your email or matricule.
> 4. The system will send you a secure link via email to choose a new password. This link expires after a short time and works only once [erp-password-reset].

Claude: **correct**: Steps right, link expires and works once; no invented button or claim

Your verdict (7B ERP-03): ok

### TTB-03: When are the exams?

*timetables, factual, en* · expected documents: timetables-exams

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**about-academic-regulations** › What is required to sit end-of-semester examinations? · similarity 0.809

> Complete institutional and financial clearance: the Finance Office does not issue examination passes, and students are not admitted to examination halls, without 100% payment of their school fees for the academic period. Ad-hoc payment arrangements or last-minute clearances at the examination doors are prohibited.

**timetables-exams-files** › When are the exams? · similarity 0.859

> For the first semester 2026/2027 the examinations are scheduled from Monday 25 January to Wednesday 3 February 2027, after the end of lectures and revision (18 to 23 January 2027), according to the official communique of 25 October 2026. Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 from 4 to 10 January 2027.

**about-academic-regulations** › What are the rules for online students and the Moodle platform? · similarity 0.802

> Continuous assessments, quizzes, term papers, assignments and online end-of-semester examinations of online students are administered and submitted exclusively through the official ICT University Moodle platform. Lecturers must not accept assignments or exam papers sent by email, except during a documented system-wide outage announced by an official technical notice of the IT Office. Online students who default on the fee schedule have their Moodle accounts automatically suspended. Sharing login credentials or using a classmate's account to bypass a suspension leads to disciplinary action, including formal academic suspension and forfeiture of course credits, for both the student and the account holder.

**about-academic-regulations** › Attachment · similarity 0.794

> Academic Compliance and Administrative Policy ICTU-VC-POL-2026/01 of 11 November 2026 signed by the Vice-Chancellor (scanned, 4 pages): attendance 80 percent rule, lecture and exam admission controls, Moodle regulations, enforcement responsibilities.

</details>

**3B answer** (cited: timetables-exams-files about-academic-regulations)

> The exams are scheduled from Monday, 25 January to Wednesday, 3 February 2027. Continuous Assessment 1 is from 14 to 19 December 2026 and Continuous Assessment 2 is from 4 to 10 January 2027.
>
> [timetables-exams-files] [about-academic-regulations]

Claude: **correct**: Dates exact

Your verdict (3B TTB-03): ok

**7B answer** (cited: timetables-exams-files)

> The exams for the first semester 2026/2027 are scheduled from Monday 25 January to Wednesday 3 February 2027. Continuous Assessment 1 is from 14 to 19 December 2026, and Continuous Assessment 2 from 4 to 10 January 2027. [timetables-exams-files]

Claude: **correct**: Exam dates and both CA windows exact

Your verdict (7B TTB-03): ok

### MHP-01: I owe part of my fees and want a transcript. What do I need to do?

*finance, multi-hop, en* · expected documents: finance-clearance procedures-transcript

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-transcript** › What do I need before I can get a transcript? · similarity 0.886

> The transcript is not available while you have outstanding fees. The cost and the processing time are not stated in the ERP manual.

**procedures-transcript** › How do I request an official stamped transcript? · similarity 0.890

> Under Requests and Services choose a partial or full official transcript, choose the turnaround (standard or express, where offered), state the purpose and submit. The fee, if any, is added to My Fees. The Registrar's Office processes the request and you can follow its status and reference number on the page.

**erp-fee-statement** › How do I view my fee statement on the ERP? · similarity 0.840

> Open My Fees. It is your complete fee statement: tuition, resit fees, senior project fees and other fees (application, student union, infirmary, graduation, bus, additional course, late registration, transcript), fines, and your wallet balance.

**procedures-transcript** › How do I get my transcript? · similarity 0.851

> The Transcript page of the ERP shows all your approved results grouped by semester with the semester GPA and your CGPA; credits transferred from another university appear at the top. Use Download/Print Transcript for the official layout.

</details>

**3B answer** (cited: erp-fee-statement procedures-transcript)

> You need to pay your outstanding fees before you can get a transcript. Once your fees are settled, follow these steps:
>
> 1. Go to the Transcript page on the ERP.
> 2. Use Download/Print Transcript to get an official stamped transcript.
> 3. Your fee statement on the ERP will show all your approved results grouped by semester with GPA and CGPA; credits transferred from another university appear at the top.
>
> [erp-fee-statement] [procedures-transcript]

Claude: **partial**: Pay first: right; 'Download/Print Transcript to get an official stamped transcript' wrong; results attributed to the fee statement

Your verdict (3B MHP-01): ok

**7B answer** (cited: procedures-transcript)

> You need to settle your outstanding fees before requesting a transcript. Once your fees are settled, you can request an official stamped transcript through the ERP system by following these steps:
>
> 1. Under Requests and Services, choose either a partial or full official transcript.
> 2. Select the turnaround time (standard or express, if offered).
> 3. State the purpose of the request.
> 4. Submit the request.
>
> The fee for the transcript, if any, will be added to your My Fees page. You can track the status and reference number on the same page. [procedures-transcript]

Claude: **correct**: Fees first, then the Requests and Services steps; finance-clearance was not retrieved, so how to clear is not covered (retrieval, not the model)

Your verdict (7B MHP-01): ok

### MHP-02: I failed a course. How do I resit, and what will it cost?

*procedures, multi-hop, en* · expected documents: procedures-resits finance-fee-schedule

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-resits** › How do I register for a resit and what does it cost? · similarity 0.874

> Open Resit Registration in the ERP. It lists your resit courses with the resit fee and its payment status. Pay the resit fee (see My Fees and the payment channels document). Once the fee is paid, your lecturer enters the resit score. The amount of the resit fee is shown in the ERP for each course; it is not stated in the manual.

**procedures-resits** › What is a special resit? · similarity 0.872

> For a course failed in an earlier, already closed semester, click Request on Resit Registration and add a note to the Dean. If the Dean agrees, the lecturer scores a fresh mark out of 100, also capped at 79.

**procedures-resits** › Who is eligible for a resit? · similarity 0.865

> A course with a total below 50 is resit-eligible, once the resit fee is paid.

**procedures-complaints** › How do I file a complaint about a mark or a grade? · similarity 0.843

> Complaints about results are filed online in the ICTU ERP; nobody needs to queue at an office. Open the Complaints page (More, then Complaints on a computer; Menu, then Complaints on a phone), keep "About a Course" selected, choose the course, and click the category that fits: Missing CA Marks, Missing Exam Marks, Missing Resit Marks, Wrong Mark Entered, Grade Appeal (a request to re-mark the script), Attendance Dispute, or Other. For a missing or wrong mark, tick the mark concerned (CA out of 30, exam and resit out of 70) and type the mark you expect. Describe the problem in a few precise sentences, optionally attach evidence (PDF, JPG or PNG, up to 10 MB), then click Submit Complaint. The ERP gives a ticket number such as C-2026-811; keep it. You cannot open a second complaint on the same course and category while the first is open; reply to the open one instead.

</details>

**3B answer** (cited: procedures-resits)

> To resit a failed course, you need to follow these steps:
>
> - First, ensure that the total mark for the course is below 50.
> - Then, register for the resit by opening Resit Registration in the ERP.
> - The ERP will list your resit courses along with the resit fee and its payment status.
> - Pay the resit fee using the payment channels provided in the document.
> - Once the fee is paid, your lecturer will enter a fresh mark out of 100 for the course.
>
> [procedures-resits] [procedures-resits] [procedures-resits]

Claude: **wrong**: 'lecturer will enter a fresh mark out of 100' is the special-resit rule; a normal resit is out of 70 added to CA. Cost not mentioned

Your verdict (3B MHP-02): ok

**7B answer** (cited: procedures-resits)

> To resit a course that you have failed:
>
> 1. Open Resit Registration in the ERP.
> 2. Pay the resit fee for each course, which amount is shown in the ERP for each course [procedures-resits].
> 3. Once the fee is paid, your lecturer will enter the resit score.
>
> The cost of the resit fee is not explicitly stated but can be found in the ERP for each course [procedures-resits].

Claude: **correct**: Normal-resit registration and "fee shown in the ERP, not in the manual"; did not mix in the special-resit rule (3B failure 29)

Your verdict (7B MHP-02): ok

### MHP-03: I'm applying for the Masters. What are the requirements and the fees?

*admissions, multi-hop, en* · expected documents: admissions-masters-requirements finance-fee-schedule

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**admissions-masters-requirements** › What are the entry requirements for the Masters program? · similarity 0.868

> To apply for a Master's degree in the Faculty of ICT or the Faculty of Business Management and Sustainability (BMS) you need: (1) the online application on the student portal (https://studentportal.ictuniversity.edu.cm/portal-sign-up/); (2) a certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution; (3) a scanned copy of identification documents (birth certificate, national ID card or passport); (4) three letters of recommendation; (5) a statement of purpose; (6) a certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA, a non-refundable application fee.

**web-maters-degree-entry-requirements** › NEW STUDENTS ! · similarity 0.834

> To complete your application for a Masters degree program at the ICT University, both in Information Communication and Technology (ICT) and in Business Management and Sustainability (BMS), please ensure you provide the following documents:
>
> 1. Complete our online application at the ICT Universty  [portal-sign-up](https://studentportal.ictuniversity.edu.cm/portal-sign-up/)
> 2. Certified Scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
> 3. Scanned copy of identification documents (birth certificate, National ID card, Passport)
> 4. Three letters or recommendations
> 5. Statement of Purpose
> 6. Certified Scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (Non-refundable Application Fee).
>
> [SEE OUR MASTERS PROGRAMS](https://ictuniversity.org/masters-programs/)
>
> [APPLY NOW](https://studentportal.ictuniversity.edu.cm/portal-sign-up/)

**web-maters-degree-entry-requirements** ›  · similarity 0.831

> ICT University :
>
> Master’s   Degree Entry  Requirements
>
> [APPLY NOW](https://studentportal.ictuniversity.edu.cm/portal-sign-up/)
>
> Master's Degree entry requirements for :

**finance-fee-schedule** › How much is the tuition? · similarity 0.834

> The complete tuition is XAF 365,000 (Central African francs). The programme and level it applies to are not specified in the information collected so far; fees may differ between Bachelor, Masters and PhD programs.

</details>

**3B answer** (cited: admissions-masters-requirements finance-fee-schedule)

> To apply for the Master's program at ICT University, you need to provide the following documents:
>
> - Complete online application on the student portal [admissions-masters-requirements].
> - Certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript from an accredited institution [admissions-masters-requirements].
> - Scanned copy of identification documents (birth certificate, national ID card or passport) [admissions-masters-requirements].
> - Three letters of recommendation [admissions-masters-requirements].
> - Statement of purpose [admissions-masters-requirements].
> - Certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA (non-refundable application fee) [admissions-masters-requirements].
>
> Regarding fees, the complete tuition is XAF 365,000 (Central African francs). However, this information is not specified in detail for Bachelor, Masters, and PhD programs. Please refer to the [finance-fee-schedule] for more specific details on fees per program and level.

Claude: **correct**: Requirements + 365,000 with caveat

Your verdict (3B MHP-03): ok

**7B answer** (cited: finance-fee-schedule)

> To apply for a Master's degree at ICT University, you need to provide the following:
>
> 1. The online application on the student portal (https://studentportal.ictuniversity.edu.cm/portal-sign-up/).
> 2. A certified scanned copy of a Bachelor's degree or Licence/Maitrise/DEA and an official transcript in a related area from an accredited institution.
> 3. A scanned copy of identification documents (birth certificate, national ID card or passport).
> 4. Three letters of recommendation.
> 5. A statement of purpose.
> 6. A certified scanned copy of the receipt of payment into the ICT-U bank account of $50 or 25,000 CFA, which is a non-refundable application fee.
>
> The complete tuition is XAF 365,000 (Central African francs). [finance-fee-schedule]

Claude: **partial**: Six requirements verbatim (application fee $50/25,000 CFA right), but "the complete tuition is XAF 365,000" for a Masters applicant WITHOUT the level caveat; requirements not cited (only finance-fee-schedule)

Your verdict (7B MHP-03): ok

### VAR-01: Comment puis-je m'inscrire aux cours ?

*procedures, variant, fr* · expected documents: procedures-course-registration

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-course-registration** › How do I register for courses each semester? · similarity 0.832

> Registration is done in the ICTU ERP (Course Registration): tick the courses of your programme and click Register Selected, then your programme Coordinator approves the registration, and you print the official Course Registration Form. Since 16 November 2026 students must present a valid, signed and stamped registration form to their lecturers before attending lectures, and only students whose names are on the official class list may attend. The detailed ERP steps are in the ERP course registration document.

**finance-scholarships** › How does a student apply and what is the deadline? · similarity 0.822 · DRAFT

> [[TO FILL]]

**transport-overview** › How does a student subscribe and who is the contact? · similarity 0.822 · DRAFT

> [[TO FILL]]

**erp-course-registration** › What must I have paid before I can register? · similarity 0.820

> You must have paid at least 50% of the semester's tuition. Until then the page explains how much you have paid and how much is still needed. If you have paid, upload the bank receipt in My Fees so that Finance can verify it.

</details>

**3B answer** (cited: procedures-course-registration erp-course-registration)

> Pour vous inscrire aux cours à ICT University, suivez ces étapes :
>
> 1. Vérifiez vos paiements dans l'ERP (Course Registration) : assurez-vous d'avoir payé au moins 50% de la cotisation semestrielle. Si vous n'avez pas encore payé, suivez les instructions pour payer et téléchargez votre reçu bancaire dans My Fees afin que Finance le vérifie.
> 2. Une fois vos paiements validés, accédez à l'ERP (Course Registration) pour inscrire les cours de votre programme. Cochez les cours correspondants et cliquez sur Register Selected.
> 3. Votre coordinateur de programme approuvera votre inscription. Après approbation, imprimez le formulaire de validation d'inscription.
> 4. À partir du 16 novembre 2026, vous devrez présenter un formulaire d'inscription valide, signé et apposé à vos professeurs avant de participer aux cours. Seuls les étudiants inscrits sur la liste des classes seront autorisés à y assister.
>
> [Voir sources : procedures-course-registration, erp-course-registration]

Claude: **correct**: French; 'ICT University', steps and 16 Nov rule sourced, ERP not expanded

Your verdict (3B VAR-01): ok

**7B answer** (cited: procedures-course-registration)

> Pour vous inscrire aux cours, procédez comme suit :
>
> 1. Connectez-vous à l'ICTU ERP (Course Registration).
> 2. Cochez les cours de votre programme.
> 3. Cliquez sur "Register Selected".
> 4. Obtenez l'approbation de votre Coordinateur de programme.
> 5. Imprimez le formulaire de registration des cours officiel.
>
> N'oubliez pas que depuis le 16 novembre 2026, vous devez présenter un formulaire de registration des cours valide, signé et tamponné à vos professeurs avant d'assister aux cours. Seuls les noms figurant sur la liste officielle des classes peuvent y assister.
>
> [procedures-course-registration]

Claude: **correct**: Steps and the 16 November rule in French; "formulaire de registration" is anglicised but not wrong

Your verdict (7B VAR-01): ok

### VAR-02: Quels sont les frais de scolarité ?

*finance, variant, fr* · expected documents: finance-fee-schedule

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**finance-fee-schedule** › How much is the tuition? · similarity 0.820

> The complete tuition is XAF 365,000 (Central African francs). The programme and level it applies to are not specified in the information collected so far; fees may differ between Bachelor, Masters and PhD programs.

**finance-scholarships** › How does a student apply and what is the deadline? · similarity 0.819 · DRAFT

> [[TO FILL]]

**finance-scholarships** › Which scholarships or discounts exist and who qualifies? · similarity 0.815 · DRAFT

> [[TO FILL]]

**campus-directions** › What are the usual fares or travel times? · similarity 0.811 · DRAFT

> [[TO FILL]]

</details>

**3B answer** (cited: finance-fee-schedule)

> Les frais de scolarité à ICT University sont de XAF 365,000 [finance-fee-schedule]. Les programmes et niveaux ne sont pas spécifiés dans les informations collectées jusqu'à présent, donc les frais peuvent varier entre les programmes Bachelor, Masters et PhD.

Claude: **correct**: French; name rule worked: 'ICT University', caveat kept

Your verdict (3B VAR-02): ok

**7B answer** (cited: finance-fee-schedule)

> Les frais de scolarité pour ICT University s'établissent à XAF 365,000 (francs centrafricains) [finance-fee-schedule]. Cependant, il n'est pas spécifié si cette somme concerne un bachelor, un master ou un doctorat.

Claude: **correct**: 365,000 with the caveat that the level is not specified, in French

Your verdict (7B VAR-02): ok

### NEG-02: What is my current fee balance?

*finance, no-answer, en* · expected documents: (none: no answer expected)

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**erp-fee-statement** › How do I view my fee statement on the ERP? · similarity 0.838

> Open My Fees. It is your complete fee statement: tuition, resit fees, senior project fees and other fees (application, student union, infirmary, graduation, bus, additional course, late registration, transcript), fines, and your wallet balance.

**erp-fee-statement** › How do I pay and prove my payment? · similarity 0.833

> 1. Pay at the bank as instructed by the Finance office (official accounts are in the payment channels document).
> 2. In My Fees click to upload the receipt: enter the bank name and the transaction reference, attach the receipt (image or PDF), and tick every fee this one payment covers with the amount for each.
> 3. If you paid more than you owe, put the surplus in your wallet.
> 4. Finance checks the receipt and approves or rejects it. Follow its status on the same page. Receipts change your balance only once Finance approves them.
> 5. Wallet credit can pay any fee instantly with Pay Selected, without waiting for verification.

**finance-fee-notices** › What fee changes or payment deadlines have been announced recently? · similarity 0.848 · DRAFT STALE

> [[TO FILL]]

**finance-fee-schedule** › Where can I find the full fee schedule per program and level? · similarity 0.817

> The full fee schedule per program and level is not available in this knowledge base yet. Please ask the Admissions office (admissions@ictuniversity.edu.cm) or the Finance office. The official fee schedule is published in the university announcements.

</details>

**3B answer** (cited: finance-fee-schedule)

> I do not have that information. You can contact the Finance office at finance@ictuniversity.edu.cm to find out your current fee balance. [finance-fee-schedule]

Claude: **refused**: Correct; invented finance@ address removed by the redactor

Your verdict (3B NEG-02): ok

**7B answer** (cited: erp-fee-statement)

> Your current fee balance can be found on the ERP system under "My Fees." It includes tuition, resit fees, senior project fees, other fees (application, student union, infirmary, graduation, bus, additional course, late registration, transcript), fines, and your wallet balance [erp-fee-statement].

Claude: **correct**: Not a refusal but a grounded redirect: see My Fees in the ERP (erp-fee-statement, verbatim). No invented contact (3B invented finance@ in most runs)

Your verdict (7B NEG-02): ok

### NEG-04: Will I pass my resit?

*procedures, no-answer, en* · expected documents: (none: no answer expected)

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

**procedures-resits** › Who is eligible for a resit? · similarity 0.833

> A course with a total below 50 is resit-eligible, once the resit fee is paid.

**procedures-resits** › How is a resit graded? · similarity 0.828

> Normal resit: the resit score (out of 70) is added to your CA mark. The final total is capped at 79 (grade B+, 3.5 points).

**procedures-resits** › How do I register for a resit and what does it cost? · similarity 0.816

> Open Resit Registration in the ERP. It lists your resit courses with the resit fee and its payment status. Pay the resit fee (see My Fees and the payment channels document). Once the fee is paid, your lecturer enters the resit score. The amount of the resit fee is shown in the ERP for each course; it is not stated in the manual.

**procedures-resits** › What is a special resit? · similarity 0.821

> For a course failed in an earlier, already closed semester, click Request on Resit Registration and add a note to the Dean. If the Dean agrees, the lecturer scores a fresh mark out of 100, also capped at 79.

</details>

**3B answer** (cited: procedures-resits)

> To determine if you will pass your resit, we need to consider a few factors based on the information provided:
>
> 1. The total mark of your course must be below 50 for it to be eligible for a resit.
> 2. If the resit is a normal resit, your final total will be capped at 79 (grade B+, 3.5 points).
>
> Therefore, if your initial course total was below 50 and you pass the resit (which scores out of 70), your final total will be capped at 79.
>
> [procedures-resits] [procedures-resits] [procedures-resits]

Claude: **partial**: No prediction and no false rule, but restates the rules instead of saying it can't know

Your verdict (3B NEG-04): ok

**7B answer** (cited: procedures-resits)

> I do not have that information [procedures-resits]. The outcome depends on your performance during the resit examination, which is scored out of 70 and added to your continuous assessment (CA) mark, with a final total capped at 79 (grade B+, 3.5 points). For courses failed in an earlier semester, you may request a special resit with the Dean's approval.

Claude: **refused**: Says it does not have that information, then explains accurately what the result depends on (out of 70 + CA, capped at 79, special resit). The ideal answer; no prediction

Your verdict (7B NEG-04): ok

*Not listed: VAR-03, NEG-01, NEG-03, NEG-05. The model wasn't called (below the similarity threshold or only unfilled drafts), so the code refused in both runs; there is nothing to judge.*

---

## The two list questions (asked of both models on 2026-11-26)

### PRG-02: Which Masters programs are offered?

*programs, list, en* · expected documents: programs-masters web-masters-programs

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

</details>

**3B answer** (cited: programs-masters)

> The following Masters programs are offered at ICT University:
>
> - Artificial Intelligence
> - Applied ICTs in Education
> - Applied ICT in Public Health
> - Information Systems Security
> - Information Technology
> - Information Systems and Networking
>
> [programs-masters]

Claude: **partial**: 6 ICT Masters, the 3 BMS Masters missing (failure 17 reproduced with current settings)

Your verdict (3B PRG-02): ok

**7B answer** (cited: programs-masters web-masters-programs)

> The following Masters programs are offered:
>
> 1. Applied Statistics and Demography
> 2. Development Planning
> 3. iMBA (iMBA)
> 4. Artificial Intelligence
> 5. Applied ICTs in Education
> 6. Applied ICT in Public Health
> 7. Information Systems Security
> 8. Information Technology
> 9. Information Systems and Networking
> 10. BMS Master's programs (Applied Statistics and Demography, Development Planning, iMBA)
>
> Sources: [programs-masters], [web-masters-programs]

Claude: **correct**: All 9 Masters (6 ICT + 3 BMS); a redundant 10th line repeats the BMS group, "iMBA (iMBA)", and the model wrote its own "Sources:" line (cosmetic)

Your verdict (7B PRG-02): ok

### ADM-02: What documents do I need for a Bachelors application?

*admissions, list, en* · expected documents: admissions-bachelor-requirements web-bachelors-degree-entry-requirements

<details><summary>Passages retrieved for this question (click to open; any far below the best match were not given to the model)</summary>

</details>

**3B answer** (cited: admissions-bachelor-requirements)

> For a Bachelor's application at ICT University, you need the following documents:
>
> - Certified copy of the birth certificate
> - Certified copies of the GCE "O" Level certificate, GCE "A" Level certificate, Probatoire, and Baccalaureate
> - Certified copy of the HND diploma (if applying as a Top-Up student)
>
> These documents are required for both new students and Top-Up students. [admissions-bachelor-requirements] [admissions-bachelor-requirements]

Claude: **partial**: HND correctly conditioned on Top-Up, then contradicts it ("required for both new students and Top-Up students"); "authenticated copies" dropped

Your verdict (3B ADM-02): ok

**7B answer** (cited: admissions-bachelor-requirements)

> To complete an application for a Bachelor's degree, you need to provide the following documents:
> - A certified copy of the birth certificate
> - Certified copies of the GCE "O" Level certificate, GCE "A" Level certificate, Probatoire, and Baccalaureate
> - Authenticated copies of the GCE "O" Level certificate, GCE "A" Level certificate, Probatoire, and Baccalaureate [admissions-bachelor-requirements].

Claude: **correct**: New-student documents verbatim (certified and authenticated copies); the Top-Up HND addition, in a separate section, not mentioned

Your verdict (7B ADM-02): ok
