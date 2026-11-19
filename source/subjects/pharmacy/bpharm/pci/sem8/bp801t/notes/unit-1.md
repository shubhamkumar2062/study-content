# Unit 1: Introduction, central tendency, dispersion and correlation

Every pharmacy decision rests on numbers that vary: tablet weights, assay results, blood pressure readings, cure rates. Statistics gives the tools to describe that variation, compare groups fairly and decide whether a difference is real or just chance. This unit builds the base: what statistics is, how data are arranged in a frequency distribution, how to find the "centre" of data (mean, median, mode), how spread out the data are (range, standard deviation) and how two variables move together (correlation).

All numbers in the worked examples below are **example numbers** made up for practice, not real product data.

## 1.1 Statistics and biostatistics

**Statistics** is the science of collecting, organising, presenting, analysing and interpreting numerical data so that sound conclusions can be drawn in the face of variation and uncertainty.

**Biostatistics** is statistics applied to biological, medical and pharmaceutical problems: clinical trials, bioequivalence, quality control of medicines, epidemiology and laboratory experiments.

**Two branches**

| Branch | What it does | Pharmacy example |
| --- | --- | --- |
| Descriptive statistics | Summarises data by tables, graphs, averages and spread | Mean weight and SD of 20 tablets |
| Inferential statistics | Draws conclusions about a population from a sample, with a stated risk of error | Is the new formulation's dissolution better than the old one? |

**Uses of biostatistics in pharmacy**

1. Quality control: weight variation, content uniformity, control charts, acceptance sampling of batches.
2. Formulation development: design of experiments and optimization of a formula.
3. Clinical trials: sample size, randomisation, comparing treatments, safety analysis.
4. Bioavailability and bioequivalence: comparing AUC and Cmax of test and reference products.
5. Pharmacology: dose–response curves, ED50 and LD50 estimation in animal studies.
6. Stability studies: regression of drug content against time to set the shelf life.
7. Analytical method validation: linearity (regression), precision (SD, RSD), accuracy.
8. Epidemiology and pharmacovigilance: rates of disease and adverse reactions.

**Limitations of statistics**

- It studies groups, not single individuals.
- Results are true only on average and only within stated chances of error.
- It can be misused: biased samples or wrong tests give misleading answers.
- It deals with data that can be expressed in numbers (or counted).

## 1.2 Basic terms

| Term | Meaning |
| --- | --- |
| Population | The whole group about which we want to conclude (all tablets of a batch) |
| Sample | A part of the population actually studied (20 tablets drawn from the batch) |
| Parameter | A value describing a population (population mean µ, SD σ) |
| Statistic | A value calculated from a sample (sample mean x̄, SD s) |
| Variable | A characteristic that changes from one unit to another |
| Observation | One recorded value of a variable |

**Types of data (variables)**

```text
Data
 ├── Qualitative (categorical)
 │     ├── Nominal  : names only, no order       (blood group, gender, brand)
 │     └── Ordinal  : ordered categories         (pain: mild / moderate / severe)
 └── Quantitative (numerical)
       ├── Discrete   : counts, whole numbers     (number of defective tablets)
       └── Continuous : any value in a range      (weight, temperature, plasma level)
```

Measurement scales: nominal, ordinal, interval (equal steps, no true zero, e.g. °C) and ratio (true zero, e.g. weight, concentration).

**Sources of data:** primary data are collected first-hand by the investigator (a trial, a survey); secondary data are taken from existing records (hospital records, published reports).

## 1.3 Frequency distribution

Raw data are hard to read. A **frequency distribution** groups the observations into classes and shows how many fall in each.

**Steps to form a grouped frequency distribution**

1. Find the range (largest − smallest value).
2. Decide the number of classes, usually 5 to 15. Sturges' rule gives a guide: k = 1 + 3.322 log10 N.
3. Class width h = range ÷ number of classes, rounded to a convenient value.
4. Write class limits so that every value fits in exactly one class (exclusive method: 0–2, 2–4, where the upper limit is not included).
5. Tally each observation and count the frequency.

**Useful terms**

| Term | Meaning |
| --- | --- |
| Class limits | Lowest and highest values of a class |
| Class mark (mid-point) | (lower limit + upper limit) ÷ 2 |
| Class width | Upper limit − lower limit |
| Relative frequency | Class frequency ÷ total frequency |
| Cumulative frequency (cf) | Frequency of a class plus all classes before it |

**Worked frame (example numbers): disintegration time of 30 tablets**

| Time (min) | Frequency f | Mid-point x | f × x | cf |
| --- | --- | --- | --- | --- |
| 0–2 | 3 | 1 | 3 | 3 |
| 2–4 | 7 | 3 | 21 | 10 |
| 4–6 | 12 | 5 | 60 | 22 |
| 6–8 | 6 | 7 | 42 | 28 |
| 8–10 | 2 | 9 | 18 | 30 |
| Total | N = 30 | | Σfx = 144 | |

This same table is used for the grouped mean, median and mode below.

## 1.4 Measures of central tendency

A measure of central tendency is a single value that represents the centre of a set of data. A good average is rigidly defined, easy to understand, based on all observations, not much affected by extreme values and suitable for further mathematical work.

### 1.4.1 Arithmetic mean

**Ungrouped data:** x̄ = Σx ÷ n

**Grouped data (direct method):** x̄ = Σfx ÷ N

**Assumed mean (short-cut) method:** x̄ = A + (Σfd ÷ N), where d = x − A; with step deviation, x̄ = A + (Σfd′ ÷ N) × h, where d′ = (x − A) ÷ h.

Properties: the sum of deviations from the mean is zero; the sum of squared deviations is least when taken from the mean; it uses every value but is pulled by extreme values.

**Worked example 1 (ungrouped, example numbers).** Weights (mg) of 10 tablets: 248, 252, 250, 249, 251, 250, 253, 247, 250, 255.

- Σx = 2505, so mean = 2505 ÷ 10 = **250.5 mg**.
- Arranged: 247, 248, 249, 250, 250, 250, 251, 252, 253, 255. With n even, median = average of 5th and 6th values = (250 + 250) ÷ 2 = **250 mg**.
- Mode = most frequent value = **250 mg** (occurs three times).

**Worked example 2 (grouped, from the table in 1.3).** Mean = Σfx ÷ N = 144 ÷ 30 = **4.8 min**.

### 1.4.2 Median

The median is the middle value when data are arranged in order; half the values lie below it and half above.

- Ungrouped: arrange in order; if n is odd, median = value at position (n + 1)/2; if n is even, average of the two middle values.
- Grouped: Median = L + [(N/2 − F) ÷ f] × h

where L = lower limit of the median class, N/2 locates the median class from the cf column, F = cf of the class before the median class, f = frequency of the median class, h = class width.

**Worked example (grouped).** N/2 = 15. The cf column first passes 15 in class 4–6 (cf 22). L = 4, F = 10, f = 12, h = 2.

Median = 4 + [(15 − 10) ÷ 12] × 2 = 4 + 0.833 = **4.83 min**.

The median is not affected by extreme values and suits skewed data (for example survival times, income) and ordinal data. It can also be read from an ogive (cumulative frequency curve).

### 1.4.3 Mode

The mode is the value that occurs most often.

Grouped data: Mode = L + [(f1 − f0) ÷ (2f1 − f0 − f2)] × h

where L = lower limit of the modal class (highest frequency), f1 = its frequency, f0 = frequency of the class before, f2 = frequency of the class after.

**Worked example (grouped).** Modal class 4–6: L = 4, f1 = 12, f0 = 7, f2 = 6, h = 2.

Mode = 4 + [(12 − 7) ÷ (24 − 7 − 6)] × 2 = 4 + (5 ÷ 11) × 2 = **4.91 min**.

**Empirical relation** (moderately skewed data): Mode ≈ 3 Median − 2 Mean = 3(4.833) − 2(4.8) = 4.90 min, which agrees closely.

A distribution may be unimodal, bimodal (two peaks, for example fast and slow acetylators) or multimodal. The mode is the only average that suits nominal data (most commonly prescribed brand).

### 1.4.4 Other means (brief)

- **Geometric mean (GM)** = nth root of the product of n values; used for ratios, growth rates, titres and log-normally distributed data such as AUC and Cmax in bioequivalence. Example: GM of 2 and 8 = √16 = 4.
- **Harmonic mean (HM)** = n ÷ Σ(1/x); used for averaging rates. Example: HM of 2 and 8 = 2 ÷ (0.5 + 0.125) = 3.2.
- For positive values: AM ≥ GM ≥ HM.

**Choosing the average**

| Situation | Best measure |
| --- | --- |
| Symmetrical numerical data | Mean |
| Skewed data or extreme values present | Median |
| Most common category or size | Mode |
| Ratios, log-normal data | Geometric mean |

## 1.5 Measures of dispersion

**Dispersion** is the extent to which values are scattered around the average. Two batches can have the same mean weight but very different spread; the one with less spread is more uniform. Absolute measures carry the unit of the data; relative measures are unit-free and allow comparison between different data sets.

### 1.5.1 Range

Range = largest value − smallest value. Coefficient of range = (L − S) ÷ (L + S).

Tablet example: range = 255 − 247 = **8 mg**. Simple and quick (used in control charts) but it depends only on two extreme values.

### 1.5.2 Quartile deviation and mean deviation

- Quartile deviation (semi-interquartile range) = (Q3 − Q1) ÷ 2; not affected by extreme values.
- Mean deviation = Σ|x − x̄| ÷ n. Tablet example: Σ|x − 250.5| = 18, so MD = **1.8 mg**.

### 1.5.3 Variance and standard deviation

**Standard deviation (SD)** is the square root of the mean of squared deviations from the mean. It is the most widely used measure of spread.

- Population SD: σ = √[Σ(x − µ)² ÷ N]
- Sample SD: s = √[Σ(x − x̄)² ÷ (n − 1)], using n − 1 (degrees of freedom) because the sample mean has already been estimated from the same data.
- Variance = SD².
- Computing form: Σ(x − x̄)² = Σx² − (Σx)²/n.
- Grouped data: s = √[Σf(x − x̄)² ÷ (N − 1)].

**Worked example (tablets, example numbers).** Mean = 250.5.

| x | 248 | 252 | 250 | 249 | 251 | 250 | 253 | 247 | 250 | 255 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x − x̄ | −2.5 | 1.5 | −0.5 | −1.5 | 0.5 | −0.5 | 2.5 | −3.5 | −0.5 | 4.5 |
| (x − x̄)² | 6.25 | 2.25 | 0.25 | 2.25 | 0.25 | 0.25 | 6.25 | 12.25 | 0.25 | 20.25 |

Σ(x − x̄)² = 50.5; variance s² = 50.5 ÷ 9 = 5.61; **s = 2.37 mg**.

**Coefficient of variation (CV) or relative standard deviation (RSD)** = (SD ÷ mean) × 100 = (2.37 ÷ 250.5) × 100 = **0.95%**. CV compares spread between data sets with different units or means; analytical precision is reported as % RSD.

**Grouped SD (from the disintegration table).** Σf(x − 4.8)² = 130.8, so s = √(130.8 ÷ 29) = **2.12 min**.

Properties of SD: always positive or zero; unchanged when a constant is added to every value; multiplied by k when every value is multiplied by k; for a normal distribution about 68%, 95% and 99.7% of values lie within ±1, ±2 and ±3 SD of the mean.

**Standard error of mean (SEM)** = SD ÷ √n. It measures the precision of the mean, not the spread of the data (detail in Unit 2).

### 1.5.4 Skewness and kurtosis (brief)

- **Skewness** describes lack of symmetry. Positive (right) skew: long tail to the right, mean > median > mode. Negative skew: mean < median < mode. Karl Pearson's coefficient = (mean − mode) ÷ SD.
- **Kurtosis** describes peakedness: leptokurtic (sharp peak), mesokurtic (normal), platykurtic (flat).

## 1.6 Correlation

**Correlation** measures the degree and direction of a linear relationship between two variables. It does not prove cause and effect.

**Types**

| Type | Meaning | Example |
| --- | --- | --- |
| Positive | Both rise together | Concentration and absorbance |
| Negative | One rises as the other falls | Drug content and storage time |
| Zero | No linear relationship | Tablet colour and hardness |
| Simple / multiple / partial | Two variables / one with several / two with others held constant | |
| Linear / non-linear | Constant / changing ratio of change | |

**Scatter diagram.** Plot pairs (x, y). A narrow upward band shows strong positive correlation; a round cloud shows none.

```text
 strong +ve         strong -ve          no correlation
 y |       .        y | .               y |  .   .  .
   |     .            |   .               | .  .   .
   |   .              |     .             |   .  .   .
   | .                |       .           | .   .  .
   +---------- x      +---------- x       +---------- x
```

### 1.6.1 Karl Pearson's coefficient of correlation (r)

r = Σ(x − x̄)(y − ȳ) ÷ √[Σ(x − x̄)² × Σ(y − ȳ)²]

Computing form: r = [nΣxy − ΣxΣy] ÷ √{[nΣx² − (Σx)²][nΣy² − (Σy)²]}

r lies between −1 and +1. r = +1: perfect positive; r = −1: perfect negative; r = 0: no linear relation. Rough guide: |r| above 0.7 strong, 0.4–0.7 moderate, below 0.4 weak. r² (coefficient of determination) gives the fraction of variation in y explained by x.

**Worked example (example numbers): calibration of a drug by UV**

| Conc x (µg/ml) | 2 | 4 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- |
| Absorbance y | 0.11 | 0.20 | 0.31 | 0.40 | 0.52 |

n = 5; Σx = 30; Σy = 1.54; Σxy = 11.28; Σx² = 220; Σy² = 0.5786.

- Sxy = Σxy − ΣxΣy/n = 11.28 − (30 × 1.54)/5 = 11.28 − 9.24 = 2.04
- Sxx = Σx² − (Σx)²/n = 220 − 180 = 40
- Syy = Σy² − (Σy)²/n = 0.5786 − 0.47432 = 0.10428

r = 2.04 ÷ √(40 × 0.10428) = 2.04 ÷ 2.0424 = **0.9988**; r² = 0.998. Almost perfect positive linear relation, as expected for Beer–Lambert behaviour.

Properties of r: independent of change of origin and scale; symmetrical (r of x with y = r of y with x); r is the geometric mean of the two regression coefficients (Unit 2).

### 1.6.2 Spearman's rank correlation (ρ)

Used for ranked (ordinal) data or when the data are not normal.

ρ = 1 − [6Σd² ÷ n(n² − 1)], where d = difference between the two ranks of each item.

**Worked example (example numbers).** Two panellists rank six flavoured syrups for taste.

| Syrup | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| Rank by panellist 1 | 1 | 2 | 3 | 4 | 5 | 6 |
| Rank by panellist 2 | 2 | 1 | 4 | 3 | 6 | 5 |
| d² | 1 | 1 | 1 | 1 | 1 | 1 |

Σd² = 6; ρ = 1 − (6 × 6) ÷ (6 × 35) = 1 − 0.171 = **0.83**, good agreement between panellists. For tied ranks, give each tied value the average of the ranks it would occupy.

**Pharmaceutical uses of correlation:** linearity of analytical methods, in vitro–in vivo correlation (IVIVC: dissolution versus absorption), relation between hardness and disintegration time, dose and response, lipophilicity and absorption.

## 1.7 Remember

- Biostatistics = statistics applied to biology, medicine and pharmacy; descriptive vs inferential.
- Mean = Σx/n; grouped median = L + [(N/2 − F)/f]h; grouped mode = L + [(f1 − f0)/(2f1 − f0 − f2)]h; Mode ≈ 3 Median − 2 Mean.
- Sample SD uses n − 1; CV (% RSD) = SD/mean × 100; SEM = SD/√n.
- About 68%, 95%, 99.7% of normal data lie within ±1, ±2, ±3 SD.
- r runs from −1 to +1; r² = fraction of variation explained; correlation is not causation.
- Spearman ρ = 1 − 6Σd²/n(n² − 1) for ranks.
