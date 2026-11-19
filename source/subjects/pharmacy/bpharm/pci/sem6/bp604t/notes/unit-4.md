# Unit 4: Two-compartment model and multiple dosing

Many drugs do not spread through the body at once: they reach the blood and well-perfused organs quickly and the rest of the tissues more slowly. Their plasma curves need a **two-compartment model**. The second part of this unit covers **multiple dosing** — how levels build up with repeated doses, the steady state, and how loading and maintenance doses are worked out. All numbers in the worked examples are **example numbers** for hypothetical drugs.

## 4.1 Why a multicompartment model?

After an IV bolus, the plot of log C against time for some drugs is **not a single straight line**. There is a steep early fall followed by a slower straight fall:

```text
 log C
   │\
   │ \  distribution (α) phase: drug leaves plasma for tissues
   │  \  AND is eliminated
   │   '.
   │     '-._
   │         '--..__   elimination (β) phase: tissues and plasma
   │                '--..__   in equilibrium, slow fall
   └──────────────────────────── t
```

- **Distribution (α) phase:** fast fall — drug moves from the central to the peripheral compartment while also being eliminated.
- **Post-distribution / elimination (β) phase:** slower fall once both compartments are in pseudo-equilibrium.

If such data are wrongly fitted to a one-compartment model, early concentrations, Vd and loading doses are misjudged. Lidocaine, digoxin and theophylline are commonly described by two-compartment kinetics.

## 4.2 The two-compartment open model — IV bolus

```text
              k12
   Dose ─►[ Central (1) ] ──────►[ Peripheral (2) ]
          │ plasma, liver,◄──────│ muscle, fat,
          │ kidney, heart   k21  │ skin, poorly
          │ (Vc, C)              │ perfused tissue
          └── k10 ─► elimination (from central only)
```

- **Central compartment:** blood and highly perfused tissues (lungs, liver, kidneys, heart, brain); drug equilibrates almost instantly.
- **Peripheral compartment:** tissues with low perfusion (muscle, skin, fat); drug enters and leaves slowly.
- k12, k21 = first-order distribution rate constants; k10 = elimination rate constant from the central compartment.

**Plasma equation (biexponential):**

C = A e^(−αt) + B e^(−βt)

α = fast (distribution) hybrid rate constant, β = slow (elimination) hybrid rate constant, with α > β. A and B are the intercepts of the two exponential components.

Relations: α + β = k12 + k21 + k10 and α β = k21 k10.

### Method of residuals (feathering) to get A, α, B, β

1. Plot log C vs t.
2. Draw the straight terminal (β) line through the late points; slope = −β/2.303; back-extrapolated intercept = B.
3. At each early time, residual = Cobserved − B e^(−βt).
4. Plot log residual vs t: straight line with slope −α/2.303 and intercept A.

### Worked example 1 — two-compartment IV bolus (example numbers)

A hypothetical drug, 500 mg IV bolus:

| t (h) | 0.25 | 0.5 | 1 | 1.5 | 2 | 4 | 6 | 8 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C (mg/L) | 37.00 | 27.94 | 17.11 | 11.62 | 8.69 | 4.59 | 3.02 | 2.02 | 0.91 |

**Step 1 — terminal line (4–12 h):** regression of ln C on t gives β = 0.202 h⁻¹ and B = 10.2 mg/L.

**Step 2 — residuals:**

| t (h) | Observed C | B e^(−βt) | Residual |
| --- | --- | --- | --- |
| 0.25 | 37.00 | 9.71 | 27.29 |
| 0.5 | 27.94 | 9.23 | 18.71 |
| 1 | 17.11 | 8.34 | 8.77 |
| 1.5 | 11.62 | 7.54 | 4.08 |
| 2 | 8.69 | 6.82 | 1.87 |

**Step 3 — residual line:** α = 1.53 h⁻¹, A = 40.2 mg/L.

Rounding to A = 40 mg/L, α = 1.5 h⁻¹, B = 10 mg/L, β = 0.2 h⁻¹:

| Parameter | Formula | Value |
| --- | --- | --- |
| C0 | A + B | 50 mg/L |
| k21 | (Aβ + Bα)/(A + B) = (8 + 15)/50 | 0.46 h⁻¹ |
| k10 | αβ / k21 = 0.30/0.46 | 0.652 h⁻¹ |
| k12 | α + β − k21 − k10 | 0.588 h⁻¹ |
| t½ (α) | 0.693/α | 0.46 h |
| t½ (β) — biological half-life | 0.693/β | 3.47 h |
| Vc (central volume) | Dose/C0 = 500/50 | 10 L |
| AUC0–∞ | A/α + B/β = 26.67 + 50 | 76.7 mg·h/L |
| CLT | Dose/AUC = k10 × Vc | 6.52 L/h |
| Vβ (Varea) | CLT/β | 32.6 L |
| Vss | Vc (1 + k12/k21) | 22.8 L |

Note that Vc < Vss < Vβ. Vβ is used with β to describe the body after distribution; Vss is the volume at steady state; Vc gives the initial concentration.

### Significance of the two-compartment model

- Explains why the **early effect** of a bolus can be high and then fall quickly (thiopental, lidocaine — the drug moves into tissues).
- Loading doses must be split or given slowly so that the high early central level does not cause toxicity (lidocaine, digoxin).
- Sampling for monitoring must be done in the β phase (digoxin at least 6 h after a dose).
- Half-life for dosing is t½β, not t½α.

### Two-compartment model — IV infusion and oral (brief)

- **IV infusion:** the level rises to Css = R0/CLT, approached more slowly than predicted from the α phase; a loading dose based on Vc gives a level that falls during distribution, while one based on Vβ may overshoot at first.
- **Oral:** C = L e^(−Ka t) + M e^(−αt) + N e^(−βt) (triexponential); Ka is found by the **Loo–Riegelman** method, which needs IV data.

## 4.3 Kinetics of multiple dosing

Most drugs are given as repeated doses at a fixed **dosing interval (τ)**. If the next dose is given before the previous one is fully eliminated, drug **accumulates** until a **steady state** is reached, where the amount eliminated in one interval equals the dose.

```text
 C │                  _/\   _/\   _/\   Css,max
   │           _/\  /   \ /   \ /   \
   │     _/\  /   \/     V     V      Css,min
   │ /\ /   \/
   │/  V                     plateau (steady state)
   └──────────────────────────────────── t
     τ   2τ  3τ  ...
```

**Principle of superposition:** with linear (first-order) kinetics, the level at any time is the sum of the levels from every earlier dose. This is valid only if the kinetics are linear (not saturable).

**Accumulation depends on** the dosing interval relative to the half-life: the shorter τ compared with t½, the greater the accumulation.

## 4.4 Steady-state drug levels (one-compartment, repeated IV bolus)

Let the fraction remaining after one interval be e^(−KE τ).

| Quantity | Equation |
| --- | --- |
| Accumulation ratio (index) R | R = 1 / (1 − e^(−KE τ)) |
| Maximum level after the nth dose | Cn,max = (X0/Vd) × (1 − e^(−n KE τ)) / (1 − e^(−KE τ)) |
| Steady-state maximum | Css,max = (X0/Vd) / (1 − e^(−KE τ)) |
| Steady-state minimum | Css,min = Css,max × e^(−KE τ) |
| Average steady-state level | Css,av = F X0 / (CLT τ) = F X0 / (KE Vd τ) = AUC (one dose) / τ |
| Fluctuation | Css,max / Css,min = e^(KE τ) |

**Time to reach steady state** depends only on t½: about 50% after 1 t½, 90% after 3.3 t½, about 97% after 5 t½. **The size of the dose and the dosing interval change the steady-state level, but not the time to reach it.**

**For oral (extravascular) doses**, Css,av = F X0/(CL τ) still holds; the peaks and troughs are smaller than with IV bolus because absorption smooths the curve.

## 4.5 Loading and maintenance doses

**Maintenance dose (DM):** the dose given each interval to keep the steady state. From Css,av:

DM = Css,av × CLT × τ / F

**Loading dose (DL):** a larger first dose that reaches the steady-state level at once, instead of waiting 4–5 half-lives.

DL = Css × Vd / F     or, for the same dosing interval,     DL = DM × R = DM / (1 − e^(−KE τ))

If τ = t½, then R = 2 and **the loading dose is twice the maintenance dose** (the classic "double the first dose" rule).

### Worked example 2 — repeated IV bolus (example numbers)

Hypothetical drug: KE = 0.1733 h⁻¹ (t½ = 4 h), Vd = 25 L; 250 mg IV every 8 h.

1. e^(−KE τ) = e^(−0.1733 × 8) = 0.25 (τ = 2 half-lives).
2. R = 1/(1 − 0.25) = **1.33**.
3. First dose: Cmax = 250/25 = 10.0 mg/L; Cmin just before the 2nd dose = 10 × 0.25 = 2.50 mg/L.
4. Peaks build up: 10.0 (dose 1) → 12.50 (dose 2) → 13.13 (dose 3) → 13.32 (dose 5) mg/L.
5. Css,max = 10/(1 − 0.25) = **13.33 mg/L**; Css,min = 13.33 × 0.25 = **3.33 mg/L**.
6. Css,av = 250/(0.1733 × 25 × 8) = **7.22 mg/L**.
7. Loading dose to reach the steady-state peak at once = DM × R = 250 × 1.33 = **333 mg**.
8. Time to about 90% of steady state = 3.3 × 4 = **13.3 h**.
9. To aim for Css,av = 5 mg/L with τ = 8 h: DM = 5 × 4.33 × 8 = **173 mg** every 8 h.

### Worked example 3 — oral maintenance dose (example numbers)

Same drug as a tablet with F = 0.8, 500 mg every 12 h: Css,av = (0.8 × 500)/(4.33 × 12) = **7.70 mg/L**.

## 4.6 Significance of loading and maintenance doses in clinical settings

1. **Rapid effect:** drugs with long half-lives (digoxin, amiodarone, phenytoin, chloroquine) would take days or weeks to reach steady state without a loading dose.
2. **Serious infections and emergencies:** loading doses of antibiotics or antiarrhythmics reach effective levels at once.
3. **Safety:** for drugs with a narrow therapeutic index, a loading dose may be given in divided parts or slowly (to avoid a high early level in the central compartment).
4. **Loading dose depends on Vd; maintenance dose depends on CL.** So in renal failure the maintenance dose is lowered (CL falls), but the loading dose often stays the same (Vd unchanged). In oedema or obesity Vd may change, altering the loading dose.
5. **Choice of dosing interval:** wide therapeutic window → longer τ with larger doses (fewer doses, better adherence); narrow window → shorter τ or controlled-release products to reduce fluctuation.
6. **Therapeutic drug monitoring:** trough levels (just before a dose) at steady state are used to adjust DM; samples should be taken after about 4–5 half-lives.
7. **Missed doses:** knowing t½ tells whether to take the missed dose or wait.

**Dosage regimen design — general steps**

1. Choose a target Css (inside the therapeutic window, between MEC and MSC).
2. Choose τ (often near t½, practical times such as 6, 8, 12 or 24 h).
3. Calculate DM = Css,av × CL × τ / F; round to an available strength.
4. Calculate DL if a fast effect is needed.
5. Check Css,max and Css,min stay inside the window.

## 4.7 Comparison of one- and two-compartment models

| Feature | One-compartment | Two-compartment |
| --- | --- | --- |
| Distribution | Instantaneous | Fast into central, slow into peripheral |
| log C vs t after IV bolus | Single straight line | Biexponential (curved, then straight) |
| Equation | C = C0 e^(−KE t) | C = A e^(−αt) + B e^(−βt) |
| Volume terms | One Vd | Vc, Vβ (Varea), Vss |
| Half-life used for dosing | 0.693/KE | 0.693/β |
| Ka from oral data | Wagner–Nelson | Loo–Riegelman (needs IV data) |

## Remember

- Two-compartment IV bolus: C = A e^(−αt) + B e^(−βt); feathering gives B and β from the terminal line, A and α from residuals.
- k21 = (Aβ + Bα)/(A + B); k10 = αβ/k21; k12 = α + β − k21 − k10; Vc = Dose/(A + B); AUC = A/α + B/β.
- Volumes: Vc < Vss < Vβ.
- Multiple dosing: R = 1/(1 − e^(−KE τ)); Css,max = (X0/Vd)·R; Css,min = Css,max·e^(−KE τ); Css,av = F X0/(CL τ).
- Time to steady state depends only on t½ (about 5 t½); dose and τ change the level, not the time.
- DM = Css,av × CL × τ / F; DL = Css × Vd / F = DM × R; when τ = t½, DL = 2 DM.
- Renal failure lowers maintenance dose (CL), usually not loading dose (Vd).
