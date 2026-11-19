# Unit 3: Lipid metabolism and amino acid metabolism

The first half of this unit covers how fatty acids are burnt (β-oxidation) and made (de novo synthesis), how ketone bodies are formed and used, what cholesterol becomes, and the common disorders of lipid metabolism. The second half covers how amino acids lose their nitrogen, how the urea cycle removes it, the fate of phenylalanine and tyrosine with their inherited disorders, the making of important amines, and the breakdown of heme with jaundice.

Energy values are given in both conventions: **newer** (NADH = 2.5 ATP, FADH2 = 1.5 ATP) and **older** (NADH = 3, FADH2 = 2).

## 3.1 β-Oxidation of saturated fatty acids (palmitic acid)

**Definition.** β-Oxidation is the stepwise removal of two-carbon units (as acetyl-CoA) from a fatty acid, by oxidation at the β-carbon (C3). **Site**: mitochondrial matrix (very long chains begin in peroxisomes). Active in liver, heart and muscle; not in brain or red cells.

### Step 1: Activation (cytosol)

Fatty acid + CoA + ATP → Fatty acyl-CoA + AMP + PPi (acyl-CoA synthetase / thiokinase)

PPi is hydrolysed, so **2 high-energy bonds** (2 ATP equivalents) are used.

### Step 2: Transport into mitochondria (carnitine shuttle)

```text
Cytosol: Acyl-CoA + carnitine → Acyl-carnitine   (carnitine acyltransferase I, CAT-I / CPT-I)
         Acyl-carnitine crosses inner membrane (translocase)
Matrix:  Acyl-carnitine + CoA → Acyl-CoA + carnitine   (CAT-II / CPT-II)
```

CPT-I is the **rate-limiting** step and is inhibited by **malonyl-CoA**, so fat synthesis and fat burning do not run together. Carnitine deficiency causes muscle weakness and fasting hypoglycaemia.

### Step 3: The four reactions of each cycle

```text
Acyl-CoA (Cn)
  │ 1. Acyl-CoA dehydrogenase              FAD → FADH2
trans-Δ2-Enoyl-CoA
  │ 2. Enoyl-CoA hydratase                 + H2O
L-3-Hydroxyacyl-CoA
  │ 3. 3-Hydroxyacyl-CoA dehydrogenase     NAD+ → NADH
3-Ketoacyl-CoA
  │ 4. Thiolase                            + CoA
Acetyl-CoA  +  Acyl-CoA (Cn−2) → goes round again
```

Memory aid for the order: **O**xidation, **H**ydration, **O**xidation, **T**hiolysis.

### Energetics for palmitic acid (C16)

Palmitoyl-CoA needs **7 cycles** and gives **8 acetyl-CoA, 7 FADH2 and 7 NADH**.

| Product | Newer | Older |
| --- | --- | --- |
| 7 FADH2 | 7 × 1.5 = 10.5 | 7 × 2 = 14 |
| 7 NADH | 7 × 2.5 = 17.5 | 7 × 3 = 21 |
| 8 acetyl-CoA via TCA | 8 × 10 = 80 | 8 × 12 = 96 |
| Gross | 108 | 131 |
| Activation | −2 | −2 |
| **Net ATP per palmitate** | **106** | **129** |

**Odd-chain fatty acids** give propionyl-CoA in the last cycle; this becomes succinyl-CoA (needs biotin and vitamin B12) and can form glucose.

**Significance**: main fuel of heart and resting muscle and of the liver during fasting; supplies acetyl-CoA for ketone bodies.

## 3.2 Ketone bodies: formation, utilisation and ketoacidosis

**Ketone bodies**: acetoacetate, β-hydroxybutyrate and acetone.

### Ketogenesis (liver mitochondria only)

```text
2 Acetyl-CoA → Acetoacetyl-CoA                       (thiolase)
Acetoacetyl-CoA + Acetyl-CoA → HMG-CoA               (HMG-CoA synthase, rate-limiting)
HMG-CoA → Acetoacetate + Acetyl-CoA                  (HMG-CoA lyase)
Acetoacetate + NADH ⇌ β-Hydroxybutyrate + NAD+       (β-hydroxybutyrate dehydrogenase)
Acetoacetate → Acetone + CO2                          (spontaneous; breathed out)
```

### Ketolysis (utilisation, outside the liver)

```text
β-Hydroxybutyrate → Acetoacetate (NADH formed)
Acetoacetate + Succinyl-CoA → Acetoacetyl-CoA + Succinate
                     (succinyl-CoA:acetoacetate CoA transferase, "thiophorase")
Acetoacetyl-CoA + CoA → 2 Acetyl-CoA (thiolase) → TCA cycle
```

The **liver lacks thiophorase**, so it makes ketone bodies but cannot use them; it exports them to heart, muscle, kidney and, in prolonged fasting, the brain.

### When ketogenesis rises

Excess fatty acid breakdown with low oxaloacetate (oxaloacetate is diverted to gluconeogenesis), so acetyl-CoA cannot enter the TCA cycle: **starvation, uncontrolled diabetes mellitus (especially type 1), very low-carbohydrate diets, prolonged vomiting, alcoholism**.

### Ketoacidosis

Ketone bodies are acids. When their production exceeds use:

- **Ketonaemia** (high blood ketones) → **ketonuria** (in urine) → fruity smell of **acetone** in breath → together called **ketosis**.
- Acetoacetic and β-hydroxybutyric acids lower blood pH → **metabolic acidosis** (low bicarbonate, high anion gap), Kussmaul (deep, rapid) breathing, dehydration from osmotic diuresis, loss of sodium and potassium, coma.
- **Diabetic ketoacidosis** is treated with insulin, fluids and potassium replacement.
- Detected by **Rothera's test** (nitroprusside reacts with acetoacetate and acetone, not with β-hydroxybutyrate).

## 3.3 De novo synthesis of fatty acids (palmitic acid)

**Site**: cytosol of liver, adipose tissue, lactating mammary gland. Occurs in the fed state with excess carbohydrate.

### Steps

1. **Transfer of acetyl-CoA to the cytosol** — acetyl-CoA is made in mitochondria but cannot cross the membrane. It leaves as **citrate** (citrate shuttle); citrate lyase in the cytosol releases acetyl-CoA and oxaloacetate.
2. **Carboxylation (rate-limiting)** — acetyl-CoA + CO2 + ATP → **malonyl-CoA**, by **acetyl-CoA carboxylase** (needs **biotin**). Activated by citrate and insulin; inhibited by palmitoyl-CoA, glucagon and adrenaline.
3. **Fatty acid synthase complex** — a multi-enzyme dimer with an **acyl carrier protein (ACP)** carrying a phosphopantetheine arm. Each cycle adds two carbons from malonyl-CoA (releasing CO2) in four steps:

```text
Condensation   (acetyl + malonyl → β-ketoacyl-ACP, CO2 released)
Reduction      (NADPH → NADP+)       → β-hydroxyacyl-ACP
Dehydration    (− H2O)               → enoyl-ACP
Reduction      (NADPH → NADP+)       → acyl-ACP (chain longer by 2 C)
Repeat 7 times → palmitoyl-ACP → thioesterase → free palmitate (C16)
```

**Overall**: 8 acetyl-CoA + 7 ATP + 14 NADPH + 14 H+ → palmitate + 8 CoA + 7 ADP + 7 Pi + 14 NADP+ + 6 H2O

**Sources of NADPH**: HMP shunt (main) and **malic enzyme** (malate → pyruvate).

Longer and unsaturated fatty acids are made later by elongation (endoplasmic reticulum) and desaturation.

### β-Oxidation versus fatty acid synthesis

| Feature | β-Oxidation | De novo synthesis |
| --- | --- | --- |
| Site | Mitochondria | Cytosol |
| Carrier of acyl group | Coenzyme A | Acyl carrier protein |
| Two-carbon unit | Released as acetyl-CoA | Added from malonyl-CoA |
| Coenzymes | FAD, NAD+ (oxidised) | NADPH (reduced) |
| Key enzyme | Carnitine acyltransferase I | Acetyl-CoA carboxylase |
| Hormone favouring | Glucagon, adrenaline (fasting) | Insulin (fed state) |
| Isomer of hydroxy intermediate | L | D |

## 3.4 Cholesterol: biological significance and conversions

**Synthesis (brief)**: from acetyl-CoA in liver cytosol and ER: acetyl-CoA → HMG-CoA → **mevalonate** (by **HMG-CoA reductase**, the rate-limiting enzyme) → isoprene units → squalene → lanosterol → cholesterol (27 carbons). **Statins** (atorvastatin, rosuvastatin) competitively inhibit HMG-CoA reductase.

**Biological significance**

1. Part of cell membranes; controls fluidity.
2. Precursor of **bile acids**, **steroid hormones** and **vitamin D3**.
3. Carried in blood mainly by LDL (to tissues) and HDL (back to liver, "reverse cholesterol transport").
4. Excess deposits in arteries (atherosclerosis) and forms gallstones.

### Conversion to bile acids (liver)

```text
Cholesterol
  │ 7α-hydroxylase (rate-limiting; inhibited by bile acids)
7α-Hydroxycholesterol → primary bile acids: cholic acid and chenodeoxycholic acid
  │ conjugation with glycine or taurine
Bile salts (glycocholate, taurocholate) → bile → intestine
  │ intestinal bacteria
Secondary bile acids: deoxycholic acid and lithocholic acid
```

About 95% of bile salts are reabsorbed in the ileum and return to the liver (**enterohepatic circulation**). Bile salts emulsify fats and help absorb fats and fat-soluble vitamins; making bile acids is the main route of cholesterol removal. Bile acid sequestrants (cholestyramine) block reabsorption and lower blood cholesterol.

### Conversion to steroid hormones (adrenal cortex, gonads, placenta)

```text
Cholesterol
  │ side-chain cleavage enzyme (desmolase, CYP11A1; rate-limiting, in mitochondria)
Pregnenolone (C21)
  ├─► Progesterone (C21) ─► Corticosterone ─► Aldosterone (mineralocorticoid, zona glomerulosa)
  ├─► 17-OH progesterone ─► 11-Deoxycortisol ─► Cortisol (glucocorticoid, zona fasciculata)
  └─► DHEA / Androstenedione (C19) ─► Testosterone ─► Oestradiol (C18, by aromatase)
```

### Conversion to vitamin D3

```text
7-Dehydrocholesterol (skin)
  │ UV-B sunlight
Cholecalciferol (vitamin D3)
  │ 25-hydroxylase (liver)
25-Hydroxycholecalciferol (calcidiol; main circulating form, measured in blood)
  │ 1α-hydroxylase (kidney; stimulated by PTH and low phosphate)
1,25-Dihydroxycholecalciferol (calcitriol; active hormone)
```

Calcitriol raises intestinal absorption of calcium and phosphate. Lack causes rickets (children) and osteomalacia (adults); kidney failure causes deficiency of the active form.

## 3.5 Disorders of lipid metabolism

### Hypercholesterolaemia

Raised serum cholesterol. Desirable total cholesterol is below about 200 mg/dl and LDL cholesterol below about 100 mg/dl (targets vary with cardiovascular risk; ranges vary by laboratory).

- **Primary (familial)**: e.g. familial hypercholesterolaemia due to defective **LDL receptors** — LDL is not cleared, very high cholesterol, tendon xanthomas and early heart attacks.
- **Secondary**: diabetes, hypothyroidism, nephrotic syndrome, obstructive jaundice, diet rich in saturated fat.
- **Treatment**: diet, exercise, statins, ezetimibe (blocks absorption), bile acid sequestrants, PCSK9 inhibitors.

### Atherosclerosis

Thickening and hardening of arteries by deposits (plaques) of lipid, mainly cholesterol esters.

1. Injury to the endothelium (high LDL, smoking, hypertension, diabetes).
2. LDL enters the vessel wall and is **oxidised**.
3. Macrophages take up oxidised LDL → **foam cells** → fatty streak.
4. Smooth muscle cells migrate, fibrous cap forms → plaque narrows the lumen.
5. Plaque rupture → thrombus → myocardial infarction or stroke.

Risk factors: high LDL, low HDL, smoking, hypertension, diabetes, obesity, inactivity, family history. HDL is protective.

### Fatty liver

Excess triacylglycerol in liver cells.

**Causes**:

- **Excess fat supply**: starvation, uncontrolled diabetes, high-fat diet.
- **Poor export as VLDL**: lack of **lipotropic factors** (choline, methionine, betaine, inositol) needed for phospholipid and lipoprotein formation; protein deficiency (kwashiorkor).
- **Alcohol**: high NADH/NAD+ ratio favours fat synthesis and blocks β-oxidation.
- **Toxins**: carbon tetrachloride.
- **Non-alcoholic fatty liver disease**: linked to obesity and insulin resistance.

Can progress to fibrosis and cirrhosis.

### Obesity

Excess body fat that harms health. Measured by **body mass index (BMI)** = weight (kg) / height (m)².

- WHO: overweight 25–29.9, obese ≥ 30 kg/m².
- Lower cut-offs are used for Asian Indians: overweight ≥ 23, obese ≥ 25 kg/m².

**Causes**: energy intake exceeding expenditure; genetic factors (leptin or leptin-receptor defects in rare cases), hormonal causes (hypothyroidism, Cushing's syndrome), drugs (corticosteroids, some antipsychotics).

**Consequences**: type 2 diabetes, hypertension, dyslipidaemia, atherosclerosis, fatty liver, osteoarthritis, sleep apnoea.

## 3.6 General reactions of amino acid metabolism

### Transamination

Transfer of an α-amino group from an amino acid to an α-keto acid, forming a new amino acid and a new keto acid. Enzyme: **aminotransferases (transaminases)**; coenzyme: **pyridoxal phosphate (PLP, vitamin B6)**. Reversible.

```text
Alanine + α-Ketoglutarate ⇌ Pyruvate + Glutamate        (ALT, alanine aminotransferase)
Aspartate + α-Ketoglutarate ⇌ Oxaloacetate + Glutamate  (AST, aspartate aminotransferase)
```

**Significance**: collects nitrogen from most amino acids as glutamate; makes non-essential amino acids; links amino acid and carbohydrate metabolism. Serum ALT and AST are markers of liver (and AST also heart) damage. Lysine, threonine and proline do not take part.

### Deamination

Removal of the amino group as **ammonia**.

- **Oxidative deamination**: glutamate + NAD(P)+ + H2O → α-ketoglutarate + NH3 + NAD(P)H, by **glutamate dehydrogenase** (liver mitochondria). Transamination + oxidative deamination together = **transdeamination**, the main route for releasing amino nitrogen.
- **Non-oxidative deamination**: serine and threonine (dehydratases, PLP), histidine (histidase), cysteine (desulphydrase).

### Decarboxylation

Removal of CO2 from an amino acid to form an amine, by **decarboxylases** with **PLP**.

| Amino acid | Amine formed | Role |
| --- | --- | --- |
| Histidine | Histamine | Allergy, gastric acid, vasodilation |
| Glutamate | GABA | Inhibitory neurotransmitter |
| 5-Hydroxytryptophan | Serotonin (5-HT) | Neurotransmitter, vasoconstriction |
| DOPA | Dopamine | Neurotransmitter, precursor of noradrenaline |
| Ornithine | Putrescine | Polyamines for cell growth |

## 3.7 Urea cycle and its disorders

Ammonia is toxic to the brain. The liver converts it to non-toxic **urea**, excreted by the kidneys. **Site**: liver, partly in mitochondria and partly in cytosol (Krebs–Henseleit cycle).

```text
MITOCHONDRIA
NH3 + CO2 + 2 ATP ──► Carbamoyl phosphate
        (1) Carbamoyl phosphate synthetase I  [rate-limiting; activated by N-acetylglutamate]
Carbamoyl phosphate + Ornithine ──► Citrulline
        (2) Ornithine transcarbamoylase
                      │ citrulline moves to cytosol
CYTOSOL
Citrulline + Aspartate + ATP ──► Argininosuccinate (+ AMP + PPi)
        (3) Argininosuccinate synthetase
Argininosuccinate ──► Arginine + Fumarate  (fumarate → TCA cycle: "Krebs bicycle")
        (4) Argininosuccinate lyase
Arginine + H2O ──► Urea + Ornithine (ornithine returns to mitochondria)
        (5) Arginase
```

**Sources of the two nitrogen atoms of urea**: one from **ammonia** (via carbamoyl phosphate), one from **aspartate**. The carbon comes from CO2.

**Energy**: 3 ATP are used but **4 high-energy bonds** (ATP → AMP + PPi in step 3).

**Overall**: NH3 + CO2 + aspartate + 3 ATP + H2O → urea + fumarate + 2 ADP + AMP + 2 Pi + PPi

**Disorders** (all cause hyperammonaemia: vomiting, lethargy, convulsions, mental retardation, coma):

| Disorder | Enzyme deficient |
| --- | --- |
| Hyperammonaemia type I | Carbamoyl phosphate synthetase I |
| Hyperammonaemia type II (most common; X-linked) | Ornithine transcarbamoylase (orotic acid in urine) |
| Citrullinaemia | Argininosuccinate synthetase |
| Argininosuccinic aciduria | Argininosuccinate lyase |
| Hyperargininaemia | Arginase |

**Management**: low-protein diet; sodium benzoate and phenylbutyrate (remove nitrogen as hippurate and phenylacetylglutamine); arginine supplements in some types; lactulose (used for hepatic encephalopathy) reduces ammonia absorption from the gut.

## 3.8 Catabolism of phenylalanine and tyrosine, and their disorders

```text
Phenylalanine
  │ Phenylalanine hydroxylase (needs tetrahydrobiopterin, BH4)      ✗ Phenylketonuria
Tyrosine ─────────► Melanocytes: tyrosinase → DOPA → melanin       ✗ Albinism
  │               ─► Catecholamines, thyroid hormones
  │ Tyrosine aminotransferase (PLP)                                  ✗ Tyrosinaemia type II
p-Hydroxyphenylpyruvate
  │ p-Hydroxyphenylpyruvate dioxygenase (needs vitamin C)
Homogentisate
  │ Homogentisate oxidase (dioxygenase)                              ✗ Alkaptonuria
Maleylacetoacetate
  │ Isomerase
Fumarylacetoacetate
  │ Fumarylacetoacetate hydrolase                                    ✗ Tyrosinaemia type I
Fumarate (→ glucose)  +  Acetoacetate (→ ketone body)
```

So phenylalanine and tyrosine are **both glucogenic and ketogenic**.

### Metabolic disorders

| Disorder | Enzyme defect | Features | Notes |
| --- | --- | --- | --- |
| **Phenylketonuria (PKU)** | Phenylalanine hydroxylase (classic); rarely BH4 deficiency | Phenylalanine builds up and forms phenylpyruvate, phenyllactate, phenylacetate (mousy odour of urine); mental retardation, seizures; fair skin and hair (less melanin) | Ferric chloride test gives green colour; newborn screening (Guthrie test); low-phenylalanine diet from birth; tyrosine becomes essential |
| **Albinism** | Tyrosinase (melanocytes) | No melanin: white hair, pale skin, light eyes, photophobia, high skin cancer risk | Catecholamine synthesis is normal (different enzyme) |
| **Alkaptonuria** | Homogentisate oxidase | Urine darkens on standing (homogentisate oxidised); **ochronosis** (dark pigment in cartilage, ears, sclera); arthritis in later life | Usually benign early; Benedict's test may be falsely positive |
| **Tyrosinaemia type I** (hepatorenal) | Fumarylacetoacetate hydrolase | Liver failure, kidney tubular defects, cabbage-like odour | Treated with nitisinone (blocks an earlier step) and diet |
| **Tyrosinaemia type II** (oculocutaneous) | Tyrosine aminotransferase | Eye lesions, skin lesions on palms and soles, mental retardation | Low-tyrosine diet |

## 3.9 Synthesis and significance of biological amines

### Catecholamines (dopamine, noradrenaline, adrenaline)

```text
Tyrosine
  │ Tyrosine hydroxylase (BH4; rate-limiting)
L-DOPA
  │ DOPA decarboxylase (aromatic L-amino acid decarboxylase, PLP)
Dopamine
  │ Dopamine β-hydroxylase (vitamin C, copper)
Noradrenaline (norepinephrine)
  │ Phenylethanolamine N-methyltransferase (S-adenosylmethionine; adrenal medulla, induced by cortisol)
Adrenaline (epinephrine)
```

Broken down by **monoamine oxidase (MAO)** and **catechol-O-methyltransferase (COMT)**; main urinary product **vanillylmandelic acid (VMA)**, raised in phaeochromocytoma; dopamine → homovanillic acid (HVA).

| Amine | Significance |
| --- | --- |
| Dopamine | Neurotransmitter for movement, reward and prolactin control; lack in Parkinson's disease (treated with levodopa + carbidopa, which blocks peripheral decarboxylation); excess activity linked to schizophrenia; renal vasodilator (used in shock) |
| Noradrenaline | Sympathetic neurotransmitter; raises blood pressure (vasoconstriction); used in septic shock |
| Adrenaline | Hormone of "fight or flight": raises heart rate, blood glucose and lipolysis; bronchodilation; drug of choice in anaphylaxis |

### Serotonin (5-HT) and melatonin

```text
Tryptophan
  │ Tryptophan hydroxylase (BH4; rate-limiting)
5-Hydroxytryptophan
  │ Aromatic L-amino acid decarboxylase (PLP)
Serotonin (5-hydroxytryptamine, 5-HT)
  │ N-acetyltransferase (pineal gland; active at night)
N-Acetylserotonin
  │ Hydroxyindole-O-methyltransferase (S-adenosylmethionine)
Melatonin
```

- **Serotonin**: found in the gut (enterochromaffin cells), platelets and brain. Neurotransmitter for mood, sleep, appetite; causes vasoconstriction and gut movement. Broken down by MAO to **5-hydroxyindoleacetic acid (5-HIAA)**, raised in urine in carcinoid tumour. Low brain serotonin is linked to depression (SSRIs such as fluoxetine raise it).
- **Melatonin**: made in the pineal gland in darkness; regulates the sleep–wake (circadian) rhythm; used for jet lag and some sleep problems; an antioxidant.

## 3.10 Catabolism of heme; hyperbilirubinaemia and jaundice

Red cells live about **120 days**; old cells are destroyed in the reticuloendothelial system (spleen, liver, bone marrow). Globin returns to the amino acid pool; iron is reused (transferrin, ferritin); heme is degraded to **bilirubin**.

```text
Heme
  │ Heme oxygenase (microsomal; O2, NADPH)  → releases Fe and CO
Biliverdin (green)
  │ Biliverdin reductase (NADPH)
Bilirubin (yellow, unconjugated, water-insoluble)
  │ carried in blood bound to albumin (some drugs, e.g. sulphonamides, displace it)
LIVER: uptake → conjugation with glucuronic acid
  │ UDP-glucuronyl transferase
Bilirubin diglucuronide (conjugated, water-soluble) → secreted into bile
  │ intestinal bacteria
Urobilinogen (colourless)
  ├─► most → stercobilinogen → stercobilin (brown colour of faeces)
  └─► part reabsorbed → liver (enterohepatic) and a little → kidney → urobilin in urine
```

Normal serum total bilirubin is about **0.2–1.0 mg/dl** (ranges vary by laboratory). **Hyperbilirubinaemia** is a level above normal; **jaundice** (icterus — yellow skin and sclera) becomes visible above about **2–2.5 mg/dl**.

### Types of jaundice

| Feature | Pre-hepatic (haemolytic) | Hepatic (hepatocellular) | Post-hepatic (obstructive) |
| --- | --- | --- | --- |
| Cause | Excess red cell breakdown (haemolytic anaemia, malaria, G6PD deficiency, incompatible transfusion) | Liver cell damage (viral hepatitis, alcohol, drugs such as paracetamol overdose) | Block of bile flow (gallstones, carcinoma head of pancreas) |
| Main bilirubin raised | Unconjugated | Both | Conjugated |
| Bilirubin in urine | Absent (acholuric) | Present | Present (dark urine) |
| Urobilinogen in urine | Increased | Variable | Absent |
| Stool colour | Dark | Normal or pale | Clay-coloured (pale) |
| Liver enzymes | Normal | ALT and AST markedly raised | ALP and GGT markedly raised |

**Inherited and neonatal hyperbilirubinaemias**

- **Neonatal (physiological) jaundice**: immature UDP-glucuronyl transferase in newborns; high unconjugated bilirubin can cross the immature blood–brain barrier and cause **kernicterus**; treated with phototherapy.
- **Gilbert syndrome**: mild reduction of conjugation; harmless.
- **Crigler–Najjar syndrome**: severe (type I, absent enzyme) or partial (type II) lack of UDP-glucuronyl transferase.
- **Dubin–Johnson syndrome**: defective secretion of conjugated bilirubin; dark liver.

## Remember

- β-Oxidation: activation (2 ATP), carnitine shuttle (CPT-I rate-limiting, inhibited by malonyl-CoA), 4 steps OHOT; palmitate = 7 cycles → 8 acetyl-CoA, 7 FADH2, 7 NADH = **106 ATP (newer) / 129 ATP (older)**.
- Ketone bodies made in liver (HMG-CoA synthase), used outside it (thiophorase absent in liver); ketoacidosis in diabetes and starvation.
- Fatty acid synthesis: cytosol, acetyl-CoA carboxylase (biotin) rate-limiting, malonyl-CoA donor, NADPH from HMP shunt, ends at palmitate.
- Cholesterol: HMG-CoA reductase (statins); → bile acids (7α-hydroxylase), steroids (desmolase → pregnenolone), vitamin D (skin UV, liver 25-, kidney 1α-hydroxylation).
- Transamination needs PLP; glutamate dehydrogenase releases NH3; decarboxylation gives amines.
- Urea cycle: CPS-I (N-acetylglutamate) and OTC in mitochondria; ASS, ASL, arginase in cytosol; 4 high-energy bonds per urea; OTC deficiency is the most common disorder.
- PKU = phenylalanine hydroxylase; alkaptonuria = homogentisate oxidase; albinism = tyrosinase; tyrosinaemia I = fumarylacetoacetate hydrolase.
- Tyrosine → DOPA → dopamine → noradrenaline → adrenaline; tryptophan → 5-HTP → 5-HT → N-acetylserotonin → melatonin.
- Heme → biliverdin → bilirubin (albumin) → glucuronide in liver → urobilinogen → stercobilin; obstructive jaundice = clay stools, bilirubin in urine, no urobilinogen.
