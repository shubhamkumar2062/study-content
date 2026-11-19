# Last-night revision sheet

## Unit 1 — Absorption, distribution, protein binding

- **Biopharmaceutics**: drug + dosage form + route → rate and extent of absorption. LADME.
- **Passive diffusion** (most drugs): Fick's law dQ/dt = D A Km/w (CGIT − C); first order, non-saturable, down the gradient.
- **Carrier-mediated**: facilitated (no energy) and active (energy, against gradient); specific, saturable, competitive. Levodopa, 5-FU, vitamin B12. P-gp pumps drugs back.
- **Others**: pore (urea), ion-pair (quaternary amines), endocytosis (pinocytosis, phagocytosis).
- **pH-partition**: un-ionised form absorbed. Acid: pH − pKa = log(I/U); base: pKa − pH = log(I/U). Limits: intestinal area, micro-climate pH, transit time.
- **Noyes–Whitney**: dC/dt = D A (Cs − Cb)/h.
- **Factors**: drug (solubility, particle size, polymorph, salt, pKa, stability, complexation); dosage form (type, excipients, process); patient (gastric emptying, transit, pH, food, blood flow, first pass, disease, age).
- **Vd = X/C**; plasma binding ↓Vd, tissue binding ↑Vd. Vd = Vp + Vt (fu/fut).
- **Albumin** binds acids (site I warfarin, II diazepam); **α1-acid glycoprotein** binds bases.
- **Scatchard**: r/[D] = nKa − rKa (slope −Ka, x-intercept n). **Klotz**: 1/r = 1/(nKa[D]) + 1/n.
- Only free drug acts, is filtered and metabolised; displacement matters for > 95% bound, small Vd, narrow-margin drugs (warfarin, phenytoin).

## Unit 2 — Elimination, bioavailability, bioequivalence

- Phase I: oxidation (CYP450), reduction, hydrolysis. Phase II: glucuronidation (most common), sulfation, acetylation, methylation, glycine, glutathione.
- **Renal excretion** = filtration (free drug, GFR ≈ 125 mL/min) + active secretion (anions, cations; probenecid blocks penicillin) − passive reabsorption (urine pH).
- **CLR** = excretion rate / C; ratio to GFR: = 1 filtration only, < 1 reabsorption, > 1 secretion.
- **Cockcroft–Gault**: CLcr = (140 − age) × wt / (72 × Scr); × 0.85 for women.
- **Non-renal**: bile (enterohepatic cycling), lungs, saliva, milk (bases concentrate), sweat, GIT.
- **F (absolute)** = (AUCoral × DIV)/(AUCIV × Doral). **Frel** compares two non-IV products.
- **Measurement**: plasma data (Cmax, tmax, AUC), urine data ((dXu/dt)max, tu, Xu∞), acute response, clinical trials.
- **Dissolution**: basket (1), paddle (2), reciprocating cylinder (3), flow-through (4); 37 °C; f2 ≥ 50 = similar.
- **IVIVC**: Level A point-to-point (best), B mean times, C single point; BCS Class II best chance.
- **BE**: crossover, washout ≥ 5 t½, log AUC and Cmax, 90% CI within 80–125%.
- **Enhance dissolution**: micronisation, salts, amorphous form, solid dispersion, cyclodextrin, surfactant, cosolvent, SEDDS, prodrug.

## Unit 3 — One-compartment model

- Zero order: constant amount/time. First order: constant fraction/time, t½ = 0.693/KE.
- Models: compartment (mammillary, catenary), non-compartmental (AUC, AUMC, MRT = AUMC/AUC), physiological (organ blood flows).
- **IV bolus**: C = C0 e^(−KE t); Vd = X0/C0; AUC = C0/KE; CL = KE Vd = X0/AUC.
- **Urine**: rate method (ln excretion rate vs midpoint time), sigma-minus (ln(Xu∞ − Xu) vs t).
- **Infusion**: C = (R0/CL)(1 − e^(−KE t)); Css = R0/CL; 90% in 3.3 t½; loading dose = Css Vd.
- **Oral**: C = F X0 Ka/[Vd(Ka − KE)] (e^(−KE t) − e^(−Ka t)); tmax = ln(Ka/KE)/(Ka − KE); AUC = F X0/CL.
- **Ka**: method of residuals (needs Ka ≥ about 3 KE), Wagner–Nelson FA = (Ct + KE AUC0–t)/(KE AUC0–∞) (one compartment only), Loo–Riegelman (two compartment).
- **Trapezoidal rule**: Σ (C1 + C2)/2 × Δt + Clast/KE.
- Worked example drug: KE 0.1733 h⁻¹, t½ 4 h, Vd 25 L, CL 4.33 L/h, AUC (500 mg IV) 115.4 mg·h/L.

## Unit 4 — Two-compartment model and multiple dosing

- C = A e^(−αt) + B e^(−βt); feathering gives B, β (terminal line) then A, α (residuals).
- k21 = (Aβ + Bα)/(A + B); k10 = αβ/k21; k12 = α + β − k21 − k10; Vc = Dose/(A + B); AUC = A/α + B/β; Vc < Vss < Vβ.
- **Multiple dosing**: R = 1/(1 − e^(−KE τ)); Css,max = (X0/Vd)R; Css,min = Css,max e^(−KE τ); Css,av = F X0/(CL τ).
- Steady state in about 5 t½, regardless of dose.
- DM = Css,av CL τ/F; DL = Css Vd/F = DM × R; τ = t½ → DL = 2 DM.
- Renal failure: reduce maintenance dose (CL ↓), loading dose usually unchanged (Vd).

## Unit 5 — Nonlinear pharmacokinetics

- Signs: AUC/dose not constant, t½ changes with dose, curved log C plot.
- Causes: saturable absorption (riboflavin, vitamin C), first pass (propranolol), protein binding (valproate), enzymes (phenytoin, ethanol, salicylate), cofactor depletion (paracetamol overdose), tubular secretion (penicillin G), auto-induction (carbamazepine).
- **Michaelis–Menten**: −dC/dt = Vmax C/(Km + C); C << Km first order; C >> Km zero order.
- t½ = 0.693 Vd (Km + C)/Vmax rises with level.
- **Css = Km R/(Vmax − R)**; R ≥ Vmax → no steady state.
- **Km, Vmax**: R = Vmax − Km (R/Css) (slope −Km, intercept Vmax); direct linear plot; Lineweaver–Burk; Hanes–Woolf; Eadie–Hofstee.
