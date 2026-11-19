# Unit 7: Carbohydrate metabolism and biological oxidation

Syllabus chapter 8 (metabolism, 20 hours) is the largest chapter. In this guide it is split into three units: carbohydrates with biological oxidation (this unit), lipids (Unit 8) and amino acids (Unit 9). The syllabus asks for the **cycles and pathways without chemical structures**, so learn the names of the intermediates, the enzymes, the energy steps and the regulation.

## 7.1 Metabolism: basic terms

- **Metabolism** = all chemical reactions in the body.
- **Catabolism** = breaking down of large molecules into smaller ones, releasing energy (glycolysis, β-oxidation).
- **Anabolism** = building up of large molecules from small ones, using energy (glycogen, protein, fatty acid synthesis).
- **ATP** is the link: catabolism makes ATP, anabolism uses it.

### Digestion and absorption (brief)

Dietary starch is digested by salivary and pancreatic **amylase** to maltose and dextrins; brush-border enzymes (**maltase, sucrase, lactase**) give glucose, fructose and galactose, which are absorbed in the small intestine (glucose and galactose by sodium-dependent active transport, fructose by facilitated diffusion) and carried to the liver by the portal vein.

```text
 Fate of glucose in the cell
                       ┌→ Glycogen (glycogenesis) – storage
 Glucose → Glucose-6-P ┼→ Pyruvate (glycolysis) → Acetyl CoA → TCA → CO2 + H2O + ATP
                       ├→ HMP shunt → NADPH + ribose-5-P
                       └→ (excess) → fat
```

## 7.2 Glycolysis (Embden–Meyerhof–Parnas pathway)

**Definition:** the breakdown of one molecule of **glucose** (6 C) into **two molecules of pyruvate** (3 C) under aerobic conditions, or into **two molecules of lactate** under anaerobic conditions, with the production of ATP.

- **Site:** **cytosol** of all cells. It is the only pathway that makes ATP without oxygen, so red blood cells (which have no mitochondria) depend on it.

### Steps (10 reactions in two phases)

```text
 PREPARATORY PHASE (uses 2 ATP)
 1. Glucose ──hexokinase / glucokinase (liver)──→ Glucose-6-phosphate       (–1 ATP) ✱
 2. Glucose-6-P ──phosphohexose isomerase──→ Fructose-6-phosphate
 3. Fructose-6-P ──phosphofructokinase-1 (PFK-1)──→ Fructose-1,6-bisphosphate (–1 ATP) ✱ key step
 4. Fructose-1,6-bisP ──aldolase──→ Glyceraldehyde-3-P + Dihydroxyacetone-P
 5. Dihydroxyacetone-P ──triose phosphate isomerase──→ Glyceraldehyde-3-P
        (so 2 molecules of glyceraldehyde-3-P go on; each step below happens twice)

 PAY-OFF PHASE (makes 4 ATP + 2 NADH)
 6. Glyceraldehyde-3-P ──glyceraldehyde-3-P dehydrogenase──→ 1,3-bisphosphoglycerate (NAD+ → NADH)
 7. 1,3-BPG ──phosphoglycerate kinase──→ 3-phosphoglycerate          (+1 ATP × 2, substrate level)
 8. 3-Phosphoglycerate ──phosphoglycerate mutase──→ 2-phosphoglycerate
 9. 2-Phosphoglycerate ──enolase (inhibited by fluoride)──→ Phosphoenolpyruvate (PEP)
10. PEP ──pyruvate kinase──→ Pyruvate                                 (+1 ATP × 2, substrate level) ✱

 ✱ irreversible, regulatory steps
 Anaerobic: Pyruvate ──lactate dehydrogenase (NADH → NAD+)──→ Lactate
```

### Energy yield of glycolysis

| Condition | ATP used | ATP made | NADH | Net ATP per glucose |
| --- | --- | --- | --- | --- |
| **Anaerobic** (NADH used to make lactate) | 2 | 4 | 0 net | **2 ATP** |
| **Aerobic** (NADH sent to mitochondria) | 2 | 4 | 2 NADH | 2 + (2 × 2.5) = **7 ATP** by the newer values (or 8 by the older P/O values of 3); 5 (or 6) if the glycerol phosphate shuttle is used |

### Regulation

The three **irreversible** enzymes – **hexokinase/glucokinase, phosphofructokinase-1 and pyruvate kinase** – control the rate.

- **PFK-1** is the most important control point (rate-limiting): activated by AMP, ADP and fructose-2,6-bisphosphate; inhibited by ATP and citrate.
- Insulin increases glycolysis (induces glucokinase, PFK-1, pyruvate kinase); glucagon decreases it.

### Significance

1. Main pathway of glucose use in all cells; gives energy quickly.
2. Only source of ATP for **red blood cells** and for muscle working without enough oxygen (heavy exercise → lactate → muscle fatigue).
3. Intermediates are used to make glycerol (for fat), amino acids (alanine, serine) and 2,3-BPG in red cells (which helps release oxygen from haemoglobin).
4. **Fluoride** inhibits enolase – sodium fluoride is used in blood-collection tubes for glucose estimation to stop glycolysis by blood cells.
5. Excess lactate in shock, heavy exercise or metformin toxicity causes **lactic acidosis**.

### Oxidative decarboxylation of pyruvate (link reaction)

In aerobic conditions pyruvate enters the **mitochondria** and is converted to **acetyl CoA** by the **pyruvate dehydrogenase (PDH) complex**:

```text
 Pyruvate + CoA + NAD+  ──PDH complex──→  Acetyl CoA + CO2 + NADH     (irreversible)
```

The complex needs **five coenzymes**: thiamine pyrophosphate (B1), lipoic acid, coenzyme A (B5), FAD (B2) and NAD+ (B3). This is why thiamine deficiency causes pyruvate and lactate to build up (beriberi). Arsenite inhibits it.

## 7.3 TCA cycle (citric acid cycle, Krebs cycle)

**Definition:** a cyclic series of reactions in the **mitochondrial matrix** in which **acetyl CoA** is completely oxidised to **CO2 and water**, with the production of reduced coenzymes (NADH, FADH2) that give ATP in the electron transport chain. Described by Sir Hans Krebs (1937).

```text
                     Acetyl CoA (2 C)
                         │
   Oxaloacetate (4 C) ───┤ 1. citrate synthase
          ▲              ▼
          │           Citrate (6 C)
 8. malate │              │ 2. aconitase (inhibited by fluoroacetate → fluorocitrate)
 dehydrogenase            ▼
 NADH ←───│           Isocitrate (6 C)
          │              │ 3. isocitrate dehydrogenase ──→ NADH + CO2
       Malate (4 C)       ▼
          ▲           α-Ketoglutarate (5 C)
 7. fumarase              │ 4. α-ketoglutarate dehydrogenase ──→ NADH + CO2
          │              ▼
       Fumarate (4 C)  Succinyl CoA (4 C)
          ▲              │ 5. succinate thiokinase (succinyl CoA synthetase) ──→ GTP (= ATP)
 6. succinate             ▼
 dehydrogenase ←──── Succinate (4 C)
 FADH2 (inhibited by malonate)
```

### Energy yield per acetyl CoA (one turn)

| Step | Product | ATP (new value) | ATP (old value) |
| --- | --- | --- | --- |
| Isocitrate dehydrogenase | NADH | 2.5 | 3 |
| α-Ketoglutarate dehydrogenase | NADH | 2.5 | 3 |
| Succinate thiokinase | GTP | 1 | 1 |
| Succinate dehydrogenase | FADH2 | 1.5 | 2 |
| Malate dehydrogenase | NADH | 2.5 | 3 |
| **Total** | 3 NADH, 1 FADH2, 1 GTP | **10** | **12** |

### Total ATP from complete oxidation of one glucose

| Stage | New values | Old values |
| --- | --- | --- |
| Glycolysis (aerobic, malate–aspartate shuttle) | 7 | 8 |
| Pyruvate → acetyl CoA (2 NADH) | 5 | 6 |
| TCA cycle (2 turns) | 20 | 24 |
| **Total** | **32** (30 with the glycerol phosphate shuttle) | **38** (36) |

Most Indian textbooks give both figures; write the one your teacher uses and say which P/O values you used.

### Regulation

Controlled at **citrate synthase, isocitrate dehydrogenase** and **α-ketoglutarate dehydrogenase**: inhibited by ATP and NADH (high energy), activated by ADP and calcium (muscle contraction).

### Significance of the TCA cycle

1. **Final common pathway** for oxidation of carbohydrates, fats and proteins (all give acetyl CoA or TCA intermediates).
2. Produces most of the reduced coenzymes, so most of the body's ATP.
3. **Amphibolic** (both catabolic and anabolic): intermediates are used for synthesis – citrate for fatty acids and cholesterol, α-ketoglutarate and oxaloacetate for amino acids, succinyl CoA for haem, oxaloacetate for glucose (gluconeogenesis).
4. Linked with the urea cycle (fumarate) and transamination.
5. Requires B vitamins: thiamine, riboflavin, niacin, pantothenic acid (and lipoic acid).

## 7.4 Glycogen metabolism

### Glycogenesis (synthesis of glycogen)

Occurs in the cytosol of **liver and muscle**, after meals when glucose is plentiful (stimulated by **insulin**).

```text
 Glucose ──hexokinase/glucokinase (ATP)──→ Glucose-6-P
         ──phosphoglucomutase──→ Glucose-1-P
         ──UDP-glucose pyrophosphorylase (UTP)──→ UDP-glucose
         ──glycogen synthase (key enzyme; adds α1→4 links to a primer)──→ longer chain
         ──branching enzyme (makes α1→6 branch points)──→ GLYCOGEN
 Primer: a small piece of glycogen or the protein glycogenin
```

### Glycogenolysis (breakdown of glycogen)

Occurs between meals, in fasting and in stress (stimulated by **glucagon** in liver and **adrenaline** in liver and muscle).

```text
 Glycogen ──glycogen phosphorylase (key enzyme; needs pyridoxal phosphate)──→ Glucose-1-P
          ──debranching enzyme──→ removes branches (releases some free glucose)
 Glucose-1-P ──phosphoglucomutase──→ Glucose-6-P
   Liver:  Glucose-6-P ──glucose-6-phosphatase──→ free GLUCOSE → blood
   Muscle: no glucose-6-phosphatase → Glucose-6-P used for glycolysis in the muscle itself
```

**Key point:** liver glycogen maintains **blood glucose**; muscle glycogen gives fuel only to the **muscle** (muscle lacks glucose-6-phosphatase).

**Regulation:** glycogen synthase and phosphorylase are controlled in opposite directions by phosphorylation. Glucagon and adrenaline (through cAMP and protein kinase A) **activate phosphorylase and inhibit synthase**; insulin does the reverse. So synthesis and breakdown do not run at the same time.

### Glycogen storage diseases (inborn errors)

| Type | Name | Enzyme deficient | Main features |
| --- | --- | --- | --- |
| I | **von Gierke's disease** | Glucose-6-phosphatase (liver) | Severe fasting hypoglycaemia, enlarged liver, lactic acidosis, high uric acid and lipids |
| II | **Pompe's disease** | Lysosomal α-1,4-glucosidase (acid maltase) | Glycogen in lysosomes; heart failure in infants |
| III | Cori's disease | Debranching enzyme | Liver enlargement, mild hypoglycaemia |
| IV | Andersen's disease | Branching enzyme | Liver cirrhosis, early death |
| V | **McArdle's disease** | Muscle glycogen phosphorylase | Muscle cramps and weakness on exercise; no rise of lactate |
| VI | Hers' disease | Liver glycogen phosphorylase | Mild hypoglycaemia, enlarged liver |

### Gluconeogenesis (brief)

The making of **new glucose from non-carbohydrate sources** – lactate, glycerol and glucogenic amino acids (mainly alanine) – mainly in the **liver** (also kidney) during fasting. It reverses glycolysis except at the three irreversible steps, which are bypassed by pyruvate carboxylase and PEP carboxykinase, fructose-1,6-bisphosphatase and glucose-6-phosphatase. The **Cori cycle** carries lactate from muscle to the liver, where it becomes glucose again.

## 7.5 Regulation of blood glucose level

**Normal fasting plasma glucose** is commonly quoted as about **70–100 mg/dl**, rising to below about 140 mg/dl two hours after a meal; ranges vary by laboratory. The level is kept steady because the brain needs a constant supply.

```text
          After a meal (glucose ↑)                    Fasting / stress (glucose ↓)
                 │                                             │
          INSULIN (β-cells) ↑                   GLUCAGON (α-cells), ADRENALINE,
                 │                              CORTISOL, GROWTH HORMONE, THYROXINE ↑
   • glucose uptake by muscle, fat (GLUT4)        • glycogenolysis (liver)
   • glycolysis ↑                                 • gluconeogenesis
   • glycogenesis ↑                               • lipolysis → fatty acids used as fuel
   • lipogenesis ↑                                • less glucose uptake by muscle
   • gluconeogenesis ↓, glycogenolysis ↓
                 │                                             │
          BLOOD GLUCOSE FALLS                        BLOOD GLUCOSE RISES
```

| Factor | Effect on blood glucose |
| --- | --- |
| **Insulin** | The **only hormone that lowers** blood glucose |
| Glucagon | Raises (glycogenolysis, gluconeogenesis) |
| Adrenaline | Raises quickly in stress (glycogenolysis) |
| Cortisol (glucocorticoids) | Raises (gluconeogenesis) |
| Growth hormone, thyroxine | Raise |
| Liver | Stores glucose as glycogen and releases it; makes new glucose |
| Kidney | Reabsorbs filtered glucose; when blood glucose exceeds the **renal threshold** (commonly quoted as about 180 mg/dl) glucose appears in urine (glycosuria) |

## 7.6 Diseases related to abnormal carbohydrate metabolism

### Diabetes mellitus

A chronic metabolic disorder with **high blood glucose (hyperglycaemia)** due to lack of insulin secretion, insulin action, or both.

| Feature | Type 1 | Type 2 |
| --- | --- | --- |
| Cause | Autoimmune destruction of β-cells → absolute insulin lack | Insulin resistance with relative insulin deficiency |
| Age of onset | Usually young | Usually adults (obesity, family history) |
| Ketoacidosis | Common | Uncommon |
| Treatment | Insulin | Diet, exercise, oral drugs (metformin), insulin later if needed |

- **Symptoms:** polyuria, polydipsia (thirst), polyphagia (hunger), weight loss, tiredness, infections, slow wound healing.
- **Biochemical changes:** hyperglycaemia, glycosuria, increased lipolysis and ketone bodies (ketoacidosis), raised cholesterol and triglycerides, protein breakdown.
- **Commonly used diagnostic cut-offs:** fasting plasma glucose **126 mg/dl or more**, 2-hour glucose (in a 75 g oral glucose tolerance test) **200 mg/dl or more**, or **HbA1c 6.5% or more**. These are guideline values; the doctor confirms the diagnosis.
- **Glycated haemoglobin (HbA1c)** reflects average blood glucose of the last 2–3 months (red cell life is about 120 days).
- **Complications:** diabetic ketoacidosis, hypoglycaemia (from treatment), damage to eyes (retinopathy), kidneys (nephropathy), nerves (neuropathy), heart and blood vessels.

**Glucose tolerance test (GTT):** after an overnight fast, blood glucose is measured, 75 g of glucose is given by mouth, and glucose is measured again (usually at 2 hours). A diabetic curve rises higher and returns to baseline slowly.

### Hypoglycaemia

Blood glucose below about 70 mg/dl (symptoms usually appear lower). Causes: insulin or sulphonylurea overdose, missed meals, alcohol, insulin-secreting tumour (insulinoma), von Gierke's disease. Symptoms: sweating, tremor, palpitations, hunger, confusion, convulsions, coma. Treatment: oral glucose or intravenous dextrose; glucagon injection.

### Other disorders

| Disorder | Defect | Features |
| --- | --- | --- |
| **Galactosaemia** | Galactose-1-phosphate uridyl transferase deficiency | Vomiting, jaundice, liver damage, cataract and mental retardation in infants fed milk; treated with a galactose-free (lactose-free) diet |
| **Lactose intolerance** | Lactase deficiency | Bloating, cramps and diarrhoea after milk |
| **Hereditary fructose intolerance** | Aldolase B deficiency | Hypoglycaemia and vomiting after fruit or sucrose |
| **Essential fructosuria** | Fructokinase deficiency | Harmless fructose in urine |
| **Glycogen storage diseases** | See 7.4 | – |
| **Lactic acidosis** | Excess lactate (shock, hypoxia, thiamine deficiency) | Acidosis, rapid breathing |

## 7.7 Biological oxidation

**Biological oxidation** is the transfer of electrons (as hydrogen atoms or electrons) from food molecules to oxygen in living cells, with the release of energy that is captured as ATP. Oxidation is loss of electrons (or hydrogen); reduction is gain of electrons.

### Electron transport chain (ETC, respiratory chain)

**Site:** the **inner mitochondrial membrane**.

The reduced coenzymes **NADH** and **FADH2** formed in glycolysis, PDH, TCA cycle and β-oxidation pass their electrons through a chain of carriers arranged in order of increasing redox potential, finally to **oxygen**, which is reduced to **water**.

```text
          Complex I                    Complex III          Complex IV
 NADH ──→ (NADH–CoQ reductase) ──→ CoQ ──→ (cyt b–c1) ──→ cyt c ──→ (cytochrome oxidase, a–a3, Cu) ──→ ½O2 → H2O
                                   ▲
 FADH2 (succinate) → Complex II ───┘
          (succinate–CoQ reductase)

 Protons (H+) are pumped from the matrix to the intermembrane space at Complexes I, III and IV.
 Complex V (ATP synthase, F0–F1) lets H+ flow back and makes ATP from ADP + Pi.
```

| Component | Description |
| --- | --- |
| Complex I | NADH dehydrogenase (FMN, iron–sulphur proteins); pumps protons |
| Complex II | Succinate dehydrogenase (FAD, Fe–S); also a TCA cycle enzyme; does not pump protons |
| Coenzyme Q (ubiquinone) | Mobile, lipid-soluble carrier in the membrane |
| Complex III | Cytochrome b–c1 complex; pumps protons |
| Cytochrome c | Small mobile protein carrier |
| Complex IV | Cytochrome oxidase (cytochromes a, a3 and copper); passes electrons to oxygen; pumps protons |
| Complex V | ATP synthase (F0 channel + F1 head) |

### Oxidative phosphorylation

**Definition:** the formation of ATP from ADP and inorganic phosphate coupled with the transfer of electrons along the respiratory chain to oxygen.

**Chemiosmotic theory (Peter Mitchell, 1961; Nobel Prize 1978):** electron flow drives the pumping of protons across the inner membrane, building a **proton gradient** (a difference in H+ concentration and charge). Protons flow back into the matrix only through **ATP synthase**, and this flow drives ATP synthesis.

**P/O ratio** (ATP formed per oxygen atom used):

| Electron donor | P/O (newer) | P/O (older) |
| --- | --- | --- |
| NADH | 2.5 | 3 |
| FADH2 | 1.5 | 2 |

### Inhibitors and uncouplers

| Site | Inhibitor |
| --- | --- |
| Complex I | **Rotenone** (fish poison, insecticide), amobarbital, piericidin |
| Complex II | Malonate (competitive), carboxin |
| Complex III | **Antimycin A**, dimercaprol (BAL) |
| Complex IV | **Cyanide**, **carbon monoxide**, **hydrogen sulphide**, azide – stop respiration completely; cyanide poisoning is rapidly fatal |
| Complex V (ATP synthase) | **Oligomycin** |
| **Uncouplers** | **2,4-Dinitrophenol**, high-dose aspirin (salicylates), thermogenin (brown fat) – let protons leak back without making ATP, so energy is lost as **heat** (fever in salicylate poisoning; heat production in newborn brown fat) |

**Substrate-level phosphorylation** (for comparison) makes ATP directly in a reaction without the ETC: phosphoglycerate kinase and pyruvate kinase (glycolysis), succinate thiokinase (TCA).

## Remember

- Glycolysis: cytosol; glucose → 2 pyruvate; key enzymes hexokinase, PFK-1 (rate-limiting), pyruvate kinase; net 2 ATP anaerobic, 7 (or 8) aerobic; fluoride inhibits enolase.
- PDH complex: pyruvate → acetyl CoA; needs TPP, lipoic acid, CoA, FAD, NAD.
- TCA: mitochondria; citrate → isocitrate → α-KG → succinyl CoA → succinate → fumarate → malate → oxaloacetate; 10 (or 12) ATP per acetyl CoA; amphibolic; malonate inhibits SDH.
- Glucose total: 32 (new) or 38 (old) ATP.
- Glycogen synthase (insulin) vs glycogen phosphorylase (glucagon, adrenaline); liver has glucose-6-phosphatase, muscle does not.
- Insulin is the only hormone that lowers blood glucose; diabetes: fasting ≥ 126 mg/dl, HbA1c ≥ 6.5% (guideline cut-offs).
- ETC: I, CoQ, III, cyt c, IV → O2; ATP synthase = complex V; chemiosmotic theory (Mitchell); cyanide and CO block complex IV; 2,4-DNP uncouples.
