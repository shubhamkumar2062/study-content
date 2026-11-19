# Unit 5: Enzymes

Enzymes are the catalysts of life. For a pharmacy student they matter in three ways: many drugs work by inhibiting an enzyme, many diseases are diagnosed by measuring enzymes in blood, and several enzymes are themselves medicines. This unit covers the nature, naming and classification of enzymes, their kinetics, inhibition and regulation, their therapeutic and diagnostic uses with isoenzymes, and the coenzymes made from B vitamins.

## 5.1 Introduction

**Definition.** Enzymes are biological catalysts, almost all proteins, that speed up chemical reactions in living cells without being used up. (A few catalytic RNAs, called **ribozymes**, also exist — e.g. the peptidyl transferase of the ribosome.)

**Terms**

- **Substrate (S)**: the molecule acted on.
- **Active site**: a small pocket or cleft on the enzyme, formed by a few amino acid side chains, where the substrate binds and the reaction occurs.
- **Apoenzyme**: the protein part alone (inactive).
- **Cofactor**: a non-protein part needed for activity —
  - a metal ion (activator: Zn2+, Mg2+, Fe2+, Cu2+); or
  - an organic **coenzyme** (often a B vitamin derivative).
  - A tightly bound cofactor is called a **prosthetic group**.
- **Holoenzyme** = apoenzyme + cofactor (active).
- **Proenzyme (zymogen)**: inactive precursor activated by cutting the chain (pepsinogen → pepsin, trypsinogen → trypsin, clotting factors).

## 5.2 Properties of enzymes

1. **Catalytic efficiency** — they increase reaction rates by a factor of millions or more and work at body temperature and neutral pH.
2. **Lower the activation energy** — they do not change the equilibrium position or ΔG of a reaction; they only help it reach equilibrium faster.
3. **Not consumed** — the enzyme is released unchanged after each cycle; small amounts suffice.
4. **Specificity**:
   - **Absolute** — one substrate only (urease acts only on urea).
   - **Group** — a type of bond with particular neighbouring groups (trypsin cuts after lysine or arginine).
   - **Bond (linkage)** — one type of bond (lipase on ester bonds).
   - **Stereo** — one optical isomer (L-amino acid oxidase; enzymes of glucose metabolism act on D-glucose).
5. **Mechanism of binding**:
   - **Lock and key model** (Fischer) — the active site is a rigid shape that fits the substrate.
   - **Induced fit model** (Koshland) — the active site changes shape when the substrate binds, giving a closer fit; this explains broader specificity and allosteric effects.
6. **Sensitive to temperature** — activity rises with temperature up to an **optimum** (about 37–40 °C for most human enzymes), then falls because the protein is denatured; enzymes are inactive in the cold but not destroyed.
7. **Sensitive to pH** — each enzyme has an **optimum pH**: pepsin about 1.5–2, salivary amylase about 6.8, trypsin about 8, alkaline phosphatase about 9–10.
8. **Can be regulated** — by inhibitors, activators, allosteric effectors, covalent modification and changes in amount.
9. Many need **cofactors**; some are made as zymogens.

**Factors affecting enzyme activity**: enzyme concentration (rate is proportional to it), substrate concentration (saturation — see kinetics), temperature, pH, product concentration (product inhibition), activators, inhibitors, time and light or radiation.

## 5.3 Nomenclature and IUB classification

**Old (trivial) names**: suffix **-ase** added to the substrate (urease, lipase, sucrase) or the reaction (dehydrogenase, transaminase); some names give no clue (pepsin, trypsin, rennin).

**Systematic (IUB) naming**: the International Union of Biochemistry (now IUBMB) gives each enzyme a four-part **Enzyme Commission (EC) number**, e.g. EC 2.7.1.1 for hexokinase:

- first digit = class;
- second = subclass;
- third = sub-subclass;
- fourth = serial number.

### The six classes

| EC class | Name | Reaction type | Examples |
| --- | --- | --- | --- |
| 1 | **Oxidoreductases** | Oxidation–reduction (transfer of H or electrons) | Lactate dehydrogenase, alcohol dehydrogenase, cytochrome oxidase, xanthine oxidase, catalase |
| 2 | **Transferases** | Transfer of a group (amino, phosphate, methyl) | ALT and AST (transaminases), hexokinase, creatine kinase, COMT |
| 3 | **Hydrolases** | Breaking of bonds by adding water | Pepsin, trypsin, lipase, amylase, urease, acetylcholinesterase, phosphatases |
| 4 | **Lyases** | Removal or addition of a group without water or oxidation (often forming double bonds) | Aldolase, fumarase, carbonic anhydrase, decarboxylases |
| 5 | **Isomerases** | Rearrangement within a molecule | Triose phosphate isomerase, phosphoglucomutase, epimerases, racemases |
| 6 | **Ligases (synthetases)** | Joining two molecules using ATP | Glutamine synthetase, pyruvate carboxylase, acetyl-CoA carboxylase, DNA ligase |

Memory aid: **OTHLIL** — Oh The Hot Lady Is Lovely.

Note: in 2018 the IUBMB added a seventh class, **translocases** (enzymes that move ions or molecules across membranes). PCI examinations normally expect the six classes above.

## 5.4 Enzyme kinetics

### Effect of substrate concentration: Michaelis–Menten plot

At a fixed enzyme concentration, the rate (velocity, v) rises with substrate concentration [S] — steeply at first, then levelling off — because the enzyme becomes **saturated** with substrate. The plot is a **rectangular hyperbola**.

```text
v │                  ______________ Vmax
  │             ____/
  │          __/
  │        _/
Vmax/2 ┼ - -/
  │     /|
  │    / |
  │   /  |
  │  /   |
  │ /    |
  └/─────┼──────────────────────── [S]
         Km
```

**Michaelis–Menten equation** (for E + S ⇌ ES → E + P):

**v = Vmax [S] / (Km + [S])**

- **Vmax** — the maximum velocity when all enzyme is saturated with substrate; depends on enzyme amount.
- **Km (Michaelis constant)** — the **substrate concentration at which velocity is half of Vmax**. Units: mol/l.
- **Meaning of Km**: a measure of the enzyme's **affinity** for its substrate. **Low Km = high affinity** (half-saturated at low [S]); high Km = low affinity.
  - Example: hexokinase (low Km for glucose) works even at low blood glucose; liver glucokinase (high Km) acts only after meals.
- When [S] = Km, v = Vmax/2. When [S] is much less than Km, v is proportional to [S] (first order). When [S] is much greater than Km, v ≈ Vmax (zero order).

### Lineweaver–Burk (double reciprocal) plot

Taking reciprocals of the Michaelis–Menten equation gives a straight line:

**1/v = (Km/Vmax) × (1/[S]) + 1/Vmax**

```text
1/v │                      /
    │                    /
    │                  /   slope = Km/Vmax
    │                /
    │              /
    │            /
    │          /
    │        /  ← y-intercept = 1/Vmax
    │      /
────┼────/────────────────────── 1/[S]
    │  ↑
  x-intercept = −1/Km
```

**Advantages**: Km and Vmax are read accurately from the intercepts (the hyperbola only approaches Vmax); the type of inhibition is easy to recognise. **Drawback**: points at low [S] are spread far out and carry the most error.

**Worked example.** A Lineweaver–Burk plot has y-intercept 0.02 min/µmol and x-intercept −0.5 mM⁻¹. Then Vmax = 1/0.02 = **50 µmol/min** and Km = 1/0.5 = **2 mM**.

## 5.5 Enzyme inhibitors with examples

An inhibitor is a substance that reduces the rate of an enzyme reaction.

```text
Enzyme inhibition
├── Reversible
│     ├── Competitive
│     ├── Non-competitive
│     └── Uncompetitive
├── Irreversible
├── Suicide (mechanism-based) inhibition
└── Allosteric (feedback) inhibition
```

### Competitive inhibition

- Inhibitor **resembles the substrate** and competes for the active site.
- Can be overcome by adding more substrate.
- **Km increases** (apparent affinity falls); **Vmax unchanged**.
- Lineweaver–Burk: lines meet on the **y-axis**.

| Inhibitor | Enzyme | Use |
| --- | --- | --- |
| Malonate | Succinate dehydrogenase | Classic laboratory example |
| Statins (atorvastatin) | HMG-CoA reductase | Lower cholesterol |
| Methotrexate | Dihydrofolate reductase | Cancer, rheumatoid arthritis |
| Sulphonamides | Dihydropteroate synthase (bacterial; PABA analogue) | Antibacterial |
| Allopurinol | Xanthine oxidase | Gout |
| Ethanol | Alcohol dehydrogenase (competes with methanol, ethylene glycol) | Antidote |
| Neostigmine, physostigmine | Acetylcholinesterase (reversible carbamate inhibitors) | Myasthenia gravis, glaucoma |
| Captopril, enalapril | Angiotensin-converting enzyme | Hypertension |
| Dicoumarol, warfarin | Vitamin K epoxide reductase | Anticoagulant |

### Non-competitive inhibition

- Inhibitor binds a site **other than** the active site, to both E and ES.
- Not reversed by more substrate.
- **Vmax decreases**; **Km unchanged**.
- Lineweaver–Burk: lines meet on the **x-axis**.
- Examples: heavy metal ions (Hg2+, Pb2+, Ag+) binding –SH groups; cyanide on cytochrome oxidase.

### Uncompetitive inhibition

- Inhibitor binds **only the ES complex**.
- **Both Km and Vmax decrease**.
- Lineweaver–Burk: **parallel** lines.
- Example: L-phenylalanine on placental alkaline phosphatase.

### Irreversible inhibition

Inhibitor forms a **covalent** bond with the enzyme, destroying activity permanently; recovery needs new enzyme.

| Inhibitor | Enzyme |
| --- | --- |
| Organophosphates (malathion, parathion, nerve gases, diisopropyl fluorophosphate) | Acetylcholinesterase (serine phosphorylated); pralidoxime can reactivate it if given early |
| **Aspirin** | Cyclooxygenase (acetylates serine) — basis of the long antiplatelet effect |
| Iodoacetate | Glyceraldehyde-3-phosphate dehydrogenase (–SH) |
| Fluoride | Enolase (with Mg2+ and phosphate) |
| Penicillins | Bacterial transpeptidase (cell wall) |

### Suicide (mechanism-based) inhibition

The enzyme itself converts an inactive inhibitor into a reactive form that then binds it irreversibly.

- **Allopurinol** → oxypurinol (xanthine oxidase).
- **5-Fluorouracil** → fluoro-dUMP (thymidylate synthase).
- **Clavulanic acid** (β-lactamase).
- **Eflornithine** / difluoromethylornithine (ornithine decarboxylase).

### Summary for the exam

| Type | Binds to | Km | Vmax | Lineweaver–Burk |
| --- | --- | --- | --- | --- |
| Competitive | Active site (E) | Increases | Same | Lines meet on y-axis |
| Non-competitive | Other site (E and ES) | Same | Decreases | Lines meet on x-axis |
| Uncompetitive | ES only | Decreases | Decreases | Parallel lines |
| Irreversible | Covalent | — | Decreases (enzyme lost) | Like non-competitive |

**Importance in drug design**: a large share of drugs are enzyme inhibitors. Knowing the substrate and mechanism lets chemists design **substrate analogues** (competitive) or **transition-state analogues**. Examples: HIV protease inhibitors, ACE inhibitors, COX-2 inhibitors, proton pump inhibitors (irreversible H+/K+-ATPase inhibitors), MAO inhibitors.

## 5.6 Regulation of enzymes

Cells control enzyme activity in two broad ways: by changing **activity** (fast — seconds to minutes) or **amount** (slow — hours to days).

### 1. Allosteric regulation

**Allosteric enzymes** have, besides the active site, a separate **regulatory (allosteric) site** where an **effector** binds and changes the enzyme's shape.

- **Positive effectors (activators)** raise activity; **negative effectors (inhibitors)** lower it.
- Usually multi-subunit enzymes; show **sigmoid (S-shaped)** v-versus-[S] curves (cooperativity) instead of a hyperbola, and do not obey Michaelis–Menten kinetics.
- Usually catalyse the **first committed (rate-limiting) step** of a pathway.
- **Feedback inhibition**: the end product of a pathway inhibits the first enzyme (CTP inhibits aspartate transcarbamoylase; cholesterol inhibits HMG-CoA reductase).

| Allosteric enzyme | Activator | Inhibitor |
| --- | --- | --- |
| Phosphofructokinase-1 | AMP, fructose-2,6-bisphosphate | ATP, citrate |
| Aspartate transcarbamoylase | ATP | CTP |
| Acetyl-CoA carboxylase | Citrate | Palmitoyl-CoA |
| Pyruvate carboxylase | Acetyl-CoA | — |
| Carbamoyl phosphate synthetase I | N-acetylglutamate | — |

```text
v │        Michaelis–Menten (hyperbola)
  │      ___________
  │    /    ___------  allosteric (sigmoid)
  │   /   /
  │  /   /
  │ /  _/
  │/__/
  └────────────────── [S]
```

### 2. Covalent modification

Adding or removing a chemical group switches enzymes on or off, mostly by **phosphorylation** (protein kinases) and **dephosphorylation** (phosphatases). Example: glucagon → cAMP → protein kinase A → glycogen phosphorylase phosphorylated (**active**), glycogen synthase phosphorylated (**inactive**).

### 3. Proteolytic activation of zymogens

Irreversible: pepsinogen → pepsin, trypsinogen → trypsin (by enteropeptidase), chymotrypsinogen → chymotrypsin, prothrombin → thrombin.

### 4. Enzyme induction and repression (control of enzyme amount)

- **Induction**: a substance (inducer) increases the **synthesis** of an enzyme at the level of gene transcription.
  - Classic model: the **lac operon** of E. coli (Jacob and Monod) — when lactose is present it removes the repressor, and the genes for lactose use are transcribed.
  - In humans: insulin induces glucokinase and the enzymes of fat synthesis; cortisol induces gluconeogenic enzymes (PEPCK) and tyrosine aminotransferase.
  - **Drug-metabolising enzymes (cytochrome P450)** are induced by phenobarbitone, rifampicin, phenytoin, carbamazepine and smoking — this speeds the breakdown of other drugs (important drug interactions, e.g. failure of oral contraceptives with rifampicin). Barbiturates induce δ-aminolevulinate synthase (worsening porphyria).
- **Repression**: the end product of a pathway (co-repressor) decreases the synthesis of its enzymes. Examples: heme represses δ-ALA synthase; cholesterol represses HMG-CoA reductase; tryptophan represses the trp operon in bacteria.
- **Degradation**: enzyme amount also depends on the rate of breakdown.

### 5. Other mechanisms

Compartmentation (β-oxidation in mitochondria, fatty acid synthesis in cytosol), isoenzymes with different properties in different tissues, and multi-enzyme complexes.

## 5.7 Isoenzymes

**Isoenzymes (isozymes)** are physically distinct forms of an enzyme that catalyse the **same reaction** but differ in amino acid composition, electrophoretic mobility, kinetic properties (Km), heat stability, tissue distribution and response to inhibitors. They come from different genes or from different combinations of subunits. They are separated by **electrophoresis**.

### Lactate dehydrogenase (LDH) — tetramer of H (heart) and M (muscle) subunits

| Isoenzyme | Subunits | Main tissue |
| --- | --- | --- |
| LDH-1 | H4 | Heart, red cells, kidney |
| LDH-2 | H3M | Heart, red cells (highest in normal serum) |
| LDH-3 | H2M2 | Lungs, other tissues |
| LDH-4 | HM3 | Liver, muscle |
| LDH-5 | M4 | Liver, skeletal muscle |

In myocardial infarction, LDH-1 exceeds LDH-2 (**"flipped pattern"**). In liver disease, LDH-5 rises.

### Creatine kinase (CK) — dimer of B (brain) and M (muscle) subunits

| Isoenzyme | Main tissue | Raised in |
| --- | --- | --- |
| CK-1 (BB) | Brain | Brain injury |
| CK-2 (MB) | Heart | **Myocardial infarction** |
| CK-3 (MM) | Skeletal muscle | Muscle injury, muscular dystrophy, intramuscular injections |

### Alkaline phosphatase (ALP)

Liver, bone, placental (heat-stable, Regan isoenzyme in some cancers) and intestinal forms. Bone ALP rises in growing children, rickets, Paget's disease; liver ALP in obstructive jaundice.

## 5.8 Diagnostic applications of enzymes

Most diagnostic enzymes are released from damaged cells into the blood. A rise in a serum enzyme points to injury of the tissue that contains it. Approximate adult reference values are given; **ranges vary by laboratory and method**.

| Enzyme | About normal (adult serum) | Raised in |
| --- | --- | --- |
| **ALT (SGPT)** | Up to about 40 U/l | Liver disease (more specific for liver), viral hepatitis |
| **AST (SGOT)** | Up to about 40 U/l | Liver disease, myocardial infarction, muscle injury |
| **ALP** | About 40–130 U/l in adults (higher in children) | Obstructive jaundice, bone disease (rickets, Paget's, bone metastases) |
| **GGT** | Up to about 50 U/l | Alcohol abuse, cholestasis, enzyme-inducing drugs |
| **CK and CK-MB** | Total CK varies widely by sex and muscle mass | Myocardial infarction (CK-MB), muscle disease |
| **LDH** | Varies widely by method | MI (LDH-1), haemolysis, liver disease, some cancers |
| **Amylase and lipase** | Method-dependent | Acute pancreatitis (lipase more specific; amylase also in mumps) |
| **Acid phosphatase** | Method-dependent | Prostate cancer (now largely replaced by PSA) |
| **Pseudocholinesterase** | Method-dependent | Low in organophosphate poisoning, liver disease; inherited deficiency causes prolonged apnoea after suxamethonium |
| **G6PD (red cell)** | — | Low in G6PD deficiency (test before primaquine) |

**Myocardial infarction** — the enzymes rise in a time sequence: CK-MB first (within hours), then AST, then LDH, which stays raised longest. Cardiac **troponins** (not enzymes) are now the preferred markers.

**Enzymes as laboratory reagents**: glucose oxidase–peroxidase (blood glucose), cholesterol oxidase (cholesterol), urease (urea), uricase (uric acid), and enzyme labels in ELISA (horseradish peroxidase, alkaline phosphatase). Restriction enzymes and DNA polymerase (Taq) are tools of genetic engineering and PCR.

## 5.9 Therapeutic applications of enzymes

| Enzyme | Use |
| --- | --- |
| **Streptokinase, urokinase, alteplase (tissue plasminogen activator)** | Thrombolytics: dissolve clots in acute myocardial infarction, stroke (alteplase), pulmonary embolism |
| **L-Asparaginase** | Acute lymphoblastic leukaemia — leukaemic cells cannot make asparagine and starve |
| **Pancreatin / pancrelipase** (lipase, amylase, protease) | Digestive aid in pancreatic insufficiency, cystic fibrosis |
| **Hyaluronidase** | Increases spread and absorption of drugs given by injection (subcutaneous fluids, local anaesthetics) |
| **Dornase alfa (DNase)** | Breaks down DNA in thick sputum in cystic fibrosis |
| **Papain, bromelain, trypsin–chymotrypsin, serratiopeptidase** | Debridement of wounds; used to reduce swelling and inflammation |
| **Collagenase** | Debridement of burns and ulcers; Dupuytren's contracture |
| **Rasburicase** | Lowers uric acid in tumour lysis syndrome |
| **Imiglucerase** (glucocerebrosidase) | Enzyme replacement in Gaucher's disease |
| **Lysozyme** | Antibacterial (in some preparations) |
| **Lactase** | Lactose intolerance |

Enzymes as drugs have limits: they are proteins, so they can provoke allergy (streptokinase), are destroyed in the stomach if taken orally (unless protected or acting in the gut), and are expensive.

## 5.10 Coenzymes: structure and biochemical functions

**Coenzymes** are small, heat-stable organic molecules that work with an apoenzyme, usually carrying a group, hydrogen atoms or electrons from one reaction to another. Most are derived from **B-complex vitamins**.

| Coenzyme | Vitamin | Structure in brief | Function (group carried) | Example enzymes |
| --- | --- | --- | --- | --- |
| **Thiamine pyrophosphate (TPP)** | B1 (thiamine) | Pyrimidine ring + thiazole ring + two phosphates; reactive C2 of thiazole | Oxidative decarboxylation of α-keto acids; transfer of 2-carbon units | Pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, transketolase |
| **FMN, FAD** | B2 (riboflavin) | Isoalloxazine ring + ribitol; FMN = riboflavin phosphate; FAD = FMN + AMP | Hydrogen (2H) carrier in oxidation–reduction | Succinate dehydrogenase, acyl-CoA dehydrogenase, Complex I (FMN), xanthine oxidase |
| **NAD+, NADP+** | B3 (niacin) | Nicotinamide–ribose–P–P–ribose–adenine; NADP+ has an extra phosphate on the adenosine ribose (2′-OH); reactive C4 of nicotinamide | Hydride (H−) carrier; NAD+ mostly in catabolism, NADPH in synthesis | Lactate dehydrogenase, G6PD, glutamate dehydrogenase |
| **Coenzyme A (CoA–SH)** | B5 (pantothenic acid) | β-Mercaptoethylamine + pantothenic acid + 3′-phospho-ADP; reactive –SH forms thioesters | Acyl (acetyl) group carrier | Pyruvate dehydrogenase, thiolase, citrate synthase |
| **Pyridoxal phosphate (PLP)** | B6 (pyridoxine) | Pyridine ring with an aldehyde at C4 (forms a Schiff base with amino groups) + phosphate | Amino acid metabolism | Transaminases (ALT, AST), decarboxylases, glycogen phosphorylase, δ-ALA synthase |
| **Biotin (carboxybiotin)** | B7 (biotin) | Fused imidazole and thiophene rings with a valeric acid side chain, bound to lysine of the enzyme | CO2 carrier (carboxylation) | Pyruvate carboxylase, acetyl-CoA carboxylase, propionyl-CoA carboxylase |
| **Tetrahydrofolate (THF)** | B9 (folic acid) | Pteridine + p-aminobenzoic acid + glutamate, reduced at four positions | One-carbon units (methyl, methylene, formyl) | Thymidylate synthase, purine synthesis |
| **Methylcobalamin, deoxyadenosylcobalamin** | B12 (cobalamin) | Corrin ring with central cobalt | Methyl transfer; intramolecular rearrangement | Methionine synthase, methylmalonyl-CoA mutase |
| **Lipoic acid** | (not a vitamin) | Eight-carbon fatty acid with a disulphide | Acyl and hydrogen carrier | Pyruvate and α-ketoglutarate dehydrogenases |
| **Coenzyme Q (ubiquinone)** | (not a vitamin) | Quinone ring with a long isoprene tail | Electron carrier in the ETC | Complexes I, II → III |

**Clinical links**

- **Thiamine deficiency** (beriberi, Wernicke encephalopathy in alcoholics): pyruvate and lactate build up, and red cell transketolase activity falls.
- **Isoniazid** causes B6 deficiency (peripheral neuropathy), so pyridoxine is given with it.
- Raw egg white **avidin** binds biotin.
- **Methotrexate** and **trimethoprim** block folate reduction.
- B12 or folate deficiency causes **megaloblastic anaemia**.

## Remember

- Enzymes lower activation energy; they do not alter equilibrium or ΔG.
- Holoenzyme = apoenzyme + cofactor; zymogens are inactive precursors.
- IUB classes: oxidoreductases, transferases, hydrolases, lyases, isomerases, ligases (OTHLIL); EC numbers have four digits.
- v = Vmax[S]/(Km + [S]); Km = [S] at half Vmax; low Km = high affinity.
- Lineweaver–Burk: y-intercept 1/Vmax, x-intercept −1/Km, slope Km/Vmax.
- Competitive: Km ↑, Vmax same (statins, methotrexate, malonate); non-competitive: Vmax ↓, Km same (heavy metals); uncompetitive: both ↓.
- Irreversible: organophosphates (AChE), aspirin (COX); suicide: allopurinol, 5-FU, clavulanic acid.
- Allosteric enzymes: sigmoid curve, regulatory site, feedback inhibition (PFK-1, ATCase).
- Induction: lac operon; CYP450 induced by rifampicin, phenobarbitone; repression: heme on ALA synthase.
- Isoenzymes: LDH (5; LDH-1 > LDH-2 in MI), CK (BB, MB, MM; CK-MB in MI).
- Therapeutic enzymes: streptokinase, alteplase, asparaginase, hyaluronidase, pancreatin, dornase alfa.
- Coenzymes: TPP (B1), FAD (B2), NAD (B3), CoA (B5), PLP (B6), biotin (B7), THF (B9), cobalamin (B12).
