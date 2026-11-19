# Demonstration experiment on HPLC

**Aim:** To study the parts and operation of a high performance liquid chromatograph, record the chromatogram of a drug mixture (for example paracetamol and caffeine) by reversed-phase HPLC, and calculate system suitability parameters and the content of a sample.

> This is a demonstration; the conditions below are typical examples. Use the method your teacher sets up and the instrument instructions. Wear goggles and gloves; methanol and acetonitrile are toxic and flammable.

## Principle

In reversed-phase HPLC the stationary phase is non-polar (octadecylsilane, C18, bonded to silica) and the mobile phase is polar (water or buffer with methanol or acetonitrile), pumped at high pressure. Polar compounds spend less time in the stationary phase and elute first; less polar ones are retained longer. A UV detector records the eluate, giving peaks whose **retention time** identifies a compound and whose **area** is proportional to its amount.

```text
 [Mobile phase] -> [Degasser] -> [Pump] -> [Injector, 20 µl loop] -> [Guard + C18 column] -> [UV detector] -> [Data system]
```

## Requirements (typical)

HPLC system with pump, Rheodyne (or auto) injector with 20 µl loop, C18 column (250 × 4.6 mm, 5 µm), UV detector, data system; 0.45 µm membrane filters, syringe filters, sonicator, volumetric flasks; HPLC-grade methanol and water; paracetamol and caffeine reference standards, sample (tablet solution).

Example conditions: mobile phase methanol : water (about 25 : 75 v/v), flow 1.0 ml/min, detection at about 254 nm (or as set), column at room temperature or 30 °C, injection 20 µl.

## Procedure

1. **Mobile phase:** mix the solvents, filter through a 0.45 µm membrane and degas (sonication or helium sparging).
2. **System start-up:** prime the pump, start the flow at 1.0 ml/min and equilibrate the column until the pressure and baseline are steady (note the back-pressure).
3. **Standard solution:** prepare a mixed standard (for example 20 µg/ml of each drug) in mobile phase; filter through a 0.45 µm syringe filter.
4. **Sample solution:** prepare from tablet powder to the same nominal concentration; filter.
5. **System suitability:** inject the standard six times (load the loop in the "load" position, turn to "inject").
6. Inject the sample (in duplicate).
7. Note retention times, peak areas, peak widths and tailing from the data system.
8. Calculate k, α, N, Rs, tailing factor and %RSD; calculate the sample content by the external standard method.
9. **Shut-down:** wash the column with a higher proportion of organic solvent (for example methanol : water 80 : 20) if buffers were used, then stop the flow.

## Observations and calculations

> Example readings, for practice only — record your own.

Dead time t0 = 1.5 min (solvent front).

| Peak | tR (min) | Base width W (min) |
| --- | --- | --- |
| Paracetamol (A) | 4.2 | 0.30 |
| Caffeine (B) | 5.6 | 0.34 |

- Capacity factors: kA = (4.2 − 1.5)/1.5 = **1.80**; kB = (5.6 − 1.5)/1.5 = **2.73**.
- Selectivity: α = 2.73/1.80 = **1.52**.
- Resolution: Rs = 2(5.6 − 4.2)/(0.30 + 0.34) = 2.8/0.64 = **4.37** (baseline separation; must be at least 1.5, or as stated in the monograph).
- Theoretical plates (caffeine): N = 16(5.6/0.34)² = **4340**.
- Tailing factor (example: width at 5% height 0.14 min, front half-width 0.06 min): T = 0.14/(2 × 0.06) = **1.17** (limit usually not more than 2.0).

**Replicate standard injections (paracetamol peak areas):** 152340, 151890, 152760, 152110, 151950, 152480.
Mean = 152,255; SD = 335; **%RSD = 0.22%** (usual limit not more than 2.0%).

**Assay (external standard):** standard 20 µg/ml gives mean area 152,255; sample area 148,900.
c_sample = 20 × 148,900/152,255 = **19.56 µg/ml**, that is 19.56/20 × 100 = **97.8%** of the nominal concentration. Convert to mg per tablet using the dilution scheme.

## Result

1. Retention times: paracetamol ___ min, caffeine ___ min.
2. System suitability: N = ___, Rs = ___, T = ___, %RSD = ___ (within / outside limits).
3. The sample contains ___% of the labelled amount.

## Precautions

1. Use only HPLC-grade, filtered and degassed solvents.
2. Never let the pump run dry; prime it to remove air.
3. Filter all samples to protect the column; use a guard column.
4. Do not exceed the column's pressure and pH limits (silica C18 is usually used between pH 2 and 8).
5. Flush buffers out of the system after use.
6. Use the same injection volume and conditions for standards and samples.

## Viva questions

1. **Why is it called reversed phase?** The stationary phase is non-polar and the mobile phase polar, the reverse of classical normal-phase chromatography.
2. **Which drug elutes first and why?** The more polar one (paracetamol), because it is held less by C18.
3. **Why is the mobile phase degassed?** Bubbles cause pump and detector problems (pressure fluctuation, noisy baseline).
4. **What is system suitability?** Checks (RSD, plates, tailing, resolution) that show the system works properly before samples are analysed.
5. **What does the guard column do?** Protects the analytical column from particles and strongly retained material.
6. **Name HPLC detectors.** UV-visible, PDA, fluorescence, refractive index, electrochemical, mass spectrometer.
