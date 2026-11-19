# Last-night revision sheet

If you only have an hour, practise one worked numerical each of: **grouped mean, median and mode with SD**, **Karl Pearson's r and the regression line**, **unpaired and paired t-tests**, **one-way ANOVA with LSD**, **Mann–Whitney U and chi-square**, and **effects of a 2² / 2³ factorial design**. Then read the theory tables for sampling, errors, study types, clinical trial phases, CCD and optimization.

**Formulas to write without thinking**

| Formula | Use | Unit |
| --- | --- | --- |
| x̄ = Σx/n; grouped x̄ = Σfx/N | Mean | 1 |
| Median = L + [(N/2 − F)/f] × h | Grouped median | 1 |
| Mode = L + [(f1 − f0)/(2f1 − f0 − f2)] × h; Mode ≈ 3Md − 2x̄ | Grouped mode | 1 |
| s = √[Σ(x − x̄)²/(n − 1)]; Σ(x − x̄)² = Σx² − (Σx)²/n | Sample SD | 1 |
| CV = (s/x̄) × 100 | Relative spread, % RSD | 1 |
| r = Sxy/√(SxxSyy); ρ = 1 − 6Σd²/n(n² − 1) | Pearson, Spearman | 1 |
| b = Sxy/Sxx; a = ȳ − bx̄; r² = b(yx)b(xy) | Regression line | 2 |
| S(y.x) = √[Σ(y − ŷ)²/(n − 2)] | Standard error of estimate | 2 |
| P(x) = nCx p^x q^(n−x); mean np; variance npq | Binomial | 2 |
| z = (x − µ)/σ | Standard normal | 2 |
| SEM = s/√n | Precision of mean | 2 |
| t = (x̄ − µ)/(s/√n), df n − 1 | One-sample t | 2 |
| sp² = (SS1 + SS2)/(n1 + n2 − 2); t = (x̄1 − x̄2)/√[sp²(1/n1 + 1/n2)] | Unpaired t | 2 |
| t = d̄/(sd/√n), df n − 1 | Paired t | 2 |
| CF = G²/N; F = MS between / MS error | ANOVA | 2 |
| LSD = t(error df) × √(2MSE/n) | Post-hoc pairs | 2 |
| U = n1n2 + n1(n1 + 1)/2 − R1 | Mann–Whitney | 3 |
| H = [12/N(N + 1)]ΣR²/n − 3(N + 1) | Kruskal–Wallis | 3 |
| χr² = [12/bk(k + 1)]ΣRj² − 3b(k + 1) | Friedman | 3 |
| χ² = Σ(O − E)²/E; E = RT × CT/N; df (r − 1)(c − 1) | Chi-square | 3 |
| n = 2(zα/2 + zβ)²σ²/d² per group | Sample size, two means | 3 |
| t = b/SE(b); F = MSR/MSE = t² | Regression testing | 4 |
| Adjusted R² = 1 − (1 − R²)(n − 1)/(n − k − 1) | Multiple regression | 4 |
| logit p = ln[p/(1 − p)] = b0 + b1x; OR = e^b1 | Logistic regression | 4 |
| 2² effect A = ½[(a + ab) − ((1) + b)]; AB = ½[((1) + ab) − (a + b)] | Factorial effects | 5 |
| 2³ effect = contrast/4; SS = contrast²/8 | Factorial effects | 5 |
| CCD runs = 2^k + 2k + n0; rotatable α = (2^k)^¼ | Response surface | 5 |

**Numbers worth memorising**

| Fact | Value |
| --- | --- |
| Normal areas | ±1σ 68.27%, ±1.96σ 95%, ±2σ 95.45%, ±2.58σ 99%, ±3σ 99.73% |
| z (two-tailed) | 1.96 at 5%, 2.58 at 1% |
| zβ for power | 0.84 (80%), 1.28 (90%) |
| t (5%, two-tailed) | df 3: 3.182, 5: 2.571, 6: 2.447, 9: 2.262, 10: 2.228 |
| χ² (5%) | 1 df 3.84, 2 df 5.99, 3 df 7.81 |
| F (5%) | (1, 3) 10.13; (2, 6) 5.14; (2, 9) 4.26 |
| Large sample | n ≥ 30 |
| Chi-square rule | Expected ≥ 5 per cell; Yates' correction for small 2 × 2 |
| Rotatable α | 1.414 (k = 2), 1.682 (k = 3) |
| Bioequivalence | 90% CI of geometric mean ratio within 80–125% |

**Choosing a test**

| Data / question | Parametric | Non-parametric |
| --- | --- | --- |
| One sample vs a claimed value | One-sample t (z if n ≥ 30) | Wilcoxon signed rank |
| Two independent groups | Unpaired t | Mann–Whitney / Wilcoxon rank sum |
| Same subjects twice | Paired t | Wilcoxon signed rank |
| ≥ 3 independent groups | One-way ANOVA | Kruskal–Wallis |
| ≥ 3 treatments on same subjects | Two-way ANOVA | Friedman |
| Relation between two variables | Pearson r, regression | Spearman ρ |
| Counts in categories | — | Chi-square |

**Theory in one line each**

- Biostatistics: statistics applied to biology, medicine and pharmacy; descriptive vs inferential.
- Sampling: probability (simple random, systematic, stratified, cluster, multistage) vs non-probability (convenience, purposive, quota, snowball).
- H0 = no difference; Type I = rejecting a true H0 (α); Type II = accepting a false H0 (β); power = 1 − β.
- Fisher's principles of design: replication, randomisation, local control (blocking).
- Plagiarism: using others' words/ideas/data without credit; UGC 2018 regulations; cite and check similarity.
- Graphs: histogram (continuous classes), pie (parts of whole, angle = value/total × 360°), cube plot (2³ design), response surface (3D), contour plot (2D top view).
- Protocol: title, background, objectives, design, criteria, sample size, treatment, end points, safety, statistics, ethics, consent.
- Cohort: exposure → forward → relative risk. Case–control: disease → backward → odds ratio. RCT: randomised, controlled, blinded; strongest evidence.
- Trial phases: 0 microdose, I safety/PK in volunteers, II efficacy and dose in patients, III large confirmatory, IV post-marketing.
- Blocking removes nuisance variation; confounding hides the block effect in an unimportant interaction (ABC in a 2³ split into two blocks of four).
- Software: Excel (Analysis ToolPak), SPSS (Analyze menu), MINITAB (Stat → DOE, Quality Tools), R (t.test, lm, aov, chisq.test).
- Factorial design advantages: fewer runs, interactions measured, hidden replication, wider validity, model for optimization.
- CCD = factorial + axial + centre points; Box–Behnken has no corner points; historical design reuses past data.
- Optimization: Lagrangian, search, simplex, EVOP, canonical analysis, overlay contour, desirability function; confirm with check-point batches.
