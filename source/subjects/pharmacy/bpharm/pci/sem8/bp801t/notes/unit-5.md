# Unit 5: Factorial design, response surface methodology and optimization

Formulation scientists rarely change one thing at a time any more. They plan a set of experiments in which several factors change together, measure the responses, fit an equation and use it to find the best formula. This unit covers the factorial design (definition, 2² and 2³ designs, effects and their testing, advantages), response surface methodology (central composite design, historical data design) and optimization techniques.

All numbers in the worked examples are **example numbers** made up for practice.

## 5.1 Factorial design

### 5.1.1 Definition and terms

A **factorial design** is an experimental design in which every level of each factor is combined with every level of every other factor, so that all possible treatment combinations are studied. With k factors each at 2 levels, the design needs **2^k** runs (per replicate); with k factors at 3 levels, 3^k runs.

| Term | Meaning | Tablet example |
| --- | --- | --- |
| Factor | An independent variable that is deliberately changed | Binder concentration, compression force |
| Level | The value at which a factor is set | Binder 2% (low, −1) and 4% (high, +1) |
| Response | The measured outcome (dependent variable) | Hardness, disintegration time, % dissolved |
| Treatment / run | One combination of factor levels | Binder 4%, force 10 kN |
| Main effect | Average change in response when one factor goes from low to high | |
| Interaction | When the effect of one factor depends on the level of another | |
| Coded levels | Low = −1, high = +1, centre = 0 | |

Coding: x(coded) = [actual value − centre value] ÷ (half the range).

### 5.1.2 The 2² factorial design

Two factors A and B, each at two levels → four runs.

| Run | A | B | AB | Notation |
| --- | --- | --- | --- | --- |
| 1 | − | − | + | (1) |
| 2 | + | − | − | a |
| 3 | − | + | − | b |
| 4 | + | + | + | ab |

```text
   B high   b ---------- ab
            |            |
            |            |
   B low   (1) --------- a
          A low        A high
```

**Formulas (single replicate)**

- Main effect of A = ½[(a + ab) − ((1) + b)] = average response at high A − average at low A
- Main effect of B = ½[(b + ab) − ((1) + a)]
- Interaction AB = ½[((1) + ab) − (a + b)]
- Model in coded units: y = b0 + b1xA + b2xB + b12xAxB, where b0 = mean of all runs and each coefficient = effect ÷ 2.

**Worked example (example numbers).** A = binder level, B = compression force; response = disintegration time (min).

| Run | (1) | a | b | ab |
| --- | --- | --- | --- | --- |
| DT (min) | 4.0 | 6.0 | 7.0 | 13.0 |

- Effect A = ½[(6 + 13) − (4 + 7)] = ½(8) = **4.0 min**
- Effect B = ½[(7 + 13) − (4 + 6)] = ½(10) = **5.0 min**
- Effect AB = ½[(4 + 13) − (6 + 7)] = ½(4) = **2.0 min**
- Mean = 30/4 = 7.5 → **y = 7.5 + 2.0xA + 2.5xB + 1.0xAxB**

Both factors lengthen disintegration time, and the positive interaction means binder has a bigger effect at high force (7 → 13 min, a rise of 6) than at low force (4 → 6 min, a rise of 2). A one-factor-at-a-time study at low force would have badly underestimated the binder effect.

**Interaction plot.** Plot response against A, with one line for each level of B. Parallel lines = no interaction; non-parallel or crossing lines = interaction.

```text
              A low     A high    rise in DT
 B low          4   →     6          +2       (flat line)
 B high         7   →    13          +6       (steep line)
 Unequal rises = non-parallel lines = A × B interaction
```

### 5.1.3 The 2³ factorial design

Three factors A, B, C → eight runs, estimating three main effects (A, B, C), three two-factor interactions (AB, AC, BC) and one three-factor interaction (ABC).

**Table of signs (standard order)**

| Run | A | B | C | AB | AC | BC | ABC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| (1) | − | − | − | + | + | + | − |
| a | + | − | − | − | − | + | + |
| b | − | + | − | − | + | − | + |
| ab | + | + | − | + | − | − | − |
| c | − | − | + | + | − | − | + |
| ac | + | − | + | − | + | − | − |
| bc | − | + | + | − | − | + | − |
| abc | + | + | + | + | + | + | + |

Rules: interaction columns are the products of their main-effect columns; each column has four "+" and four "−"; every pair of columns is orthogonal (their products sum to zero).

**Calculation:** contrast = Σ(sign × response); effect = contrast ÷ 4 (that is, ÷ 2^(k−1)); SS = contrast² ÷ 8 (÷ 2^k).

**Worked example (example numbers).** % drug released at 6 h from a matrix tablet; A = channelling agent, B = polymer level, C = compression force.

| Run | (1) | a | b | ab | c | ac | bc | abc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| % released | 62 | 74 | 55 | 69 | 50 | 81 | 47 | 79 |

Grand total = 517; mean = 64.6.

| Effect | Contrast | Effect (÷ 4) | SS (contrast²/8) |
| --- | --- | --- | --- |
| A | 89 | 22.25 | 990.125 |
| B | −17 | −4.25 | 36.125 |
| C | −3 | −0.75 | 1.125 |
| AB | 3 | 0.75 | 1.125 |
| AC | 37 | 9.25 | 171.125 |
| BC | 7 | 1.75 | 6.125 |
| ABC | −1 | −0.25 | 0.125 |
| Total | | | 1205.875 |

**Yates' algorithm** (a quick tabular way to get the same contrasts): list responses in standard order; column 1 = sums of successive pairs followed by differences (second − first) of the same pairs; repeat for k columns. For the data above, column 3 reads 517 (total), 89 (A), −17 (B), 3 (AB), −3 (C), 37 (AC), 7 (BC), −1 (ABC).

**ANOVA with one replicate.** With no replicate there is no pure error, so small high-order interactions are pooled as error (or a normal probability plot of effects is used). Pooling AB, BC and ABC: SS(error) = 1.125 + 6.125 + 0.125 = 7.375, df 3, MS = 2.458.

| Source | SS | df | F | Significant at 5%? (F(1,3) = 10.13) |
| --- | --- | --- | --- | --- |
| A | 990.1 | 1 | 402.8 | Yes |
| B | 36.1 | 1 | 14.7 | Yes |
| C | 1.1 | 1 | 0.46 | No |
| AC | 171.1 | 1 | 69.6 | Yes |
| Error (pooled) | 7.4 | 3 | | |

Conclusion: channelling agent (A) raises release strongly, polymer (B) lowers it, compression force (C) alone has little effect, but force interacts with the channelling agent (AC). Fitted model: y = 64.6 + 11.1xA − 2.1xB + 4.6xAxC (coefficients = effects ÷ 2).

**Graphs used:** Pareto chart of effects, normal probability plot of effects (large effects fall off the straight line), main-effect and interaction plots, cube plot (Unit 3).

### 5.1.4 Advantages of factorial design

1. Studies several factors at the same time with fewer total runs than one-factor-at-a-time experiments.
2. Detects and measures **interactions** between factors, which OFAT cannot.
3. Every observation is used to estimate every effect (hidden replication), so precision is high.
4. Conclusions hold over a range of conditions, not just one fixed setting.
5. Gives a mathematical model (polynomial) for prediction and optimization.
6. Orthogonal design: effects are estimated independently.
7. Easy to analyse with sign tables, Yates' method or software.

**Limitations:** runs grow fast (2^7 = 128); two levels detect only linear effects, not curvature (centre points or three-level designs are needed); high-order interactions are hard to interpret. **Fractional factorial designs** (2^(k−p)) run a chosen fraction to screen many factors, accepting some confounding (aliasing) of effects, as in Unit 4. Plackett–Burman designs are another screening option.

## 5.2 Response surface methodology (RSM)

**RSM** is a collection of mathematical and statistical techniques for modelling and analysing problems in which a response is influenced by several variables, with the aim of finding the factor settings that give the optimum response. The model is usually a **second-order (quadratic) polynomial**:

y = b0 + b1x1 + b2x2 + b12x1x2 + b11x1² + b22x2²

The squared terms describe curvature, so the model can show a maximum, minimum or saddle point. The fitted equation is drawn as a **response surface** (3D) and a **contour plot** (2D).

**Typical RSM sequence**

```text
Screening design (fractional factorial / Plackett–Burman) → important factors
→ First-order design + steepest ascent → move towards the optimum region
→ Second-order design (CCD / Box–Behnken) → quadratic model
→ ANOVA, lack-of-fit, R² checks → contour / surface plots
→ Optimization → confirmation (check-point) batches
```

### 5.2.1 Central composite design (CCD)

The most widely used design for fitting quadratic models. It has three parts:

1. **Factorial (cube) points:** 2^k runs at ±1.
2. **Axial (star) points:** 2k runs, each at ±α on one axis with the other factors at 0.
3. **Centre points:** n0 replicated runs at (0, 0, …), which give pure error and check curvature.

Total runs N = 2^k + 2k + n0.

```text
 CCD for two factors (k = 2)
                 (0, +α)
                    *
          (−1,+1) o   o (+1,+1)
   (−α, 0) *        ●         * (+α, 0)      ● centre points (repeated)
          (−1,−1) o   o (+1,−1)              o factorial points
                    *                         * axial points
                 (0, −α)
```

**Choice of α**

| Type | α | Note |
| --- | --- | --- |
| Rotatable | α = (2^k)^¼ → 1.414 for k = 2, 1.682 for k = 3 | Equal prediction precision at equal distance from the centre |
| Face-centred (CCF) | α = 1 | Only three levels per factor; axial points on the cube faces |
| Inscribed (CCI) | Axial points at ±1, cube scaled inside | When ±1 limits cannot be exceeded |

Each factor takes five levels (−α, −1, 0, +1, +α) in a rotatable CCD. Example run numbers: k = 2 → 4 + 4 + 5 = 13 runs; k = 3 → 8 + 6 + 6 = 20 runs (centre points chosen by the experimenter).

**Advantages:** fits a full quadratic model efficiently, can be built on an existing factorial design (sequential), estimates curvature and pure error. **Box–Behnken design** is an alternative three-level design with no corner points (useful when extreme combinations are unsafe or impossible); for k = 3 it needs 12 runs + centre points.

### 5.2.2 Historical design (historical data design)

A **historical data design** uses results that already exist (past development batches, production records, earlier experiments) instead of new planned runs. The data are entered into DoE software, a regression model is fitted and response surfaces are drawn.

- Advantages: no new experiments, low cost, makes use of valuable past knowledge, useful for retrospective process understanding and troubleshooting.
- Limitations: data were not planned, so factors may be correlated (not orthogonal), ranges may be narrow, some combinations missing, uncontrolled variables may bias results; the model must be checked and confirmed with new runs.

## 5.3 Optimization techniques

**Optimization** means finding the best possible formulation or process: the combination of factor levels that gives the most desirable responses within constraints (for example maximum dissolution with hardness at least 5 kg and friability below 1%).

**Terms:** independent variables (formulation and process factors), dependent variables (responses), objective function (the response to maximise or minimise), constraints (limits other responses must meet), constrained and unconstrained optimization.

**Classification of methods**

```text
Optimization techniques
 ├── Experimentation continues as optimization proceeds
 │     ├── Evolutionary operation (EVOP)
 │     └── Simplex method (sequential simplex)
 └── Experimentation completed before optimization
       ├── Classical / Lagrangian method (calculus)
       ├── Search methods (grid search)
       ├── Canonical analysis
       ├── Graphical method: contour plots and overlays
       └── Desirability function (multiple responses)
```

| Method | Principle | Note |
| --- | --- | --- |
| Classical (calculus) | Set first derivative of the fitted equation to zero to find a maximum or minimum | Works for simple models without constraints |
| Lagrangian method | Adds constraints to the objective function using Lagrange multipliers | Needs a mathematical model; classic for tablet formulas with constraints |
| Search method | Model is evaluated at a fine grid of factor combinations; the best point meeting all constraints is chosen | Easy with computers; handles many responses |
| Simplex method | A geometric figure with k + 1 vertices (a triangle for two factors) moves away from the worst response towards better ones until the optimum is reached | Sequential; no model needed |
| Evolutionary operation (EVOP) | Small, planned changes made around the normal operating point during full-scale production; process improves step by step | Used in production; no off-line experiments |
| Canonical analysis | Transforms the quadratic model to find the stationary point and whether it is a maximum, minimum or saddle | Used with RSM |
| Graphical (overlay contour) | Contour plots of each response overlaid; the region meeting all specifications is the design space | Very common in QbD |
| Desirability function | Each response converted to a desirability d (0 = unacceptable, 1 = ideal); overall D = geometric mean of all d values is maximised | Standard in DoE software for several responses |

**Applications in pharmacy:** optimizing tablet formulas (binder, disintegrant, lubricant), coating processes, sustained-release matrices (polymer level for a target release profile), microspheres and nanoparticles (polymer ratio, stirring speed), emulsions and creams, extraction of plant actives, analytical method development (mobile phase composition, pH, flow rate), and building the design space in Quality by Design.

**Steps of a formulation optimization study**

1. Define the objective and the quality target (responses and acceptable ranges).
2. Identify factors and their ranges (prior knowledge, risk assessment, screening design).
3. Choose the design (factorial, CCD, Box–Behnken, mixture).
4. Run the experiments in random order.
5. Fit models; check ANOVA, R², lack of fit and residuals.
6. Draw contour, surface and overlay plots.
7. Find the optimum (search, desirability, overlay).
8. Prepare check-point batches and compare observed with predicted values (low % prediction error confirms the model).

## 5.4 Remember

- Factorial design = all combinations of all levels; 2^k runs; coded −1 / +1.
- 2² effects: A = ½[(a + ab) − ((1) + b)]; B = ½[(b + ab) − ((1) + a)]; AB = ½[((1) + ab) − (a + b)].
- 2³: effect = contrast/4, SS = contrast²/8; interaction columns = products of main-effect columns; Yates' algorithm gives all contrasts.
- Interaction: effect of one factor depends on the level of another; non-parallel lines in an interaction plot.
- Advantages of factorial design: fewer runs, interactions, hidden replication, wide validity, model for optimization.
- RSM uses a quadratic model; CCD = 2^k factorial + 2k axial (±α) + centre points; rotatable α = (2^k)^¼; face-centred α = 1.
- Historical design uses existing data; must be confirmed.
- Optimization: Lagrangian, search, simplex, EVOP, canonical, overlay contour, desirability; always confirm with check-point batches.
