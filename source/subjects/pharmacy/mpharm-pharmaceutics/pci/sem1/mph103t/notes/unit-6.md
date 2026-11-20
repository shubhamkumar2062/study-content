# Unit 6: Consolidation, diffusion, dissolution and pharmacokinetic parameters; statistics

Syllabus item 5: study of consolidation parameters; diffusion parameters, dissolution parameters and pharmacokinetic parameters; Heckel plots; similarity factors f2 and f1; Higuchi and Peppas plots; linearity; concept of significance; standard deviation; chi-square test; Student's t-test; ANOVA test. This is the most numerical unit — every worked example below is a type examiners like.

## 6.1 Consolidation (compression) parameters

These equations describe how relative density or volume of a powder bed changes with applied pressure, so that materials can be compared and classified.

### Heckel equation

Heckel treated densification as a first-order process in which the rate of change of density with pressure is proportional to the remaining porosity:

dD/dP = K(1 − D)

Integrating: **ln[1/(1 − D)] = KP + A**

where D = relative density of the compact at pressure P (D = 1 − ε), K = slope (MPa⁻¹), A = intercept.

- **Mean yield pressure Py = 1/K.** Low Py means the material deforms plastically at low pressure (soft, plastic); high Py means hard or brittle.
- **DA = 1 − e^(−A)** — relative density from the intercept, reflecting densification at low pressure.
- **D0** = relative density of the powder at zero pressure (loose packing in the die).
- **DB = DA − D0** — densification due to particle rearrangement and fragmentation in the early stage.

**"In-die" versus "out-of-die" (zero-pressure) Heckel plots:** in-die data are recorded during compression from punch displacement (include elastic deformation, many points from one tablet); out-of-die data use dimensions of ejected tablets (after elastic recovery). They give different Py values, so the method must be stated.

**Classification of materials from Heckel plots (Hersey and Rees):**

| Type | Behaviour | Heckel plots for different particle size fractions |
| --- | --- | --- |
| A | Plastic deformation after rearrangement (e.g. sodium chloride) | Parallel linear plots; initial packing (size-dependent) decides the position |
| B | Fragmentation (e.g. lactose, dicalcium phosphate) | Curved early, then converge into one line at higher pressure as particles fragment to a common size |
| C | No rearrangement stage, plastic deformation from the start (e.g. some fats/waxes) | Linear from the start, size-independent |

**Worked example (Heckel).** A powder was compressed and the relative density recorded:

| P (MPa) | D | 1 − D | ln[1/(1 − D)] |
| --- | --- | --- | --- |
| 50 | 0.713 | 0.287 | 1.248 |
| 100 | 0.817 | 0.183 | 1.698 |
| 150 | 0.884 | 0.116 | 2.154 |
| 200 | 0.926 | 0.074 | 2.604 |
| 250 | 0.953 | 0.047 | 3.058 |

Linear regression of ln[1/(1 − D)] on P gives slope K = 0.00905 MPa⁻¹ and intercept A = 0.795 (r = 0.99999).

- Py = 1/K = **about 110 MPa** (moderately plastic behaviour).
- DA = 1 − e^(−0.795) = **0.548**. If the loose powder had D0 = 0.40, then DB = 0.548 − 0.40 = **0.148**, the densification from rearrangement and fragmentation.

**Limitations:** the plot is often curved at low pressure (rearrangement) and at very high pressure (approaching zero porosity, where errors in true density magnify); results depend on true density accuracy, punch speed (strain rate), die size, lubrication and whether in-die or out-of-die data are used.

### Kawakita equation

Kawakita described the degree of volume reduction C as a function of pressure:

C = (V0 − V)/V0 = abP/(1 + bP)

Linear form: **P/C = P/a + 1/(ab)**

- **a** = maximum (limiting) volume reduction at infinite pressure = initial porosity of the bed (related to flowability/packing; a lower a means better initial packing).
- **b** is related to the resistance to compression (plasticity); **1/b (= Pk)** is the pressure needed to reach half of the maximum volume reduction — a low 1/b means soft, easily deformed particles.
- Works best at low pressures and for tapping/low-pressure compression of powders and granules (packing and cohesion studies); complements Heckel, which suits higher pressures.

**Worked example (Kawakita).** Volume reductions C at 50, 100, 150, 200 and 250 MPa were 0.240, 0.300, 0.327, 0.343 and 0.353. P/C = 208.3, 333.3, 458.7, 583.1 and 708.2. Regression of P/C on P: slope = 2.499, intercept = 83.48 (r = 0.999999).

a = 1/slope = **0.400**; ab = 1/intercept → b = slope/intercept = **0.030 MPa⁻¹**; 1/b = **33.4 MPa**.

### Other consolidation models (brief)

- **Cooper–Eaton equation:** describes compaction as two processes — filling of voids of the same size as particles (rearrangement) and filling of smaller voids by deformation/fragmentation; two coefficients give the share of each.
- **Walker equation:** relative volume falls linearly with log pressure; the slope (compressibility coefficient) compares materials.
- **Gurnham, Shapiro, Leuenberger equations:** tensile strength or density as functions of pressure; Leuenberger's model links tablet strength to relative density and pressure (compactibility and compression susceptibility).
- **Energy-based parameters:** net work of compaction and plasticity factor (Unit 5); elastic recovery.

## 6.2 Diffusion parameters

**Diffusion** is the net movement of molecules from a region of higher to a region of lower concentration (chemical potential) by random molecular motion. It controls drug release from reservoir and matrix systems, transdermal permeation and absorption across membranes.

**Fick's first law (steady state):** J = −D(dC/dx), where J = flux (amount per unit area per time), D = diffusion coefficient (cm²/s), dC/dx = concentration gradient.

**Across a membrane:** J = D·K·ΔC/h = P·ΔC, where K = partition coefficient between membrane and donor, h = membrane thickness, and **P = DK/h = permeability coefficient** (cm/s or cm/h). Under sink conditions ΔC ≈ Cd (donor concentration).

**Fick's second law (non-steady state):** ∂C/∂t = D(∂²C/∂x²) — how concentration changes with time at each position; the basis of release equations (Higuchi, Crank solutions).

**Lag-time method (time-lag):** a plot of cumulative amount permeated per unit area against time becomes linear after an initial lag. Extrapolating the linear part to the time axis gives the **lag time tL = h²/(6D)**, so D = h²/(6tL). The slope of the linear part is the steady-state flux Jss.

**Worked example (diffusion):** membrane thickness 100 µm (0.01 cm), lag time 2 h (7,200 s): D = (0.01)²/(6 × 7,200) = **2.3 × 10⁻⁹ cm²/s**. Steady-state flux 12 µg/cm²/h from a donor of 1,000 µg/ml: P = J/Cd = 12/1,000 = **0.012 cm/h**.

**Other diffusion parameters and factors:**

- **Stokes–Einstein equation:** D = kT/(6πηr) — D rises with temperature and falls with viscosity and molecular radius.
- **Enhancement ratio** (transdermal) = flux with enhancer ÷ flux without.
- **Partition coefficient and log P**, membrane thickness and tortuosity (porous membranes: effective D = Dε/τ, where ε = porosity and τ = tortuosity).
- **Apparatus:** Franz diffusion cell (vertical, donor over receptor, membrane between, receptor stirred at 32 °C for skin studies), side-by-side (Valia–Chien) cells, Caco-2 monolayers for intestinal permeability (apparent permeability Papp = (dQ/dt)/(A·C0)).

## 6.3 Dissolution parameters and release kinetics

### Noyes–Whitney and Hixson–Crowell

**Noyes–Whitney (modified by Nernst and Brunner):** dC/dt = DA(Cs − C)/(Vh), where A = surface area, h = diffusion layer thickness, Cs = saturation solubility, V = volume. Under sink conditions (C < about 10–20% of Cs) the rate ≈ DACs/(Vh).

**Hixson–Crowell cube-root law** (dissolving particles that shrink uniformly): W0^(1/3) − Wt^(1/3) = κt.

### Release models

| Model | Equation | Plot for linearity | Typical system |
| --- | --- | --- | --- |
| Zero order | Qt = Q0 + k0t | Cumulative % released vs t | Osmotic pumps, reservoir systems with constant flux |
| First order | log(100 − Qt) = log 100 − k1t/2.303 | log % remaining vs t | Immediate-release, porous matrices with soluble drugs |
| Higuchi | Qt = kH√t | Cumulative % released vs √t | Diffusion from insoluble matrices (planar, drug load above solubility) |
| Hixson–Crowell | W0^(1/3) − Wt^(1/3) = κt | Cube root of % remaining vs t | Erosion/dissolution with changing surface area |
| Korsmeyer–Peppas (power law) | Mt/M∞ = ktⁿ | log(Mt/M∞) vs log t (first 60% only) | Polymeric (swellable) systems — the exponent n gives the mechanism |
| Weibull | m = 1 − exp[−(t − Ti)^b/a] | log[−ln(1 − m)] vs log t | Empirical fit of any profile; b describes the curve shape |
| Baker–Lonsdale | (3/2)[1 − (1 − Mt/M∞)^(2/3)] − Mt/M∞ = kt | — | Spherical matrices (microspheres) |

**Peppas release exponent n:**

| Geometry | Fickian diffusion | Anomalous (non-Fickian) transport | Case II (zero-order, relaxation) |
| --- | --- | --- | --- |
| Thin film / slab | 0.5 | 0.5 < n < 1.0 | 1.0 |
| Cylinder | 0.45 | 0.45 < n < 0.89 | 0.89 |
| Sphere | 0.43 | 0.43 < n < 0.85 | 0.85 |

n above the case II value indicates "super case II" transport (very rapid relaxation or erosion).

**Worked example (model fitting).** Cumulative release from a matrix tablet: 18, 26, 37, 45 and 52% at 1, 2, 4, 6 and 8 h.

| Model | Result |
| --- | --- |
| Zero order (Q vs t) | r² = 0.980 |
| First order (log % remaining vs t) | r² = 0.995, k1 = 0.075 h⁻¹ |
| Higuchi (Q vs √t) | r² = 0.9998, kH = 18.5 %/h^½ |
| Korsmeyer–Peppas (log Q vs log t) | r² = 0.9997, n = 0.51, k = 18.1 |

The Higuchi model fits best, showing diffusion-controlled release. For a cylindrical tablet n = 0.51 lies just above 0.45, so release is mainly diffusional with a small contribution from polymer relaxation (anomalous transport). Comparing models by r² alone is crude; adjusted r² and the Akaike information criterion (AIC) are better when models have different numbers of parameters.

### Model-independent dissolution parameters

- **t50%, t90%, Q-value at a time** (for example % released at 30 min).
- **Dissolution efficiency (DE):** area under the dissolution curve up to time t, as a percentage of the rectangle representing 100% dissolution over the same time: DE = (∫0→t y dt)/(y100 × t) × 100.
- **Mean dissolution time (MDT):** MDT = Σ(t̂j × ΔMj)/ΣΔMj, where t̂j is the midpoint of each interval and ΔMj the amount released in it. A larger MDT means slower release.
- **Mean dissolution rate (MDR)** and **difference/similarity factors f1 and f2** (below).

**Worked example (DE and MDT):** release (%) at 0, 10, 15, 20, 30 and 45 min = 0, 30, 48, 62, 80, 92.
Area by trapezoids = 150 + 195 + 275 + 710 + 1,290 = 2,620 %·min; DE45 = 2,620/(100 × 45) × 100 = **58.2%**.
MDT = (5 × 30 + 12.5 × 18 + 17.5 × 14 + 25 × 18 + 37.5 × 12)/92 = 1,520/92 = **16.5 min**.

### Similarity factor f2 and difference factor f1 (Moore and Flanner)

**f1 = {Σ|Rt − Tt| / ΣRt} × 100** — percent difference between the curves (0 when identical; 0–15 taken as similar).

**f2 = 50 × log{[1 + (1/n)Σ(Rt − Tt)²]^(−0.5) × 100}** — a logarithmic transformation of the mean squared difference. f2 = 100 when the curves are identical; **f2 between 50 and 100** means similar. An average difference of 10% at every point gives f2 ≈ 50; 15% gives about 41.

**Conditions for using f2 (regulatory guidance, US FDA / EMA / CDSCO practice):**

1. At least 12 units of each product, same test conditions, same time points.
2. At least three time points (zero excluded).
3. Only **one** measurement after 85% dissolution of both products.
4. Coefficient of variation not more than 20% at the earlier points (for example up to 10 min) and not more than 10% at later points; otherwise use model-independent multivariate or bootstrap methods.
5. If both dissolve 85% or more within 15 min (very rapidly dissolving), f2 comparison is not needed.

**Uses:** comparing test and reference products (generics), pre- and post-change batches (SUPAC-type changes, scale-up), biowaivers for lower strengths, and stability comparisons.

**Worked example (f1 and f2):**

| Time (min) | Reference R (%) | Test T (%) | R − T | (R − T)² |
| --- | --- | --- | --- | --- |
| 10 | 30 | 25 | 5 | 25 |
| 15 | 48 | 40 | 8 | 64 |
| 20 | 62 | 57 | 5 | 25 |
| 30 | 80 | 76 | 4 | 16 |
| 45 | 92 | 90 | 2 | 4 |
| Sum | 312 | | 24 | 134 |

f1 = 24/312 × 100 = **7.7** (within 0–15).
Mean squared difference = 134/5 = 26.8; f2 = 50 × log[100/√(1 + 26.8)] = 50 × log(18.97) = **63.9** (between 50 and 100) → the profiles are **similar**. Only the 45-min point lies above 85% for both products, so the rule is met.

## 6.4 Pharmacokinetic parameters

Pharmacokinetic (PK) parameters describe what the body does to the drug; for formulation scientists they are the final test of a dosage form (bioavailability and bioequivalence).

| Parameter | Meaning | How obtained |
| --- | --- | --- |
| **Cmax** | Peak plasma concentration | Directly from the observed data |
| **Tmax** | Time to reach Cmax (reflects absorption rate) | Directly from data |
| **AUC0–t** | Area under the plasma concentration–time curve to the last measured time | Linear (or linear-up/log-down) trapezoidal rule |
| **AUC0–∞** | Total exposure | AUC0–t + Clast/ke |
| **ke** (elimination rate constant) | Fraction eliminated per unit time | −slope of ln C vs t over the terminal phase |
| **t½** | Elimination half-life | 0.693/ke |
| **ka** | Absorption rate constant | Method of residuals (feathering) or Wagner–Nelson |
| **Vd** | Apparent volume of distribution | Dose/C0 (IV bolus) or CL/ke |
| **CL** | Clearance | F × dose/AUC0–∞; CL = ke × Vd |
| **MRT** | Mean residence time | AUMC0–∞/AUC0–∞ |
| **F** | Absolute bioavailability | (AUCoral × doseIV)/(AUCIV × doseoral) |
| **Frel** | Relative bioavailability | AUCtest/AUCreference (same dose) × 100 |

**Worked example (PK from plasma data after an oral dose):**

| t (h) | 0 | 0.5 | 1 | 2 | 3 | 4 | 6 | 8 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C (µg/ml) | 0 | 4.2 | 6.8 | 8.1 | 7.4 | 6.3 | 4.6 | 3.3 | 1.7 |

- Cmax = **8.1 µg/ml** at Tmax = **2 h**.
- AUC0–12 by the trapezoidal rule = **54.65 µg·h/ml**.
- Terminal slope from ln C at 6, 8 and 12 h = −0.166 h⁻¹ → ke = **0.166 h⁻¹**, t½ = 0.693/0.166 = **4.2 h**.
- AUC0–∞ = 54.65 + 1.7/0.166 = **64.9 µg·h/ml**; the extrapolated part is 15.8% (regulators expect it to be under about 20% for a reliable estimate).
- AUMC0–∞ = 442.3 µg·h²/ml → MRT = 442.3/64.9 = **6.8 h**.
- A test formulation given at the same dose gave AUC0–∞ = 61.0 µg·h/ml → relative bioavailability = 61.0/64.9 × 100 = **94%**.

**Bioequivalence (outline):** two products are bioequivalent when the **90% confidence intervals** for the ratios (test/reference) of the geometric means of AUC and Cmax, after log transformation, lie within **80.00–125.00%**. Usually a randomised, two-period, two-sequence crossover study in healthy volunteers with an adequate washout (at least five half-lives), analysed by ANOVA on log-transformed data (two one-sided tests procedure). Narrower limits may apply to narrow-therapeutic-index drugs.

**In vitro–in vivo correlation (IVIVC):** **Level A** — point-to-point relation between in vitro dissolution and in vivo absorption (fraction absorbed from deconvolution, for example Wagner–Nelson); the most useful, can support biowaivers. **Level B** — compares mean in vitro dissolution time with mean in vivo residence or absorption time (uses all data but not point-to-point). **Level C** — single-point relation (for example t50% vs Cmax or AUC); **multiple Level C** uses several time points.

## 6.5 Statistics for pharmaceutical data

### Descriptive statistics

- **Mean** x̄ = Σx/n.
- **Standard deviation** s = √[Σ(x − x̄)²/(n − 1)] — spread of individual values (n − 1 because x̄ is estimated from the same data).
- **Relative standard deviation (RSD, coefficient of variation)** = s/x̄ × 100.
- **Standard error of the mean** = s/√n.

**Worked example:** ten tablet weights (mg): 248, 252, 250, 247, 253, 251, 249, 250, 254, 246. Mean = **250 mg**, SD = **2.58 mg**, RSD = **1.03%**.

### Linearity and correlation

Linear regression y = a + bx by least squares: b = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)², a = ȳ − bx̄.
Correlation coefficient r = Σ(x − x̄)(y − ȳ)/√[Σ(x − x̄)²·Σ(y − ȳ)²]; r² (coefficient of determination) is the fraction of variation in y explained by x.

**Worked example (calibration linearity):** concentration 2, 4, 6, 8, 10 µg/ml; absorbance 0.112, 0.221, 0.335, 0.442, 0.556. Slope = **0.0555 ml/µg**, intercept = 0.0005, r = **0.99996** (r² = 0.9999). Analytical method validation (ICH Q2(R2)) reports slope, intercept, r and residual plots over the range; a high r alone does not prove linearity — look at residuals.

### Concept of significance (hypothesis testing)

- **Null hypothesis (H0):** no real difference (differences are due to chance). **Alternative (H1):** a real difference exists.
- **Level of significance (α):** the risk of rejecting H0 when it is true, usually 0.05 (5%).
- **p-value:** probability of getting a result at least as extreme as observed if H0 were true; p < α → reject H0 ("statistically significant").
- **Type I error (α):** false positive — concluding a difference that is not real. **Type II error (β):** false negative — missing a real difference; **power = 1 − β** (often 80–90% in study design).
- **Degrees of freedom**, one-tailed versus two-tailed tests, **confidence interval** (range likely to contain the true value; a 95% CI for a difference that excludes zero corresponds to p < 0.05).
- **Parametric** tests (t, ANOVA) assume normal distribution and equal variances; **non-parametric** alternatives: Mann–Whitney U, Wilcoxon, Kruskal–Wallis.

### Student's t-test

Used to compare means: one-sample (sample vs a known value), **unpaired (independent) two-sample**, and **paired** (same subjects before and after).

Unpaired with pooled variance: t = (x̄1 − x̄2) / [sp√(1/n1 + 1/n2)], where sp² = [(n1 − 1)s1² + (n2 − 1)s2²]/(n1 + n2 − 2); df = n1 + n2 − 2.

**Worked example:** hardness (kg) of tablets with low lubricant level: 6.2, 6.5, 6.0, 6.4, 6.3, 6.6 (mean 6.333); high lubricant level: 5.6, 5.9, 5.5, 5.8, 6.0, 5.7 (mean 5.750). Variances 0.0467 and 0.0350; sp = 0.202; t = 0.583/(0.202 × √(1/3)) = **5.00** with df = 10. Critical two-tailed t (0.05, 10) = 2.228 → t exceeds it → **significant**: the higher lubricant level lowers hardness.

### Chi-square (χ²) test

Used for **frequency (count) data**: goodness of fit, and test of independence in contingency tables.

χ² = Σ (O − E)²/E, where O = observed and E = expected frequency (E = row total × column total ÷ grand total); df = (rows − 1)(columns − 1).

**Worked example:** defective tablets from two machines (200 inspected each): machine 1 — 12 defective, 188 acceptable; machine 2 — 24 defective, 176 acceptable. Expected defective in each = 18, acceptable 182.
χ² = (12 − 18)²/18 + (188 − 182)²/182 + (24 − 18)²/18 + (176 − 182)²/182 = 2 + 0.198 + 2 + 0.198 = **4.40**; df = 1; critical value 3.841 → **significant**: defect rate depends on the machine. (With small expected counts, Yates' continuity correction or Fisher's exact test is used.)

### Analysis of variance (ANOVA)

Compares **three or more means** in one test (repeated t-tests inflate the type I error). Total variation is split into **between-group** and **within-group (error)** variation; F = MS(between)/MS(within).

**Worked example:** % dissolved at 30 min for tablets with three binders (n = 4 each): binder 1 — 78, 80, 76, 82 (mean 79); binder 2 — 85, 88, 86, 89 (mean 87); binder 3 — 80, 79, 83, 82 (mean 81); grand mean 82.33.

| Source | SS | df | MS | F |
| --- | --- | --- | --- | --- |
| Between binders | 138.67 | 2 | 69.33 | **15.6** |
| Within (error) | 40.00 | 9 | 4.44 | |
| Total | 178.67 | 11 | | |

Critical F(2, 9) at 0.05 = 4.26 → **significant**: binder type affects dissolution. A post-hoc test (Tukey, Bonferroni, Dunnett) then shows which binders differ. Two-way ANOVA handles two factors and their interaction — it is the analysis behind factorial designs (Unit 2) and crossover bioequivalence studies.

## Remember

- Heckel: ln[1/(1 − D)] = KP + A; Py = 1/K (example 110 MPa); DA = 1 − e^(−A); DB = DA − D0; types A, B, C.
- Kawakita: P/C = P/a + 1/(ab); example a = 0.40, b = 0.030 MPa⁻¹, 1/b = 33 MPa.
- Fick: J = −D dC/dx; P = DK/h; lag time tL = h²/6D (example D = 2.3 × 10⁻⁹ cm²/s).
- Higuchi Q = kH√t; Peppas Mt/M∞ = ktⁿ (cylinder: n 0.45 Fickian, 0.89 case II; use first 60%).
- f1 0–15 and f2 50–100 = similar; ≥ 3 points, one point after 85%, 12 units, CV limits. Example f1 7.7, f2 63.9.
- DE and MDT example: DE45 58.2%, MDT 16.5 min.
- PK example: Cmax 8.1 µg/ml, Tmax 2 h, AUC0–∞ 64.9, t½ 4.2 h, MRT 6.8 h; BE 90% CI 80.00–125.00%.
- Statistics: SD with n − 1; t-test (t = 5.00 > 2.228); χ² (4.40 > 3.841); ANOVA F (15.6 > 4.26); p < 0.05 → reject H0.
