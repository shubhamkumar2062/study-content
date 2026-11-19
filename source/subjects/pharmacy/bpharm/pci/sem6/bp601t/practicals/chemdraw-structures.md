# Drawing structures and reactions with chemical drawing software

**Aim:** To draw the structures of given drug molecules and a complete reaction scheme using chemical structure drawing software, and to obtain the name, molecular formula and molecular weight of each structure drawn.

> Work on the computers provided in the department. Save your files in your own folder and export a copy for your record. No chemicals are used, so there is no laboratory hazard, but follow the department's rules on software use and file storage.

## Principle

Chemical drawing software converts a structure drawn on screen into a **machine-readable chemical object**, not merely a picture. Once the program understands the molecule it can:

- calculate the **molecular formula, molecular weight, exact mass and elemental analysis**;
- generate the **systematic (IUPAC) name** from the structure, and in many programs draw the structure from a name typed in;
- export the structure as a **SMILES string, InChI or MOL file**, which are the standard formats used by databases, QSAR programs and docking software;
- lay out a **reaction scheme** with arrows, reagents above the arrow and conditions below it, and check that the atoms balance.

This is why the exercise sits in a medicinal chemistry course: the same file that you draw here is the input for calculating log P and the other Lipinski properties, and for the docking and pharmacophore work described in Unit 5.

```text
   Structure drawn  →  internal connection table
            ├──→ molecular formula, molecular weight, exact mass
            ├──→ IUPAC name
            ├──→ SMILES / InChI / MOL file  →  property calculators, docking software
            └──→ reaction scheme for a report or a paper
```

## Requirements

A computer with chemical structure drawing software installed (the departmental package), the list of structures set by the teacher, and a printer or an export folder for the record.

## Procedure

1. Open the program and set the drawing settings to the standard document style, so that bond length, bond width and font are uniform throughout your work.
2. **Draw a simple ring first for practice:** select the ring tool, place a benzene ring, then use the bond tool to add substituents and the atom (text) tool to change a carbon to N, O or S.
3. Draw the first assigned structure, for example **paracetamol** or **sulphanilamide**, and check it atom by atom against the printed structure.
4. Use the chain tool for aliphatic side chains and the template library for common rings such as quinoline, imidazole, benzimidazole, the steroid nucleus and the penam and cephem systems.
5. Show **stereochemistry** where it matters, using wedge and dashed bonds, for example the 3S,5R,6R centres of a penicillin or the D-threo configuration of chloramphenicol.
6. With the structure selected, use the analysis command to display the **molecular formula and molecular weight**, and the naming command to generate the **IUPAC name**. Record both.
7. Copy the SMILES string of each structure, using the "copy as SMILES" command, and paste it into your record; this is the form in which the molecule is given to property and docking programs.
8. **Draw a reaction scheme:** place the reactant, add a reaction arrow, type the reagent above the arrow and the solvent, temperature or time below it, then draw the product. A suitable example is the hydrolysis of a beta-lactam to penicilloic acid, or the Pechmann condensation of resorcinol with ethyl acetoacetate.
9. Save the file in the program's own format and also export it as an image for your practical record.
10. Repeat for the remaining structures set by the teacher, which usually include one drug from each unit of the course.

## Observations

| Structure drawn | Molecular formula | Molecular weight | IUPAC name (from the program) |
| --- | --- | --- | --- |
| Paracetamol | C8H9NO2 | 151.16 |  |
| Sulphanilamide | C6H8N2O2S | 172.20 |  |
| Metronidazole | C6H9N3O3 | 171.15 |  |
| Ciprofloxacin | C17H18FN3O3 | 331.34 |  |
| Chloroquine | C18H26ClN3 | 319.87 |  |
| (Others set by the teacher) |  |  |  |

Record also the SMILES string of each molecule and attach a printout of the reaction scheme.

## Result

The assigned structures were drawn with chemical drawing software; their molecular formulae, molecular weights and systematic names were obtained and recorded, and a complete reaction scheme was drawn and exported.

## Precautions

1. Check every structure against the reference before accepting the name the program gives; the program names exactly what you drew, including your mistakes.
2. Watch the valency warnings the program displays; a red marker usually means a wrong number of bonds or a missing charge.
3. Draw stereochemistry deliberately with wedge and dash bonds, since a flat drawing of a chiral drug is incomplete and will not name correctly.
4. Keep one drawing style throughout the document so that the record looks consistent.
5. Save frequently and keep a backup copy of your folder.
6. Do not copy structures from the internet into your record; draw them yourself, which is the purpose of the exercise.

## Viva questions

1. **Why is a drawn structure more than a picture?** The program stores a connection table of atoms and bonds, so it can calculate properties, generate names and export standard chemical file formats.
2. **What is a SMILES string?** A line notation that represents a structure as text, for example CCO for ethanol, used to pass molecules between programs and databases.
3. **What is an InChI?** The IUPAC International Chemical Identifier, a standard text identifier that is unique for a given structure and is used for searching databases.
4. **Which file format carries the coordinates of a molecule?** The MOL or SDF file, which lists the atoms with their coordinates and the bonds between them; these are the files given to docking programs.
5. **How does the program calculate molecular weight?** It sums the standard atomic weights of all the atoms in the connection table, which is why a wrongly drawn structure gives a confidently wrong answer.
6. **Why is stereochemistry drawn with wedge and dashed bonds?** They show which groups come towards and which go away from the viewer, which is essential for chiral drugs such as chloramphenicol, ethambutol and the penicillins.
7. **How does this exercise connect with Unit 5 of the theory course?** The structures drawn here are the input for calculating log P and the other Lipinski parameters, and for pharmacophore and docking studies.
