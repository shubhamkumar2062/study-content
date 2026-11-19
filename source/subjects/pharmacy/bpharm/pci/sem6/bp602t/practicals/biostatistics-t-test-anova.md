# Biostatistics in experimental pharmacology: Student's t test and ANOVA

**Aim:** To analyse data from pharmacological experiments using Student's t test and analysis of variance (ANOVA), and to state whether the difference between groups is statistically significant.

> This exercise is worked from supplied data or simulation software; no animal is used.

## Principle

A drug effect seen in a few animals may be real or may be chance variation. **Statistical tests** estimate the probability (**p value**) that a difference as large as the one observed would appear by chance alone if the groups were really the same. By convention **p < 0.05** (less than 5 in 100) is called statistically significant.

| Test | Used when | Compares |
| --- | --- | --- |
| Unpaired (independent) t test | Two **different** groups, data normally distributed | Two means |
| Paired t test | The **same** animals before and after treatment | Two means of paired values |
| One-way ANOVA | **Three or more** groups, one factor | Several means at once |
| Two-way ANOVA | Two factors (for example drug and time) | Effects of both factors and their interaction |

Why not many t tests instead of ANOVA? Every extra t test raises the chance of a false positive; ANOVA tests all groups together with one overall F test, then a **post hoc test** (Dunnett's for comparison with a control, Tukey's for all pairs) shows which groups differ.

```text
 Unpaired t = (mean1 - mean2) / SE of the difference
 One-way ANOVA:  F = variance between groups / variance within groups
 Larger F -> groups differ more than chance would explain
```

**Mean** = sum ÷ n. **Standard deviation (SD)** measures spread of the data. **Standard error of the mean (SEM) = SD ÷ √n** measures how precisely the mean is known; results in pharmacology are usually written as **mean ± SEM**.

## Requirements

Supplied experimental data, calculator or spreadsheet, statistical tables for t and F values, graph paper; or statistical software.

## Procedure

**A. Unpaired t test**

1. Calculate the mean and SD of each group.
2. Calculate the pooled standard error of the difference between the means.
3. Calculate t = difference between means ÷ standard error of the difference.
4. Find the degrees of freedom: df = n1 + n2 − 2.
5. Compare the calculated t with the table value at that df and p = 0.05; if the calculated value is larger, the difference is significant.

**B. One-way ANOVA**

1. Calculate the grand mean of all observations.
2. Calculate the sum of squares between groups (SSB) and within groups (SSW), and the total.
3. Divide each by its degrees of freedom to get the mean squares (MSB, MSW).
4. Calculate F = MSB ÷ MSW.
5. Compare with the table F value at (k − 1) and (N − k) degrees of freedom.
6. If F is significant, apply a post hoc test (Dunnett's against the control, or Tukey's for all pairs) to find which groups differ.

## Observations and calculations

**Unpaired t test — specimen data (illustrative only).** Percentage protection against ulcer in two groups of 6 rats each.

| Group | Values | Mean | SD |
| --- | --- | --- | --- |
| Control | 10, 12, 9, 11, 13, 11 | 11.0 | 1.41 |
| Test drug | 18, 21, 19, 22, 20, 20 | 20.0 | 1.41 |

Standard error of the difference = √[(1.41² ÷ 6) + (1.41² ÷ 6)] = √(0.331 + 0.331) = 0.814.
t = (20.0 − 11.0) ÷ 0.814 = **11.06**, df = 10.
Table t at df 10, p = 0.05 (two-tailed) = 2.228. Calculated t is far larger, so **p < 0.05**: the difference is statistically significant.

**One-way ANOVA — specimen summary table.**

| Source of variation | Sum of squares | df | Mean square | F |
| --- | --- | --- | --- | --- |
| Between groups | 240.0 | 2 | 120.0 | 24.0 |
| Within groups (error) | 75.0 | 15 | 5.0 | |
| Total | 315.0 | 17 | | |

Table F at df 2 and 15, p = 0.05 = 3.68. Calculated F = 24.0 is larger, so the groups differ significantly; Dunnett's test then shows which treated groups differ from the control.

## Result

The difference between the control and test groups was statistically significant by the unpaired t test (t = 11.06, df = 10, p < 0.05), and the one-way ANOVA showed a significant difference among the three groups (F = 24.0, p < 0.05), confirmed by the post hoc test.

## Precautions

1. Decide the test before collecting data, from the design: paired or unpaired, two groups or more.
2. Check that the data are measurements on a continuous scale and roughly normally distributed; otherwise use a non-parametric test.
3. Use a paired test only when the same animals are measured twice.
4. Do not run many t tests between several groups; use ANOVA with a post hoc test.
5. Report mean ± SEM with the number of animals, the test used and the exact p value.
6. Remember that a statistically significant difference is not always biologically important.
7. Keep the group sizes equal where possible; it makes the test more powerful.

## Viva questions

1. **What does p < 0.05 mean?** There is less than a 5 % probability that a difference this large would arise by chance if the groups were really the same.
2. **Difference between SD and SEM?** SD describes the spread of the data; SEM (SD ÷ √n) describes the precision of the mean.
3. **When do you use a paired t test?** When the same animals or subjects are measured before and after treatment.
4. **Why use ANOVA instead of several t tests?** Repeated t tests increase the chance of a false positive; ANOVA tests all groups together.
5. **What does the F ratio compare?** Variance between groups against variance within groups.
6. **Name two post hoc tests.** Dunnett's test (treated groups against a control) and Tukey's test (all pairs).
7. **What are degrees of freedom in an unpaired t test?** n1 + n2 − 2.
8. **What is a null hypothesis?** The assumption that there is no real difference between the groups.
9. **What is a type I error?** Rejecting the null hypothesis when it is actually true, that is, a false positive.
