# Unit 2: Biostatistics

This unit gives the statistical tools needed to plan a study (sample size) and to analyse it (tests of significance). The B.Pharm course BP801T taught the formulas; here the emphasis is on choosing the right test, checking its assumptions, and interpreting P values and confidence intervals correctly. Every worked example is set out the way an examiner expects: data → hypotheses → formula → substitution → comparison with the table value → conclusion in words.

All data in the worked examples are example numbers for practice, not real product or patient data.

## 2.1 Definition and applications

**Biostatistics** is the branch of statistics that deals with the design of studies and the collection, presentation, analysis and interpretation of data from biology, medicine and pharmacy, so that valid conclusions can be drawn in the presence of variation.

**Descriptive statistics** summarise data (mean, median, SD, tables, graphs). **Inferential statistics** draw conclusions about a population from a sample (estimation with confidence intervals, and hypothesis testing).

Applications in pharmaceutical and medical research:

| Area | Use |
| --- | --- |
| Formulation development | Design of experiments, optimisation (factorial and response surface designs), comparison of batches |
| Quality control | Content uniformity, process capability, control charts, method validation (accuracy, precision, linearity by regression) |
| Dissolution | Comparison of profiles (similarity factor f2), ANOVA of release data |
| Pharmacokinetics | Bioequivalence (90% confidence interval of the test/reference ratio of Cmax and AUC within 80.00–125.00%), model fitting |
| Stability | Regression of assay against time to estimate shelf life |
| Pharmacology | Comparing treated and control animal groups, dose–response analysis |
| Clinical trials | Sample size, randomization, interim analysis, efficacy and safety analysis |
| Epidemiology and pharmacovigilance | Rates, relative risk, odds ratio, signal detection |

### 2.1.1 Types of data and variables

| Scale | Description | Example | Summary |
| --- | --- | --- | --- |
| Nominal | Categories without order | Blood group, gender | Counts, percentage, mode |
| Ordinal | Ordered categories, gaps unequal | Pain score 0–10, NYHA class | Median, interquartile range |
| Interval | Equal gaps, no true zero | Temperature in °C | Mean, SD |
| Ratio | Equal gaps, true zero | Weight, plasma concentration, dissolution % | Mean, SD, CV |

Nominal and ordinal data are **qualitative (categorical)**; interval and ratio are **quantitative**, which may be discrete (number of seizures) or continuous (blood pressure). The type of data, together with the number of groups and whether samples are paired, decides the test (section 2.10).

## 2.2 Sample size

A **sample** is the part of a population actually studied; **sample size (n)** is the number of experimental units (patients, animals, tablets) in it.

### 2.2.1 Importance of sample size

- **Too small:** low power; a real difference may be missed (Type II error); estimates are imprecise; the study wastes the effort and the exposure of its participants and animals, which is unethical.
- **Too large:** wastes money and time, exposes more subjects than needed to risk, and can make trivial differences "statistically significant".
- An adequate, justified sample size is required by ethics committees (IEC and IAEC), regulators (ICH E9 guidance on statistical principles) and journals.

### 2.2.2 Factors influencing sample size

| Factor | Effect on n |
| --- | --- |
| Level of significance (α) | Smaller α (0.01 instead of 0.05) → larger n |
| Power (1 − β) | Higher power (90% instead of 80%) → larger n |
| Effect size (clinically important difference, Δ) | Smaller difference to detect → much larger n (n ∝ 1/Δ²) |
| Variability (σ) | Greater SD → larger n (n ∝ σ²) |
| One- or two-tailed test | Two-tailed needs more |
| Design | Paired and crossover designs need fewer; cluster designs need more |
| Type of outcome | Binary outcomes usually need more than continuous ones |
| Number of groups and comparisons | More groups or multiple end points → larger n |
| Expected dropouts | Higher dropout rate → recruit more |
| Ratio of allocation | Unequal allocation (2:1) needs more in total |

The inputs come from previous studies, a pilot study, or the smallest difference that would change clinical practice.

### 2.2.3 Formulas and worked examples

Standard normal values used: z for two-sided α = 0.05 is **1.96**; z for power 80% (β = 0.20) is **0.84** (0.8416); for power 90% it is **1.28** (1.2816).

**(a) Comparing two means (parallel groups, equal size):**

n per group = 2(zα/2 + zβ)² σ² ÷ Δ²

Example: the SD of fall in systolic pressure is 10 mmHg; the trial must detect a 5 mmHg difference, α = 0.05 two-sided, power 80%.

n = 2 × (1.96 + 0.8416)² × 10² ÷ 5² = 2 × 7.849 × 100 ÷ 25 = **62.8 → 63 per group**. With 90% power, (1.96 + 1.2816)² = 10.51, so n = 84.1 → 85 per group.

**(b) Comparing two proportions:**

n per group = (zα/2 + zβ)² [p1(1 − p1) + p2(1 − p2)] ÷ (p1 − p2)²

Example: response 40% on new therapy vs 25% on standard (α 0.05, power 80%).

n = 7.849 × (0.24 + 0.1875) ÷ 0.0225 = 7.849 × 0.4275 ÷ 0.0225 = **149.1 → 150 per group**.

**(c) Estimating a single mean with a given precision (margin of error E):**

n = (zα/2 × σ ÷ E)². With σ = 12 and E = 3: n = (1.96 × 12 ÷ 3)² = 61.5 → **62**.

### 2.2.4 Dropouts

**Dropouts** are participants who leave before completion (side effects, loss to follow-up, consent withdrawn, protocol violation); **withdrawals** are those removed by the investigator. Dropouts reduce power and can cause attrition bias if they differ between groups.

Adjustment: **n(adjusted) = n ÷ (1 − d)**, where d is the expected dropout proportion.

- Example (a) with 10% dropouts: 63 ÷ 0.9 = **70 per group**.
- Example (b) with 15% dropouts: 150 ÷ 0.85 = 176.5 → **177 per group**.

(Multiplying by 1 + d instead, 63 × 1.1 = 69.3, slightly under-corrects; dividing is the correct form.)

Dropouts are reduced by short and convenient visits, reminders, reimbursement of travel, and good communication. Their reasons must be recorded, and analysis uses intention-to-treat with suitable handling of missing data.

## 2.3 Hypothesis testing: null hypothesis, errors and power

A **test of significance** decides whether an observed difference or association is larger than would be expected by chance alone.

- **Null hypothesis (H0):** no difference or no association (µ1 = µ2; the drug has no effect). It is the hypothesis that is actually tested.
- **Alternative hypothesis (H1):** a difference exists. **Two-tailed** H1: µ1 ≠ µ2 (difference in either direction; the usual choice). **One-tailed** H1: µ1 > µ2 (only when a difference in the other direction is impossible or irrelevant, fixed before the study).

**General steps of any test:**

1. State H0 and H1.
2. Choose the level of significance α (usually 0.05).
3. Choose the test according to data type, design and assumptions.
4. Calculate the test statistic (z, t, F, χ², U, T, H).
5. Find the degrees of freedom and the table (critical) value, or the exact P value.
6. Decide: if the calculated value exceeds the table value (P < α), reject H0.
7. State the conclusion in words, with the size of the effect and its confidence interval.

| Decision | H0 actually true | H0 actually false |
| --- | --- | --- |
| Reject H0 | **Type I error (α)** — false positive | Correct decision (power = 1 − β) |
| Do not reject H0 | Correct decision | **Type II error (β)** — false negative |

- **Level of significance (α):** the maximum risk of a Type I error the investigator accepts (5%).
- **Power (1 − β):** probability of detecting a real difference of the stated size; usually 80% or 90%.
- **Critical region:** values of the test statistic that lead to rejecting H0.

## 2.4 P value and its interpretation

The **P value** is the probability of obtaining a result at least as extreme as the one observed **if H0 were true**.

- P < 0.05 → "statistically significant at the 5% level": the data would be unusual under H0, so H0 is rejected.
- P ≥ 0.05 → H0 is not rejected; the study has **not shown** a difference.

Correct interpretation — what a P value is **not**:

1. It is not the probability that H0 is true, nor that the result happened "by chance".
2. P = 0.06 and P = 0.04 are almost the same evidence; 0.05 is a convention, not a cliff. Report exact P values (P = 0.012) rather than only "P < 0.05".
3. "Not significant" does **not** mean "no difference" (absence of evidence is not evidence of absence), especially in a small study with low power.
4. Statistical significance is not clinical importance: with thousands of patients a 1 mmHg difference can be significant but useless. Always give the **effect size** and its **95% confidence interval (CI)**.
5. Testing many outcomes or subgroups inflates false positives. With k independent tests at 0.05, the chance of at least one false positive is 1 − 0.95^k (for 10 tests about 40%). Remedies: one pre-specified primary end point, **Bonferroni correction** (use α/k), or post-hoc tests designed for multiple comparisons.

**Confidence interval:** a 95% CI is a range calculated so that, in repeated sampling, 95% of such intervals would contain the true value. If the 95% CI for a difference excludes 0 (or for a ratio excludes 1), the result is significant at the 5% level, and the width shows precision. This is why CIs are preferred to P values alone.

## 2.5 Degrees of freedom

**Degrees of freedom (df)** are the number of values in a calculation that are free to vary once certain quantities (such as the mean) have been fixed from the data. If five numbers must average 10, four can be anything, but the fifth is then fixed: df = 4.

| Test | Degrees of freedom |
| --- | --- |
| One-sample or paired t | n − 1 (n = number of observations or pairs) |
| Unpaired t | n1 + n2 − 2 |
| Correlation coefficient r (t-test of r) | n − 2 |
| One-way ANOVA | Between groups k − 1; within groups N − k; total N − 1 |
| Chi-square, contingency table | (rows − 1)(columns − 1) |
| Chi-square, goodness of fit | categories − 1 − parameters estimated |
| Kruskal–Wallis, Friedman | k − 1 (chi-square approximation) |

Table values used in this unit (two-tailed, 5%): t = 2.262 (df 9), 2.365 (df 7), 2.447 (df 6), 2.145 (df 14), 2.179 (df 12); F(2, 12) = 3.89; F(7, 7) = 3.79; χ² = 3.84 (1 df), 5.99 (2 df).

## 2.6 Types of significance tests

| Basis | Types |
| --- | --- |
| Distribution assumption | **Parametric** (assume normal distribution and equal variances, interval or ratio data): z, t, F/ANOVA, Pearson r. **Non-parametric (distribution-free)**: sign, Wilcoxon, Mann–Whitney, Kruskal–Wallis, Friedman, Spearman, chi-square |
| Sample size | Large sample (n > 30): z-test. Small sample: t-test |
| Design | Independent (unpaired) or related (paired, repeated measures) |
| Direction | One-tailed or two-tailed |
| Purpose | Difference between groups, association between variables, goodness of fit |

| Feature | Parametric | Non-parametric |
| --- | --- | --- |
| Data | Interval or ratio, approximately normal | Ordinal, skewed, small samples, outliers |
| Uses | Actual values (means, SD) | Ranks or counts |
| Power | Higher when assumptions hold | Slightly lower (about 95% for Wilcoxon/Mann–Whitney vs t) |
| Example question | Does mean AUC differ? | Does median pain score differ? |

Assumptions are checked with normality tests (Shapiro–Wilk, Kolmogorov–Smirnov), Q–Q plots and histograms, and equality of variances (F-test, Levene's test). When they fail, transform the data (log of AUC and Cmax in bioequivalence) or use a non-parametric test.

## 2.7 Parametric tests

### 2.7.1 Student's t-test

Used for small samples drawn from normally distributed populations when σ is unknown (it is estimated by s). W. S. Gosset published it under the pen-name "Student".

**(a) One-sample t-test:** t = (x̄ − µ) ÷ (s/√n), df = n − 1.

Example: ten tablets assayed 99.2, 101.4, 98.6, 100.8, 97.9, 99.5, 98.8, 100.2, 98.1, 99.0% of label claim. Does the mean differ from 100%?

- x̄ = 99.35; Σ(x − x̄)² = 11.725; s = √(11.725/9) = 1.141; SE = 1.141/√10 = 0.361
- t = (99.35 − 100) ÷ 0.361 = **−1.80**, df = 9; table t = 2.262
- |t| < 2.262 (P ≈ 0.11): H0 is not rejected. The batch mean is not shown to differ from 100% — but with only ten tablets the test has limited power, so this does not prove the mean is exactly 100%.

**(b) Unpaired (independent samples) t-test:**

sp² = [Σ(x1 − x̄1)² + Σ(x2 − x̄2)²] ÷ (n1 + n2 − 2); t = (x̄1 − x̄2) ÷ √[sp²(1/n1 + 1/n2)], df = n1 + n2 − 2

Example: fall in fasting blood glucose (mg/dl) after 4 weeks.

| Group | Values | n | Mean | Σ(x − x̄)² | Variance |
| --- | --- | --- | --- | --- | --- |
| Drug A | 18, 22, 25, 20, 24, 19, 23, 21 | 8 | 21.5 | 42.0 | 6.0 |
| Drug B | 14, 17, 15, 19, 16, 13, 18, 16 | 8 | 16.0 | 28.0 | 4.0 |

- Check variances: F = 6.0/4.0 = 1.5 < F(7, 7) = 3.79, so pooling is reasonable.
- sp² = (42 + 28) ÷ 14 = 5.0; SE of difference = √[5.0 × (1/8 + 1/8)] = √1.25 = 1.118
- t = (21.5 − 16.0) ÷ 1.118 = **4.92**, df = 14; table t = 2.145
- 95% CI for the difference = 5.5 ± 2.145 × 1.118 = **3.1 to 7.9 mg/dl**
- t > 2.145 (P ≈ 0.0002): reject H0. Drug A lowers glucose more, by about 5.5 mg/dl; the CI excludes 0.

If variances are clearly unequal, use Welch's t-test (separate variances, adjusted df).

**(c) Paired t-test:** t = d̄ ÷ (sd/√n), df = n − 1, where d = difference within each pair.

Example: systolic pressure (mmHg) of 8 patients before and after 4 weeks of a drug.

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Before | 150 | 162 | 148 | 170 | 158 | 166 | 154 | 160 |
| After | 142 | 151 | 145 | 158 | 150 | 160 | 149 | 150 |
| d | 8 | 11 | 3 | 12 | 8 | 6 | 5 | 10 |

- Σd = 63; d̄ = 7.875; Σ(d − d̄)² = 66.875; sd = √(66.875/7) = 3.091; SE = 3.091/√8 = 1.093
- t = 7.875 ÷ 1.093 = **7.21**, df = 7; table t = 2.365
- Reject H0 (P < 0.001): the fall of about 7.9 mmHg is significant. A paired design removes between-patient variation, which is why it is so sensitive. Crossover trials are analysed the same way.

### 2.7.2 Analysis of variance (ANOVA)

Comparing three or more means by repeated t-tests inflates the Type I error. ANOVA, developed by R. A. Fisher, tests all means at once by splitting the total variation into parts.

Assumptions: independent random samples, normal distribution within groups, equal variances (homoscedasticity).

**One-way ANOVA** (one factor):

| Source | SS | df | MS = SS/df | F |
| --- | --- | --- | --- | --- |
| Between groups (treatments) | SSB | k − 1 | MSB | MSB/MSW |
| Within groups (error) | SSW | N − k | MSW | |
| Total | SST | N − 1 | | |

Steps: G = grand total; CF = G²/N; SST = Σx² − CF; SSB = Σ(Ti²/ni) − CF; SSW = SST − SSB.

Example: % drug released at 30 min from three sustained-release formulations (n = 5 each).

| F1 | F2 | F3 |
| --- | --- | --- |
| 78, 82, 80, 85, 75 | 88, 90, 86, 92, 89 | 80, 84, 79, 83, 84 |
| T = 400, mean 80 | T = 445, mean 89 | T = 410, mean 82 |

- G = 1255; N = 15; CF = 1255²/15 = 105001.667; Σx² = 105325
- SST = 105325 − 105001.667 = 323.333
- SSB = (400² + 445² + 410²)/5 − 105001.667 = 223.333
- SSW = 323.333 − 223.333 = 100.0

| Source | SS | df | MS | F |
| --- | --- | --- | --- | --- |
| Between formulations | 223.33 | 2 | 111.67 | **13.40** |
| Within (error) | 100.00 | 12 | 8.33 | |
| Total | 323.33 | 14 | | |

Table F(2, 12) at 5% = 3.89. F = 13.40 > 3.89 (P ≈ 0.001): the formulations differ.

**Post-hoc comparison.** A significant F says only that at least one mean differs. Least significant difference: LSD = t(0.05, 12) × √(2 × MSW/n) = 2.179 × √(2 × 8.333/5) = 2.179 × 1.826 = **3.98%**. F2 − F1 = 9 and F2 − F3 = 7 exceed 3.98; F3 − F1 = 2 does not. F2 releases significantly faster than both; F1 and F3 do not differ. Other post-hoc tests: Tukey's HSD (all pairs), Dunnett's (each group vs a control, common in pharmacology), Bonferroni, Scheffé, Newman–Keuls.

**Other ANOVA designs:** two-way ANOVA (two factors, such as formulation and batch, or drug and time, with interaction); randomized block design (subjects or batches as blocks); repeated-measures ANOVA (same subjects measured at several times); analysis of covariance (ANCOVA, adjusting for a baseline value).

### 2.7.3 Correlation coefficient

**Correlation** measures the strength and direction of the linear relation between two continuous variables. **Karl Pearson's coefficient:**

r = Sxy ÷ √(Sxx × Syy), where Sxy = Σxy − ΣxΣy/n, Sxx = Σx² − (Σx)²/n, Syy = Σy² − (Σy)²/n

r lies between −1 and +1. Assumptions: both variables continuous and roughly normal, relation linear, no major outliers. **r² (coefficient of determination)** gives the proportion of variation in y explained by x. Significance: t = r√[(n − 2)/(1 − r²)], df = n − 2.

Example: age (years, x) and creatinine clearance (ml/min, y) in 8 patients.

| x | 25 | 35 | 45 | 55 | 60 | 65 | 70 | 80 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| y | 118 | 104 | 98 | 85 | 84 | 72 | 74 | 60 |

- Σx = 435, Σy = 695, Σx² = 26025, Σy² = 62885, Σxy = 35375
- Sxx = 2371.875; Syy = 2506.875; Sxy = −2415.625
- r = −2415.625 ÷ √(2371.875 × 2506.875) = **−0.991**; r² = 0.981 (98% of the variation in clearance is linked to age)
- t = −0.991 × √(6/0.0186) = −17.8, df = 6; table 2.447: highly significant negative correlation.

Correlation does not prove causation; a third variable may be responsible, and r measures only linear relations.

### 2.7.4 Regression

**Regression** gives an equation to predict y from x. By least squares, the line of y on x is ŷ = a + bx with b = Sxy/Sxx and a = ȳ − bx̄.

From the example: b = −2415.625/2371.875 = **−1.018**; a = 86.875 − (−1.018 × 54.375) = **142.25**.

ŷ = 142.25 − 1.018x: clearance falls about 1 ml/min for each year of age. Predicted clearance at 50 years = 142.25 − 50.9 = **91.3 ml/min**. Predictions should stay within the range of x studied (no extrapolation).

The standard error of estimate √[Σ(y − ŷ)²/(n − 2)] = √(46.69/6) = 2.79 ml/min measures scatter around the line. Regression is also used for calibration curves, shelf-life estimation, and in multiple and logistic forms (several predictors; binary outcome such as cured/not cured, giving adjusted odds ratios).

| Correlation | Regression |
| --- | --- |
| Degree of relationship | Nature of relationship; prediction |
| Symmetric (r of x and y is the same) | Not symmetric (y on x differs from x on y) |
| No units; −1 to +1 | Slope has units (ml/min per year) |

## 2.8 Non-parametric tests

Non-parametric tests use ranks or counts and make no assumption about the shape of the distribution. Use them for ordinal scores, small samples, skewed data or outliers.

| Purpose | Parametric | Non-parametric equivalent |
| --- | --- | --- |
| Two related samples | Paired t | Wilcoxon signed rank test (also sign test) |
| Two independent samples | Unpaired t | Wilcoxon rank sum test = Mann–Whitney U test |
| Three or more independent groups | One-way ANOVA | Kruskal–Wallis H test ("non-parametric analysis of variance") |
| Three or more related groups | Repeated-measures ANOVA | Friedman test |
| Correlation | Pearson r | Spearman's rank ρ, Kendall's τ |
| Categorical data (frequencies) | — | Chi-square test, Fisher's exact test, McNemar test (paired) |

### 2.8.1 Wilcoxon signed rank test (paired data)

Steps: find differences; drop zeros; rank |d| (average ranks for ties); sum ranks of positive (T+) and negative (T−) differences; T = smaller sum; reject H0 if T ≤ table value for n non-zero differences.

Example: pain score (0–10) of 10 patients before and after a topical gel.

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Before | 7 | 6 | 8 | 5 | 7 | 9 | 6 | 8 | 7 | 6 |
| After | 4 | 5 | 4 | 5 | 3 | 6 | 6 | 5 | 2 | 4 |
| d | 3 | 1 | 4 | 0 | 4 | 3 | 0 | 3 | 5 | 2 |

- Two zeros dropped → n = 8. |d| ranked: 1 → 1; 2 → 2; three 3s → ranks 3, 4, 5 → 4 each; two 4s → 6.5 each; 5 → 8.
- T+ = 36, T− = 0, so **T = 0**. Table T (n = 8, two-tailed 5%) = 3.
- T ≤ 3: reject H0; the gel reduces pain significantly.

### 2.8.2 Wilcoxon rank sum / Mann–Whitney U test (two independent groups)

Rank all observations together; R1 = rank sum of group 1. U1 = n1n2 + n1(n1 + 1)/2 − R1; U2 = n1n2 − U1; U = the smaller. Reject H0 if U ≤ table value.

Example: time (min) to onset of relief with formulation A (12, 15, 9, 20, 14, 18) and B (25, 22, 17, 30, 19, 27).

- Order all twelve values with their ranks: 9(1), 12(2), 14(3), 15(4), 17(5), 18(6), 19(7), 20(8), 22(9), 25(10), 27(11), 30(12).
- R1 (A) = 2 + 4 + 1 + 8 + 3 + 6 = 24; R2 (B) = 54 (check: 24 + 54 = 78 = 12 × 13/2).
- U1 = 36 + 21 − 24 = 33; U2 = 36 − 33 = 3; **U = 3**. Table U (n1 = n2 = 6, two-tailed 5%) = 5.
- U ≤ 5: reject H0; A acts faster. For larger samples z = (U − n1n2/2) ÷ √[n1n2(n1 + n2 + 1)/12] (here −2.40).

### 2.8.3 Kruskal–Wallis H test (non-parametric one-way analysis of variance)

H = [12 ÷ N(N + 1)] × Σ(Ri²/ni) − 3(N + 1), compared with χ² at k − 1 df.

Example: pain relief scores with three analgesic regimens (5 patients each): G1 = 3, 5, 4, 6, 2; G2 = 7, 9, 8, 6, 10; G3 = 5, 7, 6, 4, 8.

- Ranking all 15 (average ranks for ties) gives rank sums R1 = 20, R2 = 60, R3 = 40 (total 120 = 15 × 16/2).
- H = [12 ÷ 240] × (20² + 60² + 40²)/5 − 48 = 0.05 × 1120 − 48 = **8.0** (8.12 after correction for ties).
- χ²(2 df) = 5.99; H > 5.99: the regimens differ. Pairwise Mann–Whitney tests with Bonferroni correction (or Dunn's test) locate the difference.

### 2.8.4 Friedman test (related groups)

For b blocks (subjects) each receiving k treatments, rank within each block: χr² = [12 ÷ bk(k + 1)] × ΣRj² − 3b(k + 1), df = k − 1.

Example: 6 volunteers rank three flavoured suspensions (1 = best); rank sums R = 8, 17, 11. χr² = [12 ÷ (6 × 3 × 4)] × (64 + 289 + 121) − 72 = 79 − 72 = **7.0** > 5.99: preferences differ; the first flavour is preferred.

### 2.8.5 Rank correlation

**Spearman's ρ = 1 − 6Σd² ÷ n(n² − 1)**, where d = difference between the two ranks of each subject.

Example: two pharmacists rank 8 package designs; Σd² = 14. ρ = 1 − (6 × 14) ÷ (8 × 63) = 1 − 84/504 = **0.83**: strong agreement. (Approximate test: t = ρ√[(n − 2)/(1 − ρ²)] = 3.69 > 2.447, significant.)

**Kendall's τ** counts concordant and discordant pairs; it handles ties well and is preferred for small samples.

### 2.8.6 Chi-square (χ²) test

χ² = Σ(O − E)²/E, where E (expected frequency) = row total × column total ÷ grand total; df = (r − 1)(c − 1).

Uses: association between two categorical variables (contingency table), goodness of fit, and homogeneity of proportions. Conditions: frequencies (not percentages), independent observations, expected frequency at least 5 in most cells; otherwise combine categories or use **Fisher's exact test**. For a 2 × 2 table with small numbers apply **Yates' continuity correction**. For paired categorical data (before/after in the same patients) use **McNemar's test**.

Example: improvement with a new drug vs standard therapy.

| | Improved | Not improved | Total |
| --- | --- | --- | --- |
| New drug | 45 (E 37.5) | 15 (E 22.5) | 60 |
| Standard | 30 (E 37.5) | 30 (E 22.5) | 60 |
| Total | 75 | 45 | 120 |

- χ² = 7.5²/37.5 + 7.5²/22.5 + 7.5²/37.5 + 7.5²/22.5 = 1.5 + 2.5 + 1.5 + 2.5 = **8.0**
- Shortcut: N(ad − bc)² ÷ [(a + b)(c + d)(a + c)(b + d)] = 120 × 900² ÷ (60 × 60 × 75 × 45) = 8.0
- df = 1; table 3.84; P ≈ 0.005; with Yates' correction χ² = 6.97, still significant. The new drug is associated with more improvement (75% vs 50%).

## 2.9 Statistical software

SPSS, GraphPad Prism, SAS (used by industry and regulators), R (free), Minitab, Design-Expert (for optimisation), Microsoft Excel (Data Analysis tool pack). Software computes exact P values, but choosing the test, checking assumptions and interpreting results remain the researcher's job. Describe the software, version and tests in the methods section.

## 2.10 Choosing the right test

```text
What is the outcome?
├── Continuous, normal ──► 2 groups: unpaired t (independent) / paired t (related)
│                         3+ groups: one-way ANOVA (+ post-hoc) / repeated-measures ANOVA
│                         relation: Pearson r, linear regression
├── Ordinal or skewed ───► 2 groups: Mann–Whitney U / Wilcoxon signed rank
│                         3+ groups: Kruskal–Wallis / Friedman
│                         relation: Spearman ρ, Kendall τ
└── Categorical (counts) ► chi-square (Fisher's exact if expected < 5; McNemar if paired)
                          binary outcome with several predictors: logistic regression
```

## 2.11 Remember

- Sample size rises with smaller α, higher power, larger SD, smaller difference; n per group (means) = 2(zα/2 + zβ)²σ²/Δ²; 1.96 and 0.84 for α 0.05 and 80% power; adjust for dropouts by n/(1 − d).
- H0 = no difference; Type I = false positive (α); Type II = false negative (β); power = 1 − β.
- P value = probability of data this extreme if H0 were true; not the probability H0 is true; report effect size with 95% CI.
- df: one-sample/paired n − 1; unpaired n1 + n2 − 2; r n − 2; ANOVA k − 1 and N − k; χ² (r − 1)(c − 1).
- Parametric: t-tests, ANOVA (+ LSD/Tukey/Dunnett), Pearson r, regression. Non-parametric: Wilcoxon signed rank, Mann–Whitney, Kruskal–Wallis, Friedman, Spearman, chi-square.
- Worked answers: unpaired t 4.92 (df 14); paired t 7.21 (df 7); ANOVA F 13.40 (2, 12); r −0.991; T = 0; U = 3; H = 8.0; χ² = 8.0.
