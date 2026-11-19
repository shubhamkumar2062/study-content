# Unit 3: Pharmacokinetic models and the one-compartment open model

This is the most numerical unit of the subject. It explains how plasma concentration–time data are turned into numbers (KE, t½, Vd, AUC, Ka, clearance) and how those numbers predict blood levels after an IV bolus, an IV infusion and an oral dose. All data in the worked examples are **example numbers** for a hypothetical drug, chosen so that the arithmetic is easy to follow.

## 3.1 Introduction to pharmacokinetics

**Pharmacokinetics** is the study of the time course of drug and metabolite concentrations in the body (absorption, distribution, metabolism and excretion) and the construction of models to describe and predict them.

**Uses:** designing dosage regimens, individualising doses (renal or liver disease, children, elderly), bioavailability and bioequivalence assessment, explaining drug interactions, and therapeutic drug monitoring.

**Rate processes**

| Order | Rate equation | Integrated form | Features |
| --- | --- | --- | --- |
| Zero order | dC/dt = −k0 | C = C0 − k0 t | Constant amount removed per unit time; t½ depends on dose (IV infusion, saturated enzymes, controlled-release products) |
| First order | dC/dt = −kC | C = C0 e^(−kt) or log C = log C0 − kt/2.303 | Constant fraction removed per unit time; t½ = 0.693/k, independent of dose (most drugs) |
| Mixed (Michaelis–Menten) | dC/dt = −Vmax C/(Km + C) | — | First order at low C, zero order at high C (Unit 5) |

## 3.2 Pharmacokinetic models

A **model** is a simple mathematical picture of the body used to describe drug concentration with time.

### A. Compartment models

The body is shown as one or more **compartments** — groups of tissues with similar blood flow and drug affinity. A compartment is a kinetic idea, not a real organ. Drug moves between compartments by first-order processes.

- **Open model:** drug leaves the body (elimination present). **Closed:** no elimination.
- **Mammillary model** (most common): one or more peripheral compartments joined to a **central compartment** (plasma and well-perfused tissues), from which elimination occurs.
- **Catenary model:** compartments joined in a chain, like train coaches; seldom used because organs are not arranged this way.

```text
One-compartment open model (IV bolus)

   Dose ──►[  Central compartment  ]── KE ──► eliminated
             (Vd, C)

Two-compartment open model (mammillary)

   Dose ──►[ Central (1) ] ⇄ k12 / k21 ⇄ [ Peripheral (2) ]
                 │
                 └── k10 ──► eliminated

Catenary:  [1] ⇄ [2] ⇄ [3]
```

**Advantages:** simple, needs few data, gives parameters for dosing. **Limitations:** compartments have no anatomical meaning; parameters are averages; the model must be chosen from the data.

### B. Non-compartmental analysis (model-independent)

Uses **statistical moment theory** — the concentration–time curve is treated as a statistical distribution. No compartment is assumed.

| Moment | Formula | Meaning |
| --- | --- | --- |
| Zero moment | AUC = ∫C dt | Extent of exposure |
| First moment | AUMC = ∫t·C dt | Area under the (C × t) vs t curve |
| Mean residence time | MRT = AUMC / AUC | Average time a molecule stays in the body; for a one-compartment IV bolus MRT = 1/KE |
| Mean absorption time | MAT = MRToral − MRTIV | Average time for absorption |

Other model-independent parameters: CL = Dose/AUC, Vss = CL × MRT. **Advantages:** no model assumption, easy, fewer errors in fitting. **Limitations:** assumes linear kinetics; less able to predict profiles of new regimens.

### C. Physiological (physiologically based, PBPK) models

Each compartment is a real organ or tissue (lung, liver, kidney, muscle, fat), with its true volume, blood flow and tissue/blood partition coefficient. Two types:

- **Perfusion (blood-flow) rate-limited models** — for lipophilic drugs; uptake set by blood flow.
- **Diffusion (membrane permeability) rate-limited models** — for polar drugs.

**Advantages:** realistic; can scale from animals to humans; predicts tissue levels and the effect of disease (change in blood flow). **Limitations:** needs many physiological data that are hard to get; complex mathematics.

## 3.3 Pharmacokinetic parameters — definitions and significance

| Parameter | Definition | Formula | Significance |
| --- | --- | --- | --- |
| KE (k, elimination rate constant) | Fraction of drug eliminated per unit time (h⁻¹) | slope of ln C vs t = −KE | Speed of elimination |
| t½ (biological half-life) | Time for plasma concentration (or amount) to fall by half | t½ = 0.693/KE | Dosing interval, time to steady state, duration of washout |
| Vd (apparent volume of distribution) | Volume that would hold the body amount at plasma concentration | Vd = X/C = X0/C0 | Loading dose; extent of distribution |
| AUC | Area under the concentration–time curve | trapezoidal rule; AUC = C0/KE (IV) | Extent of absorption; exposure |
| Ka (absorption rate constant) | Fraction absorbed per unit time (first order) | method of residuals, Wagner–Nelson | Rate of absorption, tmax |
| CLT (total clearance) | Plasma volume cleared of drug per unit time | CLT = KE × Vd = Dose/AUC (IV) = F·Dose/AUC (oral) | Maintenance dose, steady-state level |
| CLR (renal clearance) | Plasma volume cleared by the kidney per unit time | CLR = excretion rate / C = ke × Vd = fe × CLT | Adjustment in renal failure |

Clearance and Vd are **independent** physiological properties; KE and t½ **depend** on both (KE = CL/Vd).

## 3.4 One-compartment open model — (a) Intravenous bolus

**Assumptions:** the body behaves as one well-mixed compartment; distribution is instantaneous; elimination is first order.

dX/dt = −KE X → X = X0 e^(−KE t) → C = C0 e^(−KE t)

ln C = ln C0 − KE t     or     log C = log C0 − KE t / 2.303

```text
 C (linear)                    log C
  │\                           │\
  │ '.                         │  \     straight line,
  │   '-.                      │    \   slope = −KE/2.303
  │      '--..___              │      \
  └──────────────── t          └───────\──── t
  exponential fall             C0 = antilog of intercept
```

**Parameters from the plot**

- KE = −2.303 × slope (log plot) or −slope (ln plot); t½ = 0.693/KE.
- C0 = back-extrapolated y-intercept; Vd = X0/C0.
- AUC0–∞ = C0/KE; CLT = KE × Vd = X0/AUC.

### Worked example 1 — IV bolus (example numbers)

A hypothetical drug, 500 mg IV bolus. Plasma levels:

| t (h) | 1 | 2 | 4 | 6 | 8 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| C (mg/L) | 16.82 | 14.14 | 10.00 | 7.07 | 5.00 | 2.50 |

1. Plot ln C against t. Linear regression gives slope = −0.1733 h⁻¹ and intercept ln C0, so **KE = 0.1733 h⁻¹** and **C0 = 20.0 mg/L**. (Quick check from two points: KE = ln(14.14/5.00)/(8 − 2) = 0.1733 h⁻¹.)
2. t½ = 0.693/0.1733 = **4.0 h** (also seen directly: 10 → 5 mg/L from 4 to 8 h).
3. Vd = X0/C0 = 500/20 = **25 L**.
4. AUC0–∞ = C0/KE = 20/0.1733 = **115.4 mg·h/L**.
5. CLT = KE × Vd = 0.1733 × 25 = **4.33 L/h** (check: 500/115.4 = 4.33).
6. If 60% of the dose is excreted unchanged (fe = 0.6): CLR = 0.6 × 4.33 = **2.60 L/h**; non-renal clearance = 1.73 L/h.
7. Concentration at 10 h = 20 × e^(−0.1733 × 10) = **3.54 mg/L**. Time to fall from 20 to 2.5 mg/L = ln(20/2.5)/0.1733 = **12 h** (three half-lives).
8. MRT = 1/KE = 5.77 h.

### Urinary excretion data (IV bolus)

When blood sampling is difficult and the drug is excreted partly unchanged, KE can be found from urine:

1. **Rate of excretion method:** ln(dXu/dt) = ln(ke X0) − KE t*, where t* is the midpoint of each collection interval. Slope = −KE; intercept gives ke. Fluctuates more but needs fewer samples.
2. **Sigma-minus (amount remaining to be excreted) method:** ln(Xu∞ − Xu) = ln Xu∞ − KE t. Slope = −KE. Needs urine collected until no more drug appears (about 7 half-lives); a single lost sample spoils the result.

Example (example numbers): with fe = 0.6 and a 500 mg dose, Xu∞ = 300 mg. At 4 h, 150 mg have been excreted, so 150 mg remain to be excreted (one half-life); at 8 h, 225 mg excreted and 75 mg remain.

Conditions: drug excreted unchanged in some measurable amount, first-order kinetics, complete bladder emptying.

## 3.5 One-compartment open model — (b) Intravenous infusion

The drug is given at a **constant (zero-order) rate R0** (or k0) and removed by first-order elimination.

dX/dt = R0 − KE X     C = [R0/(KE Vd)] × (1 − e^(−KE t)) = (R0/CL)(1 − e^(−KE t))

**Steady state:** as t → ∞, input = output and

Css = R0/(KE Vd) = R0/CL

```text
 C │            ___________ Css
   │        .-''
   │     .-'   90% of Css after 3.3 t½
   │   .'
   │ .'
   └──────────────────────── t
```

**Time to reach steady state** depends **only on t½**, not on the infusion rate: 50% in 1 t½, 90% in 3.3 t½, 99% in 6.6 t½.

**Loading dose (bolus to reach Css at once):** XL = Css × Vd = R0/KE.

**After stopping the infusion** at time T, the level falls first-order: C = CT e^(−KE t′), where t′ is time since stopping.

**Uses:** drugs needing a steady level (heparin, lidocaine, antibiotics in critical care), drugs with short half-life, parenteral nutrition. An infusion with a loading dose gives Css immediately.

### Worked example 2 — IV infusion (same hypothetical drug, example numbers)

KE = 0.1733 h⁻¹, Vd = 25 L, CL = 4.33 L/h; infusion rate R0 = 20 mg/h.

1. Css = R0/CL = 20/4.33 = **4.62 mg/L**.
2. Level after 8 h = 4.62 × (1 − e^(−0.1733 × 8)) = 4.62 × 0.75 = **3.46 mg/L** (two half-lives → 75% of Css).
3. Time to 90% of Css = 3.32 × t½ = 3.32 × 4 = **13.3 h** (= ln 10 / KE).
4. Loading dose to reach 4.62 mg/L at once = Css × Vd = 4.62 × 25 = **115 mg**.
5. To keep a target Css of 10 mg/L: R0 = Css × CL = 10 × 4.33 = **43.3 mg/h**, with loading dose 10 × 25 = **250 mg**.
6. Infusion of 20 mg/h stopped at 24 h: C24 = 4.62 × (1 − e^(−0.1733 × 24)) = 4.55 mg/L; 6 h later C = 4.55 × e^(−0.1733 × 6) = **1.61 mg/L**.

## 3.6 One-compartment open model — (c) Extravascular administration

After an oral or IM dose the drug must be absorbed. With first-order absorption (Ka) and elimination (KE):

C = [F X0 Ka / (Vd (Ka − KE))] × (e^(−KE t) − e^(−Ka t))

- **Absorption phase:** rate of absorption > rate of elimination, C rises.
- **Peak (tmax):** absorption rate = elimination rate.
- **Post-absorption (elimination) phase:** absorption almost over, C falls.

tmax = ln(Ka/KE) / (Ka − KE)     Cmax = (F X0/Vd) e^(−KE tmax)     AUC = F X0/CL

If Ka is much larger than KE, the terminal slope gives KE. If Ka is smaller than KE, the terminal slope reflects Ka instead — **flip-flop kinetics** (seen with some slow-release products).

**Lag time (tlag):** the delay before absorption starts (gastric emptying, disintegration). It shows as the point where the extrapolated terminal line and the residual line cross above zero time.

### Worked example 3 — oral dose (example numbers)

Same hypothetical drug, 500 mg orally; F = 0.8, Ka = 1.2 h⁻¹, KE = 0.1733 h⁻¹, Vd = 25 L.

- Coefficient F X0 Ka / [Vd (Ka − KE)] = (0.8 × 500 × 1.2)/(25 × 1.0267) = 18.70 mg/L.
- tmax = ln(1.2/0.1733)/(1.2 − 0.1733) = **1.88 h**.
- Cmax = 18.70 × (e^(−0.1733 × 1.88) − e^(−1.2 × 1.88)) = **11.54 mg/L**.

Observed (rounded) data used in the next examples:

| t (h) | 0 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 12 | 16 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C (mg/L) | 0 | 6.89 | 10.09 | 11.33 | 11.53 | 10.61 | 9.20 | 6.60 | 4.68 | 2.34 | 1.17 | 0.29 |

### Worked example 4 — AUC by the trapezoidal rule

Area of each trapezoid = (C1 + C2)/2 × (t2 − t1). Add all segments, then add the tail beyond the last point: Clast/KE.

| Interval (h) | Segment area (mg·h/L) | Cumulative AUC |
| --- | --- | --- |
| 0–0.5 | (0 + 6.89)/2 × 0.5 = 1.72 | 1.72 |
| 0.5–1 | (6.89 + 10.09)/2 × 0.5 = 4.25 | 5.97 |
| 1–1.5 | 5.36 | 11.32 |
| 1.5–2 | 5.72 | 17.04 |
| 2–3 | 11.07 | 28.11 |
| 3–4 | 9.91 | 38.01 |
| 4–6 | 15.80 | 53.81 |
| 6–8 | 11.28 | 65.09 |
| 8–12 | 14.04 | 79.13 |
| 12–16 | 7.02 | 86.15 |
| 16–24 | 5.84 | 91.99 |

- AUC0–24 = **91.99 mg·h/L**
- Tail = C24/KE = 0.29/0.173 = **1.68 mg·h/L**
- AUC0–∞ = **93.67 mg·h/L**

The exact value from the equation is F X0/CL = 400/4.33 = 92.35 mg·h/L. The trapezoidal rule slightly overestimates in the falling (curved) part of the curve; more sampling points reduce the error (the log-trapezoidal rule is better on the falling limb).

**Absolute bioavailability:** F = AUCoral/AUCIV (same dose) = 93.67/115.4 = **0.81** — close to the true 0.80.

### Worked example 5 — Ka by the method of residuals (feathering)

1. Plot log C vs t. Fit the terminal straight line (8–24 h): slope gives KE = 0.174 h⁻¹; back-extrapolated intercept = 18.84 mg/L.
2. Read the extrapolated values (Cext) at early times and subtract the observed values: residual = Cext − Cobs.

| t (h) | Cext (mg/L) | Cobs (mg/L) | Residual (mg/L) |
| --- | --- | --- | --- |
| 0.5 | 17.27 | 6.89 | 10.38 |
| 1 | 15.83 | 10.09 | 5.74 |
| 1.5 | 14.51 | 11.33 | 3.18 |
| 2 | 13.30 | 11.53 | 1.77 |

3. Plot log residual vs t. It is a straight line with slope −Ka/2.303; here **Ka ≈ 1.18 h⁻¹** (true value 1.2).

Condition: Ka should be at least about 3 times KE so that the two phases separate. If the residual line and the terminal line cross at a time greater than zero, that time is the lag time.

### Worked example 6 — Wagner–Nelson method (fraction absorbed)

For a one-compartment drug, the fraction absorbed up to time t is:

FA = (Ct + KE × AUC0–t) / (KE × AUC0–∞)

KE = 0.173 h⁻¹ (terminal slope); KE × AUC0–∞ = 0.173 × 93.67 = 16.20.

| t (h) | Ct | AUC0–t | KE × AUC0–t | Ct + KE·AUC0–t | FA | % unabsorbed |
| --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 6.89 | 1.72 | 0.30 | 7.19 | 0.444 | 55.6 |
| 1 | 10.09 | 5.97 | 1.03 | 11.12 | 0.686 | 31.4 |
| 1.5 | 11.33 | 11.32 | 1.96 | 13.29 | 0.820 | 18.0 |
| 2 | 11.53 | 17.04 | 2.95 | 14.48 | 0.893 | 10.7 |
| 3 | 10.61 | 28.11 | 4.86 | 15.47 | 0.955 | 4.5 |
| 4 | 9.20 | 38.01 | 6.58 | 15.78 | 0.974 | 2.6 |

A plot of ln(% unabsorbed) against time over the first 2 h is nearly straight with slope −Ka, giving Ka of about 1.1 h⁻¹ (true value 1.2 h⁻¹). Later points flatten because of trapezoidal error — a known weakness of using sparse data.

**Wagner–Nelson — merits and limits:** needs only one oral dataset (no IV data); gives FA versus time for level A IVIVC. But it applies only to **one-compartment** drugs (for two-compartment drugs the **Loo–Riegelman** method, which needs IV data, is used), and it is sensitive to errors in KE and AUC.

## 3.7 Methods of elimination — significance and application of the parameters

- **KE and t½** decide how often to dose (interval usually near t½ for drugs with a moderate therapeutic index), how long until steady state (about 5 t½), and the washout period in crossover studies (at least 5 t½).
- **Vd** gives the **loading dose**: DL = Ctarget × Vd.
- **CL** gives the **maintenance dose rate**: dose rate = Css × CL / F.
- **AUC** measures exposure for bioavailability and bioequivalence.
- **Ka and tmax** describe onset; formulation changes alter them.
- **CLR and fe** guide dose reduction in kidney disease; non-renal clearance guides adjustment in liver disease.

## Remember

- First order: constant fraction per unit time, t½ = 0.693/KE independent of dose; zero order: constant amount per unit time.
- Compartment models are kinetic, not anatomical; non-compartmental analysis uses AUC, AUMC and MRT = AUMC/AUC; PBPK models use real organ volumes and blood flows.
- IV bolus: C = C0 e^(−KE t); Vd = X0/C0; AUC = C0/KE; CL = KE × Vd = X0/AUC.
- Infusion: Css = R0/CL; 90% of Css after 3.3 t½ whatever the rate; loading dose = Css × Vd.
- Oral: tmax = ln(Ka/KE)/(Ka − KE); AUC = F X0/CL; Ka by residuals or Wagner–Nelson.
- Trapezoidal rule: sum (C1 + C2)/2 × Δt, then add Clast/KE for AUC0–∞.
- Wagner–Nelson: FA = (Ct + KE·AUC0–t)/(KE·AUC0–∞), one-compartment only.
- Urinary methods: rate (excretion rate vs midpoint time) and sigma-minus (amount remaining to be excreted).
