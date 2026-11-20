# Last-night revision sheet

## Unit 1 — GI absorption

- Rate-limiting: dissolution (poorly soluble) or permeation (poorly permeable). F = fa × FG × FH.
- % un-ionised: acid 100/(1 + 10^(pH − pKa)); base 100/(1 + 10^(pKa − pH)). Ion trapping ratio for acid = (1 + 10^(pHp − pKa))/(1 + 10^(pHg − pKa)).
- pH-partition limits: intestinal surface area, microclimate pH (5.5–6.5), unstirred layer, ionised species cross, carriers, dissolution ignored.
- Noyes–Whitney: dM/dt = DA(Cs − C)/h. Hixson–Crowell: W0^(1/3) − W^(1/3) = κt.
- Dosage form order: solution > suspension > capsule > tablet > coated tablet.
- Transport model: 1/Peff = 1/PABL + 1/(Pm + Ppara); Pm = P0 × fneutral; flux = Peff × Cs. MAD = S × Ka × 250 mL × 270 min.
- Tight junctions: claudins, occludin, ZO; favour small hydrophilic cations. Intracellular pH 7.0–7.2.
- Permeability: PAMPA, Caco-2 (Papp = (dQ/dt)/(A C0); efflux ratio ≥ 2), MDCK-MDR1, Ussing chamber, everted sac, SPIP Peff = −Q ln(Cout/Cin)/(2πrL), Loc-I-Gut.

## Unit 2 — Product design and in vitro performance

- D0 = (dose/250)/Cs; IDR > 1 mg/min/cm² rarely limiting, < 0.1 problematic.
- USP apparatus 1–7: basket, paddle, reciprocating cylinder, flow-through, paddle over disc, rotating cylinder, reciprocating holder. 37 ± 0.5 °C, 900 mL, pH 1.2/4.5/6.8, sink ≥ 3 × saturation volume.
- S1 each ≥ Q + 5%; S2 mean(12) ≥ Q, none < Q − 15%; S3 mean(24) ≥ Q, ≤ 2 < Q − 15%, none < Q − 25%.
- IVIVC A (point-to-point) > B (MDT vs MRT) > C (single point); %PE ≤ 10% mean, ≤ 15% each.
- f1 = Σ|R − T|/ΣR × 100 (0–15); f2 = 50 log{[1 + Σ(R − T)²/n]^(−0.5) × 100} (50–100). Example: f1 8.9, f2 61.3.
- MDT = Σ tmid ΔM/Σ ΔM; DE = area/(100 × t). Korsmeyer–Peppas n (slab): 0.5 Fickian, 1 Case II.
- India zone IVb: 30 °C/75% RH long term; 40 °C/75% RH accelerated.

## Unit 3 — Compartment and NCA

- IV bolus: C = C0 e^(−Kt); Vd = X0/C0; AUC = C0/K; CL = KVd.
- Infusion: Css = R0/CL; 90% in 3.32 t½; DL = Css Vd.
- Oral: tmax = ln(Ka/K)/(Ka − K); AUC = F X0/CL; flip-flop if Ka < K.
- Wagner–Nelson: FA = (C + K·AUC0–t)/(K·AUC0–∞). Loo–Riegelman for 2-compartment.
- Two-compartment: C = Ae^(−αt) + Be^(−βt); k21 = (Aβ + Bα)/(A + B); k10 = αβ/k21; k12 = α + β − k21 − k10; V1 = D/(A + B); Vss = V1(1 + k12/k21); Vβ = CL/β. Drug Y: k21 0.56, k10 0.714, k12 0.926 h⁻¹; V1 10, Vss 26.5, Vβ 35.7 L.
- NCA: MRT = AUMC/AUC; MAT = MRToral − MRTiv = 1/Ka; Vss = CL × MRT; tail AUC = Clast/λz.
- Drug X: K 0.1733 h⁻¹, t½ 4 h, Vd 25 L, CL 4.33 L/h, AUC(500 mg IV) 115.4, oral AUC 93.67 (trapezoid), F 0.81, MRT oral 6.55 h, MAT 0.78 h.

## Unit 4 — Nonlinear PK and interactions

- Signs: AUC/dose not constant, t½ changes with dose.
- Rate = Vmax C/(Km + C); Css = Km R/(Vmax − R); CL = Vmax/(Km + C).
- Two steady states: Km = (R2 − R1)/(R1/C1 − R2/C2); Vmax = R1 + Km R1/C1. Plot R vs R/Css: slope −Km, intercept Vmax.
- t90 = [Km Vd/(Vmax − R)²](2.3 Vmax − 0.9R). Drug Z: Vmax 500 mg/day, Km 4 mg/L → 300 → 6, 400 → 16 mg/L.
- Displacement: low-extraction → unbound level unchanged at steady state; high-extraction IV → unbound AUC ↑; oral AUCu = Dose/CLint.
- Tissue binding: Vd = Vp + VT fu/fuT.
- AUCR = 1/[fm/(1 + [I]/Ki) + (1 − fm)]; strong ≥ 5, moderate 2–5, weak 1.25–2. Induction (PXR/CAR) takes 1–2 weeks.
- ICH M12 transporters: P-gp, BCRP, OATP1B1/1B3, OAT1/3, OCT2, MATE1/2-K.

## Unit 5 — BA/BE, BCS, biosimilars

- F = (AUCoral DoseIV)/(AUCIV Doseoral).
- 2 × 2 crossover, washout ≥ 5 t½, sampling ≥ 3 t½, AUC0–t ≥ 80% AUC0–∞, fasting/fed.
- ln AUC, ln Cmax; 90% CI of GMR within 80.00–125.00% (TOST); NTI 90.00–111.11%; HVD (CV ≥ 30%) replicate design, scaled Cmax limits up to 69.84–143.19%.
- Example: GMR 95.36%, CI 88.81–102.40%, CVw 9.6% → BE.
- India: CDSCO, NDCT Rules 2019, ethics committee, CTRI, BA/BE guideline 2005.
- BCS (ICH M9): solubility in ≤ 250 mL over pH 1.2–6.8 at 37 °C; fa ≥ 85%; very rapid 85%/15 min, rapid 85%/30 min; waivers Class I and III.
- Biosimilar: stepwise comparability, analytical first, PK/PD, immunogenicity, extrapolation; India Similar Biologics guidelines 2012/2016.

## Unit 6 — Applications

- Emax: E = Emax C/(EC50 + C); sigmoid Cⁿ. Anticlockwise loop → ke0 effect compartment; clockwise → tolerance. Indirect response: kin/kout.
- ER design: k0r = Css CL/F; DL = Css Vd/F; Di = DL − k0r tmax. Drug X (Css 4 mg/L, 12 h): 21.7 mg/h, 260 mg, loading 84 mg.
- %PTF = (Cmax − Cmin)/Cav × 100; dose dumping; MR BE fasted + fed.
- Targeting: EPR, MPS, PEGylation; DTI = (T/NT carrier)/(T/NT free) (example 8).
- Proteins: lymphatic SC absorption, proteolysis, renal filtration < 60 kDa, TMDD; PEG/Fc/albumin extend t½.
- mAbs: FcRn recycling (t½ about 2–3 weeks), TMDD nonlinear, ADA.
- Oligonucleotides: short plasma, long tissue t½; GalNAc–ASGPR; nucleases.
- Vaccines: titre kinetics, adjuvants, prime–boost. Gene therapy: biodistribution, shedding, expression; CAR-T expansion.
