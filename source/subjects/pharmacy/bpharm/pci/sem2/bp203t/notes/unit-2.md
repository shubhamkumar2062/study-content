# Unit 2: Carbohydrate metabolism and biological oxidation

Glucose is the body's main fuel. This unit follows glucose through glycolysis, the link reaction and the citric acid cycle; covers the HMP shunt, glycogen metabolism and gluconeogenesis; explains how hormones keep blood glucose steady and what goes wrong in diabetes; and ends with the electron transport chain and oxidative phosphorylation, where most ATP is made.

**Note on ATP yields.** Older Indian textbooks count 3 ATP per NADH and 2 ATP per FADH2. Current books use measured values of **2.5 ATP per NADH and 1.5 ATP per FADH2**. Both are given below; in the exam, state which convention you use.

## 2.1 Glycolysis (Embden–Meyerhof–Parnas pathway)

**Definition.** Glycolysis is the breakdown of one glucose molecule to two molecules of pyruvate (aerobic) or lactate (anaerobic), with a small yield of ATP.

**Site**: cytosol of all cells. It needs no oxygen. Red cells (no mitochondria) depend on it entirely.

### Steps and enzymes

```text
Glucose
  │ 1. Hexokinase (glucokinase in liver)          ATP → ADP   [irreversible]
Glucose-6-phosphate
  │ 2. Phosphoglucose isomerase
Fructose-6-phosphate
  │ 3. Phosphofructokinase-1 (PFK-1)              ATP → ADP   [irreversible, rate-limiting]
Fructose-1,6-bisphosphate
  │ 4. Aldolase (splits C6 into two C3)
Glyceraldehyde-3-P  ⇌  Dihydroxyacetone-P   (5. Triose phosphate isomerase)
  │   from here every step happens twice per glucose
  │ 6. Glyceraldehyde-3-P dehydrogenase           NAD+ → NADH, Pi added
1,3-Bisphosphoglycerate
  │ 7. Phosphoglycerate kinase                    ADP → ATP   (substrate level)
3-Phosphoglycerate
  │ 8. Phosphoglycerate mutase
2-Phosphoglycerate
  │ 9. Enolase (inhibited by fluoride)            H2O removed
Phosphoenolpyruvate (PEP)
  │ 10. Pyruvate kinase                           ADP → ATP   [irreversible, substrate level]
Pyruvate
  ├── aerobic: enters mitochondria → acetyl-CoA (pyruvate dehydrogenase)
  └── anaerobic: Lactate dehydrogenase, NADH → NAD+  → Lactate
```

**Phases**: steps 1–5 are the **preparatory (investment) phase**, using 2 ATP; steps 6–10 are the **payoff phase**, giving 4 ATP and 2 NADH.

### Energetics of glycolysis

| Step | ATP used / formed per glucose |
| --- | --- |
| Hexokinase | −1 |
| PFK-1 | −1 |
| Phosphoglycerate kinase (×2) | +2 |
| Pyruvate kinase (×2) | +2 |
| **Net ATP (substrate level)** | **+2** |
| NADH from G3P dehydrogenase | 2 NADH |

| Condition | Newer convention | Older convention |
| --- | --- | --- |
| Anaerobic (lactate) | 2 ATP | 2 ATP |
| Aerobic, NADH via malate–aspartate shuttle | 2 + (2 × 2.5) = **7 ATP** | 2 + (2 × 3) = **8 ATP** |
| Aerobic, NADH via glycerol-3-phosphate shuttle | 2 + (2 × 1.5) = **5 ATP** | 2 + (2 × 2) = **6 ATP** |

NADH made in the cytosol cannot cross the inner mitochondrial membrane, so its electrons enter by a shuttle. The malate–aspartate shuttle (liver, heart, kidney) gives full NADH value; the glycerol-3-phosphate shuttle (skeletal muscle, brain) delivers them as FADH2.

### Regulation

- **Hexokinase** is inhibited by its product glucose-6-phosphate. Liver **glucokinase** has a high Km and is induced by insulin; it acts only when blood glucose is high.
- **PFK-1** (key control point): inhibited by ATP and citrate; activated by AMP and **fructose-2,6-bisphosphate** (raised by insulin).
- **Pyruvate kinase**: activated by fructose-1,6-bisphosphate; inhibited by ATP and alanine; inactivated by glucagon (phosphorylation) in liver.

### Significance

1. The only ATP source for red cells, and the main one for exercising muscle when oxygen is short (lactate builds up).
2. Supplies pyruvate for the citric acid cycle and intermediates for other pathways (glycerol-3-phosphate for fat synthesis; 3-phosphoglycerate for serine).
3. **Rapoport–Luebering shunt** in red cells makes 2,3-bisphosphoglycerate, which lowers haemoglobin's affinity for oxygen and helps oxygen delivery to tissues (net ATP through this bypass is zero).
4. Fluoride inhibits enolase, which is why blood for glucose testing is collected in fluoride vials; arsenate uncouples step 6, so no ATP is made at step 7.
5. Pyruvate kinase deficiency causes haemolytic anaemia.

## 2.2 Link reaction: pyruvate to acetyl-CoA

In mitochondria, the **pyruvate dehydrogenase (PDH) complex** converts pyruvate to acetyl-CoA:

Pyruvate + CoA + NAD+ → Acetyl-CoA + CO2 + NADH + H+ (irreversible)

The complex has three enzymes and needs five coenzymes: **thiamine pyrophosphate (B1), lipoic acid, coenzyme A (B5), FAD (B2) and NAD+ (B3)**. Thiamine deficiency (beriberi, alcoholism) blocks this step and raises blood pyruvate and lactate. Arsenite poisons it by binding lipoic acid.

## 2.3 Citric acid cycle (TCA cycle, Krebs cycle)

**Definition.** The final common pathway that oxidises acetyl-CoA from carbohydrates, fats and amino acids to CO2, collecting the electrons as NADH and FADH2. **Site**: mitochondrial matrix.

```text
            Acetyl-CoA (C2) + Oxaloacetate (C4)
                        │ 1. Citrate synthase
                    Citrate (C6)
                        │ 2. Aconitase (inhibited by fluoroacetate → fluorocitrate)
                   Isocitrate (C6)
                        │ 3. Isocitrate dehydrogenase       → NADH + CO2
               α-Ketoglutarate (C5)
                        │ 4. α-Ketoglutarate dehydrogenase  → NADH + CO2
                 Succinyl-CoA (C4)
                        │ 5. Succinyl-CoA synthetase        → GTP (substrate level)
                   Succinate (C4)
                        │ 6. Succinate dehydrogenase        → FADH2 (malonate inhibits)
                    Fumarate (C4)
                        │ 7. Fumarase (adds H2O)
                     Malate (C4)
                        │ 8. Malate dehydrogenase           → NADH
                 Oxaloacetate (C4) ─── returns to step 1
```

### Energetics per acetyl-CoA (one turn)

| Product | Number | Newer (ATP) | Older (ATP) |
| --- | --- | --- | --- |
| NADH (steps 3, 4, 8) | 3 | 3 × 2.5 = 7.5 | 3 × 3 = 9 |
| FADH2 (step 6) | 1 | 1 × 1.5 = 1.5 | 1 × 2 = 2 |
| GTP (step 5) | 1 | 1 | 1 |
| **Total per turn** | | **10** | **12** |

One glucose gives two acetyl-CoA, so two turns: 20 ATP (newer) or 24 ATP (older).

### Total ATP from complete oxidation of one glucose

| Stage | Newer | Older |
| --- | --- | --- |
| Glycolysis (2 ATP + 2 NADH via malate–aspartate shuttle) | 7 | 8 |
| Pyruvate → acetyl-CoA (2 NADH) | 5 | 6 |
| Citric acid cycle (2 turns) | 20 | 24 |
| **Total** | **32** | **38** |

If the glycerol-3-phosphate shuttle is used, subtract 2: **30** (newer) or **36** (older).

### Regulation

Key enzymes: citrate synthase, isocitrate dehydrogenase and α-ketoglutarate dehydrogenase. High ATP and NADH slow the cycle; high ADP and Ca2+ (in muscle) speed it up.

### Significance

1. **Final common pathway** for oxidation of all fuels; produces most of the reduced coenzymes for ATP synthesis.
2. **Amphibolic**: it is both catabolic and anabolic. Intermediates are drawn off for synthesis:
   - citrate → fatty acids and cholesterol;
   - α-ketoglutarate and oxaloacetate → amino acids;
   - succinyl-CoA → heme;
   - oxaloacetate → glucose (gluconeogenesis).
3. **Anaplerotic reactions** refill the cycle, chiefly pyruvate carboxylase (pyruvate → oxaloacetate, biotin-dependent).
4. Releases CO2, part of which is used in synthesis.

## 2.4 Hexose monophosphate (HMP) shunt

Also called the pentose phosphate pathway or phosphogluconate pathway. **Site**: cytosol, most active in liver, adipose tissue, adrenal cortex, lactating mammary gland, testes and red cells. **It produces no ATP.**

```text
Oxidative phase (irreversible)
Glucose-6-P
  │ Glucose-6-phosphate dehydrogenase (G6PD, rate-limiting)   NADP+ → NADPH
6-Phosphogluconolactone
  │ Lactonase (+H2O)
6-Phosphogluconate
  │ 6-Phosphogluconate dehydrogenase                           NADP+ → NADPH, CO2 released
Ribulose-5-P

Non-oxidative phase (reversible)
Ribulose-5-P → Ribose-5-P (isomerase) and Xylulose-5-P (epimerase)
Transketolase (needs TPP) and transaldolase reshuffle sugars →
    Fructose-6-P + Glyceraldehyde-3-P (back to glycolysis)
```

### Significance

1. **NADPH** (2 per glucose-6-P in the oxidative phase) for:
   - reductive biosynthesis of fatty acids, cholesterol and steroid hormones;
   - keeping glutathione reduced in red cells (protects haemoglobin and membranes from oxidation);
   - cytochrome P450 drug metabolism;
   - the respiratory burst of phagocytes (NADPH oxidase).
2. **Ribose-5-phosphate** for nucleotides and nucleic acids.
3. Links pentose and hexose metabolism; transketolase activity of red cells is a test for thiamine status.

### G6PD deficiency

- The most common enzyme deficiency in humans; **X-linked**, so mostly seen in males.
- Red cells cannot make enough NADPH → reduced glutathione falls → oxidants damage haemoglobin (precipitates as **Heinz bodies**) and membranes → **haemolytic anaemia** and jaundice.
- **Triggers**: drugs (primaquine and other antimalarials, sulphonamides, dapsone, nitrofurantoin, high-dose aspirin), fava beans (**favism**), infections.
- Patients are mostly normal until exposed to a trigger. The deficiency gives some protection against falciparum malaria.
- **Pharmacy point**: test for G6PD before starting primaquine; avoid the trigger drugs.

## 2.5 Glycogen metabolism

Glycogen is stored mainly in **liver** (maintains blood glucose between meals) and **muscle** (fuel for the muscle itself).

### Glycogenesis (synthesis)

```text
Glucose → Glucose-6-P            (hexokinase / glucokinase, ATP)
Glucose-6-P → Glucose-1-P        (phosphoglucomutase)
Glucose-1-P + UTP → UDP-glucose + PPi   (UDP-glucose pyrophosphorylase)
UDP-glucose + primer → glycogen (n+1)    (glycogen synthase, α1→4; rate-limiting)
Branching enzyme moves a short chain to make α1→6 branches (every 8–10 residues)
```

The primer is started on the protein **glycogenin**.

### Glycogenolysis (breakdown)

```text
Glycogen phosphorylase (needs PLP) cuts α1→4 bonds with Pi → Glucose-1-P  (rate-limiting)
  ... stops 4 residues before a branch point
Debranching enzyme: (a) transferase moves 3 residues to another chain;
                    (b) α1→6 glucosidase releases the last one as free glucose
Glucose-1-P → Glucose-6-P (phosphoglucomutase)
Liver: Glucose-6-phosphatase → free glucose → blood
Muscle: no glucose-6-phosphatase → Glucose-6-P enters glycolysis for its own use
```

### Regulation

- **Glucagon** (liver) and **adrenaline** (liver and muscle) → cAMP → protein kinase A → phosphorylase **activated**, glycogen synthase **inactivated** → breakdown.
- **Insulin** → protein phosphatase → synthase activated, phosphorylase inactivated → storage.
- In muscle, Ca2+ and AMP also activate phosphorylase during contraction.

### Glycogen storage diseases (GSD)

| Type | Name | Enzyme missing | Main features |
| --- | --- | --- | --- |
| I | von Gierke | Glucose-6-phosphatase | Severe fasting hypoglycaemia, enlarged liver and kidneys, lactic acidosis, high uric acid and lipids |
| II | Pompe | Lysosomal α-1,4-glucosidase (acid maltase) | Glycogen in lysosomes, heart failure in infants |
| III | Cori | Debranching enzyme | Abnormal short-branched glycogen, milder hypoglycaemia |
| IV | Andersen | Branching enzyme | Long unbranched glycogen, liver cirrhosis, early death |
| V | McArdle | Muscle glycogen phosphorylase | Muscle cramps on exercise, no rise of blood lactate, myoglobin in urine |
| VI | Hers | Liver glycogen phosphorylase | Mild hypoglycaemia, enlarged liver |
| VII | Tarui | Muscle phosphofructokinase | Like McArdle, with haemolysis |

## 2.6 Gluconeogenesis

**Definition.** Synthesis of glucose from non-carbohydrate sources. **Sites**: mainly liver (about 90%), also kidney cortex in long fasting. Partly in mitochondria, mostly in cytosol.

**Substrates**: lactate (Cori cycle), glycerol (from fat breakdown), glucogenic amino acids (mainly alanine — glucose–alanine cycle), propionate (from odd-chain fatty acids, via succinyl-CoA). Acetyl-CoA (even-chain fatty acids) **cannot** give net glucose.

### Pathway: glycolysis in reverse, bypassing three irreversible steps

| Irreversible glycolytic step | Gluconeogenic bypass |
| --- | --- |
| Pyruvate kinase | **Pyruvate carboxylase** (mitochondria, biotin, ATP): pyruvate → oxaloacetate; then **PEP carboxykinase** (GTP): oxaloacetate → PEP |
| Phosphofructokinase-1 | **Fructose-1,6-bisphosphatase**: fructose-1,6-bisP → fructose-6-P |
| Hexokinase / glucokinase | **Glucose-6-phosphatase** (liver, kidney): glucose-6-P → glucose |

```text
2 Pyruvate → 2 Oxaloacetate → 2 PEP → (reversed glycolytic steps, 2 NADH used)
→ Fructose-1,6-bisP → Fructose-6-P → Glucose-6-P → Glucose
```

**Cost**: 2 pyruvate → 1 glucose uses 4 ATP + 2 GTP (6 high-energy phosphates) and 2 NADH. Making glucose costs more than glycolysis yields, which is why the two pathways are controlled in opposite directions.

**Regulation**: glucagon, cortisol and adrenaline stimulate (cortisol and glucagon induce PEPCK); insulin inhibits. Acetyl-CoA activates pyruvate carboxylase; fructose-2,6-bisphosphate inhibits fructose-1,6-bisphosphatase.

### Significance

1. Maintains blood glucose during fasting and starvation, after liver glycogen runs out (within about a day).
2. Supplies glucose to brain and red cells, which depend on it.
3. Clears lactate (from muscle and red cells) and glycerol from the blood.
4. Excess gluconeogenesis is a major cause of fasting hyperglycaemia in type 2 diabetes; metformin reduces it.

## 2.7 Hormonal regulation of blood glucose

Normal fasting plasma glucose is about **70–100 mg/dl** (ranges vary by laboratory). After a meal it usually stays below about 140 mg/dl.

| Hormone | Source | Effect on blood glucose | How |
| --- | --- | --- | --- |
| **Insulin** | β-cells of pancreatic islets | **Lowers** | Glucose uptake into muscle and fat (GLUT4); glycogenesis, glycolysis and fat synthesis ↑; gluconeogenesis and glycogenolysis ↓ |
| Glucagon | α-cells | Raises | Glycogenolysis and gluconeogenesis in liver |
| Adrenaline | Adrenal medulla | Raises | Glycogenolysis in liver and muscle; reduces insulin release |
| Cortisol | Adrenal cortex | Raises | Gluconeogenesis; reduces glucose use by tissues |
| Growth hormone | Anterior pituitary | Raises | Reduces glucose uptake; anti-insulin effect |
| Thyroxine | Thyroid | Raises | Increases glucose absorption and glycogenolysis |

Insulin is the **only** hormone that lowers blood glucose; the others are counter-regulatory.

## 2.8 Diabetes mellitus

**Definition.** A group of metabolic disorders with chronic hyperglycaemia due to defects in insulin secretion, insulin action, or both.

**Types**

| Feature | Type 1 | Type 2 |
| --- | --- | --- |
| Cause | Autoimmune destruction of β-cells → absolute insulin deficiency | Insulin resistance with relative insulin deficiency |
| Age of onset | Usually young | Usually adults; linked to obesity |
| Ketoacidosis | Common | Uncommon |
| Treatment | Insulin essential | Diet, exercise, oral drugs (metformin, sulphonylureas, DPP-4 and SGLT2 inhibitors), insulin later |

Other types: gestational diabetes (first found in pregnancy) and secondary diabetes (pancreatitis, Cushing's syndrome, steroid drugs).

**Diagnostic criteria (WHO / ADA)**

- Fasting plasma glucose **≥ 126 mg/dl**, or
- 2-hour plasma glucose **≥ 200 mg/dl** in an oral glucose tolerance test (75 g glucose), or
- **HbA1c ≥ 6.5%**, or
- Random plasma glucose **≥ 200 mg/dl** with classic symptoms.

**Biochemical changes**

- Glucose cannot enter cells → hyperglycaemia; glucose spills into urine above the renal threshold (about 180 mg/dl) → glycosuria, polyuria and thirst (polydipsia).
- Fat breakdown ↑ → excess acetyl-CoA → ketone bodies → **diabetic ketoacidosis** (mainly type 1).
- Protein breakdown ↑ → weight loss, negative nitrogen balance.
- Hypertriglyceridaemia and hypercholesterolaemia.
- **Glycation** of proteins: HbA1c reflects average glucose over about 2–3 months.

**Long-term complications**: microvascular (retinopathy, nephropathy, neuropathy) and macrovascular (coronary disease, stroke, peripheral artery disease); infections and foot ulcers.

## 2.9 Biological oxidation: electron transport chain (ETC)

**Definition.** The ETC (respiratory chain) is a series of electron carriers in the **inner mitochondrial membrane** that passes electrons from NADH and FADH2 to oxygen, forming water and releasing energy that is used to make ATP.

### Components in order of increasing redox potential

```text
NADH ──► Complex I (NADH–CoQ reductase; FMN, Fe–S)  pumps 4 H+
                 │
FADH2 (succinate) ► Complex II (succinate dehydrogenase; FAD, Fe–S) no pumping
                 │
                 ▼
          Coenzyme Q (ubiquinone, mobile carrier in the membrane)
                 │
          Complex III (CoQ–cytochrome c reductase; cyt b, cyt c1, Fe–S)  pumps 4 H+
                 │
          Cytochrome c (mobile, on outer face of inner membrane)
                 │
          Complex IV (cytochrome c oxidase; cyt a, a3, copper)  pumps 2 H+
                 │
          ½ O2 + 2 H+ ──► H2O
                 
Complex V (ATP synthase, F0F1) lets H+ flow back into the matrix → ADP + Pi → ATP
```

**Protons pumped**: 10 per NADH (4 + 4 + 2) and 6 per FADH2 (4 + 2, because it enters at CoQ and skips Complex I).

## 2.10 Oxidative phosphorylation

**Definition.** The formation of ATP from ADP and Pi coupled to the transfer of electrons through the ETC to oxygen.

### Chemiosmotic theory (Peter Mitchell)

1. Electron flow through Complexes I, III and IV pumps protons from the matrix to the intermembrane space.
2. This builds a **proton-motive force**: a pH gradient plus an electrical gradient across the inner membrane, which is impermeable to protons.
3. Protons return through the **F0** channel of ATP synthase; this turns the rotor and changes the shape of the **F1** head, which makes ATP (rotary catalysis — binding change mechanism).
4. About 4 protons are needed per ATP (3 for synthesis + 1 to bring Pi and ADP in and ATP out). Hence **NADH ≈ 10/4 = 2.5 ATP** and **FADH2 ≈ 6/4 = 1.5 ATP** (older P/O ratios: 3 and 2).

**P/O ratio** = number of ATP made per atom of oxygen reduced.

### Substrate-level phosphorylation

ATP (or GTP) formed directly by transfer of a phosphate from a high-energy substrate, without the ETC:

1. 1,3-Bisphosphoglycerate → 3-phosphoglycerate (phosphoglycerate kinase).
2. Phosphoenolpyruvate → pyruvate (pyruvate kinase).
3. Succinyl-CoA → succinate (succinyl-CoA synthetase, gives GTP).

| Feature | Oxidative phosphorylation | Substrate-level phosphorylation |
| --- | --- | --- |
| Site | Inner mitochondrial membrane | Cytosol (glycolysis) and matrix (TCA) |
| Needs O2 and ETC | Yes | No |
| Mechanism | Proton gradient and ATP synthase | Direct phosphate transfer |
| Share of ATP | Most (about 28 of 32 per glucose) | Small (4 per glucose) |

## 2.11 Inhibitors of the ETC and oxidative phosphorylation; uncouplers

| Site | Inhibitor | Note |
| --- | --- | --- |
| Complex I | Rotenone (fish poison, insecticide), amobarbital (amytal), piericidin A | NADH-linked oxidation stops; FADH2 route still works |
| Complex II | Malonate (competitive, on succinate dehydrogenase), carboxin | |
| Complex III | Antimycin A, dimercaprol (BAL) | |
| Complex IV | **Cyanide**, **carbon monoxide**, azide, hydrogen sulphide | Whole chain stops; cyanide poisoning is rapidly fatal |
| ATP synthase | Oligomycin | Blocks proton flow through F0 |
| ADP/ATP translocase | Atractyloside, bongkrekic acid | ADP cannot enter the matrix |

**Uncouplers** let protons leak back across the inner membrane without passing through ATP synthase. Electron transport and oxygen use continue (often faster), but no ATP is made; the energy is released as **heat**.

- **2,4-Dinitrophenol (DNP)** — a classic uncoupler; was once sold for weight loss and caused deaths from fever.
- **Thermogenin (UCP-1)** — a natural uncoupler in **brown fat**; produces heat in newborns and hibernating animals.
- High doses of **salicylates** (aspirin) — explains the fever of salicylate poisoning.
- Dicoumarol and valinomycin (an ionophore) also disturb coupling.

```text
Inhibitor: electron flow STOPS → O2 use stops → no ATP
Uncoupler: electron flow GOES ON → O2 use continues → no ATP → heat
```

## Remember

- Glycolysis: 10 steps in cytosol; 3 irreversible (hexokinase, PFK-1, pyruvate kinase); PFK-1 is rate-limiting; net 2 ATP + 2 NADH.
- PDH complex needs TPP, lipoic acid, CoA, FAD and NAD+.
- TCA per acetyl-CoA: 3 NADH + 1 FADH2 + 1 GTP = 10 ATP (newer) / 12 ATP (older).
- Glucose fully oxidised: **32 ATP (newer) or 38 ATP (older)**; 30 / 36 with the glycerol phosphate shuttle.
- HMP shunt: G6PD is rate-limiting; makes NADPH and ribose-5-P, no ATP; G6PD deficiency → drug-induced haemolysis (primaquine, sulphonamides, fava beans).
- Glycogen: synthase and phosphorylase are the controlled enzymes; von Gierke (G6Pase), Pompe (acid maltase), McArdle (muscle phosphorylase).
- Gluconeogenesis bypasses: pyruvate carboxylase + PEPCK, fructose-1,6-bisphosphatase, glucose-6-phosphatase; costs 6 ATP equivalents per glucose.
- Diabetes: FPG ≥ 126, 2-h OGTT ≥ 200, HbA1c ≥ 6.5% (mg/dl).
- ETC order: Complex I → CoQ → III → cyt c → IV → O2; cyanide and CO block IV; rotenone blocks I; oligomycin blocks ATP synthase; DNP uncouples.
