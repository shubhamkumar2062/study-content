# Unit 3: Pharmacokinetics — compartmental and non-compartmental analysis

This unit covers the first half of syllabus Unit 3: basic considerations, pharmacokinetic models, the one-compartment model (IV bolus, IV infusion, extravascular), the two-compartment model, and the non-compartmental (statistical moment) approach used in all modern bioavailability work. Nonlinear kinetics and drug interactions, the second half of syllabus Unit 3, are in Unit 4.

**Example drug.** As in the B.Pharm course (BP604T), a hypothetical "Drug X" runs through the worked examples: KE = 0.1733 h⁻¹ (t½ 4 h), Vd = 25 L, CL = 4.33 L/h; 500 mg IV bolus gives C0 = 20 mg/L and AUC = 115.4 mg·h/L; given orally, F = 0.8 and Ka = 1.2 h⁻¹. These are example numbers chosen for clear arithmetic, not values for any real medicine. A second hypothetical drug, "Drug Y", illustrates the two-compartment model.

## 3.1 Basic considerations

**Pharmacokinetics** is the quantitative study of the time course of drug absorption, distribution, metabolism and excretion (ADME). It turns plasma (or urine) concentration–time data into parameters that describe the body's handling of the drug and lets us predict levels for any dose or regimen.

**Key primary parameters** (independent of each other, physiologically meaningful):

| Parameter | Meaning | Unit |
| --- | --- | --- |
| Clearance (CL) | Volume of plasma completely cleared of drug per unit time; CL = rate of elimination / C | L/h |
| Volume of distribution (Vd) | Apparent volume relating amount in body to plasma concentration; X = Vd × C | L |
| Absorption rate constant (Ka) and bioavailability (F) | Rate and extent of entry from an extravascular site | h⁻¹, fraction |

**Secondary parameters** follow from these: KE = CL/Vd, t½ = 0.693 Vd/CL, AUC = F × Dose/CL, Css = F × Dose/(CL × τ).

**Linear (first-order) pharmacokinetics** assumes that the rate of every process is proportional to the amount present. Consequences: t½, CL and Vd do not change with dose; AUC and Css are proportional to dose; principle of superposition applies (multiple-dose profiles can be built by adding single-dose curves). Unit 4 deals with what happens when these assumptions fail.

**Rate processes**

- Zero order: dX/dt = −k0 (constant amount per time; constant-rate infusion, saturated enzymes, osmotic pumps).
- First order: dX/dt = −K X; X = X0 e^(−Kt); ln X falls linearly with slope −K; t½ = 0.693/K.
- Mixed (Michaelis–Menten): rate = Vmax C/(Km + C).

## 3.2 Pharmacokinetic models

| Approach | Idea | Advantages | Limitations |
| --- | --- | --- | --- |
| Compartment models | Body pictured as one or more kinetically homogeneous, well-mixed compartments joined by first-order rate constants | Simple equations; predict levels for new regimens; give rate constants | Compartments have no exact anatomical meaning; model must be assumed; choice affects parameters |
| Physiological (PBPK) models | Real organs with their blood flows, volumes and tissue/plasma partition coefficients | Mechanistic; scale between species, predict special populations and drug interactions | Many parameters; complex software; needs in vitro data |
| Non-compartmental (model-independent) analysis | Statistical moment theory; areas under curves | Few assumptions; standard for BA/BE and regulatory submissions | Gives fewer details about the shape of the curve; assumes linear kinetics for some parameters |
| Population PK | Nonlinear mixed-effects models of sparse data from many patients | Quantifies variability and covariates (weight, renal function) | Specialised software and statistics |

**Compartment model types**

```text
 Mammillary (central + peripheral)        Catenary (in series)
        ┌────┐                          ┌───┐   ┌───┐   ┌───┐
   k12  │ 2  │                          │ 1 │ ⇌ │ 2 │ ⇌ │ 3 │
  ┌────►│    │                          └───┘   └───┘   └───┘
  │ k21 └────┘                          (rarely used in pharmacokinetics)
 ┌┴──┐
 │ 1 │──k10──►  (elimination from the central compartment)
 └───┘
```

"Open" means drug leaves the body (elimination); a closed model would not lose drug.

## 3.3 One-compartment open model: IV bolus

The body behaves as a single well-mixed volume; after injection the drug distributes instantly and is eliminated by first-order kinetics.

X = X0 e^(−KE t)     C = C0 e^(−KE t)     ln C = ln C0 − KE t

- KE from the slope of ln C vs t; t½ = 0.693/KE; Vd = X0/C0; AUC0–∞ = C0/KE; CL = KE × Vd = X0/AUC.
- CL is additive: CLtotal = CLrenal + CLhepatic + others; KE = ke + km.

**Drug X, 500 mg IV bolus (example numbers):** C at 1, 2, 4, 6, 8, 12 h = 16.82, 14.14, 10.00, 7.07, 5.00, 2.50 mg/L. Regression gives KE = 0.1733 h⁻¹, C0 = 20.0 mg/L → t½ 4.0 h, Vd 25 L, AUC 115.4 mg·h/L, CL 4.33 L/h, MRT = 1/KE = 5.77 h.

**Urinary excretion data** (when blood sampling is difficult): rate method ln(ΔXu/Δt) = ln(ke X0) − KE t_mid; sigma-minus method ln(Xu∞ − Xu) = ln Xu∞ − KE t. Renal clearance = ΔXu/Δt ÷ C at the midpoint = fe × CL.

## 3.4 One-compartment open model: IV infusion

Constant rate R0 (zero-order input), first-order output:

C = (R0/CL)(1 − e^(−KE t))     Css = R0/CL = R0/(KE Vd)

- Time to steady state depends only on t½: 50% in 1, 90% in 3.32, 99% in 6.64 half-lives.
- Loading dose to reach Css at once: DL = Css × Vd.
- After stopping at time T: C = CT e^(−KE t′).
- Clearance can be estimated from a single steady-state level: CL = R0/Css.

**Drug X (example numbers):** R0 = 20 mg/h → Css = 20/4.33 = **4.62 mg/L**; at 8 h C = 4.62 × 0.75 = 3.46 mg/L; time to 90% of Css = 13.3 h; loading dose for 4.62 mg/L = 115 mg.

## 3.5 One-compartment open model: extravascular (oral, IM)

First-order absorption (Ka) into one compartment with first-order elimination:

C = [F X0 Ka / (Vd (Ka − KE))] × (e^(−KE t) − e^(−Ka t))

tmax = ln(Ka/KE)/(Ka − KE)     Cmax = (F X0/Vd) e^(−KE tmax)     AUC = F X0/CL

**Drug X, 500 mg orally (example numbers):** coefficient 18.70 mg/L, tmax = **1.88 h**, Cmax = **11.54 mg/L**, AUC (exact) = 400/4.33 = **92.3 mg·h/L**.

| t (h) | 0 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 12 | 16 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C (mg/L) | 0 | 6.89 | 10.09 | 11.33 | 11.53 | 10.61 | 9.20 | 6.60 | 4.68 | 2.34 | 1.17 | 0.29 |

### Estimating Ka

1. **Method of residuals (feathering):** fit the terminal line (gives KE and the intercept), subtract observed values from the extrapolated line at early times, and the log of the residuals against time has slope −Ka. Gives Ka ≈ 1.2 h⁻¹ for these data (worked in full in BP604T).
2. **Wagner–Nelson method** (one-compartment drugs): the amount absorbed up to time t is the amount in the body plus the amount eliminated:

   FA(t) = [Ct + KE × AUC0–t] / [KE × AUC0–∞]

   A plot of ln(1 − FA) vs t is a straight line with slope −Ka if absorption is first order. FA vs time shows the whole absorption profile even when absorption is not first order (zero-order, erratic, or with lag), which is why it is used for IVIVC.
3. **Loo–Riegelman method:** the two-compartment version; needs IV data to know k12, k21 and k10.
4. **Numerical deconvolution:** uses the IV (unit impulse) response to recover the input rate without assuming a model.

### Worked example 1 — Wagner–Nelson for Drug X (example numbers)

AUC by the linear trapezoidal rule: AUC0–24 = 91.99; tail = 0.29/0.1733 = 1.67; AUC0–∞ = 93.67 mg·h/L; KE × AUC0–∞ = 16.23 mg/L.

| t (h) | C | AUC0–t | KE·AUC0–t | C + KE·AUC0–t | FA | 1 − FA |
| --- | --- | --- | --- | --- | --- | --- |
| 0.5 | 6.89 | 1.72 | 0.30 | 7.19 | 0.443 | 0.557 |
| 1 | 10.09 | 5.97 | 1.03 | 11.12 | 0.685 | 0.315 |
| 1.5 | 11.33 | 11.32 | 1.96 | 13.29 | 0.819 | 0.181 |
| 2 | 11.53 | 17.04 | 2.95 | 14.48 | 0.892 | 0.108 |
| 3 | 10.61 | 28.11 | 4.87 | 15.48 | 0.954 | 0.046 |
| 4 | 9.20 | 38.01 | 6.59 | 15.79 | 0.973 | 0.027 |
| 8 | 4.68 | 65.09 | 11.28 | 15.96 | 0.983 | 0.017 |

Regression of ln(1 − FA) on t from 0.5 to 2 h gives slope −1.10 h⁻¹, so **Ka ≈ 1.1 h⁻¹**. The true value is 1.2 h⁻¹; the small underestimate comes from the linear trapezoidal rule, which overestimates the areas of the curved falling limb. Denser early sampling or the log-trapezoidal rule on the falling limb reduces this bias. The true fraction absorbed by 1 h is 1 − e^(−1.2) = 0.699 against 0.685 found.

### Flip-flop and lag time

- If Ka is smaller than KE (common with slow-release products), the terminal slope reflects Ka, not KE. Only an IV or immediate-release study can tell which is which. Example: an extended-release form of Drug X releasing with an apparent Ka of 0.05 h⁻¹ would show a terminal half-life of 0.693/0.05 = 13.9 h although the true elimination half-life is 4 h.
- **Lag time (tlag):** delay before absorption begins (gastric emptying, coat dissolution). Include it as (t − tlag) in the equation; it appears where the terminal and residual lines intersect above zero.

## 3.6 Multiple dosing (brief)

With dose X0 every τ, the drug accumulates until intake equals elimination over each interval.

- Accumulation ratio R = 1/(1 − e^(−KE τ)).
- Css,max = (X0/Vd)/(1 − e^(−KE τ)) for IV bolus; Css,min = Css,max × e^(−KE τ).
- Average steady-state concentration Css,av = F X0/(CL × τ) = AUC (single dose)/τ; independent of the model.
- Loading dose DL = X0 × R (IV).

**Drug X, 250 mg IV every 8 h (example numbers):** e^(−KE τ) = 0.25, R = 1.33, Css,max = 13.3 mg/L, Css,min = 3.33 mg/L, Css,av = 250/(4.33 × 8) = **7.22 mg/L**.

## 3.7 Multi-compartment model: two-compartment open model (in brief)

Many drugs show a fast fall (distribution, α phase) followed by a slower fall (elimination, β phase) after an IV bolus, because they distribute into less well-perfused tissues over time.

```text
           k12
   ┌──────────────────┐
   │                  ▼
 ┌─────────┐       ┌───────────┐
 │ Central │ ◄──── │ Peripheral│
 │  (1)    │  k21  │   (2)     │
 └────┬────┘       └───────────┘
      │ k10
      ▼
  elimination

 log C │\
       │ \  α phase (distribution + elimination)
       │  \___
       │      ‾‾‾‾‾‾‾‾───────── β phase (elimination)
       └───────────────────────── t
```

**IV bolus equation:** C = A e^(−αt) + B e^(−βt), with α > β.

α + β = k12 + k21 + k10     α × β = k21 × k10

**Parameters from A, α, B, β**

- k21 = (Aβ + Bα)/(A + B)
- k10 = αβ/k21
- k12 = α + β − k21 − k10
- C0 = A + B; V1 (central volume) = Dose/C0
- AUC = A/α + B/β; CL = Dose/AUC = k10 × V1
- Vss = V1 (1 + k12/k21) = CL × MRT (volume at steady state)
- Vβ (Varea) = CL/β, always larger than Vss
- t½β = 0.693/β is the clinically relevant half-life

### Worked example 2 — Drug Y, 100 mg IV bolus (example numbers)

| t (h) | 0.25 | 0.5 | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C (mg/L) | 6.755 | 4.753 | 2.720 | 1.880 | 1.487 | 1.117 | 0.901 | 0.602 | 0.404 | 0.181 |

1. **Terminal phase (4–12 h):** regression of ln C on t gives β = 0.200 h⁻¹ and intercept B = 2.01 mg/L.
2. **Residuals:** at 0.25 h the extrapolated line gives 1.910, residual = 6.755 − 1.910 = 4.845; at 0.5 h 4.753 − 1.816 = 2.937; at 1 h 2.720 − 1.643 = 1.077; at 1.5 h 1.880 − 1.486 = 0.394.
3. Regression of ln(residual) on t gives α = 2.01 h⁻¹ and A = 8.01 mg/L (true values A = 8, α = 2.0, B = 2, β = 0.2).

Using A = 8, α = 2.0, B = 2, β = 0.2:

| Parameter | Calculation | Value |
| --- | --- | --- |
| k21 | (8 × 0.2 + 2 × 2.0)/10 | 0.56 h⁻¹ |
| k10 | (2.0 × 0.2)/0.56 | 0.714 h⁻¹ |
| k12 | 2.2 − 0.56 − 0.714 | 0.926 h⁻¹ |
| V1 | 100/10 | 10 L |
| AUC | 8/2 + 2/0.2 | 14 mg·h/L |
| CL | 100/14 (check: k10 × V1 = 7.14) | 7.14 L/h |
| Vss | 10 × (1 + 0.926/0.56) | 26.5 L |
| Vβ | 7.14/0.2 | 35.7 L |
| t½α, t½β | 0.693/α, 0.693/β | 0.35 h, 3.47 h |

Note the three volumes: V1 (10 L) < Vss (26.5 L) < Vβ (35.7 L). Using V1 to calculate a loading dose risks toxic early levels in the central compartment for drugs acting on the heart or brain; using Vβ overestimates the amount in the body at steady state.

**IV infusion and oral dosing** in the two-compartment model follow the same principles (three exponentials for oral data). If distribution is fast compared with absorption, oral data may look one-compartmental even when IV data do not.

**Clinical relevance:** drugs whose effect site is in the peripheral compartment (for example digoxin, whose cardiac effect follows tissue levels) should be sampled for therapeutic monitoring only after distribution is complete.

## 3.8 Non-compartmental analysis (statistical moment theory)

The concentration–time curve is treated as a statistical distribution of residence times of drug molecules in the body. No compartment structure is assumed; only linear kinetics in the terminal phase.

**Moments**

- Zero moment: AUC = ∫ C dt
- First moment: AUMC = ∫ t × C dt
- Mean residence time: MRT = AUMC/AUC (average time a molecule stays in the body)

**Calculating areas**

- **Linear trapezoidal rule:** segment = (C1 + C2)/2 × Δt. Good on the rising limb; overestimates on the falling curved limb.
- **Log-trapezoidal rule:** segment = (C1 − C2) Δt / ln(C1/C2), for falling concentrations. "Linear-up, log-down" is the usual choice.
- **Extrapolation to infinity:** AUCtail = Clast/λz; AUMCtail = Clast × tlast/λz + Clast/λz², where λz is the terminal slope from at least three points. The extrapolated part should normally be less than 20% of AUC0–∞ in BE studies.

**Derived parameters**

| Parameter | Formula |
| --- | --- |
| CL (IV) | Dose/AUC |
| CL/F (oral) | Dose/AUC |
| Vz (Varea) | Dose/(λz × AUC) |
| Vss (IV bolus) | CL × MRT = Dose × AUMC/AUC² |
| MRT (IV bolus) | 1/KE for a one-compartment drug |
| Mean absorption time | MAT = MRToral − MRTiv; for first-order absorption MAT = 1/Ka |
| Mean dissolution time in vivo | MDTvivo = MRTsolid − MRTsolution |
| MRT after IV infusion | MRTinf = MRTobserved − T/2 (T = infusion time) |
| t½ (terminal) | 0.693/λz |

### Worked example 3 — NCA of Drug X oral data (example numbers)

| t (h) | C × t (mg·h/L) | Cumulative AUMC |
| --- | --- | --- |
| 0.5 | 3.44 | 0.86 |
| 1 | 10.09 | 4.25 |
| 1.5 | 17.00 | 11.02 |
| 2 | 23.06 | 21.03 |
| 3 | 31.83 | 48.48 |
| 4 | 36.80 | 82.79 |
| 6 | 39.60 | 159.19 |
| 8 | 37.44 | 236.23 |
| 12 | 28.08 | 367.27 |
| 16 | 18.72 | 460.87 |
| 24 | 6.96 | 563.59 |

- AUMC tail = 0.29 × 24/0.1733 + 0.29/0.1733² = 40.16 + 9.66 = 49.82; AUMC0–∞ = **613.4 mg·h²/L**.
- AUC0–∞ (linear trapezoidal) = **93.67 mg·h/L** (extrapolated part 1.8%).
- MRToral = 613.4/93.67 = **6.55 h** (theory: 1/KE + 1/Ka = 5.77 + 0.83 = 6.60 h).
- MAT = 6.55 − 5.77 = **0.78 h** → Ka ≈ 1/0.78 = **1.28 h⁻¹** (true 1.2).
- CL/F = 500/93.67 = **5.34 L/h**; Vz/F = 5.34/0.1733 = **30.8 L**.
- With the IV AUC of 115.4, F = 93.67/115.4 = **0.81** (true 0.80).

The linear-up/log-down rule gives AUC0–∞ = 91.8 here, a little below the exact 92.3: the log rule assumes exponential decline between 2 and 4 h, where the curve is still bending. No area rule is perfect; good sampling design matters more.

**Advantages of NCA:** model-free, simple, reproducible between analysts, required for bioequivalence (AUC, Cmax, tmax). **Limitations:** needs adequate sampling of the terminal phase, assumes linearity for CL and Vss, gives less insight into distribution, and higher moments (variance of residence time) are unreliable.

## 3.9 Choosing an approach

```text
 Rich data, need regimen prediction ─► compartment model (1- or 2-compartment)
 BA/BE, regulatory summary         ─► non-compartmental analysis
 Sparse clinical data, covariates  ─► population (mixed-effects) modelling
 Interaction or special-population prediction from in vitro data ─► PBPK
```

## Remember

- Primary parameters: CL, Vd, F, Ka; KE = CL/Vd; t½ = 0.693 Vd/CL.
- IV bolus: C = C0 e^(−KE t); Vd = X0/C0; AUC = C0/KE; CL = X0/AUC.
- Infusion: Css = R0/CL; 90% of Css in 3.32 t½; loading dose = Css × Vd.
- Oral: tmax = ln(Ka/KE)/(Ka − KE); AUC = F X0/CL; flip-flop when Ka < KE.
- Wagner–Nelson: FA = (C + KE·AUC0–t)/(KE·AUC0–∞); Loo–Riegelman for two-compartment drugs.
- Two-compartment: C = A e^(−αt) + B e^(−βt); k21 = (Aβ + Bα)/(A + B); k10 = αβ/k21; V1 < Vss < Vβ.
- NCA: MRT = AUMC/AUC; MAT = MRToral − MRTiv = 1/Ka; Vss = CL × MRT; AUC tail = Clast/λz.
- Drug X: KE 0.1733 h⁻¹, t½ 4 h, Vd 25 L, CL 4.33 L/h, AUC(500 mg IV) 115.4, oral AUC 92.3, F 0.8, Ka 1.2 h⁻¹, MRTiv 5.77 h.
