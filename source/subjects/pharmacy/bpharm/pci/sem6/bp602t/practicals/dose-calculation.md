# Dose calculation in pharmacological experiments

**Aim:** To calculate the amount of drug solution to be given to a laboratory animal from the dose, the body weight and the strength of the stock solution, and to convert doses between species.

> Most BP608P experiments are demonstrated by simulation software or video. Use the dose and strength printed in your lab manual; never decide an amount yourself.

## Principle

A dose in animal work is written per unit body weight, usually **mg/kg**. The volume to inject is found from three numbers: the dose, the animal's weight and the **concentration** (strength) of the solution.

```text
 Dose (mg/kg) x body weight (kg)      =  amount of drug needed (mg)
 amount needed (mg) / strength (mg/mL) =  volume to administer (mL)
```

A second calculation converts a dose from one species to another using **body surface area**, because metabolic rate follows surface area more closely than weight. The usual tool is Paget and Barnes' conversion factor table, or the FDA's **human equivalent dose (HED)** formula with the **K_m factor** (body weight in kg ÷ body surface area in m²).

```text
 HED (mg/kg) = animal dose (mg/kg) x (K_m animal / K_m human)
 Typical K_m values: mouse 3, rat 6, rabbit 12, dog 20, human adult 37
```

**Maximum volumes** that may be given are fixed by the route and species in the CCSEA (earlier CPCSEA) guidelines and in your manual; the solution must be isotonic, sterile and of suitable pH.

## Requirements

Animal weighing balance, stock drug solution of known strength, volumetric flasks and pipettes, tuberculin or insulin syringes with suitable needles, normal saline or other vehicle, calculator, record sheet; or simulation software.

## Procedure

1. Note the drug, the dose (mg/kg) and the route from your lab manual.
2. Weigh the animal and record the weight in grams; convert to kilograms.
3. Calculate the amount of drug needed: dose × body weight.
4. Note the strength of the stock solution (for example mg/mL, or % w/v, where 1 % w/v = 10 mg/mL).
5. Calculate the volume to administer: amount needed ÷ strength.
6. Check that the volume is within the limit allowed for that route and species; if it is too large or too small, prepare a fresh dilution of suitable strength instead of changing the dose.
7. Repeat for each animal in the group and enter the values in the table before dosing.
8. For a species conversion, apply the conversion factor or K_m formula and show the working.

## Observations and calculations

**Worked example (illustrative figures only).**

A stock solution is 0.2 % w/v = 2 mg/mL. The dose fixed in the manual is 10 mg/kg, given intraperitoneally.

| Animal | Weight (g) | Weight (kg) | Drug needed (mg) | Volume of 2 mg/mL (mL) |
| --- | --- | --- | --- | --- |
| Mouse 1 | 25 | 0.025 | 0.025 × 10 = 0.25 | 0.25 ÷ 2 = 0.125 |
| Mouse 2 | 30 | 0.030 | 0.30 | 0.15 |
| Mouse 3 | 20 | 0.020 | 0.20 | 0.10 |

**Species conversion example.** A rat dose of 10 mg/kg converted to a human equivalent dose:
HED = 10 × (6 ÷ 37) = 1.62 mg/kg. For a 60 kg adult this is about 97 mg. This is only a starting estimate for study design, not a prescription.

**Percentage strength conversions**

| Statement | Meaning |
| --- | --- |
| 1 % w/v | 1 g in 100 mL = 10 mg/mL |
| 0.1 % w/v | 1 mg/mL |
| 1 in 1000 | 1 g in 1000 mL = 1 mg/mL |

## Result

The volumes of drug solution to be administered to the given animals were calculated as shown in the table, and the animal dose was converted to its human equivalent using the surface area (K_m) method.

## Precautions

1. Weigh every animal on the day of the experiment; do not use an earlier weight.
2. Keep units consistent — convert grams to kilograms and % w/v to mg/mL before dividing.
3. Check the concentration written on the stock bottle, not the one you expect.
4. Keep the injected volume within the limit for the route and species in your manual.
5. Have a second person check the calculation before dosing.
6. Use a syringe whose scale suits the small volume (tuberculin or insulin syringe).
7. Record all calculations in the notebook, including rejected ones.

## Viva questions

1. **Why is the dose expressed per kg body weight?** So that each animal gets an amount proportional to its size, making results comparable.
2. **How do you convert % w/v to mg/mL?** Multiply the percentage by 10: 0.5 % w/v = 5 mg/mL.
3. **What is the human equivalent dose?** The dose in humans expected to give the same exposure as the animal dose, calculated from body surface area using K_m factors.
4. **Why use surface area and not weight for species conversion?** Metabolic rate and clearance follow body surface area more closely than body weight.
5. **What is the K_m factor?** Body weight in kg divided by body surface area in m²; it is about 3 for mice, 6 for rats and 37 for an adult human.
6. **What should you do if the calculated volume is too large to inject?** Prepare a more concentrated solution and recalculate; do not reduce the dose.
7. **Which guidelines fix the maximum injection volumes?** The CCSEA (formerly CPCSEA) guidelines, followed by the Institutional Animal Ethics Committee.
