# Unit 8: Lipid metabolism

This unit covers the lipid part of syllabus chapter 8. As in the syllabus, the pathways are studied **without chemical structures**.

## 8.1 Overview

```text
 Dietary fat ──(bile salts emulsify, pancreatic lipase)──→ fatty acids + monoglycerides
      → absorbed → re-formed into triglycerides → chylomicrons → lymph → blood

 Adipose tissue triglycerides ──LIPOLYSIS──→ glycerol + free fatty acids (carried on albumin)
      Glycerol → liver → glycolysis or gluconeogenesis
      Fatty acids → tissues → β-OXIDATION → acetyl CoA
                                    ├→ TCA cycle → CO2 + H2O + ATP
                                    └→ (liver, excess) → KETOGENESIS → ketone bodies
                                                         → KETOLYSIS in heart, muscle, brain
```

## 8.2 Lipolysis

**Definition:** the hydrolysis of stored **triglycerides** in adipose tissue into **glycerol and free fatty acids**, which are released into the blood to be used as fuel.

### Steps

```text
 Triacylglycerol ──adipose triglyceride lipase (ATGL)──→ Diacylglycerol + fatty acid
 Diacylglycerol  ──hormone-sensitive lipase (HSL)──────→ Monoacylglycerol + fatty acid
 Monoacylglycerol ──monoacylglycerol lipase────────────→ Glycerol + fatty acid
```

- **Hormone-sensitive lipase** is the classic key (regulatory) enzyme of lipolysis.
- **Fate of the products:**
  - **Free fatty acids** travel in plasma bound to **albumin** to muscle, heart, liver and other tissues for β-oxidation.
  - **Glycerol** goes to the liver (adipose tissue lacks glycerol kinase), where glycerol kinase converts it to glycerol-3-phosphate → dihydroxyacetone phosphate → glycolysis or **glucose** (gluconeogenesis).

### Regulation

| Increases lipolysis | Decreases lipolysis |
| --- | --- |
| **Adrenaline, noradrenaline, glucagon** (through cAMP – activate hormone-sensitive lipase by phosphorylation) | **Insulin** (lowers cAMP; dephosphorylates and inactivates HSL) |
| Growth hormone, cortisol, thyroxine (slow, permissive) | Prostaglandins, nicotinic acid |
| Fasting, starvation, stress, exercise, uncontrolled diabetes | Fed state (glucose and insulin high) |

Fasting and diabetes → more lipolysis → more fatty acids → more ketone bodies and fatty liver (see 8.6).

## 8.3 β-Oxidation of fatty acids

**Definition:** the oxidation of fatty acids in which **two-carbon units (acetyl CoA) are removed one at a time** from the carboxyl end, with oxidation taking place at the **β-carbon** (carbon 3). Described by Franz Knoop (1904).

**Site:** **mitochondrial matrix** of liver, muscle, heart and kidney (not brain or red cells).

### Step 1: Activation (in the cytosol)

```text
 Fatty acid + CoA + ATP ──acyl CoA synthetase (thiokinase)──→ Fatty acyl CoA + AMP + PPi
```

Uses two high-energy phosphate bonds (ATP → AMP), counted as **2 ATP**.

### Step 2: Transport into mitochondria – the carnitine shuttle

Long-chain acyl CoA cannot cross the inner mitochondrial membrane directly. **Carnitine** carries it across.

```text
 Cytosol:        Acyl CoA + carnitine ──CPT-I (outer membrane)──→ Acyl carnitine + CoA
 Inner membrane: Acyl carnitine ──translocase──→ into the matrix (carnitine goes back out)
 Matrix:         Acyl carnitine + CoA ──CPT-II──→ Acyl CoA + carnitine
```

**Carnitine palmitoyltransferase-I (CPT-I)** is the **rate-limiting step** of fatty acid oxidation; it is inhibited by **malonyl CoA** (the first product of fatty acid synthesis), so fat is not burnt and made at the same time. Carnitine deficiency causes muscle weakness and low blood sugar on fasting.

### Step 3: The four reactions of each β-oxidation cycle (in the matrix)

| No. | Reaction | Enzyme | Coenzyme / product |
| --- | --- | --- | --- |
| 1 | **Oxidation** (dehydrogenation): acyl CoA → trans-Δ2-enoyl CoA | Acyl CoA dehydrogenase | **FAD → FADH2** |
| 2 | **Hydration**: adds water → β-hydroxyacyl CoA | Enoyl CoA hydratase | – |
| 3 | **Oxidation** (dehydrogenation): → β-ketoacyl CoA | β-Hydroxyacyl CoA dehydrogenase | **NAD+ → NADH** |
| 4 | **Thiolytic cleavage**: CoA splits off a 2-carbon unit | **Thiolase** (β-ketothiolase) | **Acetyl CoA** + acyl CoA shorter by 2 carbons |

The shortened acyl CoA re-enters the cycle until the whole chain is converted into acetyl CoA.

```text
   Palmitoyl CoA (16 C)
        │ cycle 1 → 1 FADH2 + 1 NADH + 1 acetyl CoA
   Myristoyl CoA (14 C)
        │ cycle 2 → 1 FADH2 + 1 NADH + 1 acetyl CoA
        ⋮   (7 cycles in all)
   Butyryl CoA (4 C)
        │ cycle 7 → 1 FADH2 + 1 NADH + 2 acetyl CoA
```

### Energy yield from palmitic acid (C16)

Palmitic acid (16 carbons) undergoes **7 cycles** and gives **8 acetyl CoA**, **7 FADH2** and **7 NADH**.

| Source | Number | ATP each (new) | ATP (new) | ATP each (old) | ATP (old) |
| --- | --- | --- | --- | --- | --- |
| FADH2 | 7 | 1.5 | 10.5 | 2 | 14 |
| NADH | 7 | 2.5 | 17.5 | 3 | 21 |
| Acetyl CoA via TCA | 8 | 10 | 80 | 12 | 96 |
| **Gross** | | | **108** | | **131** |
| Activation | | | − 2 | | − 2 |
| **Net** | | | **106 ATP** | | **129 ATP** |

General rule for a saturated fatty acid with n carbons: number of cycles = (n/2) − 1; number of acetyl CoA = n/2.

**Other types of fatty acid oxidation (brief):** odd-chain fatty acids give propionyl CoA at the end, which becomes succinyl CoA (needs biotin and vitamin B12); unsaturated fatty acids need extra isomerase and reductase enzymes; very long chain fatty acids are first shortened in **peroxisomes** (defective in Zellweger syndrome); ω-oxidation occurs in the endoplasmic reticulum (minor).

### Significance

- Fatty acids are the main fuel for heart and resting skeletal muscle, and for the liver during fasting.
- Fat gives more energy than carbohydrate because fatty acids are more reduced.
- Acetyl CoA from β-oxidation feeds the TCA cycle and ketogenesis.

## 8.4 Ketogenesis

**Ketone bodies:** **acetoacetate**, **β-hydroxybutyrate** and **acetone**. (β-Hydroxybutyrate is not a ketone chemically, but is always grouped with them.)

**Ketogenesis** is the formation of ketone bodies from acetyl CoA. **Site:** **mitochondria of the liver only**.

It increases when fatty acid oxidation is high and oxaloacetate is low (used for gluconeogenesis), so acetyl CoA cannot enter the TCA cycle fast enough – in **starvation, uncontrolled diabetes, very low carbohydrate diets, prolonged vomiting and alcoholism**.

```text
 2 Acetyl CoA ──thiolase──→ Acetoacetyl CoA
 Acetoacetyl CoA + Acetyl CoA ──HMG-CoA synthase (rate-limiting)──→ HMG-CoA
 HMG-CoA ──HMG-CoA lyase──→ ACETOACETATE + Acetyl CoA
 Acetoacetate ──β-hydroxybutyrate dehydrogenase (NADH)──→ β-HYDROXYBUTYRATE
 Acetoacetate ──(spontaneous decarboxylation)──→ ACETONE + CO2  (breathed out – fruity smell)
```

**Note:** HMG-CoA is also the precursor of cholesterol, but cholesterol is made in the **cytosol** with **HMG-CoA reductase**; ketone bodies are made in **mitochondria** with **HMG-CoA lyase**.

## 8.5 Ketolysis (utilisation of ketone bodies)

The liver **makes** ketone bodies but **cannot use** them, because it lacks the enzyme **succinyl CoA–acetoacetate CoA transferase (thiophorase)**. They pass through the blood to **extrahepatic tissues** – heart, skeletal muscle, kidney cortex and, in prolonged starvation, the **brain** (which can then meet up to about two-thirds of its energy needs from them).

```text
 β-Hydroxybutyrate ──β-hydroxybutyrate dehydrogenase──→ Acetoacetate (+ NADH)
 Acetoacetate + Succinyl CoA ──thiophorase (CoA transferase)──→ Acetoacetyl CoA + Succinate
 Acetoacetyl CoA + CoA ──thiolase──→ 2 Acetyl CoA → TCA cycle → energy
 Acetone: not used much; excreted in breath and urine
```

**Significance:** ketone bodies are water-soluble fuels that spare glucose during fasting, protecting muscle protein from being broken down for gluconeogenesis.

## 8.6 Diseases related to abnormal lipid metabolism

### Ketosis and ketoacidosis

- **Ketosis:** increased ketone bodies in blood (**ketonaemia**) and urine (**ketonuria**). Mild ketosis in fasting is normal.
- **Ketoacidosis:** when ketone bodies (which are acids) accumulate faster than they can be used, they lower blood pH and bicarbonate → **metabolic acidosis**.
- **Causes:** uncontrolled **type 1 diabetes mellitus** (diabetic ketoacidosis, DKA), starvation, prolonged vomiting, alcohol excess.
- **Mechanism in diabetes:** lack of insulin → unchecked lipolysis → flood of fatty acids to the liver → excess acetyl CoA; at the same time oxaloacetate is used for gluconeogenesis → acetyl CoA is diverted to ketone bodies.
- **Features:** fruity (acetone) smell of breath, deep rapid breathing (**Kussmaul breathing**), nausea, vomiting, abdominal pain, dehydration (osmotic diuresis), loss of sodium and potassium, drowsiness, coma.
- **Tests:** Rothera's test for ketones in urine (purple ring); urine dipsticks; blood β-hydroxybutyrate; arterial blood gas.
- **Treatment:** insulin, intravenous fluids, potassium replacement; treat the cause.

### Fatty liver

**Fatty liver** is the excessive accumulation of fat (triglycerides) in liver cells – more than about 5% of liver weight. It happens when fat reaches the liver faster than the liver can export it as VLDL.

| Group of causes | Examples |
| --- | --- |
| **More fat coming to the liver** | High-fat diet, obesity, uncontrolled diabetes, starvation (mobilised fat) |
| **More fat made in the liver** | Excess carbohydrate and **alcohol** (alcohol increases NADH, favouring fat synthesis) |
| **Less fat leaving the liver** (poor VLDL formation) | Protein deficiency (kwashiorkor – no apoproteins); **lack of lipotropic factors** (choline, methionine, betaine, inositol) needed to make phospholipids; liver poisons such as carbon tetrachloride, chloroform, some drugs (tetracycline in high dose, methotrexate) |

- **Types:** alcoholic and **non-alcoholic fatty liver disease (NAFLD)**, now very common with obesity and diabetes.
- **Effects:** enlarged liver; may progress to inflammation (steatohepatitis), fibrosis and **cirrhosis**.
- **Lipotropic factors:** substances that prevent fatty liver by helping phospholipid and lipoprotein formation – **choline, methionine, betaine, inositol**, vitamin B12 and folic acid.
- **Management:** remove the cause (stop alcohol, lose weight, control diabetes), adequate protein and lipotropic factors.

### Hypercholesterolaemia

Raised blood cholesterol – commonly total cholesterol above about 200 mg/dl or LDL-cholesterol above about 130 mg/dl (guideline values; ranges vary by laboratory).

| Type | Causes |
| --- | --- |
| **Primary (familial)** | **Familial hypercholesterolaemia** – defective LDL receptors, so LDL is not cleared; very high LDL from childhood; xanthomas (fat deposits in tendons and skin), early heart attacks |
| **Secondary** | Diet rich in saturated fat, trans fat and cholesterol; obesity; **diabetes mellitus**; **hypothyroidism**; **nephrotic syndrome**; **obstructive jaundice**; pregnancy; drugs (thiazides, some steroids) |

- **Consequences:** **atherosclerosis** – LDL enters the artery wall, is oxidised and taken up by macrophages (foam cells), forming plaques that narrow arteries → **coronary heart disease (angina, myocardial infarction)**, stroke, peripheral vascular disease. Xanthomas, corneal arcus.
- **HDL is protective;** a low HDL also raises the risk.
- **Management:**
  - Diet low in saturated and trans fat, rich in fibre, fruits, vegetables and PUFA (especially ω-3); weight loss; exercise; stop smoking.
  - Drugs: **statins** (inhibit HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis; increase LDL receptors), ezetimibe (blocks cholesterol absorption), bile acid sequestrants (cholestyramine), fibrates (mainly for high triglycerides), niacin.

### Other disorders of lipid metabolism (brief)

- **Obesity:** excess body fat; risk factor for diabetes, hypertension, fatty liver, heart disease.
- **Atherosclerosis:** see above.
- **Lipid storage diseases (sphingolipidoses):** inherited enzyme defects, such as **Gaucher's disease** (glucocerebrosidase), **Niemann–Pick disease** (sphingomyelinase) and **Tay–Sachs disease** (hexosaminidase A).
- **Respiratory distress syndrome:** lack of lung surfactant (dipalmitoyl lecithin) in premature babies.
- **Hypertriglyceridaemia:** in diabetes, alcohol, obesity; very high levels can cause pancreatitis.

## 8.7 Cholesterol synthesis (brief, for linking)

Cholesterol is made in the **cytosol and endoplasmic reticulum**, mainly in the liver, from **acetyl CoA**:

```text
 Acetyl CoA → Acetoacetyl CoA → HMG-CoA ──HMG-CoA reductase (rate-limiting; inhibited by statins
                                          and by cholesterol)──→ Mevalonate → isoprene units
              → squalene → lanosterol → CHOLESTEROL
```

Insulin and thyroxine increase HMG-CoA reductase activity; glucagon and cholesterol decrease it.

## Remember

- Lipolysis: adipose tissue; hormone-sensitive lipase; ↑ by adrenaline and glucagon (cAMP), ↓ by insulin.
- β-Oxidation: mitochondrial matrix; activation (thiokinase, 2 ATP) → carnitine shuttle (CPT-I is rate-limiting, inhibited by malonyl CoA) → oxidation (FAD), hydration, oxidation (NAD), thiolysis.
- Palmitate: 7 cycles, 8 acetyl CoA, 7 FADH2, 7 NADH → net 106 ATP (new) or 129 (old).
- Ketone bodies: acetoacetate, β-hydroxybutyrate, acetone; made only in liver mitochondria (HMG-CoA synthase, lyase); used outside the liver (thiophorase, absent in liver).
- Ketoacidosis: uncontrolled diabetes, starvation; fruity breath, Kussmaul breathing; Rothera's test.
- Fatty liver: more fat in, more made, less out (VLDL); lipotropic factors choline, methionine, betaine, inositol.
- Hypercholesterolaemia: familial (LDL-receptor defect) or secondary (diabetes, hypothyroidism, nephrotic syndrome); → atherosclerosis; treat with diet and statins.
