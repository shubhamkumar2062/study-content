# Last-night revision sheet

If you have only one evening, practise one full example of each of these: **partial fractions with a repeated factor**, **inverse of a 3 × 3 matrix**, **Cayley–Hamilton verification**, **maxima and minima of a cubic**, **integration by parts**, **a linear differential equation**, and **solving a differential equation by Laplace transform**. Together they cover most long answers.

**Partial fractions (Unit 1)**

| Denominator factor | Write |
| --- | --- |
| (x − a) | A/(x − a) |
| (x − a)^2 | A/(x − a) + B/(x − a)^2 |
| (x^2 + bx + c), no real factors | (Ax + B)/(x^2 + bx + c) |

Improper fraction → divide first. Find constants by putting x = roots, then compare coefficients. Check at x = 0.

**Logarithms (Unit 1)**

- log(mn) = log m + log n; log(m/n) = log m − log n; log m^n = n log m; log_a a = 1; log 1 = 0.
- ln x = 2.303 log x; log_a N = log N/log a.
- Characteristic: number > 1 → (digits before decimal − 1); 0 < number < 1 → −(zeros after decimal + 1). Mantissa always positive: log 0.0345 = 2̄.5378.
- pH = −log[H+]; pH = pKa + log([salt]/[acid]); k = (2.303/t) log(C0/C).

**Limits and continuity (Unit 1)**

- lim (x → a) (x^n − a^n)/(x − a) = n·a^(n − 1); lim (θ → 0) sin θ/θ = 1; lim (1 − cos x)/x^2 = 1/2.
- Try substitution first; on 0/0 factorise, rationalise or use a standard limit.
- Continuous at a: f(a) defined, LHL = RHL = f(a).

**Matrices (Unit 2)**

- AB needs columns of A = rows of B; AB ≠ BA; (AB)^T = B^T A^T; |AB| = |A||B|.
- Cofactor Cij = (−1)^(i + j) Mij; adj A = (cofactor matrix)^T; A^−1 = adj A/|A| (needs |A| ≠ 0).
- 2 × 2: [a b; c d]^−1 = (1/(ad − bc))[d −b; −c a].
- AX = B → X = A^−1B; Cramer: x = Dx/D, y = Dy/D, z = Dz/D.
- Characteristic equation |A − λI| = 0; 2 × 2: λ^2 − (trace)λ + |A| = 0. Cayley–Hamilton: A satisfies it.

**Derivatives (Unit 3)**

| f | f′ | f | f′ |
| --- | --- | --- | --- |
| x^n | n x^(n − 1) | sin x | cos x |
| e^x | e^x | cos x | −sin x |
| a^x | a^x ln a | tan x | sec^2 x |
| ln x | 1/x | sec x | sec x tan x |
| √x | 1/(2√x) | cot x | −cosec^2 x |

Product uv′ + vu′; quotient (vu′ − uv′)/v^2; chain: × derivative of the inside. Max: f′ = 0, f″ < 0; min: f′ = 0, f″ > 0. tmax = ln(ka/k)/(ka − k).

**Geometry (Unit 4)**

- Distance √[(x2 − x1)^2 + (y2 − y1)^2]; slope (y2 − y1)/(x2 − x1); ax + by + c = 0 → m = −a/b.
- Parallel m1 = m2; perpendicular m1m2 = −1; y = mx + c; y − y1 = m(x − x1).

**Integrals (Unit 4)**

| ∫ | Result | ∫ | Result |
| --- | --- | --- | --- |
| x^n | x^(n + 1)/(n + 1) | sin x | −cos x |
| 1/x | ln\|x\| | cos x | sin x |
| e^(ax) | e^(ax)/a | sec^2 x | tan x |
| a^x | a^x/ln a | 1/(1 + x^2) | tan^−1 x |
| f′/f | ln\|f\| | 1/(x^2 − a^2) | (1/2a) ln\|(x − a)/(x + a)\| |

By parts: ∫uv dx = u∫v dx − ∫[u′∫v dx]dx, u chosen by ILATE. Definite: F(b) − F(a). AUC (IV bolus) = C0/k; trapezoid strip = (C1 + C2)/2 × Δt.

**Differential equations (Unit 5)**

| Type | Method |
| --- | --- |
| Separable | f(y)dy = g(x)dx, integrate both sides |
| Homogeneous | y = vx, dy/dx = v + x dv/dx |
| Linear dy/dx + Py = Q | IF = e^(∫P dx); y·IF = ∫Q·IF dx + c |
| Exact M dx + N dy = 0 | ∂M/∂y = ∂N/∂x; ∫M dx + ∫(N terms without x) dy = c |

Kinetics: dC/dt = −kC → C = C0e^(−kt), t½ = 0.693/k; zero order C = C0 − k0t, t½ = C0/2k0; infusion X = (k0/k)(1 − e^(−kt)), Css = k0/CL.

**Laplace transform (Unit 5)**

| f(t) | F(s) | f(t) | F(s) |
| --- | --- | --- | --- |
| 1 | 1/s | sin at | a/(s^2 + a^2) |
| t^n | n!/s^(n + 1) | cos at | s/(s^2 + a^2) |
| e^(at) | 1/(s − a) | sinh at | a/(s^2 − a^2) |
| e^(−at) | 1/(s + a) | cosh at | s/(s^2 − a^2) |

L{f′} = sF − f(0); L{f″} = s^2F − s f(0) − f′(0); L{e^(at)f} = F(s − a). Oral one-compartment model: X = [ka F D/(ka − k)](e^(−kt) − e^(−ka·t)).

**Five checks before you hand in:** partial fractions recombine; A·A^−1 = I; solution satisfies the original equations; derivative of your integral gives the integrand; every indefinite integral ends with + c.
