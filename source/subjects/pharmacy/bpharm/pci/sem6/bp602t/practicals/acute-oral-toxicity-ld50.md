# Determination of acute oral toxicity (LD50) of a drug from given data

**Aim:** To determine the median lethal dose (LD50) of a substance after oral administration from given data, and to describe the modern fixed-dose and up-and-down methods of acute toxicity testing.

> This exercise is worked from supplied data or simulation software; no animal is used. Acute toxicity studies in a laboratory follow OECD guidelines and need Institutional Animal Ethics Committee approval under CCSEA (earlier CPCSEA) rules.

## Principle

**Acute toxicity** is the harmful effect produced by a single exposure (or several within 24 hours), with the animals observed for 14 days. The classical measure is the **LD50** — the dose that kills 50 % of the animals. It is a statistical figure used to compare substances and to choose doses for later studies, not a measure of human risk by itself.

Because the classical LD50 test uses many animals, it has been replaced by methods that use far fewer, following the **3Rs** (replacement, reduction, refinement):

| Method | OECD guideline | Idea |
| --- | --- | --- |
| Fixed dose procedure | 420 | Fixed dose levels; the end point is clear toxicity, not death |
| Acute toxic class method | 423 | Stepwise, three animals per step; classifies into a toxicity class |
| Up-and-down procedure | 425 | One animal at a time; the next dose goes up or down with the result; estimates LD50 with few animals |

**Calculating LD50 from given data.** Two methods are commonly used in the exercise:

1. **Karber's method** — uses the mean of the dead in successive groups and the dose difference.

```text
 LD50 = LD100 - [ sum of (a x b) / n ]
  a = difference between two successive doses
  b = mean number of dead animals in those two groups
  n = number of animals in each group
```

2. **Graphical (log dose - probit) method** — plot the percentage mortality converted to **probit** against log dose; the dose at probit 5 (50 % mortality) is the LD50.

```text
 Probit
   6 |              *
   5 |---------*--------- 50% mortality
   4 |     *
     |________________________
          log dose    ^ LD50
```

## Requirements

Supplied mortality data, graph paper or a spreadsheet, probit table, calculator, OECD guideline summaries; or simulation software.

## Procedure

1. Tabulate the data: dose given to each group, number of animals per group and number that died.
2. Calculate the percentage mortality for each dose.
3. **Karber's method:** arrange doses in ascending order; for each pair of successive doses find *a* (dose difference) and *b* (mean of the dead in the two groups); multiply, add all the products, divide by *n*, and subtract from the dose causing 100 % mortality.
4. **Probit method:** convert each percentage mortality to its probit value from the table; plot probit against log dose; draw the best straight line; read the log dose at probit 5 and take its antilog to get the LD50.
5. Mention the confidence limits if the data allow.
6. State the toxicity class of the substance according to the classification used in your manual.

## Observations and calculation

**Given data (illustrative only, not real data).** 10 animals per group.

| Dose (mg/kg) | Deaths | % mortality | Probit |
| --- | --- | --- | --- |
| 100 | 0 | 0 | — |
| 200 | 2 | 20 | 4.16 |
| 400 | 5 | 50 | 5.00 |
| 800 | 8 | 80 | 5.84 |
| 1600 | 10 | 100 | — |

**Karber's method**

| Dose pair | a (dose difference) | b (mean dead) | a × b |
| --- | --- | --- | --- |
| 100–200 | 100 | (0+2)/2 = 1 | 100 |
| 200–400 | 200 | (2+5)/2 = 3.5 | 700 |
| 400–800 | 400 | (5+8)/2 = 6.5 | 2600 |
| 800–1600 | 800 | (8+10)/2 = 9 | 7200 |
| | | **Total** | **10600** |

LD50 = 1600 − (10600 ÷ 10) = 1600 − 1060 = **540 mg/kg**.

**Probit method:** plotting the probit values against log dose and reading at probit 5 gives a log dose of about 2.60, so LD50 = antilog 2.60 ≈ **400 mg/kg** for this data set. The two methods give figures of the same order; report the method used.

## Result

The LD50 of the given substance by the oral route was calculated as **540 mg/kg** by Karber's method and about **400 mg/kg** by the probit graphical method (specimen values from the supplied data).

## Precautions

1. Use the same number of animals in every group in the data set; Karber's formula assumes this.
2. Arrange the doses in ascending order before pairing them.
3. Keep units the same throughout (mg/kg).
4. Note that LD50 depends on species, strain, sex, age, route and the vehicle used, so always state them with the value.
5. Use logarithms of the doses, not the doses themselves, for the probit plot.
6. Remember that a single LD50 figure says nothing about chronic toxicity or about effects at low doses.
7. Prefer the OECD methods using fewer animals; the classical test is no longer recommended.

## Viva questions

1. **Define LD50.** The dose that kills 50 % of the test animals under stated conditions.
2. **Define ED50 and therapeutic index.** ED50 is the dose producing the desired effect in 50 % of animals; therapeutic index = LD50 ÷ ED50.
3. **Name the OECD methods that replaced the classical LD50 test.** Fixed dose procedure (420), acute toxic class method (423) and up-and-down procedure (425).
4. **What is a probit?** A transformation of percentage response into a normal equivalent deviate plus 5, which makes the dose–response curve a straight line.
5. **Why is log dose used?** Responses are proportional to the logarithm of the dose, so a log scale straightens the sigmoid curve.
6. **Which factors change the LD50 value?** Species, strain, sex, age, route of administration, vehicle, feeding state and environment.
7. **What are the 3Rs?** Replacement, reduction and refinement of animal use in research.
8. **Which body's approval is needed for animal experiments in India?** The Institutional Animal Ethics Committee, under CCSEA (formerly CPCSEA) rules.
9. **For how long are animals observed in an acute toxicity study?** 14 days after the single exposure.
