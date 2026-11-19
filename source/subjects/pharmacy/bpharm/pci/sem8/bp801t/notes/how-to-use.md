# How to use this guide

Biostatistics and Research Methodology is half numericals and half theory. The numerical half (averages, SD, correlation, regression, t-tests, ANOVA, non-parametric tests, chi-square, factorial effects) rewards practice: you must be able to set out a table, apply the formula and state a conclusion in words. The theory half (sampling, hypothesis testing, research design, protocol, study types, clinical trial phases, software, optimization) rewards neat definitions, lists and tables. Study one unit at a time: read the notes, then rework every worked example on paper without looking, then attempt the question bank and the MCQs for that unit.

The notes follow the five units of the PCI syllabus. Unit 2 is the largest (regression, probability, sampling and the parametric tests) and is kept as one unit because the syllabus lists it that way; give it two days. Chi-square and the Wilcoxon signed rank test are not named in the syllabus list but are added to Unit 3 because they are standard non-parametric tests that appear in papers and practicals. A short note on logistic regression (named in the syllabus scope) is placed in Unit 4. No unit has been split or merged.

All data in the worked examples are example numbers made up for practice, not real product or patient data.

**Typical PCI end-semester paper (75 marks, 3 hours).** Confirm the exact split with your college, since universities sometimes vary it.

| Section | What it asks | Marks |
| --- | --- | --- |
| A | Objective / MCQ | 20 × 1 = 20 |
| B | Long essays — attempt 2 of 3 | 2 × 10 = 20 |
| C | Short answers — attempt 7 of 9 | 7 × 5 = 35 |

The question bank has long (10-mark), short (5-mark) and very short (2-mark) questions. The very short ones are good warm-ups and help with MCQs.

**Probability ratings**

- **High** — asked in most years; prepare the full answer, with a worked numerical where one fits.
- **Medium** — asked every few years or as part of a bigger question.
- **Low** — rare, but useful for MCQs and as a backup choice.

These ratings are estimates from common patterns and syllabus weight, not a promise of what will be asked.

**Where the marks usually come from**

| Unit | Topics that keep coming back |
| --- | --- |
| 1 Introduction, averages, dispersion, correlation | Definition and uses of biostatistics, frequency distribution, mean/median/mode for grouped data, SD and CV, Karl Pearson's r, Spearman's rank correlation |
| 2 Regression, probability, sampling, parametric tests | Least-squares regression lines y on x and x on y, binomial and normal distribution with properties, types of sampling, Type I and II errors, SEM, the three t-tests, one-way ANOVA with LSD, two-way ANOVA |
| 3 Non-parametric tests, research, graphs, study design | Mann–Whitney and Wilcoxon, Kruskal–Wallis, Friedman, chi-square, need for research and DoE, plagiarism, graphs (histogram, pie, contour, response surface), sample size and power, protocol, cohort/observational/experimental studies, phases of clinical trials |
| 4 Blocking, regression modelling, software | Blocking and confounding in 2³ designs, hypothesis testing in simple and multiple regression, logistic regression idea, statistical problems in industry and clinical trials, Excel / SPSS / MINITAB / R steps |
| 5 Factorial design, RSM, optimization | Definition and advantages of factorial design, 2² and 2³ effects and interactions, central composite design, historical design, optimization techniques |

**Scoring tips for this subject**

1. In every numerical, write: data table → formula → substitution → answer with unit → conclusion in words. Most marks are for the method, so show each step even if your arithmetic slips.
2. For every test, state H0 and H1, the level of significance (5%), degrees of freedom, the table value and the decision ("calculated t 3.43 > table t 2.228, so H0 is rejected"). Carry the standard table values in your head: t(0.05) = 2.571 (df 5), 2.447 (df 6), 2.262 (df 9), 2.228 (df 10); χ²(0.05) = 3.84 (1 df), 5.99 (2 df), 7.81 (3 df); z = 1.96 and 2.58.
3. Keep the correction-factor layout for ANOVA (G, CF = G²/N, SST, SS between, SS error, df, MS, F) and always finish with an ANOVA table.
4. For choosing a test, draw the small "parametric vs non-parametric" match table (two independent groups, paired, three or more groups, association).
5. For theory questions, open with a one-line definition, then a numbered list or a table; for study types and trial phases a comparison table earns most marks.
6. Draw diagrams: normal curve with 68–95–99.7 areas, scatter diagrams, histogram, cube plot of a 2³ design, CCD layout, contour sketch, research-process flow chart.
7. Software questions want menu paths and steps, not screenshots: Excel → Data → Data Analysis; SPSS → Analyze; MINITAB → Stat → DOE; R → t.test(), lm(), aov().
8. Use a scientific calculator in statistics mode for Σx, Σx², Σxy, mean and SD, but still write the sums in the answer.
