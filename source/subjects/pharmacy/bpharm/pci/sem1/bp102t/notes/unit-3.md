# Unit 3: Precipitation, complexometric and diazotisation titrations, and gravimetry

This unit covers four methods that do not depend on simple neutralisation. Precipitation titrations measure halides with silver nitrate; complexometric titrations measure metal ions with EDTA; gravimetry weighs a pure precipitate; and diazotisation measures primary aromatic amines such as sulphonamides. The syllabus asks for the principle of each, the indicators, ways to remove interference, and named assays (sodium chloride, magnesium sulphate, calcium gluconate, barium sulphate).

## 3.1 Precipitation titrations

A **precipitation titration** is one in which the titrant forms a sparingly soluble precipitate with the analyte. Titrations with silver nitrate are called **argentometric** titrations; they are used for chlorides, bromides, iodides, thiocyanates and cyanides.

**Requirements:** the precipitate must be very sparingly soluble (small solubility product, Ksp); it must form quickly and in a fixed composition; co-precipitation must be small; there must be a way to see the end point.

**Solubility product (Ksp):** for AgCl ⇌ Ag⁺ + Cl⁻, Ksp = [Ag⁺][Cl⁻] (about 1.8 × 10⁻¹⁰ at 25 °C). A precipitate forms when the ionic product exceeds Ksp.

**Standard solution:** 0.1 M silver nitrate (AgNO3, Mw 169.87; about 17 g per litre), stored in amber bottles, standardised against **sodium chloride** (dried primary standard, Mw 58.44) by Mohr's method. 1 ml of 0.1 M AgNO3 ≡ 0.005844 g NaCl.

### Mohr's method

- **Principle:** chloride is titrated directly with AgNO3 in neutral solution with **potassium chromate** as indicator. AgCl (white) precipitates first because it is less soluble (in molar terms) than silver chromate. When all chloride is used, the first excess Ag⁺ forms **red-brown silver chromate**, marking the end point.
  - Ag⁺ + Cl⁻ → AgCl (white)
  - 2Ag⁺ + CrO4²⁻ → Ag2CrO4 (red-brown)
- **pH:** must be about **6.5 to 9** (neutral or faintly alkaline). In acid, chromate becomes dichromate (HCrO4⁻/Cr2O7²⁻) and the end point is late; in strong alkali, silver hydroxide/oxide precipitates.
- **Use:** chlorides and bromides. Not suitable for iodide and thiocyanate (they adsorb chromate strongly and give unclear end points).
- **Limitations:** neutral solutions only; ions precipitated by Ag⁺ or chromate in neutral solution (phosphate, carbonate, arsenate, Ba²⁺, Pb²⁺) interfere; an indicator blank is needed because some excess Ag⁺ is required before the red colour is visible.

### Volhard's method

- **Principle:** a **back titration** in **nitric acid** solution. A measured excess of standard AgNO3 is added to precipitate the halide; the unreacted Ag⁺ is titrated with standard **ammonium (or potassium) thiocyanate** using **ferric ammonium sulphate (ferric alum)** as indicator. After all Ag⁺ is precipitated as AgSCN, the first excess SCN⁻ forms a **red** soluble complex with Fe³⁺.
  - Ag⁺ (excess) + SCN⁻ → AgSCN (white)
  - Fe³⁺ + SCN⁻ → [Fe(SCN)]²⁺ (red)
- **Why nitric acid:** prevents hydrolysis of Fe³⁺ and prevents precipitation of carbonate, phosphate, oxalate etc. with silver, so the method works in acidic solution (its main advantage over Mohr's).
- **Use:** chlorides, bromides, iodides, thiocyanates. (For iodide, add the ferric indicator only after excess AgNO3, since Fe³⁺ oxidises I⁻.)

### Modified Volhard's method (for chloride)

AgCl is more soluble than AgSCN. Near the end point, excess SCN⁻ reacts with the AgCl precipitate (AgCl + SCN⁻ → AgSCN + Cl⁻), consuming extra thiocyanate and giving low results and a fading end point. The modification prevents this by either:

1. **Filtering off** the AgCl precipitate (after boiling to coagulate it) before titrating the excess Ag⁺; or
2. Adding a few ml of **nitrobenzene** (or dibutyl phthalate) and shaking, which coats the AgCl particles and keeps them from reacting with thiocyanate.

Bromide and iodide do not need this, because AgBr and AgI are less soluble than AgSCN.

### Fajans' method (adsorption indicators)

- **Principle:** an **adsorption indicator** is a dye that changes colour when it is adsorbed on the surface of the precipitate.
- Before equivalence in a chloride titration, AgCl particles adsorb excess Cl⁻ (primary layer, negative); the indicator anion is repelled and stays in solution (yellow-green fluorescein). Just after equivalence, the particles adsorb excess Ag⁺ (positive); the indicator anion is now attracted to the surface and forms a coloured silver compound — **pink**.

```text
 Before end point            After end point
  (AgCl) Cl-  | Na+           (AgCl) Ag+ | Fl-   <- dye adsorbed
  surface -ve, dye stays      surface +ve, dye attracted,
  in solution: yellow-green   colour on precipitate: pink
```

| Adsorption indicator | Used for | pH |
| --- | --- | --- |
| Fluorescein | Chloride | 7–10 |
| Dichlorofluorescein | Chloride | 4 upwards |
| Eosin (tetrabromofluorescein) | Bromide, iodide, thiocyanate | 2 upwards |

- **Conditions:** the precipitate must stay colloidal (large surface) — dextrin is often added to prevent coagulation; avoid strong light (silver halides darken); solutions should not be too dilute.

### Estimation of sodium chloride

- Dissolve about 0.1 g of dried sodium chloride, accurately weighed, in 50 ml water.
- Titrate with 0.1 M AgNO3 using potassium chromate solution as indicator (Mohr), to the first permanent red-brown tinge. (Volhard's or Fajans' methods may also be used.)
- NaCl + AgNO3 → AgCl + NaNO3 (1 : 1). **1 ml of 0.1 M AgNO3 ≡ 0.005844 g NaCl.**
- **Worked example:** 0.1012 g used 17.20 ml of 0.1 M AgNO3 (f = 1.004). % NaCl = 17.20 × 1.004 × 0.005844 × 100/0.1012 = **99.7%**.

## 3.2 Complexometric titrations

A **complexometric titration** is one in which a metal ion reacts with a ligand to form a stable, soluble complex, and the end point is shown by a metal-ion indicator.

- **Ligand:** an ion or molecule that donates electron pairs to a metal ion.
- **Chelate:** a ring complex formed when one ligand binds through two or more donor atoms (multidentate ligand).
- **Stability constant (K):** M + L ⇌ ML, K = [ML]/([M][L]). A high log K means a stable complex.

### EDTA

**Ethylenediaminetetraacetic acid** (H4Y) is a hexadentate ligand: two nitrogen atoms and four carboxylate oxygens. It is used as **disodium edetate** (Na2H2Y·2H2O, Mw 372.24), which dissolves in water.

```text
   HOOC-CH2               CH2-COOH
            \             /
             N-CH2-CH2-N          6 donor atoms: 2 N + 4 O
            /             \       forms a 1:1 cage around the metal
   HOOC-CH2               CH2-COOH
```

- Reacts with metal ions in a **1 : 1 ratio** whatever the charge: M²⁺ + H2Y²⁻ → MY²⁻ + 2H⁺. So 0.05 M EDTA is used with molar calculations only.
- H⁺ is released, so titrations are done in **buffers** (e.g. ammonia–ammonium chloride, pH 10).
- Stability depends on pH: in acid, the protonated forms of EDTA bind poorly. Very stable complexes (Fe³⁺, Bi³⁺) can be titrated in acid; less stable ones (Ca²⁺, Mg²⁺) need pH 10 or above.
- 0.05 M disodium edetate is standardised against **zinc** (granulated zinc dissolved in HCl), or calcium carbonate, using a metal-ion indicator.

### Classification of complexometric titrations

| Type | Principle | Example |
| --- | --- | --- |
| **Direct titration** | Buffered metal solution titrated directly with EDTA | Mg²⁺, Zn²⁺, Ca²⁺ at pH 10 with Eriochrome Black T |
| **Back titration** | Known excess of EDTA added, excess titrated with standard Mg²⁺ or Zn²⁺ solution | Metals that react slowly, precipitate at the working pH, or have no good indicator: Al³⁺, Pb²⁺ in some salts, aluminium hydroxide gel |
| **Replacement (substitution) titration** | Metal displaces Mg²⁺ (or Zn²⁺) from its EDTA complex; liberated Mg²⁺ titrated | Ca²⁺ with Mg–EDTA, giving a sharper Eriochrome end point |
| **Indirect titration** | Anion precipitated with a metal; excess metal titrated | Sulphate (as BaSO4), phosphate |
| **Alkalimetric titration** | H⁺ released on complexation titrated with NaOH | Rarely used |

### Metal ion indicators (metallochromic indicators)

A **metal ion indicator** is a dye that forms a coloured complex with the metal, less stable than the metal–EDTA complex, and has a different colour when free.

```text
 start:     M + In  -> M-In          (colour of complex, e.g. wine red)
 titration: M + EDTA -> M-EDTA       (free metal used first)
 end:       M-In + EDTA -> M-EDTA + In (free indicator colour, e.g. blue)
```

**Requirements:** sharp colour difference between free and complexed forms; metal–indicator complex stable enough to stay until the end but less stable than metal–EDTA (about 10⁴ times less); selective; stable solution.

| Indicator | pH | Colour change (metal complex → free) | Used for |
| --- | --- | --- | --- |
| **Eriochrome Black T** (mordant black 11) | 10 (ammonia buffer) | Wine red → blue | Mg, Zn, Ca (with Mg), Cd, Pb |
| **Murexide** (ammonium purpurate) | 12 (Ca), 7–9 (Cu, Ni) | Pink/red → violet (Ca) | Calcium, copper, nickel |
| **Calcon / hydroxynaphthol blue** | 12–13 | Red/pink → blue | Calcium in presence of Mg (Mg(OH)2 precipitates) |
| **Xylenol orange** | 1–6 | Red → yellow | Bi, Pb, Zn, Th |
| **Catechol violet** | Variable | Blue → yellow (acid) | Bi, Th |
| **Calmagite** | 10 | Red → blue | Ca, Mg (more stable alternative to EBT) |

### Masking and demasking

- **Masking agent:** a reagent that reacts with an interfering ion and stops it from reacting with EDTA or the indicator, without removing it physically.
- **Demasking:** the release of a masked ion so that it can be titrated.

| Masking agent | Masks | Notes |
| --- | --- | --- |
| Potassium cyanide (alkaline only — highly toxic) | Zn, Cd, Cu, Ni, Co, Hg, Ag | Mg, Ca, Pb not masked |
| Triethanolamine | Al, Fe, Mn | Used in Ca/Mg titrations of hard water |
| Ammonium fluoride | Al, Fe, Ti | Forms fluoro complexes |
| Ascorbic acid | Fe³⁺ (reduced to Fe²⁺) | Fe²⁺ complex less stable |
| Dimercaprol (BAL) | Hg, Cd, Zn, Pb, As | — |
| Iodide | Hg²⁺ | As HgI4²⁻ |
| Thiourea | Cu | — |

**Demasking examples:** formaldehyde (or chloral hydrate) releases **Zn²⁺** from its cyanide complex, so in a Zn + Mg mixture: titrate Mg with Zn masked by cyanide, then add formaldehyde and titrate the freed Zn. Also, the metal can be demasked by changing pH.

**Other ways to improve selectivity:** pH control (Fe³⁺ at pH 1–2 before Ca/Mg), precipitation of one metal (Mg(OH)2 at pH 12 when titrating Ca), kinetic masking.

### Estimation of magnesium sulphate (MgSO4·7H2O; result as MgSO4, Mw 120.37)

- Dissolve about 0.3 g of the (dried) sample, accurately weighed, in 50 ml water; add 10 ml of ammonia–ammonium chloride buffer (pH 10); add Eriochrome Black T (mordant black 11) mixture.
- Titrate with **0.05 M disodium edetate** until wine red changes to **blue**.
- Mg²⁺ + H2Y²⁻ → MgY²⁻ + 2H⁺. **1 ml of 0.05 M EDTA ≡ 0.006018 g MgSO4** (120.37 × 0.05 / 1000).
- **Worked example:** 0.2500 g dried MgSO4 sample used 41.30 ml of 0.05 M EDTA (f = 1.002). % = 41.30 × 1.002 × 0.006018 × 100/0.2500 = **99.6%**.

### Estimation of calcium gluconate (C12H22CaO14·H2O, Mw 448.4)

- Calcium gives a weak, unclear end point with Eriochrome Black T because the Ca–indicator complex is not stable enough. A small known amount of Mg²⁺ is therefore added (replacement principle): Ca²⁺ displaces Mg from Mg–EDTA / Mg is titrated last, giving a sharp wine red → blue change.
- Dissolve about 0.5 g, accurately weighed, in 50 ml warm water; cool; add **5.0 ml of 0.05 M magnesium sulphate** and 10 ml of strong ammonia–ammonium chloride buffer; add mordant black 11 mixture.
- Titrate with 0.05 M disodium edetate to blue. **Subtract the volume of 0.05 M MgSO4 added (5.0 ml)** from the burette reading.
- **1 ml of 0.05 M EDTA ≡ 0.02242 g of C12H22CaO14·H2O.**
- **Worked example:** 0.5050 g needed 27.40 ml EDTA; net = 27.40 − 5.00 = 22.40 ml (f = 1.000). % = 22.40 × 0.02242 × 100/0.5050 = **99.4%**.
- Alternative: hydroxynaphthol blue at pH 12–13 for calcium directly.

## 3.3 Gravimetric analysis

**Gravimetry** is the quantitative determination of a constituent by isolating it, or a compound of definite composition containing it, in pure form and **weighing** it. It is slow but very accurate and needs no calibration against standards.

**Types:** precipitation (most common, e.g. sulphate as BaSO4); volatilisation (loss on drying, sulphated ash); electrogravimetry (metal deposited on an electrode).

### Steps in gravimetric analysis

1. **Preparation of solution** — weighing the sample, dissolving it, adjusting pH and volume, removing interfering ions.
2. **Precipitation** — slow addition of a dilute precipitant to a hot, dilute, stirred solution; slight excess of precipitant (common-ion effect lowers solubility). Aim: large, pure, easily filtered crystals (low relative supersaturation: von Weimarn ratio (Q − S)/S kept small).
3. **Digestion** — keeping the precipitate in contact with the hot mother liquor for some time. Small particles dissolve and re-deposit on larger ones (Ostwald ripening); crystals become larger, purer and easier to filter.
4. **Filtration** — through ashless filter paper (Whatman No. 42) or a sintered glass/Gooch crucible.
5. **Washing** — with a suitable dilute electrolyte (prevents peptisation of colloids) or hot water; test the washings for completeness (e.g. no chloride with AgNO3).
6. **Drying or ignition** — drying at 100–130 °C or igniting at high temperature to convert the precipitate to a stable **weighing form** of known composition.
7. **Weighing** — cool in a desiccator, weigh, repeat heating to **constant weight** (two weighings agreeing within about 0.0005 g / as directed).
8. **Calculation** — using the gravimetric factor.

**Gravimetric factor (GF)** = (formula weight of substance sought × a) ÷ (formula weight of substance weighed × b), where a and b balance the atoms of the key element.

Mass of analyte = mass of precipitate × GF; % analyte = (mass of precipitate × GF × 100) ÷ sample weight.

### Purity of the precipitate: co-precipitation and post-precipitation

**Co-precipitation** — soluble impurities carried down **with** the precipitate as it forms.

| Kind | How it happens | Remedy |
| --- | --- | --- |
| Surface adsorption | Ions held on the surface of particles (worst with colloids) | Digestion, washing with a volatile electrolyte |
| Occlusion | Impurity ions trapped inside the crystal as it grows quickly | Slow precipitation from dilute hot solution; digestion; re-precipitation |
| Inclusion (mixed-crystal formation) | Impurity of similar size and charge takes a place in the lattice (e.g. Pb²⁺ in BaSO4) | Remove the interfering ion beforehand; change the precipitant |
| Mechanical entrapment | Pockets of mother liquor trapped between crystals | Slow growth; digestion |

**Post-precipitation** — an impurity precipitates **on top of** the first precipitate **after** it has formed, when they stand together; it increases with time. Examples: magnesium oxalate deposits on calcium oxalate; zinc sulphide on copper sulphide or mercuric sulphide.

| Point | Co-precipitation | Post-precipitation |
| --- | --- | --- |
| When | During precipitation | After, on standing |
| Effect of digestion/standing | Decreases impurity | Increases impurity |
| Effect of time | Less with longer digestion | More with longer contact |
| Remedy | Digestion, slow precipitation, re-precipitation | Filter soon after precipitation |

**Other ways to obtain a pure precipitate:** precipitation from **homogeneous solution** (the precipitant is formed slowly within the solution itself, e.g. sulphate from sulphamic acid, hydroxide from hydrolysis of urea) giving dense, pure crystals; **re-precipitation** (dissolve and precipitate again).

### Estimation of barium (or sulphate) as barium sulphate

- **Principle:** Ba²⁺ + SO4²⁻ → BaSO4 (white, very sparingly soluble). BaSO4 (Mw 233.39) is stable on ignition, so it is weighed directly.
- **Procedure (barium in barium chloride):** dissolve the weighed sample in water, add a little dilute HCl (prevents precipitation of barium carbonate, phosphate, chromate and gives larger crystals), heat nearly to boiling; add hot dilute H2SO4 slowly with stirring in slight excess; digest on a water bath for about an hour; test for complete precipitation with a drop of H2SO4; filter through ashless paper, wash with hot water until free from chloride; dry, char the paper without flaming, ignite in a weighed crucible at red heat (about 800 °C), cool in a desiccator, weigh to constant weight.
- For **sulphate** in a sample, the same procedure is used with barium chloride as the precipitant.
- **Gravimetric factors:** Ba/BaSO4 = 137.33/233.39 = **0.5884**; SO4/BaSO4 = 96.06/233.39 = **0.4116**; BaCl2·2H2O/BaSO4 = 244.26/233.39 = **1.0466**.
- **Worked example:** 0.5000 g barium chloride dihydrate gave 0.4752 g BaSO4. % BaCl2·2H2O = 0.4752 × 1.0466 × 100/0.5000 = **99.5%**; Ba = 0.4752 × 0.5884 × 100/0.5000 = 55.9%.
- **Precautions:** ignite without letting the carbon of the paper reduce BaSO4 to BaS (char at low heat with good air); avoid nitrate and chlorate (co-precipitation); do not over-dilute.

## 3.4 Diazotisation titrations

**Principle:** a **primary aromatic amine** reacts with nitrous acid (formed from **sodium nitrite** and **hydrochloric acid**) at **0–5 °C** to give a diazonium salt. The amount of nitrite used measures the amine.

Ar–NH2 + NaNO2 + 2HCl → Ar–N≡N⁺ Cl⁻ + NaCl + 2H2O (1 : 1 with nitrite)

**Conditions:**

- Low temperature (0–5 °C, ice bath) — diazonium salts decompose and nitrous acid escapes at higher temperature.
- Excess HCl — needed to form HNO2 and to stabilise the diazonium salt; prevents coupling of diazonium with unreacted amine.
- Slow addition near the end, because diazotisation is slow; **potassium bromide** is often added as a catalyst.

**Titrant:** 0.1 M sodium nitrite (NaNO2, Mw 69.00; about 7.5 g per litre), standardised against **sulphanilic acid** (Mw 173.19) — dissolved in dilute ammonia, acidified with HCl, cooled. 1 ml of 0.1 M NaNO2 ≡ 0.01732 g sulphanilic acid.

**End-point detection:**

1. **External indicator — starch–iodide paper:** a drop of solution placed on the paper turns it **blue immediately** when excess nitrous acid is present (HNO2 oxidises iodide to iodine, which gives blue with starch). The end point is reached when the blue appears immediately and persists for about 1 minute after the last addition.
2. **Internal indicators:** tropaeolin OO, or a mixture of tropaeolin OO with methylene blue (colour change from red-violet to blue).
3. **Electrometric:** **dead-stop (biamperometric) end point** with two platinum electrodes — a sudden current flows (galvanometer deflection) when free nitrous acid appears; or potentiometric. The IP uses the electrometric method for many sulphonamides.

**Types:**

- **Direct method:** amine in acid titrated with nitrite (sulphonamides, procaine, benzocaine, dapsone).
- **Indirect method:** for amines whose diazonium salt is insoluble or that react slowly — excess nitrite added and the excess back-titrated.
- Nitro compounds can be assayed after reducing them to the amine (e.g. with zinc and HCl).

**Applications:** sulphonamides (sulphadiazine, sulphamethoxazole, sulphacetamide), local anaesthetics with an aromatic amino group (procaine, benzocaine), dapsone, primaquine, p-aminosalicylic acid, isoniazid-related amines; also estimation of nitrite itself.

**Worked example.** 0.2500 g of a sulphonamide (Mw 250.3, one Ar–NH2) used 9.85 ml of 0.1 M NaNO2 (f = 1.010). 1 ml 0.1 M ≡ 0.02503 g. % = 9.85 × 1.010 × 0.02503 × 100/0.2500 = **99.6%**.

**Remember**

- Mohr: K2CrO4, neutral pH 6.5–9, red Ag2CrO4. Volhard: back titration in HNO3, NH4SCN, ferric alum, red. Modified Volhard: filter AgCl or coat with nitrobenzene. Fajans: adsorption indicators (fluorescein, dichlorofluorescein, eosin).
- NaCl: 1 ml 0.1 M AgNO3 ≡ 0.005844 g.
- EDTA binds metals 1 : 1; buffer pH 10 with Eriochrome Black T (wine red → blue).
- MgSO4: 1 ml 0.05 M EDTA ≡ 0.006018 g. Calcium gluconate: add 5 ml 0.05 M MgSO4, subtract it; 1 ml ≡ 0.02242 g.
- Masking: KCN (Zn, Cu…), triethanolamine (Al, Fe), fluoride (Al); demasking Zn with formaldehyde.
- Gravimetry steps: precipitate → digest → filter → wash → dry/ignite → weigh to constant weight → gravimetric factor.
- Co-precipitation during precipitation (less on digestion); post-precipitation after (more on standing).
- BaSO4 factors: Ba 0.5884; SO4 0.4116.
- Diazotisation: Ar–NH2 + NaNO2/HCl at 0–5 °C; starch–iodide paper or dead-stop end point; standardise NaNO2 with sulphanilic acid.
