# Unit 2: Quantitative structure activity relationship (QSAR)

SAR tells you *that* a change in structure changes activity. QSAR puts a number on it: it builds a mathematical equation linking measurable properties of a series of molecules to their biological activity, so that the activity of a molecule nobody has made yet can be predicted. This is the oldest and still the most examined part of computer aided drug design.

## 2.1 SAR versus QSAR

| Point | SAR | QSAR |
| --- | --- | --- |
| Nature | Qualitative | Quantitative |
| Statement | "Adding a chlorine increases activity" | "log(1/C) = 0.87 π + 1.09 σ + 4.19" |
| Based on | Observation, chemical intuition | Statistics (regression) on measured descriptors |
| Needs | A few analogs | A congeneric series, usually 15–20 or more compounds |
| Output | Which groups matter | Predicted activity of untested analogs, with error estimates |
| Risk | Over-generalising from a few compounds | A model that fits the training set but does not predict (over-fitting) |

**Biological activity in QSAR** is always expressed as the logarithm of the reciprocal of the concentration producing a fixed effect: log(1/C), where C is a molar concentration such as IC50, ED50, MIC or Ki. Three reasons: the response is usually log-linear with concentration; a log scale relates directly to free energy of binding (ΔG° = −2.303RT log K); and the reciprocal makes the more potent compound give the larger number.

## 2.2 History and development

| Period | Contribution |
| --- | --- |
| 1860s | Crum-Brown and Fraser: physiological action is a function of chemical constitution, Φ = f(C) |
| 1890s–1900s | Meyer and Overton: narcotic potency of simple organic compounds parallels their oil/water partition coefficient |
| 1930s | Hammett: electronic substituent constant σ and reaction constant ρ for benzene derivatives |
| 1950s | Taft: steric substituent constant Es from ester hydrolysis rates |
| 1964 | Hansch and Fujita: the linear free energy related model combining lipophilic, electronic and steric terms |
| 1964 | Free and Wilson: the additive group-contribution (de novo) model |
| 1970s–80s | Kier and Hall molecular connectivity indices; Topliss decision tree; Craig plots |
| 1988 onwards | 3D-QSAR: CoMFA (Cramer), later CoMSIA (Klebe) |
| Present | Many descriptors, machine learning models, strict external validation |

## 2.3 Types of physicochemical parameters (descriptors)

A **descriptor** is any number that describes part of a molecule's structure or behaviour. The three classical families are lipophilic, electronic and steric.

| Family | Parameter | Symbol | Measures |
| --- | --- | --- | --- |
| Lipophilic | Partition coefficient, its logarithm | P, log P | How the molecule shares itself between octanol and water |
| Lipophilic | Substituent lipophilicity constant | π | Lipophilicity contributed by one group |
| Lipophilic | Distribution coefficient | log D | Partition at a stated pH, counting the ionised form |
| Electronic | Hammett constant | σ (σm, σp) | Electron withdrawal or donation through the ring |
| Electronic | Taft polar constant | σ* | Electronic effect in aliphatic systems |
| Electronic | Ionisation constant, dipole moment, HOMO/LUMO energies, partial charges | pKa, μ, E | Charge distribution and reactivity |
| Steric | Taft steric constant | Es | Bulk of a substituent |
| Steric | Molar refractivity | MR | Volume plus polarisability |
| Steric | Verloop STERIMOL parameters | L, B1–B5 | Length and widths in defined directions |
| Steric | Molecular weight, molar volume, surface area | MW, MV, SA | Overall size |
| Topological | Connectivity index, Wiener index, Balaban index | χ, W, J | Branching and shape from the graph of the molecule |
| Others | Hydrogen bond donor/acceptor count, number of rotatable bonds, polar surface area | HBD, HBA, nRB, PSA | Drug-likeness and transport |

### Partition coefficient

P = concentration of the drug in octanol ÷ concentration in water, measured on the **un-ionised** molecule at equilibrium.

- **Experimental determination:** shake-flask method — shake a known amount of drug with equal volumes of water-saturated n-octanol and octanol-saturated water at a fixed temperature, separate, assay both layers (UV, HPLC), take the ratio. Variants: HPLC retention method (log k′ on a C18 column correlates with log P), counter-current and potentiometric titration methods.
- **Theoretical determination:** add fragment or atom contributions — Rekker's fragmental method (log P = Σ f) and the Hansch–Leo method, Crippen's atom-based method. Software gives ClogP (calculated) against measured log P.
- **π (pi) constant:** π_X = log P(R–X) − log P(R–H). A positive π means the group adds lipophilicity (Cl 0.71, CH3 0.56, t-butyl 1.98, CF3 0.88, Br 0.86), a negative π means it adds polarity (OH −0.67, NH2 −1.23, CONH2 −1.49). π values are additive within the same aromatic system, so log P of a new analog can be estimated from the parent.

### Hammett substituent constant

σ_X = log K_X − log K_H, defined from the ionisation of substituted benzoic acids in water at 25 °C.

- Positive σ = electron withdrawing (NO2 para 0.78, CN 0.66, CF3 0.54, Cl 0.23); negative σ = electron donating (OCH3 para −0.27, CH3 −0.17, OH −0.37, NH2 −0.66).
- σm and σp differ because meta groups act mainly by induction while para groups also act by resonance.
- **Hammett equation:** log(K_X/K_H) = ρσ, or log(k_X/k_H) = ρσ for rate constants. ρ (rho) is the reaction constant: it is 1.00 for benzoic acid ionisation by definition; a large positive ρ means the reaction is helped by electron withdrawal.
- Limitation: it applies to aromatic (and some unsaturated) systems only, not to ortho substituents, where steric effects intrude.

### Taft steric constant

Taft separated the mixed effects in aliphatic ester hydrolysis. Using the fact that acid-catalysed hydrolysis is mostly steric and base-catalysed hydrolysis has both steric and electronic components:

- Es = log(k_X/k_CH3) from **acid**-catalysed hydrolysis — a pure steric term; CH3 is the reference at 0, and bulkier groups give more negative Es (H +1.24, CH3 0.00, C2H5 −0.07, i-Pr −0.47, t-Bu −1.54).
- σ* = (1/2.48)[log(k_X/k_CH3)base − log(k_X/k_CH3)acid] — the polar (electronic) term for aliphatic systems.

**Molar refractivity** MR = [(n² − 1)/(n² + 2)] × (MW/d), where n is the refractive index and d the density. It combines volume and polarisability and is widely used when a substituent fits into a polar pocket.

## 2.4 Hansch analysis (the linear free energy related model)

Hansch assumed that drug action occurs in two steps — random walk to the site (controlled by lipophilicity) and binding at the site (controlled by electronic and steric fit) — and that their free energy contributions add up:

```text
log(1/C) = k1 (log P)  + k2 (sigma) + k3 (Es) + k4        (linear form)

log(1/C) = -k1 (log P)^2 + k2 (log P) + k3 (sigma) + k4   (parabolic form)
```

- Use π in place of log P when all compounds come from the same parent.
- The **parabolic** form is used when activity first rises and then falls with lipophilicity. Too polar and the drug never crosses the membrane; too lipophilic and it is trapped in fat or in the first membrane it meets.
- **Optimum lipophilicity:** differentiate and set to zero → log P₀ = k2 ÷ (2k1) for the equation written as log(1/C) = −k1(log P)² + k2 log P + …
- Bilinear model (Kubinyi): log(1/C) = a log P − b log(βP + 1) + c, which fits a sharper peak than a parabola.

### Judging a Hansch equation

| Statistic | Meaning | What is good |
| --- | --- | --- |
| n | Number of compounds | At least 5 compounds per descriptor |
| r or r² | Correlation coefficient | r > 0.9, r² > 0.8 |
| s | Standard error of the estimate | As small as possible, near the experimental error |
| F | Fisher's test of significance | Large; compare with table value |
| q² (cross-validated r²) | Predictive ability by leave-one-out | q² > 0.5 |

### Worked example (teaching data, not from a real series)

Six para-substituted analogs of one parent were tested. π and σ are the standard literature substituent values; the activities below are invented for practice.

| Substituent | π | σp | log(1/C) observed | log(1/C) calculated | Residual |
| --- | --- | --- | --- | --- | --- |
| H | 0.00 | 0.00 | 4.23 | 4.19 | +0.04 |
| CH3 | 0.56 | −0.17 | 4.45 | 4.49 | −0.04 |
| Cl | 0.71 | 0.23 | 5.08 | 5.06 | +0.02 |
| CF3 | 0.88 | 0.54 | 5.52 | 5.54 | −0.02 |
| t-Bu | 1.98 | −0.20 | 5.71 | 5.70 | +0.01 |
| OH | −0.67 | −0.37 | 3.19 | 3.20 | −0.01 |

Multiple linear regression on this set gives

```text
log(1/C) = 0.873 (pi) + 1.090 (sigma) + 4.188
n = 6    r = 0.999    r^2 = 0.999    s = 0.040    F = 1374
```

**Reading the equation:** both coefficients are positive, so activity rises with lipophilicity and with electron withdrawal; the σ coefficient is larger than the π coefficient, so electronic effects dominate here. There is no squared term, so within this narrow π range (−0.67 to 1.98) no optimum has been reached.

**Prediction:** for a bromo analog (π = 0.86, σp = 0.23) the equation predicts log(1/C) = 0.873(0.86) + 1.090(0.23) + 4.188 = **5.19**, so bromo should be a little more active than chloro. That compound is then made and tested — prediction, synthesis, test, re-fit is the QSAR cycle.

### Worked example of the parabolic form

Suppose a series gives log(1/C) = −0.35(log P)² + 1.60 log P + 3.20.

Optimum log P₀ = 1.60 ÷ (2 × 0.35) = **2.29**, and the maximum activity is −0.35(2.29)² + 1.60(2.29) + 3.20 = **5.03**. At log P = 1.0 the predicted activity is 4.45 and at log P = 4.0 it falls to 4.00. The parabola is symmetrical about log P₀, but real data often rise and fall at different rates on the two sides of the optimum, which is why Kubinyi's bilinear model is sometimes preferred.

## 2.5 Free–Wilson analysis (de novo or additive model)

Free and Wilson assumed that each substituent at each position makes a **constant, additive contribution** to the activity, independent of the rest of the molecule:

```text
BA = mu + sum(a_i * X_i)

BA  = biological activity, usually log(1/C)
mu  = activity of the unsubstituted parent (the reference)
a_i = contribution of substituent i at a particular position
X_i = 1 if that substituent is present at that position, otherwise 0
```

A matrix of 1s and 0s is built (an indicator variable for every substituent at every position) and solved by multiple regression.

### Worked example (teaching data)

Two positions were varied: R1 = H, Cl or OCH3 and R2 = H or CH3. Taking the all-hydrogen parent as the reference, μ = 4.10, and the fitted group contributions are a(Cl) = +0.68, a(OCH3) = +0.32 at R1 and a(CH3) = +0.36 at R2.

| R1 | R2 | Calculated log(1/C) |
| --- | --- | --- |
| H | H | 4.10 |
| Cl | H | 4.78 |
| OCH3 | H | 4.42 |
| H | CH3 | 4.46 |
| Cl | CH3 | 5.14 |
| OCH3 | CH3 | 4.78 |

A compound never made, with Cl at R1 and CH3 at R2, would be predicted as 4.10 + 0.68 + 0.36 = 5.14 — the best of the set, so it is the one to synthesise. (This teaching set is perfectly additive, so the residuals are zero; real data always show scatter.)

### Hansch versus Free–Wilson

| Point | Hansch | Free–Wilson |
| --- | --- | --- |
| Basis | Measured physicochemical parameters | Indicator variables for groups |
| Needs parameter values? | Yes, π, σ, Es must be known | No, only the activity data |
| Extrapolation | Can predict a substituent never used, if its π and σ are known | Cannot predict a substituent absent from the training set |
| Interpretation | Tells you *why* (lipophilic, electronic, steric) | Tells you only *how much* each group adds |
| Number of compounds | Fewer needed | Many needed, each substituent must appear several times |
| Non-linear effects | Handled by the squared or bilinear term | Cannot be handled; assumes strict additivity |

The **mixed (Fujita–Ban) approach** combines both: physicochemical terms for the properties that can be measured, indicator variables for the features that cannot.

### Limitations common to both (2D-QSAR)

1. The series must be **congeneric** — one scaffold, one mechanism and one binding mode.
2. Descriptors must be spread out and not correlated with each other (collinearity gives unstable coefficients).
3. Too many descriptors on too few compounds gives chance correlation; keep the ratio of compounds to descriptors at 5:1 or better.
4. Predictions are valid only inside the range of the training data (the "domain of applicability").
5. No three-dimensional information, so stereochemistry and shape are poorly represented. That is what 3D-QSAR was built to fix.

## 2.6 3D-QSAR: CoMFA and CoMSIA

**CoMFA (Comparative Molecular Field Analysis)** relates activity to the **fields** that surround each molecule rather than to single numbers.

Steps:

```text
1. Collect a series with measured activity; build 3D structures.
2. Find the bioactive conformation of each molecule (docking or the most active analog).
3. ALIGN all molecules on a common core - the single most critical step.
4. Put the aligned set in a 3D grid (typically 2 A spacing).
5. At every grid point calculate the interaction with a probe atom
   (sp3 carbon, +1 charge): steric field (Lennard-Jones) and
   electrostatic field (Coulomb). Cut off very large values.
6. Thousands of field values per molecule -> PLS (partial least squares)
   reduces them to a few components; leave-one-out cross-validation gives q^2.
7. Display the result as coloured contour maps around the molecules.
```

**Reading CoMFA maps:** green contours show where more bulk raises activity, yellow where bulk lowers it; blue shows where positive charge (electron-poor groups) helps and red where negative charge helps. The chemist designs the next analog by filling the green and blue regions and avoiding the yellow ones.

**CoMSIA (Comparative Molecular Similarity Indices Analysis)** is the refinement:

| Point | CoMFA | CoMSIA |
| --- | --- | --- |
| Fields used | Steric and electrostatic (hydrophobic and H-bond fields can be added) | Five: steric, electrostatic, hydrophobic, hydrogen bond donor, hydrogen bond acceptor |
| Function | Lennard-Jones and Coulomb potentials | Gaussian-type similarity function |
| Behaviour near the atom | Values rise steeply, so cut-offs are needed | Smooth, no singularity, no cut-offs required |
| Maps | Sometimes fragmented, can lie away from the molecule | Smoother, easier to read, lie closer to the molecule |
| Grid sensitivity | More sensitive to grid spacing and orientation | Less sensitive |

Both are validated by q² (leave-one-out), by an external test set, and by y-randomisation (scramble the activities; a genuine model should then collapse).

**Main limitation of 3D-QSAR:** the result depends completely on the alignment and on the conformation chosen. A different, equally reasonable alignment can give a different model.

## 2.7 Validation of any QSAR model

1. **Internal:** leave-one-out or leave-many-out cross-validation (q² > 0.5), bootstrapping.
2. **External:** keep a test set aside (about 20–25 % of compounds) and check the predicted r² (r²pred > 0.6).
3. **Y-randomisation:** shuffle the activity column and refit many times; the scrambled models must be clearly worse.
4. **Applicability domain:** only predict compounds whose descriptors lie inside the training range.
5. Report n, r², s, F and q² with every equation. An equation without statistics is not a QSAR.

## Remember

1. Activity is always log(1/C); C is molar (IC50, ED50, MIC).
2. π_X = log P(RX) − log P(RH); σ_X = log K_X − log K_H for benzoic acids; Es from acid-catalysed ester hydrolysis (CH3 = 0, bigger group = more negative).
3. Hammett equation log(k_X/k_H) = ρσ; ρ = 1.00 for benzoic acid ionisation.
4. Hansch: log(1/C) = −k1(log P)² + k2 log P + k3σ + k4Es + k5; optimum log P₀ = k2/(2k1).
5. Free–Wilson: BA = μ + Σ aᵢXᵢ, additive group contributions, cannot extrapolate to a new substituent.
6. Statistics to quote: n, r (or r²), s, F, q². Rule of thumb — at least five compounds per descriptor.
7. CoMFA = steric + electrostatic fields, Lennard-Jones and Coulomb, PLS, green/yellow and blue/red contours. CoMSIA = five Gaussian similarity fields, smoother maps, no cut-offs.
8. The weakest point of 3D-QSAR is molecular alignment; the weakest point of 2D-QSAR is the need for a congeneric series.
