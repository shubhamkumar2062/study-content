# Unit 4: Quality management systems

In a pharmaceutical company, quality cannot be "tested into" a product at the end; it has to be built into every step, from the design of the formula to the training of the person who cleans the floor. A **quality management system (QMS)** is the organised set of policies, procedures, responsibilities and records that makes this happen. This unit covers the ideas behind quality (TQM, QbD, Six Sigma), two everyday quality procedures (OOS investigation and change control) and the main standards and certifications (ISO 9000, ISO 14000, NABL, GLP).

## 4.1 Concept of quality

**Quality** can be defined in several ways:

| Source | Definition |
| --- | --- |
| ISO 9000 | Degree to which a set of inherent characteristics of an object fulfils requirements |
| J. M. Juran | Fitness for use |
| P. B. Crosby | Conformance to requirements |
| W. E. Deming | Meeting the needs of the customer, now and in the future, with continual improvement |
| Pharmaceutical (ICH Q6A idea) | Suitability of a drug substance or product for its intended use, including identity, strength and purity |

For a medicine, quality means the right drug, in the right amount, free from contamination and impurities, released as designed, stable until expiry, correctly labelled and packed.

**Related terms**

- **Quality control (QC):** testing and checking of materials and products against specifications (product-oriented, detects defects).
- **Quality assurance (QA):** the total of organised arrangements made to ensure products are of the quality required (process-oriented, prevents defects). QA includes GMP and QC.
- **Quality management:** all activities of overall management that set the quality policy, objectives and responsibilities and implement them through planning, control, assurance and improvement.

```text
Quality management
   └── Quality assurance
          └── Good manufacturing practice
                 └── Quality control
```

**Cost of quality**

| Type | Example |
| --- | --- |
| Prevention cost | Training, validation, supplier qualification |
| Appraisal cost | Testing, inspection, audits |
| Internal failure cost | Rejected batches, rework, investigations |
| External failure cost | Recalls, complaints, legal action, loss of reputation |

Money spent on prevention lowers failure costs.

## 4.2 Total Quality Management (TQM)

**TQM** is a management approach in which everyone in the organisation works continuously to improve processes, products, services and culture, with the aim of long-term customer satisfaction.

**Principles of TQM**

1. **Customer focus:** the customer (patient, doctor, regulator) decides what quality is.
2. **Total employee involvement:** every employee, not just QA, is responsible for quality; teamwork and empowerment.
3. **Process-centred approach:** work is seen as a series of processes with inputs, steps and outputs that can be measured.
4. **Integrated system:** departments are linked; horizontal processes cross departments.
5. **Strategic and systematic approach:** quality is part of the company's plans.
6. **Continual improvement (kaizen):** small, constant improvements.
7. **Fact-based decision making:** decisions from data, not opinion.
8. **Communication:** clear, open communication at all levels.

**The PDCA (Deming) cycle**

```text
        PLAN  →  DO
         ↑        ↓
        ACT  ←  CHECK
Plan: find the problem, set objectives, plan the change
Do: carry out the change on a small scale
Check: measure and compare with the expected result
Act: adopt the change as standard, or start the cycle again
```

**Quality tools used in TQM (the "seven basic tools")**

| Tool | Use |
| --- | --- |
| Check sheet | Simple tally of how often events occur |
| Histogram | Distribution of measurements |
| Pareto chart | Shows the "vital few" causes behind most problems (80/20 idea) |
| Cause-and-effect (fishbone, Ishikawa) diagram | Groups possible causes: man, machine, method, material, measurement, environment |
| Scatter diagram | Relationship between two variables |
| Control chart | Shows whether a process stays within control limits over time |
| Flow chart / stratification | Shows process steps or separates data by source |

**Benefits:** fewer defects and rejects, lower cost, higher productivity, better morale, customer confidence, easier regulatory compliance.

**Barriers:** lack of top-management commitment, poor training, resistance to change, short-term thinking, poor communication.

## 4.3 Quality by Design (QbD)

**Quality by Design** is a systematic approach to development that begins with predefined objectives and emphasises product and process understanding and process control, based on sound science and quality risk management (ICH Q8(R2) definition).

Traditional development fixed the process and tested the product at the end ("quality by testing"). QbD instead builds understanding of how materials and process settings affect quality, so the process can be controlled and improved with confidence.

**Elements of QbD**

| Element | Meaning | Example (immediate-release tablet) |
| --- | --- | --- |
| Quality target product profile (QTPP) | Summary of the quality characteristics the product should have | Oral tablet, 500 mg, immediate release, 2-year shelf life |
| Critical quality attributes (CQAs) | Physical, chemical, biological or microbiological properties that must be within limits | Assay, content uniformity, dissolution, impurities |
| Critical material attributes (CMAs) | Properties of input materials affecting CQAs | API particle size, moisture of excipient |
| Critical process parameters (CPPs) | Process settings affecting CQAs | Granulation water amount, drying temperature, compression force |
| Risk assessment | Links CMAs and CPPs to CQAs (ICH Q9) | FMEA, fishbone |
| Design of experiments (DoE) | Studies several factors together to find their effects and interactions | Factorial design for binder level × water × mixing time |
| Design space | The multidimensional combination of input variables and process parameters shown to assure quality | Range of water 20–30% and drying 50–60 °C giving acceptable dissolution |
| Control strategy | Planned set of controls from product and process understanding | Raw material specs, in-process checks, PAT, release tests |
| Life-cycle management and continual improvement | Monitoring and improving after approval | Trend data, process capability |

```text
QTPP → identify CQAs → risk assessment (link CMAs/CPPs to CQAs)
     → DoE → design space → control strategy → life-cycle management
```

**Process analytical technology (PAT):** tools for real-time measurement during manufacture (for example near-infrared spectroscopy for blend uniformity or moisture), supporting QbD and real-time release.

Related ICH guidelines: Q8(R2) pharmaceutical development, Q9 quality risk management, Q10 pharmaceutical quality system, Q11 development and manufacture of drug substances.

**Benefits of QbD:** better understanding, fewer batch failures, flexibility to move within the design space without a new approval (as accepted by regulators), continual improvement, efficient regulatory review.

## 4.4 Six Sigma concept

**Six Sigma** is a data-driven method to reduce variation and defects in a process. "Sigma" (σ) is the standard deviation. A process working at the six sigma level gives no more than about 3.4 defects per million opportunities (DPMO), allowing for the usual long-term shift of the process mean by 1.5σ.

| Sigma level | Approximate defects per million opportunities |
| --- | --- |
| 3σ | about 66,800 |
| 4σ | about 6,200 |
| 5σ | about 230 |
| 6σ | about 3.4 |

**DMAIC (for improving an existing process)**

| Step | Activity |
| --- | --- |
| Define | Define the problem, customer needs and project goal |
| Measure | Measure current performance, collect data |
| Analyse | Find root causes of defects |
| Improve | Develop and test solutions |
| Control | Hold the gains with control charts, SOPs and training |

**DMADV (for designing a new process):** Define, Measure, Analyse, Design, Verify.

**Roles (belts):** Champion (senior sponsor), Master Black Belt (expert coach), Black Belt (full-time project leader), Green Belt (part-time project member), Yellow Belt (basic awareness).

**Process capability:** Cp and Cpk compare the spread of the process with the specification width; higher values mean a more capable process (Cpk ≥ 1.33 is often taken as capable).

**Lean Six Sigma** combines Six Sigma with lean manufacturing (removing waste: overproduction, waiting, transport, over-processing, inventory, motion, defects).

**Pharmaceutical examples:** reducing tablet weight variation, cutting batch release time, lowering deviation numbers, improving yield.

## 4.5 Out of specification (OOS)

An **OOS result** is a test result that falls outside the specifications or acceptance criteria established in the official compendium, drug master file, approved application or company documents. The US FDA guidance on investigating OOS results (first issued in 2006 and revised since) is the most widely followed reference; check its current version.

Related terms:

- **Out of trend (OOT):** result within specification but different from the usual trend (e.g. in stability data).
- **Out of expectation (OOE):** result unexpected but not outside limits.

**Investigation of OOS results**

```text
OOS result
  → Phase I: laboratory investigation (analyst + supervisor)
       checks: correct method and calculation, instrument calibration and
       suitability, standards and reagents, sample preparation, dilution errors
       ├─ assignable lab error found → invalidate result, correct, retest, CAPA
       └─ no lab error → Phase II
  → Phase II: full-scale investigation (QA-led)
       review of production records, raw materials, process deviations,
       equipment, other batches; retesting/resampling per written SOP
  → conclusion: batch released or rejected → CAPA → report and trend
```

Rules:

1. Results are never discarded without a documented, scientifically justified assignable cause.
2. "Testing into compliance" (retesting until a passing result appears) is not allowed.
3. Averaging must not hide an individual OOS result where the test is meant to measure variability (e.g. content uniformity).
4. Every OOS investigation is documented, completed within a set time and reviewed by QA.
5. Corrective and preventive action (CAPA) is taken and its effectiveness checked.

## 4.6 Change control

**Change control** is a formal system by which qualified persons review proposed or actual changes that might affect the validated status of facilities, systems, equipment or processes, so that the state of control is maintained and the regulators are informed where needed.

Examples of changes: new raw-material supplier, change in formula, batch size, equipment, process parameter, specification, test method, packaging, site, software, SOP.

**Steps**

1. **Change request:** the initiator describes the change, reason and products affected.
2. **Classification:** minor, major or critical, based on effect on quality.
3. **Impact assessment and risk assessment:** by QA, QC, production, engineering, regulatory affairs (validation, stability, regulatory filing needed?).
4. **Approval or rejection:** by QA head (and others as required).
5. **Implementation:** with training, document updates, validation or stability studies as decided.
6. **Regulatory notification:** where the change needs approval or notification (see SUPAC, unit 1; in India, CDSCO).
7. **Verification of effectiveness and closure:** QA confirms the change worked and closes the record.

```text
Request → classify → assess impact/risk → approve → implement (+ validate, train)
        → notify regulator if needed → check effectiveness → close
```

## 4.7 ISO 9000 series of quality system standards

**ISO** is the International Organization for Standardization, Geneva. The **ISO 9000 family** gives requirements and guidance for quality management systems in any organisation.

| Standard | Content |
| --- | --- |
| ISO 9000 | Fundamentals and vocabulary of quality management |
| ISO 9001 | Requirements for a QMS; the only one in the family used for certification (the 2015 edition has been the current one; check iso.org for any newer edition) |
| ISO 9004 | Guidance for sustained success of an organisation |
| ISO 19011 | Guidelines for auditing management systems |

**Seven quality management principles (basis of ISO 9001)**

1. Customer focus.
2. Leadership.
3. Engagement of people.
4. Process approach.
5. Improvement.
6. Evidence-based decision making.
7. Relationship management (with suppliers and partners).

**Main clauses of ISO 9001 (high-level structure):** context of the organisation, leadership, planning (including risk-based thinking), support (resources, competence, documented information), operation, performance evaluation (monitoring, internal audit, management review), improvement (nonconformity, corrective action, continual improvement).

**Certification process:** gap analysis → documentation (quality policy, objectives, procedures) → implementation and training → internal audit → management review → certification audit by an accredited certification body → certificate (valid for a fixed period, with surveillance audits).

**ISO 9001 and GMP:** ISO 9001 is general and voluntary; GMP (Schedule M in India, WHO GMP, US cGMP) is product-specific and legally required. ICH Q10 (pharmaceutical quality system) is built on ISO quality concepts and adds GMP.

## 4.8 ISO 14000 (environmental management)

The **ISO 14000 family** deals with environmental management, helping organisations reduce their harmful effects on the environment and comply with laws.

- **ISO 14001:** requirements for an environmental management system (EMS); used for certification.
- Other members cover guidance, environmental auditing, labelling, life-cycle assessment and greenhouse-gas accounting.

**EMS elements (PDCA based):** environmental policy; planning (environmental aspects and impacts such as solvent emissions, effluent, hazardous waste, energy use; legal requirements; objectives); implementation (resources, training, communication, documentation, operational control, emergency preparedness); checking (monitoring, audits, corrective action); management review.

**Relevance to pharma:** treatment of effluents containing APIs and solvents, solvent recovery, safe disposal of expired and rejected drugs, energy saving, reduced packaging waste, and compliance with pollution control boards.

## 4.9 NABL

**NABL** is the **National Accreditation Board for Testing and Calibration Laboratories**, India. It is a constituent board of the **Quality Council of India (QCI)**. It gives third-party assessment and accreditation of laboratories.

- Testing and calibration laboratories are accredited against **ISO/IEC 17025** (general requirements for the competence of testing and calibration laboratories).
- Medical (clinical) laboratories are accredited against **ISO 15189**.
- It also accredits proficiency-testing providers and reference material producers under the relevant ISO standards.

**Benefits for a pharmaceutical testing laboratory:** recognised technical competence, wider acceptance of test reports (including abroad, through international mutual recognition arrangements), better internal quality, customer confidence.

**Accreditation steps:** application with quality manual → document review → pre-assessment (optional) → on-site assessment by assessors → corrective action → accreditation → surveillance and reassessment.

Note the difference: **certification** (ISO 9001) says a system meets a standard; **accreditation** (NABL, ISO/IEC 17025) recognises technical competence to give valid results.

## 4.10 Good Laboratory Practice (GLP)

**GLP** is a quality system concerned with the organisational process and conditions under which non-clinical health and environmental safety studies are planned, performed, monitored, recorded, archived and reported. It ensures that safety data submitted to regulators are reliable and traceable.

**Background:** introduced after cases of poor and falsified animal toxicity data in the 1970s. The US FDA issued GLP regulations (21 CFR Part 58) in 1978; the OECD Principles of GLP (revised 1997–98) are the international standard. In India, the **National GLP Compliance Monitoring Authority (NGCMA)** under the Department of Science and Technology certifies test facilities. Separately, **Schedule L-1** of the Drugs Rules sets good laboratory practice requirements for drug quality-control laboratories.

**Key elements of GLP (OECD principles)**

1. **Test facility organisation and personnel:** management responsibilities, a study director for each study, qualified and trained staff.
2. **Quality assurance programme:** an independent QA unit inspects studies and audits reports.
3. **Facilities:** suitable rooms for test systems (animals), test items, archives and waste.
4. **Apparatus, materials and reagents:** calibrated, maintained, labelled.
5. **Test systems:** proper care, identification and housing of animals or other systems.
6. **Test and reference items:** receipt, characterisation, storage and handling records.
7. **Standard operating procedures** for all routine work.
8. **Performance of the study:** written study plan (protocol) approved by the study director; raw data recorded promptly and accurately.
9. **Reporting of results:** final report signed by the study director, with QA statement.
10. **Storage and retention of records and materials** in archives.

GLP is about how a study is organised and recorded, not about whether its scientific conclusion is right.

## Remember

- Quality: fitness for use (Juran), conformance to requirements (Crosby); QM ⊃ QA ⊃ GMP ⊃ QC.
- TQM: customer focus, everyone involved, process approach, continual improvement, data-based decisions; PDCA cycle; seven basic tools (fishbone, Pareto, control chart …).
- QbD (ICH Q8(R2)): QTPP → CQA → risk assessment (Q9) → DoE → design space → control strategy → life cycle; PAT; Q10 quality system.
- Six Sigma: about 3.4 DPMO; DMAIC (Define, Measure, Analyse, Improve, Control); DMADV for new processes; belts.
- OOS: Phase I lab investigation → Phase II full investigation; no testing into compliance; CAPA.
- Change control: request → classify → assess → approve → implement → notify → verify → close.
- ISO 9000 (vocabulary), ISO 9001 (requirements, certification), ISO 9004, ISO 19011; seven QM principles.
- ISO 14001 = environmental management system.
- NABL (under QCI) accredits labs to ISO/IEC 17025 (testing/calibration) and ISO 15189 (medical).
- GLP: non-clinical safety studies; OECD principles, 21 CFR 58 (1978), NGCMA in India; study director and QA unit; Schedule L-1 for QC labs.
