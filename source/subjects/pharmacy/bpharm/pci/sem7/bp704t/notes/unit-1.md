# Unit 1: Controlled drug delivery systems and polymers

A conventional tablet releases its whole dose at once. Blood levels rise quickly, peak, then fall, so the patient must take another dose a few hours later. Over a day the level swings up and down, sometimes above the safe range and sometimes below the effective range. **Controlled drug delivery** tries to flatten these swings by releasing the drug slowly and at a predictable rate. This unit covers the ideas, the design principles and the polymers used to build such systems.

## 1.1 Introduction and terminology

A **controlled drug delivery system (CDDS)** is a dosage form that releases the drug at a predetermined rate, for a set period, so that a nearly constant drug level is kept in the blood or at the target tissue. The ideal release follows **zero-order kinetics**: the same amount of drug leaves the system every hour, whatever the amount left inside.

| Term | Meaning | Example |
| --- | --- | --- |
| Sustained release (SR) | Drug released slowly over a long time; rate is not necessarily constant (often first order) | Matrix SR tablets |
| Controlled release (CR) | Release rate is predictable and reproducible, ideally zero order; the system controls the level in the body | Osmotic pump tablets, transdermal patches |
| Prolonged / extended release (ER, XL) | Gives a longer duration of action than the conventional form; terms often used for SR products | Once-daily ER tablets |
| Delayed release | Release starts only after a lag time or at a chosen site | Enteric-coated tablets |
| Repeat action | Two doses in one unit: one released at once, the second after a delay | Repeat-action tablets with an inner core |
| Site-specific / targeted release | Drug delivered mainly to an organ, tissue or cell | Liposomes, antibody conjugates |
| Receptor targeting | Drug reaches a specific receptor inside the target cell | Ligand-coated nanoparticles |

```text
Plasma level
   |      conventional (each dose)
   | MTC ...../\....../\....../\........  minimum toxic level
   |        /  \    /  \    /  \
   |       /    \  /    \  /    \         controlled release
   |  ----/------\/------\/------\------  ________________
   | MEC /                                 steady level inside window
   |____/__________________________________________ time
        dose 1    dose 2    dose 3
```

The space between the **minimum effective concentration (MEC)** and the **minimum toxic concentration (MTC)** is the **therapeutic window**. A controlled-release product aims to keep the level inside this window for the whole dosing interval.

## 1.2 Rationale, advantages and disadvantages

**Rationale.** Many drugs are cleared quickly, so a conventional form must be taken three or four times a day. Missed doses cause dips below the MEC; large doses cause peaks near the MTC. Controlling the release rate solves both problems.

**Advantages**

1. Fewer doses per day, so better patient compliance (once- or twice-daily dosing).
2. Steadier plasma levels with less "peak and trough" fluctuation.
3. Fewer dose-related side effects (for example less gastric irritation and fewer peak-level effects).
4. Smaller total amount of drug may be needed, since less is wasted at peaks.
5. Night-time dosing is avoided; therapy continues while the patient sleeps.
6. Better control of chronic diseases (hypertension, angina, diabetes, pain).
7. Lower overall health-care cost through better outcomes and fewer visits, despite a higher product cost.

**Disadvantages**

1. **Dose dumping**: if the system fails (for example crushing, chewing or alcohol with some products), a large dose may be released at once.
2. The dose cannot be adjusted easily; tablets usually must not be split.
3. If side effects occur, the drug cannot be removed quickly from the body.
4. More expensive to develop and make.
5. Poor in vitro–in vivo correlation for some products.
6. Gut transit time limits oral systems to about 12–24 hours of release.
7. Unsuitable for drugs with special absorption problems (see selection criteria).

## 1.3 Selection of drug candidates

Not every drug is suitable for controlled release. The general requirements are:

| Property | Suitable | Unsuitable / difficult |
| --- | --- | --- |
| Biological half-life | Short to moderate (roughly 2–8 h) | Very short (under about 1 h: too much drug needed) or long (over about 12 h: already long acting) |
| Dose | Small to moderate | Very large doses (product becomes too big) |
| Therapeutic index | Reasonably wide | Very narrow (dose dumping dangerous) |
| Absorption | Well absorbed along the whole gut | Absorbed only in a narrow "window" in the upper intestine |
| Aqueous solubility | Moderate | Extremely low (release controlled by poor solubility already) |
| Stability | Stable in gut fluids | Unstable in stomach or intestine |
| First-pass metabolism | Low to moderate | Extensive, saturable metabolism (slow input may reduce bioavailability) |
| Mode of action | Effect related to plasma level | Effect not related to level, or tolerance develops with constant levels |

Typical examples of drugs given as SR/CR products are theophylline, diltiazem, nifedipine, metformin, diclofenac, isosorbide mononitrate and potassium chloride.

## 1.4 Physicochemical properties of drugs relevant to controlled release

1. **Dose size.** For oral products the whole dose for the dosing interval must fit in one unit. A very large dose makes the tablet too big to swallow.
2. **Aqueous solubility.** Drugs with very low solubility already dissolve slowly, so their release is limited by dissolution and adding a release barrier gives little benefit. Very soluble drugs are hard to slow down and may need special matrices or coatings. Solubility also changes with pH along the gut, which can change the release rate.
3. **pKa and ionisation.** Only the un-ionised form crosses membranes easily. A drug whose ionisation changes greatly between stomach and intestine may show pH-dependent release and absorption.
4. **Partition coefficient (log P).** Drugs with very high log P stay in membranes and fat; drugs with very low log P cross membranes poorly. A moderate value is best. Log P also affects diffusion through polymer membranes.
5. **Stability.** Drugs unstable in acid (some penicillins) or degraded by intestinal enzymes are poor candidates for systems that release slowly along the gut.
6. **Molecular size and diffusivity.** Diffusion through polymers slows as molecular weight rises. Large molecules such as peptides diffuse very slowly through dense polymers and need porous or biodegradable systems.
7. **Protein binding.** Highly protein-bound drugs already have a long duration of action; binding also affects the free concentration available for effect.

## 1.5 Biological properties of drugs relevant to controlled release

1. **Absorption.** The absorption rate should be faster than the release rate, so that release (not absorption) controls the level. Drugs absorbed only in a short segment of the gut are not good for once-daily oral systems unless the system is held in the stomach (see gastroretentive systems, Unit 3).
2. **Distribution.** A large apparent volume of distribution and slow redistribution affect how much drug must be released.
3. **Metabolism.** Drugs that induce or inhibit their own metabolism, or that undergo saturable first-pass metabolism, behave unpredictably when given slowly.
4. **Elimination half-life.** Decides the release rate needed. Very short half-life drugs need large amounts of drug; long half-life drugs gain little.
5. **Duration of action.** Drugs with long pharmacological action (even with short half-life) may not need CR.
6. **Margin of safety (therapeutic index).** Narrow-index drugs need very reliable release to avoid toxicity.
7. **Side effects.** CR is useful when side effects are linked to peak levels.
8. **Disease state and circadian rhythm.** Some conditions (asthma attacks at night, morning rise in blood pressure) are better treated by timed (chronotherapeutic) release than by a flat level.

## 1.6 Approaches to design controlled-release formulations

```text
Approaches to oral controlled release
├── Diffusion-controlled
│     ├── Reservoir (membrane) systems
│     └── Matrix (monolithic) systems
├── Dissolution-controlled
│     ├── Encapsulation (coated particles)
│     └── Matrix (slowly dissolving)
├── Combined diffusion and dissolution
├── Ion-exchange resin systems
└── Others: osmotic pumps (Unit 2), hydrogels, pH-independent and
            gastroretentive systems (Unit 3)
```

### a. Diffusion-controlled systems

Drug moves from a region of high concentration to low concentration through a polymer. The basic law is **Fick's first law**:

J = −D (dC/dx)

where J is the flux (amount per unit area per unit time), D the diffusion coefficient and dC/dx the concentration gradient.

**1. Reservoir (membrane-controlled) systems.** A core of drug is surrounded by a water-insoluble polymer membrane, for example ethyl cellulose or ethylene–vinyl acetate (EVA).

```text
   ┌──────────────────────┐
   │  rate-controlling    │   membrane (ethyl cellulose, EVA)
   │   ┌──────────────┐   │
   │   │  drug core   │   │   saturated drug solution / solid drug
   │   │ (reservoir)  │   │
   │   └──────────────┘   │
   └──────────────────────┘
        drug diffuses out → constant rate while core stays saturated
```

Release rate: dM/dt = A D K ΔC / L

where A is the area, D the diffusion coefficient in the membrane, K the partition coefficient between membrane and core, ΔC the concentration difference across the membrane and L the membrane thickness. As long as a saturated solution remains inside, ΔC is constant and release is **zero order**. Thicker membrane or lower permeability → slower release.

- Advantages: true zero-order release possible; rate set by the membrane.
- Disadvantages: if the membrane ruptures, the whole dose may be released (dose dumping); harder to make; large molecules diffuse poorly.

**2. Matrix (monolithic) systems.** Drug is dispersed evenly in a polymer matrix (HPMC, ethyl cellulose, waxes). Water enters, dissolves the drug near the surface, and the dissolved drug diffuses out through pores or through the swollen polymer. Drug near the surface leaves first; later drug must travel a longer path, so the rate falls with time. The amount released follows the **Higuchi equation** (square root of time, see 1.7).

- Advantages: easy to make by compression; no risk of dose dumping from a burst membrane.
- Disadvantages: release is not zero order; release rate falls with time.

Matrices may be **hydrophobic / insoluble** (ethyl cellulose, waxes, Eudragit RL/RS: drug leaves through pores) or **hydrophilic / swellable** (HPMC, sodium alginate, xanthan gum: polymer forms a gel layer that slows diffusion and gradually erodes).

### b. Dissolution-controlled systems

Release depends on how fast the drug or its coat dissolves. The **Noyes–Whitney equation** describes dissolution:

dC/dt = D A (Cs − C) / h

where D is the diffusion coefficient, A the surface area, Cs the saturation solubility, C the concentration in bulk solution and h the thickness of the diffusion layer.

1. **Encapsulation (coating) dissolution systems.** Drug particles or pellets are coated with slowly dissolving polymers or waxes of different thickness. Thin coats dissolve early and thick coats later, so the mixture gives a spread of release (the principle of many SR capsules, such as the "spansule" type).
2. **Matrix dissolution systems.** Drug is mixed in a slowly dissolving or eroding material (waxes, fatty acids, hydrogenated oils). Release depends on the rate at which the matrix surface dissolves.

### c. Combined diffusion and dissolution systems

A partly soluble membrane: when the soluble part dissolves, pores form, and drug diffuses through these pores. Example: a coat of ethyl cellulose mixed with a water-soluble polymer (HPMC or PEG) as a pore former.

### d. Ion-exchange resin systems

Ion-exchange resins are water-insoluble cross-linked polymers carrying ionisable groups. Drug ions are bound to the resin and released when they are exchanged for ions of the same charge in the gut fluids.

- **Cation exchange resins** (sulfonic acid groups) bind **basic drugs**: Resin–SO3⁻ Drug-H⁺ + Na⁺ → Resin–SO3⁻ Na⁺ + Drug-H⁺
- **Anion exchange resins** (quaternary ammonium groups) bind **acidic drugs**: Resin–N⁺R3 Drug⁻ + Cl⁻ → Resin–N⁺R3 Cl⁻ + Drug⁻

Release depends on the ion concentration in the fluid, the resin's particle size and cross-linking, not on enzymes or pH alone. To slow release further, the drug–resin complex is coated with a polymer such as ethyl cellulose (the "Pennkinetic" approach, used for liquid SR suspensions such as dextromethorphan polistirex). Resins also mask bitter taste.

## 1.7 Release kinetics: the equations you must know

The way the amount released (Q) changes with time (t) tells us the mechanism. Release data are plotted in different ways, and the plot that gives the straightest line (highest r²) is taken as the best fit.

| Model | Equation | Plot that gives a straight line | Typical system |
| --- | --- | --- | --- |
| Zero order | Q = Q0 + k0 t | Amount released vs t | Reservoir, osmotic pump, transdermal patch |
| First order | ln (100 − Q) = ln 100 − k1 t (or log C = log C0 − k t/2.303) | log % remaining vs t | Many SR matrices of soluble drugs |
| Higuchi | Q = kH √t | Amount released vs √t | Matrix (insoluble or porous) systems |
| Korsmeyer–Peppas | Mt/M∞ = k tⁿ | log (Mt/M∞) vs log t | Used to find the mechanism (value of n) |
| Hixson–Crowell | W0^(1/3) − Wt^(1/3) = k t | Cube root of weight remaining vs t | Systems where surface area shrinks as particles dissolve |

**Zero order.** Rate = k0 (a constant). Units of k0: amount per time (mg/h). Half-life t1/2 = Q0/2k0, so it depends on the starting amount.

**First order.** Rate is proportional to the amount left: dQ/dt = −k1 Q. Half-life t1/2 = 0.693/k1, independent of the starting amount. Units of k1: per hour.

**Higuchi model.** For a drug dispersed in a homogeneous matrix:

Q = [D (2A − Cs) Cs t]^½

and for a porous (granular) matrix:

Q = [(D ε / τ) (2A − ε Cs) Cs t]^½

where Q is the amount released per unit area, D the diffusion coefficient, A the total drug loading per unit volume, Cs the drug solubility in the matrix or medium, ε the porosity and τ the tortuosity. Both reduce to Q = kH √t.

**Korsmeyer–Peppas exponent n** (for the first 60% of release, thin film / slab):

| n (slab) | Mechanism |
| --- | --- |
| 0.5 | Fickian diffusion |
| between 0.5 and 1 | Anomalous (non-Fickian): diffusion plus swelling or erosion |
| 1.0 | Case II transport: polymer relaxation / erosion, giving zero-order release |

For cylinders the Fickian limit is about 0.45, and for spheres about 0.43.

### Worked example 1: zero-order, first-order and Higuchi calculations

1. A reservoir system releases drug at k0 = 5 mg/h. Amount released in 12 h = 5 × 12 = **60 mg** (independent of how much is left, as long as the core is saturated).
2. A matrix tablet releases drug by first-order kinetics with k1 = 0.1 h⁻¹.
   - t1/2 = 0.693/0.1 = **6.93 h**
   - Fraction left after 12 h = e^(−0.1 × 12) = e^(−1.2) = 0.301, so about **70% released**.
3. A matrix releases 25% of its drug in the first hour by Higuchi kinetics (Q = 25√t).
   - At 4 h: 25 × √4 = **50%**; at 9 h: 25 × 3 = **75%**; 100% would need (100/25)² = **16 h**.
   - Notice that doubling the time does not double the release; four times the time doubles it.

### Worked example 2: finding the release model from data

A matrix tablet gave this cumulative release:

| Time (h) | 1 | 2 | 4 | 6 | 8 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| % released | 12 | 17 | 24 | 29.5 | 34 | 41.5 |

Linear regression of each plot gives:

| Plot | Slope | r² |
| --- | --- | --- |
| Zero order (% released vs t) | 2.63 %/h | 0.971 |
| First order (ln % remaining vs t) | −0.0366 h⁻¹ | 0.988 |
| Higuchi (% released vs √t) | 11.99 % per h^½ | 0.99997 |
| Korsmeyer–Peppas (log % vs log t) | n = 0.50 | 0.99998 |

The Higuchi plot is the straightest, and the Peppas exponent n = 0.50 shows **Fickian diffusion** from a matrix. Using Q = 12√t, the time for 60% release would be (60/12)² = **25 h**.

### Worked example 3: design of an oral zero-order product (hypothetical drug)

For a hypothetical drug with elimination rate constant ke = 0.2 h⁻¹, volume of distribution 50 L and a desired steady level of 2 mg/L:

- Required zero-order release rate k0 = ke × Css × Vd = 0.2 × 2 × 50 = **20 mg/h**
- Maintenance amount for 12 h = 20 × 12 = **240 mg**
- Immediate-release (loading) portion Di = Css × Vd = 2 × 50 = **100 mg**
- If the maintenance part already starts releasing at time zero and the peak of the loading portion is at Tp = 1 h, the corrected loading portion Di* = Di − k0 × Tp = 100 − 20 = **80 mg**

These figures are only a teaching example showing how release rate is linked to pharmacokinetics; they are not doses of any real medicine.

## 1.8 Polymers in controlled release

A **polymer** is a large molecule made of many repeating units (monomers) joined by covalent bonds. Polymers form the membranes, matrices, coatings and carriers of almost all novel delivery systems.

### a. Classification

**By origin**

| Class | Examples |
| --- | --- |
| Natural | Gelatin, albumin, collagen, sodium alginate, chitosan, starch, guar gum, xanthan gum, gum acacia, pectin, hyaluronic acid |
| Semisynthetic | Hydroxypropyl methylcellulose (HPMC), methylcellulose, ethyl cellulose, sodium carboxymethylcellulose, cellulose acetate, cellulose acetate phthalate |
| Synthetic | Polymethacrylates (Eudragit), polyvinyl alcohol, polyvinylpyrrolidone, polyethylene glycol, polylactic acid (PLA), poly(lactic-co-glycolic acid) (PLGA), polycaprolactone, polyanhydrides, ethylene–vinyl acetate, silicone (polydimethylsiloxane), polyacrylic acid (carbomer) |

**By biodegradability**

- **Biodegradable**: broken down in the body to harmless products, so they need not be removed: PLA, PLGA, polycaprolactone, polyanhydrides, polyorthoesters, chitosan, albumin, gelatin.
- **Non-biodegradable**: stay intact and must be removed or excreted unchanged: ethyl cellulose, EVA, silicone rubber, polyurethanes, polymethyl methacrylate.

**By interaction with water**

- Hydrophilic / water-soluble (PEG, PVP, HPMC).
- Hydrogels: swell in water without dissolving (cross-linked HPMC, polyhydroxyethyl methacrylate, carbomer).
- Hydrophobic / water-insoluble (ethyl cellulose, EVA, silicone).

**By structure**: homopolymer (one monomer) and copolymer (two or more monomers: random, block, graft, alternating); linear, branched or cross-linked.

**Smart (stimuli-responsive) polymers** change their properties with pH, temperature, ions or enzymes:

| Stimulus | Example polymer | Use |
| --- | --- | --- |
| pH | Eudragit L100 (dissolves above about pH 6), Eudragit S100 (above about pH 7), cellulose acetate phthalate | Enteric and colon delivery |
| Temperature | Poloxamer 407, poly(N-isopropylacrylamide) | In situ gels |
| Ions | Gellan gum, sodium alginate (gel with Ca²⁺) | Ophthalmic in situ gels, rafts |

### b. Properties that matter

1. **Molecular weight and its distribution**: higher molecular weight → more viscous gels, slower diffusion and slower erosion.
2. **Glass transition temperature (Tg)**: below Tg the polymer is glassy and rigid; above it, rubbery and more permeable. Plasticisers lower Tg.
3. **Crystallinity**: crystalline regions are impermeable; drug diffuses through amorphous regions.
4. **Solubility and swelling** in water and at different pH values.
5. **Permeability** to the drug and to water.
6. **Degradation**: **bulk erosion** (water enters the whole mass, which degrades throughout, as with PLGA) or **surface erosion** (only the surface wears away, as with polyanhydrides, giving release nearer zero order).
7. **Biocompatibility and safety**: non-toxic, non-irritant, non-carcinogenic; degradation products safe.
8. **Mechanical strength, film-forming ability and processability.**
9. **Compatibility** with the drug and other excipients; stability; cost and availability.

### c. Ideal properties of a polymer for drug delivery

- Inert and compatible with the drug.
- Non-toxic, biocompatible and free of leachable impurities.
- Easy to make, sterilise and process into the needed shape.
- Allows the desired release rate with a wide range of drugs.
- Stable during storage; good mechanical strength.
- If biodegradable, degrades at a predictable rate to safe products.
- Inexpensive and available in consistent quality.

### d. Advantages of polymers in controlled release

- Release rate can be controlled by choosing polymer type, grade, amount and thickness.
- Protect drug from the environment (moisture, acid, enzymes).
- Mask taste and reduce irritation.
- Allow targeting (enteric, colon, mucoadhesive, tumour-seeking carriers).
- Biodegradable polymers avoid surgical removal of implants.

### e. Applications

| Polymer | Application |
| --- | --- |
| HPMC | Hydrophilic matrix tablets, film coating, ophthalmic solutions |
| Ethyl cellulose | Insoluble membrane coatings, matrix tablets, microcapsule walls |
| Eudragit L, S | Enteric and colon-targeted coatings |
| Eudragit RL, RS | Insoluble but permeable SR coatings (RL high, RS low permeability) |
| Eudragit E | Coating that dissolves in stomach acid; taste masking |
| Carbomer, polycarbophil | Mucoadhesive buccal and vaginal systems |
| PLGA, PLA | Biodegradable microspheres and implants for injections lasting weeks to months |
| EVA | Rate-controlling membranes (ocular inserts, contraceptive vaginal rings, implants) |
| Silicone | Implants, transdermal adhesives, intrauterine devices |
| Cellulose acetate | Semipermeable membrane of osmotic pumps |
| Sodium alginate, chitosan | Microspheres, raft-forming and floating systems, nanoparticles |
| Polyanhydrides | Surface-eroding implant wafers |

## Remember

- CR = predetermined, ideally zero-order release that keeps the level within the therapeutic window; SR = slow release, not necessarily constant.
- Good candidates: half-life about 2–8 h, small dose, wide therapeutic index, good absorption throughout the gut, stable in gut fluids.
- Reservoir: dM/dt = ADKΔC/L, zero order while the core is saturated, risk of dose dumping. Matrix: Higuchi Q = kH√t.
- Noyes–Whitney: dC/dt = DA(Cs − C)/h for dissolution-controlled systems.
- First-order t1/2 = 0.693/k; zero-order t1/2 = Q0/2k0.
- Peppas n (slab): 0.5 Fickian, 0.5–1 anomalous, 1 case II (zero order).
- Cation exchangers carry basic drugs; anion exchangers carry acidic drugs; coated drug–resin complexes give SR suspensions.
- Polymers: natural, semisynthetic, synthetic; biodegradable (PLGA, PLA, polyanhydrides) vs non-biodegradable (EVA, silicone, ethyl cellulose); bulk vs surface erosion.
