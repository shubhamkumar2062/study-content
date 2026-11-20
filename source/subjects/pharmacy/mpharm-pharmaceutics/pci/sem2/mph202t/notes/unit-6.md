# Unit 6: Application of pharmacokinetics — modified-release, targeted and biotechnological products

This unit covers syllabus Unit 5: the relationship between pharmacokinetics and pharmacodynamics (building a PK/PD equation), pharmacokinetic and pharmacodynamic interactions, pharmacokinetic design of modified-release and targeted delivery systems, and the pharmacokinetics and pharmacodynamics of biotechnology drugs: proteins and peptides, monoclonal antibodies, oligonucleotides, vaccines (immunotherapy) and gene therapies.

Worked examples use example numbers for hypothetical drugs, including Drug X from Unit 3 (KE 0.1733 h⁻¹, t½ 4 h, Vd 25 L, CL 4.33 L/h, F 0.8, Ka 1.2 h⁻¹). They are not values for any real medicine.

## 6.1 Relating pharmacokinetics to pharmacodynamics

**Pharmacokinetics (PK)** describes concentration against time; **pharmacodynamics (PD)** describes effect against concentration. A **PK/PD model** links them so that the effect–time course can be predicted for any dose or regimen.

```text
 Dose ─► PK model ─► C(t) in plasma ─► [link: effect compartment or indirect response] ─► Ce(t) ─► PD model ─► E(t)
```

### Pharmacodynamic models (direct)

| Model | Equation | Use |
| --- | --- | --- |
| Linear | E = S × C + E0 | Narrow concentration range |
| Log-linear | E = m × log C + b | Middle part (20–80%) of the effect curve |
| Emax (hyperbolic) | E = E0 + Emax × C/(EC50 + C) | Most receptor-mediated effects |
| Sigmoid Emax (Hill) | E = E0 + Emax × Cⁿ/(EC50ⁿ + Cⁿ) | Steeper or flatter curves; n = Hill coefficient |
| Inhibitory Emax | E = E0 − Imax × C/(IC50 + C) | Inhibition of a baseline (enzyme, heart rate) |

- **Emax:** maximal effect (efficacy); **EC50:** concentration for half-maximal effect (potency).
- A higher n gives a steeper, more "all-or-none" curve.

### Worked example 1 — Emax model (example numbers)

Emax = 100%, EC50 = 2 mg/L, E0 = 0.

| C (mg/L) | Emax model (n = 1) | Sigmoid model (n = 2) |
| --- | --- | --- |
| 0.5 | 100 × 0.5/2.5 = 20% | 100 × 0.25/4.25 = 5.9% |
| 2 | 50% | 50% |
| 6 | 75% | 100 × 36/40 = 90% |
| 18 | 90% | — |

Going from 6 to 18 mg/L (three times higher) adds only 15% effect in the n = 1 model: above about 4 × EC50, raising the dose mainly prolongs the effect rather than increasing it, and it raises the risk of concentration-related toxicity.

### Generating a PK/PD equation: the effect-compartment (link) model

When the effect lags behind plasma concentration, a plot of effect against plasma concentration forms a loop (**hysteresis**).

- **Anticlockwise hysteresis:** effect lags concentration: distribution delay to the site of action, active metabolite formation, or indirect mechanism.
- **Clockwise (proteresis):** effect falls while concentration is still high: tolerance (acute desensitisation), or an antagonistic metabolite.

The **Sheiner effect-compartment model** adds a hypothetical effect compartment of negligible volume connected to plasma by a first-order rate constant ke0:

dCe/dt = ke0 × (Cp − Ce)

Ce (not Cp) drives the Emax model. ke0 is chosen so that the hysteresis loop collapses into a single curve. t½,ke0 = 0.693/ke0 describes the delay in onset (for example ke0 = 0.693 h⁻¹ gives an equilibration half-life of 1 h).

For an IV bolus in a one-compartment model:

Ce(t) = [Dose × ke0 / (V (ke0 − K))] × (e^(−Kt) − e^(−ke0 t))

which has the same form as the oral one-compartment equation; inserting Ce into the Emax equation gives the full **PK/PD equation**: E(t) = Emax × Ce(t)/(EC50 + Ce(t)).

### Indirect response models

Many drugs act by stimulating or inhibiting the production (kin) or loss (kout) of a body substance (for example clotting factors with oral anticoagulants, glucose, cortisol):

dR/dt = kin × [1 ± drug effect] − kout × [1 ± drug effect] × R

Four basic types: inhibition of kin, inhibition of kout, stimulation of kin, stimulation of kout. The delay depends on kout (turnover of the response), not on the drug's distribution. These explain why some effects build up over days though plasma levels peak in hours.

### Other PK/PD concepts

- **Tolerance and sensitisation** (time-dependent changes in EC50 or Emax).
- **Time-dependent antibiotics** (effect linked to time above MIC) versus **concentration-dependent** ones (Cmax/MIC, AUC/MIC); this guides dosing interval design.
- **Exposure–response** analysis (AUC or Css against outcome) supports dose selection in drug development.

## 6.2 Pharmacokinetic and pharmacodynamic drug interactions

| Type | Mechanism | Examples (mechanism only) |
| --- | --- | --- |
| PK: absorption | Chelation, pH change, gut transporters and CYP3A4 | Divalent cations with tetracyclines; grapefruit juice |
| PK: distribution | Protein and tissue binding displacement | Unit 4 |
| PK: metabolism | CYP inhibition or induction | Unit 4 |
| PK: excretion | Transporter inhibition, urinary pH | Probenecid with penicillins |
| PD: additive or synergistic | Same or complementary effect | Two CNS depressants; trimethoprim with sulphamethoxazole |
| PD: antagonistic | Opposing effects or receptor competition | Naloxone reverses opioids |
| PD: indirect | Change in physiology that alters response | Diuretic-induced hypokalaemia increasing digoxin toxicity |
| Biologic–small molecule | Cytokines (IL-6, TNF) suppress CYP expression during inflammation; anti-cytokine biologics can restore CYP activity and lower levels of co-administered CYP substrates | Anti-IL-6 receptor antibodies with CYP3A4 substrates |

**Isobologram analysis** tests combinations: points on the straight line joining equi-effective doses of each drug alone show additivity; below the line, synergy; above, antagonism.

## 6.3 Pharmacokinetics of modified-release drug products

**Terms:** modified release = any product whose release rate or site differs from a conventional product. **Extended (sustained, controlled) release:** slow release over a long time to reduce dosing frequency. **Delayed release:** release starts after a delay (enteric coating). **Pulsatile:** release at programmed times. **Site-specific/targeted:** release at a chosen site (colon).

### Rationale

- Fewer doses (better adherence), smoother plasma levels (less fluctuation, fewer peak-related side effects and trough-related failures), possibly lower total dose, protection from GI irritation (enteric).

### Drug candidates (pharmacokinetic suitability)

| Property | Favourable | Unfavourable |
| --- | --- | --- |
| Elimination half-life | About 2–8 h | Very short (impractically large amount needed) or very long (already long-acting) |
| Absorption | Throughout the GI tract | Narrow absorption window in the upper intestine (unless gastroretentive) |
| Therapeutic index | Moderate | Very narrow, if release cannot be controlled tightly |
| Dose | Small to moderate | Very large doses (product too big) |
| First pass | Low or non-saturable | Saturable first pass (slow input lowers F) |
| Solubility and stability | Adequate across GI pH | Very poor solubility in the lower gut, instability in colon |

### Designing the dose: zero-order release

To keep a target Css with zero-order release (rate k0r), the amount absorbed per hour must equal the amount eliminated:

F × k0r = Css × CL  →  k0r = Css × CL / F

Total dose = immediate (loading) portion + maintenance portion = DL + k0r × T, where T is the duration of release.

- DL (immediate portion) = Css × Vd / F.
- If the maintenance portion starts releasing at the same time as the loading portion, the loading dose is reduced (Robinson–Eriksen correction): Di = DL − k0r × tmax.

### Worked example 2 — extended-release design for Drug X (example numbers)

Target Css = 4 mg/L; CL = 4.33 L/h; Vd = 25 L; F = 0.8; tmax of the immediate portion = 1.88 h; release over 12 h.

1. Required absorption rate = Css × CL = 4 × 4.33 = 17.3 mg/h.
2. Release rate k0r = 17.3/0.8 = **21.7 mg/h**.
3. Maintenance amount for 12 h = 21.7 × 12 = **260 mg**.
4. Loading (immediate) portion = 4 × 25/0.8 = **125 mg**; corrected for simultaneous release: 125 − 21.7 × 1.88 = **84 mg**.
5. Total ≈ 84 + 260 = **344 mg** per 12-hour unit (example numbers).

### Evaluating extended-release products

- **Fluctuation:** peak–trough fluctuation (%PTF) = (Css,max − Css,min)/Css,av × 100; swing = (Css,max − Css,min)/Css,min × 100; should be lower than for the immediate-release product.
- **Flip-flop kinetics:** slow release makes Ka smaller than KE; the apparent terminal half-life reflects release (Unit 3).
- **Bioequivalence of MR products:** single-dose fasted and fed studies, sometimes multiple-dose; parameters AUC, Cmax, partial AUCs, Cmin at steady state.
- **Dose dumping:** rapid release of the whole dose (with food or alcohol, or from coating failure) is a safety concern; tested in vitro (alcohol-containing media) and in fed studies.
- **IVIVC** (Level A) is expected for extended-release products and allows dissolution-based waivers.
- **Effective half-life and MRT** increase; mean absorption time (MAT) reflects in vivo release.

## 6.4 Pharmacokinetics of targeted drug delivery systems

**Aim:** raise drug exposure at the target (tumour, infected cells, inflamed tissue, a specific organ) and lower it elsewhere, to widen the therapeutic window.

### Strategies

| Strategy | Basis | Examples |
| --- | --- | --- |
| Passive targeting | Size and surface properties: enhanced permeability and retention (EPR) in leaky tumour vessels; uptake by the mononuclear phagocyte system (MPS) in liver and spleen | Liposomes, polymeric nanoparticles, micelles |
| Active targeting | Ligands (antibodies, peptides, folate, transferrin, GalNAc) bind receptors on target cells | Antibody–drug conjugates, ligand-decorated nanocarriers |
| Physical or triggered | Release triggered by heat, pH, light, magnetic field, ultrasound | Thermosensitive liposomes |
| Prodrug / site-specific activation | Enzyme or condition at the target converts the prodrug | Colon-specific azo prodrugs |

### Pharmacokinetic features of carrier systems

- Two forms must be followed: **carrier-associated (encapsulated)** drug and **released (free)** drug. Total plasma levels mostly reflect encapsulated drug, which may be inactive; assays separating the two are needed.
- **Clearance of the carrier** by the MPS depends on size, charge and surface; PEGylation ("stealth") reduces opsonisation, extends circulation half-life and increases EPR accumulation. Repeated PEGylated doses can trigger "accelerated blood clearance" through anti-PEG antibodies.
- **Volume of distribution** of carriers is small (often near plasma volume) initially, rising as they accumulate in tissues.
- **Release rate** from the carrier controls the free-drug profile and often limits efficacy and toxicity.
- PK may be **nonlinear** (saturation of MPS uptake).

### Measures of targeting

- **Drug targeting index (DTI)** = (AUCtarget/AUCnon-target) with carrier ÷ (AUCtarget/AUCnon-target) with free drug.
- **Targeting efficiency** = AUCtarget / Σ AUC of all tissues.
- **Therapeutic availability** = AUC of free drug at the target relative to that after free-drug administration.

### Worked example 3 — targeting index (example numbers)

| | AUC in tumour | AUC in heart (non-target) |
| --- | --- | --- |
| Free drug | 30 | 40 |
| Liposomal drug | 120 | 20 |

DTI = (120/20)/(30/40) = 6/0.75 = **8**: the liposome improves the tumour-to-heart exposure ratio eight-fold.

**Hunt's pharmacokinetic analysis** of targeting shows that a carrier helps most when the target receives a small fraction of cardiac output and the free drug is rapidly eliminated outside the target, and when release occurs mainly at the target.

## 6.5 Pharmacokinetics and pharmacodynamics of biotechnology drugs: introduction

Biotechnology drugs differ from small molecules in size, structure and disposition:

| Aspect | Small molecules | Biotechnology drugs |
| --- | --- | --- |
| Size | Usually below 1 kDa | Peptides about 1–10 kDa, proteins 10–150 kDa or more, nucleic acids and vectors larger |
| Oral bioavailability | Often good | Very poor (digestion, size); given parenterally (IV, SC, IM) |
| Metabolism | CYP and conjugation enzymes | Proteolysis to amino acids; nucleases for oligonucleotides |
| Elimination | Renal excretion, hepatic metabolism | Proteolysis throughout the body, renal filtration (small proteins), receptor-mediated uptake |
| Linearity | Usually linear | Often nonlinear (target-mediated drug disposition) |
| Immunogenicity | Rare | Anti-drug antibodies (ADA) can change PK and efficacy |
| Bioanalysis | LC–MS/MS | Ligand-binding assays (ELISA), LC–MS/MS of signature peptides, qPCR for nucleic acids |
| PD | Often directly linked | Often delayed, indirect and long-lasting |

## 6.6 Proteins and peptides

### Absorption

- **Subcutaneous and IM:** molecules larger than about 16–20 kDa reach the blood mainly through the lymphatics, so absorption is slow (tmax of a day or more for large proteins) and bioavailability is incomplete (presystemic proteolysis in tissue and lymph).
- **Oral:** generally very low because of proteolysis and poor permeability; technologies such as permeation enhancers (sodium caprylate-type carriers) give small but useful bioavailability for selected peptides.
- **Other routes:** nasal, pulmonary (insulin inhalation was developed), transdermal microneedles.

### Distribution

- Limited by size: initial volume close to plasma volume; steady-state volume often about plasma plus part of interstitial fluid (roughly 2 times plasma volume) unless the protein binds tissue receptors.
- Transport from blood to tissue by convection through capillary pores and by transcytosis, not simple diffusion.

### Elimination

1. **Proteolysis** everywhere (blood, liver, kidney, tissues).
2. **Renal filtration** for small proteins and peptides (below about 60 kDa; albumin-sized molecules are mostly retained), followed by tubular uptake and breakdown, so little intact protein appears in urine.
3. **Receptor-mediated endocytosis** by the target (TMDD) or by clearance receptors (for example the asialoglycoprotein receptor for desialylated glycoproteins, mannose receptors).
4. **Hepatic uptake** of larger proteins.

### Strategies to extend half-life

PEGylation (larger hydrodynamic size, less filtration and proteolysis), fusion with the Fc fragment of IgG or with albumin (FcRn recycling), lipidation to bind albumin, glyco-engineering (more sialic acid), sustained-release depots (microspheres, in situ gels).

### Pharmacodynamics

Often an indirect or receptor-mediated response; effects can outlast plasma levels (for example hormones that switch on gene expression). PK/PD modelling with indirect response or receptor occupancy models is common.

## 6.7 Monoclonal antibodies (mAbs)

**Structure:** IgG (about 150 kDa), two Fab arms (antigen binding) and an Fc region (effector functions and FcRn binding). Types: chimeric, humanised and fully human; antibody fragments, bispecifics and antibody–drug conjugates (ADCs).

**Absorption:** IV infusion or SC (lymphatic absorption, tmax of several days, bioavailability often about 50–80%).

**Distribution:** small volume (close to plasma volume initially, steady-state volume somewhat larger); slow transfer to tissues; limited brain penetration.

**Elimination**

- **Non-specific (linear) clearance:** pinocytosis by endothelial and other cells followed by lysosomal proteolysis.
- **FcRn recycling:** inside the acidic endosome, IgG binds the neonatal Fc receptor (FcRn) and is returned to the cell surface and released at blood pH instead of being destroyed. This gives IgG1, IgG2 and IgG4 antibodies long half-lives (typically about 2–3 weeks). Engineering the Fc region to bind FcRn more tightly at acidic pH extends half-life further.
- **Target-mediated drug disposition (TMDD):** binding to the target (especially membrane-bound targets) followed by internalisation removes antibody. At low doses the target sink is large and clearance high; at high doses the target is saturated and clearance falls to the linear value. Result: **nonlinear PK**, with a shorter apparent half-life at low concentrations.

```text
 log C │\
       │ \      high dose: linear (target saturated)
       │  \___________
       │      ‾‾‾‾‾\
       │            \  falls faster at low C (target-mediated clearance)
       └───────────────────── t
```

**Other factors:** anti-drug antibodies (ADA) can speed clearance or neutralise effect; body weight, albumin and disease (high tumour burden, inflammation, protein-losing conditions) change clearance; high-dose IVIG and some diseases compete for FcRn.

**Dosing approaches** (concepts only): body-size-based dosing versus fixed (flat) dosing, often similar in variability for mAbs; loading regimens to saturate the target quickly.

**Pharmacodynamics:** often measured by target engagement (receptor occupancy, free soluble target levels) and downstream biomarkers; effects can persist long after the antibody is cleared. ADCs need three analytes: total antibody, conjugated antibody (or conjugated payload) and free payload.

## 6.8 Oligonucleotides

**Types:** antisense oligonucleotides (ASOs, single-stranded, about 16–20 nucleotides), small interfering RNAs (siRNA, double-stranded, about 21–23 base pairs), aptamers, splice-switching oligonucleotides.

**Chemical modifications** (phosphorothioate backbone, 2′-O-methyl, 2′-O-methoxyethyl, locked nucleic acids) protect against nucleases and increase plasma protein binding (reducing renal filtration).

**Pharmacokinetics**

- Given SC, IV or intrathecally; SC absorption is fairly rapid (tmax of hours).
- **Plasma half-life is short (hours)** because of rapid distribution to tissues, especially liver and kidney cortex.
- **Tissue half-life is long (weeks)**; the drug acts inside cells, so plasma levels do not track effect.
- Conjugation with **N-acetylgalactosamine (GalNAc)** targets hepatocytes through the asialoglycoprotein receptor, allowing small, infrequent SC doses for liver targets.
- Elimination by nucleases to shorter fragments, excreted in urine; no CYP metabolism, so few CYP-based interactions.
- Lipid nanoparticle formulations change the disposition of siRNA (uptake via apolipoprotein E and LDL receptors in liver).

**Pharmacodynamics:** reduction of target mRNA and protein builds up and lasts for weeks to months; dosing intervals are set by PD duration, not plasma half-life.

## 6.9 Vaccines (immunotherapy)

Vaccines do not follow classical PK; what matters is the **kinetics of the immune response**.

- After injection, antigen (and adjuvant) is taken up by antigen-presenting cells and carried to lymph nodes; the antigen itself is cleared within days, but the immune response develops over 1–3 weeks.
- The measurable "exposure" is the antibody titre or cellular immune response over time: rise, peak, decline and the memory response after a booster (prime–boost schedules).
- **Adjuvants** (aluminium salts, emulsions, TLR agonists) prolong antigen presence (depot effect) and stimulate innate immunity.
- **mRNA vaccines** in lipid nanoparticles: mRNA is translated locally and in lymph nodes for days; both mRNA and lipid components are followed in biodistribution studies.
- **Therapeutic (cancer) vaccines and other immunotherapies:** aim to stimulate immune attack on disease; response depends on patient immune status. Checkpoint-inhibitor antibodies follow mAb PK (section 6.7) with exposure–response relationships.
- Regulatory focus: immunogenicity, potency assays, biodistribution and persistence for novel platforms, rather than AUC and Cmax.

## 6.10 Gene therapies

**Platforms:** viral vectors (adeno-associated virus, AAV; lentivirus; adenovirus), non-viral vectors (lipid nanoparticles, plasmid DNA), and genetically modified cell therapies (for example CAR-T cells).

**"Pharmacokinetics" of gene therapy** means:

- **Biodistribution:** which tissues receive the vector (measured by quantitative PCR of vector DNA); depends on the serotype (tissue tropism), route (IV, intramuscular, subretinal, intrathecal) and pre-existing neutralising antibodies.
- **Vector shedding:** excretion of vector in body fluids (relevant to environmental and contact safety).
- **Transgene expression kinetics:** onset over days to weeks, and duration (months to years for non-dividing cells transduced by AAV; lentiviral integration gives permanent expression in dividing cells).
- **Cellular kinetics for CAR-T:** after infusion the cells expand (peak within about 1–2 weeks), contract and may persist; exposure is described by the peak expansion and AUC of transgene copies in blood.

**Pharmacodynamics:** level of functional protein produced, biomarkers and clinical response; the effect is long-lasting from a single administration. **Immunogenicity** against the capsid or the transgene product, and toxicity linked to vector dose, are central concerns. Re-dosing is often limited by neutralising antibodies.

## 6.11 Summary of pharmacokinetic applications

```text
 Modified release   ─► k0r = Css × CL/F; DL = Css × Vd/F; check fluctuation, flip-flop, dose dumping
 Targeted delivery  ─► follow carrier-bound and free drug; MPS clearance; DTI
 Biotech drugs      ─► proteolysis, lymphatic SC absorption, FcRn, TMDD, ADA, long PD
 PK/PD              ─► Emax/sigmoid Emax; ke0 effect compartment; indirect response
```

## Remember

- Emax model: E = Emax C/(EC50 + C); sigmoid uses Cⁿ; inhibitory Imax/IC50.
- Anticlockwise hysteresis = effect lags (ke0 effect compartment); clockwise = tolerance.
- Indirect response models: stimulation or inhibition of kin or kout; delay set by kout.
- Extended release: k0r = Css × CL/F; DL = Css × Vd/F; Di = DL − k0r × tmax; Drug X example 21.7 mg/h, 260 mg over 12 h, loading 84 mg.
- %PTF = (Cmax − Cmin)/Cav × 100; flip-flop when release is slower than elimination.
- Targeting: EPR, MPS, PEGylation, DTI = (T/NT with carrier)/(T/NT free).
- Proteins: SC absorption via lymph (> about 16–20 kDa), proteolysis, renal filtration below about 60 kDa, half-life extension by PEG, Fc, albumin.
- mAbs: small Vd, FcRn recycling (half-life about 2–3 weeks for IgG), TMDD → nonlinear, ADA.
- Oligonucleotides: short plasma, long tissue half-life; GalNAc → hepatocytes; nucleases, no CYP.
- Vaccines: immune-response kinetics (titres), adjuvants, prime–boost. Gene therapy: biodistribution, shedding, expression kinetics, CAR-T expansion.
