# Unit 3: Titrimetric analysis — acid–base, non-aqueous, precipitation, gravimetry, complexometric and redox

This is the largest unit of the course (14 lecture hours) and the heart of the practical work. It covers all five families of titration used in the Indian Pharmacopoeia (IP) and the classical weighing method, gravimetry. For each method learn four things: the **principle (equation)**, the **titrant and how it is standardised**, the **indicator and end point**, and **one IP assay with its equivalence factor**. All equivalence factors below are worked from the balanced equation, so you can rebuild them in the exam.

How to build any equivalence factor:

```text
 g of substance per ml of titrant
   = molar mass of substance × molarity of titrant × (mol substance per mol titrant) ÷ 1000

 % purity = (titre in ml × f × factor × 100) ÷ weight of sample in g
 (f = actual molarity ÷ nominal molarity of the titrant)
```

## Part A: Acid–base titrations

### 3.1 Theories of acid–base indicators

An **acid–base indicator** is a weak organic acid or base whose ionised and un-ionised forms have different colours. It changes colour over a narrow pH range (about 2 pH units).

**1. Ostwald's theory (ionisation theory).** The indicator is a weak acid HIn (or weak base) whose un-ionised molecule and ion differ in colour.

```text
 HIn  ⇌  H⁺  +  In⁻         KIn = [H⁺][In⁻]/[HIn]
 colour A      colour B      pH = pKIn + log([In⁻]/[HIn])
```

- Phenolphthalein: HIn colourless, In⁻ pink. In acid, H⁺ pushes the equilibrium left (colourless); in alkali, OH⁻ removes H⁺ and the pink ion forms.
- The eye sees one colour when one form is about 10 times the other, so the visible change happens between pH = pKIn − 1 and pKIn + 1.

**2. Quinonoid (chromophore) theory.** The two forms of the indicator are different structures (tautomers): a **benzenoid** form (usually colourless or light) and a **quinonoid** form (deeply coloured). Change of pH converts one into the other. Phenolphthalein is benzenoid (colourless) in acid and quinonoid (pink) in alkali; methyl orange is benzenoid (yellow) in alkali and quinonoid (red) in acid.

Modern view: both are combined — the ionisation (Ostwald) triggers a change in structure (quinonoid), which is the cause of colour.

**Common indicators**

| Indicator | pH range | Colour (acid → alkali) | Suits |
| --- | --- | --- | --- |
| Methyl orange | 3.1–4.4 | Red → yellow | Strong acid vs weak base |
| Methyl red | 4.2–6.3 | Red → yellow | Strong acid vs weak base |
| Bromothymol blue | 6.0–7.6 | Yellow → blue | Strong acid vs strong base |
| Phenol red | 6.8–8.4 | Yellow → red | Strong–strong; near neutral |
| Phenolphthalein | 8.3–10.0 | Colourless → pink | Weak acid vs strong base |
| Thymolphthalein | 9.3–10.5 | Colourless → blue | Weak acids |

**Mixed indicators** (two indicators, or an indicator with an inert dye) give a sharper colour change over a narrower range, for example methyl orange with xylene cyanol, or bromocresol green with methyl red.

**Choice of indicator**: its colour-change range must fall within the steep part (pH jump) of the titration curve at the equivalence point.

### 3.2 Classification of acid–base titrations

| Basis | Kinds | Examples |
| --- | --- | --- |
| What is titrated | **Acidimetry**: a base titrated with a standard acid | Sodium bicarbonate with HCl |
| | **Alkalimetry**: an acid titrated with a standard base | Boric acid with NaOH |
| Strength of acid and base | Strong acid–strong base; strong acid–weak base; weak acid–strong base; weak acid–weak base; very weak acids/bases (need special methods) | HCl–NaOH; HCl–NH3; CH3COOH–NaOH |
| Technique | Direct, back (residual), replacement/displacement, indirect | Back titration of ammonia; formol titration of NH4Cl |
| Solvent | Aqueous, non-aqueous | Part B |

### 3.3 Preparation and standardisation of hydrochloric acid and sodium hydroxide

**0.1 M HCl**

- Preparation: dilute about 8.5 ml of concentrated hydrochloric acid (about 11.5 M) with water to 1000 ml.
- Standardisation: weigh accurately about 0.13 g of **anhydrous sodium carbonate** (primary standard, previously heated and cooled in a desiccator), dissolve in 50 ml water, add methyl orange, titrate with the acid to a faint orange-red (boil to expel CO2 near the end if needed).
- Na2CO3 + 2HCl → 2NaCl + H2O + CO2 → **1 ml of 0.1 M HCl ≡ 0.005299 g Na2CO3** (105.99 × 0.1 ÷ 2 ÷ 1000).
- Example: 0.1325 g Na2CO3 required 24.80 ml. Expected volume at exactly 0.1 M = 0.1325/0.005299 = 25.00 ml. f = 25.00/24.80 = **1.008**; molarity = **0.1008 M**.

**0.1 M NaOH**

- Preparation: dissolve about 4.2 g NaOH in carbon dioxide-free water to 1000 ml. It must be carbonate-free; a concentrated (about 50%) stock solution lets sodium carbonate settle out, and the clear liquid is diluted. Store in polythene bottles with a soda-lime guard tube.
- Standardisation: weigh about 0.4 g **potassium hydrogen phthalate (KHP)**, dissolve in 50 ml CO2-free water, phenolphthalein, titrate to a permanent pink.
- KHC8H4O4 + NaOH → KNaC8H4O4 + H2O → **1 ml of 0.1 M NaOH ≡ 0.02042 g KHP**.
- Example: 0.4050 g KHP needed 19.75 ml. Moles = 0.4050/204.22 = 0.001983; M = 0.001983/0.01975 = **0.1004 M**.

Why NaOH is not a primary standard: it absorbs moisture (hygroscopic) and CO2 (forms Na2CO3) from air. Why HCl is not: concentrated HCl is volatile and its exact strength is unknown.

### 3.4 Neutralisation curves and theory of titrations

A **neutralisation curve** plots pH (y-axis) against volume of titrant (x-axis). The steep rise near the equivalence point is the **pH jump**; a good indicator changes colour inside it.

```text
 pH                                    pH
 14│                 ____ (excess      14│
   │               /       NaOH)         │                  ____
 11│              |                   11 │                /
   │              |  ← jump ~3.5–10.5     │               |  jump ~7–10.5
  7│- - - - - - - ● equivalence pH 7    8.7│- - - - - - - ●  (equivalence > 7)
   │              |                       │        _____/
  3│              |                     4.76│ ___/  ← buffer region (half-neutralised pH = pKa)
  1│_____________/                     2.9│/
   └──────────────┴──── ml NaOH           └──────────────┴──── ml NaOH
   (a) strong acid–strong base            (b) weak acid–strong base
```

**(a) Strong acid–strong base (0.1 M HCl with 0.1 M NaOH)**: starts at pH 1, rises slowly, then jumps from about pH 3.5 to 10.5 at the equivalence point, which is at **pH 7** (NaCl does not hydrolyse). Methyl orange, methyl red, bromothymol blue and phenolphthalein all work.

**(b) Weak acid–strong base (0.1 M acetic acid with 0.1 M NaOH)**: starts higher (pH 2.88), a buffer region forms (at half-neutralisation pH = pKa = 4.76), the jump is smaller (about pH 7–10.5) and the equivalence pH is **above 7** (about 8.7, because the acetate formed hydrolyses: CH3COO⁻ + H2O ⇌ CH3COOH + OH⁻). **Phenolphthalein** is right; methyl orange would change far too early.

**(c) Strong acid–weak base (0.1 M HCl with 0.1 M ammonia)**: equivalence pH **below 7** (about 5.3; NH4⁺ is acidic); jump about pH 3–7. **Methyl orange or methyl red**; phenolphthalein is unsuitable.

**(d) Weak acid–weak base**: no sharp jump; no simple indicator gives a good end point; avoided in practice (or done by conductometry).

**(e) Very weak acids and bases** (Ka or Kb below about 10⁻⁸, for example boric acid, phenols, alkaloids, NH4⁺ ion): the curve hardly rises at the equivalence point, so they cannot be titrated directly in water. Solutions:

- Boric acid (pKa about 9.2): add **glycerin or mannitol**, which forms a stronger complex acid; then titrate with NaOH and phenolphthalein. 1 ml of 0.1 M NaOH ≡ 0.006183 g H3BO3.
- Ammonium chloride: **formol method** — neutralised formaldehyde converts NH4⁺ into hexamine and releases an equal amount of HCl, which is titrated with NaOH: 4NH4Cl + 6HCHO → (CH2)6N4 + 4HCl + 6H2O.
- Very weak bases and acids generally: **non-aqueous titration** (Part B).

**Polybasic acids and mixtures**: phosphoric acid gives two end points (methyl orange for the first H⁺, phenolphthalein for the second); a mixture of NaOH and Na2CO3 is analysed with phenolphthalein then methyl orange (double-indicator method).

### 3.5 Assay of ammonium hydroxide (strong ammonia solution)

Ammonia is volatile, so it is assayed by **back titration** in a closed flask, so that none escapes.

1. Put a known excess of standard **1 M HCl** (for example 50.0 ml) in a stoppered flask and weigh it.
2. Add the sample (about 2 ml of strong ammonia solution) from a pipette below the surface of the acid; stopper and reweigh to get the exact weight of sample.
3. Titrate the unused acid with **1 M NaOH** using **methyl red** (the solution contains NH4Cl, so the equivalence pH is slightly acid).

NH3 + HCl → NH4Cl (1 : 1). **1 ml of 1 M HCl ≡ 0.01703 g NH3** (17.03 × 1 ÷ 1000; derived from the equation).

Example: 2.000 g sample; 50.00 ml 1 M HCl; back titre 20.10 ml 1 M NaOH. Acid used = 29.90 ml; NH3 = 29.90 × 0.01703 = 0.5092 g; **25.5% w/w NH3**.

## Part B: Non-aqueous titrations

### 3.6 Why non-aqueous?

Water is both a weak acid and a weak base, so it **competes** with very weak acids or bases and flattens the end point. Many drugs are also insoluble in water. Titrating in a suitable non-aqueous solvent increases their apparent acidic or basic strength and gives sharp end points. Used for alkaloids, amines, salts of organic acids (sodium benzoate), sulphonamides, barbiturates and phenols.

### 3.7 Types of solvents

| Type | Behaviour | Examples | Used for |
| --- | --- | --- | --- |
| **Aprotic (inert)** | Neither give nor take protons; dilute the sample | Benzene, chloroform, toluene, carbon tetrachloride, dioxane | Diluents |
| **Protophilic (basic)** | Accept protons; strengthen weak acids | Pyridine, dimethylformamide (DMF), ethylenediamine, liquid ammonia, n-butylamine | Titration of weak **acids** |
| **Protogenic (acidic)** | Give protons; strengthen weak bases | Glacial acetic acid, formic acid, sulphuric acid | Titration of weak **bases** |
| **Amphiprotic** | Both give and accept | Water, alcohols, glacial acetic acid | General |

**Levelling and differentiating effect**: water **levels** strong acids (HClO4, HCl, HNO3 all become H3O⁺ and look equally strong). In glacial acetic acid they are **differentiated**: perchloric acid stays by far the strongest, so it is the titrant of choice for bases.

### 3.8 Acidimetry in non-aqueous medium (titration of weak bases)

**Titrant: 0.1 M perchloric acid in glacial acetic acid.**

- Preparation: mix about 8.5 ml of perchloric acid (about 72%) with about 900 ml glacial acetic acid, add about 30 ml **acetic anhydride**, make to 1000 ml with glacial acetic acid and keep for 24 hours. Acetic anhydride removes water [(CH3CO)2O + H2O → 2CH3COOH], because water would weaken the titrant and spoil the end point. Too much anhydride is avoided because it can acetylate primary and secondary amines.
- Standardisation: weigh about 0.35 g **KHP**, dissolve in glacial acetic acid, add **crystal violet**, titrate to blue-green. In this solvent KHP behaves as a base. **1 ml of 0.1 M HClO4 ≡ 0.02042 g KHP.** Example: 0.3500 g needed 17.05 ml; expected 17.14 ml; f = **1.005**.

**How it works**

```text
 HClO4 + CH3COOH ⇌ CH3COOH2⁺ + ClO4⁻      (onium ion, a very strong acid)
 CH3COOH2⁺ + B  ⇌ BH⁺ + CH3COOH           (base titrated)
```

**Indicators**: crystal violet (violet → blue-green), oracet blue B, 1-naphtholbenzein, quinaldine red; or a potentiometric end point.

**Halide salts of bases** (for example amine hydrochlorides) are first treated with **mercuric acetate**, which takes up the halide as un-ionised HgCl2 and releases acetate, which is then titrated.

**Temperature correction**: glacial acetic acid expands appreciably with heat, so the strength of the titrant is corrected if the temperature at titration differs from that at standardisation.

### 3.9 Estimation of sodium benzoate

Sodium benzoate is the salt of a weak acid; in glacial acetic acid the benzoate ion acts as a base.

1. Weigh about 0.25 g, dissolve in about 20 ml anhydrous glacial acetic acid (warm if needed), cool.
2. Add 1-naphtholbenzein or crystal violet; titrate with 0.1 M perchloric acid.
3. Run a **blank** and subtract.

C6H5COONa + HClO4 → C6H5COOH + NaClO4 → **1 ml of 0.1 M HClO4 ≡ 0.01441 g C7H5NaO2** (144.10 × 0.1 ÷ 1000).

Example: 0.2500 g; titre 17.30 ml; blank 0.10 ml; f 1.005. % = (17.20 × 1.005 × 0.01441 × 100)/0.2500 = **99.6%**.

### 3.10 Alkalimetry in non-aqueous medium (titration of weak acids)

**Titrants**: 0.1 M **sodium methoxide** or **lithium methoxide** in toluene–methanol, or **tetrabutylammonium hydroxide**. Protected from atmospheric CO2 and moisture.

- Sodium methoxide is prepared by dissolving clean sodium metal in dry methanol (cooled) and diluting with toluene.
- Standardisation: weigh about 0.25 g **benzoic acid**, dissolve in DMF, add **thymol blue**, titrate to blue; blank. **1 ml of 0.1 M sodium methoxide ≡ 0.01221 g benzoic acid.**
- Solvents: DMF, pyridine, ethylenediamine, butylamine (protophilic, strengthen weak acids).
- Indicators: thymol blue, azo violet, o-nitroaniline.
- Applications: phenols, barbiturates, sulphonamides, imides, carboxylic acids poorly soluble in water.

Advantages of non-aqueous titration: very weak acids and bases titrated; water-insoluble drugs handled; sharp end points; mixtures can sometimes be resolved. Disadvantages: solvents costly, often toxic and inflammable; moisture and CO2 must be excluded; temperature correction needed.

## Part C: Precipitation titrations and gravimetry

### 3.11 Precipitation titrations (argentometry)

The titrant forms a sparingly soluble precipitate with the analyte. Most use **silver nitrate** (argentometric titrations) for chloride, bromide, iodide and thiocyanate. A suitable reaction is fast, quantitative, gives a precipitate of very low solubility (AgCl Ksp about 1.8 × 10⁻¹⁰) and has a clear end point.

**0.1 M silver nitrate**: dissolve about 17 g AgNO3 in water to 1000 ml; store in amber bottles (light-sensitive). Standardise against dried **sodium chloride** by Mohr's method: 1 ml of 0.1 M AgNO3 ≡ 0.005844 g NaCl.

**0.1 M ammonium thiocyanate** (for Volhard): about 7.6 g NH4SCN per litre, standardised against standard AgNO3 with ferric ammonium sulphate indicator.

### 3.12 Mohr's method (direct titration, chromate indicator)

- Chloride (or bromide) is titrated directly with AgNO3 using **potassium chromate** as indicator.
- Ag⁺ + Cl⁻ → AgCl (white). When all chloride is precipitated, the first excess Ag⁺ forms red-brown **silver chromate**: 2Ag⁺ + CrO4²⁻ → Ag2CrO4.
- Works because AgCl is less soluble than Ag2CrO4, so it precipitates first.
- **pH must be about 6.5–9 (neutral or weakly alkaline)**: in acid, chromate becomes dichromate and the end point is lost; in alkali, silver precipitates as Ag2O.
- Not suitable for iodide or thiocyanate (they adsorb chromate). An indicator blank is subtracted.

### 3.13 Volhard's method (back titration in acid)

- A known **excess** of standard AgNO3 is added to the halide in **nitric acid** solution; the unreacted Ag⁺ is titrated with standard **ammonium (or potassium) thiocyanate** using **ferric ammonium sulphate** as indicator.
- Ag⁺ (excess) + SCN⁻ → AgSCN (white). The first excess thiocyanate gives a **red** ferric thiocyanate complex: Fe³⁺ + SCN⁻ → [Fe(SCN)]²⁺.
- Advantage: works in acid solution, so carbonate, phosphate, oxalate and arsenate do not interfere.

### 3.14 Modified Volhard's method (for chloride)

**Problem**: AgCl is **more soluble** than AgSCN. Near the end point, excess thiocyanate reacts with the AgCl precipitate (AgCl + SCN⁻ → AgSCN + Cl⁻), the red colour fades, and too much thiocyanate is used, giving a **low** result for chloride.

**Modification** (either):

1. **Filter off** the AgCl (after boiling to coagulate it) and titrate the filtrate, or
2. Add a few ml of **nitrobenzene** (or dibutyl phthalate) and shake: it coats the AgCl particles and stops them reacting with thiocyanate.

Bromide and iodide do not need this, because AgBr and AgI are less soluble than AgSCN.

**Assay of sodium chloride (modified Volhard)**: dissolve about 0.1 g in water, add dilute HNO3, a measured excess of 0.1 M AgNO3 (say 50.0 ml), shake, add nitrobenzene (or filter), add ferric ammonium sulphate, titrate the excess Ag⁺ with 0.1 M NH4SCN to a permanent reddish colour.

Example: 0.1000 g NaCl; 50.00 ml 0.1 M AgNO3; back titre 32.95 ml 0.1 M NH4SCN. Ag⁺ used = 17.05 ml; % = 17.05 × 0.005844 × 100/0.1000 = **99.6%**.

### 3.15 Fajans' method (adsorption indicators)

- Direct titration with AgNO3 using an **adsorption indicator** (an organic dye) such as **fluorescein** or **dichlorofluorescein** (chloride) or **eosin** (bromide, iodide).
- Before the equivalence point, the AgCl particles have excess Cl⁻ adsorbed on their surface (negative); the dye anion stays in solution (yellow-green).
- After the equivalence point, excess Ag⁺ is adsorbed (positive surface), which attracts the dye anion; the adsorbed dye turns **pink/red** on the precipitate.
- Conditions: keep the precipitate colloidal (dextrin added), avoid strong light, suitable pH for the dye.

| Method | Titration | Indicator | End point | Medium |
| --- | --- | --- | --- | --- |
| Mohr | Direct with AgNO3 | K2CrO4 | Red-brown Ag2CrO4 | Neutral (pH 6.5–9) |
| Volhard | Back titration, excess AgNO3 with NH4SCN | Ferric ammonium sulphate | Red Fe–SCN complex | Nitric acid |
| Modified Volhard | As Volhard + filter or nitrobenzene | Ferric ammonium sulphate | Red | Nitric acid (for chloride) |
| Fajans | Direct with AgNO3 | Fluorescein, eosin | Colour on the precipitate surface | Near neutral, colloid kept |

### 3.16 Gravimetric analysis

**Gravimetry** finds the amount of a constituent by converting it into a pure, stable compound of known composition and **weighing** it.

**Steps**

```text
 Sample weighed and dissolved
        ↓
 Precipitation (reagent added slowly, hot, dilute, with stirring)
        ↓
 Digestion (precipitate kept warm in its mother liquor — crystals grow, become purer)
        ↓
 Filtration (ashless filter paper or sintered/Gooch crucible)
        ↓
 Washing (with dilute electrolyte or water to remove adsorbed impurities)
        ↓
 Drying or ignition to constant weight
        ↓
 Weighing → calculation with the gravimetric factor
```

**Requirements of a good precipitate**: very low solubility; easily filtered (large crystals); pure; known, constant composition after drying or ignition; not hygroscopic.

**Impurities in precipitates**

- **Co-precipitation**: soluble impurities carried down during precipitation (surface adsorption, occlusion inside crystals, mixed crystals).
- **Post-precipitation**: a second substance precipitates on the first after it has formed, on standing.
- Reduced by precipitating from dilute hot solution, adding reagent slowly, digestion, washing and sometimes re-precipitation.

**Gravimetric factor (GF)** = (molar mass of what is sought × a) ÷ (molar mass of what is weighed × b), where a and b balance the atoms.

### 3.17 Estimation of barium as barium sulphate

**Principle**: barium ions are precipitated with dilute sulphuric acid in hot, dilute, slightly acid (HCl) solution as **barium sulphate**, which is very insoluble, filtered, washed, ignited and weighed.

Ba²⁺ + SO4²⁻ → BaSO4

**Procedure (outline)**: dissolve about 0.5 g of barium chloride (BaCl2·2H2O), accurately weighed, in about 100 ml water with a little dilute HCl; heat nearly to boiling; add hot dilute H2SO4 slowly with stirring; digest on a water bath for about an hour; filter through ashless paper; wash with hot water until the washings are free from chloride (test with AgNO3); dry, ignite in a weighed crucible to constant weight.

Why HCl? It makes the precipitate coarser (easier to filter) and prevents precipitation of barium carbonate, phosphate or chromate.

**Gravimetric factors** (BaSO4 = 233.38): Ba = 137.33/233.38 = **0.5884**; SO4 = 96.06/233.38 = **0.4116**; BaCl2·2H2O = 244.26/233.38 = **1.0466**.

Example: 0.5000 g BaCl2·2H2O gave 0.4770 g BaSO4. Ba = 0.4770 × 0.5884 = 0.2807 g (56.1%); purity as BaCl2·2H2O = 0.4770 × 1.0466 × 100/0.5000 = **99.8%**.

The same method estimates **sulphate** (precipitated with BaCl2) using the factor 0.4116.

## Part D: Complexometric titrations

### 3.18 Principle and classification

A metal ion reacts with a **ligand** (an electron-pair donor) to form a stable, soluble **complex**. When the ligand binds through several atoms it forms a ring — a **chelate**. **EDTA** (ethylenediaminetetra-acetic acid) is a **hexadentate** ligand (2 N + 4 O) that forms 1 : 1 chelates with almost all metal ions, whatever their charge:

M²⁺ + H2Y²⁻ → MY²⁻ + 2H⁺

H⁺ is released, so a **buffer** keeps the pH constant. Stability of the complex depends on pH: highly charged ions (Fe³⁺, Bi³⁺) can be titrated in acid; Ca²⁺ and Mg²⁺ need pH 10 or more.

**Classification**

| Type | How | Example |
| --- | --- | --- |
| **Direct** | Metal titrated straight with EDTA at the right pH | Mg, Zn, Ca |
| **Back** | Excess EDTA added; excess titrated with Zn²⁺ or Mg²⁺ | Aluminium (reacts slowly), metals that precipitate at the titration pH, insoluble samples |
| **Replacement (substitution)** | Mg–EDTA complex added; the metal displaces Mg, which is titrated | Calcium (when its own end point is poor) |
| **Indirect** | Anion precipitated with excess metal; excess metal titrated | Sulphate, phosphate |
| **Alkalimetric** | H⁺ released on complexation titrated with NaOH | — |

### 3.19 Metal ion indicators

A metal ion indicator is a dye that forms a **coloured complex with the metal**, less stable than the metal–EDTA complex. At the start the solution shows the metal–indicator colour; at the end point EDTA takes the metal away and the **free indicator** colour appears.

```text
 Start:  M–In (wine red)  +  EDTA  →  M–EDTA  +  free In (blue)  at end point
```

| Indicator | pH | Colour change | Metals |
| --- | --- | --- | --- |
| **Eriochrome Black T (mordant black 11)** | 10 (ammonia buffer) | Wine red → blue | Mg, Zn, Ca (with Mg), Cd, Pb |
| **Murexide (ammonium purpurate)** | 11–12 | Pink/red → violet | Ca, Cu, Ni |
| **Calcon / hydroxynaphthol blue** | 12–13 | Red → blue | Ca in presence of Mg |
| **Xylenol orange** | Acid (about 1–6) | Red → yellow | Bi, Pb, Zn |
| **Catechol violet** | Various | Blue → yellow | Bi, Th |

Requirements: forms a less stable complex than M–EDTA, sharp colour change, specific to the metal, stable.

### 3.20 Masking and demasking reagents

A **masking agent** stops an ion from reacting with EDTA or the indicator without removing it (usually by forming a more stable complex or a precipitate). **Demasking** releases the masked ion so that it can be titrated.

| Masking agent | Masks | Use |
| --- | --- | --- |
| Potassium cyanide | Zn, Cu, Ni, Co, Cd, Hg, Ag | Titrate Mg or Ca in their presence (handle with great care) |
| Triethanolamine | Al, Fe, Mn | Ca/Mg in presence of Al, Fe |
| Ammonium fluoride | Al, Fe | |
| Ascorbic acid | Reduces Fe³⁺ to Fe²⁺ | |
| Dimercaprol (BAL) | Hg, Cd, Pb, Zn | |
| Thiourea | Cu | |

**Demasking**: formaldehyde (with a little acetic acid) breaks the zinc–cyanide complex and frees Zn²⁺, so Zn and Mg can be found in one sample — Mg titrated first with Zn masked by cyanide, then Zn titrated after demasking.

### 3.21 Preparation and standardisation of disodium EDTA (0.05 M)

- Disodium edetate (Na2H2Y·2H2O, 372.24) is used because the free acid is poorly soluble. Dissolve about **18.6 g** in water to 1000 ml; store in polythene (glass releases metal ions).
- Standardise against **granulated zinc** (primary standard): dissolve an accurately weighed amount in a little dilute HCl (with a drop of bromine water, excess boiled off), neutralise, dilute to volume; titrate an aliquot at pH 10 (ammonia buffer) with Eriochrome Black T to blue, or with xylenol orange in hexamine buffer. Zn²⁺ + H2Y²⁻ → ZnY²⁻ + 2H⁺ → 1 ml of 0.05 M EDTA ≡ 0.003269 g Zn (derived). Calcium carbonate is also used: 1 ml ≡ 0.005004 g CaCO3.
- Example: 0.8200 g zinc dissolved and diluted to 250 ml; 25.00 ml (0.08200 g Zn) needed 25.30 ml. M = (0.08200/65.38)/0.02530 = **0.04957 M** (f = 0.991).

### 3.22 Estimation of magnesium sulphate

Direct titration at pH 10.

1. Weigh about 0.3 g (dried), dissolve in 50 ml water.
2. Add 10 ml of strong ammonia–ammonium chloride buffer (pH 10) and Eriochrome Black T (mordant black 11) mixture.
3. Titrate with 0.05 M disodium EDTA until wine red changes to **blue**.

Mg²⁺ + H2Y²⁻ → MgY²⁻ + 2H⁺ → **1 ml of 0.05 M EDTA ≡ 0.006018 g MgSO4** (120.36 × 0.05 ÷ 1000; MgSO4 calculated on the dried substance).

Example: 0.3000 g dried; 49.60 ml; f 1.004 → % = 49.60 × 1.004 × 0.006018 × 100/0.3000 = **99.9%**.

### 3.23 Estimation of calcium gluconate

Calcium forms a **weak complex with Eriochrome Black T**, so the direct end point is poor. A small known amount of **magnesium** is added (replacement principle): EDTA first takes calcium (its EDTA complex is more stable), then magnesium; the Mg–EBT complex gives a sharp wine red → blue change.

1. Dissolve about 0.5 g in about 50 ml warm water; cool.
2. Add **5.0 ml of 0.05 M magnesium sulphate** and 10 ml strong ammonia buffer (pH 10).
3. Add Eriochrome Black T; titrate with 0.05 M disodium EDTA to blue.
4. **Subtract the volume of EDTA equivalent to the MgSO4 added** (5.0 ml if both are exactly 0.05 M).

**1 ml of 0.05 M EDTA ≡ 0.02242 g C12H22CaO14·H2O** (448.39 × 0.05 ÷ 1000).

Example: 0.5000 g; titre 27.20 ml; minus 5.00 ml → 22.20 ml; % = 22.20 × 0.02242 × 100/0.5000 = **99.5%**.

## Part E: Redox titrations

### 3.24 Concepts of oxidation and reduction

| | Oxidation | Reduction |
| --- | --- | --- |
| Classical | Addition of oxygen / removal of hydrogen | Removal of oxygen / addition of hydrogen |
| Electronic | **Loss of electrons** | **Gain of electrons** |
| Oxidation number | Increases | Decreases |

An **oxidising agent** gains electrons (is reduced); a **reducing agent** loses electrons (is oxidised). The two always occur together (redox).

**Electrode potential.** The tendency of a couple to gain electrons is its standard reduction potential E°. The Nernst equation relates potential to concentrations:

E = E° + (0.0591/n) log([oxidised]/[reduced]) at 25 °C.

A titration works well when the E° values of the titrant and analyte couples differ by about 0.2 V or more, which gives a large jump in potential at the equivalence point.

**Redox indicators** change colour at a particular potential: diphenylamine and its sulphonate (colourless → violet), ferroin (red → pale blue), N-phenylanthranilic acid. Some titrants are **self-indicating** (KMnO4); iodine uses **starch** (specific indicator).

**Equivalent weight** in redox = molar mass ÷ electrons transferred per formula unit.

### 3.25 Permanganometry

**Titrant: 0.02 M KMnO4.** In acid: MnO4⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H2O (n = 5). Purple → colourless; the first permanent **pink** marks the end point (self-indicator).

- Not a primary standard: contains MnO2 and decomposes in light and with organic matter.
- Preparation: dissolve about **3.2 g** in 1000 ml water, heat on a water bath for an hour (or boil), stand for about two days, filter through glass wool (not paper), store in an amber bottle.
- Standardisation: against **oxalic acid** or **sodium oxalate** in dilute H2SO4 at 60–70 °C (the reaction is slow cold; Mn²⁺ formed catalyses it — **autocatalysis**).
  2MnO4⁻ + 5C2O4²⁻ + 16H⁺ → 2Mn²⁺ + 10CO2 + 8H2O → 1 ml of 0.02 M KMnO4 ≡ 0.006303 g (COOH)2·2H2O.
  Example: 0.1600 g oxalic acid needed 25.20 ml; expected 25.38 ml; f = **1.007**.
- Medium: **sulphuric acid** only; HCl is oxidised to chlorine and nitric acid is itself an oxidant.
- Uses: hydrogen peroxide, ferrous salts, oxalates, nitrites, calcium (as oxalate).

**Assay of hydrogen peroxide**: dilute 10 ml of the solution to 100 ml; to 10 ml of this add 20 ml dilute H2SO4 and titrate with 0.02 M KMnO4 to permanent pink.
2MnO4⁻ + 5H2O2 + 6H⁺ → 2Mn²⁺ + 5O2 + 8H2O → **1 ml of 0.02 M KMnO4 ≡ 0.001701 g H2O2** (34.01 × 0.02 × 5/2 ÷ 1000). Detailed in Unit 4.

### 3.26 Cerimetry

**Titrant: 0.1 M ceric ammonium sulphate** in dilute H2SO4. Ce⁴⁺ + e⁻ → Ce³⁺ (n = 1), E° about 1.44 V in sulphuric acid.

- Preparation: dissolve about 65 g ceric ammonium sulphate with gentle heat in a mixture of 30 ml H2SO4 and water; cool, filter if turbid, dilute to 1000 ml.
- Standardisation: against **arsenic trioxide** (dissolved in NaOH, acidified, a drop of osmic acid as catalyst), ferroin indicator; 1 ml of 0.1 M ≡ 0.004946 g As2O3. Or against standard ferrous ammonium sulphate.
- Indicator: **ferroin** (orange-red → pale blue), N-phenylanthranilic acid.
- **Advantages over KMnO4**: very stable (even on boiling), single one-electron change (no intermediate states), usable in HCl, Ce³⁺ colourless, does not oxidise chloride readily.
- Uses: ferrous salts (ferrous sulphate, ferrous gluconate, ferrous fumarate), paracetamol (after hydrolysis), tocopherol, nitrites.

**Assay of ferrous sulphate** (detailed in Unit 5): Fe²⁺ + Ce⁴⁺ → Fe³⁺ + Ce³⁺ → **1 ml of 0.1 M ceric ammonium sulphate ≡ 0.02780 g FeSO4·7H2O**.

### 3.27 Iodimetry and iodometry

Iodine couple: I2 + 2e⁻ ⇌ 2I⁻ (E° about 0.54 V). Iodine is a mild oxidant; iodide is a mild reductant.

| | **Iodimetry** (direct) | **Iodometry** (indirect) |
| --- | --- | --- |
| Analyte | A **reducing agent** | An **oxidising agent** |
| Method | Titrated directly with standard iodine | Treated with excess KI; the **liberated iodine** is titrated with standard sodium thiosulphate |
| Titrant | 0.05 M iodine (in KI) | 0.1 M sodium thiosulphate |
| End point (starch) | First permanent **blue** | **Blue disappears** |
| Examples | Ascorbic acid, sodium thiosulphate, arsenic(III), sulphites | Copper sulphate, potassium dichromate, chlorinated lime, KMnO4, H2O2 |

**0.05 M iodine**: dissolve about 12.7 g iodine and about 18 g KI in a little water (iodine dissolves as tri-iodide, I3⁻), dilute to 1000 ml; store in amber, glass-stoppered bottles. Standardise against standard thiosulphate (or arsenic trioxide).

**0.1 M sodium thiosulphate**: dissolve about 25 g Na2S2O3·5H2O and 0.2 g sodium carbonate in freshly boiled and cooled water to 1000 ml (boiling kills thiosulphate-decomposing bacteria; carbonate keeps it slightly alkaline). Standardise with **potassium dichromate** or **potassium bromate** or **potassium iodate** + excess KI in acid, titrating the liberated iodine:

K2Cr2O7 + 6KI + 14HCl → 2CrCl3 + 8KCl + 3I2 + 7H2O; I2 + 2Na2S2O3 → 2NaI + Na2S4O6.
1 Cr2O7²⁻ ≡ 3 I2 ≡ 6 S2O3²⁻ → **1 ml of 0.1 M thiosulphate ≡ 0.004903 g K2Cr2O7**. Example: 0.1225 g needed 24.80 ml; expected 24.98 ml; f = **1.007**.

**Starch indicator**: forms an intense blue complex with iodine. In **iodometry** it is added **near the end point** (pale straw colour), because a large amount of iodine bound to starch is released slowly and the end point overshoots. Use freshly made starch solution.

**Sources of error and precautions**: loss of volatile iodine (excess KI, cool solution, stoppered iodine flasks); air oxidation of iodide in acid (worse in light; titrate promptly); pH — thiosulphate decomposes in strong acid and iodine forms hypoiodite above about pH 9.

**Assay of copper sulphate (iodometry)**: 2Cu²⁺ + 4I⁻ → 2CuI + I2; then I2 + 2S2O3²⁻ → 2I⁻ + S4O6²⁻. So Cu : thiosulphate = 1 : 1. Add acetic acid and KI, titrate with 0.1 M thiosulphate, starch near the end; **potassium thiocyanate** is added near the end to release iodine adsorbed on CuI. **1 ml of 0.1 M Na2S2O3 ≡ 0.02497 g CuSO4·5H2O.** Details in Unit 5.

### 3.28 Titrations with potassium iodate

**Potassium iodate** (KIO3, 214.00) is a primary standard and a strong oxidant.

1. **Andrews' titration (strong HCl).** In 3–6 M HCl, reductants are oxidised and iodine is converted to **iodine monochloride**: IO3⁻ + 2I⁻ + 6H⁺ + 3Cl⁻ → 3ICl + 3H2O (iodate +5 → +1, a 4-electron change). End point: shake with **chloroform**; the violet iodine colour in the chloroform layer first appears and then **disappears** when all I2 becomes ICl. Used for **potassium iodide**, hydrazine, arsenic(III), antimony(III). For KI: KIO3 + 2KI + 6HCl → 3ICl + 3KCl + 3H2O → **1 ml of 0.05 M KIO3 ≡ 0.01660 g KI** (Unit 5).
2. **In dilute acid with excess KI**, iodate liberates iodine: IO3⁻ + 5I⁻ + 6H⁺ → 3I2 + 3H2O (1 IO3⁻ ≡ 6 S2O3²⁻) — used to standardise thiosulphate (1 ml of 0.1 M thiosulphate ≡ 0.003567 g KIO3).

## 3.29 Summary of titrants and factors

| Titrant | Standardised against | Indicator | Example factor (1 ml ≡) |
| --- | --- | --- | --- |
| 0.1 M HCl | Anhydrous Na2CO3 | Methyl orange | 0.005299 g Na2CO3 |
| 0.1 M NaOH | KHP | Phenolphthalein | 0.02042 g KHP |
| 0.1 M HClO4 (acetic acid) | KHP | Crystal violet | 0.01441 g sodium benzoate |
| 0.1 M NaOMe | Benzoic acid | Thymol blue | 0.01221 g benzoic acid |
| 0.1 M AgNO3 | NaCl | K2CrO4 / Fe³⁺ (back) | 0.005844 g NaCl |
| 0.05 M disodium EDTA | Zinc / CaCO3 | Eriochrome Black T | 0.006018 g MgSO4; 0.02242 g Ca gluconate |
| 0.02 M KMnO4 | Oxalic acid / sodium oxalate | Self | 0.001701 g H2O2 |
| 0.1 M ceric ammonium sulphate | As2O3 | Ferroin | 0.02780 g FeSO4·7H2O |
| 0.1 M Na2S2O3 | K2Cr2O7 / KIO3 / KBrO3 | Starch (late) | 0.02497 g CuSO4·5H2O |
| 0.05 M iodine | Na2S2O3 / As2O3 | Starch | 0.02482 g Na2S2O3·5H2O |
| 0.05 M KIO3 | Primary standard | Chloroform layer | 0.01660 g KI |

## Remember

- Indicator range must fall inside the pH jump: phenolphthalein for weak acids, methyl orange/red for weak bases, any for strong–strong.
- Equivalence pH: strong–strong 7; weak acid–strong base > 7 (~8.7); strong acid–weak base < 7 (~5.3).
- HCl ← Na2CO3 (methyl orange); NaOH ← KHP (phenolphthalein); NaOH must be carbonate-free.
- Ammonia: back titration with excess 1 M HCl and 1 M NaOH, methyl red; 1 ml 1 M HCl ≡ 0.01703 g NH3.
- Non-aqueous: HClO4 in glacial acetic acid + acetic anhydride for weak bases (crystal violet); NaOMe in DMF for weak acids (thymol blue); levelling vs differentiating.
- Mohr: chromate, neutral; Volhard: back titration in HNO3, ferric alum; modified Volhard: filter or nitrobenzene because AgCl is more soluble than AgSCN; Fajans: adsorption indicators.
- Gravimetry: precipitate → digest → filter → wash → ignite → weigh; Ba = BaSO4 × 0.5884.
- EDTA 1 : 1, hexadentate, buffered; EBT wine red → blue at pH 10; Ca needs added Mg; KCN/triethanolamine mask, formaldehyde demasks.
- KMnO4 self-indicator, H2SO4 only; ceric stable, ferroin; iodimetry direct (blue appears), iodometry indirect (blue disappears, starch late); KIO3 Andrews ends as ICl.
