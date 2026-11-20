# Unit 4: Fermentation Technology

Fermentation technology is the large-scale culture of microorganisms or cells to produce a desired product. The term originated with yeast fermentation for ethanol but now covers bacterial, fungal and mammalian cell cultures producing antibiotics, enzymes, amino acids, vitamins, biofuels and biopharmaceuticals.

## 4.1 Types of fermentation

**By oxygen requirement:**

| Type | Organism | Products |
| --- | --- | --- |
| Aerobic fermentation | Bacteria, fungi, actinomycetes | Antibiotics, enzymes, amino acids, recombinant proteins |
| Anaerobic fermentation | Yeast, Clostridium | Ethanol, lactic acid, acetone-butanol, methane |

**By operating mode — the three main process types:**

| Feature | Batch | Fed-batch | Continuous |
| --- | --- | --- | --- |
| Nutrients | Added at start | Added during the run | Added continuously; spent medium removed continuously |
| Volume | Constant | Increases | Constant (inflow = outflow) |
| Growth phase | Full growth curve (lag, log, stationary) | Extended log phase possible | Maintained at a steady state |
| Product accumulation | Ends at harvest | Can accumulate to high level | Steady output |
| Risk of contamination | Lower | Lower | Higher |
| Use | Penicillin, beer | Most industrial fermentations | Wastewater treatment, some amino acids |

**Batch fermentation** is simplest: nutrients, organism and water are added; fermentation proceeds; at the end the vessel is harvested and cleaned. The product yield is limited by exhaustion of nutrients and accumulation of toxic products.

**Fed-batch fermentation** extends the productive phase by feeding nutrients (glucose, nitrogen source, precursors) continuously or periodically. It avoids the repression of secondary metabolite pathways by high initial glucose (the Crabtree effect in yeast) and allows very high cell densities. It is the most used industrial mode for antibiotics and many recombinant proteins.

**Continuous fermentation (chemostat):** Fresh medium is added at a constant dilution rate D = F/V (flow rate / volume); spent medium is withdrawn at the same rate. When D equals the specific growth rate µ, the culture reaches a steady state. If D > µmax, the cells are washed out. Useful for studying growth kinetics; less used industrially because of contamination risk and strain stability concerns over long runs.

## 4.2 Bioreactor design

A bioreactor (fermenter) is a vessel designed to maintain optimal conditions for cell growth and product formation.

**Components of a stirred-tank bioreactor:**

```text
                Air inlet (sparger at the bottom)
                      ↓
          Cooling/heating jacket ─── [STIRRED TANK] ─── Sample port
                      │
        Impeller/agitator (Rushton turbine) ─ mixing and dispersion
                      │
        Baffles (vertical plates on vessel wall) ─ prevent vortex
                      │
        pH probe ─ controls acid/base addition
        DO (dissolved oxygen) probe ─ controls aeration/agitation
        Temperature probe ─ controls jacket temperature
                      │
        Foam probe ─ triggers antifoam addition
        Exhaust gas outlet
```

**Sparger:** The porous ring or disc through which air or oxygen is bubbled into the medium. Bubble size determines mass transfer efficiency (smaller bubbles = more surface area = better oxygen transfer).

**Impeller types:**
- **Rushton turbine** (flat-blade disc turbine): high shear, good oxygen dispersion; can damage fragile mammalian cells.
- **Pitched-blade impeller**: lower shear, better for animal cell culture.
- **Marine propeller**: used in simple mixing applications.

**Baffles** are four vertical plates equally spaced around the vessel wall. They break up the circular flow created by the impeller, converting it to axial flow and improving mixing without increasing shear.

**Air-lift bioreactor:** Mixes the culture by pumping air into one side of an internal draft tube; culture circulates up the aerated side and down the other without mechanical agitation. Lower shear than stirred-tank; suitable for plant cells and mammalian cells. Used for some monoclonal antibody production.

**Hollow-fibre bioreactor:** Cells grow on the shell side of semi-permeable hollow fibres; medium perfuses through the fibres. Very high cell densities; product is secreted and concentrated in the shell space. Used for small-scale mAb production.

**Scale-up considerations:** Moving from a 10-litre laboratory vessel to a 10,000-litre industrial fermenter requires maintaining the same oxygen transfer rate (OTR), mixing time, shear stress and pH gradients. Scale-up criteria include constant tip speed, constant power-to-volume ratio (P/V), or constant mass transfer coefficient (kLa). Temperature and pH control become more difficult at large scale because of the volume-to-surface-area ratio.

## 4.3 Upstream processing

**Medium formulation:** A fermentation medium supplies carbon (glucose, sucrose, starch, molasses), nitrogen (ammonium salts, corn steep liquor, soy protein hydrolysate, urea), phosphorus, sulphur, minerals (Mg, Fe, Zn, Mn) and growth factors (vitamins) depending on the organism. Defined (synthetic) media are used in GMP biopharmaceutical production to avoid lot-to-lot variation; complex media are used in antibiotic fermentations for economy.

**Inoculum preparation:** A cryopreserved master cell bank vial is thawed → inoculated into a shake flask → grown → transferred to a seed fermenter → grown → used to inoculate the production fermenter. This ensures genetic consistency and uniform inoculum quality. For fungi, spore suspensions or mycelial pellet suspensions are used.

**Sterilisation:**

| Method | Principle | Use |
| --- | --- | --- |
| Autoclave (121°C, 15 psi, 15 min) | Moist heat kills all organisms including spores | Batch sterilisation of medium; glassware |
| Continuous sterilisation (HTST) | High temperature (140°C), short time (20–30 s) | Industrial-scale medium sterilisation; less nutrient destruction |
| Filtration (0.2 µm membrane) | Physical removal of microorganisms | Heat-sensitive media components, air inlet, exhaust gas |
| UV radiation | DNA damage | Surface sterilisation; air treatment |

## 4.4 Process parameters

**pH control:** Most bacteria grow at pH 6.5–7.5; fungi at pH 4–6. During fermentation, acid or base accumulates (from organic acid by-products or ammonia uptake). Automatic titration with sterile sodium hydroxide or sulphuric acid maintains the set point. Penicillin production requires careful pH control around 6.5; deviations reduce yield.

**Temperature:** Most bacteria: 30–37°C; fungi: 25–28°C; mammalian cells: 37°C. Temperature control via jacket water and internal coils. A temperature shift (e.g. from 37°C for growth to 30°C for expression) is sometimes used to improve protein solubility.

**Dissolved oxygen (DO):** Aerobic fermentations require DO above a critical minimum (typically 20–30% of air saturation). DO is maintained by increasing stirrer speed, increasing airflow rate, increasing oxygen concentration in the sparge gas, or increasing vessel pressure. DO is measured with a Clark-type polarographic electrode.

**Foam control:** Foam is generated by protein secretion and aeration. Excessive foam blocks the air outlet and can cause contamination. Antifoam agents (silicone oils, polypropylene glycol) are added automatically when a foam detector triggers. Excess antifoam can reduce oxygen transfer.

## 4.5 Penicillin production

Penicillin was the first industrial antibiotic, produced by *Penicillium chrysogenum* (or *P. rubens* in modern taxonomy). The discovery by Fleming (1928), scale-up by Florey and Chain, and the wartime American fermentation programme led to the current industrial process.

**Industrial process:**

```text
1. Inoculum preparation
   Spore stock → shake-flask culture → seed fermenter (5–10% inoculum)

2. Submerged fermentation
   Fed-batch in stirred-tank fermenter (up to 200,000 litres)
   Medium: corn steep liquor (nitrogen + growth factors), lactose or
   glucose as carbon source, precursor (phenylacetic acid or its derivatives
   for penicillin G; phenoxyacetic acid for penicillin V)

3. Process control
   Temperature: 25–26°C
   pH: 6.0–6.5 (critical — penicillin is acid-labile)
   DO: >30% air saturation
   Glucose fed-batch feeding to avoid catabolite repression
   Precursor added continuously to direct synthesis to the right side chain

4. Harvest and extraction
   After 6–8 days when penicillin titre peaks and growth stops
   Mycelium removed by vacuum filtration or centrifugation
   Broth acidified to pH 2–3 (penicillin is extracted into organic solvent)
   Re-extract into aqueous buffer at neutral pH
   Activated charcoal treatment → crystallisation as potassium salt
```

**Kinetics:** Penicillin is a secondary metabolite — it is produced in the **idiophase** (stationary phase), after active growth (trophophase) has ended or slowed. This is **non-growth-associated production** in Luedeking-Piret terms. This is why fed-batch feeding (slowly feeding glucose to maintain low glucose concentrations) is used: fast growth consumes glucose and suppresses penicillin synthesis via catabolite repression.

**Streptomycin** (Streptomyces griseus): first aminoglycoside, submerged fermentation in stirred-tank; not growth-linked.
**Erythromycin** (Saccharopolyspora erythraea): macrolide antibiotic; similar submerged fed-batch process; precursor propionate fed to build the macrolide ring.

## 4.6 Secondary metabolite production kinetics

**Luedeking-Piret model:**

```text
Product formation rate = α × (growth rate) + β × (biomass)
Where α is growth-associated and β is non-growth-associated coefficient
```

- **Growth-associated products** (α >> 0, β ≈ 0): formed during active growth; e.g. primary metabolites (ethanol, lactic acid).
- **Non-growth-associated products** (α ≈ 0, β >> 0): formed mainly during stationary phase; e.g. antibiotics (penicillin, streptomycin), alkaloids.
- **Mixed type** (both α and β significant): e.g. xanthan gum.

The idiophase begins when growth slows due to nutrient limitation or product inhibition; regulatory genes then switch on secondary metabolic pathways.

## 4.7 Enzyme production by fermentation

Industrial enzymes are produced by submerged fermentation of bacteria or fungi.

| Enzyme | Producer organism | Industrial use |
| --- | --- | --- |
| Amylase (alpha) | *Bacillus licheniformis*, *Aspergillus oryzae* | Starch hydrolysis, food, detergents |
| Protease | *Bacillus subtilis*, *Aspergillus niger* | Detergents, food processing, leather |
| Lipase | *Candida rugosa*, *Rhizomucor miehei* | Biodiesel, food, cosmetics |
| Glucose isomerase | *Streptomyces* spp. | High-fructose corn syrup production |
| Cellulase | *Trichoderma reesei* | Textile, biofuel, paper |

Enzyme fermentations are usually aerobic fed-batch processes. Extracellular enzymes (secreted by the organism) are easier to harvest than intracellular ones.

## 4.8 Solid-state fermentation vs submerged fermentation

| Feature | Submerged fermentation (SmF) | Solid-state fermentation (SSF) |
| --- | --- | --- |
| Moisture | High (80–90%) | Low (20–70%); substrate is moistened solid |
| Substrate | Defined liquid medium | Agricultural residues, bran, etc. |
| Scale-up | Easy; well-controlled | Difficult; heat and mass transfer problems |
| Product concentration | Lower | Higher per g substrate |
| Industrial use | Most biopharmaceuticals, antibiotics, enzymes | Traditional fermented foods, some enzymes, composting |

Traditional fermented foods (soy sauce via *Aspergillus oryzae* koji; tempeh via *Rhizopus oligosporus*) use SSF.

## 4.9 GMP requirements in fermentation facilities

For biopharmaceutical fermentation under GMP:
- **Closed systems** to prevent contamination
- **In-line sensors** (pH, DO, temperature, biomass) with electronic data recording
- **Validated sterilisation-in-place (SIP) and cleaning-in-place (CIP)** systems
- **Sterility testing** of the inoculum and the final batch
- **Master cell bank (MCB) and working cell bank (WCB)** system to ensure genetic consistency
- **Environmental monitoring** of manufacturing suites
- **Batch records** documenting every step and all deviations

## Remember

1. Batch = fixed volume, one shot; fed-batch = nutrients added during the run = most industrial antibiotic and recombinant protein fermentations; continuous = steady state, medium in and out constantly.
2. Penicillin is produced by *Penicillium chrysogenum* in a fed-batch aerobic submerged process; it is a non-growth-associated (idiophase) secondary metabolite.
3. The stirred-tank bioreactor components to draw: sparger (air inlet), impeller/agitator, baffles (prevent vortex), pH and DO probes, jacket (temperature control), foam detector.
4. Precursor feeding (phenylacetic acid for Pen G, phenoxyacetic acid for Pen V) channels biosynthesis towards the desired penicillin side chain.
5. Scale-up criteria include constant P/V (power per unit volume) or constant kLa (oxygen mass transfer coefficient).
6. GMP fermentation facilities require validated SIP, CIP, master and working cell banks, closed systems and full batch records.
7. Solid-state fermentation uses low moisture on solid substrates; submerged fermentation uses liquid medium; SmF is preferred for pharmaceutical production.
8. Alpha-amylase (Bacillus), protease (Bacillus, Aspergillus) and lipase (Candida, Rhizomucor) are the most important industrial enzymes from fermentation.
