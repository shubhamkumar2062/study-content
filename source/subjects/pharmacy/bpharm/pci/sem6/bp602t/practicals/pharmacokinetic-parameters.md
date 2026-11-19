# Calculation of pharmacokinetic parameters from given data

**Aim:** To calculate the pharmacokinetic parameters of a drug — elimination rate constant, half-life, volume of distribution, clearance, area under the curve and bioavailability — from given plasma concentration–time data.

> This exercise is worked from supplied data or simulation software; no animal is used.

## Principle

After an intravenous bolus, a drug that follows **one-compartment, first-order** kinetics shows a plasma concentration that falls exponentially:

```text
 C = C0 . e^(-Kt)        and     log C = log C0 - Kt/2.303

 Plot of log C against time = straight line
   log C |*
         |  *                slope = -K / 2.303
         |     *             intercept = log C0
         |        *
         |___________________ time
```

| Parameter | Formula | Meaning |
| --- | --- | --- |
| Elimination rate constant K | K = 2.303 × slope (sign reversed), or K = 0.693 ÷ t½ | Fraction of drug removed per unit time |
| Half-life t½ | t½ = 0.693 ÷ K | Time for the plasma level to fall by half |
| Volume of distribution Vd | Vd = dose ÷ C0 | Apparent volume relating amount in body to plasma level |
| Clearance CL | CL = K × Vd, or dose ÷ AUC (IV) | Volume of plasma cleared of drug per unit time |
| AUC | Trapezoidal rule, or C0 ÷ K | Total exposure to the drug |
| Bioavailability F | F = (AUC oral ÷ AUC IV) × (dose IV ÷ dose oral) | Fraction of the dose reaching the circulation unchanged |

**Trapezoidal rule:** AUC between two points = (C1 + C2) ÷ 2 × (t2 − t1). The tail beyond the last point is added as C_last ÷ K.

Steady state on repeated dosing is reached in about **4 to 5 half-lives**, and the same number of half-lives is needed for almost complete elimination after stopping.

## Requirements

Supplied plasma concentration–time data, semi-log graph paper or a spreadsheet, calculator with logarithms, ruler.

## Procedure

1. Tabulate time and plasma concentration; add a column for log C.
2. Plot log C against time; draw the best straight line through the points of the elimination phase.
3. Find the slope from two well-separated points on the line and calculate K = 2.303 × slope.
4. Read the intercept at time zero to get C0; calculate t½ = 0.693 ÷ K.
5. Calculate Vd = dose ÷ C0, and CL = K × Vd.
6. Calculate AUC by the trapezoidal rule up to the last point and add the tail C_last ÷ K.
7. If oral data are also given, calculate the oral AUC the same way and work out the bioavailability.
8. State all values with their units.

## Observations and calculations

**Given data (illustrative only, not real data).** Single IV bolus of 500 mg.

| Time (h) | Plasma concentration (µg/mL) | log C |
| --- | --- | --- |
| 0.5 | 40 | 1.602 |
| 1 | 35 | 1.544 |
| 2 | 27 | 1.431 |
| 4 | 16 | 1.204 |
| 6 | 9.5 | 0.978 |
| 8 | 5.7 | 0.756 |

**Slope** from 1 h and 8 h: (1.544 − 0.756) ÷ (8 − 1) = 0.788 ÷ 7 = 0.1126 per hour (as a fall).
**K** = 2.303 × 0.1126 = **0.259 per hour**.
**t½** = 0.693 ÷ 0.259 = **2.67 hours**.
**C0** from the intercept ≈ 45 µg/mL = 45 mg/L.
**Vd** = 500 mg ÷ 45 mg/L = **11.1 L**.
**CL** = 0.259 × 11.1 = **2.87 L/h**.
**AUC** = C0 ÷ K = 45 ÷ 0.259 = **173.7 mg·h/L** (check by the trapezoidal rule).

**Bioavailability example:** an oral dose of 500 mg of the same drug gives AUC 121.6 mg·h/L.
F = (121.6 ÷ 173.7) × (500 ÷ 500) = **0.70, that is 70 %**.

Time to steady state on repeated dosing ≈ 4 to 5 × 2.67 h ≈ **11 to 13 hours**.

## Result

From the given data the pharmacokinetic parameters are: K = 0.259 per hour, t½ = 2.67 hours, Vd = 11.1 L, clearance = 2.87 L/h, AUC = 173.7 mg·h/L and oral bioavailability = 70 % (specimen values).

## Precautions

1. Keep units consistent: convert µg/mL to mg/L (they are numerically equal) before using the dose in mg.
2. Use only the terminal straight part of the log C–time plot for the slope.
3. Take two widely separated points for the slope so that reading errors matter less.
4. Remember that Vd is an apparent volume and may be larger than total body water for drugs bound in tissues.
5. Add the tail area when calculating AUC by the trapezoidal rule.
6. For bioavailability, correct for the doses if the oral and IV doses differ.
7. State whether the data follow one-compartment kinetics; a curved log plot means a two-compartment model.

## Viva questions

1. **What is first-order kinetics?** A constant **fraction** of the drug is eliminated per unit time, so the rate is proportional to concentration.
2. **What is zero-order kinetics? Give an example.** A constant **amount** is eliminated per unit time; alcohol, and phenytoin at higher levels.
3. **Define volume of distribution.** The apparent volume that would be needed to contain the amount of drug in the body at the measured plasma concentration.
4. **Define clearance.** The volume of plasma completely cleared of drug per unit time; CL = K × Vd.
5. **How many half-lives to reach steady state?** About 4 to 5.
6. **How is bioavailability calculated?** From the ratio of the oral to the intravenous AUC, corrected for dose.
7. **What is the bioavailability of an intravenous dose?** 100 %, by definition.
8. **Which drugs show low oral bioavailability and why?** Drugs with high first-pass metabolism, such as glyceryl trinitrate, propranolol, lignocaine and morphine.
9. **What does a curved log concentration–time plot indicate?** More than one compartment, usually a distribution phase followed by an elimination phase.
