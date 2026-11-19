# Unit 5: Differential equations and Laplace transform

A **differential equation** links a quantity with its rate of change. Almost every equation in pharmacokinetics and chemical kinetics starts as one: "the rate of loss of drug is proportional to the amount present" is dX/dt = −kX. Solving it gives the familiar exponential curve. The **Laplace transform** is a tool that turns such equations into simple algebra, which is why it is used for multi-step models such as absorption followed by elimination.

## Part A: Differential equations

## 5.1 Basic definitions

- **Differential equation (DE):** an equation containing derivatives of a dependent variable with respect to an independent variable, e.g. dy/dx = 3x^2.
- **Ordinary DE:** only one independent variable (all in this syllabus).
- **Order:** the order of the highest derivative present.
- **Degree:** the power of the highest-order derivative, after the equation is made free of fractional powers (roots) of the derivatives.
- **General solution:** contains as many arbitrary constants as the order. **Particular solution:** constants found from given conditions (initial conditions).

| Equation | Order | Degree |
| --- | --- | --- |
| d²y/dx² + 3 dy/dx + 2y = 0 | 2 | 1 |
| (dy/dx)^3 + y = x | 1 | 3 |
| (d²y/dx²)^2 + (dy/dx)^3 = 0 | 2 | 2 |
| d³y/dx³ + y = sin x | 3 | 1 |
| y = x(dy/dx) + √(1 + (dy/dx)^2) | 1 | 2 |

For the last one, move x(dy/dx) across and square: (y − x·p)^2 = 1 + p^2, where p = dy/dx. The highest power of p is now 2, so the degree is 2.

## 5.2 Equations in separable form (variables separable)

If the equation can be written f(y) dy = g(x) dx, integrate both sides.

```text
(1) dy/dx = x/y
    y dy = x dx → y^2/2 = x^2/2 + c
    → y^2 − x^2 = C

(2) dy/dx = e^(x − y) = e^x · e^(−y)
    e^y dy = e^x dx → e^y = e^x + c

(3) (1 + x^2) dy = (1 + y^2) dx
    dy/(1 + y^2) = dx/(1 + x^2)
    tan^−1 y = tan^−1 x + c

(4) dy/dx = ky   (k constant)
    dy/y = k dx → ln y = kx + c
    → y = A e^(kx)   (A = e^c)
```

Example (4) is the growth/decay law used in Section 5.6.

## 5.3 Homogeneous equations

dy/dx = f(x, y)/g(x, y) is **homogeneous** if f and g are homogeneous functions of the same degree (every term has the same total power of x and y). Then dy/dx can be written as a function of y/x.

**Method:** put y = vx, so dy/dx = v + x dv/dx. The variables then separate.

```text
(5) dy/dx = (x + y)/x
    y = vx: v + x dv/dx = 1 + v
    x dv/dx = 1 → dv = dx/x
    v = ln|x| + c → y = x ln|x| + cx

(6) dy/dx = (x^2 + y^2)/(2xy)
    y = vx: v + x dv/dx = (1 + v^2)/(2v)
    x dv/dx = (1 + v^2 − 2v^2)/(2v) = (1 − v^2)/(2v)
    2v dv/(1 − v^2) = dx/x
    −ln|1 − v^2| = ln|x| + c
    x(1 − v^2) = C → x(1 − y^2/x^2) = C
    → x^2 − y^2 = Cx
    Check: 2x − 2y y′ = C = (x^2 − y^2)/x
    → y′ = (x^2 + y^2)/(2xy) ✓
```

## 5.4 Linear differential equations

A first-order **linear** DE has the form

```text
dy/dx + P y = Q      (P, Q functions of x only)
Integrating factor (IF) = e^(∫P dx)
Solution: y × IF = ∫ (Q × IF) dx + c
```

```text
(7) dy/dx + y = e^x
    P = 1, IF = e^x
    y e^x = ∫ e^x · e^x dx = e^(2x)/2 + c
    y = e^x/2 + c e^(−x)
    Check: y′ + y = e^x/2 − c e^(−x) + e^x/2 + c e^(−x)
          = e^x ✓

(8) dy/dx + y/x = x^2
    P = 1/x, IF = e^(ln x) = x
    xy = ∫ x^3 dx = x^4/4 + c
    y = x^3/4 + c/x

(9) dy/dx − 2y = 4, y(0) = 1
    IF = e^(−2x)
    y e^(−2x) = ∫ 4e^(−2x) dx = −2e^(−2x) + c
    y = −2 + c e^(2x); y(0) = 1 → c = 3
    y = 3e^(2x) − 2
```

## 5.5 Exact equations

M dx + N dy = 0 (M, N functions of x and y) is **exact** if

```text
∂M/∂y = ∂N/∂x
```

∂M/∂y (a **partial derivative**) means differentiate M with respect to y treating x as a constant; ∂N/∂x means differentiate N with respect to x treating y as a constant.

**Solution:** ∫ M dx (treat y as constant) + ∫ (terms of N not containing x) dy = c.

```text
(10) (2xy + 3) dx + (x^2 + 4y) dy = 0
     ∂M/∂y = 2x, ∂N/∂x = 2x → exact
     ∫ M dx = x^2 y + 3x
     terms of N without x: 4y → ∫ 4y dy = 2y^2
     Solution: x^2 y + 3x + 2y^2 = c

(11) (x^2 − ay) dx + (y^2 − ax) dy = 0
     ∂M/∂y = −a, ∂N/∂x = −a → exact
     ∫ M dx = x^3/3 − axy
     N terms without x: y^2 → y^3/3
     x^3/3 − axy + y^3/3 = c
     or x^3 + y^3 − 3axy = C
```

## 5.6 Application in solving pharmacokinetic and kinetic equations

**1. First-order elimination (IV bolus, one compartment).**

```text
dC/dt = −kC   (separable)
dC/C = −k dt → ln C = −kt + c
At t = 0, C = C0 → c = ln C0
C = C0 e^(−kt)
log C = log C0 − kt/2.303
Half-life: C = C0/2 → t½ = ln 2/k = 0.693/k

Example: k = 0.1155 per h, C0 = 40 µg/ml
t½ = 0.693/0.1155 = 6 h
After 12 h (two half-lives): C = 40 × 1/4 = 10 µg/ml
```

**2. Zero-order process.**

```text
dC/dt = −k0 → C = C0 − k0 t
t½ = C0/(2k0)
```

**3. Constant-rate IV infusion (linear DE).** Drug enters at a constant rate k0 (mg/h) and leaves by first-order elimination:

```text
dX/dt = k0 − kX  →  dX/dt + kX = k0
IF = e^(kt)
X e^(kt) = ∫ k0 e^(kt) dt = (k0/k) e^(kt) + c
X(0) = 0 → c = −k0/k
X = (k0/k)(1 − e^(−kt))
As t → ∞, X → k0/k (steady state)
Css = k0/(kV) = k0/CL

Example: k0 = 10 mg/h, k = 0.1 per h, V = 20 L
Xss = 100 mg, Css = 5 mg/L
At t = t½ = 6.93 h, X = 50 mg (half of steady state)
```

## Part B: Laplace transform

## 5.7 Definition

For a function f(t) defined for t ≥ 0, the **Laplace transform** is

```text
L{f(t)} = F(s) = ∫ (0 to ∞) e^(−st) f(t) dt
```

It changes a function of time t into a function of a new variable s. Its main power: **differentiation in t becomes multiplication by s**, so a DE becomes an algebraic equation.

**Deriving two results:**

```text
L{1} = ∫ (0 to ∞) e^(−st) dt = [−e^(−st)/s] (0 to ∞)
     = 0 + 1/s = 1/s      (s > 0)

L{e^(at)} = ∫ e^(−(s − a)t) dt = 1/(s − a)   (s > a)
```

## 5.8 Laplace transforms of elementary functions

| f(t) | F(s) |
| --- | --- |
| 1 | 1/s |
| t | 1/s^2 |
| t^n (n = 1, 2, 3 …) | n!/s^(n + 1) |
| e^(at) | 1/(s − a) |
| e^(−at) | 1/(s + a) |
| sin at | a/(s^2 + a^2) |
| cos at | s/(s^2 + a^2) |
| sinh at | a/(s^2 − a^2) |
| cosh at | s/(s^2 − a^2) |

## 5.9 Properties

| Property | Statement |
| --- | --- |
| Linearity | L{a f + b g} = a F(s) + b G(s) |
| First shifting | L{e^(at) f(t)} = F(s − a) |
| Change of scale | L{f(at)} = (1/a) F(s/a) |
| Multiplication by t | L{t f(t)} = −dF/ds |
| Derivative | L{f′(t)} = sF(s) − f(0) |
| Second derivative | L{f″(t)} = s^2 F(s) − s f(0) − f′(0) |

```text
(12) L{3t^2 + 2e^(−3t) − 4 sin 2t}
     = 3(2/s^3) + 2/(s + 3) − 4(2/(s^2 + 4))
     = 6/s^3 + 2/(s + 3) − 8/(s^2 + 4)

(13) L{e^(2t) sin 3t}: L{sin 3t} = 3/(s^2 + 9);
     replace s by s − 2 → 3/((s − 2)^2 + 9)

(14) L{t e^(−t)}: L{t} = 1/s^2 → 1/(s + 1)^2
```

## 5.10 Inverse Laplace transform

L^−1{F(s)} = f(t) means L{f(t)} = F(s). Read the table backwards, using partial fractions when needed.

```text
(15) L^−1{1/(s + 4)}      = e^(−4t)
(16) L^−1{5/(s^2 + 25)}   = sin 5t
(17) L^−1{s/(s^2 + 9)}    = cos 3t
(18) L^−1{1/s^3}          = t^2/2

(19) L^−1{1/((s + 1)(s + 2))}
     1/((s + 1)(s + 2)) = 1/(s + 1) − 1/(s + 2)
     = e^(−t) − e^(−2t)

(20) L^−1{(3s + 5)/((s + 2)(s − 1))}
     = L^−1{(1/3)/(s + 2) + (8/3)/(s − 1)}
     = (1/3)e^(−2t) + (8/3)e^t

(21) L^−1{(s + 3)/(s^2 + 4s + 13)}
     s^2 + 4s + 13 = (s + 2)^2 + 9
     (s + 3) = (s + 2) + 1
     = e^(−2t) cos 3t + (1/3) e^(−2t) sin 3t
```

## 5.11 Solving linear differential equations

**Steps:** (1) take the Laplace transform of both sides, using the derivative formulas and the initial values; (2) solve the algebra for Y(s); (3) split by partial fractions; (4) take the inverse transform.

```text
(22) y′ + 2y = 0, y(0) = 3
     sY − 3 + 2Y = 0 → Y = 3/(s + 2)
     y = 3e^(−2t)

(23) y′ + y = 1, y(0) = 0
     sY + Y = 1/s → Y = 1/(s(s + 1))
     = 1/s − 1/(s + 1)
     y = 1 − e^(−t)

(24) y″ − 3y′ + 2y = 0, y(0) = 0, y′(0) = 1
     (s^2 Y − 0 − 1) − 3(sY − 0) + 2Y = 0
     Y(s^2 − 3s + 2) = 1
     Y = 1/((s − 1)(s − 2)) = −1/(s − 1) + 1/(s − 2)
     y = e^(2t) − e^t
     Check: y(0) = 0; y′ = 2e^(2t) − e^t → y′(0) = 1 ✓
```

## 5.12 Application in chemical kinetics and pharmacokinetics

**1. IV bolus.** dX/dt = −kX, X(0) = D (the dose).

```text
sX̄ − D = −kX̄ → X̄ = D/(s + k) → X = D e^(−kt)
```

(X̄ is the Laplace transform of X.)

**2. Oral dose, one compartment, first-order absorption.** Xa = amount at the absorption site, X = amount in the body, F = fraction absorbed.

```text
dXa/dt = −ka Xa,          Xa(0) = F·D
dX/dt  = ka Xa − kX,      X(0)  = 0
Transform:
X̄a = F·D/(s + ka)
sX̄ = ka X̄a − kX̄ → X̄ = ka F D/((s + ka)(s + k))
Partial fractions:
1/((s + ka)(s + k)) = [1/(ka − k)] [1/(s + k) − 1/(s + ka)]
Inverse:
X = [ka F D/(ka − k)] (e^(−kt) − e^(−ka·t))
C = X/V
```

This is the **Bateman equation** that describes the rise and fall of blood levels after a tablet. The time of its peak is found in Unit 3.

**3. IV infusion.** dX/dt = k0 − kX, X(0) = 0.

```text
sX̄ = k0/s − kX̄ → X̄ = k0/(s(s + k))
= (k0/k)[1/s − 1/(s + k)]
X = (k0/k)(1 − e^(−kt))   (same answer as 5.6)
```

**4. Consecutive reactions A → B → C** (rate constants k1, k2) give the same algebra as the oral model: [B] = k1A0/(k2 − k1) × (e^(−k1 t) − e^(−k2 t)). Drug degradation through an intermediate follows this pattern.

## Remember

- Order = highest derivative; degree = its power after removing roots.
- Separable: f(y)dy = g(x)dx; homogeneous: y = vx; linear: IF = e^(∫P dx), y·IF = ∫Q·IF dx + c.
- Exact if ∂M/∂y = ∂N/∂x; solution ∫M dx + ∫(N terms without x) dy = c.
- dC/dt = −kC → C = C0e^(−kt), t½ = 0.693/k; infusion → X = (k0/k)(1 − e^(−kt)).
- L{f} = ∫ (0 to ∞) e^(−st) f dt; L{1} = 1/s, L{t^n} = n!/s^(n + 1), L{e^(at)} = 1/(s − a), L{sin at} = a/(s^2 + a^2), L{cos at} = s/(s^2 + a^2).
- L{f′} = sF − f(0); L{f″} = s^2F − s f(0) − f′(0); first shifting: e^(at) → s − a.
- Laplace method: transform → solve for Y → partial fractions → inverse.
