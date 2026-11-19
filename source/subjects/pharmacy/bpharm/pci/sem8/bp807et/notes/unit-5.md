# Unit 5: Molecular modelling — mechanics, quantum methods, energy minimisation and conformational analysis

Docking, pharmacophore mapping and 3D-QSAR all assume we know what a molecule actually looks like in three dimensions and how much energy each shape costs. This unit supplies that foundation: the two ways of calculating molecular energy (molecular mechanics and quantum mechanics), how a structure is relaxed to a minimum, and how the biologically relevant shape is found among the many a flexible molecule can adopt.

## 5.1 What molecular modelling means

**Molecular modelling** is the use of theoretical and computational methods to build, display and calculate the structures, properties and behaviour of molecules. It answers questions such as: what is the lowest-energy shape of this drug? Where is its negative charge concentrated? How much energy is needed to rotate this bond? How well does it fit this receptor?

Two levels of theory are used:

| | Molecular mechanics (MM) | Quantum mechanics (QM) |
| --- | --- | --- |
| Treats the molecule as | Balls (atoms) joined by springs (bonds) — classical physics | Nuclei and electrons, solving the Schrödinger equation |
| Electrons | Not treated explicitly | Treated explicitly |
| Speed | Very fast; thousands of atoms, long simulations | Slow; tens to a few hundred atoms |
| Can it break or form bonds? | No (bond types are fixed) | Yes |
| Gives | Geometry, strain energy, conformational energy | Geometry plus electron density, orbitals, charges, spectra, reaction paths |
| Typical use in drug design | Energy minimisation, conformational search, docking, molecular dynamics, whole proteins | Partial charges, HOMO/LUMO, electrostatic potential maps, small-molecule geometry, mechanism studies |

## 5.2 Molecular mechanics and the force field

A **force field** is the set of equations and the parameters (equilibrium bond lengths, angles, force constants, atomic charges, van der Waals radii) used to calculate the potential energy of a molecule from its geometry.

```text
E(total) = E(bond stretching)
         + E(angle bending)
         + E(torsion / dihedral)
         + E(out-of-plane / improper)
         + E(van der Waals)
         + E(electrostatic)
         ( + E(hydrogen bond), + cross terms, + solvation term )

bonded terms: the first four      non-bonded terms: the last two
```

| Term | Usual equation | Meaning |
| --- | --- | --- |
| Bond stretching | Eb = Σ kb(l − l0)² | Hooke's law spring; l0 is the natural bond length. (A Morse function is more accurate but slower.) |
| Angle bending | Eθ = Σ kθ(θ − θ0)² | Resistance to opening or closing a bond angle |
| Torsion | Eφ = Σ (Vn/2)[1 + cos(nφ − γ)] | Energy as a bond is rotated; n is the periodicity (3 for ethane), γ the phase |
| Out-of-plane | Harmonic penalty | Keeps sp² centres and aromatic rings flat |
| van der Waals | Lennard-Jones 12-6: E = ε[(r0/r)¹² − 2(r0/r)⁶] | Steep repulsion when atoms clash, weak attraction (London forces) at longer range |
| Electrostatic | Coulomb: E = qiqj/(4πε0 εr r) | Attraction or repulsion between partial charges; a distance-dependent dielectric is often used to imitate water |

**Important properties of MM energies**

- The number is a **steric (strain) energy**, meaningful only when comparing conformers or isomers of the **same** molecule with the **same** force field. It is not a heat of formation and cannot be compared between force fields.
- Parameters are fitted to experimental data (crystal structures, spectra) and to QM calculations. A molecule with unusual atoms may be outside the parameter set — then the program guesses, and the result is unreliable.

**Common force fields:** MM2, MM3 and MM4 (small organic molecules, very accurate geometries), AMBER and CHARMM (proteins and nucleic acids, also used for drug–protein systems), GROMOS (simulations), OPLS (liquids and proteins), MMFF94 (broad coverage of drug-like organics), UFF and DREIDING (generic, cover nearly the whole periodic table but with lower accuracy).

## 5.3 Quantum mechanics methods

QM solves (approximately) the Schrödinger equation HΨ = EΨ under the Born–Oppenheimer approximation (nuclei fixed, electrons move around them).

| Class | Approach | Examples | Comment |
| --- | --- | --- | --- |
| **Ab initio** | From first principles, no experimental parameters | Hartree–Fock (HF); beyond-HF methods such as MP2 and coupled cluster | Most rigorous and most expensive; needs a **basis set** (STO-3G minimal, 3-21G, 6-31G*, 6-311++G**; polarisation functions * and diffuse functions + improve accuracy) |
| **Semi-empirical** | Simplified QM — valence electrons only, many integrals replaced by parameters fitted to experiment | CNDO, INDO, MINDO/3, MNDO, AM1, PM3 | Hundreds of times faster than ab initio; good for geometries, heats of formation and charges of ordinary organic molecules; poor for unusual bonding |
| **Density functional theory (DFT)** | Energy expressed as a functional of the electron density instead of the wave function | B3LYP, M06, PBE with similar basis sets | Accuracy near good ab initio at much lower cost; the usual choice today for medium-sized molecules |
| **Hybrid QM/MM** | The reactive site treated by QM, the rest of the protein by MM | Used for enzyme mechanisms | Lets a reaction be studied inside a whole protein |

**What QM gives a drug designer**

- Accurate geometries and relative energies, including strained or conjugated systems.
- **Partial atomic charges** (Mulliken, electrostatic-potential-derived) used later in docking and MM calculations.
- **Molecular electrostatic potential (MEP) maps** — coloured surfaces showing where a molecule is electron-rich (red, attracts positive charge or donates to an H-bond acceptor) and electron-poor (blue).
- **Frontier orbitals**: HOMO (highest occupied) relates to electron-donating ability, LUMO (lowest unoccupied) to electron-accepting ability; the HOMO–LUMO gap relates to reactivity and stability. These appear as descriptors in QSAR.
- Dipole moment, polarisability, ionisation potential, electron affinity.
- Transition states and reaction energetics (mechanism of an enzyme, stability of a prodrug).

## 5.4 Energy minimisation (geometry optimisation)

A structure drawn on screen or taken from a database has unrealistic bond lengths and clashes. **Energy minimisation** adjusts the coordinates step by step until the net force on every atom is essentially zero — a point where the first derivative of energy with respect to the coordinates is zero and the second derivative is positive (a minimum, not a maximum or saddle point).

```text
Energy
  |        X start
  |         \
  |          \      local minimum
  |           \____/\
  |                  \        global minimum
  |                   \______/
  +-------------------------------------> geometry (one coordinate)

Minimisation only runs downhill, so it always lands in the nearest
minimum - not necessarily the lowest one.
```

| Method | Derivatives used | How it works | Points to remember |
| --- | --- | --- | --- |
| **Steepest descent** | First | Move along the direction of the steepest downhill gradient; repeat | Very robust, excellent for a badly strained starting structure; converges slowly near the minimum because successive steps are at right angles and it zig-zags |
| **Conjugate gradient** | First | Each new direction takes the previous ones into account, avoiding zig-zag | Faster convergence than steepest descent; the usual workhorse, often run after a few hundred steps of steepest descent |
| **Newton–Raphson** | First and second (Hessian) | Uses curvature to jump close to the minimum in few steps | Converges very fast near a minimum, but the Hessian is expensive (memory grows with the square of the number of atoms) and it can fail far from the minimum |
| **Quasi-Newton (BFGS, adopted-basis NR)** | First, with an estimated Hessian | Builds up curvature information as it goes | Good compromise, widely used in practice |

**Convergence criteria:** the run stops when the energy change between steps, or the root-mean-square gradient, falls below a set value, or when a maximum number of steps is reached.

**Practical sequence:** clean the structure → add hydrogens → assign the force field → steepest descent (removes bad contacts) → conjugate gradient (refines) → check the final geometry and gradient.

**The key limitation:** minimisation is a downhill-only procedure. It finds the **local** minimum nearest the starting point. Finding the **global** minimum needs a search method (Section 5.6).

## 5.5 Conformational analysis

**Conformers** are the different arrangements of the same molecule produced by rotation about single bonds, without breaking any bond.

- A molecule with N atoms has 3N − 6 internal degrees of freedom (3N − 5 if linear); for a 20-atom molecule that is 54.
- The practical variables are the **rotatable (torsion) bonds**. If each rotatable bond is sampled at only three staggered positions, 5 rotatable bonds give 3⁵ = 243 conformers and 10 give 3¹⁰ = 59,049. This explosion is why systematic searching fails for flexible molecules.

**Potential energy surface (PES):** a plot of energy against the geometric variables. Minima are stable conformers; the highest point on the lowest path between two minima is the **transition state** (rotational barrier).

```text
Ethane, rotation about C-C          n-Butane, rotation about C2-C3

E |   /\      /\      /\            E |    /\      ___      /\
  |  /  \    /  \    /  \             |   /  \    /   \    /  \
  | /    \__/    \__/    \            |__/    \__/     \__/    \__
  +---------------------------->      +----------------------------->
  0   60  120 180 240 300 360         0   60  120 180 240 300 360

Minima at 60, 180, 300 (staggered)   anti (180) lowest; two gauche
Maxima at 0, 120, 240 (eclipsed)     minima (60, 300) slightly higher
```

Standard results you should be able to state: ethane has a three-fold barrier of about 3 kcal/mol (12 kJ/mol); n-butane's anti conformer is the most stable, the gauche conformers are a little higher, and the syn (fully eclipsed) arrangement is the highest point; cyclohexane prefers the chair, with the twist-boat and boat much higher, and a bulky substituent prefers the equatorial position.

**Boltzmann populations.** At equilibrium the ratio of two conformers is N2/N1 = exp(−ΔE/RT). At 25 °C (298 K, RT ≈ 0.59 kcal/mol):

| ΔE (kcal/mol) | Share of the higher conformer | Share of the lower conformer |
| --- | --- | --- |
| 0.5 | about 30 % | about 70 % |
| 1.0 | about 16 % | about 84 % |
| 2.0 | about 3 % | about 97 % |
| 3.0 | under 1 % | over 99 % |

So differences of 2–3 kcal/mol already decide which shape a molecule is in — but note that the **bioactive conformation** (the shape bound to the receptor) is often *not* the global minimum. The binding energy released can pay for a strain of a few kcal/mol, so conformers within roughly 5–10 kcal/mol of the minimum are all kept as candidates for docking.

**Ways to study conformation**

- Experimental: X-ray crystallography (the solid-state conformation), NMR coupling constants and NOE (solution conformation), the Cambridge Structural Database for preferred torsion values.
- Computational: torsion driving (rotate one bond in fixed steps and minimise the rest at each step), full conformational search, molecular dynamics.

**Ramachandran plot** — for proteins, a plot of the backbone torsions φ (phi) against ψ (psi) showing the allowed regions (right-handed α-helix, β-sheet, left-handed helix). It is the standard check on the quality of a protein structure or a homology model.

## 5.6 Finding the global conformational minimum

The **multiple-minimum problem**: the number of minima grows roughly exponentially with the number of rotatable bonds, so the lowest one cannot be found simply by minimising once.

| Method | How it searches | Notes |
| --- | --- | --- |
| **Systematic (grid) search** | Rotate every rotatable bond through fixed increments and minimise each combination | Complete and reproducible for rigid or nearly rigid molecules; impossible beyond about 6–8 rotatable bonds (combinatorial explosion). Tree pruning and rules reduce the cost |
| **Monte Carlo** | Make a random change to a torsion, accept it if the energy falls; if it rises, accept with probability exp(−ΔE/kT) (the Metropolis criterion) | The uphill moves let it escape local minima |
| **Simulated annealing** | Monte Carlo (or dynamics) starting at a high temperature and cooling slowly | Mimics the annealing of a metal; widely used in docking and structure refinement |
| **Molecular dynamics (MD)** | Solve Newton's equations of motion in small time steps (typically 1–2 fs) at a chosen temperature; the molecule explores the surface over time | Gives motion and time-dependent behaviour; high temperature runs help cross barriers; snapshots are then minimised |
| **Genetic algorithm** | A population of conformers encoded as "chromosomes" of torsion angles; selection, crossover and mutation across generations | Efficient for flexible ligands; used by several docking programs |
| **Distance geometry** | Generate coordinates from allowed interatomic distance ranges, then minimise | Used in NMR structure determination and in some conformer generators |
| **Low-mode / normal-mode search** | Follow the soft vibrational modes out of a minimum, then minimise again | Good at finding related minima efficiently |

**Practical routine:** generate many conformers by one of the above → minimise each → remove duplicates (by RMSD) → keep everything within an energy window of the lowest → use this set for pharmacophore searching, 3D-QSAR alignment or ensemble docking.

**Important cautions**

1. No search method can *prove* that the global minimum has been found; confidence comes from repeating the search from different starting points and seeing the same lowest structure appear again and again.
2. Most routine calculations are done in the gas phase. Water changes relative energies a great deal — intramolecular hydrogen bonds that dominate in vacuum often open up in water. Use a solvation model (implicit continuum or explicit water) when the answer matters.
3. Garbage in, garbage out: wrong protonation state, wrong tautomer, wrong stereochemistry or a missing parameter will produce a confident but meaningless number.

## Remember

1. MM = balls and springs, no electrons, fast, cannot break bonds. QM = electrons included, slow, can study reactions and gives charges, HOMO/LUMO and MEP maps.
2. Force field terms: bond stretch + angle bend + torsion + out-of-plane (bonded) and van der Waals + electrostatic (non-bonded). Lennard-Jones 12-6 for van der Waals, Coulomb for electrostatics.
3. Name force fields: MM2/MM3, AMBER, CHARMM, OPLS, GROMOS, MMFF94. MM strain energy is comparable only within the same molecule and the same force field.
4. QM classes: ab initio (HF, basis sets such as STO-3G and 6-31G*), semi-empirical (CNDO, MINDO, MNDO, AM1, PM3), DFT (B3LYP), and QM/MM hybrids.
5. Minimisation methods: steepest descent (first derivative, robust, slow near the end), conjugate gradient (first derivative, no zig-zag), Newton–Raphson (second derivative, fast near the minimum, expensive Hessian). All go downhill only, so they stop at the nearest local minimum.
6. Conformers arise from rotation about single bonds; 3N − 6 degrees of freedom; three positions per rotatable bond give 3ⁿ combinations.
7. N2/N1 = exp(−ΔE/RT); about 2 kcal/mol already gives a 97:3 split at room temperature. The bioactive conformation need not be the global minimum, so keep a window of low-energy conformers.
8. Global search methods: systematic grid, Monte Carlo (Metropolis criterion), simulated annealing, molecular dynamics, genetic algorithms, distance geometry, low-mode search.
