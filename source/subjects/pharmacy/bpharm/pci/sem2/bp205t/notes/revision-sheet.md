# Last-night revision sheet

If you only have an hour, learn these six topics well: **number system conversions with 1's and 2's complement subtraction**, **DFD symbols and the SDLC**, **HTML vs XML with a sample page**, **database terms and MS Access objects**, **applications of computers in hospital pharmacy (e-prescribing, barcodes, automated dispensing)**, and **bioinformatics databases with reverse vaccinology**. Add CDS and LIMS for unit 5. Together they cover most long answers.

## Unit 1 — number systems

| From → to | Method |
| --- | --- |
| Decimal → binary/octal/hex | Divide by 2/8/16, remainders read bottom to top |
| Decimal fraction → binary | Multiply by 2, whole parts read top to bottom |
| Any base → decimal | Digit × place value, then add |
| Octal ↔ binary | 1 octal digit = 3 bits |
| Hex ↔ binary | 1 hex digit = 4 bits (A=10 … F=15) |
| Octal ↔ hex | Go through binary |

Ready examples: 25 = 11001₂; 45 = 101101₂; 156 = 234₈; 2470 = 9A6₁₆; 357₈ = 11101111₂ = 239; 10111010₂ = BA₁₆ = 186; 0.625 = 0.101₂.

| Operation | Rule |
| --- | --- |
| Addition | 1 + 1 = 0 carry 1; 1 + 1 + 1 = 1 carry 1 |
| 1's complement | Invert every bit |
| 2's complement | 1's complement + 1 |
| A − B by 1's complement | A + 1's comp(B); carry → add it back (end-around), positive; no carry → negative, take 1's comp of sum |
| A − B by 2's complement | A + 2's comp(B); carry → discard, positive; no carry → negative, take 2's comp of sum |
| Multiplication | Shift and add (1011 × 101 = 110111, i.e. 11 × 5 = 55) |
| Division | Long division (110110 ÷ 110 = 1001, i.e. 54 ÷ 6 = 9) |

## Unit 1 — information systems

- Data = raw facts; information = processed, meaningful data. IS = people + hardware + software + data + procedures + network.
- Information gathering: interviews, questionnaires, observation, record review, JAD, prototyping.
- Requirements: functional and non-functional → SRS document.
- Feasibility (TELOS): technical, economic, legal, operational, schedule.
- DFD: external entity (square), process (circle/rounded box), data store (open box), data flow (arrow). Context diagram = level 0.
- Process specification: structured English, decision table, decision tree, pseudocode.
- Input design: validation (range, type, presence, format, lookup). Output: screens, reports, labels, alerts.
- SDLC: planning → feasibility → analysis → design → coding → testing → implementation → maintenance. Changeover: direct, parallel, pilot, phased.
- Project management: scope, work breakdown, Gantt chart, PERT/CPM, critical path, risk, monitoring.

## Unit 2 — web and databases

| Item | One-line answer |
| --- | --- |
| HTML | Markup language for page structure; predefined tags; `<html><head><title><body>` |
| XML | Stores/carries data; user-defined, case-sensitive tags; one root element; must be well-formed |
| CSS | Style of pages; `selector {property: value;}`; inline, internal, external |
| Languages | Machine → assembly → high-level → 4GL (SQL) → 5GL; compiler (whole program) vs interpreter (line by line) |
| Web servers | Apache, Nginx, IIS, Tomcat; server products: database, application, mail, proxy, DNS servers |
| DBMS | Software to create and manage databases; less redundancy, consistency, security, integrity, sharing, backup |
| Keys | Primary key = unique, not blank; foreign key = refers to another table's primary key |
| SQL | DDL (CREATE, ALTER, DROP), DML (INSERT, SELECT, UPDATE, DELETE), DCL (GRANT, REVOKE) |
| MySQL | Open-source client–server RDBMS (Oracle-owned); many users; used behind websites |
| MS Access | Desktop RDBMS in Office; objects: tables, queries, forms, reports, macros, modules; `.accdb` |
| Drug databases | NFI, Indian drug indexes, DrugBank, PubChem, Micromedex, PubMed |

## Unit 3 — applications

- Drug information: tertiary → secondary → primary sources; Boolean AND/OR/NOT; document every query.
- Pharmacokinetics: AUC (trapezoidal), Cmax, tmax, k, t½ = 0.693/k, clearance, Vd; model fitting; simulation; TDM (digoxin, aminoglycosides, phenytoin, lithium, vancomycin).
- Drug design: QSAR (Hansch — π lipophilicity, σ electronic, Es steric), molecular mechanics, docking, virtual screening, pharmacophore, ADMET, Lipinski's rule of five.
- Hospital pharmacy: inventory, unit-dose dispensing, patient profiles, interaction alerts, ADR reporting.
- EP systems (CPOE): legible, complete orders + automatic checks; e-discharge for continuity of care.
- Barcode medication administration: scan wristband + medicine → checks right patient, drug, dose, route, time.
- Automated dispensing cabinets and robots: fewer picking errors, controlled-drug audit trail.
- Adherence: SMS/app reminders, electronic pill caps, smart pill boxes, video-observed therapy.
- Diagnostic (expert systems, imaging aid), lab-diagnostic (LIS, analyser interface), patient monitoring (ECG, BP, SpO2, alarms, central station), pharma information system (R&D, regulatory, manufacturing, QC, sales).

## Unit 4 — bioinformatics

- Definition: computers + mathematics applied to biological sequence and structure data.
- Central dogma DNA → RNA → protein; alignment pairwise/multiple, global (Needleman–Wunsch)/local (Smith–Waterman); BLAST.
- Primary databases: GenBank (NCBI, USA), ENA (EMBL–EBI, UK), DDBJ (Japan) = INSDC; PDB (structures). Secondary: PROSITE, Pfam. UniProt = Swiss-Prot (reviewed) + TrEMBL.
- Specialised: KEGG, OMIM, DrugBank, IEDB. Literature: PubMed.
- Vaccines: reverse vaccinology (genome → predicted surface antigens → test; meningococcus B), epitope prediction, strain comparison (influenza), rapid genome sharing (COVID-19 mRNA vaccines), structure-based antigen design.

## Unit 5 — preclinical data

- GLP + ALCOA (attributable, legible, contemporaneous, original, accurate); audit trail, e-signatures, validation (21 CFR Part 11).
- CDS: control → acquire → integrate peaks → calibrate/calculate → system suitability (plates, tailing, resolution, %RSD) → report → secure storage.
- LIMS: sample login, barcode, test assignment, instrument interface, OOS flag, stability pull points, CoA, inventory, calibration records.
- TIMS: store, index, full-text search and version-control text documents (protocols, reports, SOPs, literature); text mining. Related: ELN, DMS.

## Full forms to know

DBMS, RDBMS, SQL, HTML, XML, CSS, URL, HTTP(S), DFD, SDLC, SRS, PERT, CPM, CPOE, BCMA, ADC, TDM, QSAR, CADD, ADMET, LIS, HIS, ERP, BLAST, NCBI, EMBL, DDBJ, PDB, CDS, LIMS, TIMS, ELN, GLP, OOS, CoA.
