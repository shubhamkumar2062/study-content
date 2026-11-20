# Unit 3: Shared care and electronic health records

This unit covers INC Unit IV, **Shared Care & Electronic Health Records** (4 hours theory, 4 hours lab). It explains what electronic records are, why it is hard to capture a patient's history in a form a computer can use, and the standards that let records from different systems be joined into one lifelong record. It ends with India's own EHR standards and the Ayushman Bharat Digital Mission (ABDM).

## 3.1 Shared care

**Shared care** means that several professionals and facilities look after one patient over time, for example a diabetic patient seen by an ASHA, a community health officer at an Ayushman Arogya Mandir, a physician at the district hospital and an eye specialist. Shared care works only if every provider can see the same up-to-date information: diagnoses, medicines, allergies, test results and plans. Paper files stay in one place; electronic records can follow the patient.

## 3.2 EMR, EHR and PHR

| Record | Definition | Who controls it | Scope |
| --- | --- | --- | --- |
| **EMR** (electronic medical record) | Digital version of the paper chart in **one** clinic or hospital | That facility | One provider/organisation |
| **EHR** (electronic health record) | A longitudinal record of a person's health information that can be **shared across** facilities | Shared by authorised providers | Many providers, over a lifetime |
| **PHR** (personal health record) | A record **kept and controlled by the person**, who can collect and share their own data | The individual | Whatever the person adds |

```text
   EMR (hospital A) ─┐
   EMR (clinic B)  ──┼──►  EHR: one lifelong record shared with consent
   EMR (lab C)     ──┘                   │
                                         ▼
                              PHR app on the patient's phone
```

**Contents of an EHR**: demographics, problem list, medical and surgical history, allergies, medications, immunisations, vital signs, progress and nursing notes, investigations, imaging, discharge summaries, advance directives, billing and insurance data.

**Advantages**

- Complete, legible information available at the point of care, even in an emergency.
- Fewer duplicate tests and medication errors.
- Better continuity and coordination of care.
- Decision support (alerts, reminders).
- Data for public health, quality and research.
- Patients can see and share their own records.

**Disadvantages**: cost, privacy risk, downtime, documentation burden, alert fatigue, copy-paste errors, and the risk that a wrong entry spreads to every system.

## 3.3 Challenges of capturing rich patient histories in computable form

A **computable** record is one whose data a computer can recognise, compare and use (for alerts, summaries and statistics), not just display.

| Challenge | Explanation and example |
| --- | --- |
| **Free text vs structured data** | A nurse writes "c/o pain abd since 2 days, not taking food well". A human understands; a computer cannot reliably find "abdominal pain, onset 2 days" unless it is entered in structured fields or coded |
| **Richness and nuance** | Social history, the patient's own words, beliefs and context are hard to fit into tick boxes |
| **Ambiguity** | Abbreviations ("MS" = multiple sclerosis, mitral stenosis or morphine sulphate); local language terms; spelling variations |
| **Different terms for one concept** | "Heart attack", "MI", "myocardial infarction": the computer needs one code |
| **Time and change** | Conditions start, change and resolve; medicines are stopped and restarted; the record must keep history, not just the latest value |
| **Uncertainty and negation** | "No history of TB", "suspected dengue" must not be read as a TB or dengue diagnosis |
| **Data from many sources** | Devices, labs, other hospitals, the patient's own app, each in a different format |
| **Clinician time** | Structured entry is slower; too many fields frustrate users |
| **Legacy paper records** | Old notes must be scanned (an image is not computable) or re-entered |
| **Privacy** | Sensitive parts (HIV status, mental health, sexual history) need extra protection |

**Solutions**: structured templates with free-text space, pick-lists, standard clinical terminologies (SNOMED CT, LOINC, ICD), archetypes and templates (openEHR), and natural-language processing software that turns text into codes.

## 3.4 Interoperability

**Interoperability** is the ability of different information systems and devices to **exchange data** and **use the data** that has been exchanged.

| Level | Meaning |
| --- | --- |
| **Foundational (technical)** | Data can be sent from one system to another (connection, transport) |
| **Structural (syntactic)** | The format and structure of the message are standard, so fields arrive in the right place |
| **Semantic** | Both systems understand the **meaning** of the data the same way, using shared codes (SNOMED CT, LOINC) |
| **Organisational** | Policies, consent, trust and workflows allow the exchange to happen |

## 3.5 Global standards for lifelong, integrated EHRs

Standards are agreed rules that allow systems from different vendors to work together.

### Messaging and exchange standards

| Standard | Body | Use |
| --- | --- | --- |
| **HL7 Version 2** | Health Level Seven International | Messages between hospital systems (admission, orders, lab results); the most widely used in hospitals |
| **HL7 Version 3 / CDA** | HL7 | Clinical Document Architecture: XML documents such as discharge summaries |
| **HL7 FHIR** (Fast Healthcare Interoperability Resources) | HL7 | Modern web-based standard; data in small units called **resources** (Patient, Observation, MedicationRequest) exchanged through web APIs; used by apps and national programmes, including ABDM |
| **DICOM** | NEMA | Storing and sending medical images (X-ray, CT, MRI) |
| **IHE profiles** | Integrating the Healthcare Enterprise | Guides to using existing standards together for real workflows |

"Level Seven" refers to the application layer, the seventh layer of the OSI network model.

### Terminology and coding standards

| Standard | Use |
| --- | --- |
| **SNOMED CT** | Comprehensive clinical terminology (findings, procedures, body structures); see Unit 5 |
| **LOINC** | Codes for laboratory tests and clinical observations |
| **ICD (ICD-10, ICD-11)** | WHO classification of diseases for statistics, mortality and billing; ICD-11 came into effect from 1 January 2022 |
| **Nursing terminologies** | NANDA-I, NIC, NOC, Omaha System, ICNP (Unit 5) |

### EHR architecture and content standards

- **openEHR**: separates the stable software from clinical content models called **archetypes** (e.g. "blood pressure") so that content can change without rebuilding software.
- **ISO 13606**: EHR communication standard based on a similar two-level model.
- **ISO 27001 / security standards**: protect information.

### What the standards make possible

A **lifelong EHR** built from many systems: the birth record, immunisations, school health checks, hospital admissions and old-age care all linked to one person through a unique identifier, with consent.

## 3.6 EHR standards in India

- The **Ministry of Health and Family Welfare (MoHFW)** first notified **EHR Standards for India in September 2013** and released a **revised version in December 2016**.
- They recommend standards for identification, data exchange, terminology, imaging and security, including **HL7** messaging and clinical documents, **DICOM** for images, **SNOMED CT** as the primary clinical terminology, **LOINC** for tests and observations, and **ICD-10** for disease classification. They also cover privacy, security, access control and audit trails.
- A **National Resource Centre for EHR Standards (NRCeS)** was set up at **C-DAC, Pune** to help providers and software makers adopt the standards. SNOMED CT has been made available for free use in India.
- Under ABDM, health records are exchanged as **HL7 FHIR** documents built from India-specific FHIR profiles.

## 3.7 Ayushman Bharat Digital Mission (ABDM)

The **Ayushman Bharat Digital Mission** was launched nationwide by the Prime Minister on **27 September 2021**, after a pilot in six Union Territories announced on 15 August 2020. It is implemented by the **National Health Authority (NHA)**. Its aim is a national digital health ecosystem in which records are **federated** (they stay with the facility that created them) and are shared **only with the patient's consent**.

**Building blocks**

| Building block | What it is |
| --- | --- |
| **ABHA number** (Ayushman Bharat Health Account) | A **14-digit** unique health identifier for each person |
| **ABHA address** | A self-chosen, easy-to-remember username such as `name@abdm`, linked to the ABHA number, used to share records |
| **HPR** (Healthcare Professionals Registry) | Registry of verified health professionals of modern and traditional systems, including nurses |
| **HFR** (Health Facility Registry) | Registry of hospitals, clinics, labs, pharmacies and other facilities |
| **Health Information Exchange and Consent Manager (HIE-CM)** | Routes records between facilities after the person gives digital consent; the consent states purpose, which records, and for how long |
| **PHR apps** | Apps where the person sees and stores linked records |
| **Unified Health Interface (UHI)** | An open network for services such as booking appointments and teleconsultation |

```text
  Hospital A (stores its own records)        Lab B (stores its own reports)
          │  links records to ABHA                 │
          └──────────────►  Consent manager  ◄─────┘
                                  ▲
               patient approves   │  request with purpose and time period
                                  │
                       Doctor/nurse at Hospital C
```

**Nurse's role in ABDM**: help patients create and link ABHA at registration, explain consent, use the hospital system to view shared records only for care, register on the HPR when required, and protect the patient's data.

## 3.8 Practical: report on current EHR standards in the Indian setting

A good student report includes: the 2013 and 2016 EHR standards (what they cover), the NRCeS, the ABDM building blocks, which standards the student's hospital system uses (HL7, DICOM, ICD coding in the medical records department), how ABHA is linked at registration, and gaps seen (paper records, systems that do not share data). Take care to confirm current facts on the official websites of MoHFW, NHA/ABDM and NRCeS.

## Remember

- EMR = one facility; EHR = shared, lifelong; PHR = controlled by the person.
- Computable data are structured and coded; free text is hard for computers to use.
- Interoperability levels: foundational, structural, semantic, organisational.
- HL7 v2 = hospital messages; CDA = clinical documents; FHIR = web resources and APIs; DICOM = images.
- SNOMED CT = clinical terms; LOINC = lab tests; ICD = disease classification (ICD-11 from 2022).
- India's EHR standards: 2013, revised 2016; NRCeS at C-DAC Pune.
- ABDM launched 27 September 2021 by NHA; ABHA number = 14 digits; ABHA address = name@abdm.
- HPR = professionals; HFR = facilities; records are shared only with consent.
