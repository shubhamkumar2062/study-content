# Unit 2: Optimization techniques and design of experiments

This unit covers syllabus item 1(b): the concept and parameters of optimization, optimization techniques in pharmaceutical formulation and processing, statistical design, response surface methodology, contour plots, factorial designs and their application in formulation. It links directly to QbD (ICH Q8(R2)), where design of experiments (DoE) is the tool that builds the **design space**.

## 2.1 Concept of optimization

**Optimization** means finding the best possible composition or process conditions for a product, within the given constraints, so that one or more responses (dissolution, hardness, entrapment, particle size) reach their desired values.

The traditional approach, **one factor at a time (OFAT)** — change one variable while holding others fixed — has serious drawbacks:

- It cannot detect **interactions** (for example, the effect of binder level on hardness may depend on compression force).
- It needs many experiments for limited information and may miss the true optimum, which can lie in a region never tested.
- It gives no predictive model, so the formulator cannot say what will happen between tested points.

Statistical optimization varies all factors together according to a planned design, fits a mathematical model, and uses the model to predict and locate the optimum with a known uncertainty.

## 2.2 Terms and parameters of optimization

| Term | Meaning | Example |
| --- | --- | --- |
| Factor (independent variable) | Input the formulator controls | Polymer %, compression force, stirring speed |
| Level | Value at which a factor is set | Low (−1), centre (0), high (+1) |
| Response (dependent variable) | Measured output | % drug released at 8 h, hardness, particle size |
| Quantitative factor | Measured on a numeric scale | Binder concentration |
| Qualitative (categorical) factor | Type, not amount | Type of binder (PVP or starch paste), type of mixer |
| Effect | Change in response caused by changing a factor from low to high level | Main effect of A |
| Interaction | Effect of one factor depends on the level of another | AB |
| Coded value | Actual value scaled to −1 … +1 | X = (actual − centre)/half-range |
| Constraint | Limit the solution must meet | Hardness ≥ 5 kg, friability < 1% |
| Confounding (aliasing) | Two effects cannot be separated in a reduced design | In a half-fraction 2³⁻¹, C aliased with AB |
| Replication | Repeating runs to estimate pure error | Centre point repeated 3–5 times |
| Randomisation | Running trials in random order | Protects against drift and time effects |
| Blocking | Grouping runs to remove a known nuisance source | Two batches of raw material |

**Optimization parameters** are classified as:

- **Problem type: constrained versus unconstrained.** Real pharmaceutical problems are constrained (for example "maximise dissolution while hardness stays above 5 kg").
- **Variables: independent (formulation and process) and dependent (responses).**
- **Single-response versus multiple-response.** Multiple responses need trade-off tools such as the **desirability function** (each response converted to a 0–1 scale; overall D is the geometric mean, and the optimum maximises D) or overlay of contour plots.

## 2.3 Classification of optimization techniques

```text
Optimization techniques
├─ Classical (calculus based) — differentiate a known equation, set derivative = 0;
│                               works only for simple single-response problems
├─ Statistical design (DoE) — experiments first, then model
│   ├─ Screening designs: Plackett–Burman, fractional factorial, Taguchi
│   ├─ Factorial designs: full 2^k, 3^k, mixed-level
│   ├─ Response surface designs: central composite, Box–Behnken, 3^k
│   └─ Mixture designs: simplex lattice, simplex centroid, extreme vertices
├─ Model-free / sequential search: EVOP, simplex method (Spendley), steepest ascent
└─ Computer search methods: grid search, Lagrangian method, canonical analysis,
   artificial neural networks, genetic algorithms
```

### Sequential (search) methods

- **Evolutionary operation (EVOP):** small deliberate changes are made to a running production process (usually a 2² design around the current set point), repeated many times; when a change shows a real improvement the set point is moved. Safe because changes are too small to make out-of-specification product. Suited to production, not development.
- **Simplex method:** a geometric figure with k + 1 vertices for k factors (triangle for two factors). The worst vertex is reflected through the centroid of the others, and the simplex "walks" towards the optimum. The modified (Nelder–Mead) simplex can expand or contract.

### Lagrangian method

Used when the response and constraint can be written as equations (from a fitted model). The objective function and the constraints are combined with a Lagrange multiplier λ and the partial derivatives are set to zero. A classical example is optimizing tablet dissolution subject to a hardness constraint.

### Search (grid) method

The fitted model is evaluated at a fine grid of combinations; all combinations that meet the constraints are listed and the best is chosen. With a computer it handles many responses and constraints and does not need differentiable equations.

## 2.4 Statistical designs

### Screening designs

Used early, when there are many factors (say 6–15) and the aim is only to find the few important ones.

- **Plackett–Burman designs:** N runs (a multiple of 4) screen up to N − 1 factors at two levels; main effects only, interactions assumed negligible. For example 12 runs for up to 11 factors.
- **Fractional factorial (2^(k−p)):** a fraction of the full factorial. The **resolution** tells what is aliased: resolution III — main effects aliased with two-factor interactions; resolution IV — main effects clear, two-factor interactions aliased with each other; resolution V — main effects and two-factor interactions clear.
- **Taguchi orthogonal arrays** (L4, L8, L9, L18): also aim at **robustness** — choosing settings that make the product insensitive to noise factors, using signal-to-noise ratios.

### Full factorial designs

All combinations of all levels. For k factors at 2 levels: **2^k runs**; at 3 levels: **3^k runs** (3² = 9, 3³ = 27).

**2² design with interaction model:** Y = b0 + b1X1 + b2X2 + b12X1X2.

**2^k design** fits a linear model with interactions but cannot detect curvature; adding **centre points** tests for curvature and gives pure error.

### Response surface designs

To fit a **second-order (quadratic) model**:

Y = b0 + b1X1 + b2X2 + b12X1X2 + b11X1² + b22X2²

each factor needs at least three levels.

- **Central composite design (CCD):** a 2^k factorial (or fraction) + 2k **axial (star) points** at ±α + several **centre points**. Runs = 2^k + 2k + n0; for two factors with five centre points, 4 + 4 + 5 = 13 runs. α = (2^k)^(1/4) makes the design **rotatable** (equal prediction variance at equal distance from the centre): 1.414 for k = 2, 1.682 for k = 3. α = 1 gives a **face-centred CCD**, with only three levels per factor.
- **Box–Behnken design (BBD):** three levels per factor, points at the mid-points of the cube edges plus centre points; no runs at the extreme corners (useful when all-high or all-low combinations are impossible or unsafe). Three factors: 12 + centre points (commonly 3) = 15 runs; four factors: 24 + 3 = 27 runs.
- **3^k full factorial:** 9 runs for two factors; becomes large quickly.

### Mixture designs

When factors are proportions of a whole that must sum to 1 (for example the oil : surfactant : co-surfactant ratio of a SMEDDS, or a blend of three fillers), the factors are not independent, so ordinary factorial designs cannot be used.

- **Simplex lattice {q, m}:** q components, proportions in steps of 1/m. A {3, 2} lattice has 6 points: three pure components and three 50:50 binary blends.
- **Simplex centroid:** adds the centroid (1/3 : 1/3 : 1/3) and similar blends; 7 points for 3 components.
- **Extreme vertices design:** used when components have lower and upper limits (constrained mixture region).
- The model is the **Scheffé polynomial**, for example Y = b1X1 + b2X2 + b3X3 + b12X1X2 + b13X1X3 + b23X2X3 (no intercept).

## 2.5 Calculating effects in a 2³ factorial design (worked example)

A tablet was studied with factor A = binder concentration, B = superdisintegrant concentration, C = compression force, each at two levels (coded −1 and +1). Response: disintegration time (min).

| Run (Yates order) | A | B | C | Disintegration time (min) |
| --- | --- | --- | --- | --- |
| (1) | − | − | − | 4.2 |
| a | + | − | − | 7.8 |
| b | − | + | − | 2.6 |
| ab | + | + | − | 5.0 |
| c | − | − | + | 5.9 |
| ac | + | − | + | 10.1 |
| bc | − | + | + | 3.7 |
| abc | + | + | + | 7.3 |

**Rule:** effect of a factor = (sum of responses where the column sign is +) − (sum where it is −), divided by 2^(k−1) = 4. The sign column for an interaction is the product of the parent columns.

Main effect of A = [(7.8 + 5.0 + 10.1 + 7.3) − (4.2 + 2.6 + 5.9 + 3.7)] / 4 = (30.2 − 16.4)/4 = **3.45 min**.

| Effect | Value (min) | Regression coefficient (= effect/2) |
| --- | --- | --- |
| Mean (b0) | 5.825 | 5.825 |
| A (binder) | +3.45 | +1.725 |
| B (disintegrant) | −2.35 | −1.175 |
| C (force) | +1.85 | +0.925 |
| AB | −0.45 | −0.225 |
| AC | +0.45 | +0.225 |
| BC | −0.15 | −0.075 |
| ABC | +0.15 | +0.075 |

**Interpretation:**

- Binder level has the largest effect: raising it lengthens disintegration by 3.45 min on average.
- Superdisintegrant shortens it by 2.35 min; higher force lengthens it by 1.85 min.
- Interactions are small; AB negative means the disintegrant partly offsets the binder effect at high binder level.
- The model (ignoring the three-factor term) is Y = 5.825 + 1.725A − 1.175B + 0.925C − 0.225AB + 0.225AC − 0.075BC. Predicted disintegration at A = −1, B = +1, C = −1 is 2.53 min (observed 2.6 min).

Which effects are real? Without replicates, use a **half-normal (or normal) probability plot** of effects: real effects fall off the straight line formed by the small (noise) effects. With replicates or centre points, test each effect by ANOVA or a t-test against the error (Unit 6).

**Yates' algorithm** gives the same effects by repeated pairwise sums and differences of the responses arranged in standard order — handy without software.

## 2.6 Response surface method and contour plots

**Response surface methodology (RSM)** is a collection of statistical and mathematical techniques used to model and analyse problems in which a response is influenced by several variables, with the aim of optimizing that response. Steps:

1. Choose factors (from screening) and ranges; choose a design (CCD, BBD).
2. Run experiments in random order; measure responses.
3. Fit a polynomial model by multiple linear regression; check it by ANOVA: significant model, non-significant **lack of fit**, high R² with adjusted R² and predicted R² in reasonable agreement, adequate precision; check residual plots.
4. Draw **response surface (3-D)** and **contour (2-D)** plots.
5. Find the optimum (numerical optimization, desirability, or overlay of contour plots).
6. **Check-point (validation) batches:** prepare 2–3 batches at the predicted optimum and compare observed with predicted responses; a small percentage prediction error confirms the model.

**Contour plot:** a 2-D graph with two factors on the axes and lines joining combinations that give the same response (like height lines on a map). Straight parallel lines mean no interaction; curved lines mean interaction or quadratic terms; closed ellipses show a maximum or minimum inside the region (a stationary point); a saddle shape shows a minimax.

**Overlay plot:** contour plots of several responses are superimposed and the region meeting every constraint is shaded — this is the operational **design space** (or "sweet spot").

### Worked example: 2² design for a matrix tablet

Factors: X1 = HPMC (coded −1 = 10%, +1 = 20% of tablet weight), X2 = lactose : microcrystalline cellulose ratio (coded). Response: % drug released at 8 h.

| X1 | X2 | Released at 8 h (%) |
| --- | --- | --- |
| −1 | −1 | 92 |
| +1 | −1 | 68 |
| −1 | +1 | 96 |
| +1 | +1 | 80 |

b0 = (92 + 68 + 96 + 80)/4 = 84; b1 = (−92 + 68 − 96 + 80)/4 = −10; b2 = (−92 − 68 + 96 + 80)/4 = +4; b12 = (92 − 68 − 96 + 80)/4 = +2.

Model: **Y = 84 − 10X1 + 4X2 + 2X1X2**.

- Target 85% release with X2 = 0: 85 = 84 − 10X1, so X1 = −0.1, i.e. HPMC = 15 + 5 × (−0.1) = **14.5%**.
- The 80% contour passes through (X1, X2) = (0.0, −1), (0.4, 0) and (1.0, +1) — a curved line, because of the interaction term.

Because a 2² design has no curvature terms, the predicted optimum should be confirmed by check-point batches or by adding centre and axial points (moving to a CCD).

## 2.7 Applications of optimization in pharmaceutical formulation and processing

| Area | Typical factors | Typical responses |
| --- | --- | --- |
| Immediate-release tablets | Binder, disintegrant, lubricant level, force | Hardness, friability, disintegration, dissolution |
| Matrix sustained-release tablets | Polymer level and viscosity grade, filler type | Release at fixed times, release exponent n, f2 against target |
| Granulation | Binder volume, impeller speed, wet-massing time | Granule size, density, flow |
| Coating | Spray rate, inlet temperature, atomisation pressure | Coating efficiency, film defects, lag time |
| Microspheres / nanoparticles | Polymer:drug ratio, stirring speed, surfactant level | Particle size, entrapment efficiency, release |
| SMEDDS, nanoemulsions | Oil, surfactant, co-surfactant proportions (mixture design) | Droplet size, emulsification time, drug load |
| Liposomes | Lipid:cholesterol ratio, hydration time, sonication | Size, entrapment, zeta potential |
| Analytical methods (AQbD) | Mobile phase pH, organic %, flow rate, column temperature | Resolution, tailing, retention time |
| Process scale-up and robustness | Process parameters around the set point | Robustness of CQAs |

## 2.8 Optimization in Quality by Design

DoE is the link between the steps of QbD (ICH Q8(R2)):

```text
QTPP (quality target product profile)
  → CQAs (critical quality attributes)
  → risk assessment (ICH Q9: fishbone, FMEA) to pick likely CMAs and CPPs
  → screening DoE (Plackett–Burman / fractional factorial)
  → optimization DoE (CCD / BBD / mixture) → models
  → design space (overlay of acceptable regions; movement inside it is not a
    regulatory change)
  → control strategy → continual improvement (ICH Q10)
```

**Software** commonly used: Design-Expert, Minitab, JMP, Statistica, MODDE.

**Advantages of statistical optimization:** fewer experiments for more information; interactions and curvature detected; predictive models; documented scientific basis acceptable to regulators; robust products. **Limitations:** model valid only inside the studied region; poorly chosen ranges or responses give misleading optima; needs statistical skill; qualitative factors complicate RSM.

## Remember

- OFAT misses interactions; DoE varies all factors together and builds a model.
- Runs: 2^k full factorial; CCD = 2^k + 2k + n0 (13 for k = 2 with 5 centre points); rotatable α = (2^k)^¼ (1.414 for k = 2); BBD 15 runs for 3 factors.
- Effect = (Σ+ − Σ−)/2^(k−1); coefficient = effect/2. Worked 2³ example: A +3.45, B −2.35, C +1.85, AB −0.45 min.
- 2² example model Y = 84 − 10X1 + 4X2 + 2X1X2; 85% release needs HPMC 14.5% at X2 = 0.
- Screening: Plackett–Burman, fractional factorial (resolution III/IV/V), Taguchi. Optimization: CCD, BBD, 3^k. Mixtures: simplex lattice/centroid with Scheffé model.
- Validate with check-point batches; check lack of fit, R², adjusted and predicted R².
- Contour lines curved → interaction; overlay plot → design space; desirability 0–1 for many responses.
