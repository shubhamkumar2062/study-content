# Demonstration experiment on gas chromatography

**Aim:** To study the parts and working of a gas chromatograph, record the chromatogram of a mixture of volatile alcohols, and calculate column parameters, percentage composition by area normalisation and ethanol content by the internal standard method.

> This is a demonstration; the conditions below are typical examples. Use the method your teacher sets up and the instrument instructions. Carrier and fuel gas cylinders must be handled only by trained staff; hydrogen is flammable.

## Principle

In gas–liquid chromatography the sample is vaporised in a heated injection port and carried by an inert gas through a column containing a liquid stationary phase. Components separate according to their volatility and their interaction with the stationary phase; each leaves the column at its own **retention time**. A **flame ionisation detector (FID)** burns the eluate in a hydrogen–air flame; organic compounds produce ions and a current proportional to the amount of carbon reaching the flame. Peak area is used for quantitation.

```text
 [N2/He cylinder] -> [Regulator + flow control] -> [Heated injector] -> [Column in oven] -> [FID (H2 + air)] -> [Data system]
```

## Requirements (typical)

Gas chromatograph with FID, capillary column (for example polyethylene glycol type, 30 m × 0.32 mm) or packed column, carrier gas (nitrogen or helium), hydrogen and air for the FID, microsyringe (1–10 µl); methanol, ethanol, isopropanol, n-propanol (internal standard), water, sample (for example a hydroalcoholic preparation).

Example conditions: injector 200 °C, detector 250 °C, oven 60 °C isothermal (or programmed 40 → 150 °C at 10 °C/min), split ratio 1 : 50, injection 1 µl.

## Procedure

1. Check gas supplies; set carrier gas flow and the hydrogen and air flows for the FID; ignite the flame.
2. Set injector, oven and detector temperatures and wait for a steady baseline.
3. **Identification:** inject each alcohol separately (diluted in water) and note its retention time.
4. **Mixture:** inject the mixture and note the separated peaks.
5. **Internal standard method for ethanol:** prepare a standard containing 5% v/v ethanol and a fixed amount of n-propanol; prepare the sample with the same amount of n-propanol. Inject each and record the areas of ethanol and n-propanol.
6. Calculate resolution, plates, capacity factor, % composition and ethanol content.
7. After use, lower the oven temperature, switch off the flame gases and then the carrier gas as instructed.

## Observations and calculations

> Example readings, for practice only — record your own.

**Column parameters** (air peak t0 = 0.9 min):

| Peak | tR (min) | W (min) |
| --- | --- | --- |
| Ethanol | 2.8 | 0.12 |
| Isopropanol | 3.4 | 0.14 |

- k (ethanol) = (2.8 − 0.9)/0.9 = **2.11**
- Rs = 2(3.4 − 2.8)/(0.12 + 0.14) = 1.2/0.26 = **4.6**
- N (isopropanol) = 16(3.4/0.14)² = **9440 plates**

**Area normalisation** (peaks of similar response):

| Component | Area | % = area/total × 100 |
| --- | --- | --- |
| Methanol | 2150 | 4.3 |
| Ethanol | 46,800 | 93.6 |
| Isopropanol | 1050 | 2.1 |
| Total | 50,000 | 100 |

**Internal standard method:**

- Standard (5.0% v/v ethanol): ethanol area 38,000, n-propanol area 40,000; ratio = 0.950.
- Sample: ethanol area 36,100, n-propanol area 40,500; ratio = 0.891.
- Ethanol in sample = 5.0 × 0.891/0.950 = **4.69% v/v**.

## Result

1. Retention times: methanol ___, ethanol ___, isopropanol ___ min.
2. Rs = ___, N = ___.
3. The sample contains ___% v/v ethanol.

## Precautions

1. Never heat the column or detector without carrier gas flowing.
2. Rinse the syringe with the next sample; inject quickly and smoothly to the same depth.
3. Replace the septum regularly to avoid leaks.
4. Keep the injector hotter than the boiling point of the least volatile component.
5. Check that the FID flame is lit before injecting.

## Viva questions

1. **What is the mobile phase in GC?** An inert carrier gas such as nitrogen, helium or hydrogen.
2. **Why is FID widely used?** It is sensitive to almost all organic compounds and has a wide linear range; it does not respond to water.
3. **Why use an internal standard?** It corrects for small differences in injected volume.
4. **What is temperature programming?** Raising the oven temperature during the run to elute wide-boiling mixtures as sharp peaks.
5. **Which compounds cannot be analysed directly by GC?** Non-volatile or heat-unstable ones; they may need derivatization.
6. **Give a pharmacopoeial use of GC.** Residual solvents (headspace GC), ethanol content in tinctures.
