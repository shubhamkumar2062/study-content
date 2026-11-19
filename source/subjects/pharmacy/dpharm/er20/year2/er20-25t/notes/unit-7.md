# Unit 7: Radiopharmaceuticals and computers in hospital pharmacy

This unit joins two short syllabus chapters (2 hours each): chapter 7, storage, dispensing and disposal of radiopharmaceuticals; and chapter 8, application of computers in hospital pharmacy practice, electronic health records and software used in hospital pharmacy. A worked example on radioactive decay and dose volume is included.

## Part A – Radiopharmaceuticals

## 7.1 Definition and basic terms

A **radiopharmaceutical** is a medicinal preparation that contains a **radioactive isotope (radionuclide)**, used for **diagnosis** (imaging, function tests) or **treatment** (destroying diseased tissue). The branch of medicine that uses them is **nuclear medicine**, and the pharmacy that prepares and dispenses them is a **nuclear (radio) pharmacy**.

| Term | Meaning |
| --- | --- |
| Radionuclide | An unstable atom that gives off radiation as it changes (decays) to a stable form |
| Radioactivity | Spontaneous emission of radiation (alpha, beta, gamma) from unstable nuclei |
| Activity | Number of disintegrations per second; SI unit **becquerel (Bq)** = 1 disintegration/s; older unit curie (Ci); 1 mCi = 37 MBq |
| Half-life (T½) | Time for the activity to fall to half |
| Specific activity | Activity per unit mass of the substance |
| Radiochemical purity | Fraction of the total radioactivity present in the desired chemical form |

**Examples:**

| Radiopharmaceutical | Approx. half-life | Use |
| --- | --- | --- |
| **Technetium-99m** (as various kits, e.g. MDP for bone, DTPA for kidney) | about 6 hours | Most widely used for imaging (gamma emitter); obtained from a **Mo-99/Tc-99m generator** |
| **Iodine-131** (sodium iodide) | about 8 days | Treatment of hyperthyroidism and thyroid cancer; thyroid studies |
| **Fluorine-18 fludeoxyglucose (FDG)** | about 110 minutes | PET scans in cancer, brain and heart studies |

A **generator** contains a longer-lived parent (molybdenum-99) bound on a column; the short-lived daughter (technetium-99m) is washed out ("eluted", "milked") with sterile saline when needed.

## 7.2 Radiation safety principles

Radiation can damage cells and DNA, so exposure of staff, patients and the public is kept **As Low As Reasonably Achievable (ALARA)** using three rules:

1. **Time** – work quickly; minimise time near the source.
2. **Distance** – exposure falls sharply with distance (inverse-square law); use tongs and forceps.
3. **Shielding** – lead containers, lead bricks, lead-glass screens, syringe shields; perspex for beta emitters.

Other safety measures: personal dosimeters (TLD badges) for staff, regular area monitoring with a survey meter, no eating or drinking in the area, gloves and gowns, and spill kits. In India, use of radioactive material is regulated by the **Atomic Energy Regulatory Board (AERB)**; the facility needs AERB licensing and a designated **Radiological Safety Officer (RSO)**.

## 7.3 Storage of radiopharmaceuticals

1. In a separate, restricted **"hot lab"** with the radiation warning symbol (trefoil) on the door and containers.
2. In **lead-shielded containers** ("lead pots"), behind lead bricks, in lockable cabinets or fume cupboards for volatile materials such as radio-iodine.
3. At the temperature required for the product (some kits refrigerated before labelling).
4. Records of receipt: radionuclide, activity, calibration date and time, supplier, batch, and storage location; regular stock checks.
5. Generators kept shielded as supplied; elution records maintained.
6. Access only to trained, authorised staff; area monitored for contamination.

## 7.4 Dispensing of radiopharmaceuticals

```text
Prescription / request from nuclear medicine physician
   ↓
Calculate activity needed at the time of administration (decay-corrected)
   ↓
Prepare (elute generator, label kit) in shielded LAF / hot cell, aseptically
   ↓
Quality control: radionuclidic and radiochemical purity, pH, clarity
   ↓
Draw dose into a syringe inside a lead syringe shield
   ↓
Measure in a DOSE CALIBRATOR (must match prescribed activity within limits)
   ↓
Label: patient, radiopharmaceutical, activity (MBq) at stated time,
volume, date, radiation symbol → transport in shielded carrier
   ↓
Record in dispensing register
```

The **dose calibrator** is an ionisation chamber that measures the activity in a syringe or vial; it is checked daily for constancy.

**Worked example 1 – decay and volume.** A vial of Tc-99m preparation contains **800 MBq in 8 mL at 8:00 am**. A patient needs **370 MBq at 11:00 am**. T½ of Tc-99m = 6 h. How many mL should be drawn at 11:00 am?

```text
Decay formula: A = A0 × (1/2)^(t / T½)
t = 3 h, so A = 800 × (1/2)^(3/6) = 800 × (1/2)^0.5 = 800 × 0.707 ≈ 566 MBq
Concentration at 11 am = 566 / 8 ≈ 70.7 MBq/mL
Volume for 370 MBq = 370 / 70.7 ≈ 5.2 mL
(Check: at 2:00 pm, after one half-life, only 400 MBq would remain.)
```

## 7.5 Disposal of radiopharmaceutical waste

| Method | Used for |
| --- | --- |
| **Decay-in-storage** | Short-lived waste (Tc-99m, F-18): kept in shielded, labelled containers for about **10 half-lives** (activity falls to about 1/1000), checked with a survey meter to be at background, radiation labels removed, then disposed of as ordinary or bio-medical waste |
| **Return to supplier** | Used generators and long-lived sources |
| **Controlled release** | Very low-activity liquid waste and patient excreta, only within limits set by the regulator |
| **Disposal through authorised agency** | Long-lived waste as directed by AERB |

Example: Tc-99m waste (T½ 6 h) needs about 60 hours (2.5 days) of storage; I-131 waste (T½ 8 days) needs about 80 days. Patients treated with high-dose I-131 may be admitted in shielded isolation rooms with special toilets until their activity falls.

Records of disposal (date, nuclide, estimated activity, method) are kept for inspection.

## Part B – Computers in hospital pharmacy

## 7.6 Applications of computers in hospital pharmacy practice

| Area | How the computer helps |
| --- | --- |
| **Prescription processing** | Receipt of electronic orders, label printing, dose and interaction checks, duplicate-therapy alerts |
| **Patient medication profile** | Complete record of current and past drugs, allergies, weight, renal function |
| **Inventory control** | Real-time stock, automatic reorder alerts at reorder level, expiry alerts (FEFO), ABC/VED reports, consumption analysis |
| **Purchase** | Indents, purchase orders, supplier records, e-tender, GRN entry |
| **Billing and accounts** | Patient charging per dose, insurance claims, ward-wise cost |
| **Drug distribution** | Unit-dose fill lists, automated dispensing cabinets, barcode checking |
| **Drug information** | Electronic databases and references (drug monographs, interaction checkers, IV compatibility, poison data) |
| **Clinical services** | Pharmacokinetic dose calculations, TPN calculations, renal dose adjustment, clinical decision support |
| **Pharmacovigilance** | ADR reporting forms and online submission; error reporting |
| **Narcotic control** | Electronic registers with balance and audit trail |
| **Education and administration** | Formulary on intranet, staff rosters, reports for committees and accreditation |

**Advantages:** speed, accuracy, legible labels, instant information, fewer errors, better stock control, easy reports and audits, less paperwork.

**Disadvantages / problems:** cost of hardware, software and training; system failure or power failure (need back-up and manual system); data security and privacy; alert fatigue (too many warnings ignored); wrong data entry gives wrong output.

## 7.7 Computerised prescriber order entry and decision support

- **CPOE (computerised prescriber order entry):** doctors enter orders directly into the system → no illegible handwriting or transcription errors; orders reach the pharmacy instantly.
- **CDSS (clinical decision support system):** software that checks orders against patient data and gives alerts – drug allergy, interaction, dose range, renal dose, duplicate therapy, pregnancy warnings.
- **Barcoding:** used at receipt, dispensing and administration (BCMA) to confirm the right product and patient.

## 7.8 Electronic health records (EHR)

An **electronic health record** is a digital, longitudinal record of a person's health information – demographics, history, diagnoses, medications, allergies, laboratory and imaging results, immunisations, progress notes and discharge summaries – that can be shared securely among authorised health providers and over time.

| EMR (electronic medical record) | EHR (electronic health record) |
| --- | --- |
| Digital chart of one hospital or clinic | Covers the person's care across many providers |
| Mainly used inside one organisation | Designed to be shared (interoperable) |
| Replaces the paper file | Follows the patient over a lifetime |

**Benefits for pharmacy:** complete medication history and allergy data, accurate medicine reconciliation at admission and discharge, lab values available for dose adjustment, fewer duplicate tests and prescriptions, data for drug use studies.

**Concerns:** privacy and confidentiality, cyber-security, standard formats (interoperability), cost and training, need for consent.

In India, the **Ayushman Bharat Digital Mission (ABDM)** is building a national digital health system in which each person can have an **ABHA (Ayushman Bharat Health Account)** number to link their health records across providers with their consent.

## 7.9 Software used in hospital pharmacy

1. **Hospital Information System (HIS / HMIS)** with a pharmacy module – links registration, wards, laboratory, billing and pharmacy; used in most large hospitals (commercial or in-house software).
2. **e-Hospital** (developed by the National Informatics Centre for government hospitals) – patient registration, OPD, in-patient management, laboratory and pharmacy modules.
3. **Drugs and vaccines supply chain software** used by many states (for example the **e-Aushadhi** platform for the Drugs and Vaccines Distribution Management System) – indents, stock, expiry, transfers between warehouses and facilities.
4. **Pharmacy inventory and billing software** – stock, purchase, sales, GST billing, expiry and reorder reports.
5. **Drug information databases** – electronic versions of standard references, interaction checkers, IV compatibility databases.
6. **Pharmacovigilance tools** – online ADR reporting to the national programme.
7. **Spreadsheets** for ABC/VED analysis, TPN and dose calculations, and committee reports.

**Choosing pharmacy software:** covers all pharmacy functions; links with HIS/EHR; easy to use; secure with user log-ins and audit trail; supports barcodes; produces legal registers (NDPS, H1); has vendor support and back-up.

## Remember

- Radiopharmaceutical = drug containing a radionuclide for diagnosis or therapy; Tc-99m (about 6 h) is the main imaging agent, from a Mo-99 generator; I-131 (about 8 days) for thyroid; F-18 FDG (about 110 min) for PET.
- Activity in becquerel (1 mCi = 37 MBq); A = A0 × (1/2)^(t/T½).
- ALARA: time, distance, shielding; AERB licence; RSO; TLD badges.
- Store in lead pots in a hot lab with trefoil sign; dispense after measuring in a dose calibrator; label with activity at a stated time.
- Disposal: decay-in-storage about 10 half-lives, then survey and dispose; generators returned.
- Computers: prescriptions, profiles, inventory, purchase, billing, DI, ADR, narcotics, CPOE + CDSS, barcoding.
- EHR = shareable lifelong digital record (EMR = one organisation's record); ABDM/ABHA in India.
