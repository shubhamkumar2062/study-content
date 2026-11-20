# Unit 1: Principles and Ethics of Bioassay

Experimental pharmacology uses living systems — isolated tissues, whole animals or even microorganisms — to measure the potency of a drug or biological substance. This unit covers the logic of bioassay, the statistical machinery behind it, and the ethical framework that governs work with animals.

## 1.1 Definition and concept of bioassay

A **bioassay** (biological assay) is a procedure that uses a living organism or its components to estimate the potency or concentration of a substance by comparing its effect with that of a reference standard. It is used when the substance is chemically undefined, structurally heterogeneous, or when its pharmacological activity cannot be predicted from its chemical composition alone.

**Advantages over chemical assay**
- Measures the actual biological activity, not just the chemical quantity present.
- Detects unknown impurities that alter biological effect but are chemically identical.
- Useful for heterogeneous mixtures such as insulin, digitalis or heparin.
- Required for substances whose structure is incompletely known.

**Limitations**
- Greater biological variability than a chemical measurement.
- Requires living systems that must be maintained under strict, standardised conditions.
- Results can vary with the species, age, sex, strain and physiological state of the animal or tissue.
- More expensive and time-consuming than physicochemical assays.
- Ethical constraints limit use of animals.

## 1.2 Types of bioassay by nature of the response

### Quantal (all-or-none) bioassay
The response is binary: either an event occurs or it does not. Examples: death or survival, convulsion or none, sleep or wakefulness, oedema or none. The endpoint is the **proportion of animals showing the response** at each dose. Because each animal gives only one piece of information (yes or no), larger group sizes are needed.

### Graded bioassay
The response is measured on a continuous scale: height of a muscle contraction, change in blood pressure in mmHg, change in heart rate. Each animal or tissue can receive several doses, and the **degree** of response is measured against dose. Graded assays are more efficient because one preparation gives multiple data points.

| Feature | Quantal | Graded |
| --- | --- | --- |
| Response measured | Proportion responding | Magnitude of response |
| Data per subject | One observation | Multiple observations |
| Statistical endpoint | ED50, LD50 | Relative potency, Emax |
| Example | Sleeping time test, LD50 | Muscle bath, blood pressure |

## 1.3 Standard preparations and working standards

A **standard preparation** (or reference standard) is a stable, well-characterised preparation of the substance, adopted by a regulatory authority, against which test preparations are compared. Its potency is defined in **International Units (IU)** or **Units**.

A **working standard** is a secondary standard prepared and calibrated against the international or national standard within a laboratory. It is used for daily assays to avoid depleting the reference standard.

**WHO International Biological Standards** are maintained by the WHO Expert Committee on Biological Standardisation. Examples include:
- 1st IRP for Insulin (defined as 1 IU = 41.67 μg).
- International Standard for Heparin.
- International Standards for vaccines, antibiotics, blood products and cytokines.

**Units of biological activity** are defined empirically for each substance: one Unit of insulin lowers blood glucose in a rabbit by a specified amount under defined conditions; one Unit of heparin prolongs the clotting time of sheep plasma under specified conditions. The numerical value of one Unit is arbitrary and historical.

## 1.4 Dose-response curves

### Log-dose vs response (semi-logarithmic plot)
When dose is plotted on a linear scale the relationship between dose and graded response is hyperbolic. When dose is replotted on a **logarithmic scale** the curve becomes sigmoidal (S-shaped), which has a linear region between about 20% and 80% of the maximum. This linear region is used for statistical analysis and for bioassay calculations.

### Emax model (rectangular hyperbola)
```text
Effect = Emax × [D] / (EC50 + [D])

Where:
  Emax = maximum achievable effect
  EC50 = concentration producing 50% of Emax
  [D]  = concentration of drug
```
This is a saturable, hyperbolic relationship. When [D] >> EC50 the effect approaches Emax; when [D] << EC50 the effect is proportional to [D] (linear pharmacology).

### Hill equation (sigmoidal Emax model)
```text
Effect = Emax × [D]^n / (EC50^n + [D]^n)

Where n = Hill coefficient (measure of cooperativity)
  n = 1 : simple hyperbola (Langmuir isotherm)
  n > 1 : sigmoidal, cooperativity (binding at one site facilitates the next)
  n < 1 : negative cooperativity
```

## 1.5 Methods of bioassay

### Matching assay (direct comparison method)
The unknown preparation is compared with the standard by finding doses of each that produce the **same response**. The response matched is typically mid-range (around 50% of Emax).

```text
Potency of unknown = (Dose of standard that matches) / (Dose of unknown that matches) × Potency of standard
```

Simple and quick; assumes linearity at the matched response level. Used where rapid results are needed and few data points are available.

### Interpolation assay
A calibration curve (log-dose vs response) is constructed with the standard. The response produced by an unknown dose is read off the curve to find the equivalent dose of standard. The potency of the unknown is then calculated from the ratio.

```text
If 10 units standard gives the same response as 0.5 mL unknown → 1 mL unknown = 20 units
```

### Bracketing assay (two-point, two-dose assay)
Two doses of standard (d1 and d2) **bracket** the response of the unknown. The relationship between log-dose and response is assumed to be linear in this range.

```text
Example:
  d1 (standard, 2 units) → response r1 = 20 mm
  d2 (standard, 4 units) → response r2 = 32 mm
  Unknown dose d_u    → response r_u = 26 mm
  By interpolation: log(potency) = log(d1) + (r_u - r1)/(r2 - r1) × (log d2 - log d1)
```

### Three-point assay
Uses three doses of standard (or two doses of standard and one of unknown) to construct the linear portion of the log-dose response curve. More precise than bracketing because it checks linearity. Commonly used for bioassay of acetylcholine on frog rectus abdominis.

### Four-point assay (parallel-line assay)
Two doses each of the **standard (S1, S2)** and the **unknown (U1, U2)** are used. Doses are chosen so that S1:S2 = U1:U2 (the same dose ratio). The two log-dose response lines must be **parallel** (a validity test) and must not cross. The horizontal distance between the two parallel lines is the **log-potency ratio** (M).

```text
Potency ratio R = antilog(M)
Potency of unknown = R × potency of standard per unit dose

Validity tests for a four-point parallel-line assay:
1. Parallelism: the two lines must be parallel (no significant slope difference).
2. Linearity: each line must be straight (no significant departure from linearity).
3. No significant difference in blank responses.
```

## 1.6 Statistical analysis

### ED50 and LD50 by probit analysis
For quantal data, the **probit** (probability unit) transformation converts sigmoidal cumulative frequency curves to straight lines.

```text
Probit = 5 + (z), where z is the z-score corresponding to the proportion responding
  Proportion 0.50 → probit 5.0
  Proportion 0.84 → probit 6.0
  Proportion 0.16 → probit 4.0
```
Probit vs log-dose gives a straight line. The log-dose corresponding to probit 5 (50% response) is the **ED50 (effective dose 50%)** or **LD50 (lethal dose 50%)**, depending on the endpoint.

### Moving averages method (Thompson 1947)
Used when the dose spacing is uniform on a log scale. The LD50 is estimated directly from the number of responses at each dose without full probit transformation. Simpler but less informative than probit analysis.

### Dixon and Mood method (up-and-down method)
Used when the number of animals is small. The first animal receives a dose near the expected LD50. If it survives, the next dose is raised by a fixed step; if it dies, the next dose is lowered. The LD50 is the geometric mean of doses at the transition points. Very economical in animal use.

## 1.7 Precision and validity

### Index of precision (λ)
```text
λ = s / b

Where:
  s = standard deviation of the log-dose response line about the regression
  b = slope of the line
```
A lower λ means a more precise assay. λ < 0.1 is excellent; λ > 0.2 is poor. Precision improves with more observations and a steeper, less variable response.

### Limits of error
The **fiducial limits** (confidence limits) of the estimated potency are calculated from the variance of the potency estimate. Typically the 95% fiducial limits are reported: the potency ratio lies within these limits with 95% probability.

### Validity tests for parallel-line assays
Four validity tests are assessed by analysis of variance (ANOVA) of the assay data:
1. **Preparations**: the two mean response levels (standard vs unknown) should not differ significantly from zero.
2. **Regression**: the slope (b) must be significant; a flat line gives no information.
3. **Parallelism**: the difference in slopes of the two lines must not be significant.
4. **Deviation from linearity (non-linearity)**: the response must not deviate significantly from a straight line.

If parallelism or linearity fail, the assay is invalid and must be redesigned.

## 1.8 Ethics in experimental pharmacology: the 3Rs

The 3Rs framework was proposed by Russell and Burch (1959) in "The Principles of Humane Experimental Technique" and is the foundation of modern animal ethics in research.

### Replacement
Finding methods that **avoid or replace** the use of animals. Full replacement substitutes cell culture, computer models, organ-on-a-chip, in-silico pharmacokinetic models or physicochemical tests for the animal. Partial replacement uses lower organisms (insects, fish larvae) instead of mammals.

Examples: Limulus amoebocyte lysate (LAL) test replaced the rabbit pyrogen test; human cell-based assays replaced animal bioassays for many cytokines; QSAR models predict toxicity without animals.

### Reduction
Using **fewer animals** to obtain the same quality of information. Strategies include better statistical design (fewer but informative group sizes), sharing tissues and control groups between studies, using in-vitro data to narrow the dose range before in-vivo work, and systematic reviews to avoid repeating experiments.

### Refinement
Modifying procedures to **minimise pain, suffering, distress and lasting harm** in animals that must still be used. Examples: use of local anaesthesia or analgesia, the choice of less invasive routes of administration, training animals to cooperate with procedures, use of humane endpoints, environmental enrichment, and housing in compatible social groups.

## 1.9 CPCSEA guidelines (India)

The **Committee for the Purpose of Control and Supervision of Experiments on Animals (CPCSEA)** operates under the Prevention of Cruelty to Animals Act, 1960.

**Key requirements:**
- Every institution using animals must register with CPCSEA.
- An **Institutional Animal Ethics Committee (IAEC)** must be constituted. It must include a veterinarian, a scientist in charge of animal care, a biological scientist, a scientist using animals, a nominee of the institutional head, and two nominees from CPCSEA (one of whom must be a person concerned with animal welfare outside the institution).
- All protocols involving animals must be reviewed and approved by the IAEC before the work begins.
- Animals must be housed in species-appropriate facilities with adequate space, bedding, environmental enrichment, food, water and a 12:12 light-dark cycle.
- Transport, procurement and anaesthesia must comply with prescribed standards.
- A veterinarian must be available to the facility.

**Humane endpoints** are criteria that allow early termination of a study when the animal shows signs of severe pain, distress or moribund condition, before death occurs. Examples: weight loss exceeding 20%, laboured breathing, inability to reach food or water, persistent prostration. Using humane endpoints is both more ethical and scientifically more informative than death as the endpoint.

## 1.10 Species and strain selection

The choice of animal for a pharmacological experiment depends on:
- **Pharmacological appropriateness**: the target organ, receptor or pathway must be present and functional in the species. For example, guinea pigs show strong bronchoconstriction with histamine (H1 receptors in bronchial muscle), making them suitable for anti-asthmatic screening; rats are preferred for cardiovascular work.
- **Body weight and size**: larger animals provide more tissue and blood but are more expensive and require larger doses.
- **Breeding history**: inbred strains are genetically homogeneous and reduce biological variability (Wistar and Sprague-Dawley rats, Swiss albino and C57BL/6 mice). Outbred stocks are more representative of human genetic diversity.
- **Regulatory requirements**: ICH guidelines specify species for toxicity studies.

## 1.11 Randomisation and blinding

**Randomisation** assigns animals to treatment groups by a random process (random number tables, computer-generated sequences), so that systematic bias in group allocation is eliminated. All known and unknown confounding factors are, on average, balanced between groups.

**Blinding** (masking) prevents the investigator from knowing which treatment a specific animal has received, which removes unconscious measurement bias. Single blinding is when the animal handler does not know the treatment; double blinding is when both the handler and the person scoring the results do not know.

## 1.12 Study design considerations

**Parallel design**: each animal receives one treatment only. Groups of animals are run simultaneously. Variability comes from between-animal differences. Requires more animals but is preferred when treatments have long carry-over effects.

**Crossover design**: each animal receives every treatment in sequence, acting as its own control. Variability is reduced because between-animal differences cancel out. Requires fewer animals. Valid only when treatments do not permanently alter the animal and when washout periods between treatments are adequate.

**Latin square design**: a crossover design for multiple treatments and multiple periods, balanced so that each treatment appears once in each row (animal) and each column (period). Removes both animal-to-animal and period-to-period variation from the error term.

```text
Latin square example (3 treatments: S, U, V; 3 periods; 3 animals):
         Period 1    Period 2    Period 3
Animal 1    S           U           V
Animal 2    U           V           S
Animal 3    V           S           U
```

## Remember

1. Bioassay measures biological activity by comparison with a standard; it is used when chemistry alone cannot determine potency.
2. Quantal assays count the proportion showing an all-or-none response; graded assays measure the magnitude on a continuous scale.
3. The log-dose vs response curve is linear between 20% and 80% of maximum; this linear region is used for calculations.
4. Four-point parallel-line assay uses two doses each of standard and unknown; validity requires parallelism and linearity.
5. Probit 5.0 = 50% response = ED50 or LD50; probit analysis converts the sigmoidal quantal curve to a straight line.
6. Index of precision λ = s/b; lower is better; λ < 0.1 is excellent.
7. 3Rs: Replacement = no animals at all; Reduction = fewer animals; Refinement = less suffering.
8. CPCSEA requires institutional registration and an IAEC that approves every protocol before work begins.
9. Use humane endpoints; never use death as the routine endpoint when alternatives exist.
10. Randomisation removes allocation bias; blinding removes measurement bias.
