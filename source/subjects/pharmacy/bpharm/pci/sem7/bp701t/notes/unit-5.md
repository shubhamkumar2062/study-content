# Unit 5: Ion exchange, gel and affinity chromatography

The last unit covers three column methods that separate by something other than simple adsorption or partition: **electrical charge** (ion exchange), **molecular size** (gel chromatography) and **specific biological recognition** (affinity chromatography). They are especially important for purifying water, amino acids, proteins, enzymes and antibodies.

## 5.1 Ion exchange chromatography: introduction

**Ion exchange** is a reversible exchange of ions between a solution and an insoluble solid (the ion exchanger) carrying fixed charged groups. The fixed groups hold **counter-ions** of opposite charge, which can be replaced by other ions of the same charge from the solution.

```text
 Cation exchange:  Resin-SO3- H+  +  Na+   <=>  Resin-SO3- Na+  +  H+
 Anion exchange:   Resin-N+(CH3)3 OH-  +  Cl-  <=>  Resin-N+(CH3)3 Cl-  +  OH-
```

In **ion exchange chromatography**, ions in a sample are held by the exchanger to different extents and are then eluted one after another by changing the pH or the ionic strength of the eluent.

## 5.2 Classification of ion exchangers

**By origin**

- **Natural inorganic:** zeolites, clays, permutit (aluminosilicates) used in old water softeners.
- **Synthetic inorganic:** zirconium phosphate, hydrous oxides.
- **Synthetic organic resins:** the most important; cross-linked polymers carrying ionic groups.
- **Modified natural polymers:** cellulose (DEAE-cellulose, CM-cellulose), dextran (DEAE-Sephadex, CM-Sephadex), agarose; used for proteins because their open structure lets large molecules enter.

**By the exchanged ion and strength**

| Type | Functional group | Example resins | Works over pH |
| --- | --- | --- | --- |
| **Strong acid cation exchanger** | Sulphonic acid, –SO3⁻ H⁺ | Dowex 50, Amberlite IR-120, Zeo-Karb 225 | Whole pH range |
| **Weak acid cation exchanger** | Carboxylic acid, –COO⁻ H⁺ | Amberlite IRC-50, CM-cellulose | Ionised only above about pH 6 |
| **Strong base anion exchanger** | Quaternary ammonium, –N⁺(CH3)3 OH⁻ | Dowex 1, Amberlite IRA-400 | Whole pH range |
| **Weak base anion exchanger** | Primary, secondary or tertiary amine | Amberlite IR-45, Dowex 3, DEAE-cellulose | Charged only below about pH 9 |

Some resins carry chelating groups (iminodiacetic acid) and bind heavy metals selectively; **mixed-bed** columns hold both cation and anion resins.

## 5.3 Ion exchange resins: structure and preparation

The commonest resins are made by copolymerising **styrene with divinylbenzene (DVB)**. DVB forms cross-links between the polystyrene chains, making a three-dimensional insoluble network. The beads are then:

- **sulphonated** with concentrated sulphuric acid → strong acid cation exchanger, or
- **chloromethylated** and then treated with trimethylamine → strong base anion exchanger.

Acrylic or methacrylic acid polymers give weak acid exchangers. The **degree of cross-linking** is stated as % DVB (for example Dowex 50-X8 has 8% DVB).

```text
   -CH-CH2-CH-CH2-         polystyrene chain
    |       |
   Ph-SO3H  Ph
            |              <- divinylbenzene cross-link
   -CH-CH2-CH-CH2-
    |
   Ph-SO3H                 sulphonic acid groups = exchange sites
```

## 5.4 Properties of ion exchange resins

1. **Cross-linking:** more DVB makes the resin harder, less swollen, more selective and with smaller pores; less DVB lets large ions in but the resin swells more and is softer. Usual range 2–16%; 8% is common.
2. **Swelling:** resins absorb water and swell; swelling falls with higher cross-linking and higher ionic strength of the solution and depends on the counter-ion.
3. **Exchange capacity:** number of exchangeable groups per unit weight or volume, in **milliequivalents per gram (meq/g)** of dry resin or meq/ml of wet resin. Typical strong acid resins hold about 4–5 meq/g dry. **Determination:** a known weight of resin in the H⁺ form is treated with excess sodium chloride; the released H⁺ is titrated with standard NaOH. Example: 1.0 g resin releases acid needing 42.5 ml of 0.1 M NaOH, so capacity = 42.5 × 0.1/1.0 = **4.25 meq/g**.
4. **Particle size and shape:** spherical beads, usually 50–400 mesh; finer beads give better separation but slower flow.
5. **Selectivity (affinity) of ions:** a resin prefers ions of
   - **higher charge:** Th⁴⁺ > Al³⁺ > Ca²⁺ > Na⁺;
   - **smaller hydrated radius** among ions of equal charge: for cation resins Ag⁺ > Cs⁺ > K⁺ > NH4⁺ > Na⁺ > H⁺ > Li⁺; Ba²⁺ > Sr²⁺ > Ca²⁺ > Mg²⁺;
   - for anion resins: I⁻ > NO3⁻ > Br⁻ > Cl⁻ > OH⁻ > F⁻ (approximately).
6. **Stability:** chemical (resistant to acids, alkalis, many solvents), thermal (strong base resins degrade above about 60 °C in the OH⁻ form), mechanical (resistance to breaking on swelling cycles).
7. **Regeneration:** used resin is converted back to its original form with excess acid (cation resin) or alkali (anion resin) and reused.

## 5.5 Mechanism of the ion exchange process

Exchange takes place by diffusion in steps:

```text
 (1) ion diffuses through the solution to the bead surface (film)
 (2) ion diffuses through the bead to the exchange site (particle)
 (3) exchange at the fixed group (very fast chemical step)
 (4) released ion diffuses back to the bead surface
 (5) released ion diffuses away into the bulk solution
```

The **slowest step controls the rate**: in dilute solutions, film diffusion (steps 1 and 5); in concentrated solutions and highly cross-linked resins, particle diffusion (steps 2 and 4). Stirring, smaller beads and higher temperature speed up exchange.

The equilibrium is described by a **selectivity coefficient**, for A⁺ replacing B⁺: K = [A]resin [B]solution / ([B]resin [A]solution). Ions with K greater than 1 are held more strongly and elute later.

## 5.6 Factors affecting ion exchange

1. **Nature of the exchanger:** strong or weak groups, capacity, cross-linking, particle size.
2. **Charge and size of the ions** (selectivity order above).
3. **pH of the solution:** decides whether weak exchangers and amphoteric solutes (amino acids, proteins) are charged. A protein above its pI is negative and binds anion exchangers; below its pI it is positive and binds cation exchangers.
4. **Ionic strength (concentration of the eluent):** higher salt concentration competes for sites and elutes bound ions; gradients of salt are used for elution.
5. **Temperature:** speeds diffusion and changes selectivity slightly.
6. **Solvent:** organic solvents change swelling and selectivity.
7. **Complexing agents in the eluent** (citrate, EDTA) change the effective charge of metal ions and improve separation (rare earths).
8. **Flow rate and column dimensions.**

## 5.7 Methodology

1. **Choice of resin:** cation or anion, strong or weak, suitable cross-linking and mesh.
2. **Pretreatment (conditioning):** swell the resin in water, wash, and convert it fully to the required ionic form with acid, alkali or salt; wash out the excess.
3. **Packing:** pour as a slurry into a column without air bubbles; keep the bed covered with liquid.
4. **Loading:** apply the sample in a low-ionic-strength buffer at a pH where the wanted ions bind.
5. **Washing:** unbound substances are washed out.
6. **Elution:** by stepwise or gradient increase of ionic strength, or by change of pH; fractions collected.
7. **Detection:** conductivity, UV absorbance, chemical tests (ninhydrin for amino acids).
8. **Regeneration** of the resin for reuse.

## 5.8 Applications of ion exchange

- **Demineralised (DM) water and softening of water:** a cation resin (H⁺ form) followed by an anion resin (OH⁻ form), or a mixed bed, removes salts; Na⁺-form cation resins remove hardness (Ca²⁺, Mg²⁺).
- **Separation of amino acids** (automated amino acid analysers) and of proteins and nucleotides.
- **Separation of similar ions:** rare earths, lanthanides, transition metals.
- **Removal of interfering ions** before an assay; conversion of one salt into another (preparation of a drug's free acid or base).
- **Purification and recovery of antibiotics** (streptomycin, neomycin) and alkaloids from fermentation broths and plant extracts.
- **Drug delivery:** drug–resin complexes (resinates) for taste masking and sustained release (dextromethorphan polistirex is an example of the approach).
- **Therapeutic resins:** cholestyramine (bile acid sequestrant), sodium polystyrene sulphonate (lowering high potassium).
- **Ion chromatography** with conductivity detection for inorganic ions in water and drug salts.

## 5.9 Gel chromatography

### Introduction

**Gel chromatography** (size-exclusion chromatography) separates molecules according to their **size (molecular volume)**, which is related to molecular weight. With water-swollen gels and aqueous eluents it is called **gel filtration**; with organic solvents and polymer gels it is **gel permeation chromatography (GPC)**, used for synthetic polymers.

### Theory

The gel beads have pores of a controlled range of sizes.

```text
  large molecules  -> cannot enter pores -> travel only between beads -> come out FIRST (at V0)
  medium molecules -> enter some pores   -> partly delayed             -> come out in between
  small molecules  -> enter all pores    -> longest path               -> come out LAST

     O O O   <- gel beads with pores
    O . O .
     O O O
```

- **Void volume V0:** volume of liquid between the beads (found with a very large molecule such as Blue Dextran 2000).
- **Internal volume Vi:** volume of liquid inside the pores.
- **Total bed volume Vt** = V0 + Vi + volume of gel matrix.
- **Elution volume: Ve = V0 + Kd·Vi**, where **Kd** is the distribution coefficient (0 for fully excluded molecules, 1 for fully permeating ones, in between for partly included ones).
- In practice **Kav = (Ve − V0)/(Vt − V0)** is used.
- **Exclusion limit:** molecular weight above which molecules cannot enter the pores at all. **Fractionation range:** range of molecular weights the gel separates.
- Within the fractionation range, **Ve is roughly linear with log (molecular weight)**, so a gel column calibrated with standard proteins gives the molecular weight of an unknown.

**Worked example.** V0 = 30 ml, Vi = 60 ml, a protein elutes at Ve = 54 ml: Kd = (54 − 30)/60 = **0.40**. If Vt = 100 ml, Kav = (54 − 30)/(100 − 30) = **0.34**.

Separation is not caused by adsorption; ideally solutes do not interact with the gel at all.

### Gel materials

| Gel | Material | Notes |
| --- | --- | --- |
| **Sephadex** (G-10 to G-200) | Cross-linked dextran (with epichlorohydrin) | The number indicates water regain × 10; G-25 for desalting, G-100/G-200 for proteins |
| **Bio-Gel P** | Polyacrylamide | Chemically inert; wide range of grades |
| **Sepharose / Bio-Gel A** | Agarose | Very large pores; for viruses, large proteins and nucleic acids |
| **Sephacryl, Superdex** | Composite allyl dextran or agarose–dextran | Rigid; faster flow |
| **Styragel, polystyrene–DVB** | Organic-solvent gels | GPC of synthetic polymers |
| Porous silica, porous glass | Rigid inorganic | High-pressure size exclusion |

A good gel is chemically inert, has low ionic content (no adsorption), uniform particle and pore size, and enough mechanical strength.

### Instrumentation and methodology

```text
 GEL CHROMATOGRAPHY SET-UP

 [Eluent reservoir] -> [Pump or gravity feed (peristaltic pump)] -> [Column packed with swollen gel] -> [UV detector at 280 nm or RI] -> [Fraction collector] -> [Recorder]
                                          sample applied as a small volume on top ^
```

1. **Swelling the gel:** dry gel soaked in the eluent (hours at room temperature, faster in a boiling water bath); fine particles removed; degassed.
2. **Packing:** slurry poured in one go into a long, narrow column with a flow adaptor; the bed must be even and free of air.
3. **Testing the bed:** a coloured high-molecular-weight marker (Blue Dextran) should move as a flat, even band; it also gives V0.
4. **Sample application:** a small volume (1–5% of the bed volume) of a clear sample on the bed surface.
5. **Elution:** with the same buffer (isocratic) at a controlled low flow rate.
6. **Detection:** UV at 280 nm for proteins, 260 nm for nucleic acids, refractive index for polymers, conductivity for salts; fractions collected.
7. Modern **size-exclusion HPLC** uses rigid small-particle columns with an HPLC pump.

### Applications

- **Desalting** of proteins and removal of small molecules (buffer exchange) on Sephadex G-25.
- **Purification and fractionation** of proteins, enzymes, polysaccharides, nucleic acids and viruses.
- **Molecular weight determination** of proteins (calibration with standards) and molecular weight distribution of polymers (GPC of polyethylene glycols, povidone, dextrans).
- **Detection of aggregates** in protein drugs (insulin, monoclonal antibodies, vaccines) and of high-molecular-weight impurities.
- Studies of protein–drug binding (free drug separated from bound drug).

**Advantages:** gentle (no binding, so proteins keep their activity), simple isocratic elution, good recovery, predictable elution. **Limitations:** limited resolution (only a few peaks in one run; molecules need about a 10% or larger difference in size), limited sample volume, dilution of the sample.

## 5.10 Affinity chromatography

### Introduction

**Affinity chromatography** separates a biomolecule using its **specific, reversible binding to a ligand** that is chemically attached to an insoluble matrix. Only the molecule that recognises the ligand is retained; everything else passes through. It is the most selective chromatographic method and can purify a protein several thousand-fold in one step.

### Theory

```text
 AFFINITY CHROMATOGRAPHY

 matrix bead --- spacer arm --- ligand        target protein binds   wash out others   elute target
   (agarose)     (6-carbon       (substrate     to ligand  -->         -->              (change pH, salt,
                  chain)          analogue,                                              or add free ligand)
                                  antibody...)
   Step 1 load        Step 2 wash        Step 3 elute        Step 4 regenerate
```

**Specific pairs used**

| Ligand on the matrix | Molecule purified |
| --- | --- |
| Substrate analogue, inhibitor, cofactor (NAD⁺, AMP) | Enzymes (dehydrogenases, kinases) |
| Antigen | Antibody (immunoaffinity) |
| Antibody | Antigen, hormones |
| Protein A or protein G | IgG antibodies |
| Lectin (concanavalin A) | Glycoproteins, polysaccharides |
| Hormone or drug | Receptor |
| Complementary nucleic acid, oligo(dT) | Nucleic acids, mRNA |
| Metal ion (Ni²⁺ on nitrilotriacetic acid) | Proteins with a histidine tag (immobilised metal affinity chromatography) |
| Heparin | Coagulation factors, lipoproteins |
| Dye ligand (Cibacron Blue) | Albumin, nucleotide-binding enzymes |

**Requirements of the matrix:** insoluble, porous, hydrophilic, chemically stable, with groups that can be activated, low non-specific adsorption, good flow. **Agarose (Sepharose)** is the most used; polyacrylamide, cellulose and porous silica are others. Agarose is activated with **cyanogen bromide (CNBr)**, epoxy or N-hydroxysuccinimide groups, then the ligand is coupled.

**Spacer arm:** a short chain (often 6–10 carbon atoms, for example 6-aminohexanoic acid) between matrix and ligand, so that the target can reach the ligand without steric hindrance from the bead surface.

**Requirements of the ligand:** specific and reversible binding of suitable strength (too weak, the target is not held; too strong, it cannot be eluted without damage), a group for attachment that does not interfere with binding, and stability during coupling and use.

### Instrumentation and methodology

The equipment is the same as low-pressure column chromatography: column, pump or gravity flow, UV detector at 280 nm, fraction collector (or an HPLC system for high-performance affinity work, and batch methods in a beaker).

1. **Preparation of the affinity matrix:** activation and ligand coupling, washing off unbound ligand, blocking the remaining active groups.
2. **Equilibration** with binding buffer.
3. **Loading** the crude mixture (cell extract, serum, fermentation broth) under conditions that favour binding.
4. **Washing** away unbound and weakly bound material.
5. **Elution** of the target:
   - **Specific elution:** a solution of free ligand or a competitor displaces the target.
   - **Non-specific elution:** change of pH (glycine–HCl pH 2.5–3 for antibodies, neutralised at once), higher ionic strength, chaotropic agents (urea, guanidine), or a change in polarity.
6. **Regeneration** of the column for reuse.

### Applications

- **Purification of enzymes**, receptors, transport proteins and hormones.
- **Monoclonal and polyclonal antibody purification** on protein A or protein G columns; production of therapeutic antibodies.
- **Recombinant proteins** with tags (His-tag on Ni-NTA, GST-tag on glutathione) in biotechnology.
- **Isolation of nucleic acids** (mRNA on oligo(dT)), glycoproteins on lectins.
- **Removal of unwanted proteins** (removing albumin from serum samples with dye ligands).
- **Immunoaffinity clean-up** of samples before analysis (aflatoxins, drug residues) and studies of drug–receptor binding.

**Advantages:** extremely selective, high purification in one step, concentrates the target, gentle conditions. **Limitations:** a suitable ligand must exist for each target; matrices are costly; ligand may leak; harsh elution can denature the product.

**Comparison of the three methods**

| Feature | Ion exchange | Gel (size exclusion) | Affinity |
| --- | --- | --- | --- |
| Separates by | Charge | Size | Specific biological binding |
| Binding to stationary phase | Yes (electrostatic) | No | Yes (specific) |
| Elution | Salt or pH gradient | Isocratic buffer | Free ligand, pH or salt change |
| Selectivity | Medium | Low | Very high |
| Typical use | Water purification, amino acids, proteins | Desalting, molecular weight | Enzymes, antibodies, tagged proteins |

## Remember

- Ion exchange: reversible exchange of counter-ions; cation exchangers (–SO3H strong, –COOH weak), anion exchangers (quaternary ammonium strong, amines weak).
- Styrene–divinylbenzene resin; % DVB = cross-linking; capacity in meq/g.
- Selectivity: higher charge and smaller hydrated radius are held more strongly.
- Mechanism: film diffusion → particle diffusion → exchange → back diffusion; slowest step controls the rate.
- Gel chromatography: large molecules elute first; Ve = V0 + Kd·Vi; Ve is linear with log M; Sephadex (dextran), Bio-Gel P (polyacrylamide), Sepharose (agarose).
- Affinity: ligand + spacer arm on activated agarose (CNBr); load, wash, elute, regenerate; protein A for IgG, Ni-NTA for His-tag.
