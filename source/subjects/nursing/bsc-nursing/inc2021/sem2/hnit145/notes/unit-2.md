# Unit 2: Principles of health informatics and information systems in healthcare

This notes file joins two small INC units: **Unit II, Principles of Health Informatics** (4 hours theory, 5 hours lab) and **Unit III, Information Systems in Healthcare** (3 hours theory, 5 hours lab). Unit II explains what health informatics is and why it matters; Unit III explains how information systems are built and used in hospitals.

## 2.1 Definitions

| Term | Meaning |
| --- | --- |
| **Informatics** | The science of how data, information and knowledge are collected, stored, processed, communicated and used |
| **Health informatics** | The use of information science and information and communication technology (ICT) to improve health care, health education, research and health policy |
| **Medical informatics** | Health informatics focused on medical practice (diagnosis, treatment) |
| **Nursing informatics** | A speciality that combines nursing science, computer science and information science to manage and communicate data, information, knowledge and wisdom in nursing practice (the American Nurses Association uses a definition of this kind) |
| **Public health informatics** | Informatics applied to the health of populations: surveillance, disease registries, programme data |
| **Consumer health informatics** | Informatics from the patient's side: health apps, portals, personal health records |

## 2.2 The data–information–knowledge–wisdom (DIKW) pyramid

```text
                 ▲  WISDOM      using knowledge well in a situation
                ▲▲▲            ("this post-op patient may be bleeding;
               ▲▲▲▲▲            call the surgeon and prepare fluids")
              ▲▲▲▲▲▲▲  KNOWLEDGE  patterns and relationships
             ▲▲▲▲▲▲▲▲▲           ("falling BP + rising pulse = shock")
            ▲▲▲▲▲▲▲▲▲▲▲  INFORMATION  data with context
           ▲▲▲▲▲▲▲▲▲▲▲▲▲              ("BP 90/60, pulse 120 at 10 am, day 1 post-op")
          ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲  DATA  raw facts ("90/60", "120")
```

- **Data**: discrete, unorganised facts. Nurses collect huge amounts: vital signs, intake–output, pain scores.
- **Information**: data organised, interpreted and placed in context.
- **Knowledge**: information combined and synthesised so that relationships and patterns are understood.
- **Wisdom**: the appropriate use of knowledge to solve a real patient problem.

Nursing informatics is often explained as moving nurses up this pyramid: from charting data to using knowledge and wisdom for better care.

## 2.3 Need for health informatics

1. **Volume of data**: modern care produces more data than paper can handle.
2. **Patient safety**: illegible handwriting, lost files and transcription errors cause harm.
3. **Continuity of care**: patients move between PHCs, district hospitals and specialists; records must move with them.
4. **Evidence-based practice**: clinicians need quick access to current knowledge.
5. **Rising costs**: duplicate tests and long stays waste money.
6. **Public health**: disease surveillance and national programmes need timely data.
7. **Accountability and quality**: accreditation (NABH), audits and legal cases need complete records.
8. **Patient expectations**: people want online appointments, reports and teleconsultation.

## 2.4 Objectives of health informatics

- Make the right information available to the right person at the right time and place.
- Improve the quality, safety and efficiency of care.
- Support clinical decisions with alerts, reminders and guidelines.
- Allow sharing of records between providers (interoperability).
- Reduce cost and duplication.
- Support education, research and planning.
- Empower patients to take part in their own care.
- Protect the privacy and security of health data.

## 2.5 Limitations and barriers

| Limitation | Explanation |
| --- | --- |
| Cost | Hardware, software licences, maintenance, training |
| Infrastructure | Power cuts, poor internet in rural areas |
| Interoperability | Different systems cannot "talk" to each other |
| Human factors | Resistance to change, low computer literacy, extra workload during the change-over |
| Data quality | "Garbage in, garbage out": wrong or incomplete entries give wrong decisions |
| Privacy and security | Hacking, ransomware, unauthorised viewing |
| Over-reliance | Alert fatigue; trusting the screen over the patient |
| Loss of the human touch | Looking at the screen instead of the patient |
| Legal and ethical issues | Ownership of data, consent, liability for software errors |

## 2.6 Using data, information and knowledge for better health

| Level | Example of use |
| --- | --- |
| Individual patient | Trend charts of vital signs warn of deterioration; allergy alerts prevent reactions |
| Ward/unit | Data on falls or pressure injuries show where to target prevention |
| Hospital | Bed occupancy, infection rates, average length of stay guide planning |
| Population | Immunisation coverage and disease surveillance (e.g. IDSP/IHIP) guide public health action |
| Research | Large data sets reveal which treatments work best |

**Characteristics of good-quality data**: accurate, complete, timely, consistent, relevant, legible/clear, and secure. Nurses are the largest group entering data, so the quality of health data depends greatly on nursing documentation.

## 2.7 What is an information system?

An **information system** is an organised combination of **people, procedures, data, hardware, software and networks** that collects, processes, stores and distributes information to support decisions.

**Components**

```text
   PEOPLE      (users: nurses, doctors, clerks, IT staff)
   PROCEDURES  (policies, workflows, downtime plans)
   DATA        (patient records, codes, results)
   SOFTWARE    (applications, database management system)
   HARDWARE    (computers, servers, devices, scanners)
   NETWORK     (LAN, Wi-Fi, internet, cloud)
```

**Functions**: input (capture) → processing → storage → output (reports, screens) → feedback.

## 2.8 Role of information systems in modern healthcare

- Clinical care: records, orders, results, medication management, alerts.
- Administration: registration, billing, stores, staffing.
- Communication: between departments and with other facilities.
- Decision support: clinical guidelines and reminders.
- Quality and safety: incident reports, audit trails, indicators.
- Planning and policy: summary data for managers and the government.
- Education and research: data for teaching cases and studies.

## 2.9 Architecture of information systems

**Architecture** means how the parts of a system are arranged and connected.

| Architecture | Description | Example |
| --- | --- | --- |
| Centralised (mainframe) | One central computer, users connect through terminals | Older hospital systems |
| Client–server | Data on a central server; user computers (clients) run the program and request data | Most hospital systems in a LAN |
| Web-based / cloud | Accessed through a browser; the system runs on remote servers | Many newer HMIS, e-Hospital |
| Distributed / federated | Data stay in many places but are linked when needed | ABDM, where records stay with each facility and are shared with patient consent |

**Integration approaches**

- **Monolithic (single vendor)**: all modules from one company share one database; easy to integrate but costly and hard to change.
- **Best-of-breed (interfaced)**: different systems for lab, pharmacy, radiology linked by **interface engines** using standards such as **HL7**; flexible but needs strong interoperability.

**Layers of a typical system**

```text
 Presentation layer  →  what the user sees (screens, forms, mobile app)
 Application layer   →  rules and processing (order checks, alerts)
 Data layer          →  database (patients, orders, results)
```

## 2.10 Clinical information system (CIS) and hospital information system (HIS)

### Hospital information system (HIS)

A **comprehensive, integrated information system** designed to manage the **clinical, administrative and financial** aspects of a hospital. It is the umbrella system.

### Clinical information system (CIS)

The part of the HIS that directly supports **patient care**. It holds clinical data used by doctors, nurses and therapists.

| Feature | HIS | CIS |
| --- | --- | --- |
| Scope | Whole hospital: clinical + administrative + financial | Clinical care only |
| Main users | All staff, management, accounts | Doctors, nurses, allied clinicians |
| Examples of modules | Registration, billing, stores, HR, plus all clinical modules | EHR, order entry, results, nursing documentation, medication administration, ICU charting |

**Common clinical subsystems**

| Subsystem | Purpose |
| --- | --- |
| CPOE (computerised provider order entry) | Doctors enter orders electronically; checks for dose range, allergy and duplicates |
| LIS (laboratory information system) | Sample tracking, results, critical-value alerts |
| RIS and PACS | Radiology scheduling and reports; picture archiving and communication system stores images |
| Pharmacy information system | Dispensing, stock, drug interaction checks |
| eMAR / BCMA | Electronic medication administration record with barcode checking at the bedside |
| Nursing information system | Assessment, care plans, nursing notes, staffing (Unit 6) |
| CDSS | Clinical decision support system: alerts, reminders, guidelines (Unit 5) |

## 2.11 Steps in setting up an information system (system life cycle)

1. **Planning**: identify need, form a team that includes nurses.
2. **Analysis**: study current workflow and requirements.
3. **Design**: screens, forms, reports.
4. **Selection/development**: choose or build software.
5. **Testing**: try it with real users.
6. **Training** and **implementation** (go-live): pilot, phased or "big bang".
7. **Evaluation and maintenance**: user feedback, updates, upgrades.

Nurses should be involved at every step because they use the system most.

## 2.12 Nurse's role

- Take part in selecting and testing systems; describe nursing workflow.
- Act as a "super-user" who helps colleagues.
- Enter accurate, complete, timely data; avoid copy-paste.
- Use data to improve care (e.g. fall and pressure-injury rates).
- Protect confidentiality and report security incidents.

## Remember

- Health informatics = information science + ICT applied to health care.
- DIKW: data → information → knowledge → wisdom.
- Barriers: cost, infrastructure, interoperability, human factors, data quality, privacy.
- Components of an information system: people, procedures, data, software, hardware, network.
- HIS covers the whole hospital; CIS covers clinical care only.
- CPOE = electronic orders; LIS = lab; RIS/PACS = radiology and images; BCMA = barcode medication administration.
- Architectures: centralised, client–server, web/cloud, federated.
- Nurses are the largest group of users and should be involved from planning to evaluation.
