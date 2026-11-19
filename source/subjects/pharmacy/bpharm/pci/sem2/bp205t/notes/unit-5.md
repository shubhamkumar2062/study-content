# Unit 5: Computers as data analysis in preclinical development

Before a new drug can be given to people, it goes through **preclinical development**: laboratory and animal studies of its chemistry, formulation, stability, pharmacology, pharmacokinetics and toxicity. These studies produce very large amounts of data, and regulators must be able to trust every number. This unit covers the three computer systems named in the syllabus: the **chromatography data system (CDS)**, the **laboratory information management system (LIMS)** and the **text information management system (TIMS)**, together with the data-integrity rules they must follow.

## 5.1 Preclinical development and the need for computers

| Preclinical activity | Data produced |
| --- | --- |
| Characterisation of the drug substance | Spectra, chromatograms, impurity profiles |
| Formulation development | Dissolution profiles, content uniformity, physical tests |
| Stability studies | Assay and impurity results at many time points and storage conditions |
| Bioanalysis | Drug levels in plasma of test animals (LC–MS/MS, HPLC) |
| Pharmacology and toxicology | Doses, observations, body weights, clinical pathology, histopathology |
| Reports and submissions | Study protocols, final reports, summaries for the regulator |

**Why computers are needed**

- The volume of data is too large for paper notebooks.
- Calculations (peak areas, calibration curves, statistics) must be accurate and repeatable.
- Results must be **traceable**: who did what, when, on which instrument.
- Studies must follow **Good Laboratory Practice (GLP)**, under which raw data, records and reports are kept so the study can be reconstructed later.
- Data must be ready to submit to regulators and easy to retrieve years later.

### Data integrity: ALCOA

Regulators expect computerised records to be **ALCOA** (often extended to ALCOA+):

| Letter | Meaning |
| --- | --- |
| A — Attributable | Each entry shows who made it and when |
| L — Legible | Readable and permanent |
| C — Contemporaneous | Recorded at the time the work is done |
| O — Original | The first record (or a verified true copy) is kept |
| A — Accurate | Correct and free of errors; changes are explained |
| "+" | Complete, consistent, enduring and available |

In the USA, **21 CFR Part 11** sets the rules for electronic records and electronic signatures; laboratories that supply data for global submissions design their systems to meet it. Key features required: unique user logins, **audit trails** (a secure, time-stamped record of every creation, change and deletion with the reason), electronic signatures, access control, validation of the software, and secure backup and archiving.

## 5.2 Chromatographic data system (CDS)

**Chromatography** (HPLC, GC, UPLC, LC–MS) is the most used analytical technique in pharmaceutical analysis: assay, related substances, dissolution, stability and bioanalysis. The detector gives an electrical signal over time; a **chromatography data system** is the software that **controls the instrument and collects, processes, stores and reports** these data.

### Functions of a CDS

```text
 Instrument control  →  Data acquisition  →  Processing  →  Reporting  →  Storage / review
 (pump flow, oven       (signal vs time      (peak detection,  (results,     (secure database,
  temperature,           stored as raw        integration,      system        audit trail,
  injection sequence)    data file)           calibration)      suitability)  approval)
```

1. **Instrument control** — sets flow rate, gradient, column temperature, detector wavelength and injection volume; runs a **sequence** of standards and samples automatically, overnight if needed.
2. **Data acquisition** — records the detector signal against time and stores it as an unchangeable raw-data file.
3. **Peak detection and integration** — finds where each peak starts and ends, draws the baseline and calculates **retention time**, **peak area** and **peak height**. Integration parameters (threshold, peak width) are set in a processing method; manual integration is allowed only with justification and is recorded in the audit trail.
4. **Calibration and calculation** — builds a calibration curve from standards (external or internal standard method), calculates concentrations, % assay, % impurities and % dissolved.
5. **System suitability** — calculates theoretical plates (column efficiency), tailing factor, resolution between peaks and % RSD of replicate injections, and checks them against limits before results are accepted.
6. **Reporting** — prints or exports results with chromatograms, summary tables and pass/fail against specifications.
7. **Review and approval** — results are reviewed and signed electronically by an analyst and a reviewer.
8. **Security and compliance** — user roles, password control, audit trail, prevention of deleting or overwriting raw data, and archiving.

**Networked CDS:** in large laboratories, many instruments connect to a central server, so data are stored centrally and reviewers can work from any desk. Common commercial CDS products include Empower (Waters), Chromeleon (Thermo Fisher) and OpenLab (Agilent).

### Advantages of a CDS

- Accurate, reproducible integration and calculations; no manual errors in reading charts.
- Unattended operation of long sequences saves time.
- Raw data and every change are traceable (audit trail) — essential in GLP and GMP inspections.
- Quick comparison of chromatograms, trend analysis and easy retrieval of old data.
- Results can be passed electronically to a LIMS.

## 5.3 Laboratory information management system (LIMS)

A **LIMS** is software that manages the **samples, tests, results, people and instruments** of a laboratory and the **workflow** that links them. Where a CDS handles data from one type of instrument, a LIMS manages the whole laboratory's operations.

### Sample life cycle in a LIMS

```text
 Sample login        →  Labelling     →  Test assignment  →  Analysis   →  Result entry
 (registered with        (barcode)       (tests from the     (on the       (manual, or directly
  unique ID, source,                      specification;       instrument)   from instruments/CDS)
  batch, date)                            work given to analyst)
        →  Calculation and check against specification  →  Review and approval
        →  Report / certificate of analysis  →  Storage, archive and disposal of the sample
```

### Functions

| Function | Description |
| --- | --- |
| Sample management | Registration, barcode labels, location tracking, chain of custody |
| Test and specification management | Stores test methods and limits for each product; flags out-of-specification (OOS) results automatically |
| Workload and scheduling | Assigns work to analysts and instruments, shows pending tests and due dates |
| Instrument integration | Takes results directly from balances, pH meters, CDS and other instruments |
| Stability study management | Plans pull points (e.g. 0, 3, 6, 9, 12 months) under each storage condition, reminds when samples are due, trends results |
| Inventory | Reference standards, reagents, columns, with expiry dates |
| Instrument management | Calibration and maintenance schedules; blocks use of an out-of-calibration instrument |
| Quality records | Deviations, OOS investigations, training records of analysts |
| Reporting | Certificates of analysis, trend charts, management reports |
| Compliance | Audit trail, electronic signatures, user access levels (21 CFR Part 11, GLP/GMP) |

### Advantages of a LIMS

- Less paperwork and fewer transcription errors.
- Faster turnaround time and better use of analysts and instruments.
- Full traceability of each sample and result; easy audits.
- Automatic checking against limits and quick detection of trends.
- Data shared with other company systems (ERP for batch release, document systems).

**Limitations:** high cost, time to configure and validate, staff training, and dependence on the system (downtime procedures needed). Examples of commercial LIMS include LabWare, STARLIMS and LabVantage.

### CDS vs LIMS

| CDS | LIMS |
| --- | --- |
| Handles chromatography instruments and their data | Handles the whole laboratory's samples, tests and workflow |
| Raw data: signals, chromatograms, peak areas | Results, specifications, sample status, reports |
| Focus on acquisition and processing | Focus on management, tracking and reporting |
| Sends final results to the LIMS | Receives results from the CDS and other instruments |

## 5.4 Text information management system (TIMS)

Much of the information in drug development is **unstructured text**, not numbers in tables: study protocols, laboratory reports, standard operating procedures (SOPs), literature articles, regulatory documents, correspondence and scientists' notes. A **text information management system** stores, organises, indexes and retrieves such text documents.

### Functions

1. **Capture and storage** — documents entered in electronic form or scanned (with optical character recognition to make scanned text searchable).
2. **Indexing** — each document is tagged with keywords and details (title, author, date, study number, compound, document type) so it can be found later.
3. **Full-text search and retrieval** — searching inside documents by words or phrases, with Boolean operators, filters and ranking.
4. **Version control** — keeps every version of a document (draft, reviewed, approved, superseded) so only the current approved version is used.
5. **Workflow** — routes documents for review and approval with electronic signatures.
6. **Security** — access only to authorised users; audit trail of who viewed or changed a document.
7. **Text mining** — software that reads large collections of text (such as published literature or adverse event narratives) to find patterns, for example new drug–side-effect associations or links between genes and diseases.
8. **Archiving** — long-term secure storage, as GLP requires study records to be retained.

### Uses in preclinical development

- Managing study protocols, amendments and final reports of toxicology and pharmacology studies.
- Keeping SOPs, specifications and test methods under document control.
- Literature searching and storing references for the drug.
- Preparing regulatory documents by reusing approved text.
- Searching past reports to avoid repeating experiments.

**Related systems:** **electronic laboratory notebooks (ELN)**, which replace paper lab notebooks, and **document management systems (DMS)** used for SOPs and regulatory dossiers. Together with CDS and LIMS they make up the paperless laboratory.

```text
                ┌──────────────────────────────────────────┐
                │   Preclinical data analysis by computers  │
                └──────────────────────────────────────────┘
       ┌──────────────────┬──────────────────────┬────────────────────┐
       ▼                  ▼                      ▼                    ▼
     CDS                LIMS                   TIMS               ELN / DMS
 chromatography     samples, tests,       text documents:      experiments,
 raw data and       results, workflow,    protocols, reports,  SOPs and
 calculations       stability, CoA        SOPs, literature     controlled docs
       └──────── results flow ──────►┘
```

## 5.5 Other computer tools in preclinical data analysis

- **Statistical software** (SAS, R, SPSS, GraphPad Prism) — analysing dose–response, comparing treated and control animal groups, calculating LD50 or ED50 and confidence intervals.
- **Pharmacokinetic software** — calculating AUC, Cmax and half-life in animal studies to choose doses for first-in-human trials.
- **Toxicology data systems** — recording animal observations, body weights and pathology findings directly at the bench.
- **Standard electronic formats** for submitting non-clinical study data to regulators (such as the SEND standard used by the US FDA).

## Remember

- Preclinical studies follow GLP; computer records must be ALCOA (attributable, legible, contemporaneous, original, accurate).
- Part 11 features: unique logins, audit trail, electronic signatures, validation, secure backup.
- CDS: instrument control → acquisition → peak integration → calibration and calculation → system suitability → report → secure storage.
- LIMS: sample login, barcodes, test assignment, instrument interface, OOS flags, stability scheduling, certificates of analysis, audit trail.
- TIMS: stores, indexes and searches unstructured text (protocols, reports, SOPs, literature); version control; text mining.
- CDS feeds results to LIMS; TIMS, ELN and DMS handle the documents.
