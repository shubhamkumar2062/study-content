# Overall heat transfer coefficient of a heat exchanger

**Aim:** To determine the overall heat transfer coefficient (U) of a given heat exchanger (double-pipe or shell-and-tube), in parallel and counter-current flow.

> Follow your lab manual and your teacher where they differ. Hot water lines and steam are hot; do not touch uninsulated pipes.

## Principle

In a heat exchanger, heat passes from the hot fluid to the cold fluid through a metal wall. The rate of heat transfer is:

Q = U × A × ΔTlm

where U is the overall heat transfer coefficient (W/m²·K), A the heat transfer area and ΔTlm the **log mean temperature difference**:

ΔTlm = (ΔT1 − ΔT2) / ln (ΔT1/ΔT2)

ΔT1 and ΔT2 are the temperature differences between the two fluids at the two ends.

The heat given up by the hot fluid (or taken up by the cold fluid) is Q = m × c × (temperature change), where m is the mass flow rate and c the specific heat (4.18 kJ/kg·K for water).

## Requirements

Double-pipe (or shell-and-tube) heat exchanger set-up with hot water tank and heater, cold water supply, valves to switch between parallel and counter flow, four thermometers (or sensors) at the inlets and outlets, rotameters or measuring jar and stopwatch for flow rates.

## Procedure

1. Measure (or note from the set-up) the tube diameter and length; calculate the heat transfer area A = π D L.
2. Heat water in the tank to about 60–70 °C.
3. Set the valves for **parallel flow**. Start hot water through the inner tube and cold water through the annulus at steady, known flow rates.
4. Wait until temperatures are steady (about 10 minutes). Record hot inlet (Th1), hot outlet (Th2), cold inlet (Tc1) and cold outlet (Tc2).
5. Measure both flow rates by collecting water for a known time.
6. Switch to **counter-current flow** and repeat.

## Observations and calculations

| Flow | Hot flow (kg/s) | Cold flow (kg/s) | Th1 | Th2 | Tc1 | Tc2 |
| --- | --- | --- | --- | --- | --- | --- |
| Parallel | | | | | | |
| Counter | | | | | | |

1. Heat lost by hot water: Qh = mh × 4180 × (Th1 − Th2) W. Heat gained by cold water: Qc = mc × 4180 × (Tc2 − Tc1) W. Use the average Q.
2. Parallel flow: ΔT1 = Th1 − Tc1, ΔT2 = Th2 − Tc2. Counter flow: ΔT1 = Th1 − Tc2, ΔT2 = Th2 − Tc1.
3. ΔTlm = (ΔT1 − ΔT2) / ln (ΔT1/ΔT2).
4. U = Q ÷ (A × ΔTlm).

**Worked example (illustration only):** counter flow, mh = 0.05 kg/s, Th1 = 65, Th2 = 50 °C → Q = 0.05 × 4180 × 15 = 3135 W. Tc1 = 30, Tc2 = 42 °C. ΔT1 = 65 − 42 = 23, ΔT2 = 50 − 30 = 20, ΔTlm = 3/ln(1.15) ≈ 21.5 K. With A = 0.25 m², U = 3135/(0.25 × 21.5) ≈ 583 W/m²·K.

## Result

The overall heat transfer coefficient was ___ W/m²·K in parallel flow and ___ W/m²·K in counter-current flow. Counter-current flow gave better heat transfer.

## Precautions

1. Take readings only after steady state is reached.
2. Keep flow rates constant during a run.
3. Make sure no air is trapped in the tubes.
4. Check that heat lost and heat gained agree reasonably; a large gap means heat loss to surroundings.

## Viva questions

1. **What is the overall heat transfer coefficient?** The rate of heat transfer per unit area per degree of temperature difference across all resistances (films and wall): 1/U = 1/h1 + x/k + 1/h2.
2. **Why use LMTD and not the simple average?** Temperature difference changes along the exchanger in a logarithmic way.
3. **Why is counter-current flow better?** It keeps a larger average temperature difference and lets the cold fluid leave hotter than the hot fluid's outlet.
4. **What is fouling?** Scale or deposit on the surfaces that adds resistance and lowers U.
5. **Differentiate heat exchanger and heat interchanger.** Exchanger uses steam/hot gas as heating medium; interchanger transfers heat between two process fluids.
