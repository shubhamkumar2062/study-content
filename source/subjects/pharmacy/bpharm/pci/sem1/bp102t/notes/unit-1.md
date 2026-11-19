# Unit 1: Fundamentals of pharmaceutical analysis, errors and limit tests

Every batch of a medicine must be tested before it reaches a patient: is it the right substance, is there the right amount of it, and is it free from harmful impurities? Pharmaceutical analysis answers these questions. This unit lays the groundwork for the whole subject: how concentration is expressed, how standard solutions are made and checked, how errors creep into results, and how the pharmacopoeia controls impurities with limit tests.

## 1.1 Pharmaceutical analysis: definition and scope

**Pharmaceutical analysis** is the branch of chemistry that identifies a drug substance (qualitative analysis), measures how much of it is present (quantitative analysis), and checks its purity, in raw materials, intermediates and finished dosage forms.

- **Qualitative analysis** answers "what is it?" — identification tests, colour reactions, melting point, IR spectrum.
- **Quantitative analysis** answers "how much?" — assay by titration, weighing, or instruments.

**Scope**

| Area | What analysis does there |
| --- | --- |
| Raw material testing | Confirms identity and purity before a batch is made |
| In-process control | Checks blend uniformity, pH, weight of tablets during manufacture |
| Finished product testing | Assay, uniformity of content, dissolution, limit tests before release |
| Stability studies | Measures drug left and degradation products over the shelf life |
| Drug discovery and development | Purity of new molecules, structure confirmation, impurity profiling |
| Clinical and forensic work | Drug levels in blood and urine, poisoning cases, therapeutic drug monitoring |
| Regulatory and quality control | Testing against pharmacopoeial standards; government analysts check samples |

## 1.2 Different techniques of analysis

```text
                       Methods of analysis
              ______________|_________________
             |                                |
      Chemical (classical)               Instrumental
      ______|______                ________|___________________
     |             |              |           |       |        |
 Volumetric   Gravimetric   Electrochemical  Optical  Chromato-  Others
 (titrimetric)              (potentiometry,  (UV-Vis, graphic   (thermal,
                            conductometry,   IR,      (TLC,     mass
                            polarography)    fluorimetry) HPLC, GC) spectrometry)
```

| Technique | Basis | Example |
| --- | --- | --- |
| Volumetric (titrimetric) | Volume of a solution of known strength that reacts exactly with the sample | Acid–base, redox, complexometric, precipitation, non-aqueous titrations |
| Gravimetric | Mass of a pure, stable product formed from the analyte | Sulphate weighed as BaSO4 |
| Electrochemical | Potential, current or conductance of a solution | pH meter, potentiometric and conductometric titrations |
| Spectroscopic (optical) | Absorption or emission of light | UV assay of paracetamol tablets |
| Chromatographic | Separation between a stationary and a mobile phase | HPLC assay, related substances |
| Biological / microbiological | Response of a living system | Antibiotic potency by zone of inhibition |

**Volumetric terms you must know**

- **Titrant** — the solution of known concentration added from the burette.
- **Titrand (analyte)** — the solution being titrated.
- **Equivalence point** — the theoretical point where exactly equivalent amounts have reacted.
- **End point** — the point where the indicator (or instrument) shows the change; the small gap between the two is the **titration error**.
- **Indicator** — a substance that shows the end point by a change in colour, turbidity or fluorescence.

**Requirements for a reaction to be used in a titration:** it must be fast, go to completion in one well-defined way (known stoichiometry), have no side reactions, and have a way of seeing the end point.

## 1.3 Methods of expressing concentration

| Expression | Definition | Formula |
| --- | --- | --- |
| Molarity (M) | Moles of solute in 1 litre of solution | M = (w / Mw) × (1000 / V in ml) |
| Normality (N) | Gram equivalents in 1 litre of solution | N = (w / Eq wt) × (1000 / V in ml) |
| Molality (m) | Moles of solute in 1 kg of solvent | m = (w / Mw) × (1000 / W solvent in g) |
| Formality (F) | Formula weights per litre (used for ionic solids) | Numerically like molarity |
| Mole fraction (X) | Moles of a component ÷ total moles | No unit |
| % w/w, % w/v, % v/v | g per 100 g; g per 100 ml; ml per 100 ml | — |
| ppm | Parts per million; 1 ppm = 1 µg/ml (dilute water solutions) or 1 µg/g | Trace impurities, limit tests |
| ppb | Parts per billion; 1 µg/L | Very small traces |

**Equivalent weight** = molecular weight ÷ n, where n is:

| Type of substance | n |
| --- | --- |
| Acid | Number of replaceable H+ (HCl 1, H2SO4 2, oxalic acid 2) |
| Base | Number of OH− it can accept H+ for (NaOH 1, Na2CO3 to methyl orange 2) |
| Oxidising or reducing agent | Electrons gained or lost per molecule (KMnO4 in acid 5, K2Cr2O7 6) |

**Normality = Molarity × n.** So 0.05 M H2SO4 is 0.1 N, 0.02 M KMnO4 (acid medium) is 0.1 N, and 0.01667 M K2Cr2O7 is 0.1 N. The Indian Pharmacopoeia (IP) now writes titrants in molarity and gives an **equivalence statement** for each assay, for example "1 ml of 0.1 M sodium hydroxide is equivalent to 0.02042 g of potassium hydrogen phthalate".

**Worked examples (check each against the molecular weight)**

1. 4.0 g NaOH (Mw 40.00) in 500 ml: M = (4.0/40.00) × (1000/500) = **0.20 M = 0.20 N**.
2. 4.904 g H2SO4 (Mw 98.08) in 1000 ml: M = 0.05 M; n = 2, so **0.1 N**.
3. 6.303 g oxalic acid dihydrate (H2C2O4·2H2O, Mw 126.07) in 1000 ml: 6.303/126.07 = **0.05 M = 0.1 N** (n = 2 both as an acid and as a reducing agent).
4. 3.161 g KMnO4 (Mw 158.03) in 1000 ml: **0.02 M**; in acid MnO4− + 8H+ + 5e− → Mn2+ + 4H2O, n = 5, so **0.1 N**.
5. 4.903 g K2Cr2O7 (Mw 294.18) in 1000 ml: 0.01667 M; n = 6 → **0.1 N**.
6. Dilution: C1V1 = C2V2. To make 500 ml of 0.1 M HCl from 1 M HCl: V1 = (0.1 × 500)/1 = 50 ml diluted to 500 ml.
7. ppm: 0.5 mg of lead in 1 g of sample = 0.5 mg/1000 mg × 10⁶ = **500 ppm**.

## 1.4 Primary and secondary standards

A **primary standard** is a substance pure enough that a solution of exactly known concentration can be made simply by weighing it and dissolving to a known volume.

**Properties of a good primary standard**

1. Available in very high purity (about 99.9% or better), easy to purify and dry.
2. Stable in air: not hygroscopic, not efflorescent, not oxidised or attacked by CO2.
3. Unchanged on drying at 110–120 °C.
4. High equivalent weight, so weighing errors are small.
5. Readily soluble in the solvent used.
6. Reacts quickly, completely and in a known ratio with the titrant.
7. Impurities easy to test for; cheap and non-toxic where possible.

| Titration type | Primary standards |
| --- | --- |
| Acid–base (to standardise acids) | Anhydrous sodium carbonate, borax (sodium tetraborate decahydrate) |
| Acid–base (to standardise alkalis) | Potassium hydrogen phthalate (KHP), benzoic acid, oxalic acid dihydrate |
| Redox | Potassium dichromate, potassium bromate, potassium iodate, sodium oxalate, arsenic trioxide |
| Precipitation | Sodium chloride, potassium chloride |
| Complexometric | Zinc metal, calcium carbonate |
| Non-aqueous | Potassium hydrogen phthalate (for perchloric acid), benzoic acid (for methoxides) |

A **secondary standard** is a substance whose solution cannot be made accurately by weighing, so its strength is found by titrating against a primary standard (**standardisation**). Examples: NaOH (absorbs moisture and CO2), HCl (volatile, concentrated acid of variable strength), KMnO4 (contains MnO2, decomposes in light), sodium thiosulphate (decomposed by bacteria and CO2), iodine (volatile).

**Molarity factor (f)** = actual molarity ÷ nominal molarity. A solution labelled 0.1 M with f = 1.012 is really 0.1012 M. Results are multiplied by f.

## 1.5 Preparation and standardisation of molar and normal solutions

General rule: weigh roughly (secondary standard) or exactly (primary standard), dissolve in the right solvent, make up to volume, then standardise against a primary standard in triplicate; concordant readings must agree within 0.1 ml.

**General calculation for standardisation**

Actual molarity = (weight of primary standard in g) ÷ (burette reading in ml × weight equivalent to 1 ml of 1 M titrant)

or, from the IP equivalence: expected volume = weight taken ÷ (g equivalent to 1 ml of the nominal solution); f = expected volume ÷ volume used.

| Solution (0.1 M unless stated) | Preparation | Standardised against | Indicator / end point | 1 ml of the nominal titrant ≡ |
| --- | --- | --- | --- | --- |
| Oxalic acid 0.05 M | 6.303 g H2C2O4·2H2O to 1000 ml (primary standard, needs no standardisation, but may be checked against NaOH or KMnO4) | — | — | — |
| Sodium hydroxide | About 4.2 g NaOH in carbon-dioxide-free water to 1000 ml; carbonate-free | Potassium hydrogen phthalate (Mw 204.22) | Phenolphthalein, colourless → pink | 0.02042 g KHP |
| Hydrochloric acid | About 8.5 ml concentrated HCl to 1000 ml | Anhydrous sodium carbonate (Mw 105.99), dried at 270 °C | Methyl orange (or methyl red), boil off CO2 near the end | 0.005299 g Na2CO3 |
| Sulphuric acid 0.05 M | About 3 ml concentrated H2SO4 added slowly to water, cooled, to 1000 ml | Anhydrous sodium carbonate, or standardised NaOH | Methyl orange | 0.005299 g Na2CO3 |
| Sodium thiosulphate | About 25 g Na2S2O3·5H2O and 0.2 g Na2CO3 in freshly boiled, cooled water to 1000 ml | Potassium bromate (or potassium dichromate) + KI + HCl; liberated iodine titrated | Starch near the end, blue → colourless | 0.002784 g KBrO3 (or 0.004903 g K2Cr2O7) |
| Potassium permanganate 0.02 M | About 3.2 g KMnO4 in water, boiled, kept, filtered through glass wool, to 1000 ml; store in dark bottle | Oxalic acid dihydrate or sodium oxalate in dilute H2SO4 at about 60–70 °C | Self-indicator, first permanent pink | 0.006303 g oxalic acid dihydrate (0.006700 g Na2C2O4) |
| Ceric ammonium sulphate | About 65 g ceric ammonium sulphate dissolved with gentle heat in 30 ml H2SO4 and water, to 1000 ml | Arsenic trioxide (dissolved in NaOH, acidified) with osmic acid catalyst | Ferroin, pink → pale blue | 0.004946 g As2O3 |

**Reactions behind the table**

- KHP + NaOH → KNaP + H2O (1 : 1). Mw 204.22 → 0.02042 g per ml of 0.1 M.
- Na2CO3 + 2HCl → 2NaCl + H2O + CO2. Mw 105.99 ÷ 2 = 52.99 → 0.005299 g per ml of 0.1 M HCl. With H2SO4, 1 mol Na2CO3 reacts with 1 mol H2SO4, so 1 ml of 0.05 M H2SO4 ≡ 0.005299 g as well.
- KBrO3 + 6KI + 6HCl → KBr + 3I2 + 6KCl + 3H2O; I2 + 2Na2S2O3 → 2NaI + Na2S4O6. One bromate releases 3 I2 = 6 thiosulphate, so 167.00 ÷ 6 = 27.83 → 0.002783 g per ml of 0.1 M (IP rounds to 0.002784).
- Cr2O7²⁻ + 6I⁻ + 14H⁺ → 2Cr³⁺ + 3I2 + 7H2O; 294.18 ÷ 6 = 49.03 → 0.004903 g per ml.
- 2MnO4⁻ + 5C2O4²⁻ + 16H⁺ → 2Mn²⁺ + 10CO2 + 8H2O. 0.02 M permanganate is 0.1 N, oxalate n = 2: 126.07 ÷ 2 × 0.1 = 6.303 mg; Na2C2O4 134.00 ÷ 2 × 0.1 = 6.700 mg.
- Ce⁴⁺ + e⁻ → Ce³⁺ (n = 1, so 0.1 M = 0.1 N). As2O3 gives 2 As(III) each losing 2 e⁻ = 4 e⁻; 197.84 ÷ 4 × 0.1 = 4.946 mg.

**Worked standardisation of NaOH**

0.4085 g KHP dissolved in 50 ml water needed 19.85 ml of "0.1 M" NaOH.
Moles KHP = 0.4085/204.22 = 0.002000 mol. Molarity = 0.002000/0.01985 L = **0.1008 M** (f = 1.008).
Same by the IP route: expected volume = 0.4085/0.02042 = 20.00 ml; f = 20.00/19.85 = 1.008.

**Worked standardisation of thiosulphate with dichromate**

0.1225 g K2Cr2O7 (with excess KI and acid) needed 24.80 ml thiosulphate. Expected volume for 0.1 M = 0.1225/0.004903 = 24.98 ml; f = 24.98/24.80 = 1.007; **M = 0.1007**.

## 1.6 Errors in analysis

**Error** = observed value − true value. No measurement is free from error; analysis aims to know it and keep it small.

### Types of errors

| Type | Nature | Examples | Remedy |
| --- | --- | --- | --- |
| **Determinate (systematic)** | Have a definite cause; same direction each time; can be found and corrected | See below | Calibration, blanks, controls, change of method |
| **Indeterminate (random)** | No single cause; small, scatter both ways; follow normal distribution | Tiny fluctuations in reading a burette, temperature, judging colour | Repeat measurements and average; statistics |
| **Gross errors** | Big human mistakes | Wrong reading, spilled sample, wrong calculation | Care; discard results with a known mistake |

**Determinate errors in detail (sources)**

1. **Instrumental errors** — uncalibrated burettes, pipettes and flasks; unequal balance arms; drifting pH meter.
2. **Reagent errors** — impurities in reagents, attack of glass by alkali, water containing CO2.
3. **Method errors** — the chemistry itself: incomplete reaction, side reactions, co-precipitation, solubility of a precipitate, indicator changing colour before or after the equivalence point.
4. **Personal (operative) errors** — colour blindness, consistently reading the meniscus too high, parallax, bias toward an expected value.
5. Also: constant errors (same size whatever the sample) and proportional errors (grow with sample size).

### Methods of minimising errors

1. **Calibration** of apparatus (burettes, pipettes, flasks, weights) and instruments.
2. **Blank determination** — repeat the procedure without the sample; subtract the blank (corrects reagent impurities and indicator consumption).
3. **Control determination** — analyse a standard of known composition alongside the sample.
4. **Independent method** — check by a different method of analysis.
5. **Parallel (replicate) determinations** — run in duplicate or triplicate; concordant results.
6. **Standard addition** — add a known amount of analyte and see that it is recovered.
7. **Internal standards** (mainly in instrumental methods).
8. **Amplification and isotope dilution** — for very small quantities.
9. Use pure reagents, good technique, proper training.

### Accuracy, precision and significant figures

- **Accuracy** — how close a result is to the true value. Measured by error.
  - Absolute error E = X − Xt.
  - Relative error = (X − Xt)/Xt × 100 (as %) or × 1000 (as parts per thousand).
- **Precision** — how close repeated results are to each other (reproducibility). Measured by deviation, standard deviation, relative standard deviation.

```text
  Target analogy (centre = true value)
  accurate + precise:     hits clustered in the centre
  precise, not accurate:  tight cluster away from the centre  (systematic error)
  accurate, not precise:  scattered around the centre         (random error)
  neither:                scattered and away from centre
```

**Statistical terms**

| Term | Formula |
| --- | --- |
| Mean | x̄ = Σx / n |
| Median | Middle value of results in order |
| Deviation | d = x − x̄ |
| Average deviation | Σ|d| / n |
| Range | Highest − lowest |
| Standard deviation (sample) | s = √[Σ(x − x̄)² / (n − 1)] |
| Relative standard deviation (RSD, coefficient of variation) | RSD = (s / x̄) × 100 |

**Worked example.** Five titres: 10.12, 10.15, 10.10, 10.14, 10.14 ml.

- Mean = 50.65/5 = **10.13 ml**.
- Deviations: −0.01, +0.02, −0.03, +0.01, +0.01. Squares: 0.0001, 0.0004, 0.0009, 0.0001, 0.0001; sum = 0.0016.
- s = √(0.0016/4) = √0.0004 = **0.02 ml**.
- RSD = 0.02/10.13 × 100 = **0.20%**.
- If the true titre is 10.00 ml: absolute error = +0.13 ml; relative error = 1.3% (13 parts per thousand). The results are precise but not accurate — a sign of a systematic error.

**Significant figures** — all certain digits plus the first uncertain digit.

| Rule | Example | Significant figures |
| --- | --- | --- |
| All non-zero digits count | 24.85 | 4 |
| Zeros between non-zero digits count | 10.05 | 4 |
| Leading zeros do not count | 0.0042 | 2 |
| Trailing zeros after a decimal point count | 25.00 | 4 |
| Trailing zeros in a whole number are unclear; use scientific notation | 2500 vs 2.50 × 10³ | 2–4 vs 3 |

- **Addition and subtraction**: keep as many decimal places as the least precise number (24.1 + 0.256 = 24.4).
- **Multiplication and division**: keep as many significant figures as the number with the fewest (2.54 × 1.2 = 3.0).
- **Rounding**: round only at the end; if the digit dropped is above 5 round up, below 5 leave it.
- A burette reads to 0.05 ml (write 20.35, not 20.3); an analytical balance to 0.0001 g.

## 1.7 Pharmacopoeia

A **pharmacopoeia** is the official book of standards for drugs, published under the authority of a government. Its standards are legally binding for drugs sold in that country.

- **Indian Pharmacopoeia (IP)** — published by the **Indian Pharmacopoeia Commission (IPC), Ghaziabad**, under the Ministry of Health and Family Welfare. First edition 1955; the current edition is IP 2022. Its standards are enforced through the Drugs and Cosmetics Act, 1940.
- Others: British Pharmacopoeia (BP), United States Pharmacopeia (USP), European Pharmacopoeia (Ph. Eur.), Japanese Pharmacopoeia, International Pharmacopoeia (WHO).

**What a monograph contains:** title, chemical name, structure, molecular formula and weight, category, dose (in some), description, solubility, identification tests, tests for purity (limit tests, related substances, loss on drying, sulphated ash, heavy metals), assay with the equivalence statement, storage and labelling. **Appendices** describe general methods: limit tests, titrations, reagents, volumetric solutions, apparatus.

## 1.8 Sources of impurities in medicinal agents

An **impurity** is any substance in a drug other than the drug itself and intended additives. Impurities can be toxic, reduce the strength of the drug, change its colour, smell or taste, or speed up its breakdown.

| Source | How impurities get in | Examples |
| --- | --- | --- |
| Raw materials | The starting material is itself impure | Rock salt containing calcium and magnesium salts; lead and arsenic in minerals |
| Reagents used in manufacture | Excess or impure reagents left behind | Soluble alkali left in a precipitated drug; ammonia, sulphate |
| Solvents | Water and organic solvents carry impurities | Tap water brings Ca, Mg, chloride; residual organic solvents |
| Reaction vessels and apparatus | Metal and glass dissolve into the product | Iron, copper, lead from vessels; alkali from glass |
| Intermediates and by-products | Incomplete reaction or side reactions | Unreacted p-aminophenol in paracetamol |
| Manufacturing hazards | Particulate matter, cross-contamination, microbial contamination, errors | Dust, fibres, traces of another product made in the same plant |
| Atmospheric contamination | Dust, moisture, CO2, sulphur dioxide | Sodium hydroxide absorbing CO2 to form carbonate |
| Storage (decomposition) | Light, air, heat, moisture | Ferrous sulphate oxidised to ferric; hydrogen peroxide losing oxygen; deliquescence or efflorescence |
| Containers and closures | Leaching from glass, metal, plastic, rubber | Alkali from soft glass; plasticisers |
| Deliberate adulteration | Cheaper material added for profit | — |

## 1.9 Limit tests

A **limit test** is a semi-quantitative test that checks whether a small, known impurity is below the maximum amount allowed (the limit), by comparing the turbidity, colour or stain produced by the sample with that from a **standard** containing exactly the permitted amount under identical conditions.

- If the test is **less** turbid / coloured than the standard, the sample **passes**.
- Limit tests do not measure the exact amount; they only say "within limit" or "not".
- **Nessler cylinders** (matched glass cylinders of equal diameter and glass) are used so that turbidity or colour can be compared by viewing vertically against a white or black background.

| Limit test | Reagent and conditions | What forms | Compared by |
| --- | --- | --- | --- |
| **Chloride** | Dilute nitric acid + silver nitrate | White opalescence of AgCl | Opalescence (black background) |
| **Sulphate** | Dilute HCl + barium sulphate reagent (barium chloride with a seed of barium sulphate, potassium sulphate in alcohol) | White turbidity of BaSO4 | Turbidity |
| **Iron** | Citric acid (20% w/v) + thioglycollic acid, made alkaline with ammonia | Purple ferrous thioglycollate complex | Colour (white background) |
| **Arsenic** | Gutzeit apparatus: stannated HCl, potassium iodide, stannous chloride, arsenic-free zinc; lead acetate cotton wool; mercuric chloride paper | Arsine gas → yellow to brown stain on HgCl2 paper | Length and intensity of stain |
| **Heavy metals** | Acetate buffer pH 3.5 + hydrogen sulphide (or thioacetamide) | Brown/black colour of metal sulphides | Colour against a lead standard |

**Why each reagent is used**

- **Chloride**: nitric acid keeps the solution acidic so that other ions (carbonate, phosphate) do not precipitate with silver, and makes the opalescence finer.
- **Sulphate**: HCl prevents precipitation of barium carbonate, phosphate etc.; the alcoholic potassium sulphate in the reagent gives seed crystals so that turbidity forms quickly and evenly.
- **Iron**: citric acid forms a complex with iron and prevents its precipitation as hydroxide when ammonia is added; thioglycollic acid reduces Fe³⁺ to Fe²⁺ and forms the purple complex, so all iron is detected whatever its oxidation state.
- **Arsenic**: zinc + HCl produce nascent hydrogen, which reduces arsenic compounds to **arsine (AsH3)**; KI and SnCl2 reduce pentavalent arsenic to the trivalent form, which is reduced faster, and keep evolution steady; **lead acetate cotton wool** traps hydrogen sulphide (which would otherwise blacken the paper); arsine reacts with mercuric chloride paper to give a yellow-brown stain.

```text
   GUTZEIT ARSENIC APPARATUS
        ___
       |   |  <- mercuric chloride paper clamped between
       |___|     two flat ends of glass tube
         |
         |   <- glass tube packed with lead acetate cotton wool
         |      (absorbs H2S)
     ____|____
    |         |  <- wide-mouthed bottle (about 120 ml)
    | sample  |     sample + stannated HCl + KI + SnCl2 + zinc
    |_________|     kept at about 40 °C for 40 minutes
```

**Remember**

- Molarity × n = Normality; IP titrants are written in molarity with an equivalence statement.
- Primary standards: pure, stable, non-hygroscopic, high equivalent weight (KHP, Na2CO3, K2Cr2O7, KBrO3, As2O3, NaCl).
- NaOH vs KHP (phenolphthalein); HCl/H2SO4 vs Na2CO3 (methyl orange); thiosulphate vs KBrO3 or K2Cr2O7 (starch); KMnO4 vs oxalic acid (self-indicator); ceric vs As2O3 (ferroin, osmic acid).
- Systematic errors can be corrected; random errors are reduced by repeating and averaging.
- Accuracy = closeness to the true value; precision = closeness of results to each other; RSD = s/x̄ × 100.
- IP is published by the IPC, Ghaziabad; first edition 1955.
- Limit tests compare sample with standard in Nessler cylinders: Cl (AgNO3 + HNO3), SO4 (BaCl2 + HCl), Fe (thioglycollic acid + citric acid + NH3), As (Gutzeit, HgCl2 paper).
