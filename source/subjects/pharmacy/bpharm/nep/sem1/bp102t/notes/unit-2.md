# Unit 2: Pharmaceutical calculations, posology, dosage forms, APIs and excipients

This unit gives you the tools used every day in dispensing: weighing and measuring in metric units, working out strengths and dilutions, making alcohol and eye drops of the right strength, calculating a child's dose, and understanding what a dosage form is made of. Numericals from this unit appear in nearly every paper. All drug names and numbers in the worked examples below are made up for practice.

## 2.1 Metric system of weights and measures

The metric (SI-based) system is the official system in the IP. Units grow or shrink in steps of 10, so conversion is only moving the decimal point.

| Quantity | Base unit | Common pharmaceutical units |
| --- | --- | --- |
| Mass (weight) | gram (g) | kilogram (kg) = 1000 g; milligram (mg) = 10^-3 g; microgram (µg) = 10^-6 g; nanogram (ng) = 10^-9 g |
| Volume | litre (L) | millilitre (ml) = 10^-3 L; microlitre (µl) = 10^-6 L; 1 ml ≈ 1 cm³ |
| Length | metre (m) | centimetre (cm) = 10^-2 m; millimetre (mm) = 10^-3 m; micrometre (µm) = 10^-6 m; nanometre (nm) = 10^-9 m |

**Prefixes**: kilo (10³), centi (10^-2), milli (10^-3), micro (10^-6), nano (10^-9).

Older systems (imperial and apothecaries') are no longer official, but you may meet them: 1 grain ≈ 64.8 mg, 1 pound (lb) ≈ 0.4536 kg (so 1 kg ≈ 2.2 lb), 1 fluid ounce (imperial) ≈ 28.4 ml. Household measures used in labels: **1 teaspoonful = 5 ml, 1 tablespoonful = 15 ml**.

### Scientific notation

Very large or very small numbers are written as a number between 1 and 10 multiplied by a power of 10.

| Ordinary | Scientific notation |
| --- | --- |
| 0.00025 g | 2.5 × 10^-4 g (= 250 µg) |
| 1 500 000 units | 1.5 × 10^6 units |
| 0.000001 m | 1 × 10^-6 m (= 1 µm) |

Rules: when you multiply, add the powers; when you divide, subtract them. Example: (3 × 10^-3) × (2 × 10²) = 6 × 10^-1 = 0.6.

**Tips for accurate work**: always write units; put a zero before a decimal point (0.5 not .5); never add a trailing zero (5 not 5.0); check the answer is sensible.

## 2.2 Percentage and ratio strength (dilute solutions)

| Expression | Meaning |
| --- | --- |
| % w/w (weight in weight) | g of solute in 100 g of product (ointments, powders) |
| % w/v (weight in volume) | g of solute in 100 ml of product (solutions of solids) |
| % v/v (volume in volume) | ml of solute in 100 ml of product (liquids in liquids, alcohol) |
| % v/w | ml of liquid in 100 g of product |
| Ratio strength | 1 in 1000 (1:1000) means 1 g in 1000 ml for a solid in a liquid, unless stated otherwise |
| ppm | parts per million; 1 ppm = 1 mg per litre (or per kg) |

When a percentage is written without a type, the IP convention is: solids in liquids w/v, liquids in liquids v/v, solids in solids w/w.

**Worked examples**

1. 2.5 g of a drug in 50 ml solution: strength = 2.5/50 × 100 = **5% w/v**.
2. 4 g of drug in 80 g of ointment: 4/80 × 100 = **5% w/w**.
3. A 1 in 2500 solution as a percentage: 100/2500 = **0.04% w/v**.
4. Drug in 250 ml of a 1 in 400 solution: 250/400 = **0.625 g**.

### Dilution of solutions

Amount of drug does not change on dilution, so

```text
C1 × V1 = C2 × V2        (C = strength, V = volume or weight)
```

- **Example 1**: How much water must be added to 200 ml of a 25% w/v solution to make it 10% w/v? V2 = 200 × 25/10 = 500 ml. Dilute to **500 ml**, i.e. add about **300 ml** water (always "make up to volume").
- **Example 2**: Volume of a 1 in 200 stock needed to make 500 ml of a 1 in 1000 solution: V1 = 500 × (1/1000) ÷ (1/200) = **100 ml** stock, made up to 500 ml.
- **Stock solutions** are concentrated solutions kept ready so that small quantities can be measured accurately by dilution.

## 2.3 Alligation

Alligation is a quick arithmetic method for mixing two strengths to get an intermediate strength.

### Alligation medial

Finds the strength of a mixture of known quantities. Strength of mixture = Σ(quantity × strength) ÷ Σ quantity.

Example: 300 g of 10% w/w ointment mixed with 200 g of 4% w/w ointment: (3000 + 800)/500 = **7.6% w/w**.

### Alligation alternate

Finds in what proportion two strengths must be mixed.

```text
 Higher strength  10 \           / (5 − 2) = 3 parts of 10%
                      \ 5 (wanted)
 Lower strength    2 /           \ (10 − 5) = 5 parts of 2%
                                  -----------
                                   total 8 parts
```

Example: make **400 g of 5% w/w** ointment from 10% w/w and 2% w/w ointments. Parts = 3 : 5 (total 8). 10% ointment = 400 × 3/8 = **150 g**; 2% ointment = 400 × 5/8 = **250 g**.

A diluent (water, base) is treated as **0%**. Example: 500 ml of 4% w/v from a 20% w/v stock: 20 → 4 parts, 0 → 16 parts, ratio 1 : 4; take **100 ml** stock and make up to 500 ml (same as C1V1).

Check every alligation answer by alligation medial.

## 2.4 Proof spirit

- **Proof spirit** is a mixture of ethanol and water that contains **57.1% v/v** (about 49.3% w/w) ethanol at 51 °F (about 10.6 °C). It is defined as **100° proof**.
- The name comes from an old test: gunpowder soaked in the spirit could still be lit ("proved") only if the spirit was at least this strong.
- Spirit stronger than proof is **over proof (OP)**; weaker is **under proof (UP)**. 100% ethanol is 175.3° proof, i.e. 75.3 OP.
- Proof strength matters for excise duty on alcohol used in medicines.

**Formulae**

```text
Degree proof          = % v/v ethanol × 1.753      (1.753 = 100 / 57.1)
Degrees OP            = degree proof − 100
Degrees UP            = 100 − degree proof
Volume of proof spirit = volume of sample × degree proof / 100
% v/v ethanol         = degree proof / 1.753
```

**Worked examples**

1. 90% v/v alcohol: 90 × 1.753 = 157.8° proof = **57.8 OP**.
2. 40% v/v alcohol: 40 × 1.753 = 70.1° proof = **29.9 UP**.
3. Proof spirit in 2 litres of 60% v/v alcohol: 60 × 1.753 = 105.18° proof; 2000 × 105.18/100 = **2103.6 ml** of proof spirit.
4. 500 ml of spirit at 60 OP (160° proof): proof spirit = 500 × 160/100 = **800 ml**; strength = 160/1.753 = **91.3% v/v**.
5. Dilute 95% v/v alcohol to 45% v/v: by alligation 95 vs 0 → 45 parts of 95% to 50 parts water; in practice take 45 volumes of 95% alcohol and **make up to 95 volumes** with water, because alcohol and water contract on mixing.

## 2.5 Isotonic solutions

- **Osmotic pressure** depends on the number of particles in solution. **Isotonic** solutions have the same osmotic pressure as body fluids (blood, tears); **hypotonic** have less (cells swell and may burst, haemolysis); **hypertonic** have more (cells shrink, crenation).
- Blood plasma and tears freeze at **−0.52 °C**. A solution that freezes at −0.52 °C is isotonic. **0.9% w/v sodium chloride** and **5% w/v dextrose** are isotonic.
- Importance: injections (especially large volume and intrathecal), eye drops, nasal drops and wound washes should be isotonic for comfort and to avoid tissue damage.

### Method 1: Freezing point depression (FPD) method

```text
W = (0.52 − a) / b
W = g of adjusting substance per 100 ml
a = FPD of the unadjusted drug solution (°C)
b = FPD of a 1% w/v solution of the adjusting substance (NaCl: 0.576 °C)
```

Check: plain NaCl, a = 0, W = 0.52/0.576 = 0.90 g per 100 ml, which is why 0.9% is isotonic.

Example: a 1% w/v solution of drug X lowers the freezing point by 0.10 °C. NaCl needed = (0.52 − 0.10)/0.576 = **0.73 g per 100 ml**.

### Method 2: Sodium chloride equivalent (E) method

**E** = weight of NaCl that has the same osmotic effect as 1 g of the drug.

Example: make 60 ml of an isotonic 2% w/v solution of drug Y (E = 0.20).
1. Drug present = 2 × 60/100 = 1.2 g.
2. Its NaCl equivalent = 1.2 × 0.20 = 0.24 g.
3. NaCl needed for 60 ml isotonic = 0.9 × 60/100 = 0.54 g.
4. NaCl to add = 0.54 − 0.24 = **0.30 g**.

### Other methods

- **White–Vincent method**: volume of water that makes a given weight of drug isotonic, V = W × E × 111.1 (ml); the rest of the volume is made up with an isotonic vehicle. Example: 0.3 g of drug Y (E 0.20) needs 0.3 × 0.20 × 111.1 = **6.7 ml** water.
- **Molar concentration method**: uses the number of particles (osmolarity); plasma is about 290 mOsm/L.

## 2.6 Geometric dilution

Used to mix a **small amount of a potent drug** evenly with a large amount of diluent (for example lactose).

1. Weigh the drug and the diluent.
2. Put the drug in the mortar; add an **equal amount** of diluent and triturate well.
3. Add diluent equal to the amount now in the mortar and mix again.
4. Keep doubling until all the diluent is added.

```text
 drug 50 mg + diluent 50 mg  →  100 mg
 + 100 mg diluent             →  200 mg
 + 200 mg diluent             →  400 mg
 ... continue doubling until the total (for example 5 g) is reached
```

A coloured inert powder (for example a trace of carmine) can be used to check uniform mixing. In the example, 50 mg in 5 g gives a **1% w/w** trituration.

## 2.7 Posology

**Posology** (Greek *posos* = how much, *logos* = study) is the branch of pharmacy that deals with doses. A **dose** is the quantity of a drug given at one time to produce the desired effect.

| Term | Meaning |
| --- | --- |
| Therapeutic dose | Amount that gives the desired effect |
| Minimum dose | Smallest amount that gives an effect |
| Maximum dose | Largest amount that can be given safely at one time |
| Loading dose | Larger first dose to reach the needed blood level quickly |
| Maintenance dose | Dose that keeps the level steady |
| Prophylactic dose | Dose given to prevent disease |

### Factors affecting dose

Age (children and elderly need less), body weight and body surface area, sex (pregnancy and lactation need care), route of administration, time of administration (before or after food), environment (temperature, altitude), emotional factors and placebo effect, presence of disease (liver or kidney disease reduces elimination), tolerance, idiosyncrasy and allergy, cumulation, synergism and antagonism with other drugs, accumulation and genetic factors.

### Dose calculation formulas

All give a **fraction of the adult dose**. They are approximations; for most drugs official references give doses by weight (per kg) or BSA, and the pharmacist checks these.

| Basis | Rule | Formula |
| --- | --- | --- |
| Age | **Young's rule** (children 1–12 years) | Child dose = Age (years) / (Age + 12) × Adult dose |
| Age | **Dilling's rule** | Child dose = Age (years) / 20 × Adult dose |
| Age | **Cowling's rule** | Child dose = Age at next birthday / 24 × Adult dose |
| Age | **Fried's rule** (infants under 2 years) | Infant dose = Age (months) / 150 × Adult dose |
| Body weight | **Clark's rule** | Child dose = Weight (lb) / 150 × Adult dose |
| Body weight | Per kg | Dose = dose per kg × body weight (kg) |
| Body surface area | **BSA method** (most accurate) | Child dose = BSA of child (m²) / 1.73 × Adult dose |

BSA is read from a **nomogram** (height and weight) or calculated, for example by the Mosteller formula: BSA (m²) = √[height (cm) × weight (kg) / 3600]. The average adult BSA is taken as **1.73 m²**.

**Worked fractions**

- 6-year-old by Young's rule: 6/(6 + 12) = **1/3** of the adult dose. By Dilling's rule: 6/20 = **0.3**.
- Child of 44 lb (about 20 kg) by Clark's rule: 44/150 = **0.29** of the adult dose.
- Infant of 18 months by Fried's rule: 18/150 = **0.12** of the adult dose.
- Child 120 cm tall and 25 kg: BSA = √(120 × 25/3600) = 0.91 m²; fraction = 0.91/1.73 = **0.53** of the adult dose.

## 2.8 Routes of administration

| Route | Examples of dosage forms | Points |
| --- | --- | --- |
| Oral | Tablets, capsules, syrups, suspensions | Safe, convenient; slow onset; first-pass metabolism |
| Sublingual / buccal | Sublingual tablets, lozenges | Rapid absorption; avoids first-pass effect |
| Parenteral (IV, IM, SC, intradermal) | Injections, infusions | Fast and complete; needs sterility and trained staff |
| Rectal | Suppositories, enemas | For vomiting or unconscious patients; partly avoids first pass |
| Vaginal | Pessaries, creams | Local action |
| Topical (skin) | Ointments, creams, lotions, dusting powders | Local action on skin |
| Transdermal | Patches | Systemic effect through skin over long time |
| Inhalation | Aerosols, inhalers | Lungs; rapid local action |
| Ophthalmic, otic, nasal | Eye drops, ear drops, nasal drops/sprays | Local action; eye products must be sterile |

## 2.9 Classification of dosage forms

A **dosage form** is the physical form in which a drug is given (drug + excipients made into a usable, stable product).

```text
Dosage forms
 ├── Solid:     powders, granules, tablets, capsules, pills, lozenges, suppositories*
 ├── Liquid
 │    ├── Monophasic: solutions, syrups, elixirs, linctuses, aromatic waters, drops, gargles
 │    └── Biphasic:   suspensions, emulsions
 ├── Semisolid: ointments, creams, pastes, gels, jellies, suppositories*
 └── Gaseous:   aerosols, inhalations, sprays
 (*suppositories are solid at room temperature and melt or dissolve in the body)
```

They are also classified by **route** (oral, parenteral, topical, rectal, etc.) and by **use** (internal or external).

## 2.10 Active pharmaceutical ingredients (APIs) and excipients

### API

**Active pharmaceutical ingredient (API, drug substance)**: the substance in a product that produces the pharmacological (therapeutic) effect. Ideal characteristics: pure and of known identity; stable to light, heat, moisture and air; suitable particle size and solubility for absorption; compatible with excipients; reproducible manufacture; safe and effective at the intended dose.

### Excipients

**Excipients** are substances other than the API that are added intentionally to a dosage form to help make it, protect it, help the patient take it, or control release. They should be pharmacologically inactive at the amount used.

**Ideal characteristics of an excipient**: inert (no therapeutic effect), non-toxic and non-irritant, chemically and physically compatible with the API and other excipients, stable, does not affect bioavailability adversely, acceptable taste, colour and odour, available from reliable sources at low cost, and meets pharmacopoeial standards.

**Importance**: they make manufacture possible (flow, compression, filling), protect the drug from degradation, mask taste and odour, improve appearance and identification, control release and help absorption, and ensure uniform dose.

| Class | Function | Examples |
| --- | --- | --- |
| Diluents (fillers) | Bulk up small doses | Lactose, starch, microcrystalline cellulose |
| Binders | Hold particles together | Starch paste, PVP, acacia |
| Disintegrants | Break tablets apart in fluid | Starch, sodium starch glycolate |
| Lubricants, glidants | Flow and release from machine | Magnesium stearate, talc, colloidal silica |
| Solvents and vehicles | Dissolve or carry drug | Water, ethanol, glycerin |
| Preservatives | Stop microbial growth | Parabens, benzoic acid, benzalkonium chloride |
| Antioxidants | Prevent oxidation | Ascorbic acid, BHA, sodium metabisulphite |
| Sweeteners, flavours, colours | Acceptability and identification | Sucrose, sorbitol, peppermint oil, approved dyes |
| Suspending, emulsifying agents | Stabilise biphasic liquids | Tragacanth, acacia, methylcellulose |
| Buffers, tonicity agents | Control pH, isotonicity | Phosphates, citrates, sodium chloride |
| Bases | Carry drug in semisolids and suppositories | Soft paraffin, PEG, theobroma oil |

## Remember

- Metric steps of 10; 1 teaspoon = 5 ml; 1 kg ≈ 2.2 lb; write 0.5 not .5.
- C1V1 = C2V2 for dilution; alligation alternate gives parts = differences across the cross; diluent = 0%.
- Proof spirit 57.1% v/v = 100° proof; degree proof = % v/v × 1.753; OP above 100, UP below.
- Isotonic: FP −0.52 °C; 0.9% NaCl; FPD of 1% NaCl 0.576 °C; W = (0.52 − a)/b; E method subtracts the drug's NaCl equivalent.
- Geometric dilution: add diluent equal to the mixture each time.
- Young's Age/(Age + 12); Clark's Weight(lb)/150; Fried's months/150; Dilling's Age/20; BSA/1.73.
- Excipient: inert, safe, compatible, stable, cheap, official.
