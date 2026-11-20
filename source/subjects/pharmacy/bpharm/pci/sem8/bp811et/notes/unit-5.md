# Unit 5: Hyphenated techniques

A chromatograph separates a mixture but identifies each peak only by its retention time, which many compounds can share. A mass spectrometer identifies a compound by its mass and fragments but struggles with mixtures. Joining the two online gives a technique that separates **and** identifies in one run. Such combinations are called **hyphenated techniques**, because their names are written with a hyphen: GC-MS, LC-MS, HPTLC-MS. With a second stage of mass analysis (MS/MS) they become the most sensitive and selective tools in modern drug analysis.

## 5.1 The idea of hyphenation

**Hyphenated technique:** an online coupling of a separation technique with one (or more) spectroscopic detection techniques, so that each separated component is identified as it emerges.

| Separation | Spectroscopic detector | Hyphenated technique |
| --- | --- | --- |
| Gas chromatography | Mass spectrometry | GC-MS, GC-MS/MS |
| Liquid chromatography (HPLC, UHPLC) | Mass spectrometry | LC-MS, LC-MS/MS |
| HPTLC | Mass spectrometry | HPTLC-MS |
| Gas chromatography | Infrared | GC-IR (GC-FTIR) |
| Liquid chromatography | NMR | LC-NMR |
| Capillary electrophoresis | Mass spectrometry | CE-MS |
| Inductively coupled plasma | Mass spectrometry | ICP-MS (elements) |

**Advantages of hyphenation**

1. Separation and identification in one run; no need to collect fractions.
2. Very high **selectivity**: two independent properties (retention and mass) must both match.
3. Very high **sensitivity** (pg or even fg amounts with MS/MS).
4. Structural information on unknown peaks (molecular mass, fragments).
5. Peaks that co-elute can still be measured separately if their masses differ.
6. Faster method development and fewer sample handling errors; easy automation.

**The main technical problem is the interface:** the chromatograph works at or above atmospheric pressure with a gas or liquid stream, while the mass analyser needs high vacuum. Every hyphenated technique is defined by how it solves this.

## 5.2 Tandem mass spectrometry (MS/MS)

**MS/MS** uses two stages of mass analysis with a fragmentation step between them.

```text
  ion source ──> Q1 ──────────> q2 (collision cell) ──────────> Q3 ──────────> detector
               select one       ions collide with argon or      separate or
               precursor ion    nitrogen and break up (CID)      select product ions
               (parent)         into product (daughter) ions
                                         Triple quadrupole (QqQ)
```

- **Q1** acts as a filter and lets through one chosen **precursor ion** (for example [M + H]⁺).
- **q2** is a collision cell (an RF-only quadrupole or hexapole) filled with an inert gas. The precursor ions collide with gas atoms, gain internal energy and break into **product ions**. This is **collision-induced dissociation (CID)**, also called collision-activated dissociation.
- **Q3** analyses the product ions.

**Scan modes**

| Mode | Q1 | Q3 | Use |
| --- | --- | --- | --- |
| **Product ion scan** | Fixed on one precursor | Scans | Fragmentation pattern of one compound; structure work |
| **Precursor ion scan** | Scans | Fixed on one product ion | Finds all compounds giving a common fragment (for example a family of metabolites) |
| **Neutral loss scan** | Scans | Scans with a fixed mass offset | Finds all compounds losing the same neutral (for example 80 for sulfate, 176 for glucuronide conjugates) |
| **Selected (multiple) reaction monitoring, SRM / MRM** | Fixed on precursor | Fixed on product | **Quantitation**: very selective and sensitive; several transitions monitored in one run |

**Worked example: paracetamol by MRM.** Paracetamol (C8H9NO2, monoisotopic mass 151.063) gives [M + H]⁺ at m/z **152.1** in positive electrospray. In the collision cell it loses ketene (CH2=C=O, 42.0) from the acetamide group, giving a product ion at m/z **110.1** (152.07 − 42.01 = 110.06). The transition **152 → 110** is monitored. Only a molecule that has mass 152 **and** gives a 110 fragment **and** elutes at paracetamol's retention time is counted, so the plasma background almost disappears.

Other tandem instruments: **Q-TOF** (quadrupole + time of flight, accurate-mass product ions for metabolite identification), **ion trap** (traps ions and fragments them repeatedly, MSⁿ) and Orbitrap-based hybrids.

## 5.3 GC-MS and GC-MS/MS

**Principle.** Volatile, thermally stable compounds are separated on a GC column; each one passes through an interface into the ion source of a mass spectrometer, where it is ionised (usually by EI at 70 eV), and its mass spectrum is recorded every fraction of a second.

**Instrumentation**

```text
 carrier gas (He) ──> injector ──> capillary column in oven ──> heated transfer line ──> EI/CI ion source
                                                                                              │
              data system <── detector (electron multiplier) <── mass analyser (quadrupole, ion trap, TOF)
                                                                  (high vacuum: turbomolecular pump)
```

| Part | Notes |
| --- | --- |
| **Carrier gas** | Helium (inert, light, does not interfere); hydrogen also used |
| **Injector and column** | Split/splitless injector; fused-silica capillary columns (for example 30 m × 0.25 mm) with low-bleed stationary phases, since column bleed raises MS background |
| **Interface** | With capillary columns (about 1 ml/min of gas) the column end goes **directly into the ion source** through a heated transfer line; the vacuum pumps can remove this small flow. With older packed columns (20–30 ml/min) a **separator** was needed to remove most of the carrier gas: the **jet separator** (light helium atoms spread out of the supersonic jet and are pumped away, while heavier analyte molecules travel straight into the next nozzle), the **effusion (Watson–Biemann) separator** (porous glass through which light helium escapes) and the **membrane separator** (a silicone membrane through which organic molecules dissolve, but helium does not) |
| **Ion source** | EI (library-searchable spectra); CI for molecular mass |
| **Analyser** | Single quadrupole most common; ion trap; TOF; **triple quadrupole for GC-MS/MS** |
| **Data system** | Spectra stored for every scan; library search against reference spectra |

**Data obtained**

- **Total ion chromatogram (TIC):** sum of all ion intensities in each scan plotted against time; looks like a normal chromatogram.
- **Mass spectrum of each peak:** taken from the scans across that peak; identified by library matching.
- **Extracted ion chromatogram (EIC):** intensity of one chosen m/z plotted against time; picks out a compound from co-eluting peaks.
- **Selected ion monitoring (SIM):** the analyser monitors only a few chosen ions instead of scanning; much higher sensitivity for quantitation.
- **MRM (GC-MS/MS):** precursor → product transitions; best selectivity in dirty samples.

**Derivatisation** makes polar, non-volatile drugs suitable for GC-MS: silylation (trimethylsilyl derivatives of OH, COOH, NH), acylation and methylation (esters of acids).

**Advantages:** high resolving power of capillary GC, reproducible EI spectra and large libraries, robust, relatively cheap. **Limitations:** only volatile and thermally stable compounds (or derivatives); large, polar, ionic molecules (peptides, salts) cannot be handled; derivatisation adds steps.

**Applications of GC-MS and GC-MS/MS**

1. **Residual solvents** in drugs (with headspace sampling).
2. **Forensic toxicology and drugs of abuse** in urine and blood; confirmation of screening tests.
3. **Doping control:** anabolic steroids and stimulants in athletes.
4. **Pesticide residues** in herbal drugs, food and water (MS/MS for very low limits).
5. **Essential oils and volatile constituents** of medicinal plants; fingerprinting.
6. **Impurity profiling** of volatile impurities, including potential genotoxic impurities such as alkyl halides.
7. **Environmental analysis:** dioxins, polyaromatic hydrocarbons.
8. **Metabolomics** of small volatile or derivatised metabolites.

## 5.4 LC-MS and LC-MS/MS

**Principle.** Compounds separated by HPLC (or UHPLC) are converted into gas-phase ions **at atmospheric pressure** in an interface (ion source) and then pass into the mass analyser through a small orifice and stages of pumping.

**Why LC-MS is harder than GC-MS.** An HPLC pumps about 0.2–1 ml/min of liquid. Each millilitre of water expands to more than a litre of vapour, far more than a mass spectrometer's vacuum pumps can remove. Early interfaces (moving belt, thermospray, particle beam) were complicated and unreliable. **Atmospheric pressure ionisation (API)** solved the problem by making ions outside the vacuum and letting only the ions (with little solvent) enter.

### Electrospray ionisation (ESI)

```text
 LC eluent ──> metal capillary at high voltage (2–5 kV) ──> Taylor cone ──> spray of charged droplets
                    (nebulising N2 gas around it)                                   │
          heated drying gas evaporates solvent; droplet shrinks; charge density rises│
          droplets split (Coulomb fission at the Rayleigh limit) ─> gas-phase ions ──> sampling cone ──> MS
```

1. The eluent passes through a narrow capillary held at a high voltage; a fine mist of **charged droplets** forms (helped by nebulising nitrogen).
2. Heated drying gas evaporates the solvent. The droplet shrinks while its charge stays the same.
3. When charge repulsion exceeds surface tension (Rayleigh limit) the droplet bursts into smaller droplets (Coulomb fission).
4. Finally ions are released into the gas phase (ion evaporation, or charged residue for large molecules).
5. Ions are drawn through a sampling cone or heated capillary into the vacuum region.

**Features of ESI**
- Very soft: gives [M + H]⁺ or [M + Na]⁺ in positive mode and [M − H]⁻ in negative mode, with little fragmentation.
- Best for **polar and ionic** compounds already charged in solution: most drugs, metabolites, peptides, proteins, nucleotides.
- Large molecules carry **many charges**, so a protein of 15,000 Da appears at m/z values within a normal analyser's range: with 10 protons, m/z = (15,000 + 10 × 1.007)/10 ≈ **1501.0**; with 15 protons, ≈ 1001.0. Two adjacent peaks of the charge envelope give both the charge and the mass. For peaks at m/z 1501.0 and 1364.6, the charge of the 1501.0 peak is (1364.6 − 1.007)/(1501.0 − 1364.6) = 10, and M = 10 × (1501.0 − 1.007) ≈ 15,000.
- Sensitive to **ion suppression** by salts and co-eluting matrix.

### Atmospheric pressure chemical ionisation (APCI)

- The eluent is sprayed into a **heated nebuliser** (about 350–500 °C) where solvent and analyte are vaporised.
- A **corona discharge needle** ionises solvent molecules, which then transfer protons to the analyte in the gas phase (as in CI).
- Gives mainly singly charged [M + H]⁺; tolerates higher flow rates.
- Suits **less polar, smaller, thermally stable** compounds that ESI ionises poorly (steroids, some lipophilic drugs).

**Atmospheric pressure photoionisation (APPI)** uses a UV lamp to ionise non-polar compounds; useful where both ESI and APCI fail.

| Point | ESI | APCI |
| --- | --- | --- |
| Where ions form | In solution, then released from droplets | In the gas phase after vaporisation |
| Energy source | High voltage on capillary | Heat + corona discharge |
| Best analytes | Polar, ionic, large (proteins, peptides) | Medium to low polarity, smaller, thermally stable |
| Multiple charging | Yes | No (singly charged) |
| Flow rate | Low to moderate | Higher flows tolerated |
| Matrix suppression | More | Less |

**Instrumentation of LC-MS/MS**

```text
 mobile phase ─> pump ─> autosampler ─> column (C18) ─> [UV detector optional] ─> API source (ESI/APCI)
                                                                                         │
       data system <── electron multiplier <── Q3 <── q2 collision cell <── Q1 <── ion optics (vacuum stages)
```

**Practical rules for LC-MS mobile phases**

1. Use **volatile** buffers and additives: formic acid, acetic acid, ammonium formate, ammonium acetate, ammonia.
2. Avoid **non-volatile** salts (phosphate, sulfate buffers) and non-volatile ion-pair reagents: they crystallise in the source and suppress ionisation.
3. Use low flow rates or split the flow; narrow-bore and UHPLC columns suit MS.
4. Use a **stable-isotope-labelled internal standard** (for example a deuterated drug) to correct for ion suppression and extraction losses.
5. Clean samples (SPE, protein precipitation; Unit 4) reduce **matrix effects**.

**Advantages of LC-MS/MS:** handles polar, non-volatile and thermally unstable compounds without derivatisation; very low LOQ (pg/ml); high throughput (run times of a few minutes); identification and quantitation together. **Limitations:** expensive; matrix effects; fewer spectral libraries than EI; needs skilled operators.

**Applications of LC-MS and LC-MS/MS**

1. **Bioanalysis for pharmacokinetic, bioavailability and bioequivalence studies:** drug levels in plasma by MRM.
2. **Drug metabolism:** finding and identifying metabolites (precursor ion and neutral loss scans, accurate mass Q-TOF).
3. **Impurity and degradation product identification** in APIs and formulations; trace genotoxic impurities.
4. **Proteins and biopharmaceuticals:** intact mass, peptide mapping, glycosylation (proteomics).
5. **Therapeutic drug monitoring** of immunosuppressants and other narrow-range drugs.
6. **Newborn screening** and clinical biomarkers.
7. **Natural product dereplication:** quickly recognising known compounds in plant extracts.
8. **Doping, forensic and food safety** (antibiotic residues, mycotoxins).

## 5.5 HPTLC-MS

**HPTLC refresher.** High-performance thin layer chromatography uses plates with fine, uniform particles (about 5–6 µm), automated sample application as narrow bands, controlled development chambers and **densitometric scanning** for quantitation. Many samples and standards run side by side on one plate.

**Why couple HPTLC with MS?** A spot or band on a TLC plate is identified only by its Rf and colour reaction. MS gives the molecular mass and fragments of the compound in the zone, confirming its identity without isolating it.

**Ways of coupling**

| Approach | How it works |
| --- | --- |
| **Offline scraping** | Scrape the zone, extract with solvent, filter and infuse into MS (simple, slow) |
| **Elution-head interface (TLC-MS interface)** | A plunger with an oval or round head presses on the chosen zone and seals it; solvent from an HPLC pump flows through the layer under the head, dissolves the compound and carries it directly to the ESI or APCI source. Takes about a minute per zone |
| **Direct desorption methods** | **DESI** (desorption electrospray: a charged solvent spray hits the plate surface and releases ions), **DART** (direct analysis in real time: excited gas desorbs and ionises), **MALDI** from the plate after matrix application, laser desorption |

**Steps of HPTLC-MS (elution-head method)**

1. Develop the plate; mark zones under UV light or by densitometry (avoid derivatising reagents on zones meant for MS, or use a parallel track).
2. Position the elution head on the zone using the laser crosshair.
3. Pump a suitable volatile solvent (for example methanol with formic acid or ammonium formate) through the zone.
4. Send the eluate to the MS (optionally through a short column to remove silica fines).
5. Record the spectrum; compare with the reference standard spotted on the same plate.
6. Elute a blank area of the plate as a background check.

**Advantages:** fast identification of selected zones; many samples screened on one plate, only interesting zones sent to MS; low solvent use; ideal for complex herbal extracts. **Limitations:** not continuous (zone by zone); possible interference from binders and plate impurities; lower sensitivity than LC-MS/MS; needs volatile elution solvents.

**Applications of HPTLC-MS**

1. Identification of marker compounds and **fingerprinting of herbal drugs** and botanicals.
2. Detecting **adulterants**, for example synthetic drugs illegally added to herbal or "natural" products.
3. Identifying **unknown impurities and degradation products** found during HPTLC stability studies.
4. Detecting **counterfeit** medicines.
5. Screening food contaminants, dyes and residues.
6. Effect-directed analysis: combining a bioassay on the plate with MS to identify the active zone.

## 5.6 Comparison of the three couplings

| Point | GC-MS/MS | LC-MS/MS | HPTLC-MS |
| --- | --- | --- | --- |
| Separation | Gas, capillary column | Liquid, packed column | Planar, silica plate |
| Analytes | Volatile, thermally stable (or derivatised) | Polar, non-volatile, thermally labile, large | Wide range; mainly screening and identification |
| Usual ionisation | EI, CI | ESI, APCI, APPI | ESI/APCI via elution head; DESI, DART, MALDI |
| Interface problem | Small gas flow, direct into source (capillary) | Large solvent load, solved by API | Getting the compound off the plate |
| Library search | Large EI libraries | Limited | Limited |
| Quantitation | Excellent (SIM, MRM) | Excellent (MRM) | Mainly qualitative; quantitation by densitometry |
| Typical pharmacy use | Residual solvents, steroids, forensic work, pesticides | Bioanalysis, metabolites, impurities, biologics | Herbal fingerprinting, adulterant detection |

## Remember

- Hyphenation = online separation + spectroscopic identification; the interface is the key problem.
- MS/MS: Q1 selects precursor → q2 collision cell (CID with Ar or N2) → Q3 analyses products. Product, precursor, neutral loss scans; MRM for quantitation.
- Paracetamol MRM 152 → 110 (loss of ketene, 42).
- GC-MS: helium, capillary column straight into EI source; jet, effusion and membrane separators for packed columns; TIC, EIC, SIM; derivatise polar drugs.
- LC-MS: API sources. ESI (charged droplets, multiply charged proteins, polar analytes); APCI (heated vaporiser + corona needle, less polar); APPI (UV lamp).
- Use volatile buffers; avoid phosphate; isotope-labelled internal standard against ion suppression.
- HPTLC-MS: elution-head interface or DESI/DART/MALDI; herbal fingerprinting and adulterant detection.
