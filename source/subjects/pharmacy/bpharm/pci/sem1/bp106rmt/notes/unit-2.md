# Unit 2: Matrices and determinants

Matrices are a neat way to store numbers in rows and columns and to solve several equations at once. In pharmacy they appear when two drugs in one mixture are found from two absorbance readings, and when the rate equations of multi-compartment models are written together. This unit is the most predictable part of the paper: inverse of a 3 × 3 matrix, solving three equations, Cramer's rule and the Cayley–Hamilton theorem come almost every year.

## 2.1 What a matrix is

A **matrix** is a rectangular arrangement of numbers in rows and columns, written inside square brackets. A matrix with m rows and n columns has **order m × n**. The element in row i and column j is written aij.

```text
A = [ 2  −1   4 ]      order 2 × 3
    [ 0   3   5 ]      a12 = −1, a23 = 5
```

## 2.2 Types of matrices

| Type | Meaning | Example |
| --- | --- | --- |
| Row matrix | One row | [1 4 7] |
| Column matrix | One column | 3 × 1 |
| Square matrix | Rows = columns | 2 × 2, 3 × 3 |
| Rectangular | Rows ≠ columns | 2 × 3 |
| Null (zero) matrix O | All elements 0 | [0 0; 0 0] |
| Diagonal matrix | Square; all off-diagonal elements 0 | diag(2, 5, 1) |
| Scalar matrix | Diagonal with all diagonal elements equal | diag(4, 4, 4) |
| Identity (unit) matrix I | Diagonal elements 1, rest 0 | I2, I3 |
| Upper triangular | All elements below the diagonal 0 | — |
| Lower triangular | All elements above the diagonal 0 | — |
| Symmetric | A^T = A (aij = aji) | — |
| Skew-symmetric | A^T = −A (diagonal all 0) | — |
| Singular | Square, \|A\| = 0 | — |
| Non-singular | Square, \|A\| ≠ 0 | — |

```text
I3 = [ 1 0 0 ]   symmetric  [ 1 2 3 ]   skew  [  0  2 −3 ]
     [ 0 1 0 ]              [ 2 4 5 ]         [ −2  0  4 ]
     [ 0 0 1 ]              [ 3 5 6 ]         [  3 −4  0 ]
```

The **principal (leading) diagonal** runs from top-left to bottom-right. Its sum is the **trace**.

## 2.3 Operations on matrices

**Equality:** same order and every element equal.

**Addition and subtraction:** only for matrices of the same order; add or subtract element by element. A + B = B + A.

**Scalar multiplication:** multiply every element by the number k.

**Multiplication AB:** possible only when the number of **columns of A = rows of B**. The element in row i, column j of AB = (row i of A) · (column j of B): multiply pair by pair and add. If A is m × n and B is n × p, AB is m × p.

```text
A = [ 1 2 ]   B = [ 2 0 ]
    [ 3 4 ]       [ 1 3 ]

AB: row1·col1 = 1×2 + 2×1 = 4
    row1·col2 = 1×0 + 2×3 = 6
    row2·col1 = 3×2 + 4×1 = 10
    row2·col2 = 3×0 + 4×3 = 12
AB = [  4  6 ]       BA = [  2  4 ]
     [ 10 12 ]            [ 10 14 ]
```

So **AB ≠ BA** in general (matrix multiplication is not commutative). It is associative, A(BC) = (AB)C, and distributive, A(B + C) = AB + AC. A·I = I·A = A.

## 2.4 Transpose

The **transpose** A^T (or A′) is obtained by turning rows into columns.

```text
A = [ 1 2 3 ]      A^T = [ 1 4 ]
    [ 4 5 6 ]            [ 2 5 ]
                         [ 3 6 ]
```

Properties: (A^T)^T = A; (A + B)^T = A^T + B^T; (kA)^T = kA^T; **(AB)^T = B^T A^T** (order reverses).

## 2.5 Determinants

Every square matrix has a single number called its **determinant**, written |A| or det A.

```text
2 × 2:  | a b |  = ad − bc
        | c d |

3 × 3 (expand along row 1):
| a1 b1 c1 |
| a2 b2 c2 | = a1(b2c3 − b3c2) − b1(a2c3 − a3c2)
| a3 b3 c3 |        + c1(a2b3 − a3b2)
```

Signs used in expansion follow the pattern:

```text
[ + − + ]
[ − + − ]
[ + − + ]
```

**Example:** solve for x.

```text
|  2  3  4 |
| −4  x −8 | = 0
|  5  6  7 |
2(7x − (−8)(6)) − 3((−4)(7) − (−8)(5))
   + 4((−4)(6) − 5x) = 0
2(7x + 48) − 3(−28 + 40) + 4(−24 − 5x) = 0
14x + 96 − 36 − 96 − 20x = 0
−6x − 36 = 0 → x = −6
Check: with x = −6, row 2 = −2 × row 1,
so the determinant is 0 ✓
```

### Properties of determinants

1. |A^T| = |A| (rows and columns can be swapped).
2. Swapping two rows (or columns) changes the sign.
3. Two identical rows (or columns) → determinant = 0.
4. Multiplying one row by k multiplies the determinant by k; so a common factor of a row can be taken outside.
5. Adding a multiple of one row to another leaves the determinant unchanged.
6. A row of zeros → determinant = 0.
7. Determinant of a triangular or diagonal matrix = product of the diagonal elements.
8. **Product of determinants:** |AB| = |A| × |B|.

```text
Using A and B from 2.3:
|A| = 4 − 6 = −2,  |B| = 6 − 0 = 6
|AB| = 4×12 − 6×10 = −12 = (−2)(6) ✓
```

**Example using properties:** show that the determinant with rows (1, a, b + c), (1, b, c + a), (1, c, a + b) is zero.

```text
Add column 2 to column 3: column 3 becomes
(a + b + c) in every row = (a + b + c)(1, 1, 1).
Take (a + b + c) out: column 3 = column 1,
so the determinant = 0.
```

## 2.6 Minors and cofactors

- **Minor Mij** of element aij: the determinant left after deleting row i and column j.
- **Cofactor Cij** = (−1)^(i + j) Mij, i.e. the minor with the sign from the + − pattern.
- A determinant = sum of (elements of any row) × (their cofactors).

## 2.7 Adjoint, singular and non-singular matrices, inverse

- **Adjoint (adjugate) adj A** = transpose of the matrix of cofactors.
- A·(adj A) = (adj A)·A = |A| I.
- **Singular** if |A| = 0: no inverse. **Non-singular** if |A| ≠ 0: inverse exists.
- **Inverse:** A^−1 = (adj A)/|A|, and A·A^−1 = A^−1·A = I.
- 2 × 2 shortcut: for A = [a b; c d], A^−1 = (1/(ad − bc)) [d −b; −c a] (swap the diagonal, change signs of the other two).

### Example: inverse of a 3 × 3 matrix

```text
A = [ 1 0 −1 ]
    [ 1 2  1 ]
    [ 2 2  3 ]

Step 1: |A| = 1(2·3 − 1·2) − 0 + (−1)(1·2 − 2·2)
            = 1(4) − 1(−2) = 6   (≠ 0, inverse exists)

Step 2: cofactors
C11 = +(6 − 2)        = 4
C12 = −(3 − 2)        = −1
C13 = +(2 − 4)        = −2
C21 = −(0·3 − (−1)·2) = −2
C22 = +(3 − (−2))     = 5
C23 = −(2 − 0)        = −2
C31 = +(0·1 − (−1)·2) = 2
C32 = −(1 − (−1))     = −2
C33 = +(2 − 0)        = 2

Step 3: adj A = transpose of cofactor matrix
adj A = [  4 −2  2 ]
        [ −1  5 −2 ]
        [ −2 −2  2 ]

Step 4: A^−1 = (1/6) [  4 −2  2 ]
                     [ −1  5 −2 ]
                     [ −2 −2  2 ]

Check: row 1 of A × column 1 of adj A
       = 4 + 0 + 2 = 6; row 1 × column 2
       = −2 + 0 + 2 = 0 ... A·adj A = 6I ✓
```

## 2.8 Solving linear equations by the matrix method

Write the equations as **AX = B**. If |A| ≠ 0, the unique solution is **X = A^−1 B**.

**Consistency:** |A| ≠ 0 → one unique solution. |A| = 0 and (adj A)B ≠ O → no solution (inconsistent). |A| = 0 and (adj A)B = O → infinitely many solutions or none (check further).

### Example

Solve x + y + z = 6, x − y + z = 2, 2x + y − z = 1.

```text
A = [ 1  1  1 ]   X = [ x ]   B = [ 6 ]
    [ 1 −1  1 ]       [ y ]       [ 2 ]
    [ 2  1 −1 ]       [ z ]       [ 1 ]

|A| = 1(1 − 1) − 1(−1 − 2) + 1(1 + 2) = 0 + 3 + 3 = 6

Cofactors:
C11 = 0,  C12 = 3,  C13 = 3
C21 = 2,  C22 = −3, C23 = 1
C31 = 2,  C32 = 0,  C33 = −2

adj A = [ 0  2  2 ]
        [ 3 −3  0 ]
        [ 3  1 −2 ]

X = (1/6) adj A · B
x = (0×6 + 2×2 + 2×1)/6  = 6/6  = 1
y = (3×6 − 3×2 + 0×1)/6  = 12/6 = 2
z = (3×6 + 1×2 − 2×1)/6  = 18/6 = 3
Check in eq 3: 2 + 2 − 3 = 1 ✓
```

## 2.9 Cramer's rule

For AX = B with D = |A| ≠ 0: x = Dx/D, y = Dy/D, z = Dz/D, where Dx is D with the x-column replaced by the constants B (similarly Dy, Dz).

**Two equations:** 2x + 3y = 13, 3x − y = 3.

```text
D  = | 2  3 | = −2 − 9 = −11
     | 3 −1 |
Dx = | 13  3 | = −13 − 9 = −22  → x = 2
     |  3 −1 |
Dy = | 2 13 | = 6 − 39 = −33    → y = 3
     | 3  3 |
```

**Three equations** (same system as 2.8):

```text
D  = 6
Dx = | 6  1  1 |
     | 2 −1  1 | = 6(0) − 1(−3) + 1(3) = 6   → x = 1
     | 1  1 −1 |
Dy = | 1 6  1 |
     | 1 2  1 | = 1(−3) − 6(−3) + 1(−3) = 12 → y = 2
     | 2 1 −1 |
Dz = | 1  1 6 |
     | 1 −1 2 | = 1(−3) − 1(−3) + 6(3) = 18  → z = 3
     | 2  1 1 |
```

If D = 0, Cramer's rule cannot be used.

## 2.10 Characteristic equation, roots and Cayley–Hamilton theorem

For a square matrix A, **|A − λI| = 0** is the **characteristic equation**. Its roots λ are the **characteristic roots** (eigenvalues).

For a 2 × 2 matrix: λ^2 − (trace)λ + |A| = 0.
For a 3 × 3 matrix: λ^3 − (trace)λ^2 + (sum of the minors of the diagonal elements)λ − |A| = 0.

Useful facts: sum of roots = trace; product of roots = |A|; the roots of a triangular matrix are its diagonal elements.

**Cayley–Hamilton theorem:** every square matrix satisfies its own characteristic equation. If λ^2 − 4λ + 3 = 0 is the characteristic equation, then A^2 − 4A + 3I = O.

### Example (2 × 2): verify and find the inverse

```text
A = [ 2 1 ]   trace = 4, |A| = 3
    [ 1 2 ]
Characteristic equation: λ^2 − 4λ + 3 = 0
Roots: (λ − 1)(λ − 3) = 0 → λ = 1, 3

A^2 = [ 5 4 ]   4A = [ 8 4 ]   3I = [ 3 0 ]
      [ 4 5 ]        [ 4 8 ]        [ 0 3 ]
A^2 − 4A + 3I = [ 0 0 ] = O  ✓ (theorem verified)
                [ 0 0 ]

Inverse: multiply A^2 − 4A + 3I = O by A^−1:
A − 4I + 3A^−1 = O → A^−1 = (4I − A)/3
A^−1 = (1/3) [  2 −1 ]
             [ −1  2 ]
```

### Example (3 × 3)

```text
A = [ 1 2 0 ]
    [ 2 1 0 ]
    [ 0 0 3 ]
|A − λI| = (3 − λ)[(1 − λ)^2 − 4]
         = (3 − λ)(λ^2 − 2λ − 3)
Characteristic equation:
  λ^3 − 5λ^2 + 3λ + 9 = 0  → roots 3, 3, −1

A^2 = [ 5 4 0 ]    A^3 = [ 13 14  0 ]
      [ 4 5 0 ]          [ 14 13  0 ]
      [ 0 0 9 ]          [  0  0 27 ]
A^3 − 5A^2 + 3A + 9I:
 (1,1): 13 − 25 + 3 + 9 = 0
 (1,2): 14 − 20 + 6     = 0
 (3,3): 27 − 45 + 9 + 9 = 0  ... all zero ✓

A^−1 = −(A^2 − 5A + 3I)/9
     = (1/3) [ −1  2 0 ]
             [  2 −1 0 ]
             [  0  0 1 ]
```

## 2.11 Applications of matrices in pharmacy

**1. Two drugs in one mixture (simultaneous equation method).** Absorbance is additive: at each wavelength A = a1·C1 + a2·C2. Two readings give two equations, solved by matrices or Cramer's rule.

```text
Absorptivities (per µg/ml): drug X 0.05 and 0.01,
drug Y 0.02 and 0.04 at λ1 and λ2.
Readings: 0.60 at λ1, 0.30 at λ2.
0.05x + 0.02y = 0.60
0.01x + 0.04y = 0.30
D  = 0.05×0.04 − 0.02×0.01 = 0.0018
Dx = 0.60×0.04 − 0.02×0.30 = 0.018  → x = 10 µg/ml
Dy = 0.05×0.30 − 0.60×0.01 = 0.009  → y = 5 µg/ml
```

**2. Pharmacokinetic compartment models.** In a two-compartment model the rates of change of drug in the central and peripheral compartments are linked equations. Writing them as one matrix equation dX/dt = K·X, with K the matrix of rate constants, lets them be solved together; the characteristic roots of K give the two exponents (α and β) of the plasma concentration curve.

**3. Other uses:** fitting straight lines to experimental data (least squares in matrix form), storing formula batches (ingredients × products) and multiplying by unit costs to cost a production plan.

## Remember

- Order m × n; AB exists only if columns of A = rows of B; AB ≠ BA in general.
- (AB)^T = B^T A^T; |AB| = |A||B|; |A^T| = |A|.
- Cofactor = (−1)^(i + j) × minor; adj A = transpose of cofactor matrix.
- A^−1 = adj A / |A|; exists only if |A| ≠ 0.
- AX = B → X = A^−1 B; Cramer: x = Dx/D.
- Characteristic equation |A − λI| = 0; 2 × 2: λ^2 − (trace)λ + |A| = 0.
- Cayley–Hamilton: A satisfies its own characteristic equation; use it to find A^−1 and powers of A.
- Always check: A·A^−1 = I, and put the solution back into one original equation.
