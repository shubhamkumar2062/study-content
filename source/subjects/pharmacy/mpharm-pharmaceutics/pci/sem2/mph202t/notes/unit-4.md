# Unit 4: Nonlinear pharmacokinetics and drug interactions

This unit covers the second half of syllabus Unit 3: causes of nonlinearity, the Michaelis–Menten equation and estimation of Km (written "Kmax" in the syllabus) and Vmax, and pharmacokinetic drug interactions caused by protein binding, tissue binding, cytochrome P450 enzymes and transporters.

Worked examples use example numbers for hypothetical drugs ("Drug Z" for capacity-limited elimination). They are not values for any real medicine.

## 4.1 Linear versus nonlinear pharmacokinetics

In **linear (dose-independent)** kinetics every rate is proportional to concentration, so CL, Vd and t½ are constant, AUC and Css rise in direct proportion to dose, and superposition works.

In **nonlinear (dose-dependent)** kinetics one or more processes involve a capacity-limited step (enzyme, carrier, binding site) that saturates. Then:

- dose-normalised AUC (AUC/dose) or Css/dose changes with dose;
- the elimination "half-life" changes with concentration;
- the composition of metabolites may change with dose;
- small dose changes can cause large changes in plasma level;
- superposition fails, so single-dose data cannot predict multiple-dose levels simply.

**Tests for nonlinearity:** give several doses (at least three spanning the clinical range) and compare dose-normalised AUC; plot AUC against dose; compare single- and multiple-dose AUC (AUCτ at steady state should equal single-dose AUC0–∞ in linear kinetics); check whether t½ changes with dose or time.

```text
 AUC │                 . more than proportional (saturable elimination,
     │              .     saturable first pass)
     │           .  ___ proportional (linear)
     │        ._--
     │     .-‾   ‾‾‾‾--- less than proportional (saturable absorption,
     │  .-‾                saturable protein binding with total levels)
     └───────────────────────── Dose
```

## 4.2 Causes of nonlinearity (with mechanism)

| ADME step | Mechanism | Effect with rising dose | Classic examples (mechanism only) |
| --- | --- | --- | --- |
| Absorption | Saturation of uptake carriers | F falls; AUC rises less than proportionally | Riboflavin, some β-lactams absorbed by PEPT1 |
| | Solubility- or dissolution-limited absorption | F falls at high doses | Poorly soluble drugs (griseofulvin type) |
| | Saturation of gut-wall or hepatic first-pass metabolism, or of efflux | F rises; AUC rises more than proportionally | Propranolol-type high-extraction drugs, some P-gp substrates |
| Distribution | Saturation of plasma protein binding | fu rises; total levels rise less than proportionally, unbound levels nearly proportional | Valproic acid, disopyramide |
| | Saturation of tissue binding or of transport into tissues | Vd changes with dose | Some drugs taken up into cells by transporters |
| Metabolism | Capacity-limited (Michaelis–Menten) enzymes | CL falls, AUC and Css rise more than proportionally, t½ lengthens | Phenytoin, ethanol, high-dose salicylate |
| | Co-factor depletion | Metabolism slows at high doses | Paracetamol overdose (glutathione depletion) |
| | Enzyme induction by the drug itself (autoinduction, time-dependent) | CL rises over the first weeks | Carbamazepine |
| | Product inhibition | Metabolite slows its own formation | |
| Excretion | Saturation of active tubular secretion | Renal CL falls at high levels | Penicillins at very high levels |
| | Saturation of active tubular reabsorption | Renal CL rises at high levels | Ascorbic acid |
| | Changes in urine pH or flow caused by the drug | | |
| Target-mediated drug disposition (TMDD) | Binding to the pharmacological target removes drug | CL falls as target saturates (common with monoclonal antibodies, Unit 6) | |

## 4.3 Michaelis–Menten kinetics

For capacity-limited elimination, the rate of elimination is:

−dC/dt = Vmax × C / (Km + C)

- **Vmax:** maximum rate of the process (amount per time, or concentration per time when divided by Vd).
- **Km:** Michaelis constant, the concentration at which the rate is half of Vmax.

**Limiting cases**

1. **C much smaller than Km:** −dC/dt ≈ (Vmax/Km) × C, first order with K = Vmax/Km.
2. **C much larger than Km:** −dC/dt ≈ Vmax, zero order; a constant amount is removed per hour regardless of level.
3. In between, mixed order.

```text
 Rate │            ________________ Vmax
      │        .-‾‾
      │     .-‾
      │   .‾   ← half Vmax at C = Km
      │  /
      │ /  (first-order region)
      └─────────────────────────── C
```

**Integrated equation (after an IV bolus)**

t = (C0 − C)/Vmax + (Km/Vmax) × ln(C0/C)     (Vmax here in concentration per time)

- The time for the level to halve gets longer as C0 increases: "half-life" is not constant. At low levels t½ approaches 0.693 Km/Vmax.

**Clearance at a given concentration:** CL = Vmax/(Km + C) (Vmax in amount per time). As C rises, CL falls. Intrinsic clearance at low concentration CLint = Vmax/Km.

**Steady state on regular dosing** (dosing rate R, amount per time, equals elimination rate):

R = Vmax × Css/(Km + Css)  →  **Css = Km × R/(Vmax − R)**

If R reaches Vmax, no steady state is possible; levels keep rising.

**Time to reach 90% of steady state** (useful for monitoring):

t90 = [Km × Vd / (Vmax − R)²] × (2.3 Vmax − 0.9 R)

It becomes very long as R approaches Vmax.

## 4.4 Estimation of Km and Vmax

### In vivo, from steady-state levels at two or more dosing rates

**Direct calculation with two pairs (R1, C1) and (R2, C2):**

Km = (R2 − R1)/[(R1/C1) − (R2/C2)]     Vmax = R1 + Km × (R1/C1)

**Graphical methods** (Michaelis–Menten rearranged):

| Plot | x-axis | y-axis | Slope | Intercept |
| --- | --- | --- | --- | --- |
| R vs R/Css (Eadie–Hofstee type, most used) | R/Css | R | −Km | Vmax |
| Lineweaver–Burk | 1/Css | 1/R | Km/Vmax | 1/Vmax |
| Css vs Css/R (Hanes–Woolf type) | Css | Css/R | 1/Vmax | Km/Vmax |
| Direct linear plot | Lines joining −Css on the x-axis to R on the y-axis for each pair; they cross at the point (Km, Vmax) | | | |

Lineweaver–Burk gives too much weight to the low-concentration points; the R vs R/Css plot and the direct linear plot are more robust.

### In vivo, from a single IV dose

Fit the integrated equation to the declining curve by nonlinear regression, or use the slope of the terminal (low-concentration) phase to find Vmax/Km and the extrapolated intercept to separate Km.

### In vitro (enzyme kinetics)

Incubate the drug at several concentrations with liver microsomes, hepatocytes or recombinant enzymes; measure initial rate of metabolite formation v at each substrate concentration S; plot v vs S and fit. In vitro CLint = Vmax/Km is scaled to the whole liver for prediction of hepatic clearance (in vitro–in vivo extrapolation).

### Worked example 1 — capacity-limited Drug Z (example numbers)

Drug Z: Vmax = 500 mg/day, Km = 4 mg/L, Vd = 50 L.

| Dosing rate R (mg/day) | Css = Km R/(Vmax − R) (mg/L) |
| --- | --- |
| 300 | 4 × 300/200 = **6.0** |
| 350 | 4 × 350/150 = **9.3** |
| 400 | 4 × 400/100 = **16.0** |
| 450 | 4 × 450/50 = **36.0** |

A 33% increase in dose (300 → 400 mg/day) raises Css by 167% (6 → 16 mg/L).

**Recovering Km and Vmax from two steady states:** (300 mg/day, 6 mg/L) and (400 mg/day, 16 mg/L):

Km = (400 − 300)/(300/6 − 400/16) = 100/(50 − 25) = **4 mg/L**
Vmax = 300 + 4 × (300/6) = 300 + 200 = **500 mg/day**

**Dosing rate for a target of 10 mg/L:** R = Vmax × C/(Km + C) = 500 × 10/14 = **357 mg/day**.

**Time to 90% of steady state at 357 mg/day:** t90 = [4 × 50/(500 − 357)²] × (2.3 × 500 − 0.9 × 357) = (200/20,449) × 829 = **8.1 days**. At 300 mg/day t90 is 4.4 days; at 400 mg/day it is 15.8 days. The closer the dose is to Vmax, the slower steady state is reached.

**Clearance falls with level:** at 1 mg/L CL = 500/5 = 100 L/day; at 6 mg/L 50 L/day; at 16 mg/L 25 L/day.

### Clinical implications

- Increase doses in small steps and monitor plasma levels (therapeutic drug monitoring).
- Do not assume a doubled dose doubles the level.
- Steady state may take much longer than "five half-lives".
- Interactions that change Vmax (inhibitors, inducers) have large effects.
- Overdose is cleared slowly (zero-order region).

## 4.5 Drug interactions: introduction

A **drug interaction** is a change in the effect of one drug (the object or victim) by another drug, food, herbal product or disease (the precipitant or perpetrator).

- **Pharmacokinetic interactions** change the concentration of the object drug at its site of action (absorption, distribution, metabolism, excretion).
- **Pharmacodynamic interactions** change the response at the same concentration (additive, synergistic, antagonistic effects at receptors or physiological systems).

Clinical importance depends on the size of the change, the therapeutic window of the object drug, and whether the change is predictable and manageable. Regulatory guidance (ICH M12, finalised 2024, adopted by many agencies) describes how to study enzyme- and transporter-mediated interactions: in vitro screening, static mechanistic or PBPK prediction, then clinical studies with index substrates or inhibitors.

**Interactions in absorption (brief):** chelation (tetracyclines or fluoroquinolones with polyvalent cations), change in gastric pH (acid-reducing drugs lower dissolution of weakly basic drugs that need acid), adsorption (cholestyramine, activated charcoal), changed gastric emptying or motility, gut-wall CYP3A4 or transporter inhibition (grapefruit juice).

## 4.6 Interactions due to protein binding

**Basis:** only unbound drug is active and is cleared by restrictive processes. A displacer competes for the same binding site (often albumin site I or site II) and raises the unbound fraction fu of the object drug.

**What happens next depends on how the drug is cleared** (well-stirred liver model):

CLH = Q × fu × CLint / (Q + fu × CLint)     E = CLH/Q

- **Low-extraction, restrictively cleared drug** (fu CLint much smaller than Q): CLH ≈ fu × CLint. When fu rises, total clearance rises in proportion, total concentration falls, and **unbound concentration returns to its original value** at steady state. The effect is transient (a brief rise in unbound level before clearance catches up). Clinically important only for narrow-index drugs given IV during the transient, or when the displacer also inhibits metabolism.
- **High-extraction drug** (fu CLint much larger than Q): CLH ≈ Q, not affected by fu. **After IV dosing**, unbound AUC rises in proportion to fu, so displacement can matter. **After oral dosing**, AUCu = Dose/CLint, unchanged by fu, because a higher fu raises first-pass extraction as well.

### Worked example 2 — displacement (example numbers)

Liver blood flow Q = 90 L/h, dose 100 mg. Unbound fraction doubled from 0.1 to 0.2 by a displacer.

| Drug | fu | CLH (L/h) | E | IV AUC total | IV AUC unbound | Oral AUC unbound |
| --- | --- | --- | --- | --- | --- | --- |
| Low-extraction (CLint 20 L/h) | 0.1 | 1.96 | 0.022 | 51.1 | 5.11 | 5.00 |
| | 0.2 | 3.83 | 0.043 | 26.1 | 5.22 | 5.00 |
| High-extraction (CLint 9,000 L/h) | 0.1 | 81.8 | 0.909 | 1.22 | 0.122 | 0.0111 |
| | 0.2 | 85.7 | 0.952 | 1.17 | 0.233 | 0.0111 |

(AUC in mg·h/L.) For the low-extraction drug, total AUC halves but unbound AUC is essentially unchanged. For the high-extraction drug given IV, unbound AUC almost doubles; given orally it is unchanged.

**Other points**

- Drugs most likely to be affected: highly bound (above about 90%), small Vd, narrow therapeutic index.
- Interpreting total plasma levels during displacement is misleading: total level falls while unbound level is normal, so a dose increase may cause toxicity. Measure unbound concentration where possible.
- Disease states (hypoalbuminaemia, uraemia, liver disease) change binding in the same way.

## 4.7 Interactions due to tissue binding

The apparent volume of distribution depends on binding in plasma and tissues:

Vd = Vp + VT × (fu / fuT)

where Vp is plasma volume (about 3 L in an adult), VT the aqueous volume outside plasma, fu and fuT the unbound fractions in plasma and tissue.

- A drug that **displaces another from tissue binding** raises fuT, which lowers Vd. With unchanged clearance, the loading phase gives higher plasma levels, and the half-life (0.693 Vd/CL) shortens.
- The classic example is the quinidine–digoxin interaction: quinidine reduces digoxin's tissue binding (lower Vd) and also reduces its renal and biliary clearance (P-gp inhibition), so digoxin plasma levels rise substantially.

**Example (example numbers):** Vp = 3 L, VT = 38 L, fu = 0.5. With fuT = 0.01, Vd = 3 + 38 × 50 = **1,903 L**. If a second drug doubles fuT to 0.02, Vd = 3 + 38 × 25 = **953 L**: a loading dose that previously gave the target level would now give about twice that level.

## 4.8 Cytochrome P450-based drug interactions

**CYP enzymes:** haem monooxygenases in liver and gut wall. CYP3A4/5 metabolises about half of marketed drugs that are metabolised; CYP2D6, CYP2C9, CYP2C19 and CYP1A2 account for much of the rest. Several (2D6, 2C9, 2C19) are genetically polymorphic, giving poor, intermediate, extensive and ultra-rapid metabolisers.

### Inhibition

| Type | Mechanism | Onset and offset | Notes |
| --- | --- | --- | --- |
| Competitive (reversible) | Inhibitor competes with substrate for the active site; raises apparent Km | Rapid; ends as inhibitor is cleared | Most common; degree depends on [I]/Ki |
| Non-competitive / mixed (reversible) | Binds elsewhere; lowers Vmax | Rapid | |
| Mechanism-based (time-dependent, irreversible) | A reactive intermediate formed by the enzyme inactivates it (covalent or quasi-irreversible haem complex) | Builds up over days; recovery needs new enzyme synthesis (days) | Some macrolide antibiotics and furanocoumarins of grapefruit juice (gut CYP3A4) |

**Static prediction of AUC change (reversible inhibition)**

AUCi/AUC = 1 / [fm / (1 + [I]/Ki) + (1 − fm)]

where fm is the fraction of the object drug's clearance through the inhibited enzyme and [I] the relevant unbound inhibitor concentration. The ratio cannot exceed 1/(1 − fm), however potent the inhibitor: a drug with several elimination routes is protected.

### Worked example 3 — inhibition (example numbers)

Inhibitor with Ki = 0.5 µM at an unbound concentration of 1.5 µM: 1 + [I]/Ki = 4.

| fm (fraction through the enzyme) | AUC ratio |
| --- | --- |
| 1.0 | 4.0 |
| 0.9 | 1/(0.9/4 + 0.1) = **3.08** |
| 0.5 | 1/(0.5/4 + 0.5) = **1.60** |

Guidance classifies inhibitors by their effect on a sensitive index substrate: **strong** (AUC ratio 5 or more), **moderate** (2 to 5), **weak** (1.25 to 2).

For a high-extraction drug given orally, inhibition of gut-wall and hepatic first pass raises F as well as lowering CL, so the AUC change is larger than the systemic CL change.

### Induction

- Mechanism: the inducer activates nuclear receptors (PXR, CAR, AhR), increasing transcription of CYP enzymes (and often P-gp). Example inducers: rifampicin, carbamazepine, phenytoin, St John's wort.
- Time course: needs new protein synthesis, so the full effect takes about 1–2 weeks to appear and to wear off after stopping.
- Effect: CLint increases. If CLint of a drug with fm = 0.9 triples, AUC ratio = 1/(0.9 × 3 + 0.1) = **0.36** (a 64% fall).
- Consequences: therapeutic failure (for example of hormonal contraceptives), toxicity when the inducer is stopped without reducing the object drug dose, more toxic metabolite formation.

### Management

Avoid the combination, choose an alternative not cleared by the same enzyme, adjust dose with monitoring, separate administration only helps absorption interactions (not metabolic ones).

## 4.9 Drug interactions linked to transporters

Transporters move drugs across intestinal, hepatic, renal and blood–brain barrier membranes. Two superfamilies:

- **ABC (ATP-binding cassette):** efflux pumps using ATP: P-glycoprotein (P-gp, MDR1, ABCB1), breast cancer resistance protein (BCRP, ABCG2), multidrug resistance-associated proteins (MRP2 etc.), bile salt export pump (BSEP).
- **SLC (solute carrier):** mostly uptake: organic anion transporting polypeptides (OATP1B1, OATP1B3, OATP2B1), organic anion transporters (OAT1, OAT3), organic cation transporter (OCT2), multidrug and toxin extrusion proteins (MATE1, MATE2-K; efflux into urine and bile driven by proton exchange), peptide transporter PEPT1.

```text
          Intestine                     Liver                        Kidney
 lumen  ─OATP2B1/PEPT1→ cell        blood ─OATP1B1/1B3→ hepatocyte   blood ─OAT1/3, OCT2→ tubule cell
 lumen  ←P-gp/BCRP──── cell        bile  ←P-gp/BCRP/MRP2/BSEP─      urine ←P-gp, MATE1/2-K, BCRP─
```

Transporters recommended for routine evaluation of new drugs (ICH M12): **P-gp, BCRP, OATP1B1, OATP1B3, OAT1, OAT3, OCT2, MATE1 and MATE2-K**.

| Transporter (site) | Effect of inhibiting it | Mechanistic examples |
| --- | --- | --- |
| P-gp (gut, kidney, liver, brain) | Higher absorption and lower renal or biliary clearance of substrates → higher levels | Digoxin levels raised by P-gp inhibitors such as verapamil, quinidine or clarithromycin |
| BCRP (gut, liver) | Higher absorption of substrates | Some statins (rosuvastatin) |
| OATP1B1/1B3 (liver uptake) | Less hepatic uptake → higher plasma levels of substrates, risk of muscle toxicity with statins | Statins with cyclosporine; single doses of rifampicin inhibit OATP1B1 |
| OAT1/OAT3 (renal uptake) | Lower tubular secretion of anions | Probenecid prolongs the action of penicillins and raises methotrexate levels |
| OCT2 and MATE1/2-K (renal) | Lower secretion of cations; rise in serum creatinine without real change in kidney function | Cimetidine, trimethoprim, dolutegravir with metformin |
| Intestinal OATP2B1 | Lower absorption of substrates | Fruit juices (grapefruit, orange, apple) lower fexofenadine absorption |

**Induction of transporters:** rifampicin and St John's wort induce intestinal P-gp, lowering the absorption of P-gp substrates such as digoxin.

**Combined enzyme–transporter interplay:** many CYP3A4 substrates are also P-gp substrates, and many inhibitors (ketoconazole-type azoles, macrolides, ritonavir) act on both, magnifying the interaction in the gut wall. Hepatic uptake by OATP can be the rate-determining step of hepatic clearance ("extended clearance concept"), so an OATP inhibitor can raise levels of a drug that is metabolised.

**In vitro study tools:** Caco-2 or MDCK-MDR1 bidirectional transport (efflux ratio), transfected cell lines over-expressing a single transporter (uptake and inhibition IC50), vesicle assays for ABC transporters, sandwich-cultured hepatocytes for biliary excretion. Endogenous biomarkers (coproporphyrin I for OATP1B, N1-methylnicotinamide for OCT2/MATE) are used in early clinical studies.

## 4.10 Putting it together: assessing an interaction risk

```text
 Object drug: which routes clear it? (fm by enzyme/transporter, fe, extraction ratio)
           │
 Precipitant: inhibits or induces which enzymes/transporters? Ki, IC50, [I]u
           │
 Static model (AUC ratio) ── small risk ──► no clinical study
           │ possible risk
           ▼
 PBPK simulation / clinical DDI study with index substrate or inhibitor
           │
 Label: avoid, adjust dose, monitor
```

## Remember

- Nonlinear signs: dose-normalised AUC changes, t½ changes with dose, superposition fails.
- Saturable absorption → less than proportional AUC; saturable metabolism or first pass → more than proportional.
- Michaelis–Menten: rate = Vmax C/(Km + C); Css = Km R/(Vmax − R); CL = Vmax/(Km + C); first order below Km, zero order above.
- Two steady states: Km = (R2 − R1)/(R1/C1 − R2/C2); Vmax = R1 + Km R1/C1; R vs R/Css plot gives slope −Km, intercept Vmax.
- t90 = [Km Vd/(Vmax − R)²](2.3 Vmax − 0.9 R).
- Protein-binding displacement: low-extraction drugs → unbound level returns (transient); high-extraction IV → unbound AUC rises; oral unbound AUC = Dose/CLint.
- Tissue binding: Vd = Vp + VT fu/fuT.
- CYP inhibition AUC ratio = 1/[fm/(1 + [I]/Ki) + (1 − fm)]; strong ≥ 5, moderate 2–5, weak 1.25–2; induction takes 1–2 weeks.
- ICH M12 transporters: P-gp, BCRP, OATP1B1, OATP1B3, OAT1, OAT3, OCT2, MATE1, MATE2-K.
