# Unit 3: Applications of computers in pharmacy

Computers are now part of almost every pharmacy task: storing and finding drug information, calculating pharmacokinetic values, designing new molecules, running hospital and clinical pharmacy services, prescribing electronically, identifying medicines by barcode, dispensing automatically and helping patients take their medicines. This unit covers each application named in the syllabus, together with diagnostic, laboratory, patient-monitoring and pharma information systems.

## 3.1 Overview: where computers are used

| Area | Examples of use |
| --- | --- |
| Community pharmacy | Billing, stock control, expiry tracking, patient records, drug interaction alerts |
| Hospital and clinical pharmacy | Hospital information system, e-prescribing, unit-dose dispensing, therapeutic drug monitoring, adverse drug reaction reporting |
| Industry | Drug design, formulation development, production control, quality control data, documentation |
| Research | Pharmacokinetic modelling, statistics, bioinformatics, literature search |
| Regulation and education | Online submissions, drug databases, e-learning |

## 3.2 Drug information storage and retrieval

**Drug information** means accurate, up-to-date facts about medicines given to health professionals and patients. A **drug information centre** answers queries about doses, interactions, side effects, use in pregnancy, compatibility and identification of tablets.

**Storage** — information is kept in electronic databases instead of books and files:

- Tertiary sources: drug compendia, formularies and drug databases (National Formulary of India, Indian drug indexes, Micromedex, Lexicomp).
- Secondary sources: indexing and abstracting services (MEDLINE/PubMed, Embase) that point to articles.
- Primary sources: original research articles in online journals.
- The centre's own records of queries and answers, stored for reuse.

**Retrieval** — finding the needed information quickly by searching:

- Search by generic name, brand, class, indication or keyword.
- Use **Boolean operators**: AND (narrows: *metformin AND pregnancy*), OR (widens: *paracetamol OR acetaminophen*), NOT (excludes).
- Use filters (year, language, study type) and controlled vocabulary such as MeSH terms in PubMed.

**Steps in answering a query with a computer**

```text
Receive query → classify it and collect patient details → search tertiary source
     → if needed, secondary and primary sources → evaluate the evidence
     → give the answer (oral/written) → document the query and answer in the database
```

**Advantages:** speed, large storage in little space, easy updating, many users at once, search by many fields, records available for audit and teaching. **Limitations:** cost of subscriptions and hardware, need for training, dependence on power and Internet, risk of outdated or unreliable online information.

## 3.3 Computers in pharmacokinetics

**Pharmacokinetics** studies what the body does to a drug: absorption, distribution, metabolism and excretion (ADME). It needs many calculations on plasma concentration–time data, which computers do quickly and accurately.

**Uses**

1. **Calculating parameters** from concentration–time data: Cmax, tmax, area under the curve (AUC, by the trapezoidal rule), elimination rate constant (k), half-life (t½ = 0.693/k), clearance, volume of distribution and bioavailability.
2. **Fitting models** — choosing a one- or two-compartment model, or a non-compartmental analysis, and fitting the data by non-linear regression.
3. **Simulation** — predicting plasma levels for a new dose, dosing interval or route before giving it.
4. **Dosage regimen design and individualisation** — adjusting doses for kidney or liver disease, age and weight; used in **therapeutic drug monitoring (TDM)** of narrow therapeutic index drugs such as digoxin, aminoglycosides, phenytoin, lithium and vancomycin.
5. **Population pharmacokinetics** — studying how parameters vary between patients using data from many people.
6. **Bioavailability and bioequivalence studies** — calculating and statistically comparing AUC and Cmax of test and reference products.
7. **Physiologically based pharmacokinetic (PBPK) models** — models built from organ blood flows and volumes to predict drug levels in organs.

**Software examples:** spreadsheets (MS Excel) for simple calculations, and specialised programs such as Phoenix WinNonlin and NONMEM used in industry and research.

```text
Plasma concentration
   |        * Cmax
   |      *    *
   |    *         *          AUC = area under this curve
   |  *              *  *
   |*                      *  *
   +----------------------------------- time
        tmax
```

## 3.4 Mathematical models in drug design

Discovering a drug by making and testing thousands of compounds is slow and costly. **Computer-aided drug design (CADD)** uses mathematical and computer models to predict which molecules are likely to work before they are made.

**1. Quantitative structure–activity relationship (QSAR)**

QSAR relates biological activity to measurable properties of molecules through an equation. The best known is the **Hansch approach**, which links activity (often written as log 1/C, where C is the concentration giving a fixed effect) to:

- **Lipophilicity** — partition coefficient (log P) or the substituent constant π;
- **Electronic effects** — the Hammett constant σ;
- **Steric (size) effects** — Taft's constant Es or molar refractivity.

A typical form is: log 1/C = a·π + b·σ + c·Es + d (a, b, c and d are found by regression; a squared π term is added when activity rises and then falls with lipophilicity). Once the equation is known, activity of new molecules can be predicted. **3D-QSAR** methods (such as CoMFA) use the three-dimensional fields around the molecules.

**2. Molecular modelling**

- **Molecular mechanics** — treats atoms as balls and bonds as springs to find the lowest-energy shape (conformation).
- **Quantum mechanics** — calculates electron distribution and reactivity for more accurate, slower results.
- **Molecular dynamics** — simulates how molecules move over time.

**3. Structure-based design** (when the 3D structure of the target protein is known, e.g. from X-ray crystallography in the Protein Data Bank):

- **Docking** — fits candidate molecules into the binding site and scores how well they bind.
- **Virtual screening** — docks large libraries of compounds by computer to pick a few for testing.

**4. Ligand-based design** (when the target structure is unknown): **pharmacophore** models (the 3D arrangement of features needed for activity, such as a hydrogen-bond donor, an aromatic ring and a positive charge) and similarity searching.

**5. ADMET prediction** — estimating absorption, distribution, metabolism, excretion and toxicity from structure, e.g. checking Lipinski's rule of five for oral drugs (molecular weight not more than 500, log P not more than 5, not more than 5 hydrogen-bond donors and not more than 10 acceptors).

**Advantages:** fewer compounds to synthesise, lower cost, shorter discovery time, better understanding of how drugs bind. Computer predictions must still be confirmed by laboratory and clinical tests.

## 3.5 Computers in hospital and clinical pharmacy

A **hospital information system (HIS)** links all departments (registration, wards, laboratory, radiology, pharmacy, billing). The **pharmacy module** handles:

- **Inventory control** — purchase orders, receipt, stock levels, reorder alerts, batch and expiry tracking, ABC/VED analysis.
- **Dispensing** — to outpatients and to wards (floor stock, individual prescription and **unit-dose** systems); labels and records.
- **Patient medication profiles** — all current and past drugs, allergies, weight, laboratory results.
- **Clinical decision support** — alerts for drug–drug interactions, drug–allergy problems, duplicate therapy, dose limits and renal dose adjustment.
- **Clinical pharmacy services** — medication review, TDM calculations, total parenteral nutrition calculations, intravenous admixture records.
- **Pharmacovigilance** — recording and reporting adverse drug reactions (in India to the Pharmacovigilance Programme of India).
- **Formulary management**, drug use evaluation, billing and statistical reports for the pharmacy and therapeutics committee.
- **Narcotic and psychotropic registers** kept electronically with audit trails.

## 3.6 Electronic prescribing and discharge (EP) systems

**Electronic prescribing (e-prescribing)** means the prescriber enters the prescription into a computer instead of writing it, and it is sent electronically to the pharmacy. In hospitals it is often part of **computerised physician (provider) order entry (CPOE)**. An **electronic discharge** system produces the discharge prescription and summary for the patient and the next care provider.

**How it works**

```text
Doctor selects drug, dose, route, frequency on screen
      → system checks allergies, interactions, dose range (decision support)
      → order sent to pharmacy electronically
      → pharmacist verifies and dispenses
      → nurse records administration on the electronic chart
      → at discharge: discharge prescription + summary printed/sent to patient and family doctor
```

**Benefits**

- No problems from illegible handwriting; complete orders (no missing dose or route).
- Fewer medication errors through automatic checks.
- Faster communication between doctor, pharmacy and nurse.
- Complete medication history and easier audit; better continuity of care at discharge.
- Data for research, stock planning and cost control.

**Problems:** cost and training, system downtime, "alert fatigue" when too many warnings appear, and new errors such as choosing the wrong item from a drop-down list.

## 3.7 Barcode medicine identification and automated dispensing

### Barcode medicine identification

A **barcode** stores a product's code as a pattern of bars (linear barcode) or squares (two-dimensional codes such as the DataMatrix or QR code) that a scanner reads. Global standards for product barcodes come from GS1. A 2D code can also carry the batch number and expiry date. Indian rules now also require a QR code on the labels of active pharmaceutical ingredients and of specified leading formulation brands, to help detect fake medicines.

**Barcode medication administration (BCMA)** in hospitals:

1. The nurse scans the patient's wristband barcode.
2. The nurse scans the barcode on the medicine.
3. The computer checks the **"rights"** of medication use — right patient, right drug, right dose, right route, right time — against the electronic order.
4. A warning appears if anything does not match; administration is recorded automatically.

**Uses in the pharmacy:** receiving stock, picking the right product, billing, batch recall, expiry checks and stock counts.

### Automated dispensing

- **Automated dispensing cabinets (ADCs)** — computer-controlled cabinets on wards that release only the drugs ordered for a patient after the nurse logs in; they record who removed what and when, which is useful for controlled drugs.
- **Pharmacy robots** — machines that store, pick and deliver packs to the counter, or count tablets and fill and label containers.
- **Unit-dose packaging machines** — pack each dose separately with the patient's name and barcode.

**Benefits:** fewer picking errors, faster dispensing, better stock control and security, and more pharmacist time for patient care. **Limitations:** high cost, maintenance, and errors if the machine is loaded wrongly.

## 3.8 Mobile technology and adherence monitoring

**Adherence** means taking medicines as agreed with the prescriber. Poor adherence leads to treatment failure, resistance (in tuberculosis and HIV) and extra cost. Mobile technology (**mHealth**) helps:

- **Reminder apps and SMS** messages at dose times; refill reminders.
- **Electronic pill bottles and caps** (medication event monitoring systems) that record each opening with date and time.
- **Smart pill boxes** that light up or beep and alert a family member if a dose is missed.
- **Video-observed therapy** — the patient records or shows taking the dose (used in tuberculosis programmes).
- **Tele-pharmacy and teleconsultation** — counselling by phone or video.
- **Wearables** linked to apps (glucose and blood pressure readings shared with the care team).
- Apps that hold the patient's medicine list, allergies and pill images.

Problems include privacy of health data, cost, low smartphone or digital literacy in some patients, and reminders being ignored over time.

## 3.9 Diagnostic system

A **computer-aided diagnostic system** helps a doctor reach a diagnosis.

- **Expert systems** store medical knowledge as rules ("IF fever AND neck stiffness THEN consider meningitis"). An early example was MYCIN, built in the 1970s for choosing antibiotics in infections.
- **Computer-aided detection in imaging** — software marks suspicious areas on X-ray, CT or MRI images for the radiologist.
- **Decision support** in ECG machines that print an interpretation, and symptom-checker programs.

Such systems support, but do not replace, the clinician's judgement.

## 3.10 Lab-diagnostic system

A **laboratory diagnostic system (laboratory information system, LIS)** manages clinical laboratory work:

- Test ordering from the ward, barcode labelling of samples, sample tracking.
- Automatic analysers (haematology, biochemistry) connected to the computer send results directly, avoiding copying errors.
- Checking results against reference ranges and flagging abnormal or critical values.
- Quality control charts, result validation and printing or sending reports to the doctor's screen.
- Storage of past results for comparison.

## 3.11 Patient monitoring system

A **patient monitoring system** continuously measures and displays a patient's vital signs, mainly in ICU, operation theatres and emergency wards.

- Parameters: heart rate and ECG, blood pressure (non-invasive and arterial), oxygen saturation (SpO2), respiratory rate, temperature, end-tidal CO2.
- Sensors send signals to a bedside monitor; values and waveforms are displayed and stored.
- **Alarms** sound when a value crosses a set limit.
- A **central station** lets one nurse watch many beds; data can feed into the electronic record.
- **Remote monitoring** sends readings from the patient's home by Internet or phone (heart failure, diabetes, implanted devices).

## 3.12 Pharma information system

A **pharma (pharmaceutical) information system** is the set of computer systems used to manage information in a pharmaceutical company or pharmacy organisation.

| Area | What it manages |
| --- | --- |
| Research and development | Compound and study data, laboratory notebooks, literature |
| Regulatory affairs | Dossiers for approval, product registrations, submissions |
| Manufacturing | Batch records, production planning, ERP (enterprise resource planning) |
| Quality control and assurance | LIMS, deviations, change control, document control |
| Sales and marketing | Distribution, sales analysis, field force reports |
| Pharmacovigilance | Adverse event case processing and reporting |
| Supply chain | Inventory, warehouse, track and trace |

**Benefits:** quick, correct decisions; less paperwork; compliance with good manufacturing and good laboratory practice; traceability of every batch.

## Remember

- Drug information retrieval: search databases with keywords and Boolean operators (AND narrows, OR widens, NOT excludes).
- Pharmacokinetics: computers calculate AUC, k, t½ = 0.693/k, clearance; fit models; simulate doses; support TDM.
- Drug design: QSAR (Hansch: π, σ, Es), molecular modelling, docking, virtual screening, pharmacophores, ADMET prediction.
- Hospital pharmacy: inventory, unit-dose dispensing, patient profiles, interaction alerts, ADR reporting.
- EP systems remove illegible handwriting and add automatic checks; e-discharge improves continuity of care.
- Barcode medication administration checks the rights of patient, drug, dose, route and time.
- Automated dispensing cabinets and robots cut picking errors.
- Mobile adherence tools: reminders, electronic pill caps, smart boxes, video-observed therapy.
- Diagnostic, lab-diagnostic, patient monitoring and pharma information systems support, not replace, professionals.
