# Estimation of serum creatinine (Jaffe's method)

**Aim:** To estimate the creatinine concentration in the given (simulated) serum sample by Jaffe's alkaline picrate method.

> The printed ER-2020 practical list says "creatine" among the blood tests; colleges almost always estimate **serum creatinine**, which is the routine kidney function test. Follow your kit or manual for exact volumes.

## Principle

Creatinine reacts with **picric acid in alkaline medium** to form an **orange-red** complex (**Jaffe's reaction**), measured at about **490–520 nm** (as stated by the kit).

Two common ways of doing it:

- **Deproteinised (end-point) method:** serum proteins are first removed with picric acid (or tungstic acid); the protein-free filtrate is treated with alkali, and the colour is compared with a standard.
- **Kinetic method (most kits):** serum is added directly to alkaline picrate, and the **increase in absorbance between two fixed times** (for example 30 and 90 seconds) is measured. Creatinine reacts fast, while many interfering substances react slowly, so timing improves specificity.

## Requirements

Colorimeter or semi-auto analyser (kinetic mode), micropipettes, test tubes, centrifuge (for deproteinisation), timer, water bath at 37 °C if the kit requires it. Reagents: picric acid reagent, sodium hydroxide (alkaline buffer), creatinine standard (commonly 2 mg/dl; check the label). Serum sample.

## Procedure (kinetic method, typical)

1. Prepare the working reagent by mixing picric acid and alkaline buffer in the ratio given (often equal volumes); allow to reach room temperature or 37 °C.
2. Set the instrument to zero with distilled water (or reagent) at the stated wavelength.
3. **Standard:** add 100 µl creatinine standard to 1000 µl working reagent, mix, start the timer, read absorbance at 30 seconds (A1) and at 90 seconds (A2).
4. **Test:** repeat with 100 µl serum.
5. Calculate the change in absorbance ΔA = A2 − A1 for each.

### Alternative: deproteinised method (outline)

1. Mix serum with picric acid reagent (as directed), centrifuge, and take clear supernatant.
2. Set up blank, standard and test tubes with supernatant/standard and NaOH; stand about 15–20 minutes; read absorbance against the blank.

## Observations (kinetic method, example)

| | A1 (30 s) | A2 (90 s) | ΔA |
| --- | --- | --- | --- |
| Standard (2 mg/dl) | 0.210 | 0.290 | 0.080 |
| Test | 0.205 | 0.249 | 0.044 |

## Calculations

```text
                          ΔA(test)
 Creatinine (mg/dl)  =  ──────────  ×  Concentration of standard (mg/dl)
                          ΔA(std)
```

**Worked example:** (0.044 / 0.080) × 2 = **1.1 mg/dl**.

**Interpretation:** commonly quoted adult range about 0.6–1.2 mg/dl in men and slightly lower in women; ranges vary by laboratory. Raised values suggest reduced kidney function (acute or chronic kidney disease, obstruction, severe dehydration).

**Using the result:** estimated creatinine clearance by the Cockcroft–Gault equation:
CrCl (ml/min) = [(140 − age) × weight (kg)] / (72 × serum creatinine), × 0.85 for women.
Example: 50-year-old man, 70 kg, creatinine 1.1 → (90 × 70) / (72 × 1.1) = 6300 / 79.2 ≈ **80 ml/min**.

## Result

The serum creatinine of the given sample is ________ mg/dl.

## Precautions

1. Time the readings exactly in the kinetic method.
2. Keep temperature constant – the reaction is very temperature-sensitive.
3. Avoid haemolysed and lipaemic samples; high bilirubin, glucose, ketones and some cephalosporins interfere.
4. Picric acid is explosive when dry; keep it wet and handle with care.

## Viva questions

1. **Why is serum creatinine preferred to urea for kidney function?** It is produced at a constant rate and is little affected by diet or hydration.
2. **What is the colour in Jaffe's reaction?** Orange-red.
3. **Why is the kinetic method more specific?** Creatinine reacts quickly, while slow-reacting interfering substances contribute less in the early timed window.
4. **Name substances that interfere with Jaffe's reaction.** Acetoacetate, glucose, ascorbic acid, bilirubin, cephalosporins.
5. **When is serum creatinine low?** Low muscle mass (elderly, wasting), pregnancy.
