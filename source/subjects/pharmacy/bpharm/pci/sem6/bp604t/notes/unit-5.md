# Unit 5: Nonlinear pharmacokinetics

Everything in Units 3 and 4 assumed **linear** (first-order) kinetics: double the dose and you double the plasma level and the AUC, while the half-life stays the same. For some drugs this breaks down at therapeutic doses because a process in the body becomes **saturated**. This unit explains why it happens, how to recognise it, and how the Michaelis–Menten equation is used to estimate the parameters. Numbers in the worked examples are **example numbers** for a hypothetical drug.

## 5.1 Introduction

**Linear (dose-independent) pharmacokinetics**

- All rate processes are first order.
- t½, KE, Vd and CL do not change with dose.
- Plasma levels and AUC are directly proportional to dose (dose-normalised curves superimpose).
- The principle of superposition holds.

**Nonlinear (dose-dependent, capacity-limited or saturation) pharmacokinetics**

- One or more processes (absorption, distribution, metabolism, excretion) has a limited capacity — enzymes, carriers or binding sites can be saturated.
- Parameters change with dose or concentration.
- AUC and steady-state levels are **not proportional** to dose: a small increase in dose can cause a large rise in level (when elimination saturates) or a smaller-than-expected rise (when absorption or binding saturates).

```text
 AUC                         elimination saturates
  │                        /  (more than proportional)
  │                      /
  │                 ___/____ linear (proportional)
  │            ___/
  │      ___/'''''''''''''' absorption saturates
  │ ___/                     (less than proportional)
  └──────────────────────────── Dose
```

## 5.2 Tests (signs) of nonlinearity

1. AUC or Css divided by dose is not constant across doses.
2. t½ (or KE) changes when the dose changes.
3. Log C vs t plot after a large dose is curved (concave down at first — slow fall while saturated, faster fall when levels drop).
4. Fraction excreted unchanged in urine, or the ratio of metabolites, changes with dose.
5. Competitive effects: another drug using the same enzyme or carrier changes the kinetics.
6. Time-dependent changes on repeated dosing (auto-induction).

## 5.3 Factors (causes) of nonlinearity

| ADME process | Cause of nonlinearity | Effect on AUC with rising dose | Drug examples |
| --- | --- | --- | --- |
| **Absorption** | Saturable carrier-mediated absorption | Less than proportional | Riboflavin, ascorbic acid (vitamin C), gabapentin |
| | Poor solubility / slow dissolution at high doses | Less than proportional | Griseofulvin |
| | Saturable gut-wall or hepatic first-pass metabolism | More than proportional | Propranolol, hydralazine, verapamil |
| | Saturable efflux (P-gp) in the gut | More than proportional | Some P-gp substrates |
| **Distribution** | Saturation of plasma protein binding | Total AUC less than proportional (free fraction rises) | Phenylbutazone, naproxen, valproic acid, disopyramide |
| | Saturation of tissue binding | Vd changes with dose | Thiopental |
| **Metabolism** | Saturation of metabolising enzymes (capacity-limited) | More than proportional; t½ rises | Phenytoin, ethanol, salicylates at high doses, theophylline at high levels |
| | Cofactor depletion | More than proportional | Paracetamol (glutathione, sulfate depleted in overdose) |
| | Enzyme induction (auto-induction) | Levels fall with time | Carbamazepine |
| **Excretion** | Saturation of active tubular secretion | More than proportional | Penicillin G, PAH |
| | Saturation of active tubular reabsorption | Less than proportional (more excreted) | Ascorbic acid, riboflavin |
| | Forced diuresis, change of urine pH | Variable | Salicylic acid, theophylline |
| | Saturation of biliary secretion | More than proportional | Iodipamide |
| | Nephrotoxicity at high dose | More than proportional | Aminoglycosides |

## 5.4 The Michaelis–Menten equation

When elimination is by an enzyme (or carrier) of limited capacity, the rate of elimination follows **Michaelis–Menten kinetics**:

−dC/dt = Vmax C / (Km + C)

- **Vmax** — maximum rate of elimination (amount or concentration per unit time) when the enzyme is fully saturated.
- **Km** — Michaelis constant: the concentration at which the rate is half of Vmax. A low Km means the enzyme saturates easily.

**Three situations**

| Condition | Simplified equation | Kinetics |
| --- | --- | --- |
| C much smaller than Km | −dC/dt = (Vmax/Km) C | **First order** (KE = Vmax/Km) |
| C much greater than Km | −dC/dt = Vmax | **Zero order** (constant amount per unit time) |
| C close to Km | Full equation | **Mixed order** |

```text
 Rate of
 elimination
  │            ___________________ Vmax
  │        .-''
  │      .'
  │ Vmax/2 ┼
  │    /  │
  │   /   │
  │  /    │
  │ /     │
  └───────┴───────────────── C
         Km
```

**Clearance and half-life change with concentration**

CL = Vmax / (Km + C)   (if Vmax is in amount per time) — so CL falls as C rises.

t½ = 0.693 Vd (Km + C) / Vmax — so t½ rises as C rises.

**Worked example 1 — how t½ grows with level (example numbers).** Hypothetical drug: Vmax = 500 mg/day, Km = 4 mg/L, Vd = 50 L.

| C (mg/L) | Elimination rate = Vmax C/(Km + C) (mg/day) | CL = rate/C (L/day) | t½ = 0.693 Vd / CL |
| --- | --- | --- | --- |
| 1 | 100 | 100 | 8.3 h |
| 4 (= Km) | 250 (= Vmax/2) | 62.5 | 13.3 h |
| 10 | 357 | 35.7 | 23.3 h |
| 20 | 417 | 20.8 | 39.9 h |

The higher the level, the longer the half-life — so steady state also takes longer to reach at higher doses.

## 5.5 Steady state with Michaelis–Menten elimination

At steady state, the dosing rate R (amount per day, corrected for F) equals the elimination rate:

R = Vmax Css / (Km + Css)     →     Css = Km R / (Vmax − R)

Important points:

- When R approaches Vmax, Css rises very steeply; if R ≥ Vmax, no steady state is reached and the drug keeps accumulating.
- Small dose increases can produce large, toxic rises in level.

**Worked example 2 — disproportionate rise (example numbers).** Same drug, Vmax = 500 mg/day, Km = 4 mg/L.

| Dosing rate R (mg/day) | Css = Km R/(Vmax − R) (mg/L) |
| --- | --- |
| 200 | 2.67 |
| 300 | 6.00 |
| 350 | 9.33 |
| 400 | 16.0 |
| 450 | 36.0 |

Raising the dose from 300 to 400 mg/day (by one-third, ×1.33) raises Css from 6 to 16 mg/L (×2.67). For a linear drug the level would rise only by one-third.

## 5.6 Estimation of Km and Vmax

### A. From the plasma decline after a single IV dose

Measure the rate of fall (−ΔC/Δt) at different average concentrations, then use a linear form of the Michaelis–Menten equation:

| Plot | Equation | Axes | Slope | Intercept |
| --- | --- | --- | --- | --- |
| Lineweaver–Burk (double reciprocal) | 1/v = Km/(Vmax C) + 1/Vmax | 1/v vs 1/C | Km/Vmax | 1/Vmax |
| Hanes–Woolf | C/v = C/Vmax + Km/Vmax | C/v vs C | 1/Vmax | Km/Vmax |
| Eadie–Hofstee | v = Vmax − Km (v/C) | v vs v/C | −Km | Vmax |

(v = rate of elimination.) The Lineweaver–Burk plot gives too much weight to low-concentration points; Hanes–Woolf and Eadie–Hofstee spread the points more evenly.

**From the terminal phase of a log C plot:** at low levels the curve becomes linear with slope −Vmax/(2.303 Km); extrapolating this line back and comparing it with the early zero-order part also gives Km and Vmax (the graphical method of Wagner).

### B. From steady-state data (clinical method)

The patient receives two (or more) dosing rates, each until steady state, and Css is measured.

1. **Rearranged equation (R vs R/Css plot):** R = Vmax − Km (R/Css). Plot R on the y-axis against R/Css: slope = −Km, y-intercept = Vmax.
2. **Direct linear plot (Mullen):** on the x-axis mark −Css values, on the y-axis the matching R values; draw a line through each pair. The lines meet at a point whose x-coordinate is Km and y-coordinate is Vmax. No calculation needed.
3. **Lineweaver–Burk:** 1/R = Km/(Vmax Css) + 1/Vmax; plot 1/R vs 1/Css.

**Worked example 3 — Km and Vmax from two steady states (example numbers).** A patient's steady-state levels are 6 mg/L on 300 mg/day and 16 mg/L on 400 mg/day (F taken as 1).

| R (mg/day) | Css (mg/L) | R/Css (L/day) |
| --- | --- | --- |
| 300 | 6 | 50 |
| 400 | 16 | 25 |

- Slope = (400 − 300)/(25 − 50) = −4 → **Km = 4 mg/L**.
- Vmax = R + Km × R/Css = 300 + 4 × 50 = **500 mg/day**.
- Check with Lineweaver–Burk: 1/R vs 1/Css has slope 0.008 and intercept 0.002 → Vmax = 1/0.002 = 500 mg/day, Km = 0.008/0.002 = 4 mg/L.
- **Dose for a target Css of 10 mg/L:** R = Vmax Css/(Km + Css) = 500 × 10/14 = **357 mg/day**.

## 5.7 Explanation with examples of drugs

**Phenytoin** — the classic example. Its metabolising enzymes saturate within the usual therapeutic range, so Km lies near or below therapeutic plasma levels. Consequences: half-life lengthens as the level rises; small dose increments can cause a large jump in level and toxicity (nystagmus, ataxia); steady state takes longer at higher doses. Dose changes are therefore made in small steps with level monitoring, and individual Km and Vmax are estimated from two steady-state levels as in Worked example 3.

**Ethanol** — alcohol dehydrogenase saturates at low blood levels, so ethanol is eliminated at a roughly **constant amount per hour** (zero-order) over most of its range.

**Salicylates (aspirin)** — at low doses elimination is first order; at anti-inflammatory and toxic doses the conjugation pathways (glycine and glucuronide) saturate, half-life rises markedly and levels climb disproportionately.

**Theophylline** — shows some saturation at higher levels; monitoring is advised because the therapeutic window is narrow.

**Penicillin G** — at very high doses tubular secretion saturates (also blocked by probenecid), raising and prolonging levels.

**Riboflavin, ascorbic acid** — saturable intestinal absorption; large single doses are absorbed less efficiently, and saturable renal reabsorption means excess vitamin C is excreted.

**Valproic acid, disopyramide, naproxen** — saturable plasma protein binding; at higher doses the free fraction rises, so total levels rise less than proportionally while free levels behave differently from what total levels suggest.

**Carbamazepine** — induces its own metabolism (auto-induction); after a few weeks of dosing, clearance rises and levels fall, a time-dependent nonlinearity.

## 5.8 Clinical significance of nonlinear pharmacokinetics

1. Dose adjustments must be small and guided by measured levels.
2. Linear equations (Css = F X0/(CL τ), t½ = 0.693/KE) cannot be used blindly; Michaelis–Menten equations are needed.
3. Time to steady state is longer at higher doses; checking levels too early misleads.
4. Drug interactions that compete for the saturable enzyme or carrier have exaggerated effects.
5. In overdose, elimination may be zero order, so recovery takes longer than predicted from normal half-life.
6. Bioavailability and bioequivalence studies should check dose proportionality.

## Remember

- Linear: parameters independent of dose, AUC proportional to dose. Nonlinear: saturable process, parameters change with dose.
- Causes in every ADME step: saturable absorption, first pass, protein binding, enzymes, cofactors, tubular secretion and reabsorption, auto-induction.
- Michaelis–Menten: −dC/dt = Vmax C/(Km + C); first order when C << Km, zero order when C >> Km; Km = C at half Vmax.
- t½ = 0.693 Vd (Km + C)/Vmax rises with C; CL falls with C.
- Steady state: Css = Km R/(Vmax − R); a small dose rise can give a big level rise; R ≥ Vmax → no steady state.
- Km and Vmax from steady-state pairs: R = Vmax − Km (R/Css) (slope −Km, intercept Vmax), direct linear plot, Lineweaver–Burk, Hanes–Woolf, Eadie–Hofstee.
- Key drugs: phenytoin, ethanol, high-dose salicylate, theophylline, penicillin G, vitamin C, riboflavin, valproate, carbamazepine.
