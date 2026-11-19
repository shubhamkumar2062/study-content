# Biostatistics in experimental pharmacology: chi-square test and Wilcoxon signed rank test

**Aim:** To analyse experimental data using the chi-square test for counted (categorical) data and the Wilcoxon signed rank test for paired data that are not normally distributed.

> This exercise is worked from supplied data or simulation software; no animal is used.

## Principle

Not all data are measurements. Some results are **counts in categories** (cured or not cured, ulcer present or absent, dead or alive), and some measurements are **ranked** rather than normally distributed (scores, grades, small samples). These need different tests from the t test.

| Test | Type of data | Question answered |
| --- | --- | --- |
| Chi-square (χ²) test | Counts in categories (nominal) | Are the proportions in two or more groups different? |
| Wilcoxon signed rank test | Paired, ordinal or non-normal | Has the treatment changed the value in the same subjects? |
| Mann–Whitney U test | Two unpaired, non-normal groups | Do two independent groups differ? |

**Chi-square test.** Observed frequencies are compared with the frequencies expected if there were no association.

```text
 chi-square = sum of [ (O - E)^2 / E ]

 O = observed frequency in a cell
 E = expected frequency = (row total x column total) / grand total
 df = (rows - 1) x (columns - 1)
```

**Wilcoxon signed rank test.** A **non-parametric** test for paired data. The differences between pairs are ranked by size, ignoring the sign; the ranks of the positive and the negative differences are then added separately. If the treatment had no effect, the two sums would be about equal. The smaller sum **T** is compared with the critical value in the table: a calculated value **smaller than or equal to** the table value means the difference is significant. (Note the direction — this is the opposite of the t and F tests.)

## Requirements

Supplied experimental data, calculator or spreadsheet, chi-square and Wilcoxon tables, record sheet; or statistical software.

## Procedure

**A. Chi-square test**

1. Arrange the counted data in a contingency table with row and column totals.
2. Calculate the expected frequency for each cell: (row total × column total) ÷ grand total.
3. For each cell find (O − E)² ÷ E and add them all to get χ².
4. Find the degrees of freedom: (rows − 1) × (columns − 1).
5. Compare the calculated χ² with the table value at p = 0.05; a larger calculated value means the difference is significant.
6. Apply Yates' correction for a 2 × 2 table with small numbers, and use Fisher's exact test when any expected frequency is below 5.

**B. Wilcoxon signed rank test**

1. For each pair, calculate the difference (after − before). Discard pairs with a difference of zero and reduce n accordingly.
2. Rank the absolute differences from smallest to largest; give tied values the average rank.
3. Attach the original sign to each rank.
4. Add the positive ranks and the negative ranks separately; T is the smaller of the two sums.
5. Compare T with the critical value for n at p = 0.05. If **T is less than or equal to** the table value, the difference is significant.

## Observations and calculations

**A. Chi-square — specimen data (illustrative only).** Ulcer present or absent after treatment.

| Group | Ulcer present | No ulcer | Total |
| --- | --- | --- | --- |
| Control | 18 | 6 | 24 |
| Test drug | 8 | 16 | 24 |
| **Total** | **26** | **22** | **48** |

Expected for control–ulcer present = (24 × 26) ÷ 48 = 13; control–no ulcer = 11; test–ulcer present = 13; test–no ulcer = 11.

χ² = (18−13)²/13 + (6−11)²/11 + (8−13)²/13 + (16−11)²/11
= 25/13 + 25/11 + 25/13 + 25/11 = 1.92 + 2.27 + 1.92 + 2.27 = **8.38**, df = 1.

Table χ² at df 1, p = 0.05 = 3.84. Calculated value is larger, so the proportion of ulcers differs significantly between the groups.

**B. Wilcoxon signed rank — specimen data (illustrative only).** Pain score before and after treatment in 8 patients.

| Pair | Before | After | Difference | Rank of difference | Signed rank |
| --- | --- | --- | --- | --- | --- |
| 1 | 7 | 4 | −3 | 5.5 | −5.5 |
| 2 | 6 | 5 | −1 | 1.5 | −1.5 |
| 3 | 8 | 4 | −4 | 7 | −7 |
| 4 | 5 | 6 | +1 | 1.5 | +1.5 |
| 5 | 7 | 5 | −2 | 3.5 | −3.5 |
| 6 | 9 | 4 | −5 | 8 | −8 |
| 7 | 6 | 4 | −2 | 3.5 | −3.5 |
| 8 | 8 | 5 | −3 | 5.5 | −5.5 |

Sum of positive ranks = 1.5. Sum of negative ranks = 34.5. T = **1.5**, n = 8.
Critical value for n = 8 at p = 0.05 (two-tailed) = 3. Since 1.5 is less than 3, the reduction in pain score is statistically significant.

## Result

The chi-square test showed a significant difference in the proportion of animals with ulcers between the control and the test group (χ² = 8.38, df = 1, p < 0.05), and the Wilcoxon signed rank test showed a significant fall in pain score after treatment (T = 1.5, n = 8, p < 0.05).

## Precautions

1. Use the chi-square test on **frequencies (counts)**, never on percentages or means.
2. Check that the expected frequency in each cell is at least 5; otherwise use Fisher's exact test.
3. Apply Yates' correction for a 2 × 2 table with small numbers.
4. In the Wilcoxon test, rank the **absolute** differences and give tied values the average rank.
5. Drop pairs whose difference is zero and reduce n before using the table.
6. Remember the direction of the Wilcoxon table: a **small** calculated T is significant.
7. Choose a non-parametric test when the data are scores or the sample is small and clearly not normal.
8. Always report the test used, the statistic, n or df, and the p value.

## Viva questions

1. **What kind of data is the chi-square test used for?** Counts (frequencies) in categories, such as cured or not cured.
2. **How is the expected frequency calculated?** (Row total × column total) ÷ grand total.
3. **What are the degrees of freedom of a 2 × 2 table?** One: (2 − 1) × (2 − 1).
4. **When is Fisher's exact test used instead of chi-square?** When any expected frequency is less than 5.
5. **What is a non-parametric test?** A test that does not assume the data follow a normal distribution.
6. **Which parametric test does the Wilcoxon signed rank test replace?** The paired t test.
7. **Which test replaces the unpaired t test for non-normal data?** The Mann–Whitney U test.
8. **In the Wilcoxon test, when is the result significant?** When the calculated T is less than or equal to the table value.
9. **Why are pairs with zero difference discarded?** They give no information about the direction of change, and n is reduced accordingly.
