# Unit 5: Downstream Processing and Regulatory Affairs

Downstream processing (DSP) covers all the steps that convert a fermentation broth or cell culture harvest into a purified, formulated drug product. For biopharmaceuticals, DSP typically accounts for 50–80% of the total manufacturing cost. The regulatory pathway for biologics (FDA, EMA, CDSCO) and the special challenges of biosimilars close this unit.

## 5.1 Downstream processing overview

The four stages of DSP form a logical funnel from crude harvest to finished product:

```text
Stage 1: RECOVERY (harvest)
  Separate cells from the medium → clarification
  Desired product may be intracellular (need cell disruption) or
  extracellular (secreted into medium)

Stage 2: ISOLATION
  Concentration and initial purification
  Remove most water and major contaminants (nucleic acids, cell debris)

Stage 3: PURIFICATION
  Chromatography steps to remove closely related impurities
  (host cell proteins, DNA, process-related impurities, viruses)

Stage 4: POLISHING
  Final removal of trace contaminants, viral clearance, formulation
  into the drug substance
```

## 5.2 Cell disruption

Required only for intracellular products (e.g. inclusion body proteins from *E. coli*, intracellular enzymes).

| Method | Principle | Scale | Products |
| --- | --- | --- | --- |
| French press | High pressure; cell suspension forced through a narrow orifice | Laboratory | Bacterial cells |
| Bead mill (ball mill) | High-speed grinding with glass or steel beads | Pilot/industrial | Bacteria, yeast |
| High-pressure homogeniser (APV type) | Continuous high-pressure disruption | Industrial | Most bacteria and yeast |
| Sonication | High-frequency ultrasound creates cavitation | Laboratory only | Bacteria; heat generation limits scale-up |
| Chemical lysis: detergents (Triton X-100, Tween 20) | Solubilise membrane lipids | Laboratory | Gentle; leaves membranes partly intact |
| Chemical lysis: lysozyme | Degrades peptidoglycan cell wall of gram-positive bacteria | Small scale | Bacteria |
| Enzymatic: protease + osmotic shock | Digest wall then osmotic lysis | Research | Gram-negative bacteria |

## 5.3 Solid-liquid separation

After cell disruption, cell debris must be removed.

**Centrifugation:**

| Type | Speed (g) | Use |
| --- | --- | --- |
| Low-speed (tubular/disc centrifuge) | 300–3,000 g | Remove whole cells and large debris from broth |
| High-speed centrifuge | 5,000–15,000 g | Collect smaller particles, inclusion bodies |
| Ultracentrifuge | Up to 500,000 g | Isolate viruses, ribosomes, membrane fragments |

**Filtration:**
- **Microfiltration (0.1–10 µm membrane):** removes whole cells, cell debris, large particles
- **Ultrafiltration (1–300 kDa MWCO membrane):** concentrates proteins and removes small molecules; also used for **diafiltration** — buffer exchange by continuous addition of buffer while maintaining constant volume via UF
- **Depth filtration (diatomaceous earth pads):** traps particles in a thick filter bed; used to clarify viscous broths

## 5.4 Protein purification techniques

### Precipitation

**Ammonium sulphate precipitation:** Adding ammonium sulphate to a protein solution reduces water activity (salting-out). Proteins precipitate at different concentrations of ammonium sulphate depending on their hydrophobicity. This is a cheap, scalable bulk purification step. The precipitate is collected by centrifugation and redissolved.

**Isoelectric precipitation:** At the protein's isoelectric point (pI), net charge is zero and solubility is minimal. Adjusting the pH of the solution to pI causes the target protein to precipitate while others stay in solution. Used for casein (pI 4.6) and many industrial enzymes.

### Chromatography — the core of biopharmaceutical purification

**Ion exchange chromatography (IEX):**
- Cation exchangers (CM-Sepharose, SP-Sepharose) bind positively charged proteins; anion exchangers (DEAE-Sepharose, Q-Sepharose) bind negatively charged proteins.
- Load sample in low-salt buffer → non-binding proteins wash through → elute bound proteins with increasing salt (NaCl gradient) or pH change.
- Both preparative and analytical uses.

**Affinity chromatography:**
- The most specific method; a ligand that binds the target protein is immobilised on the matrix.
- **Protein A/G affinity:** Protein A (from *Staphylococcus aureus*) binds the Fc region of IgG antibodies. This is the first capture step in almost all monoclonal antibody purifications. Elution with low-pH buffer (pH 3–3.5) releases the antibody.
- **IMAC (Immobilised Metal Affinity Chromatography):** Nickel or cobalt resin binds His-tagged proteins (6× His-tag at the N or C terminus). Elute with imidazole. Widely used in research and for some recombinant proteins.
- **Substrate/inhibitor affinity:** e.g. heparin-Sepharose for coagulation factors and growth factors.

**Size exclusion chromatography (SEC, also called gel filtration):**
- Porous beads (Sephadex, Superose); small molecules enter the pores and are retarded; large molecules are excluded and elute first.
- Separates by molecular size; used for removal of aggregates, final polishing, and analytical quality control.

**Hydrophobic interaction chromatography (HIC):**
- Binds proteins at high salt; elutes with decreasing salt. Used after ammonium sulphate precipitation; complements IEX.

**Reversed-phase HPLC (RP-HPLC):**
- Used mainly analytically for small proteins and peptides; can damage protein structure.

**Typical mAb purification train:**
1. Protein A capture (affinity, 1000-fold purification)
2. Low-pH viral inactivation step
3. Cation exchange chromatography (removes residual impurities and aggregates)
4. Anion exchange in flow-through mode (removes DNA, endotoxin, viruses)
5. Viral filtration (20 nm membrane)
6. Ultrafiltration/diafiltration (concentrate and buffer-exchange)

## 5.5 Viral clearance and inactivation

For products derived from animal cell culture or plasma, viral safety is critical. A combination of orthogonal steps is required:

| Step | Method | Log reduction |
| --- | --- | --- |
| pH hold (pH 3.5 for 30 min) | Inactivates enveloped viruses (HIV, hepatitis C) | 4–6 log |
| Solvent/detergent (Triton X-100 + TNBP) | Inactivates enveloped viruses | >4 log |
| Heat treatment (pasteurisation) | Inactivates viruses in albumin solutions | Variable |
| Viral filtration (20 nm membrane) | Physical removal of enveloped and some non-enveloped viruses | >4 log |

Regulatory guidelines (ICH Q5A) require demonstration of at least 12 log reduction for model viruses in a production process.

## 5.6 Formulation of biopharmaceuticals

Biologics are chemically and physically more complex than small molecules and are more susceptible to degradation.

**Protein stability issues:**
- **Aggregation:** irreversible self-association, can be immunogenic; minimised by formulation excipients
- **Deamidation:** asparagine and glutamine side chains are chemically labile; promoted by high pH and temperature
- **Oxidation:** methionine and cysteine oxidised by peroxide or metal ions; prevented by antioxidants (methionine, polysorbate) and low oxygen headspace

**Lyophilisation (freeze-drying):** Most biopharmaceuticals are lyophilised because liquid formulations are unstable.

```text
Step 1: FREEZING — product frozen; ice crystals form
Step 2: PRIMARY DRYING (sublimation) — temperature raised below Tg (glass
        transition temperature); ice sublimes under vacuum
Step 3: SECONDARY DRYING — residual moisture removed at higher temperature
        and lower pressure; residual moisture < 1–3%
Final product: dry powder that can be reconstituted with water for injection
```

**Excipients used in lyophilisation:**
- Bulking agents: mannitol, sucrose (increase cake size; mannitol gives crystalline cake; sucrose amorphous)
- Lyoprotectants: sucrose, trehalose (protect protein during freeze-drying by hydrogen bonding)
- Stabilisers: polysorbate 20 or 80 (prevent surface-induced aggregation)
- Buffer: histidine (most common for mAbs), citrate, phosphate

**Cold chain:** Most protein biologics require storage at 2–8°C. Temperature excursions can cause irreversible aggregation or activity loss. Lyophilised products are more stable and may tolerate ambient conditions for shorter periods. The cold chain must be validated from manufacturing through distribution to the patient.

## 5.7 Quality control of biopharmaceuticals

| Test | Method | Purpose |
| --- | --- | --- |
| Identity | SDS-PAGE, Western blot, peptide mapping, mass spectrometry | Confirm correct protein |
| Purity | SDS-PAGE, SEC-HPLC, RP-HPLC | Detect aggregates, fragments, impurities |
| Potency (biological activity) | Cell-based assay (e.g. CTLL-2 proliferation for IL-2) or ligand-binding assay | Confirm functional activity |
| Isoelectric focusing (IEF) | Capillary IEF or slab gel | Glycoform pattern, charge variants |
| Peptide mapping | Tryptic digest + LC-MS | Sequence confirmation, detect modifications |
| Sterility | USP/BP sterility test | Absence of viable microorganisms |
| Endotoxin (pyrogen) | LAL (Limulus amebocyte lysate) test | Detect bacterial endotoxin (< 5 EU/kg per dose) |
| Mycoplasma | PCR or cell culture | Absence of mycoplasma contamination |
| Host cell proteins (HCP) | ELISA | Residual HCP from CHO or *E. coli* (< ppm levels) |
| Residual DNA | qPCR | Host cell DNA (< 10 ng per dose, WHO guidance) |

## 5.8 Regulatory pathway for biologics

**In India (CDSCO):**
- Central Drugs Standard Control Organisation regulates biologics under the New Drugs and Clinical Trial Rules 2019.
- Biologics require pre-clinical safety data, Phase I, II and III clinical trials, and manufacturing site inspection before a New Drug Application (NDA) is granted.
- The Drug and Cosmetics Act covers biopharmaceutical approval.

**In the USA (FDA):**
- Biologics are approved under the **Biologics License Application (BLA)** pathway, under the Public Health Service Act.
- Quality requirements are specified in 21 CFR Parts 210, 211 and 610.

**In Europe (EMA):**
- Approval is centralised through the **European Medicines Agency (EMA)**, Committee for Medicinal Products for Human Use (CHMP).
- Mandatory centralised procedure for all novel biologics and biosimilars.

### Biosimilars vs originator biologics

A **biosimilar** is a biologic drug approved on the basis of demonstrated similarity to an already-approved originator biologic (reference product) in terms of quality, safety and efficacy. Biosimilars are not "generic" biologics because:

| Feature | Small molecule generic | Biosimilar |
| --- | --- | --- |
| Active substance | Identical (can be synthesised identically) | Highly similar but not identical (produced by living cells) |
| Manufacturing | Chemistry; reproducible | Biotechnology; cell line, process and product characteristics differ |
| Approval requirement | Bioequivalence (PK study) | Full analytical comparability + clinical data (at least PK/PD and safety) |
| Naming | Same INN | Same INN + suffix (e.g. filgrastim-sndz) in the US |

**Comparability concept:** When a manufacturer changes the manufacturing process (cell line, process conditions, formulation), they must demonstrate through analytical, non-clinical and sometimes clinical studies that the product before and after the change is comparable — the same principle applies to biosimilar development.

**Pharmacovigilance of biotherapeutics:** Adverse events, including immunogenicity (formation of anti-drug antibodies), must be monitored and reported. Traceability (which batch, from which manufacturer, was given to which patient) is essential because immunogenicity problems may be product-specific or batch-specific.

## Remember

1. DSP stages in order: recovery (cell harvest + disruption if needed) → isolation (precipitation, ultrafiltration) → purification (chromatography) → polishing (viral clearance, formulation).
2. Protein A affinity chromatography is the standard first capture step for monoclonal antibodies; it exploits the Fc region binding and achieves >1000-fold purification in one step.
3. Viral clearance requires orthogonal steps: at least one inactivation step (low pH or solvent/detergent) plus one removal step (viral filtration). ICH Q5A governs this.
4. Lyophilisation steps: freezing → primary drying (sublimation) → secondary drying. Sucrose and trehalose are lyoprotectants; mannitol is a bulking agent.
5. The LAL test (Limulus amebocyte lysate) detects bacterial endotoxin; the limit is typically 5 EU/kg body weight per dose for intravenous products.
6. Biosimilars require a comparability exercise covering analytical, PK/PD and clinical data; they are not identical to the originator but highly similar.
7. BLA (FDA) or centralised EMA procedure covers novel biologic approval; CDSCO is the Indian regulatory authority for biologics.
8. SDS-PAGE separates proteins by size; Western blot identifies a specific protein with an antibody; peptide mapping by LC-MS confirms primary structure and detects modifications.
