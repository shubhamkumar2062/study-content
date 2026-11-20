# Unit 4: Patient safety and clinical risk

This unit covers INC Unit V, **Patient Safety & Clinical Risk** (3 hours theory). It explains how informatics can make care safer, how it can also create new risks, and how the risk management process works in a hospital.

## 4.1 Key terms

| Term | Meaning |
| --- | --- |
| **Patient safety** | Preventing errors and adverse effects to patients associated with health care; reducing the risk of unnecessary harm to an acceptable minimum |
| **Error** | Failure of a planned action to be completed as intended, or use of a wrong plan |
| **Adverse event** | An incident that results in harm to a patient |
| **Near miss** | An incident that did not reach the patient, or reached the patient without harm (e.g. a wrong medicine is picked but noticed before giving) |
| **Sentinel event** | An unexpected event causing death or serious physical or psychological injury, which needs immediate investigation (e.g. wrong-site surgery, infant abduction) |
| **Risk** | The chance that something harmful will happen, combined with how serious the harm would be |
| **Clinical risk management** | Identifying, assessing and reducing risks to patients, staff and the organisation |
| **Hazard** | Anything that can cause harm (a wet floor, a look-alike medicine, a confusing screen) |

World Patient Safety Day is observed on **17 September**. The WHO Global Patient Safety Action Plan 2021–2030 aims to eliminate avoidable harm in health care.

## 4.2 Why errors happen: the systems view

Most errors are not caused by one careless person but by weaknesses in the **system**. James Reason's **Swiss cheese model** shows that an organisation has several layers of defence (policies, training, equipment, double checks, alerts); each layer has "holes". Harm happens when the holes line up.

```text
   Hazard ─►  [policy]  [training]  [IT alert]  [double check]  ─► Harm
                 o          o           o            o
          when holes in every layer line up, the error reaches the patient
```

**Active failures** are unsafe acts by people at the bedside; **latent conditions** are hidden weaknesses built into the system (understaffing, poor software design, missing alerts). A "just culture" encourages staff to report errors without fear, while still holding people responsible for reckless behaviour.

## 4.3 Relationship between patient safety and informatics

### How informatics improves safety

| Tool | How it prevents harm |
| --- | --- |
| **CPOE** (computerised provider order entry) | Removes illegible handwriting and transcription; checks dose ranges, allergies, interactions, duplicates |
| **Barcode medication administration (BCMA)** with eMAR | Scanning the wristband and the medicine confirms the five rights: right patient, drug, dose, route and time |
| **Clinical decision support** | Alerts (allergy, drug–drug interaction, critical lab value), reminders (vaccination, repositioning), early-warning scores that flag deterioration |
| **Smart infusion pumps** | A drug library with limits stops dangerous programming |
| **Electronic records** | Complete, legible information; allergy and problem lists visible everywhere |
| **Patient identification** | Barcode or RFID wristbands, photos in the record, two identifiers |
| **Electronic incident reporting** | Easy, often anonymous reporting; trends can be analysed |
| **Lab and radiology systems** | Critical results sent directly to the clinician |
| **Electronic handover tools** | Structured handover (e.g. SBAR) reduces missed information |
| **Telemonitoring** | Remote monitoring of ICU or home patients |
| **Data analysis** | Rates of falls, infections and pressure injuries show where to act |

### How informatics can create new risks (technology-induced errors)

| Risk | Example |
| --- | --- |
| **Wrong-patient selection** | Two patients with similar names open in two windows; a medicine is charted on the wrong one |
| **Alert fatigue** | Too many unimportant alerts; staff click "override" without reading, and miss an important one |
| **Copy-paste (cloning)** | Yesterday's note copied into today's; old or wrong information carried forward |
| **Poor screen design** | Small fonts, drop-down lists where the wrong item is easy to click, units hidden (mg vs mcg) |
| **Workarounds** | Scanning a barcode stuck on the bed rail instead of the patient's wristband |
| **Downtime** | System failure; no access to medication lists or results |
| **Interface errors** | Data lost or changed when passed between systems |
| **Over-reliance** | Trusting a calculated dose without thinking |
| **Security breaches** | Ransomware attacks that shut down hospital systems |

**Safety lessons**: involve nurses in design and testing, keep alerts few and meaningful, display two identifiers on every screen, keep downtime procedures and paper forms ready, report IT-related incidents like any other incident, and use technology as an aid, not a replacement for clinical judgement.

## 4.4 International patient safety goals

Hospital accreditation standards (NABH in India; JCI internationally) emphasise goals such as:

1. Identify patients correctly (at least two identifiers, never the bed number).
2. Improve effective communication (read-back of verbal and telephone orders, critical results).
3. Improve the safety of high-alert medications (concentrated electrolytes, look-alike/sound-alike drugs).
4. Ensure correct-site, correct-procedure, correct-patient surgery (marking, time-out, surgical safety checklist).
5. Reduce the risk of health care-associated infections (hand hygiene).
6. Reduce the risk of patient harm from falls.

Informatics supports each goal: barcode wristbands (1), electronic critical-value alerts (2), drug libraries and tall-man lettering (3), electronic checklists (4), infection surveillance software (5), fall-risk scores with alerts (6).

## 4.5 The risk management process

Risk management is a continuous cycle. A commonly taught version (based on the international standard ISO 31000) has these steps:

```text
     ┌──────────────► 1. Establish the context ───────────────┐
     │                                                        ▼
  7. Monitor and review                              2. Identify risks
     ▲                                                        │
     │                                                        ▼
  6. Treat (control) the risk  ◄── 5. Evaluate ◄── 3–4. Analyse
                                                     (likelihood × severity)
          Communication and consultation run through every step
```

1. **Establish the context**: what area (ward, procedure, system) and what goals.
2. **Identify risks**: incident reports, near misses, complaints, audits, inspections, patient feedback, claims, staff interviews, data trends.
3. **Analyse**: how **likely** is it, and how **severe** would the harm be?
4. **Rate the risk** using a **risk matrix**:

| Likelihood ↓ / Severity → | Minor | Moderate | Major | Catastrophic |
| --- | --- | --- | --- | --- |
| Almost certain | Medium | High | Extreme | Extreme |
| Likely | Medium | High | High | Extreme |
| Possible | Low | Medium | High | Extreme |
| Unlikely | Low | Low | Medium | High |
| Rare | Low | Low | Medium | High |

5. **Evaluate**: compare with what is acceptable; set priorities (extreme and high first).
6. **Treat (control)**: options are to **avoid** the risk (stop the activity), **reduce** it (training, checklists, alerts, redesign), **transfer** it (insurance, outsourcing) or **accept** it (if low and documented).
7. **Monitor and review**: check that controls work; record in a **risk register**; repeat the cycle.

**Communication and consultation** with staff, patients and managers happen at every step.

## 4.6 Tools used in clinical risk management

| Tool | Use |
| --- | --- |
| **Incident reporting system** | Staff report adverse events and near misses (paper or electronic) |
| **Root cause analysis (RCA)** | After an event, asks *what* happened, *why*, and *what system change* will prevent it; uses tools such as **5 Whys** and the **fishbone (Ishikawa) diagram** |
| **Failure mode and effects analysis (FMEA)** | Looks *ahead*: lists each step of a process, how it could fail, the effect, and gives a risk priority number so the worst risks are fixed first |
| **Risk register** | A record of identified risks, their rating, owner and actions |
| **Clinical audit** | Compares practice with standards |
| **Trigger tools** | Search records for "triggers" (e.g. naloxone use) that suggest harm |
| **Morbidity and mortality reviews** | Team review of cases with poor outcomes |

**Fishbone example**: a medication error might have causes under People (fatigue), Methods (no double check), Equipment (pump library out of date), Environment (noise, interruptions), Materials (look-alike packaging) and Software (confusing drop-down).

## 4.7 Health IT risk management

When a hospital brings in new software, it should:

- Do a **risk assessment** before going live (FMEA of key workflows such as medication ordering).
- Test with real users and real-looking data.
- Train all users; give quick-reference guides.
- Keep **downtime procedures** and backups; practise them.
- Set up **access control**, audit trails and cyber-security measures.
- Monitor IT-related incidents after go-live and fix design problems.

## 4.8 Nurse's role

- Use two identifiers and scan wristbands every time.
- Read alerts before overriding; document the reason for an override.
- Never use workarounds; report equipment and software problems.
- Report all incidents and near misses promptly and factually.
- Take part in RCA, FMEA and audits; suggest system fixes.
- Teach patients and families to speak up about their care.

## Remember

- Near miss = no harm or did not reach the patient; adverse event = harm; sentinel event = death or serious harm.
- Swiss cheese model (Reason): errors pass through holes in several defence layers; active failures vs latent conditions.
- Informatics improves safety (CPOE, BCMA, CDSS, smart pumps) but can create risks (wrong patient, alert fatigue, copy-paste, downtime).
- Risk = likelihood × severity; risk matrix gives the priority.
- Risk treatment: avoid, reduce, transfer, accept.
- RCA looks back after an event; FMEA looks ahead at a process.
- World Patient Safety Day: 17 September.
