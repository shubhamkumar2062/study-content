# Unit 5: Drug store management and inventory control, investigational use of drugs, and interpretation of clinical laboratory tests

This unit brings together **managing the drug store** (organisation, storage, purchase, **EOQ, reorder level** and **ABC/VED analysis**), the safe handling of **investigational drugs** in hospital, and **interpreting common laboratory tests** – blood chemistry, haematology and urinalysis – as monitoring parameters for drug therapy. Inventory control and ABC/VED analysis are frequent long questions; EOQ often comes as a short numerical.

## 5.1 Drug store management

### Organisation of the drug store

The **central (main) drug store** of a hospital receives, stores and issues drugs and medical supplies to the pharmacy and other departments. It is managed by the **chief pharmacist or a pharmacist store-in-charge**, helped by store keepers, clerks and helpers.

```text
 Supplier → Receiving & inspection → Quarantine (if needed) → Main store
      (check against purchase order, batch, expiry,                │
       quantity, condition; goods received note)                    ▼
                                    Issue on indent → Pharmacy / wards / OT / ICU
                                                    │
                                     Stock & issue records (manual or computer)
```

**Functions of the store:** receiving and checking goods, proper storage, **stock records**, issue to user departments, **expiry and stock control**, returns and disposal, and helping in purchase planning.

**Requirements of a good store:** central location with vehicle access, adequate space, racks and pallets (goods kept off the floor and away from walls), protection from heat, light, moisture, rodents and insects, fire safety, security, and good lighting.

### Types of materials stocked

| Category | Examples |
| --- | --- |
| Drugs – oral, parenteral, topical | Tablets, capsules, syrups, injections, ointments |
| Large-volume parenterals | IV fluids |
| Surgical items and dressings | Cotton, gauze, bandages, sutures, gloves, syringes, catheters |
| Biologicals and cold-chain items | Vaccines, insulin, sera, blood products |
| Chemicals and reagents | Disinfectants, laboratory reagents |
| Flammable materials | Alcohol, ether, acetone |
| Controlled drugs | Narcotic and psychotropic drugs, Schedule X drugs |
| Radiopharmaceuticals (in some hospitals) | Stored in shielded areas |
| Medical gases (separately) | Oxygen, nitrous oxide cylinders |

### Storage conditions

| Storage term (pharmacopoeial meaning) | Temperature |
| --- | --- |
| **Cold** (refrigerator) | **2–8 °C** |
| **Cool** | **8–25 °C** |
| Room temperature | Temperature of the working area; for most products **not above 25–30 °C** as stated on the label |
| Frozen | Below 0 °C, as stated on the label |

General storage rules:

1. **Arrange systematically** – by dosage form, then alphabetically by generic name, or by therapeutic class.
2. **First-expiry, first-out (FEFO)** issue; check expiry regularly; segregate expired stock.
3. Protect **light-sensitive** items in amber containers or dark areas; **moisture-sensitive** items with desiccants.
4. **Cold chain** – refrigerators with temperature logs twice daily, alarms, power back-up; never freeze freeze-sensitive vaccines.
5. **Flammables** in a separate, cool, ventilated, fire-proof room.
6. **Controlled drugs** in a double-locked cupboard with a register.
7. **Look-alike, sound-alike** drugs kept apart with warning labels.
8. **Quarantine** area for goods awaiting checks, recalled or damaged items.

## 5.2 Purchase and inventory control

### Inventory control – meaning and objectives

**Inventory** is the stock of materials held for use. **Inventory control** is the **scientific management of stock** so that the **right items are available in the right quantity at the right time at the lowest total cost**.

**Objectives:** no stock-out of needed drugs; minimum capital locked in stock; least expiry, deterioration and pilferage; lower ordering and holding costs; accurate records.

### Principles of purchase

1. Buy **quality** products from **reliable, licensed suppliers**.
2. Buy the **right quantity** at the **right time** – based on consumption and lead time.
3. Get the **best price** – competition, bulk purchase, rate contracts.
4. Prefer **generic** formulary drugs.
5. Follow **transparent procedures** and government rules.

### Purchase procedure

**Methods of purchase:**

| Method | Features |
| --- | --- |
| **Open tender** | Advertised publicly; any qualified supplier may quote; fair and competitive, but slow |
| **Limited (restricted) tender** | Invitations to selected approved suppliers |
| **Single tender** | Only one supplier (patented or proprietary item) |
| **Negotiated purchase** | Price negotiated directly, often for emergency or special items |
| **Rate contract** | Price fixed for a period (often one year); items ordered as needed |
| **Direct (cash) purchase** | Small, urgent purchases |
| **Centralised purchase** | One agency buys for many hospitals (e.g. State medical services corporations) – lower prices |

**Steps:**

```text
 Need identified (indent / reorder level reached)
   → Specifications prepared → Approval of purchase committee
   → Tender / quotation → Comparison and selection of supplier
   → Purchase order issued → Supplier delivers
   → Receipt and inspection (quantity, quality, batch, expiry, documents)
   → Goods received note, entry in stock register → Payment
```

### Purchase order

A **purchase order** is the formal written document from buyer to supplier authorising supply. It contains: **order number and date**, name and address of supplier and buyer, **description of each item** (generic name, strength, dosage form, pack), **quantity**, **unit price and total value**, **delivery date and place**, terms of payment, required **shelf life at delivery**, packing and labelling conditions, and the **signature** of the authorised officer.

### Procurement and stocking

- **Receiving** – check against the purchase order and invoice; physical check for damage; batch number and expiry; quality certificate; cold-chain condition.
- **Recording** – goods received note; entry in stock ledger or computer (bin cards).
- **Stocking** – store at the correct place and condition; label shelves; FEFO.
- **Issue** – against **indents** from departments; issue records; periodic **physical stock verification**.

### Economic order quantity (EOQ)

**EOQ** is the **order size at which the total of ordering cost and inventory carrying (holding) cost is lowest**.

- **Ordering cost** – cost of placing and receiving an order (paperwork, staff time, transport, inspection). More orders → more ordering cost.
- **Carrying cost** – cost of holding stock (capital locked up, storage, insurance, expiry, deterioration, pilferage). Bigger orders → more carrying cost.

```text
 Small orders  → many orders a year  → HIGH ordering cost, LOW carrying cost
 Large orders  → few orders a year   → LOW ordering cost,  HIGH carrying cost
 EOQ           → the order size where ordering cost = carrying cost
                 and the TOTAL cost is lowest
```

**Formula (Wilson's formula):**

```text
 EOQ = √( 2 × A × O / C )

 A = annual demand (units per year)
 O = cost of placing one order (₹)
 C = carrying cost per unit per year (₹)
     (often written as unit price × carrying cost rate)
```

**Worked example:** a hospital uses 4,000 vials of an injection per year; the cost of placing one order is ₹200; the carrying cost is ₹4 per vial per year.

```text
 EOQ = √(2 × 4000 × 200 / 4) = √(400000) ≈ 632 vials per order
 Number of orders per year = 4000 / 632 ≈ 6.3, i.e. about 6 orders
```

Assumptions: steady demand, fixed lead time, constant price, no shortages allowed. In practice EOQ is rounded to pack sizes and adjusted for discounts and shelf life.

### Reorder level and related stock levels

| Level | Meaning | Formula (commonly used) |
| --- | --- | --- |
| **Lead time** | Time from placing an order to receiving the goods | – |
| **Safety (buffer) stock** | Extra stock kept to cover delays or sudden rise in use | (Maximum usage − normal usage) × lead time, or set by policy |
| **Reorder level (ROL)** | Stock level at which a fresh order must be placed | **Maximum usage × maximum lead time**, or **(average usage × lead time) + safety stock** |
| **Reorder quantity** | Quantity ordered each time | Usually the **EOQ** |
| **Minimum level** | Stock should not fall below this | ROL − (normal usage × normal lead time) |
| **Maximum level** | Stock should not rise above this | ROL + reorder quantity − (minimum usage × minimum lead time) |

**Example:** average daily use 20 strips, lead time 10 days, safety stock 100 strips → ROL = (20 × 10) + 100 = **300 strips**; when stock falls to 300, an order of EOQ size is placed.

### Methods used for the analysis of drug expenditure

**1. ABC analysis (Always Better Control)** – based on **annual consumption value** (quantity used × unit cost):

| Class | Share of items | Share of annual expenditure (approx.) | Control |
| --- | --- | --- | --- |
| **A** | About 10–20% | About 70–80% | **Tight control**, frequent orders in small lots, close monitoring, senior officer |
| **B** | About 20–30% | About 15–20% | Moderate control |
| **C** | About 50–70% | About 5–10% | Simple control, bulk orders, fewer checks |

Steps: list items with annual quantity and unit cost → calculate annual value → arrange in descending order → calculate cumulative percentage of value and of items → classify.

**2. VED analysis** – based on **criticality** (importance to patient care):

- **V – Vital**: life-saving drugs whose absence is dangerous (emergency drugs, oxygen, anti-snake venom, adrenaline) – must **never** be out of stock.
- **E – Essential**: drugs for important but not immediately life-threatening needs.
- **D – Desirable**: drugs whose shortage causes little harm.

**3. ABC–VED matrix** – combines cost and criticality into categories I (AV, AE, AD, BV, CV – managed closely), II (BE, CE, BD) and III (CD – least attention). It balances saving money with keeping vital drugs available.

**4. Other analyses:**

| Analysis | Basis |
| --- | --- |
| **FSN** | Movement – Fast-moving, Slow-moving, Non-moving (helps remove dead stock) |
| **SDE** | Availability – Scarce, Difficult, Easy to obtain |
| **HML** | Unit price – High, Medium, Low cost per unit |
| **XYZ** | Value of stock in hand at a given time |
| **VEN** | WHO's Vital, Essential, Non-essential grouping, similar to VED |

**5. Other tools** – drug utilisation review, **therapeutic category analysis** of expenditure, comparison of **cost per patient-day**, defined daily dose (DDD) studies, and **pharmacoeconomic** comparisons of alternatives.

## 5.3 Investigational use of drugs

### Description

An **investigational drug** is a new chemical entity, or an approved drug for a new use, dose, dosage form or route, that is **being studied in clinical trials** and is **not yet approved** for marketing for that use. In India, clinical trials of new drugs are governed by the **New Drugs and Clinical Trials Rules, 2019** (under the Drugs and Cosmetics Act), with approval from the **Central Licensing Authority (DCGI/CDSCO)**.

### Principles involved

1. **Scientific need** and sound study design (protocol).
2. **Ethics** – the **Declaration of Helsinki**, **Good Clinical Practice (GCP)** guidelines, and the **ICMR National Ethical Guidelines** for research on human participants.
3. **Informed consent** – voluntary, written (audio-video recording required in certain cases), in a language the participant understands.
4. **Approval** of the **ethics committee** (registered with the CLA) and of the regulator before starting.
5. **Safety monitoring** – reporting of **serious adverse events** within the prescribed time; compensation for trial-related injury.
6. **Confidentiality** of participants and accurate records.

### Classification (phases of clinical trials)

| Phase | Subjects | Main aim |
| --- | --- | --- |
| **Phase I** | Small number of healthy volunteers (or patients for toxic drugs such as anticancer drugs) | Safety, tolerability, pharmacokinetics, dose range |
| **Phase II** | Small groups of patients | Efficacy (therapeutic exploratory), dose finding, short-term safety |
| **Phase III** | Large numbers of patients, often multicentre, randomised and controlled | Confirm efficacy and safety; basis for marketing approval |
| **Phase IV** | Patients after approval | Post-marketing surveillance – rare ADRs, long-term effects, new uses |

### Control

- Trial conducted only under an **approved protocol** at approved sites by qualified **investigators**.
- Investigational drugs **supplied by the sponsor**, used only for enrolled participants.
- Stored **separately** from regular stock, under the stated conditions, with **restricted access**.
- **Accountability records** for every unit received, dispensed, returned and destroyed.
- Unused drugs **returned to the sponsor** or destroyed as per protocol.
- Monitoring and audits by the sponsor, ethics committee and regulator.

### Identification

Investigational products are **labelled for clinical trial use only**, with protocol number, **code or study number**, batch number, storage conditions, expiry or retest date, and sponsor's name; in **blinded** trials, the label does not show whether the product is active or placebo, and **emergency code-break** arrangements exist.

### Role of the hospital pharmacist

1. Receiving, checking and recording investigational supplies.
2. Proper **storage** (temperature logs), segregation and security.
3. **Dispensing** only on the investigator's written order for enrolled patients; maintaining **randomisation and blinding**.
4. Keeping **drug accountability records** and reconciling stock.
5. Preparing doses (including sterile preparations) as per protocol.
6. Providing **information** on the drug to nurses and doctors (investigator's brochure).
7. Helping detect and report **adverse events**.
8. Serving on the **ethics committee** or PTC; handling returns and destruction.

### Advisory committee

The hospital's **Institutional Ethics Committee (IEC)**, together with the **PTC** and any **research committee**, reviews and approves trials, monitors their conduct, and protects participants. The IEC is multidisciplinary – medical and non-medical members, a legal expert, a social scientist, a lay person – with at least one woman member, and must be **registered** with the regulator under the NDCT Rules.

## 5.4 Interpretation of clinical laboratory tests

Laboratory tests help in **diagnosis, choosing a drug and dose, monitoring effectiveness and detecting toxicity**. Values below are **typical adult reference ranges**; ranges **differ between laboratories, methods, age and sex**, so always read the range printed on the report.

### Blood chemistry

**Glucose**

| Test | Normal | Notes |
| --- | --- | --- |
| Fasting plasma glucose | 70–99 mg/dL | 100–125 impaired fasting glucose; **≥126 mg/dL** suggests diabetes |
| Post-prandial (2-hour) glucose | Below 140 mg/dL | ≥200 mg/dL suggests diabetes |
| HbA1c | Below 5.7% | 5.7–6.4% prediabetes; **≥6.5%** diabetes; reflects average glucose over about 2–3 months |

**Kidney function tests**

| Test | Typical range | Raised in / significance |
| --- | --- | --- |
| Serum creatinine | About 0.6–1.2 mg/dL | Renal failure, dehydration; used to estimate creatinine clearance for dose adjustment |
| Blood urea | About 15–40 mg/dL (BUN about 7–20 mg/dL) | Renal failure, dehydration, GI bleeding, high protein intake |
| Serum uric acid | About 3–7 mg/dL | Gout, thiazide diuretics, tumour lysis |

**Electrolytes**

| Test | Typical range | Drug relevance |
| --- | --- | --- |
| Sodium | 135–145 mEq/L | Low with thiazides, SSRIs, carbamazepine (hyponatraemia) |
| Potassium | 3.5–5.0 mEq/L | Low with loop/thiazide diuretics (raises digoxin toxicity); high with ACE inhibitors, potassium-sparing diuretics, renal failure |
| Chloride | About 98–106 mEq/L | Acid–base disorders |
| Bicarbonate | About 22–28 mEq/L | Low in metabolic acidosis |
| Calcium | About 8.5–10.5 mg/dL | Interpret with albumin |

**Liver function tests (LFTs)**

| Test | Typical range | Significance |
| --- | --- | --- |
| Total bilirubin | About 0.3–1.2 mg/dL | Raised in jaundice (haemolytic, hepatic, obstructive) |
| ALT (SGPT) | Up to about 40 U/L | More **liver-specific**; raised in hepatitis and drug-induced liver injury (e.g. isoniazid, paracetamol overdose) |
| AST (SGOT) | Up to about 40 U/L | Liver, heart and muscle damage |
| Alkaline phosphatase | About 40–130 U/L | Raised in cholestasis and bone disease |
| Total protein / albumin | 6–8 g/dL / 3.5–5.0 g/dL | Low albumin in liver disease, malnutrition – more free drug for highly bound drugs (e.g. phenytoin) |

**Lipid profile** (desirable): total cholesterol below 200 mg/dL; LDL-cholesterol below 100 mg/dL; HDL-cholesterol above 40 mg/dL in men and above 50 mg/dL in women; triglycerides below 150 mg/dL. Used to start and monitor statin therapy.

**Cardiac markers** – **troponin I/T** (most specific for myocardial injury) and **CK-MB** rise after myocardial infarction. **Serum amylase and lipase** rise in acute pancreatitis.

### Haematology

| Test | Typical adult range | Significance |
| --- | --- | --- |
| Haemoglobin | Men about 13–17 g/dL; women about 12–15 g/dL | Low in anaemia, bleeding |
| RBC count | Men about 4.5–5.5; women about 4.0–5.0 million/µL | |
| Haematocrit (PCV) | Men about 40–50%; women about 36–46% | Raised in dehydration, polycythaemia |
| MCV | About 80–100 fL | **Low (microcytic)** in iron deficiency; **high (macrocytic)** in vitamin B12/folate deficiency, methotrexate, alcohol |
| MCH / MCHC | About 27–32 pg / 32–36 g/dL | Low in hypochromic anaemia |
| Reticulocytes | About 0.5–2.5% | Raised after bleeding, haemolysis, response to iron therapy |
| Total WBC | 4,000–11,000/µL | **Leucocytosis** in infection; **leucopenia** with anticancer drugs, clozapine, carbimazole (risk of agranulocytosis) |
| Differential count | Neutrophils about 40–75%, lymphocytes 20–40%, monocytes 2–10%, eosinophils 1–6%, basophils 0–1% | Neutrophilia – bacterial infection; lymphocytosis – viral; eosinophilia – allergy, parasites |
| Platelets | 1.5–4.5 lakh/µL | **Thrombocytopenia** with heparin, some antibiotics, cancer drugs |
| ESR | Men 0–15 mm/h; women 0–20 mm/h | Non-specific marker of inflammation |
| Prothrombin time / INR | INR about 1 in people not on anticoagulants | **INR monitors warfarin therapy** |
| aPTT | Range set by laboratory | Monitors unfractionated heparin |

### Urinalysis

| Part | Normal | Abnormal findings and meaning |
| --- | --- | --- |
| Volume | About 0.8–2 L/day | Polyuria (diabetes, diuretics), oliguria (renal failure, dehydration) |
| Colour / appearance | Pale yellow, clear | Red (blood, rifampicin causes red-orange urine), dark (bilirubin), cloudy (infection) |
| Specific gravity | 1.005–1.030 | Low in diabetes insipidus; high in dehydration |
| pH | About 4.5–8 | Alkaline in some infections; affects drug excretion and crystalluria |
| Protein | Absent / trace | **Proteinuria** in kidney disease, nephrotoxic drugs |
| Glucose | Absent | **Glycosuria** in diabetes, SGLT2 inhibitor therapy |
| Ketones | Absent | Diabetic ketoacidosis, starvation |
| Bilirubin / urobilinogen | Bilirubin absent; urobilinogen small amount | Liver disease, haemolysis, obstruction |
| Blood | Absent | Stones, infection, trauma, tumours, anticoagulant excess |
| Nitrite / leucocyte esterase | Negative | Positive in urinary tract infection |
| Microscopy | Few epithelial cells, 0–2 RBC and 0–5 WBC per high-power field, occasional hyaline casts | Many WBC (pyuria) – UTI; RBC casts – glomerulonephritis; crystals – stones or drug crystalluria (e.g. sulphonamides) |

### Using lab tests in practice

- Compare with **baseline** and look at **trends**, not single values.
- Think of **drug causes** of abnormal results (drug-induced liver injury, hypokalaemia, neutropenia).
- Use results to **adjust doses** (creatinine clearance, INR, drug levels) and to **monitor effect** (glucose, HbA1c, lipids).
- Check that **samples** were taken correctly (timing, haemolysis can falsely raise potassium).

## Remember

- Store terms: **cold 2–8 °C**, **cool 8–25 °C**; FEFO; separate stores for controlled drugs and flammables.
- Purchase methods: **open, limited, single tender, negotiated, rate contract, centralised**.
- **EOQ = √(2AO/C)** – lowest total of ordering and carrying cost.
- **ROL = maximum usage × maximum lead time** (or average usage × lead time + safety stock).
- **ABC** = value (A: few items, most money); **VED** = criticality; **FSN** = movement; ABC–VED matrix.
- Investigational drugs: **NDCT Rules 2019**, ethics committee, informed consent, GCP, labelled for trial use, **accountability records**.
- Trial phases **I** (safety, PK), **II** (efficacy, dose), **III** (confirm, large), **IV** (post-marketing).
- Lab values: Na **135–145**, K **3.5–5.0** mEq/L; creatinine about **0.6–1.2** mg/dL; fasting glucose **≥126** = diabetes; WBC **4,000–11,000/µL**; platelets **1.5–4.5 lakh/µL**; INR monitors warfarin.
