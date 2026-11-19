# Simultaneous estimation of ibuprofen and paracetamol by UV spectroscopy

**Aim:** To estimate ibuprofen and paracetamol together in a combined tablet by the simultaneous equation (Vierordt's) method.

> Quantities and wavelengths are typical for a student batch. Determine the λmax values and absorptivities on your own instrument. Follow your lab manual and your teacher where they differ. Wear goggles and gloves; methanol is flammable and toxic.

## Principle

Both drugs absorb in the UV region and their spectra overlap, so one cannot be measured at a single wavelength without the other interfering. If the two do not interact, **absorbances are additive**. The mixture is measured at two wavelengths: λ1 = λmax of paracetamol (X) and λ2 = λmax of ibuprofen (Y). In methanol these lie at about 243–249 nm and about 221–222 nm respectively. With a 1 cm cell:

- A1 = ax1·Cx + ay1·Cy
- A2 = ax2·Cx + ay2·Cy

Solving the two equations:

**Cx = (A2·ay1 − A1·ay2) / (ax2·ay1 − ax1·ay2)**

**Cy = (A1·ax2 − A2·ax1) / (ax2·ay1 − ax1·ay2)**

where ax1, ax2 and ay1, ay2 are the absorptivities, A(1%, 1 cm), of pure paracetamol and pure ibuprofen at λ1 and λ2 (concentration then comes out in g/100 ml).

## Requirements

UV-visible spectrophotometer, matched quartz cells, volumetric flasks (100 ml, 10 ml), pipettes, Whatman filter paper; paracetamol and ibuprofen reference standards, methanol (AR or spectroscopic grade), tablets containing both drugs (for example ibuprofen 400 mg and paracetamol 325 mg).

## Procedure

1. **Standard stocks:** dissolve 10 mg of each drug separately in methanol and make up to 100 ml (100 µg/ml).
2. **λmax:** dilute each stock to about 10 µg/ml and scan from 200 to 400 nm against methanol; note λmax of each (λ1 for paracetamol, λ2 for ibuprofen).
3. **Absorptivities:** prepare 4–5 dilutions of each drug (for example 2–20 µg/ml); read each at both λ1 and λ2. Calculate A(1%, 1 cm) = A/c (c in g/100 ml) for each reading and take the mean (ax1, ax2, ay1, ay2). Check that each drug obeys Beer's law at both wavelengths.
4. **Sample:** weigh and powder 20 tablets; find the average weight. Weigh powder equal to one-tenth of the average tablet weight, shake with about 60 ml methanol for 15 minutes, make up to 100 ml, and filter (discard the first few ml).
5. Dilute 2.5 ml of the filtrate to 100 ml with methanol (dilution 2.5 → 100).
6. Read the absorbance of the diluted sample at λ1 and λ2 against methanol.
7. Calculate Cx and Cy with the equations and convert to mg per tablet.

## Observations and calculations

> Example readings and absorptivities, for practice only — record your own.

| Drug | A(1%, 1 cm) at λ1 (paracetamol λmax) | A(1%, 1 cm) at λ2 (ibuprofen λmax) |
| --- | --- | --- |
| Paracetamol (X) | ax1 = 650 | ax2 = 300 |
| Ibuprofen (Y) | ay1 = 30 | ay2 = 450 |

Sample absorbances: A1 = 0.553, A2 = 0.687.

Denominator: ax2·ay1 − ax1·ay2 = (300 × 30) − (650 × 450) = 9,000 − 292,500 = −283,500.

Cx = (0.687 × 30 − 0.553 × 450)/(−283,500) = (20.61 − 248.85)/(−283,500) = 8.051 × 10⁻⁴ g/100 ml = **8.05 µg/ml paracetamol**.

Cy = (0.553 × 300 − 0.687 × 650)/(−283,500) = (165.9 − 446.55)/(−283,500) = 9.899 × 10⁻⁴ g/100 ml = **9.90 µg/ml ibuprofen**.

**Back to the tablet:** dilution factor = 100/2.5 = 40, so the first 100 ml held 8.05 × 40 = 322 µg/ml paracetamol (32.2 mg) and 9.90 × 40 = 396 µg/ml ibuprofen (39.6 mg). The powder taken was one-tenth of a tablet, so per tablet: paracetamol **322 mg (99.1% of 325 mg)** and ibuprofen **396 mg (99.0% of 400 mg)**.

**Validity check:** (A2/A1)/(ax2/ax1) = 2.69 and (ay2/ay1)/(A2/A1) = 12.1; both lie outside 0.1–2.0, so the method gives reliable results.

## Result

Each tablet contains ___ mg of paracetamol (___% of label) and ___ mg of ibuprofen (___% of label).

## Precautions

1. Use the same matched cell for all readings, or check matching with solvent.
2. Measure absorptivities on the same instrument and same day as the sample.
3. Filter the sample solution; insoluble excipients scatter light.
4. Keep absorbances within 0.2–0.8.
5. Methanol is toxic and flammable; work in a ventilated area.

## Viva questions

1. **What is the basis of the simultaneous equation method?** Additivity of absorbance of non-interacting components (Beer's law).
2. **How are the two wavelengths chosen?** The λmax of each drug.
3. **What is an isosbestic point?** A wavelength where two species have equal absorptivity; used in the absorbance ratio (Q-value) method.
4. **Name other multicomponent methods.** Absorbance ratio, derivative spectroscopy, difference spectroscopy, HPLC.
5. **Why is methanol used?** Both drugs dissolve well and it is transparent above about 205 nm.
6. **When does the method fail?** When the spectra are almost identical, when the drugs interact, or when excipients absorb.
