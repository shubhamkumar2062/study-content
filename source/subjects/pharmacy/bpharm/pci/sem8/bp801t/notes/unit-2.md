# Unit 2: Regression, probability, sampling and parametric tests

This is the heaviest unit of the subject. It moves from describing data to predicting and testing: regression gives an equation to predict one variable from another, probability and its distributions explain how chance behaves, sampling explains how a small group can stand for a whole batch or population, and parametric tests (t-tests and ANOVA) decide whether observed differences are real. Most 10-mark numericals come from here.

All numbers in the worked examples are **example numbers** made up for practice.

## 2.1 Regression

**Regression** is the estimation of the value of one variable (dependent, y) from a known value of another (independent, x) using a mathematical relationship. Correlation tells how strongly two variables are related; regression gives the actual equation for prediction.

| Point | Correlation | Regression |
| --- | --- | --- |
| Purpose | Degree and direction of relationship | Prediction of one variable from another |
| Variables | Both treated alike | One dependent, one independent |
| Coefficient | r, from −1 to +1, no unit | b (slope), carries units, any value |
| Symmetry | r(xy) = r(yx) | b(yx) ≠ b(xy) |

### 2.1.1 Curve fitting by the method of least squares

The best-fitting line is the one that makes the **sum of squared vertical deviations** (residuals) of observed points from the line the smallest. This is the principle of least squares.

For the line **y = a + bx**, minimising Σ(y − a − bx)² gives two normal equations:

- Σy = na + bΣx
- Σxy = aΣx + bΣx²

Solving them:

- b(yx) = Sxy ÷ Sxx = [nΣxy − ΣxΣy] ÷ [nΣx² − (Σx)²]
- a = ȳ − b x̄ (the line always passes through the point of means x̄, ȳ)

For the line **x = a′ + b′y** (regression of x on y), used to predict x from y:

- b(xy) = Sxy ÷ Syy, and a′ = x̄ − b′ȳ.

Link with correlation: r = ±√[b(yx) × b(xy)], and r takes the sign of the regression coefficients. Both coefficients have the same sign; if one is above 1, the other must be below 1. The two regression lines cross at (x̄, ȳ); they coincide when r = ±1 and are perpendicular when r = 0.

**Worked example (example numbers): UV calibration line**

Data from Unit 1: x = 2, 4, 6, 8, 10 µg/ml; y = 0.11, 0.20, 0.31, 0.40, 0.52. Sxy = 2.04, Sxx = 40, Syy = 0.10428, x̄ = 6, ȳ = 0.308.

- b(yx) = 2.04 ÷ 40 = **0.051**; a = 0.308 − 0.051 × 6 = **0.002**
- Regression of y on x: **y = 0.002 + 0.051x**
- Predict: a sample shows absorbance 0.35 → x = (0.35 − 0.002) ÷ 0.051 = **6.82 µg/ml**
- b(xy) = 2.04 ÷ 0.10428 = 19.56; a′ = 6 − 19.56 × 0.308 = −0.025; regression of x on y: **x = −0.025 + 19.56y**
- Check: b(yx) × b(xy) = 0.051 × 19.56 = 0.9977 = r², so r = 0.9988 (same as Unit 1).

### 2.1.2 Standard error of regression (standard error of estimate)

The standard error of estimate measures how far the observed points lie from the regression line on average:

S(y.x) = √[Σ(y − ŷ)² ÷ (n − 2)], with n − 2 degrees of freedom because two constants (a and b) were estimated.

Calibration example: predicted ŷ = 0.104, 0.206, 0.308, 0.410, 0.512; residuals 0.006, −0.006, 0.002, −0.010, 0.008; Σ(residual)² = 0.00024.

S(y.x) = √(0.00024 ÷ 3) = **0.0089** absorbance units. A small value means points lie close to the line. Standard error of the slope = S(y.x) ÷ √Sxx = 0.0089 ÷ √40 = 0.0014 (used for testing the slope in Unit 4).

### 2.1.3 Multiple regression

When y depends on two or more independent variables:

y = b0 + b1x1 + b2x2 + … + bkxk

Each partial regression coefficient (b1, b2…) is the change in y for a one-unit change in that x while the other x's are held constant. Coefficients are found by least squares, solving one normal equation per constant. For two variables:

- Σy = nb0 + b1Σx1 + b2Σx2
- Σx1y = b0Σx1 + b1Σx1² + b2Σx1x2
- Σx2y = b0Σx2 + b1Σx1x2 + b2Σx2²

**Worked example (example numbers): tablet hardness y (kg) against compression force x1 (kN) and binder level x2 (%)**

| Run | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| x1 | 5 | 10 | 5 | 10 | 7.5 | 7.5 |
| x2 | 1 | 1 | 3 | 3 | 2 | 2 |
| y | 4.0 | 6.1 | 5.2 | 7.9 | 5.9 | 6.1 |

Sums: n = 6, Σx1 = 45, Σx2 = 12, Σy = 35.2, Σx1² = 362.5, Σx2² = 28, Σx1x2 = 90, Σx1y = 276.0, Σx2y = 73.4.

Solving the three normal equations gives **y = 0.767 + 0.48x1 + 0.75x2**. Hardness rises 0.48 kg for each extra kN of force and 0.75 kg for each extra 1% of binder.

Multiple coefficient of determination R² = 1 − SSE/SST = 1 − 0.163/8.173 = **0.98**: 98% of the variation in hardness is explained by the two variables. Standard error of regression = √[SSE ÷ (n − k − 1)] = √(0.163 ÷ 3) = 0.23 kg.

Pharmaceutical uses of regression: calibration curves and assay, stability (log concentration against time for first-order decay, giving k and shelf life), dose–response and probit analysis, IVIVC, QSAR, predicting formulation responses in design of experiments.

## 2.2 Probability

**Probability** is a number from 0 to 1 that measures how likely an event is. 0 means impossible, 1 means certain.

**Classical (a priori) definition:** P(A) = number of favourable outcomes ÷ total number of equally likely outcomes.

**Relative frequency (empirical) definition:** P(A) = the limit of (number of times A occurred ÷ number of trials) as trials increase. Example: if 3 of 1000 patients show a rash, P(rash) ≈ 0.003.

**Key terms and rules**

| Term / rule | Meaning |
| --- | --- |
| Experiment, outcome, sample space | A trial, one result, the set of all results |
| Mutually exclusive events | Cannot occur together (a tablet passes or fails) |
| Independent events | One does not change the chance of the other |
| Addition rule | P(A or B) = P(A) + P(B) − P(A and B); for exclusive events P(A) + P(B) |
| Multiplication rule | P(A and B) = P(A) × P(B) for independent events |
| Complement | P(not A) = 1 − P(A) |
| Conditional probability | P(A given B) = P(A and B) ÷ P(B) |

A **probability distribution** lists every possible value of a random variable with its probability. Discrete examples: binomial and Poisson; continuous example: normal.

### 2.2.1 Binomial distribution

Used when there are n independent trials, each with only two outcomes (success or failure), and the probability of success p stays the same in each trial (q = 1 − p).

P(x successes) = nCx × p^x × q^(n − x)

Mean = np; variance = npq; SD = √npq.

**Worked example (example numbers).** 10% of capsules from a machine are defective. In a sample of 5, find the probabilities.

| Defectives x | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| P(x) | 0.5905 | 0.3281 | 0.0729 | 0.0081 | 0.00045 | 0.00001 |

P(no defective) = 0.9^5 = 0.5905; P(at least one) = 1 − 0.5905 = **0.4095**. Mean = 5 × 0.1 = 0.5 defective; variance = 5 × 0.1 × 0.9 = 0.45.

Uses: number of patients responding out of n treated, number of defective units in a sample, acceptance sampling plans.

### 2.2.2 Poisson distribution (brief)

For counts of rare events in a fixed interval when n is large and p small: P(x) = e^(−m) m^x ÷ x!, with mean = variance = m (= np). Examples: particles per ml of an injection, rare adverse reactions, bacterial colonies per plate.

### 2.2.3 Normal distribution

The most important continuous distribution. Many biological measurements (body weight, tablet weight, assay values, errors of measurement) follow it approximately.

Equation: f(x) = [1 ÷ (σ√2π)] × e^[−(x − µ)² / 2σ²]

**Properties**

1. Bell-shaped and symmetrical about the mean.
2. Mean = median = mode, at the centre.
3. Described fully by two parameters, µ and σ.
4. The tails approach the x-axis but never touch it (asymptotic).
5. Total area under the curve = 1.
6. Area within µ ± 1σ = 68.27%, µ ± 1.96σ = 95%, µ ± 2σ = 95.45%, µ ± 2.58σ = 99%, µ ± 3σ = 99.73%.
7. Skewness zero; mesokurtic.
8. Points of inflexion at µ ± σ.

```text
                    _.-'''-._
                 .-'    |    '-.
               .'       |       '.
            _.'         |         '._
      __..-'  |    |    |    |    |  '-..__
   ---+-------+----+----+----+----+-------+---
     -3σ     -2σ  -1σ   µ   +1σ  +2σ     +3σ
              |<--- 68.27% --->|
         |<-------- 95.45% -------->|
```

**Standard normal variable:** z = (x − µ) ÷ σ, which has mean 0 and SD 1. Areas are read from z tables.

**Worked example (example numbers).** Tablet weights are normal with mean 250 mg and SD 5 mg.

- P(240 to 260 mg): z = ±2, area = **0.9545** (95.45% of tablets).
- P(more than 258 mg): z = (258 − 250) ÷ 5 = 1.6; area beyond z = 1.6 is **0.0548**, so about 5.5% of tablets.
- P(245 to 255 mg): z = ±1, area = 0.6827.

The normal distribution is the basis of z-tests, confidence intervals, control charts and most parametric tests; by the **central limit theorem**, means of large samples are close to normal even if the original data are not.

## 2.3 Sampling

### 2.3.1 Terms

- **Population (universe):** all units of interest. Finite (all tablets in batch B-101) or infinite.
- **Sample:** the part actually examined.
- **Large sample:** usually n ≥ 30; tested with the z (normal) test.
- **Small sample:** n < 30; tested with t, F and chi-square tests, which allow for extra uncertainty.
- **Sampling frame:** the list from which the sample is drawn.

**Essence (need) of sampling.** Studying every unit is often impossible or pointless: tests may destroy the product (assay, dissolution), populations may be huge, and time and money are limited. A well-drawn sample gives reliable results faster and cheaper, and with care (fewer units) the measurements can be more accurate. Good sampling needs a representative sample, an adequate size, independence of units and no bias.

### 2.3.2 Types of sampling

| Type | How it works | Example |
| --- | --- | --- |
| **Probability sampling** | Every unit has a known, non-zero chance of selection | |
| Simple random | Lottery or random-number table; every unit has an equal chance | Picking 20 tablets from a batch by random numbers |
| Systematic | Every kth unit after a random start | Every 100th tablet off the press |
| Stratified | Population split into similar groups (strata); random sample from each | Sampling from beginning, middle and end of a batch |
| Cluster | Groups (clusters) chosen at random, all units in them studied | Choosing whole villages in a survey |
| Multistage | Random selection in stages | District → village → household |
| **Non-probability sampling** | Selection chance not known; risk of bias | |
| Convenience | Units easiest to reach | Patients attending one clinic |
| Purposive (judgement) | Chosen by the investigator's judgement | Experts for a panel |
| Quota | Fixed numbers from each category, chosen non-randomly | 50 men, 50 women |
| Snowball | Subjects recruit others | Rare-disease patients |

**Sampling error** is the difference between a sample statistic and the population parameter due to chance; it falls as sample size rises. **Non-sampling errors** come from bias, faulty measurement, non-response or recording mistakes.

### 2.3.3 Standard error of mean (SEM)

SEM = σ ÷ √n (estimated by s ÷ √n). It is the SD of the distribution of sample means. A small SEM means the sample mean is a precise estimate of µ. SEM is used to build confidence intervals and in t and z tests.

**Example.** Ten tablets: s = 2.37 mg. SEM = 2.37 ÷ √10 = **0.75 mg**.

95% confidence interval for µ (large sample): x̄ ± 1.96 SEM; for a small sample: x̄ ± t(0.05, n − 1) × SEM.

SD vs SEM: SD describes the spread of individual values; SEM describes the precision of the mean. Report "mean ± SD" to describe data and "mean ± SEM" or a confidence interval when comparing means.

## 2.4 Testing of hypothesis

**Hypothesis:** a statement about a population parameter that can be tested with sample data.

- **Null hypothesis (H0):** there is no difference or no effect (new and old formulations dissolve equally; µ1 = µ2).
- **Alternative hypothesis (H1 or Ha):** there is a difference (µ1 ≠ µ2, two-tailed) or a difference in one stated direction (µ1 > µ2, one-tailed).

**Level of significance (α):** the risk we accept of rejecting a true H0, commonly 0.05 (5%) or 0.01 (1%). **P value:** the probability of getting a result at least this extreme if H0 were true. Reject H0 when P < α.

**Errors in testing**

| Decision | H0 true | H0 false |
| --- | --- | --- |
| Reject H0 | **Type I error (α)**: false positive | Correct (power = 1 − β) |
| Accept H0 | Correct (1 − α) | **Type II error (β)**: false negative |

- Type I error: concluding a drug works when it does not, or rejecting a good batch. In quality control α is called the producer's risk.
- Type II error: missing a real effect (concluding a useful drug does not work), or accepting a bad batch. In quality control β is called the consumer's risk.
- **Power** = 1 − β, the chance of detecting a real difference; usually set at 80% or 90%. Increasing sample size lowers both risks together.

**Steps of a test of significance**

1. State H0 and H1.
2. Choose α (0.05) and decide one- or two-tailed.
3. Choose the test (z, t, F, chi-square, non-parametric) and compute the test statistic.
4. Find the critical (table) value for the degrees of freedom.
5. If |calculated| ≥ critical (or P < α), reject H0; otherwise do not reject it.
6. State the conclusion in words.

**Degrees of freedom (df):** the number of values free to vary after constraints are fixed; for one sample, df = n − 1.

**Large-sample z-test for a mean:** z = (x̄ − µ) ÷ (σ/√n). Example (example numbers): 100 tablets give mean 248.6 mg, SD 6 mg; label claim 250 mg. z = (248.6 − 250) ÷ (6/10) = −2.33. |z| > 1.96, so the mean differs significantly from 250 mg at the 5% level.

## 2.5 Parametric tests

**Parametric tests** assume that data are quantitative, come from a normally distributed population, the samples are random and independent, and (for comparing groups) the variances are equal (homogeneity of variance). They use the mean and SD and are more powerful than non-parametric tests when these assumptions hold.

### 2.5.1 Student's t-test

Developed by W.S. Gosset ("Student") for small samples. The t distribution is symmetrical and bell-shaped like the normal but has heavier tails; it approaches the normal as df increases.

**(a) One-sample t-test** — compares a sample mean with a known or claimed value.

t = (x̄ − µ) ÷ (s/√n), df = n − 1

**Worked example (example numbers).** Assay of six tablets (% of label claim): 98.2, 99.1, 97.5, 98.8, 99.4, 97.9. Does the mean differ from 100%?

- x̄ = 98.48; Σ(x − x̄)² = 2.708; s = √(2.708/5) = 0.736; SEM = 0.736/√6 = 0.300
- t = (98.48 − 100) ÷ 0.300 = **−5.05**, df = 5
- Table t(0.05, 5) = 2.571. |t| > 2.571, so reject H0: the mean assay is significantly below 100% (P ≈ 0.004).

**(b) Unpaired (independent, pooled) t-test** — compares means of two independent groups.

Pooled variance: sp² = [Σ(x1 − x̄1)² + Σ(x2 − x̄2)²] ÷ (n1 + n2 − 2)

t = (x̄1 − x̄2) ÷ √[sp²(1/n1 + 1/n2)], df = n1 + n2 − 2

**Worked example (example numbers).** Percent drug dissolved at 30 min:

| Formulation A | 82 | 85 | 79 | 88 | 84 | 86 |
| --- | --- | --- | --- | --- | --- | --- |
| Formulation B | 76 | 80 | 74 | 79 | 77 | 82 |

- A: mean 84.0, Σ(x − x̄)² = 50.0; B: mean 78.0, Σ(x − x̄)² = 42.0
- sp² = (50 + 42) ÷ 10 = 9.2; sp = 3.03
- SE of difference = √[9.2(1/6 + 1/6)] = 1.751
- t = (84 − 78) ÷ 1.751 = **3.43**, df = 10; table t(0.05, 10) = 2.228
- Reject H0: A dissolves significantly faster than B (P ≈ 0.006).
- Check equal variances with the F ratio: 10.0/8.4 = 1.19, below F(5,5) = 5.05, so pooling is fair.

**(c) Paired t-test** — compares two related measurements on the same subjects (before and after, crossover).

d = difference for each pair; t = d̄ ÷ (sd/√n), df = n − 1 (n = number of pairs)

**Worked example (example numbers).** Diastolic BP (mm Hg) of six patients before and after a drug:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Before | 96 | 100 | 92 | 104 | 98 | 95 |
| After | 90 | 94 | 90 | 96 | 93 | 92 |
| d | 6 | 6 | 2 | 8 | 5 | 3 |

- d̄ = 30/6 = 5.0; Σ(d − d̄)² = 24; sd = √(24/5) = 2.19; SE = 2.19/√6 = 0.894
- t = 5.0 ÷ 0.894 = **5.59**, df = 5; table value 2.571
- Reject H0: the drug lowers diastolic BP significantly (P ≈ 0.003).

Pairing removes the variation between patients, which is why a paired design is more sensitive than comparing two separate groups.

### 2.5.2 F-test for two variances

F = larger variance ÷ smaller variance, with df (n1 − 1, n2 − 1). Used to check equality of variances (precision of two methods or two analysts) and as the basis of ANOVA.

### 2.5.3 Analysis of variance (ANOVA)

Repeating t-tests for three or more groups raises the overall chance of a Type I error. **ANOVA**, developed by R.A. Fisher, compares several means in one test by splitting the total variation into parts due to known sources and a part due to chance (error).

**Assumptions:** normal populations, equal variances, independent random samples, additive effects.

#### One-way ANOVA (one factor)

| Source | SS | df | MS = SS/df | F |
| --- | --- | --- | --- | --- |
| Between groups (treatments) | SSB | k − 1 | MSB | MSB/MSW |
| Within groups (error) | SSW | N − k | MSW | |
| Total | SST | N − 1 | | |

Computing steps: G = grand total; correction factor CF = G²/N; SST = Σx² − CF; SSB = Σ(Ti²/ni) − CF, where Ti = group total; SSW = SST − SSB.

**Worked example (example numbers).** Tablet hardness (kg) with three binders, four tablets each:

| Binder | Values | Total | Mean |
| --- | --- | --- | --- |
| PVP | 5.1, 5.4, 5.0, 5.3 | 20.8 | 5.2 |
| Starch | 6.2, 6.0, 6.5, 6.1 | 24.8 | 6.2 |
| MCC | 5.6, 5.9, 5.5, 5.8 | 22.8 | 5.7 |

- G = 68.4; N = 12; CF = 68.4²/12 = 389.88; Σx² = 392.22
- SST = 392.22 − 389.88 = 2.34
- SSB = (20.8² + 24.8² + 22.8²)/4 − 389.88 = 391.88 − 389.88 = 2.00
- SSW = 2.34 − 2.00 = 0.34

| Source | SS | df | MS | F |
| --- | --- | --- | --- | --- |
| Between binders | 2.00 | 2 | 1.000 | **26.5** |
| Within (error) | 0.34 | 9 | 0.0378 | |
| Total | 2.34 | 11 | | |

Table F(2, 9) at 5% = 4.26. F calculated is far greater, so the binders give significantly different hardness.

#### Least significant difference (LSD)

ANOVA says "the means differ" but not which ones. The LSD (Fisher's) test compares pairs after a significant F:

LSD = t(α, error df) × √(2 × MSE ÷ n)

Example: LSD = 2.262 × √(2 × 0.0378 ÷ 4) = 2.262 × 0.1374 = **0.31 kg**.

Differences between means: Starch − PVP = 1.0; Starch − MCC = 0.5; MCC − PVP = 0.5. All exceed 0.31, so every pair differs; starch gives the hardest tablets. (Other post-hoc tests: Tukey, Duncan, Bonferroni, Dunnett for comparison with one control.)

#### Two-way ANOVA (two factors)

Two sources of variation are studied together, for example formulation (rows) and analyst or day (columns, often a block). Without replication:

| Source | SS | df | F |
| --- | --- | --- | --- |
| Rows (factor A) | SSR | r − 1 | MSR/MSE |
| Columns (factor B) | SSC | c − 1 | MSC/MSE |
| Error (residual) | SSE | (r − 1)(c − 1) | |
| Total | SST | rc − 1 | |

SSR = Σ(row total²)/c − CF; SSC = Σ(column total²)/r − CF; SSE = SST − SSR − SSC.

**Worked example (example numbers).** Assay (%) of three formulations, each tested by four analysts:

| Formulation | Analyst 1 | 2 | 3 | 4 | Row total |
| --- | --- | --- | --- | --- | --- |
| F1 | 98.5 | 99.4 | 98.2 | 99.0 | 395.1 |
| F2 | 100.2 | 100.3 | 99.6 | 100.9 | 401.0 |
| F3 | 99.1 | 99.9 | 98.7 | 99.4 | 397.1 |
| Column total | 297.8 | 299.6 | 296.5 | 299.3 | G = 1193.2 |

CF = 1193.2²/12 = 118643.853; Σx² = 118650.820.

| Source | SS | df | MS | F | F table (5%) |
| --- | --- | --- | --- | --- | --- |
| Formulations | 4.502 | 2 | 2.251 | **33.3** | 5.14 |
| Analysts | 2.060 | 3 | 0.687 | **10.2** | 4.76 |
| Error | 0.405 | 6 | 0.0675 | | |
| Total | 6.967 | 11 | | | |

Both formulations and analysts differ significantly. Taking analysts out as a separate source made the error smaller, so the formulation comparison became more sensitive. With replication, two-way ANOVA also tests the **interaction** (A × B): whether the effect of one factor depends on the level of the other.

## 2.6 Remember

- Least squares: y = a + bx, b = Sxy/Sxx, a = ȳ − bx̄; r² = b(yx) × b(xy).
- Standard error of estimate = √[Σ(y − ŷ)²/(n − 2)].
- Binomial: nCx p^x q^(n−x), mean np, variance npq. Normal: z = (x − µ)/σ; 68–95–99.7 rule.
- Large sample ≥ 30 → z test; small sample → t test.
- Type I = reject true H0 (α); Type II = accept false H0 (β); power = 1 − β.
- One-sample t = (x̄ − µ)/(s/√n); unpaired uses pooled variance, df n1 + n2 − 2; paired uses differences, df n − 1.
- ANOVA: CF = G²/N; F = MS(between)/MS(error); LSD = t × √(2MSE/n) after a significant F.
