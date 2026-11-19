# Determination of physicochemical properties and drug-likeness screening (Lipinski's rule of five)

**Aim:** To determine log P, clog P, molar refractivity, molecular weight and the number of hydrogen bond donors and acceptors for a set of drugs from the course, using drug design software, and to screen them against Lipinski's rule of five.

> Work on the computers provided in the department, using the software and the database access your college subscribes to. No chemicals are used. Save your results in your own folder and attach a printout to your record.

## Principle

Before a molecule is made, its chance of being an orally active drug can be judged from a few calculated properties. The exercise introduces the **descriptors used in QSAR** and the best known **drug-likeness filter**.

**The descriptors**

| Property | Meaning | Why it matters |
| --- | --- | --- |
| **Molecular weight (MW)** | Sum of the atomic weights | Large molecules diffuse poorly through membranes |
| **log P** | Logarithm of the octanol-water partition coefficient, measured | Measures lipophilicity, which governs absorption and distribution |
| **clog P** | The same quantity calculated from the structure by fragment or atom contributions | Available before the compound is made |
| **Molar refractivity (MR)** | Calculated from refractive index, molecular weight and density; reflects volume and polarisability | A steric and polarisability descriptor in QSAR |
| **Hydrogen bond donors (HBD)** | Number of OH and NH groups | Each donor must be stripped of water to cross a membrane |
| **Hydrogen bond acceptors (HBA)** | Number of N and O atoms | Too many make the molecule too polar to be absorbed |
| **Topological polar surface area (TPSA)** | Surface area of the polar atoms | Correlates with absorption and with brain penetration |
| **Rotatable bonds** | Single, non-ring, non-terminal bonds | Too many lower oral bioavailability (Veber's criterion) |

**Lipinski's rule of five.** An orally active drug usually breaks **none or at most one** of these limits, which are all multiples of five:

```text
   Molecular weight        ≤ 500
   clog P                  ≤ 5
   Hydrogen bond donors    ≤ 5
   Hydrogen bond acceptors ≤ 10
```

**Veber's additional criteria:** rotatable bonds ≤ 10 and TPSA ≤ 140 square angstroms.

The rule is a **filter for likely absorption and permeability only**. It says nothing about potency, selectivity, metabolism or safety, and there are well-known exceptions — natural products, antibiotics such as erythromycin and the penicillins, and drugs carried by active transporters.

## Requirements

A computer with drug design or cheminformatics software (the departmental package) or access to a public molecular property calculator, the structures drawn in the previous exercise or their SMILES strings, and the list of drugs set by the teacher.

## Procedure

1. Obtain the structure of each assigned drug, either by drawing it in the chemical drawing program or by copying its **SMILES string** from the previous exercise.
2. Import or paste each structure into the property calculator.
3. Compute and record **molecular weight, clog P, molar refractivity, hydrogen bond donors, hydrogen bond acceptors, TPSA and rotatable bonds** for every molecule.
4. Count the donors and acceptors **by hand as well**, directly from the drawn structure, and check that your count agrees with the program; this is the part of the exercise the examiner usually asks about.
5. Enter the values in the table and mark each of the four Lipinski criteria as passed or violated.
6. Count the violations for each drug and classify it as drug-like (none or one violation) or as a likely exception (two or more).
7. For any drug that violates the rule, write one line explaining how it is still useful — for example that it is given by injection, is actively transported, or is applied topically.
8. Repeat the calculation of log P for one molecule using a second program or method and compare, to see that calculated values differ a little between methods.

## Observations

| Drug | MW | clog P | HBD | HBA | TPSA | Rotatable bonds | Violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Paracetamol |  |  |  |  |  |  |  |
| Metronidazole |  |  |  |  |  |  |  |
| Ciprofloxacin |  |  |  |  |  |  |  |
| Chloroquine |  |  |  |  |  |  |  |
| Dapsone |  |  |  |  |  |  |  |
| Erythromycin |  |  |  |  |  |  |  |
| Amphotericin B |  |  |  |  |  |  |  |

**Worked example (counting by hand).** Paracetamol, C8H9NO2, molecular weight 151.16. Hydrogen bond donors: the phenolic OH and the amide NH, that is **2**. Hydrogen bond acceptors, counted as all nitrogen and oxygen atoms: one N and two O, that is **3**. Its clog P is about 0.5. All four criteria are satisfied, so there are **no violations** and the molecule is drug-like, which agrees with its good oral absorption.

**Worked example (an exception).** Erythromycin has a molecular weight of about 734, which exceeds 500, and several donors and many acceptors. It therefore violates the rule, yet it is used orally — a reminder that antibiotics derived from natural products are a recognised class of exceptions, and that formulation as enteric-coated or ester forms compensates in practice.

## Result

The physicochemical properties of the assigned drugs were calculated and compared with Lipinski's rule of five. Of the ______ molecules examined, ______ satisfied all four criteria, ______ showed one violation and ______ showed two or more, and the reasons for the exceptions were noted.

## Precautions

1. Check that the structure imported is the one you intended; a single wrong bond changes every calculated value.
2. Use the free base or the free acid for the calculation, not the salt, unless the teacher directs otherwise, since the rule was framed for the un-ionised molecule.
3. Remember that clog P is a calculated estimate; different programs use different fragment sets and give slightly different values.
4. Count donors as OH and NH groups and acceptors as nitrogen and oxygen atoms, and state the convention you used, because other conventions exist.
5. Do not treat a violation as proof that a molecule is useless, or compliance as proof that it is a drug; the rule predicts absorption only.
6. Record the name and version of the software used, since results are only reproducible with that information.

## Viva questions

1. **State Lipinski's rule of five.** Molecular weight not more than 500, clog P not more than 5, hydrogen bond donors not more than 5 and acceptors not more than 10, with at most one violation.
2. **Why is it called the rule of five?** Because every limit is five or a multiple of five.
3. **What does the rule predict and what does it not predict?** It predicts the likelihood of good oral absorption and permeability; it says nothing about potency, selectivity, metabolism or toxicity.
4. **What is the difference between log P and clog P?** log P is measured experimentally by partitioning between octanol and water, while clog P is calculated from the structure before the compound is made.
5. **Why is log P important in pharmacy?** It governs absorption, distribution, protein binding and the ability to cross the blood-brain barrier, and activity usually passes through an optimum log P.
6. **What is molar refractivity a measure of?** The volume of a group together with its polarisability, used as a steric descriptor in QSAR.
7. **Name two classes of drugs that commonly break the rule and are still useful.** Natural product antibiotics such as erythromycin and amphotericin B, and drugs taken up by active transporters such as levodopa; injectable and topical drugs are outside the scope of the rule altogether.
