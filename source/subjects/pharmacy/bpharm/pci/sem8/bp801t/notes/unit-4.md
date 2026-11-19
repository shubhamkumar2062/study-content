# Unit 4: Blocking and confounding, regression modelling and statistical software

This unit joins three practical ideas. First, how to run a two-level factorial experiment when all runs cannot be done under the same conditions (blocking and confounding). Second, how to test whether a fitted regression model and each of its coefficients are real (hypothesis testing in simple and multiple regression, with a short note on logistic regression). Third, how statistical problems from industry and clinical trials are handled in software: Excel, SPSS, MINITAB, design-of-experiments packages and R.

All numbers in the worked examples are **example numbers** made up for practice.

## 4.1 Two-level factorial designs: a quick recap

A **2^k factorial design** studies k factors, each at two levels (low "−" and high "+"), in all 2^k combinations. The runs are written in **standard (Yates) order** using lower-case letters for factors at their high level; (1) means every factor is low.

```text
2^3 runs in standard order:  (1), a, b, ab, c, ac, bc, abc
```

Each effect is estimated from a **contrast**: add the responses with a "+" sign in that effect's column and subtract those with "−". Effect = contrast ÷ 2^(k−1); sum of squares = contrast² ÷ 2^k (single replicate). Full detail is in Unit 5.

## 4.2 Blocking

Sometimes the runs of a design cannot all be made under uniform conditions: one batch of raw material is enough for only four runs, a machine can do only four runs a day, or two analysts share the work. These differences (batch, day, operator, equipment) are **nuisance factors**: they are not of interest but can add variation.

**Blocking** groups the runs into sets (blocks) that are as uniform as possible inside, so the difference between blocks is removed from the experimental error. Each block is treated as a level of an extra factor.

Benefits: smaller error, sharper tests of the real factors, fair comparison when conditions change. Randomise the run order within each block.

If the whole design is **replicated**, each replicate can simply form one block (for example replicate 1 on Monday, replicate 2 on Tuesday). No information is lost.

## 4.3 Confounding

When a single replicate of a 2^k design must be split into blocks smaller than 2^k runs, some effect must be mixed with the block difference. **Confounding** is the deliberate arrangement in which a chosen effect (usually a high-order interaction that is expected to be negligible) cannot be separated from the block effect. That effect is "sacrificed"; all other effects are still estimated cleanly.

### 4.3.1 2³ design in two blocks of four (confounding ABC)

Assign runs to blocks by the sign of the ABC column.

| Run | A | B | C | ABC sign | Block |
| --- | --- | --- | --- | --- | --- |
| (1) | − | − | − | − | 1 |
| a | + | − | − | + | 2 |
| b | − | + | − | + | 2 |
| ab | + | + | − | − | 1 |
| c | − | − | + | + | 2 |
| ac | + | − | + | − | 1 |
| bc | − | + | + | − | 1 |
| abc | + | + | + | + | 2 |

```text
 Block 1 (ABC = −):  (1)   ab   ac   bc      ← principal block, contains (1)
 Block 2 (ABC = +):   a    b    c    abc
```

**Worked check (example numbers).** Responses: (1) = 62, a = 74, b = 55, ab = 69, c = 50, ac = 81, bc = 47, abc = 79.

- Block 1 total = 62 + 69 + 81 + 47 = 259; Block 2 total = 74 + 55 + 50 + 79 = 258.
- ABC contrast = 258 − 259 = −1, so ABC effect = −1/4 = −0.25.
- The block difference (per run) is exactly the same quantity: the ABC interaction and the block effect cannot be told apart. They are **confounded**.
- All main effects and two-factor interactions are unaffected because each has two "+" and two "−" runs in every block.

### 4.3.2 Method using the defining contrast

Write L = α1x1 + α2x2 + … + αkxk, where xi = 1 if factor i is at its high level in that run and 0 if low, and αi = 1 if factor i appears in the effect to be confounded. Runs with L mod 2 = 0 go to one block and L mod 2 = 1 to the other.

For ABC: L = x1 + x2 + x3. (1) → 0, a → 1, b → 1, ab → 2 = 0 (mod 2) and so on, giving the same blocks as above. The block containing (1) is the **principal block**; other blocks can be made by multiplying it by any run not in it (exponents taken mod 2).

### 4.3.3 2³ design in four blocks of two

Two effects are chosen, and their **generalised interaction** (product, squares dropped) is confounded too. Choosing AB and AC confounds AB × AC = A²BC = BC as well.

```text
 L1 = x1 + x2 (AB),  L2 = x1 + x3 (AC)
 Block (L1, L2) = (0,0): (1), abc
                  (1,1): a, bc
                  (1,0): b, ac
                  (0,1): ab, c
 Confounded with blocks: AB, AC, BC  (3 df for 4 blocks)
```

This is a poor choice if two-factor interactions matter, so in practice a larger design is blocked and only high-order interactions are confounded.

**Complete vs partial confounding.** If the same effect is confounded in every replicate it is completely confounded (no information on it). If a different effect is confounded in different replicates, it is **partially confounded**, and each effect is estimated from the replicates where it is not confounded.

**Remember the logic:** blocks are a nuisance; we hide the block difference inside an effect we do not care about, usually the highest interaction.

## 4.4 Regression modelling: hypothesis testing

A fitted regression equation is only useful if its slope (or coefficients) differ significantly from zero and the model explains enough of the variation.

### 4.4.1 Simple linear regression: y = a + bx

**Tests**

1. **t-test for the slope.** H0: β = 0 (no linear relation). t = b ÷ SE(b), with SE(b) = S(y.x) ÷ √Sxx and df = n − 2.
2. **t-test for the intercept.** H0: α = 0. SE(a) = S(y.x) × √(1/n + x̄²/Sxx).
3. **ANOVA (F-test) for regression.** Total SS (Syy) = regression SS + residual SS.

| Source | SS | df | MS | F |
| --- | --- | --- | --- | --- |
| Regression | SSR = b × Sxy | 1 | SSR/1 | MSR/MSE |
| Residual | SSE = Syy − SSR | n − 2 | SSE/(n − 2) | |
| Total | Syy | n − 1 | | |

For one x, F = t² of the slope test.

4. **Coefficient of determination** R² = SSR ÷ SST.
5. **Confidence interval of the slope:** b ± t(α, n − 2) × SE(b).

**Worked example (example numbers): the UV calibration from Unit 2.** b = 0.051, a = 0.002, S(y.x) = 0.00894, Sxx = 40, Syy = 0.10428, n = 5.

- SE(b) = 0.00894 ÷ √40 = 0.001414; t = 0.051 ÷ 0.001414 = **36.1**. Table t(0.05, 3) = 3.182, so the slope is highly significant.
- SE(a) = 0.00894 × √(0.2 + 36/40) = 0.00938; t = 0.002 ÷ 0.00938 = 0.21 < 3.182, so the intercept does not differ from zero (the line passes through the origin, as Beer's law expects).
- ANOVA: SSR = 0.051 × 2.04 = 0.10404; SSE = 0.00024; MSE = 0.00008; F = 0.10404 ÷ 0.00008 = **1300.5** (= 36.06²). Table F(1, 3) = 10.13.
- R² = 0.10404 ÷ 0.10428 = 0.998.
- 95% CI of slope = 0.051 ± 3.182 × 0.001414 = **0.0465 to 0.0555**.

### 4.4.2 Multiple regression: y = b0 + b1x1 + … + bkxk

1. **Overall F-test.** H0: all slopes are zero. F = (SSR/k) ÷ [SSE/(n − k − 1)].
2. **t-test for each coefficient.** H0: bi = 0 while the other variables stay in the model. t = bi ÷ SE(bi), df = n − k − 1.
3. **R² and adjusted R².** R² never falls when a variable is added, even a useless one. Adjusted R² = 1 − (1 − R²)(n − 1)/(n − k − 1) penalises extra variables and is better for comparing models.
4. Check residuals (random scatter, normal), **multicollinearity** (highly correlated x's make coefficients unstable) and outliers.
5. Variable selection: forward selection, backward elimination, stepwise regression.

**Worked example (example numbers): hardness model from Unit 2.** y = 0.767 + 0.48x1 + 0.75x2; n = 6, k = 2; SST = 8.173, SSE = 0.163, SSR = 8.010.

| Source | SS | df | MS | F |
| --- | --- | --- | --- | --- |
| Regression | 8.010 | 2 | 4.005 | **73.6** |
| Residual | 0.163 | 3 | 0.0544 | |
| Total | 8.173 | 5 | | |

Table F(2, 3) at 5% = 9.55: the model is significant. Because the design is balanced, SE(b1) = 0.233 ÷ √25 = 0.047 → t = 10.3; SE(b2) = 0.233 ÷ √4 = 0.117 → t = 6.4. Both exceed t(0.05, 3) = 3.18, so both force and binder matter. R² = 0.980; adjusted R² = 1 − 0.020 × 5/3 = 0.967.

### 4.4.3 Logistic regression (brief)

Used when the response is **binary** (cured/not cured, responder/non-responder, dead/alive) rather than a measured number. It models the log of the odds:

logit(p) = ln[p ÷ (1 − p)] = b0 + b1x1 + b2x2 + …

p = 1 ÷ [1 + e^−(b0 + b1x)]

e^b1 is the **odds ratio** for a one-unit rise in x. Coefficients are found by maximum likelihood and tested with the Wald test or likelihood-ratio test.

**Example (example numbers).** A fitted model logit(p) = −4 + 0.5 × dose gives p = 0.27 at dose 6, p = 0.50 at dose 8 (the ED50) and p = 0.73 at dose 10. Odds ratio = e^0.5 = 1.65: each extra unit of dose multiplies the odds of response by 1.65.

Uses: dose–response with quantal end points, risk factors for adverse drug reactions, predicting treatment success in clinical studies.

## 4.5 Practical components of industrial and clinical trial problems

**Industrial (pharmaceutical manufacturing and development) problems solved by statistics**

| Problem | Statistical tool |
| --- | --- |
| Is a batch uniform? | Mean, SD, % RSD; weight variation and content uniformity limits |
| Is the process in control? | Control charts (x̄ and R charts, with limits at mean ± 3σ), process capability (Cp, Cpk) |
| Should a lot be accepted? | Acceptance sampling plans (binomial / Poisson) |
| Do two methods, analysts or sites agree? | F-test for precision, t-test for accuracy, ANOVA |
| Is the analytical method linear? | Regression, r, residuals |
| What is the shelf life? | Regression of assay on time; 95% confidence limit meeting the specification |
| Which formula is best? | Factorial design, response surface, optimization |
| Validation of a process | Three consecutive batches, mean and variability, capability |

**Clinical trial problems**

| Problem | Statistical tool |
| --- | --- |
| How many patients? | Sample size and power |
| Fair allocation | Randomisation (simple, block, stratified), blinding |
| Comparing two treatments | t-test, Mann–Whitney, chi-square |
| Before vs after on same patients, crossover | Paired t-test, Wilcoxon signed rank, ANOVA for crossover |
| Several doses | ANOVA, Kruskal–Wallis, trend tests |
| Binary outcome with risk factors | Chi-square, relative risk, odds ratio, logistic regression |
| Time to event | Survival analysis (Kaplan–Meier, log-rank test) |
| Bioequivalence | Two one-sided tests; 90% CI of the ratio of geometric means within 80–125% for AUC and Cmax |
| Interim looks and safety | Data safety monitoring, adjusted significance levels |

## 4.6 Statistical analysis using software

Exams usually ask for features and steps, not screen-by-screen detail. Learn what each package is good for and the outline of one analysis.

### 4.6.1 Microsoft Excel

A spreadsheet with built-in statistical functions and the **Analysis ToolPak** add-in.

- Useful functions: AVERAGE, MEDIAN, MODE, STDEV.S (sample SD), VAR.S, CORREL, SLOPE, INTERCEPT, RSQ, T.TEST, CHISQ.TEST, NORM.DIST.
- Enable ToolPak: File → Options → Add-ins → Manage Excel Add-ins → Go → tick Analysis ToolPak.
- **Steps for an unpaired t-test:** enter the two groups in two columns → Data → Data Analysis → "t-Test: Two-Sample Assuming Equal Variances" → choose the two ranges, set hypothesised difference 0 and alpha 0.05 → choose the output range → OK → read t Stat, P(T<=t) two-tail and t Critical two-tail.
- Other ToolPak tools: Descriptive Statistics, Anova: Single Factor, Anova: Two-Factor, Correlation, Regression, Histogram, F-Test.
- Charts: Insert → Chart (scatter with trendline showing the equation and R²).
- Limits: few non-parametric tests, no built-in DoE, easy to make undetected errors.

### 4.6.2 SPSS (Statistical Package for the Social Sciences, IBM)

Menu-driven software widely used in clinical and social research.

- Two views: **Data View** (rows = cases, columns = variables) and **Variable View** (name, type, label, value labels, measurement level).
- **Steps for one-way ANOVA:** define variables in Variable View (for example "hardness" scale, "binder" nominal with value labels) → enter data → Analyze → Compare Means → One-Way ANOVA → move hardness to Dependent List and binder to Factor → Post Hoc (tick LSD or Tukey) → Options (Descriptives, Homogeneity of variance test) → OK → read the ANOVA table (F, Sig.) in the Output Viewer.
- Other menus: Analyze → Descriptive Statistics; Correlate → Bivariate; Regression → Linear / Binary Logistic; Nonparametric Tests (Mann–Whitney, Wilcoxon, Kruskal–Wallis, Friedman); Crosstabs → chi-square; Survival → Kaplan–Meier.
- Output can be pasted as syntax for repeatable analysis.

### 4.6.3 MINITAB

Widely used in industry for quality improvement, Six Sigma and design of experiments.

- Worksheet plus Session window (results) and graphs.
- Stat menu: Basic Statistics (descriptive, 1-sample and 2-sample t, paired t), Regression, ANOVA, Nonparametrics, Tables (chi-square), **Quality Tools** (control charts, capability analysis, gauge R&R) and **DOE**.
- **Steps for a 2² factorial design:** Stat → DOE → Factorial → Create Factorial Design → 2-level factorial, 2 factors, full factorial, set replicates and blocks → name factors and low/high levels → MINITAB prints a randomised run sheet → do the experiments and type responses in a new column → Stat → DOE → Factorial → Analyze Factorial Design → choose terms → read effects, coefficients, P values; draw Pareto and normal plots of effects, main-effects and interaction plots, contour and surface plots; use Response Optimizer for the best settings.

### 4.6.4 Design of experiments software

Packages such as Design-Expert (Stat-Ease) and the DOE modules of MINITAB and JMP are built for formulation and process optimization.

- Steps: choose design type (factorial, fractional factorial, central composite, Box–Behnken, mixture) → enter factors, ranges and responses → software gives the randomised run order → run experiments, enter responses → fit model (linear, interaction, quadratic) and check ANOVA, lack of fit, R², adjusted and predicted R² → view diagnostics (residual plots) → view contour, 3D surface and overlay plots → numerical optimization with desirability function → confirm the predicted optimum with check-point batches.

### 4.6.5 R (online / open-source statistical software)

R is free, open-source software from the R Project (CRAN), usually used through RStudio, and also available in online versions that run in a web browser.

- Works through commands (scripts) and thousands of add-on packages.
- Basic commands with example vectors:

```text
a <- c(82, 85, 79, 88, 84, 86)
b <- c(76, 80, 74, 79, 77, 82)
mean(a); sd(a)                 # descriptive statistics
t.test(a, b, var.equal = TRUE) # unpaired t-test
wilcox.test(a, b)              # Mann-Whitney / Wilcoxon rank sum
fit <- lm(y ~ x1 + x2)         # multiple regression
summary(fit)                   # coefficients, t, P, R-squared, F
aov(y ~ group)                 # one-way ANOVA
chisq.test(table)              # chi-square
```

- Strengths: free, reproducible scripts, excellent graphics, packages for clinical trials, bioequivalence, survival analysis and DoE. Limitation: needs learning the command language.

**Comparison of software**

| Feature | Excel | SPSS | MINITAB | R |
| --- | --- | --- | --- | --- |
| Interface | Spreadsheet | Menus (+ syntax) | Menus | Commands / scripts |
| Cost | Office licence | Licensed | Licensed | Free |
| Strength | Simple calculations, charts | Clinical and survey data | Quality control, DoE | Everything, reproducible |
| Non-parametric tests | Limited | Yes | Yes | Yes |

## 4.7 Remember

- Blocking removes nuisance variation (day, batch, operator) from error; randomise within blocks.
- Confounding: an unimportant interaction (usually the highest, e.g. ABC in a 2³) is sacrificed to the block difference; L = Σαixi mod 2 assigns runs; principal block contains (1).
- With four blocks, the generalised interaction is also confounded (AB × AC = BC).
- Regression tests: t for slope (df n − 2), F = MSR/MSE (= t² for one x), R², CI of slope; multiple regression: overall F, t per coefficient, adjusted R².
- Logistic regression: logit p = b0 + b1x; e^b1 = odds ratio; for binary outcomes.
- Excel → Analysis ToolPak; SPSS → Analyze menu; MINITAB → Stat → DOE / Quality Tools; R → commands such as t.test, lm, aov.
