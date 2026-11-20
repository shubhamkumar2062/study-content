# Unit 4: Chromatography

Chromatography separates the components of a mixture by distributing them between a **stationary phase** and a **mobile phase** that moves past it. Components that interact more with the stationary phase move more slowly. It is the backbone of pharmaceutical analysis: assay and related substances of almost every IP monograph, stability-indicating methods, dissolution of combinations, residual solvents, bioanalysis and purification. The PCI syllabus asks, for paper, thin-layer, ion exchange, column, gas, high-performance liquid and affinity chromatography, about the principle, apparatus, instrumentation, chromatographic parameters, factors affecting resolution and applications. This unit first builds the common theory, then takes each technique in turn.

## 4.1 Classification

| Basis | Types |
| --- | --- |
| Mechanism | Adsorption, partition, ion exchange, size exclusion (gel), affinity, chiral |
| Mobile phase | Liquid (LC), gas (GC), supercritical fluid (SFC) |
| Bed shape | Planar (paper, TLC, HPTLC); column (open column, HPLC, GC) |
| Purpose | Analytical; preparative |
| Polarity | Normal phase (polar stationary, non-polar mobile); reversed phase (non-polar stationary, polar mobile) |

**Mechanisms in brief**
- **Adsorption**: solutes compete with the mobile phase for active sites on a solid surface (silica, alumina). Polar solutes held more on silica.
- **Partition**: solute distributes between two liquids, one held on a support (paper water, bonded C18 chains). Governed by the partition (distribution) coefficient K = Cs/Cm.
- **Ion exchange**: charged solutes exchange with counter-ions on a charged resin.
- **Size exclusion**: molecules separate by size in a porous gel; large ones elute first.
- **Affinity**: specific biological binding (enzyme–inhibitor, antigen–antibody).

## 4.2 Chromatographic parameters

```text
 Detector
 response      t0 (dead time)     tR1        tR2
   ^             |                 /\         /\
   |             |                /  \       /  \
   |____________ |______________ /    \_____/    \______→ time
                                 |<W1>|     |<W2>|   (W = base width by tangents)
```

| Parameter | Formula | Meaning |
| --- | --- | --- |
| Retention time tR | measured | Time from injection to peak maximum |
| Dead time t0 (tM) | measured with an unretained marker (uracil in RP-HPLC, methane in GC) | Time for the mobile phase to pass through |
| Adjusted retention time | t′R = tR − t0 | Time actually spent in the stationary phase |
| Retention (capacity) factor | k = (tR − t0)/t0 = K × Vs/Vm | Ideal 1–10 (2–10 in HPLC); too low = poor separation, too high = long run, broad peaks |
| Selectivity (separation) factor | α = k2/k1 (> 1) | Chemical ability to tell two solutes apart |
| Theoretical plates | N = 16 (tR/W)² = 5.54 (tR/W½)² | Column efficiency |
| Height equivalent to a theoretical plate | H (HETP) = L/N | Smaller H = more efficient column |
| Resolution | Rs = 2(tR2 − tR1)/(W1 + W2) = 1.18 (tR2 − tR1)/(W½1 + W½2) | Rs ≥ 1.5 = baseline separation; IP system suitability often asks for ≥ 1.5 or 2.0 |
| Tailing (symmetry) factor | T = W0.05/2f (at 5% height) | 1 = symmetric; IP usually ≤ 2.0 |
| Retardation factor (planar) | Rf = distance by solute / distance by solvent front | 0 to 1 |

**Worked example**: tR1 = 6.0 min, tR2 = 6.6 min, t0 = 1.0 min, both base widths 0.40 min, column 250 mm.
- N (peak 1) = 16 × (6.0/0.40)² = 3600 plates; H = 250 mm / 3600 = 0.069 mm = 69 µm.
- k1 = 5.0, k2 = 5.6; α = 5.6/5.0 = 1.12.
- Rs = 2 × (6.6 − 6.0)/(0.40 + 0.40) = 1.5 → just baseline-resolved.

**System suitability** (pharmacopoeial): before analysis, replicate injections must meet limits for resolution, tailing, plate count, RSD of peak area (often ≤ 2.0% for assay) and signal-to-noise for impurity limits.

## 4.3 Factors affecting resolution

**Purnell (master resolution) equation**:

```text
 Rs = (√N / 4) × ((α − 1)/α) × (k / (1 + k))
       efficiency   selectivity   retention
```

1. **Efficiency (N)**: longer column, smaller particles (5 → 3 → sub-2 µm), well-packed bed, low extra-column volume, optimum flow. Rs rises only with √N, so doubling column length raises Rs by about 1.4 and doubles run time.
2. **Selectivity (α)**: the most powerful lever — change the stationary phase (C18 → phenyl → cyano), organic modifier (methanol ↔ acetonitrile ↔ THF), pH relative to the pKa of ionisable drugs, ion-pair reagent, temperature, buffer type.
3. **Retention (k)**: adjust mobile phase strength (percentage organic in RP-HPLC, temperature programme in GC). Gains level off above k ≈ 10.

**Band broadening — van Deemter equation**:

```text
 H = A + B/u + C·u          u = linear velocity of mobile phase
 A = eddy (multiple path) diffusion: 2λdp — depends on particle size and packing
 B = longitudinal (molecular) diffusion: 2γDm — matters at low flow, large in GC
 C = resistance to mass transfer (Cs + Cm) — matters at high flow
 H vs u is a curve with a minimum at the optimum velocity (uopt)
```

Smaller particles reduce A and C, flattening the curve so higher flow is possible without loss of efficiency — the basis of UHPLC. In open-tubular GC columns A = 0 (Golay equation).

Other factors: column temperature (lowers viscosity, speeds mass transfer, changes α), sample load (overloading broadens and distorts peaks), injection solvent stronger than the mobile phase (distorted peaks), dead volume in tubing and detector cell.

## 4.4 Paper chromatography

**Principle**: mainly **partition** between water held in the cellulose fibres (stationary) and an organic mobile phase; some adsorption and ion exchange also occur.

**Apparatus and method**
- Whatman No. 1 (medium) or No. 3 (thick, preparative) paper; may be impregnated (formamide, paraffin for reversed phase).
- Sample spotted with a capillary on a pencil baseline about 2 cm from the edge; spots kept small and dried.
- Mobile phase example: n-butanol : acetic acid : water (4:1:5, upper layer) for amino acids and sugars.
- Chamber saturated with solvent vapour before development.

**Development techniques**: ascending, descending (faster, for low-Rf compounds; solvent can run off the end), radial/circular, and **two-dimensional** (develop, dry, turn 90°, develop with a second solvent — resolves complex mixtures such as protein hydrolysates).

**Detection**: ninhydrin (amino acids, purple), aniline hydrogen phthalate (sugars), iodine vapour, UV light, ferric chloride (phenols), Dragendorff (alkaloids).

**Factors affecting Rf**: nature of paper, solvent composition and purity, temperature, chamber saturation, pH, distance and direction of development, sample amount.

**Applications**: amino acids, sugars, simple separations in teaching, phytochemical screening; largely replaced by TLC.

## 4.5 Thin-layer chromatography (TLC) and HPTLC

**Principle**: mainly **adsorption** on silica gel (or alumina); partition on cellulose or reversed-phase layers.

**Stationary phases**: silica gel G (with gypsum binder), silica gel GF254 (with a fluorescent indicator — UV-absorbing spots appear dark on a green background at 254 nm), alumina, cellulose, kieselguhr, C18 bonded silica. Layer thickness 0.25 mm (analytical) to 1–2 mm (preparative). Plates are activated by heating (about 110 °C for 30–60 min) to remove water.

**Steps**: plate preparation (spreading, pouring, dipping, or precoated plates) → activation → spotting → development in a saturated twin-trough chamber → drying → detection (UV 254/366 nm, iodine, charring with sulphuric acid, anisaldehyde, ninhydrin, Dragendorff) → Rf calculation (e.g. 4.2 cm / 10.5 cm = 0.40).

**Mobile phase selection**: the **eluotropic series** orders solvents by eluting strength on silica — hexane < toluene < chloroform < dichloromethane < ethyl acetate < acetone < ethanol < methanol < water. Mixtures are tuned to give Rf about 0.2–0.8.

**HPTLC (high-performance TLC)**: smaller, more uniform particles (about 5 µm), thinner layers, automated band application (spray-on), automated development, densitometric scanning, and validated quantitation. Gives sharper bands, more samples per plate, lower solvent use, and quantitative results — widely used for herbal fingerprinting and marker assay.

**Applications**: identity test and limit test for related substances in IP monographs (comparison with a diluted reference spot), monitoring reactions, checking column fractions, herbal drug fingerprinting, detection of adulterants, stability screening.

**TLC vs paper chromatography**: TLC is faster, gives compact spots and higher resolution, tolerates corrosive spray reagents (charring), and offers many stationary phases.

## 4.6 Column chromatography (classical, open column)

**Principle**: adsorption (silica, alumina, charcoal) or partition, in a vertical glass column under gravity (or low pressure in flash chromatography).

**Apparatus and method**
- Glass column with a stopcock and cotton or sintered-glass plug.
- **Packing**: wet (slurry) method — preferred, no air bubbles or cracks — or dry method. A layer of sand on top protects the bed.
- **Adsorbent activity**: alumina graded by Brockmann activity (I most active, adjusted by adding water); particle size 60–200 µm (flash: 40–63 µm).
- **Sample loading**: as a concentrated band in minimum solvent or adsorbed on a little silica.
- **Elution**: isocratic, stepwise or gradient increase of polarity (eluotropic series); **frontal analysis**, **displacement** and **elution** development.
- Fractions collected and monitored by TLC.

**Factors affecting separation**: particle size, column length-to-diameter ratio (about 10:1 to 30:1), adsorbent activity, solvent polarity, flow rate, temperature, sample amount (about 1/30–1/100 of adsorbent weight).

**Applications**: purification of synthetic products, isolation of natural products (alkaloids, glycosides), separation of plant pigments, removal of impurities; gel filtration columns (Sephadex) for desalting proteins.

## 4.7 Ion exchange chromatography

**Principle**: reversible exchange of ions in solution with ions of like charge bound to an insoluble resin.

```text
 Cation exchanger:  R–SO3⁻ H⁺  + Na⁺  ⇌  R–SO3⁻ Na⁺ + H⁺
 Anion exchanger:   R–N(CH3)3⁺ OH⁻ + Cl⁻ ⇌ R–N(CH3)3⁺ Cl⁻ + OH⁻
```

**Resins**
- Matrix: polystyrene cross-linked with divinylbenzene (DVB, 2–16%; more cross-linking = more rigid, less swelling, smaller pores), cellulose, dextran, agarose (for proteins).
- **Strong acid cation** (sulphonic acid, –SO3H), **weak acid cation** (carboxylic, –COOH), **strong base anion** (quaternary ammonium), **weak base anion** (primary to tertiary amines, DEAE). Strong exchangers are ionised over the whole pH range; weak ones only in a limited range.
- Properties: exchange capacity (meq/g), swelling, cross-linking, particle size, selectivity (higher charge and smaller hydrated radius bind more strongly: Ca²⁺ > Na⁺; for anions, citrate > sulphate > chloride).

**Method**: column packed with swollen, converted resin → sample applied at a pH and ionic strength where the analyte binds → elution by increasing ionic strength (salt gradient) or changing pH → regeneration (acid for cation resins, alkali for anion resins).

**Factors affecting separation**: pH (controls charge of analyte and weak resins), ionic strength, cross-linking, temperature, flow rate, nature of counter-ion, presence of organic solvent.

**Ion chromatography**: HPLC-scale ion exchange with **suppressed conductivity** detection (a suppressor removes the eluent's own conductivity) for inorganic anions and cations (chloride, sulphate, nitrate, sodium, potassium) and counter-ion content of drug salts.

**Applications**: water demineralisation (purified water), separation of amino acids, proteins (charge variants of monoclonal antibodies), nucleotides; removal of interfering ions before assay; **drug–resin complexes (resinates)** for taste masking and sustained release (e.g. dextromethorphan polistirex) — a formulation link; recovery of antibiotics from fermentation broths.

## 4.8 Gas chromatography (GC)

**Principle**: partition (gas–liquid, GLC) or adsorption (gas–solid, GSC) of **volatile, thermally stable** compounds between a carrier gas and a stationary phase in a heated column.

```text
 Carrier gas cylinder → pressure/flow regulator → injector (heated) → column in oven
 (He, N2, H2)                                  (split/splitless,     (temperature
                                                headspace)            programmed)
                                                → detector (heated) → data system
```

**Components**
1. **Carrier gas**: helium (inert, efficient), nitrogen (cheap, best at low velocity), hydrogen (fastest optimum, flammable). Must be pure and dry (moisture and oxygen traps).
2. **Injector**: split (only a fraction enters the column; concentrated samples), splitless (trace analysis), on-column, programmed temperature vaporiser; **static headspace** sampler for residual solvents (vapour above a heated sample vial is injected — the IP/ICH Q3C method).
3. **Columns**: packed (2–3 m, 2–4 mm id; stationary phase on diatomaceous earth) or **capillary/open tubular** (WCOT, 15–60 m, 0.1–0.53 mm id, fused silica with polyimide coating) — much higher efficiency. Stationary phases: polydimethylsiloxane (non-polar), 5% phenyl, 50% phenyl, cyanopropyl, polyethylene glycol (Carbowax, polar). Like dissolves like: choose polarity similar to the analytes.
4. **Oven**: isothermal or **temperature programming** (steady rise) to elute wide-boiling mixtures with sharp peaks in reasonable time.
5. **Detectors**

| Detector | Principle | Selectivity / notes |
| --- | --- | --- |
| Flame ionisation (FID) | Organic compounds burned in H2–air flame produce ions; current measured | Almost universal for organics; no response to water, CO2, inert gases; wide linear range; destructive. Standard for residual solvents |
| Thermal conductivity (TCD) | Change in conductivity of the carrier gas changes the temperature and resistance of a heated filament | Universal (including water, gases), non-destructive, less sensitive |
| Electron capture (ECD) | β-emitter (⁶³Ni) ionises carrier; electronegative analytes capture electrons and reduce the standing current | Very sensitive to halogens, nitro groups; pesticides |
| Nitrogen–phosphorus (NPD) | Alkali bead enhances ionisation of N and P compounds | Drugs with nitrogen, organophosphates |
| Flame photometric (FPD) | Emission of S and P species in flame | Sulphur, phosphorus |
| Mass spectrometer (GC–MS) | Ionisation and m/z | Identification and trace analysis |

**Derivatisation**: makes polar, non-volatile or unstable compounds suitable for GC — silylation (BSTFA, TMCS for –OH, –COOH, –NH), acylation, alkylation/esterification (methyl esters of fatty acids).

**Retention index** (Kovats): expresses retention relative to n-alkanes, helping identification across instruments.

**Applications**: residual solvents (ICH Q3C, headspace GC-FID), assay of volatile drugs and essential oils (camphor, menthol), fatty acid composition of oils (as methyl esters), alcohol content in tinctures and elixirs, ethylene oxide residues, genotoxic alkyl halides and nitrosamines (GC–MS), anaesthetic gases, forensic toxicology.

## 4.9 High-performance liquid chromatography (HPLC)

**Principle**: liquid chromatography on columns of very small particles (sub-2 to 5 µm), so a high-pressure pump is needed; most methods are **reversed-phase partition** on bonded silica.

```text
 Solvent reservoirs → degasser → high-pressure pump → injector (autosampler,
 (filtered)          (helium      (reciprocating,     loop) → guard column →
                      sparging,     gradient mixer)     analytical column (in oven)
                      vacuum)                           → detector → data system
```

**Components**
1. **Solvents and degassing**: HPLC grade, filtered (0.45 or 0.22 µm), degassed (online vacuum, helium sparging, sonication) to avoid bubbles in pump and detector.
2. **Pump**: reciprocating dual-piston pumps give pulse-free flow up to about 400 bar (HPLC) or 1000–1300 bar (UHPLC). Isocratic or **gradient elution** (high-pressure mixing with two pumps, or low-pressure mixing with a proportioning valve).
3. **Injector**: Rheodyne six-port valve with a fixed loop (e.g. 20 µL) or autosampler — precise, reproducible.
4. **Columns**: stainless steel, typically 150–250 × 4.6 mm, 5 µm (UHPLC 50–100 × 2.1 mm, sub-2 µm). Guard column protects the analytical column.
   - **Stationary phases**: silica (normal phase), C18 (ODS), C8, phenyl, cyano, amino; end-capping masks residual silanols that cause tailing of basic drugs; core–shell (superficially porous) particles give high efficiency at moderate pressure; monolithic columns; chiral stationary phases (polysaccharide derivatives, cyclodextrins, proteins) for enantiomers.
5. **Mobile phase**: water/buffer + methanol or acetonitrile. Buffer pH set about 2 units away from the drug's pKa so it is fully ionised or un-ionised (robust retention). **Ion-pair chromatography** adds an oppositely charged reagent (alkyl sulphonates for bases, tetrabutylammonium for acids) to retain ions on RP columns.
6. **Detectors**

| Detector | Principle | Notes |
| --- | --- | --- |
| UV-visible (fixed or variable λ) | Absorbance | Most common; needs a chromophore |
| Photodiode array (PDA/DAD) | Full spectrum each moment | Peak purity, identification |
| Fluorescence | Emission | ng–pg sensitivity, selective; derivatisation possible |
| Refractive index (RI) | Change in refractive index | Universal (sugars, polymers); no gradient; temperature-sensitive |
| Evaporative light scattering (ELSD), charged aerosol (CAD) | Nebulise, evaporate mobile phase, measure particles | Non-chromophoric compounds (lipids, surfactants, excipients); gradient-compatible |
| Electrochemical (amperometric) | Oxidation/reduction current | Catecholamines, very sensitive |
| Conductivity | Ionic conductance | Ion chromatography |
| Mass spectrometer (LC–MS) | m/z | Identification, bioanalysis |

**Normal vs reversed phase**

| Feature | Normal phase | Reversed phase |
| --- | --- | --- |
| Stationary phase | Polar (silica, amino, cyano) | Non-polar (C18, C8) |
| Mobile phase | Non-polar (hexane + IPA) | Polar (water/buffer + MeOH/ACN) |
| Elution order | Non-polar first | Polar first |
| Increasing solvent strength | More polar solvent | More organic solvent |
| Use | Isomers, very non-polar compounds, chiral | About 80% of pharmaceutical methods |

**Method development and validation (brief)**: choose column and mobile phase from analyte properties (pKa, log P, UV); optimise k, α and Rs; apply system suitability; validate per **ICH Q2(R2)** — specificity (forced degradation for stability-indicating methods), linearity, range, accuracy, precision (repeatability, intermediate), detection and quantitation limits, robustness.

**Applications**: assay and related substances of APIs and dosage forms, content uniformity and dissolution of combinations, stability-indicating methods, chiral purity, bioanalysis (with fluorescence or MS), preparative purification, drug release from nanoparticles and implants, encapsulation efficiency, polymer and excipient analysis (size exclusion with RI).

**GC vs HPLC**: GC needs volatile, heat-stable analytes and is excellent for solvents and small volatile molecules; HPLC handles non-volatile, polar, thermally labile and large molecules and covers most drugs.

## 4.10 Affinity chromatography

**Principle**: a highly **specific, reversible biological interaction** between the target molecule and a **ligand** covalently attached to an insoluble support. Only molecules that recognise the ligand bind; everything else washes through.

| Ligand | Binds |
| --- | --- |
| Substrate analogue, inhibitor, cofactor (NAD, ATP) | Enzymes |
| Antibody | Antigen (immunoaffinity) |
| Antigen | Antibody |
| **Protein A / Protein G** | Fc region of IgG antibodies — the capture step in monoclonal antibody manufacture |
| Lectins (concanavalin A) | Glycoproteins with specific sugars |
| Heparin | Coagulation factors, growth factors |
| Metal ions (Ni²⁺, Co²⁺) — IMAC | Histidine-tagged recombinant proteins |
| Oligo(dT) | mRNA with poly(A) tail |
| Dyes (Cibacron blue) | Albumin, dehydrogenases |
| Biotin / avidin–streptavidin | Biotinylated molecules |

**Steps**

```text
 1. Matrix (agarose, cross-linked dextran, polyacrylamide, silica) activated
    (cyanogen bromide, epoxy, NHS ester) → ligand coupled, often through a
    SPACER ARM (6–10 carbon chain) so the binding site is not hindered
 2. Equilibrate column with binding buffer
 3. Load sample → target binds, contaminants pass
 4. Wash away unbound material
 5. Elute target: change pH (low pH 3 for protein A), raise ionic strength,
    add free competing ligand (imidazole for His-tag, glucose for lectin),
    chaotropic agents, or change temperature
 6. Regenerate and re-equilibrate the column
```

**Requirements of a ligand**: specific and reversible binding, dissociation constant about 10⁻⁴–10⁻⁸ M (too strong makes elution damaging), a functional group for coupling that does not destroy binding.

**Factors affecting separation**: ligand density, spacer length, pH and ionic strength of binding buffer, flow rate (slow loading for full binding), temperature, non-specific adsorption.

**Applications**: purification of enzymes, antibodies, receptors, recombinant proteins (single step, high purity and yield); removal of specific contaminants (endotoxin, albumin); immunoaffinity clean-up of samples for trace analysis (aflatoxins); studying drug–protein and receptor binding (frontal affinity chromatography); high-performance affinity columns for drug–plasma protein binding screening.

## 4.11 Comparison table for quick revision

| Technique | Main mechanism | Typical stationary phase | Typical application |
| --- | --- | --- | --- |
| Paper | Partition | Water in cellulose | Amino acids, sugars |
| TLC/HPTLC | Adsorption | Silica gel GF254 | Identity, related substances, herbal fingerprint |
| Column | Adsorption | Silica, alumina | Purification, isolation |
| Ion exchange | Ion exchange | Sulphonated or quaternised resin | Water, amino acids, proteins, resinates |
| GC | Partition (gas–liquid) | Polysiloxane, PEG | Residual solvents, volatiles |
| HPLC | Partition (RP) | C18 bonded silica | Assay, impurities, bioanalysis |
| Affinity | Biospecific binding | Ligand on agarose | Protein and antibody purification |

## Remember

- k = (tR − t0)/t0 (ideal 2–10); α = k2/k1; N = 16(tR/W)² = 5.54(tR/W½)²; H = L/N; Rs = 2ΔtR/(W1 + W2), baseline at 1.5.
- Rs = (√N/4)((α − 1)/α)(k/(1 + k)); selectivity is the strongest lever.
- van Deemter H = A + B/u + Cu; smaller particles flatten the curve (UHPLC).
- Paper = partition; TLC = adsorption; HPTLC = automated, densitometric, quantitative.
- Ion exchange: strong/weak, cation/anion resins; DVB cross-linking; elute with salt or pH; resinates in formulation.
- GC: volatile and heat-stable; capillary columns; FID universal for organics, ECD halogens, NPD nitrogen; headspace for residual solvents; derivatise polar analytes.
- HPLC: pump, injector, column, detector; RP C18 with buffer–ACN; pH 2 units from pKa; validate per ICH Q2(R2).
- Affinity: ligand + spacer arm + matrix; protein A for antibodies, IMAC for His-tags; elute by pH, salt or competitor.
