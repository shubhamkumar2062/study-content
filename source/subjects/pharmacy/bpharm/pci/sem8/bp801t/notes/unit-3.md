# Unit 3: Non-parametric tests, research, graphs and study design

The first part of this unit covers tests that work without assuming a normal distribution. The second part moves from statistics to research method: why we do research, why experiments must be designed, honesty in writing (plagiarism), the graphs used to present results, and how to plan a study (sample size, power, protocol, types of study and the phases of a clinical trial).

All numbers in the worked examples are **example numbers** made up for practice.

## 3.1 Non-parametric tests

**Non-parametric (distribution-free) tests** do not assume that data come from a normal population and do not estimate parameters such as µ and σ. Most work on **ranks** instead of the actual values.

**When to use them**

- Data are ordinal (pain scores, taste rankings, grades).
- Data are clearly skewed or have outliers.
- Sample is very small and normality cannot be checked.
- Variances are unequal.

| Point | Parametric | Non-parametric |
| --- | --- | --- |
| Assumption | Normal distribution, equal variances | No distribution assumed |
| Data | Interval / ratio | Ordinal or ranked (also numerical) |
| Uses | Mean, SD | Median, ranks |
| Power | Higher when assumptions hold | Slightly lower |
| Examples | t-test, ANOVA, Pearson r | Mann–Whitney, Wilcoxon, Kruskal–Wallis, Friedman, Spearman ρ, chi-square |

**Parametric and matching non-parametric tests**

| Purpose | Parametric | Non-parametric |
| --- | --- | --- |
| Two independent groups | Unpaired t-test | Wilcoxon rank sum / Mann–Whitney U |
| Two related (paired) samples | Paired t-test | Wilcoxon signed rank test |
| Three or more independent groups | One-way ANOVA | Kruskal–Wallis H test |
| Three or more related groups (blocks) | Two-way ANOVA (randomised block) | Friedman test |
| Association of two variables | Pearson r | Spearman ρ |

**Ranking rule.** Rank all values from smallest (rank 1) upwards; tied values each get the average of the ranks they would occupy.

### 3.1.1 Wilcoxon rank sum test and Mann–Whitney U test

Both compare two independent groups and give the same conclusion; the Mann–Whitney U is the rank sum rearranged.

**Steps**

1. H0: the two groups come from the same population (equal medians).
2. Combine both samples and rank all values together.
3. Add the ranks of each group: R1 and R2. (Wilcoxon's statistic W is the rank sum of the smaller group.)
4. U1 = n1n2 + n1(n1 + 1)/2 − R1; U2 = n1n2 − U1. Use the smaller U.
5. If the smaller U ≤ table critical value, reject H0. For large samples (each n > 20) use z = (U − n1n2/2) ÷ √[n1n2(n1 + n2 + 1)/12].

**Worked example (example numbers).** Time to pain relief (min):

| Drug A | 18 | 22 | 15 | 25 | 20 |
| --- | --- | --- | --- | --- | --- |
| Ranks | 2 | 4 | 1 | 6 | 3 |
| Drug B | 30 | 26 | 28 | 24 | 35 |
| Ranks | 9 | 7 | 8 | 5 | 10 |

- R(A) = 16, R(B) = 39 (check: total = 55 = 10 × 11/2)
- U(A) = 25 + 15 − 16 = 24; U(B) = 25 − 24 = **1**
- Table critical U for n1 = n2 = 5 (two-tailed, 5%) = 2. Since 1 ≤ 2, reject H0: drug A gives faster relief.
- Wilcoxon rank sum W = 16; the lower critical rank sum for 5 and 5 is 17, so W ≤ 17 gives the same decision.

### 3.1.2 Wilcoxon signed rank test (paired data)

Non-parametric version of the paired t-test.

1. Find each difference d; drop zero differences.
2. Rank |d| from smallest, ignoring signs.
3. Give each rank the sign of its d; add positive ranks (T+) and negative ranks (T−).
4. T = the smaller sum; reject H0 if T ≤ table value for n (number of non-zero differences).

**Example (example numbers).** Eight patients' diastolic BP before and after a drug gave differences 6, 6, −1, 8, 5, 3, 2, 0. Dropping the zero, n = 7. Ranks of |d| (1, 2, 3, 5, 6, 6, 8) are 1, 2, 3, 4, 5.5, 5.5, 7. T− = 1 (the −1), T+ = 27. Critical T for n = 7 (two-tailed 5%) = 2. T = 1 ≤ 2, so the fall in BP is significant.

### 3.1.3 Kruskal–Wallis H test

Non-parametric version of one-way ANOVA for k ≥ 3 independent groups.

H = [12 ÷ N(N + 1)] × Σ(Ri² ÷ ni) − 3(N + 1)

N = total observations, Ri = rank sum of group i. Compare H with chi-square at k − 1 df (or exact tables for very small groups).

**Worked example (example numbers).** Percent inhibition of oedema with three treatments (four rats each):

| Group | Values | Ranks | Rank sum R |
| --- | --- | --- | --- |
| Drug X | 42, 48, 39, 45 | 2, 6, 1, 4 | 13 |
| Drug Y | 55, 60, 52, 58 | 10, 12, 8, 11 | 41 |
| Drug Z | 47, 50, 44, 53 | 5, 7, 3, 9 | 24 |

H = [12 ÷ (12 × 13)] × (13²/4 + 41²/4 + 24²/4) − 3 × 13 = 0.07692 × 606.5 − 39 = **7.65**

Chi-square (2 df, 5%) = 5.99. H > 5.99, so the treatments differ (P ≈ 0.02).

### 3.1.4 Friedman test

Non-parametric version of two-way ANOVA (randomised block design) for k ≥ 3 related treatments given to the same b subjects (blocks).

1. Rank the treatments within each subject (1 to k).
2. Add the ranks for each treatment: Rj.
3. χr² = [12 ÷ bk(k + 1)] × ΣRj² − 3b(k + 1), with k − 1 df.

**Worked example (example numbers).** Five panellists score three syrup flavours (1–10); scores are ranked within each panellist.

| Panellist | Orange | Mango | Mint |
| --- | --- | --- | --- |
| 1 | 6 (1) | 8 (3) | 7 (2) |
| 2 | 5 (1) | 9 (3) | 8 (2) |
| 3 | 7 (2) | 8 (3) | 6 (1) |
| 4 | 4 (1) | 7 (3) | 6 (2) |
| 5 | 5 (1) | 8 (3) | 6 (2) |
| Rank sum Rj | 6 | 15 | 9 |

χr² = [12 ÷ (5 × 3 × 4)] × (36 + 225 + 81) − 3 × 5 × 4 = 0.2 × 342 − 60 = **8.4**. Table chi-square (2 df) = 5.99, so flavour preference differs; mango is preferred.

### 3.1.5 Chi-square (χ²) test

The chi-square test compares **observed frequencies (O)** with **expected frequencies (E)**. It is a non-parametric test for counts.

χ² = Σ[(O − E)² ÷ E]

Uses: (1) goodness of fit (do data fit an expected ratio?); (2) test of independence or association in a contingency table; (3) homogeneity of proportions.

Conditions: data are counts (not percentages), observations independent, expected frequency in each cell ideally at least 5. For a 2 × 2 table with small numbers, Yates' continuity correction [(|O − E| − 0.5)²/E] is applied; for very small tables Fisher's exact test is used.

df: (rows − 1)(columns − 1) for a contingency table; (classes − 1) for goodness of fit.

**Worked example (example numbers).** Eighty patients in a trial:

| | Cured | Not cured | Total |
| --- | --- | --- | --- |
| New drug | 30 | 10 | 40 |
| Placebo | 18 | 22 | 40 |
| Total | 48 | 32 | 80 |

Expected E = row total × column total ÷ grand total: E(cured) = 40 × 48/80 = 24 in each row; E(not cured) = 16 in each row.

χ² = (30 − 24)²/24 + (10 − 16)²/16 + (18 − 24)²/24 + (22 − 16)²/16 = 1.5 + 2.25 + 1.5 + 2.25 = **7.5**

df = 1; table χ² = 3.84. Reject H0: cure is associated with the drug (P ≈ 0.006). (With Yates' correction χ² = 6.30, still significant.) The shortcut for 2 × 2: χ² = N(ad − bc)² ÷ [(a + b)(c + d)(a + c)(b + d)] = 80 × 400² ÷ (40 × 40 × 48 × 32) = 7.5.

## 3.2 Introduction to research

**Research** is a careful, systematic and objective search for new knowledge, or for answers to a defined question, using accepted methods.

**Need for research in pharmacy**

1. Discovery and development of new drugs and dosage forms.
2. Improving existing products (stability, bioavailability, patient acceptance, cost).
3. Proving safety and efficacy for regulatory approval.
4. Solving manufacturing and quality problems.
5. Generating evidence for rational drug use and better patient care (clinical and pharmacy practice research).
6. Building scientific knowledge and training scientists.

**Types of research:** basic (fundamental) and applied; descriptive and analytical; quantitative and qualitative; experimental and observational; cross-sectional and longitudinal.

**Steps of the research process**

```text
Identify problem → Review literature → Set objectives / hypothesis
→ Design study (variables, sample, methods) → Write protocol, get approvals
→ Collect data → Analyse statistically → Interpret → Report and publish
```

### 3.2.1 Need for design of experiments (DoE)

The traditional approach, one factor at a time (OFAT), changes one variable while all others are fixed. It needs many runs, cannot detect **interactions** between factors and may miss the true best condition. A planned **design of experiments** changes several factors together in a structured pattern so that:

- the effect of every factor and their interactions are estimated with few runs;
- experimental error is estimated and controlled;
- results can be modelled and the optimum predicted;
- it supports Quality by Design (QbD) and the design space concept.

### 3.2.2 Experimental design technique: basic principles

Fisher's three principles:

1. **Replication** — repeating each treatment so experimental error can be estimated and precision improved.
2. **Randomisation** — assigning treatments and run order by chance to remove systematic bias.
3. **Local control (blocking)** — grouping similar units into blocks (same day, same batch of raw material, same animal) so variation between blocks is removed from the error.

Common designs: completely randomised design (CRD), randomised block design (RBD), Latin square design, crossover design, factorial design (Unit 5), response surface designs.

Terms: **factor** (independent variable, e.g. binder level), **level** (the values of a factor, e.g. 2% and 4%), **response** (dependent variable, e.g. hardness), **run** (one experimental trial), **treatment** (one combination of levels).

### 3.2.3 Plagiarism

**Plagiarism** is presenting another person's words, ideas, data, figures or work as one's own without proper acknowledgement.

Forms: copying text without citation (direct), changing a few words (paraphrasing without credit), mixing sources (mosaic), reusing one's own published work without saying so (self-plagiarism), and copying data or images.

Consequences: rejection or retraction of papers, loss of degree, disciplinary action and loss of reputation. In India, the UGC (Promotion of Academic Integrity and Prevention of Plagiarism in Higher Educational Institutions) Regulations, 2018 set graded penalties for theses and research work.

Prevention: cite every source, quote exact words in quotation marks, write in your own words, keep good notes, and check drafts with similarity-checking software (for example Turnitin or Drillbit; Indian universities receive such software through INFLIBNET's ShodhShuddhi initiative).

## 3.3 Graphs

Graphs present data at a glance and show trends that tables hide. Every graph needs a title, labelled axes with units, a suitable scale, a legend where needed and the data source.

**Histogram** — adjacent bars drawn over class intervals of a continuous frequency distribution; bar area is proportional to frequency. Shows the shape of the distribution (symmetric, skewed, bimodal). Example: distribution of tablet weights. A frequency polygon joins the mid-points of the bar tops.

```text
 f |        ____
   |   ____|    |____
   |  |    |    |    |___
   |__|____|____|____|___|___ x (class)
```

**Bar chart** — separate bars for categories (number of prescriptions per brand). **Pie chart** — a circle divided into sectors; each sector angle = (value ÷ total) × 360°. It shows parts of a whole (share of each dosage form in sales). Best with few categories.

**Line graph** — trend over time (plasma level–time curve, stability profile). **Scatter plot** — relation between two variables (Unit 1).

**Cubic graph (3D plot)** — a three-dimensional plot with three axes (two factors and the response, or three factors), often drawn as a cube for a 2³ factorial design with the response written at each corner. It shows how the response changes with all three factors at once.

```text
          bc ________ abc
           /|       /|
        c /_______ac |
          | |      | |
          | b______|_|ab
          | /      | /
       (1)|/_______|/ a
```

**Response surface plot** — a three-dimensional surface showing the predicted response (z-axis) against two factors (x and y axes), drawn from a fitted model. A peak or valley shows a maximum or minimum.

**Contour plot ("counter plot" in the syllabus)** — the two-dimensional view of a response surface seen from above; lines join combinations of the two factors that give the same response, like height lines on a map. Overlaying contour plots of several responses shows the region where all specifications are met (design space). Software such as Design-Expert and MINITAB draws these.

## 3.4 Designing the methodology

### 3.4.1 Sample size determination and power of a study

A study that is too small may miss a real effect (Type II error); one that is too large wastes money and exposes extra subjects. Sample size depends on:

- significance level α (usually 0.05) → zα/2 = 1.96;
- desired power 1 − β (80% → zβ = 0.84; 90% → zβ = 1.28);
- the smallest clinically important difference d;
- the variability (SD σ) or the expected proportions;
- design (paired, parallel), number of groups and expected drop-outs.

**Formulas**

| Situation | Formula |
| --- | --- |
| Estimating a mean within ±E | n = (zα/2 × σ ÷ E)² |
| Comparing two means (per group) | n = 2(zα/2 + zβ)² σ² ÷ d² |
| Comparing two proportions (per group) | n = (zα/2 + zβ)² [p1(1 − p1) + p2(1 − p2)] ÷ (p1 − p2)² |

**Worked example (example numbers).** A trial will compare a new antihypertensive with a standard. SD of fall in BP = 10 mm Hg; difference worth detecting = 5 mm Hg; α = 0.05; power 80%.

n = 2 × (1.96 + 0.84)² × 10² ÷ 5² = 2 × 7.84 × 100 ÷ 25 = **62.7 → 63 patients per group**. With 90% power, n = 2 × (1.96 + 1.28)² × 4 ≈ 84 per group. Adding about 10% for drop-outs gives the number to recruit.

**Power** rises with larger sample size, larger true difference, smaller variability and a larger α.

### 3.4.2 Report writing and presentation of data

**Structure of a research report or paper (IMRAD)**

1. Title, authors, affiliations
2. Abstract (background, methods, results, conclusion)
3. Introduction — problem, rationale, objectives
4. Materials and methods — design, subjects, procedures, statistics used
5. Results — tables, graphs, statistical values (mean ± SD, P values, confidence intervals)
6. Discussion — meaning, comparison with earlier work, limitations
7. Conclusion
8. Acknowledgements, references (a standard style such as Vancouver), appendices

**Good presentation:** number every table and figure, give titles and units, do not repeat the same data in a table and a graph, state the test used and the exact P value, give the sample size, and round sensibly. Reporting guidelines help: CONSORT for randomised trials, STROBE for observational studies.

### 3.4.3 Protocol

A **protocol** is the written plan of a study, approved before the study starts. For clinical trials it must be approved by an Ethics Committee and, where required, the regulator (CDSCO under the New Drugs and Clinical Trials Rules, 2019).

Contents: title, investigators and sites, background and rationale, objectives and hypothesis, study design (randomisation, blinding, controls), inclusion and exclusion criteria, sample size with its justification, treatments and dosing schedule, outcome measures (primary and secondary end points), study procedures and visit schedule, safety monitoring and adverse event reporting, statistical analysis plan, ethics and informed consent, data management and confidentiality, timelines, budget and references.

### 3.4.4 Types of studies

```text
Epidemiological / clinical studies
 ├── Observational (investigator only watches)
 │     ├── Descriptive : case report, case series, cross-sectional survey
 │     └── Analytical  : case–control (retrospective)
 │                        cohort (prospective or retrospective)
 └── Experimental / interventional (investigator assigns the treatment)
       ├── Randomised controlled trial (parallel, crossover)
       ├── Non-randomised controlled trial
       └── Community / field trials
```

**Observational studies** — the investigator does not give the exposure; people are observed as they are. Useful when an experiment would be unethical or impractical (effect of smoking).

- **Cross-sectional:** exposure and outcome measured at one time; gives prevalence.
- **Case–control:** start with people who have the disease (cases) and those without (controls), look back for past exposure; quick and cheap, good for rare diseases; gives the odds ratio; prone to recall bias.

**Cohort studies** — a group (cohort) free of the disease is classified by exposure and followed forward to see who develops it. Give incidence and **relative risk** (RR = incidence in exposed ÷ incidence in unexposed). Can study several outcomes; need large numbers and long follow-up; loss to follow-up is a problem. A retrospective (historical) cohort uses past records.

| Point | Case–control | Cohort |
| --- | --- | --- |
| Starts with | Outcome (disease) | Exposure |
| Direction | Backward | Forward |
| Measure | Odds ratio | Relative risk, incidence |
| Time and cost | Less | More |
| Best for | Rare diseases | Rare exposures |

**Experimental studies** — the investigator assigns the intervention, usually by randomisation, with a control group (placebo or standard drug) and blinding (single, double, triple) to reduce bias. The **randomised controlled trial (RCT)** gives the strongest evidence of cause and effect.

### 3.4.5 Designing a clinical trial and its phases

A **clinical trial** is a systematic study of a new drug in human subjects to find its pharmacological effects, efficacy and safety. Design points: clear objective and end points, choice of control, randomisation, blinding, parallel or crossover design, sample size, inclusion/exclusion criteria, ethics approval and written informed consent, following Good Clinical Practice (ICH E6 and the Indian GCP guidelines).

| Phase | Subjects | Number (typical) | Main aim |
| --- | --- | --- | --- |
| Phase 0 (exploratory, optional) | Healthy volunteers or patients | About 10–15 | Microdose pharmacokinetics, early go/no-go |
| Phase I (clinical pharmacology) | Healthy volunteers (patients for toxic drugs such as anticancer agents) | About 20–80 | Safety, tolerability, maximum tolerated dose, pharmacokinetics |
| Phase II (exploratory therapeutic) | Patients with the disease | About 100–300 | Efficacy, dose range, short-term safety |
| Phase III (confirmatory) | Larger patient groups, often multicentre | About 1,000–3,000 or more | Confirm efficacy and safety against standard or placebo; basis of marketing approval |
| Phase IV (post-marketing) | General patient population | Thousands | Long-term and rare adverse effects, new uses, pharmacovigilance |

The numbers are typical ranges and vary with the disease and drug.

## 3.5 Remember

- Non-parametric tests use ranks and need no normality: Mann–Whitney / Wilcoxon rank sum (2 independent), Wilcoxon signed rank (paired), Kruskal–Wallis (≥ 3 independent), Friedman (≥ 3 related).
- U = n1n2 + n1(n1 + 1)/2 − R1; H = 12/N(N + 1) × ΣR²/n − 3(N + 1); χr² = 12/bk(k + 1) × ΣR² − 3b(k + 1).
- χ² = Σ(O − E)²/E; E = row total × column total ÷ N; df = (r − 1)(c − 1); E ≥ 5 per cell.
- Fisher's principles: replication, randomisation, local control.
- Contour plot = top view of a response surface; cubic graph = 3D cube plot of a 2³ design.
- n per group = 2(zα/2 + zβ)²σ²/d²; zβ = 0.84 for 80% power.
- Cohort → relative risk, forward; case–control → odds ratio, backward; RCT = strongest evidence.
- Phases: 0 microdose, I safety/PK, II efficacy/dose, III confirmatory, IV post-marketing.
