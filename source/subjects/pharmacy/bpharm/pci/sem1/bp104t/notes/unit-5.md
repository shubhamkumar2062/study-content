# Unit 5: Radiopharmaceuticals

Radiopharmaceuticals are medicines that contain a radioactive atom. They are used to see how organs work (diagnosis) and to destroy diseased tissue (therapy). This short unit carries good marks: a long question on radioactivity and its measurement, or on the properties of α, β and γ radiation, and short notes on half-life, sodium iodide I-131, and storage and precautions appear in almost every paper.

## 5.1 Basic terms

An atom has a small **nucleus** of protons and neutrons, surrounded by electrons.

| Term | Meaning | Example |
| --- | --- | --- |
| Atomic number (Z) | Number of protons | Iodine: Z = 53 |
| Mass number (A) | Protons + neutrons | I-131: A = 131 |
| Isotopes | Same Z, different A (same element) | I-127 (stable), I-131, I-125 (radioactive) |
| Isobars | Same A, different Z | C-14 and N-14 |
| Isotones | Same number of neutrons | – |
| Radioisotope (radionuclide) | An isotope with an unstable nucleus that decays and gives out radiation | Tc-99m, I-131, Co-60 |

A nucleus is stable only when its **neutron-to-proton ratio** is in a certain range (close to 1 for light elements, rising to about 1.5 for heavy ones). Nuclei outside this range are unstable and change by radioactive decay.

## 5.2 Radioactivity

**Radioactivity** is the spontaneous breakdown of an unstable nucleus with the emission of particles (α, β) or electromagnetic radiation (γ), until a stable nucleus is formed.

- **Discovery**: Henri Becquerel (1896) found that uranium salts darken photographic plates. Marie and Pierre Curie then isolated polonium and radium (1898).
- **Natural radioactivity**: shown by naturally occurring elements such as uranium, thorium and radium.
- **Artificial (induced) radioactivity**: produced by bombarding stable nuclei with neutrons, protons or other particles in a nuclear reactor or a cyclotron. Almost all medical radioisotopes are made this way, or obtained from a **generator** (for example, Tc-99m from a molybdenum-99 generator).

Radioactive decay is not affected by temperature, pressure or chemical combination; it depends only on the nucleus.

**Modes of decay**

```text
α decay:   heavy nucleus  →  daughter (Z − 2, A − 4) + ⁴He nucleus
β⁻ decay:  neutron        →  proton + electron (β⁻) + antineutrino   (Z + 1, A same)
β⁺ decay:  proton         →  neutron + positron (β⁺) + neutrino      (Z − 1, A same)
Electron capture: proton + inner electron → neutron + neutrino        (Z − 1)
γ emission: excited nucleus → same nucleus in lower energy state + γ ray
            (isomeric transition, e.g. Tc-99m → Tc-99)
```

A positron quickly meets an electron and the two **annihilate**, giving two gamma photons of 511 keV in opposite directions. This is the basis of **PET** (positron emission tomography).

## 5.3 Properties of α, β and γ radiations

| Property | α (alpha) | β (beta) | γ (gamma) |
| --- | --- | --- | --- |
| Nature | Helium nuclei (2 protons + 2 neutrons) | Electrons (β⁻) or positrons (β⁺) from the nucleus | Electromagnetic radiation (photons) |
| Charge | +2 | −1 (β⁻) or +1 (β⁺) | None |
| Mass | About 4 atomic mass units (heavy) | Very small (1/1836 of a proton) | None |
| Velocity | About one-tenth of the speed of light or less | Up to close to the speed of light | Speed of light |
| Energy spectrum | Discrete (monoenergetic) | Continuous, from zero to a maximum | Discrete |
| Ionising power | Very high | Moderate | Low |
| Penetrating power | Very low: stopped by a sheet of paper, the outer skin or a few cm of air | Moderate: stopped by a few mm of aluminium or perspex | Very high: reduced only by thick lead or concrete |
| Deflection in electric/magnetic field | Small, towards negative plate | Larger, towards positive plate (β⁻) | Not deflected |
| Effect on photographic plate | Affects | Affects | Affects |
| Main hazard | Internal (if swallowed or inhaled) | External and internal | External (whole body) |
| Medical use | Some targeted therapy | Therapy (I-131, P-32) | Imaging (Tc-99m), external therapy (Co-60), sterilisation |

```text
PENETRATION
   α ──►│paper
   β ──────────►│ aluminium (few mm)
   γ ─────────────────────────►│ thick lead / concrete (reduced, not fully stopped)

Ionising power: α > β > γ          Penetrating power: γ > β > α
```

## 5.4 Half-life and the decay law

Each radioactive nucleus has a fixed chance of decaying per unit time, called the **decay constant (λ)**. The number of nuclei falls exponentially:

**N = N0 e^(−λt)**, or in log form, **2.303 log (N0/N) = λt**

- N0 = number of nuclei (or activity) at the start; N = number left after time t.
- **Activity (A)** = rate of decay = λN; activity falls in the same exponential way.

**Half-life (t½)** is the time in which half of the radioactive nuclei (and so half of the activity) decay.

**t½ = 0.693 / λ**

**Average (mean) life** τ = 1/λ = 1.44 t½.

After n half-lives, the fraction remaining = (1/2)ⁿ.

```text
Activity
100% ┤●
 50% ┤   ●
 25% ┤       ●
12.5%┤           ●
6.25%┤               ●
     └───┬───┬───┬───┬──── time
        1   2   3   4   (half-lives)
```

**Physical, biological and effective half-life.** In the body, a radiopharmaceutical is lost both by physical decay (physical half-life, Tp) and by excretion (biological half-life, Tb). The **effective half-life (Te)** is:

**1/Te = 1/Tp + 1/Tb**, or Te = (Tp × Tb) / (Tp + Tb)

Te is always shorter than either one.

**Worked example 1.** A vial of sodium iodide I-131 has an activity of 80 MBq. What will it be after 24 days? (t½ = 8 days)
24 days = 3 half-lives → 80 × (1/2)³ = **10 MBq**.

**Worked example 2.** Find λ for I-131.
λ = 0.693 / 8 days = **0.0866 per day**.

**Worked example 3.** Find the time for a radioisotope with t½ = 6 hours to fall to 10% of its activity.
2.303 log (100/10) = λt → 2.303 = (0.693/6) t → t = **19.9 hours** (about 3.3 half-lives).

**Why half-life matters in pharmacy.** A diagnostic agent should have a half-life long enough to prepare, transport and complete the scan, but short enough to give the patient a low radiation dose (hours to a few days). The half-life also decides the expiry time, the storage period of waste, and how quickly a product must be used after calibration.

## 5.5 Units of radioactivity and radiation dose

| Quantity | Older unit | SI unit | Relation |
| --- | --- | --- | --- |
| Activity | Curie (Ci) = 3.7 × 10¹⁰ disintegrations per second | Becquerel (Bq) = 1 disintegration per second | 1 mCi = 37 MBq |
| Exposure (X and γ in air) | Roentgen (R) | Coulomb per kg | – |
| Absorbed dose | Rad (100 erg per g) | Gray (Gy) = 1 J per kg | 1 Gy = 100 rad |
| Equivalent dose (biological effect) | Rem | Sievert (Sv) | 1 Sv = 100 rem |

The equivalent dose takes into account that α particles do much more biological damage per unit of energy than β or γ radiation.

## 5.6 Measurement of radioactivity

Radiation cannot be seen, felt or smelled, so instruments are used. All of them work because radiation either **ionises** a material or **excites** it to give light.

```text
DETECTORS OF RADIATION
├── Gas-filled (ionisation) detectors
│      ├── Ionisation chamber (dose calibrator)
│      ├── Proportional counter
│      └── Geiger–Müller (GM) counter
├── Scintillation detectors
│      ├── Solid: sodium iodide crystal with thallium, NaI(Tl) (γ rays)
│      └── Liquid scintillation counter (weak β emitters such as H-3, C-14)
├── Semiconductor (solid-state) detectors
└── Personal dosimeters: film badge, thermoluminescent dosimeter (TLD), pocket dosimeter
```

### a. Gas-filled detectors

A gas-filled chamber has two electrodes with a voltage between them. Radiation entering the chamber ionises the gas; the ions move to the electrodes and give an electric signal.

```text
   radiation
      │
  ┌───▼──────────────┐
  │  +  gas  −       │  central wire (anode, +)
  │      ●───────────┼─── to counter / meter
  │  ion pairs       │  outer wall (cathode, −)
  └──────────────────┘
       high voltage supply
```

| Detector | Voltage | Behaviour | Use |
| --- | --- | --- | --- |
| Ionisation chamber | Low | Collects only the ions made by the radiation; current proportional to energy deposited | **Dose calibrator** to measure the activity of each patient dose; survey meters |
| Proportional counter | Medium | Ions accelerate and create more ions (gas amplification); pulse size proportional to energy | Distinguishes α from β; research |
| Geiger–Müller counter | High | Every ionising event triggers a full avalanche along the wire; all pulses are the same size | Sensitive detection and contamination surveys; does not tell energy |

**Geiger–Müller counter in detail.** A sealed tube with a thin mica window contains an inert gas (argon or neon) at low pressure and a small amount of a **quenching gas** (a halogen or an organic vapour). The central wire is held at several hundred volts positive. A single ionising particle produces an avalanche of ions and a large pulse, which is counted (clicks or a digital count). The quenching gas stops the discharge so the tube is ready for the next event. After each pulse the tube is insensitive for a short **dead time**, so very high count rates are underestimated.

### b. Scintillation counters

Certain substances (**scintillators**) give a tiny flash of light when radiation is absorbed in them. A **photomultiplier tube** turns each flash into an electrical pulse whose size is proportional to the energy absorbed. So scintillation counters both count and **measure energy** (spectrometry).

- **Solid scintillation**: a sodium iodide crystal activated with thallium, NaI(Tl), is very efficient for γ rays. It is the detector in gamma cameras and thyroid uptake probes.
- **Liquid scintillation**: the radioactive sample is dissolved in a liquid "cocktail" containing a scintillator; used for weak β emitters such as tritium (H-3) and carbon-14 in research and drug metabolism studies.

### c. Semiconductor detectors

Germanium or silicon crystals in which radiation produces electron–hole pairs; they give very good energy resolution.

### d. Personal monitoring

Workers wear **film badges** (blackening of a photographic film behind filters) or **thermoluminescent dosimeters** (crystals such as lithium fluoride store energy and release it as light on heating; the light is proportional to the dose). Pocket dosimeters give a direct reading.

## 5.7 Radioisotopes used in pharmacy and medicine

| Radioisotope | Half-life (standard value) | Main emission | Main use |
| --- | --- | --- | --- |
| Technetium-99m | About 6 hours | γ (140 keV) | Most used imaging agent: bone, thyroid, heart, brain, kidney scans; obtained from a Mo-99 generator |
| Iodine-131 | About 8 days | β and γ | Thyroid diagnosis and therapy (hyperthyroidism, thyroid cancer) |
| Iodine-125 | About 60 days | γ / X rays (low energy) | Radioimmunoassay; brachytherapy seeds |
| Phosphorus-32 | About 14.3 days | β | Polycythaemia vera, some skin and bone conditions (older use) |
| Cobalt-60 | About 5.3 years | γ | External beam therapy of cancer; sterilisation of medical products |
| Fluorine-18 | About 110 minutes | β⁺ (positron) | PET imaging (fluorodeoxyglucose for cancer) |
| Carbon-14 | About 5,730 years | Weak β | Research tracer; urea breath test; dating |
| Tritium (H-3) | About 12.3 years | Weak β | Research labelling |

In India, radioisotopes and radiopharmaceuticals are supplied by the **Board of Radiation and Isotope Technology (BRIT)**, Department of Atomic Energy, and their safe use is regulated by the **Atomic Energy Regulatory Board (AERB)**.

## 5.8 Sodium iodide I-131

**Production.** By neutron irradiation of tellurium (Te-130) in a nuclear reactor. The tellurium-131 formed decays by β emission to iodine-131, which is separated by distillation and converted to sodium iodide:

```text
Te-130 + neutron → Te-131 → (β⁻ decay) → I-131
```

It is also obtained from the fission products of uranium-235.

**Forms.** Oral solution and capsules (for diagnosis and therapy); injection in some cases. The product contains sodium iodide with a small amount of reducing agent (such as sodium thiosulphate) to keep the iodine as iodide and stop it from becoming volatile iodine; it is buffered to an alkaline pH.

**Properties.** Clear, colourless solution (or a capsule); the glass container may slowly darken because of radiation. Half-life about **8 days**; emits **β particles** (which destroy tissue, useful in therapy) and **γ rays** (364 keV, which pass out of the body, useful for detection and imaging). The activity is stated on the label for a given date and time (calibration).

**Mechanism.** The thyroid traps iodide actively and uses it to make thyroid hormones; radioactive iodide is concentrated in the same way, so the radiation is delivered mainly to thyroid tissue.

**Uses**

1. **Diagnosis**: thyroid uptake test (the fraction of a small oral dose taken up by the thyroid after a fixed time, measured with a probe over the neck); thyroid scanning to locate nodules and metastases.
2. **Therapy**: hyperthyroidism (Graves' disease, toxic nodules) with moderate doses; ablation of thyroid tissue and treatment of metastases in differentiated thyroid cancer with larger doses.

**Precautions specific to I-131.** Contraindicated in pregnancy and during breastfeeding (it crosses the placenta and enters milk and can destroy the baby's thyroid). Patients treated with large doses are kept away from others, especially children and pregnant women, for a period advised by the nuclear medicine team, and their urine, saliva and sweat are radioactive for some days. Potassium iodide given before exposure blocks thyroid uptake of radioiodine in a nuclear emergency.

## 5.9 Storage conditions of radioactive substances

1. Store in a **designated, restricted area** marked with the radiation warning symbol (trefoil), accessible only to authorised staff.
2. Keep in **shielded containers**: lead pots or lead-lined boxes for γ emitters; perspex or plastic for pure β emitters (heavy metals with high-energy β emitters produce secondary X rays called bremsstrahlung).
3. Every container is **labelled** with the name of the radioisotope and compound, activity at the calibration date and time, volume, batch number and expiry.
4. Store at the temperature stated on the label; volatile substances (such as radioiodine) in sealed containers with ventilation or fume hood.
5. Keep a **record (stock register)** of receipt, use and disposal of every radioactive material.
6. Store away from photographic film and from inflammable materials.
7. **Radioactive waste**: short half-life waste is kept in shielded storage until it decays to safe levels (**decay-in-storage**, usually about 10 half-lives), then disposed of as ordinary waste; other waste is disposed of only as permitted by the regulator.

## 5.10 Precautions in handling radioactive substances

The three basic rules of external protection are **time, distance and shielding**, applied with the principle of keeping dose **as low as reasonably achievable (ALARA)**:

- **Time**: work quickly and plan the job beforehand; dose is proportional to time.
- **Distance**: dose falls with the square of distance (**inverse square law**); use long tongs and forceps.
- **Shielding**: lead bricks, syringe shields, lead aprons, lead-glass screens.

General laboratory precautions:

1. Wear a laboratory coat, disposable gloves and a personal dosimeter (film badge or TLD).
2. Never eat, drink, smoke or apply cosmetics in the radioactive area; **never pipette by mouth**.
3. Work over trays lined with absorbent paper so that spills are contained; handle volatile materials in a fume hood.
4. Monitor hands, clothing and work surfaces with a survey meter after work.
5. Deal with spills at once: contain, decontaminate, monitor, record.
6. Workers have regular medical check-ups and dose records; pregnant workers take extra care.
7. Patients are given the lowest activity that gives the required result, and the dose is checked in the **dose calibrator** before administration.

## 5.11 Pharmaceutical applications of radioactive substances

| Area | Application | Examples |
| --- | --- | --- |
| Diagnosis (in vivo) | Imaging the structure and function of organs | Tc-99m bone, renal, cardiac, brain scans; F-18 FDG PET; I-131 thyroid scan |
| Diagnosis (function tests) | Measuring how an organ handles a substance | Thyroid uptake test, red cell volume and survival studies, Schilling-type absorption tests |
| Diagnosis (in vitro) | Radioimmunoassay of hormones and drugs in blood | I-125 labelled antigens |
| Therapy | Destroying diseased tissue | I-131 for thyroid disease, P-32 for polycythaemia, Co-60 teletherapy, I-125 seeds (brachytherapy) |
| Sterilisation | Gamma radiation kills micro-organisms without heat | Co-60 sterilisation of disposable syringes, sutures, surgical gloves, dressings and some heat-sensitive products |
| Research | Following a drug's absorption, distribution, metabolism and excretion with labelled molecules | C-14 and H-3 labelled drugs; tracer studies |
| Quality control and industry | Measuring fill levels, thickness, leak detection | Industrial gauges |

## Remember

- Radioactivity = spontaneous decay of unstable nuclei; discovered by Becquerel (1896).
- α: He nucleus, +2, most ionising, least penetrating (paper). β: electron/positron, moderate (aluminium). γ: photons, least ionising, most penetrating (lead).
- N = N0 e^(−λt); t½ = 0.693/λ; mean life = 1.44 t½; 1/Te = 1/Tp + 1/Tb.
- 1 Ci = 3.7 × 10¹⁰ Bq; 1 mCi = 37 MBq; 1 Gy = 100 rad; 1 Sv = 100 rem.
- Detectors: ionisation chamber (dose calibrator), proportional counter, GM counter (no energy information, dead time), scintillation counter (NaI(Tl) for γ; liquid for H-3, C-14), film badge and TLD for personal dose.
- Standard half-lives: Tc-99m about 6 h, I-131 about 8 days, I-125 about 60 days, P-32 about 14.3 days, Co-60 about 5.3 years, F-18 about 110 min.
- I-131: made from tellurium-130; β for therapy, γ for imaging; thyroid uptake, hyperthyroidism, thyroid cancer; not in pregnancy or breastfeeding.
- Storage: shielded, labelled, restricted, recorded; waste by decay-in-storage.
- Safety: time, distance, shielding; ALARA; no mouth pipetting; wear dosimeters.
