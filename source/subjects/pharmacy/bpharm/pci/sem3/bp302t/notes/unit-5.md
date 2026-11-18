# Unit 5: pH, buffers and isotonic solutions

Eye drops that sting, an injection that damages red blood cells, or a solution in which the drug breaks down within days are usually problems of pH, buffering or tonicity. This unit gives the tools to measure and control pH, design buffers, and make solutions isotonic with body fluids. Numericals from this unit (buffer pH, buffer capacity, sodium chloride needed for isotonicity) appear in almost every paper.

## 5.1 Sørensen's pH scale

Sørensen (1909) proposed expressing hydrogen ion concentration on a logarithmic scale:

**pH = − log [H3O+]** (strictly, − log of the hydrogen ion **activity**)

Water ionises slightly: 2H2O ⇌ H3O+ + OH−

Kw = [H3O+][OH−] = 1 × 10⁻¹⁴ at 25 °C, so **pH + pOH = 14**.

| [H3O+] (mol/L) | pH | Nature |
| --- | --- | --- |
| 10⁻¹ | 1 | Strongly acidic |
| 10⁻⁷ | 7 | Neutral (at 25 °C) |
| 10⁻¹² | 12 | Strongly basic |

**Points to note**

- A change of 1 pH unit means a **10-fold** change in [H3O+].
- Kw increases with temperature, so neutral water at 37 °C has a pH slightly below 7.
- pH can be below 0 or above 14 for very concentrated acids or bases, but 0–14 covers practical work.

**Calculating pH**

| Solution | Formula | Example |
| --- | --- | --- |
| Strong acid | pH = − log C | 0.01 M HCl → pH 2 |
| Strong base | pOH = − log C, pH = 14 − pOH | 0.001 M NaOH → pOH 3, pH 11 |
| Weak acid | pH = ½ pKa − ½ log C | 0.1 M acetic acid (pKa 4.76) → pH = 2.38 + 0.5 = **2.88** |
| Weak base | pOH = ½ pKb − ½ log C, then pH = 14 − pOH | 0.1 M ammonia (pKb 4.75) → pOH 2.88, pH 11.12 |

## 5.2 Determination of pH

### Colorimetric method (the syllabus prints it as "calorimetric")

**Indicators** are weak acids or bases whose ionised and un-ionised forms have different colours. For an acid indicator HIn ⇌ H+ + In−:

pH = pKIn + log [In−]/[HIn]

The eye sees a colour change when the ratio moves from about 1:10 to 10:1, so an indicator works over roughly **pKIn ± 1**.

| Indicator | pH range | Colour change (acid → base) |
| --- | --- | --- |
| Methyl orange | 3.1–4.4 | Red → yellow |
| Methyl red | 4.4–6.2 | Red → yellow |
| Bromothymol blue | 6.0–7.6 | Yellow → blue |
| Phenol red | 6.8–8.4 | Yellow → red |
| Phenolphthalein | 8.3–10.0 | Colourless → pink |

**Ways of using indicators:** a series of standard buffers of known pH with the same indicator for colour matching (comparator tubes or discs); **universal indicators** (mixtures giving a range of colours across pH 1–14); **pH papers**.

**Limitations:** only about ±0.1–0.2 pH accuracy; errors in coloured or turbid solutions, in the presence of proteins (protein error) and with high salt concentration (salt error); the indicator itself can change the pH of weakly buffered solutions.

### Electrometric method (pH meter)

The potential of an electrode that responds to H+ is measured against a reference electrode of constant potential.

- **Hydrogen electrode** — the primary standard (platinum black + hydrogen gas at 1 atm); not convenient for routine use.
- **Glass electrode** — a thin bulb of special glass that develops a potential depending on the H+ activity on either side; contains a buffer and an Ag/AgCl internal electrode. Used in all pH meters.
- **Reference electrode** — saturated calomel electrode or silver/silver chloride electrode.

At 25 °C the cell potential changes by about **0.0592 V (59.2 mV) per pH unit**: E = E° + 0.0592 pH (sign depends on the cell arrangement).

```text
        pH METER (millivoltmeter)
          |                 |
   glass electrode    reference electrode
   (H+-sensitive)     (calomel or Ag/AgCl, constant potential)
          \_________________/
              test solution
   Combined electrodes put both in one body.
```

**Using a pH meter:** calibrate with two or three standard buffers (for example pH 4.0, 7.0 and 9.2) at the same temperature as the sample; rinse the electrode between solutions; keep the glass bulb hydrated.

**Errors:** **alkaline (sodium) error** at very high pH with high Na⁺ (reading too low) and **acid error** in very strong acid; temperature differences; dirty or dry membranes.

The electrometric method is accurate (±0.01 pH), works in coloured and turbid solutions, and is the pharmacopoeial method.

## 5.3 Buffers and the buffer equation

A **buffer** is a solution that resists a change in pH when small amounts of acid or base are added, or when it is diluted.

**Types**

| Type | Composition | Example |
| --- | --- | --- |
| Acidic buffer | Weak acid + its salt with a strong base | Acetic acid + sodium acetate |
| Basic buffer | Weak base + its salt with a strong acid | Ammonia + ammonium chloride |
| Salt buffers | Two salts of a polybasic acid | NaH2PO4 + Na2HPO4 (phosphate buffer) |

**How a buffer works (acetate buffer)**

- Add acid: CH3COO− + H3O+ → CH3COOH + H2O (the acetate "mops up" H+).
- Add base: CH3COOH + OH− → CH3COO− + H2O (the acid neutralises OH−).

Either way, only the ratio of salt to acid changes slightly, so pH changes very little.

**Buffer equation (Henderson–Hasselbalch)**

Acidic buffer: **pH = pKa + log [salt] / [acid]**

Basic buffer: **pH = pKw − pKb + log [base] / [salt]**

**Worked example 1.** Buffer of 0.1 M acetic acid and 0.2 M sodium acetate (pKa 4.76):
pH = 4.76 + log (0.2/0.1) = 4.76 + 0.30 = **5.06**.

**Worked example 2.** Ratio of sodium acetate to acetic acid needed for pH 5.0:
log ([salt]/[acid]) = 5.0 − 4.76 = 0.24 → ratio = **1.74 : 1**.

**Worked example 3.** Ammonia buffer, 0.1 M NH3 and 0.1 M NH4Cl, pKb 4.75:
pH = 14 − 4.75 + log (0.1/0.1) = **9.25**.

**Effect of dilution and salts:** dilution changes the pH very little (the ratio stays the same), though ionic strength effects shift pH slightly; adding neutral salts changes the activity coefficients and can shift pH a little.

**Effect of temperature:** pKa changes with temperature, so buffers are calibrated at a stated temperature.

## 5.4 Buffer capacity

**Buffer capacity (β)**, also called buffer efficiency, buffer index or buffer value, is the amount of strong acid or base (gram equivalents per litre) needed to change the pH of the buffer by one unit:

β = ΔB / ΔpH

**Van Slyke equation** (more exact):

β = 2.303 C × Ka [H3O+] / (Ka + [H3O+])²

C = total buffer concentration (acid + salt).

**Key facts**

- β is **maximum when pH = pKa** (salt : acid = 1 : 1). Then βmax = **0.576 C**.
- A buffer is useful over about **pKa ± 1**.
- β increases with the **total concentration** of the buffer.

**Worked example 1 (simple equation).** Adding 0.01 mol of NaOH to 1 L of a buffer raises the pH from 4.76 to 4.86. β = 0.01 / 0.10 = **0.1**.

**Worked example 2 (maximum).** An acetate buffer, total 0.1 M, at pH = pKa: βmax = 0.576 × 0.1 = **0.0576**.

```text
 β
 |        /\           maximum β at pH = pKa
 |      /    \
 |    /        \       useful range: pKa - 1 to pKa + 1
 |__/____________\____
     pKa-1  pKa  pKa+1   pH
```

## 5.5 Buffers in pharmaceutical and biological systems

### Biological buffers

- **Blood** pH is kept at about **7.4** (normal range 7.35–7.45). Buffers: **bicarbonate/carbonic acid** (main plasma buffer), **phosphate** (mainly inside cells), **plasma proteins and haemoglobin**.
  - Using pKa 6.1 for carbonic acid: 7.4 = 6.1 + log [HCO3−]/[H2CO3] → ratio **20 : 1**. The lungs control CO2 and the kidneys control HCO3−.
  - pH below 7.35 = acidosis; above 7.45 = alkalosis.
- **Lacrimal fluid (tears)** has a pH of about 7.4 and some buffering capacity, so tears can bring a slightly acidic or basic eye drop towards neutral if the drop is **weakly buffered**.
- **Urine** pH is about 6 on average (it ranges roughly from 4.5 to 8), which affects excretion of weak acids and bases.

### Pharmaceutical buffers

| Use | Buffers commonly chosen |
| --- | --- |
| Ophthalmic solutions | Boric acid, borate, phosphate (Sørensen's), Gifford's and Palitzsch's borate buffers |
| Parenteral products | Phosphate, citrate, acetate (low concentration) |
| Oral liquids | Citrate, phosphate, acetate |
| Analysis (pharmacopoeial standard buffers) | Phthalate (acidic), phosphate (neutral), borate (alkaline) |

### Preparing pharmaceutical buffer solutions — points to consider

1. Choose a weak acid with **pKa close to the wanted pH**.
2. Use the buffer equation to fix the salt : acid ratio.
3. Choose a **total concentration** that gives enough capacity (usually 0.05–0.5 M for general buffers) — but keep it **low for eye drops and injections** so body fluids can adjust it.
4. Check the pH with a pH meter and adjust.
5. Consider **toxicity and compatibility**: borate buffers must not be used for injections or on broken skin; some buffers precipitate with drugs or metal ions (phosphate with calcium).
6. Consider **sterility, tonicity and stability**.

### Influence of pH and buffers on a product

| Requirement | Explanation |
| --- | --- |
| Stability | Many drugs are most stable in a narrow pH range (e.g. many esters and penicillins degrade faster in acid or alkali), so the product is buffered there |
| Solubility | Weak acids and bases need a suitable pH to stay dissolved (Unit 1) |
| Therapeutic activity / absorption | Un-ionised forms are absorbed better; some preservatives (benzoic acid) work only in the un-ionised form at low pH |
| Comfort | Eye drops and injections far from pH 7.4 sting or cause pain; tissue irritation increases with buffer capacity of the product |
| Compromise | Often a product is made at the pH of best stability with a low buffer capacity, so the body brings it to physiological pH after use |

## 5.6 Buffered isotonic solutions

### Tonicity

**Osmosis** is the movement of solvent through a semipermeable membrane from a dilute solution to a concentrated one. Red blood cells and the cornea behave like semipermeable membranes.

| Solution | Compared with body fluid | Effect on red blood cells |
| --- | --- | --- |
| Isotonic | Same osmotic pressure (e.g. 0.9% NaCl, 5% dextrose) | No change |
| Hypertonic | Higher (e.g. 2% NaCl) | Water leaves cells → they shrink (**crenation**) |
| Hypotonic | Lower (e.g. 0.2% NaCl, water for injection) | Water enters → cells swell and burst (**haemolysis**) |

**Iso-osmotic vs isotonic:** iso-osmotic means equal osmotic pressure measured by a colligative property; isotonic means no change in cell volume in practice. A substance such as boric acid that passes freely into red cells is iso-osmotic at 1.9% but not isotonic with red cells (it causes haemolysis), although it is suitable for the eye.

**Measuring tonicity**

- **Haemolytic method** — observe red cells (or measure haemoglobin released) in the test solution.
- **Colligative methods** — mainly **freezing point depression** (cryoscopy) and osmometry. Blood plasma and tears freeze at **−0.52 °C**, so any solution with a freezing point depression (ΔTf) of 0.52 °C is iso-osmotic with them.

**Calculating ΔTf (Liso method).** ΔTf = Liso × c (c = molar concentration). Liso values (approximate): non-electrolytes 1.9; weak electrolytes 2.0; uni-univalent electrolytes (e.g. NaCl) 3.4; uni-divalent (e.g. Na2SO4) 4.3; di-univalent (e.g. CaCl2) 4.8.

### Methods of adjusting tonicity

**Class I methods** — add sodium chloride (or another substance) to the drug solution to bring its freezing point down to −0.52 °C.

**1. Cryoscopic (freezing point depression) method**

W = (0.52 − a) / b

W = grams of NaCl to add per 100 ml; a = freezing point depression of the unadjusted drug solution; b = freezing point depression of 1% NaCl (about 0.58 °C).

*Worked example.* A 1% boric acid solution has ΔTf about 0.29 °C. NaCl needed per 100 ml:
W = (0.52 − 0.29) / 0.58 = **0.40 g**.

**2. Sodium chloride equivalent (E) method**

**E** = grams of NaCl that have the same osmotic effect as **1 g of the drug**. E can be calculated as E = 17 × Liso / M (M = molecular weight).

Steps: (i) find the NaCl needed to make the whole volume isotonic (0.9 g per 100 ml); (ii) subtract the NaCl equivalent of the drug (weight of drug × E); (iii) the difference is the NaCl to add.

*Worked example.* Make 30 ml of 2% atropine sulfate eye drops isotonic (E = 0.13).
- Atropine sulfate needed = 0.6 g; its NaCl equivalent = 0.6 × 0.13 = 0.078 g.
- NaCl for 30 ml isotonic = 0.9 × 30/100 = 0.27 g.
- NaCl to add = 0.27 − 0.078 = **0.192 g**.

If another tonicity agent (e.g. boric acid, E = 0.50) is used instead of NaCl, divide the NaCl amount by its E: 0.192 / 0.50 = 0.384 g boric acid.

**Class II methods** — dissolve the drug in enough water to make an isotonic solution, then make up to volume with an isotonic (often buffered) vehicle.

**3. White–Vincent method**

V = w × E × 111.1

V = ml of water that makes w g of drug isotonic (111.1 ml is the volume of water made isotonic by 1 g of NaCl, since 0.9 g per 100 ml).

*Worked example.* For the atropine sulfate drops above: V = 0.6 × 0.13 × 111.1 = **8.7 ml**. Dissolve 0.6 g atropine sulfate in 8.7 ml water, then add an isotonic buffered diluent to 30 ml.

**4. Sprowls method** — a ready-made table giving V (the volume of isotonic solution that can be prepared from **0.3 g** of each drug), worked out from the White–Vincent equation. The pharmacist reads V from the table and makes up to volume with an isotonic vehicle.

### Buffered isotonic vehicles

Isotonic buffered diluting solutions (for example isotonic phosphate or borate vehicles) are kept ready to dilute drug concentrates prepared by the White–Vincent or Sprowls method. They give eye drops and injections that are both **buffered at a suitable pH** and **isotonic**.

## Remember

- pH = −log[H3O+]; pH + pOH = 14 at 25 °C; weak acid pH = ½pKa − ½log C.
- Indicators work over about pKIn ± 1; the glass electrode changes about 59 mV per pH unit at 25 °C; calibrate with standard buffers.
- Buffer equation: pH = pKa + log[salt]/[acid]; basic buffer pH = pKw − pKb + log[base]/[salt].
- β = ΔB/ΔpH; Van Slyke β = 2.303CKa[H3O+]/(Ka + [H3O+])²; βmax = 0.576C at pH = pKa.
- Blood pH 7.4, bicarbonate : carbonic acid = 20 : 1; tears pH about 7.4.
- Plasma and tears freeze at −0.52 °C; 1% NaCl ΔTf about 0.58 °C; 0.9% NaCl is isotonic.
- Cryoscopic W = (0.52 − a)/b; E method subtracts drug × E from 0.9 g/100 ml; White–Vincent V = w × E × 111.1; Sprowls table is for 0.3 g of drug.
