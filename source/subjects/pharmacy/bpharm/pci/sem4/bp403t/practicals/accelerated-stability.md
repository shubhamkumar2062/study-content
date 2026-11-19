# Accelerated stability study and shelf-life prediction

**Aim:** To carry out an accelerated stability study of a drug solution (for example ascorbic acid solution) at elevated temperatures, and to predict its shelf life at 25 °C using the Arrhenius equation.

> Quantities, temperatures and the assay method are typical for a student batch. Follow your lab manual and your teacher where they differ. The readings below are example values to show the calculation.

## Principle

The rate of chemical degradation rises with temperature according to the **Arrhenius equation**:

log k = log A − Ea/(2.303RT)

Samples are stored at several elevated temperatures. At each temperature the drug remaining is assayed at intervals, the order of reaction is found, and the rate constant k is calculated. A plot of **log k against 1/T** (T in kelvin) is a straight line with slope −Ea/(2.303R). Extrapolating this line to the storage temperature (25 °C, 1/T = 0.003354 K⁻¹) gives k at 25 °C, and the shelf life is:

**t90 = 0.105/k** (first order)

**Assay (example):** ascorbic acid is titrated with standard iodine using starch as indicator (ascorbic acid + I2 → dehydroascorbic acid + 2HI). % drug remaining = (titre at time t / titre at zero time) × 100.

## Requirements

Ascorbic acid (or another suitable drug), distilled water, stoppered glass vials or ampoules, ovens or water baths at 50, 60 and 70 °C, 0.01 N or 0.1 N iodine (standardised), starch indicator, dilute acid (for example metaphosphoric or acetic acid) to stabilise samples before titration, pipettes, burette, conical flasks, graph paper.

## Procedure

1. Prepare a solution of the drug of known strength (for example 1% w/v ascorbic acid) and fill equal volumes into a series of stoppered vials.
2. Assay three vials immediately (zero time) and record the mean titre.
3. Place sets of vials at 50, 60 and 70 °C.
4. At fixed intervals (for example 2, 4, 6 and 8 days), remove vials from each temperature, cool them quickly to room temperature, and assay the remaining drug.
5. Calculate % remaining. Plot log % remaining against time for each temperature; a straight line shows first-order kinetics.
6. Find k at each temperature from the slope (k = −2.303 × slope) or from k = (2.303/t) log (100/% remaining).
7. Plot log k against 1/T, extrapolate to 1/298 K⁻¹, read k at 25 °C and calculate t90. Calculate Ea from the slope.

## Observations and calculations

**% drug remaining**

| Time (days) | 50 °C | 60 °C | 70 °C |
| --- | --- | --- | --- |
| 0 | 100.0 | 100.0 | 100.0 |
| 2 | 97.4 | 94.2 | 87.6 |
| 4 | 95.0 | 88.7 | 76.7 |
| 6 | 92.5 | 83.5 | 67.2 |
| 8 | 90.2 | 78.7 | 58.9 |

log % remaining against time is linear at each temperature, so degradation is first order.

**Rate constants (from day 8 values; the slope of the full line gives the same within error)**

| T (°C) | T (K) | 1/T (K⁻¹) | k = (2.303/8) log(100/%) (day⁻¹) | log k |
| --- | --- | --- | --- | --- |
| 50 | 323.15 | 0.003095 | 0.2879 × log(100/90.2) = 0.0129 | −1.890 |
| 60 | 333.15 | 0.003002 | 0.2879 × log(100/78.7) = 0.0300 | −1.524 |
| 70 | 343.15 | 0.002914 | 0.2879 × log(100/58.9) = 0.0662 | −1.179 |

**Worked calculation.**

1. Slope of log k vs 1/T = (−1.179 − (−1.890))/(0.002914 − 0.003095) = 0.711/(−0.000181) ≈ **−3,930 K**.
2. Ea = −slope × 2.303 × R = 3,930 × 2.303 × 1.987 ≈ **18,000 cal/mol (18 kcal/mol)**.
3. Extrapolate to 25 °C (1/T = 0.003354): log k25 = −1.890 + (−3,930) × (0.003354 − 0.003095) = −1.890 − 1.018 = −2.908; k25 = **1.24 × 10⁻³ day⁻¹**.
4. Shelf life t90 = 0.105/0.00124 ≈ **85 days** (about 2.8 months) at 25 °C.

```text
 log k ^
  -1.2 |                   o 70 °C
       |             o 60 °C
  -1.9 |       o 50 °C
       |                          extrapolated line
  -2.9 | x 25 °C  <------------------------------
       +----------------------------------------> 1/T (K⁻¹)
        0.00335   0.00310   0.00300   0.00291   (1/T decreases to the right)
```

## Result

1. The degradation of the drug follows ___-order kinetics.
2. Rate constants: ___ day⁻¹ (50 °C), ___ day⁻¹ (60 °C), ___ day⁻¹ (70 °C); Ea ≈ ___ kcal/mol.
3. Predicted rate constant at 25 °C = ___ day⁻¹; predicted shelf life (t90) at 25 °C = ___ days.

## Precautions

1. Fill all vials with equal volumes, close them tightly to avoid evaporation and keep headspace the same.
2. Keep oven or bath temperatures constant (±0.5 °C or better).
3. Cool samples quickly and assay them promptly; stabilise ascorbic acid samples in acid before titration.
4. Use at least three temperatures so the Arrhenius line can be checked.
5. Remember the prediction is valid only if the degradation mechanism is the same at all temperatures; confirm with real-time data.

## Viva questions

1. **What is accelerated stability testing?** Storing a product at elevated temperatures (and humidity) to speed degradation and predict shelf life at normal storage by the Arrhenius equation.
2. **What is plotted in the Arrhenius plot?** log k against 1/T (kelvin).
3. **Define shelf life.** Time for the drug content to fall to 90% of its initial value; t90 = 0.105/k for first order.
4. **What is the ICH accelerated condition?** 40 °C ± 2 °C / 75% RH ± 5% RH for 6 months.
5. **Give two limitations.** Mechanism may change at high temperature; not valid for physical instability (emulsions, suspensions), photolysis, microbial or protein degradation.
6. **What is Q10?** The factor by which the rate constant rises for a 10 °C rise in temperature, roughly 2–4 for drug degradation.
7. **Why is ascorbic acid used as an example?** It degrades (mainly by oxidation) at a measurable rate at moderate temperatures and is easily assayed by iodine titration.
