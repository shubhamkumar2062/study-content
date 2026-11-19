# Unit 4: Analytical geometry and integration

This unit has two parts. **Analytical (coordinate) geometry** describes points and straight lines with numbers; every calibration curve and every log-concentration-versus-time plot you draw in the lab is a straight line. **Integration** is the reverse of differentiation and is used to find areas, such as the area under a blood-level curve (AUC).

## Part A: Analytical geometry

## 4.1 Coordinates and their signs

Two perpendicular number lines, the x-axis and the y-axis, meet at the **origin** O(0, 0). A point is written P(x, y): x is the **abscissa** (distance from the y-axis) and y the **ordinate** (distance from the x-axis).

```text
             y
   II (−, +) |  I (+, +)
             |
 ------------O------------ x
             |
  III (−, −) |  IV (+, −)
```

| Quadrant | Sign of x | Sign of y | Example |
| --- | --- | --- | --- |
| I | + | + | (3, 2) |
| II | − | + | (−3, 2) |
| III | − | − | (−3, −2) |
| IV | + | − | (3, −2) |

Points on the x-axis have y = 0; points on the y-axis have x = 0.

## 4.2 Distance formula

The distance between P(x1, y1) and Q(x2, y2) is

```text
PQ = √[(x2 − x1)^2 + (y2 − y1)^2]
Distance of P from the origin = √(x1^2 + y1^2)
```

It comes from Pythagoras' theorem: the horizontal gap and vertical gap form the two shorter sides of a right triangle.

**Examples:**

```text
(a) A(1, 2), B(4, 6):
    AB = √(3^2 + 4^2) = √25 = 5

(b) Show (0, 0), (3, 0), (3, 4) form a right triangle.
    sides: 3, 4 and √(9 + 16) = 5
    3^2 + 4^2 = 5^2 → right angle at (3, 0) ✓

(c) Find k if the distance between (k, 2) and (1, 5) is 5.
    (k − 1)^2 + 9 = 25 → (k − 1)^2 = 16
    k − 1 = ±4 → k = 5 or −3
```

## 4.3 Slope (gradient) of a straight line

If a line makes an angle θ with the positive x-axis, its **slope** m = tan θ.

```text
Slope of the line through (x1, y1) and (x2, y2):
   m = (y2 − y1)/(x2 − x1)
```

| Line | Slope |
| --- | --- |
| Rising left to right | positive |
| Falling left to right | negative |
| Parallel to x-axis | 0 |
| Parallel to y-axis | not defined |
| Line ax + by + c = 0 | m = −a/b |

**Parallel lines** have equal slopes: m1 = m2.
**Perpendicular lines** have slopes whose product is −1: m1 × m2 = −1.

**Examples:**

```text
(a) Slope through (2, 3) and (6, 11): (11 − 3)/(6 − 2) = 2

(b) Are (1, 1), (2, 3), (3, 5) collinear?
    slope AB = 2/1 = 2, slope BC = 2/1 = 2
    equal slopes and a common point → collinear ✓

(c) 2x − y + 3 = 0 has m = 2;
    x + 2y − 4 = 0 has m = −1/2;
    product = −1 → the lines are perpendicular
```

## 4.4 Equations of a straight line

| Form | Equation |
| --- | --- |
| Slope–intercept | y = mx + c (c = intercept on the y-axis) |
| Point–slope | y − y1 = m(x − x1) |
| Two-point | (y − y1)/(y2 − y1) = (x − x1)/(x2 − x1) |
| General | ax + by + c = 0 |

**Examples:**

```text
(a) Slope 3, y-intercept −2:  y = 3x − 2

(b) Slope and intercept of 2x + 3y − 6 = 0:
    3y = −2x + 6 → y = (−2/3)x + 2
    m = −2/3, c = 2

(c) Line through (−2, 0) perpendicular to 4x − 3y = 2:
    slope of given line = 4/3
    required slope = −3/4
    y − 0 = (−3/4)(x + 2)
    4y = −3x − 6 → 3x + 4y + 6 = 0

(d) Line through (1, 2) parallel to y = 5x + 7:
    m = 5 → y − 2 = 5(x − 1) → y = 5x − 3
```

## 4.5 Straight lines in pharmacy

**Calibration curve (Beer–Lambert law).** A = εbc, so absorbance against concentration is a straight line through the origin with slope εb.

```text
Standards: 2 µg/ml → A = 0.10; 6 µg/ml → A = 0.30
slope = (0.30 − 0.10)/(6 − 2) = 0.05 per µg/ml
intercept: 0.10 = 0.05(2) + c → c = 0
Unknown with A = 0.42: c = 0.42/0.05 = 8.4 µg/ml
```

**First-order kinetics.** log C = log C0 − kt/2.303 is the line y = mx + c with y = log C, x = t, slope m = −k/2.303 and intercept log C0. If the slope is −0.0434 per hour, k = 0.0434 × 2.303 = 0.100 per hour and t½ = 0.693/0.100 = 6.93 h.

**Zero-order kinetics.** C = C0 − k0·t is a straight line with slope −k0.

## Part B: Integration

## 4.6 Meaning of integration

If d/dx F(x) = f(x), then F(x) is an **integral (antiderivative)** of f(x):

```text
∫ f(x) dx = F(x) + c
```

The **constant of integration c** is added because the derivative of a constant is zero. ∫ is the integral sign, f(x) the integrand and dx shows the variable.

## 4.7 Standard formulae

| ∫ … dx | Result (+ c) |
| --- | --- |
| x^n (n ≠ −1) | x^(n + 1)/(n + 1) |
| 1/x | ln \|x\| |
| e^x | e^x |
| e^(ax) | e^(ax)/a |
| a^x | a^x/ln a |
| sin x | −cos x |
| cos x | sin x |
| sec^2 x | tan x |
| cosec^2 x | −cot x |
| sec x tan x | sec x |
| cosec x cot x | −cosec x |
| 1/(1 + x^2) | tan^−1 x |
| 1/√(1 − x^2) | sin^−1 x |
| 1/(x^2 + a^2) | (1/a) tan^−1(x/a) |
| 1/(x^2 − a^2) | (1/2a) ln \|(x − a)/(x + a)\| |
| 1/(a^2 − x^2) | (1/2a) ln \|(a + x)/(a − x)\| |

## 4.8 Rules of integration

1. ∫ k·f(x) dx = k ∫ f(x) dx (a constant comes out).
2. ∫ [f(x) ± g(x)] dx = ∫ f dx ± ∫ g dx.
3. There is **no** simple product rule: ∫ fg dx is not (∫f)(∫g). Products need substitution or integration by parts.

```text
(1) ∫ (3x^2 + 4x − 5) dx = x^3 + 2x^2 − 5x + c

(2) ∫ (x^2 + 1)^2/x^2 dx = ∫ (x^4 + 2x^2 + 1)/x^2 dx
    = ∫ (x^2 + 2 + x^(−2)) dx
    = x^3/3 + 2x − 1/x + c

(3) ∫ (e^x + 1/x + cos x) dx = e^x + ln|x| + sin x + c
```

## 4.9 Method of substitution

If part of the integrand is the derivative of another part, put that other part = t.

```text
(4) ∫ 2x/(x^2 + 1) dx
    t = x^2 + 1, dt = 2x dx
    = ∫ dt/t = ln t = ln(x^2 + 1) + c

(5) ∫ x e^(x^2) dx
    t = x^2, dt = 2x dx → x dx = dt/2
    = (1/2)∫ e^t dt = (1/2)e^(x^2) + c

(6) ∫ (ln x)/x dx
    t = ln x, dt = dx/x
    = ∫ t dt = (ln x)^2/2 + c

(7) ∫ (2x + 3)^5 dx
    t = 2x + 3, dx = dt/2
    = (1/2) t^6/6 = (2x + 3)^6/12 + c

(8) ∫ tan x dx = ∫ sin x/cos x dx
    t = cos x, dt = −sin x dx
    = −∫ dt/t = −ln|cos x| = ln|sec x| + c
```

Rule worth remembering: ∫ f′(x)/f(x) dx = ln|f(x)| + c.

## 4.10 Method of partial fractions

Split the rational function (Unit 1) and integrate each piece.

```text
(9) ∫ dx/(x^2 − a^2)
    1/(x^2 − a^2) = (1/2a)[1/(x − a) − 1/(x + a)]
    check: (x + a − x + a)/(x^2 − a^2) = 2a/(x^2 − a^2) ✓
    = (1/2a)[ln|x − a| − ln|x + a|]
    = (1/2a) ln|(x − a)/(x + a)| + c

(10) ∫ (3x + 5)/((x + 2)(x − 1)) dx
     = ∫ [1/(3(x + 2)) + 8/(3(x − 1))] dx
     = (1/3) ln|x + 2| + (8/3) ln|x − 1| + c

(11) ∫ dx/((x − 1)(x − 2))
     1/((x − 1)(x − 2)) = −1/(x − 1) + 1/(x − 2)
     = ln|x − 2| − ln|x − 1| = ln|(x − 2)/(x − 1)| + c
```

## 4.11 Integration by parts

For a product of two functions u and v:

```text
∫ u·v dx = u ∫ v dx − ∫ [ u′ · ∫ v dx ] dx
```

Choose u (the first function) by **ILATE**: Inverse trigonometric, Logarithmic, Algebraic, Trigonometric, Exponential — whichever comes first in this list is u.

```text
(12) ∫ x e^x dx       u = x, v = e^x
     = x e^x − ∫ 1·e^x dx = x e^x − e^x + c

(13) ∫ x sin x dx     u = x, v = sin x
     = x(−cos x) − ∫ 1·(−cos x) dx
     = −x cos x + sin x + c

(14) ∫ ln x dx = ∫ ln x · 1 dx    u = ln x, v = 1
     = x ln x − ∫ (1/x)·x dx = x ln x − x + c

(15) ∫ x ln x dx      u = ln x, v = x
     = (x^2/2) ln x − ∫ (1/x)(x^2/2) dx
     = (x^2/2) ln x − x^2/4 + c
```

Check any result by differentiating it: d/dx (x e^x − e^x) = x e^x + e^x − e^x = x e^x ✓.

## 4.12 Definite integrals

```text
∫ (from a to b) f(x) dx = [F(x)] from a to b = F(b) − F(a)
```

No constant c is needed. Properties: swapping the limits changes the sign; ∫ from a to a = 0.

```text
(16) ∫ (1 to 2) (5x^4 + 2x + 2) dx
     = [x^5 + x^2 + 2x] from 1 to 2
     = (32 + 4 + 4) − (1 + 1 + 2) = 40 − 4 = 36

(17) ∫ (0 to 1) x e^x dx = [x e^x − e^x] from 0 to 1
     = (e − e) − (0 − 1) = 1

(18) ∫ (0 to π/2) sin x dx = [−cos x] = −0 + 1 = 1

(19) ∫ (0 to 1) dx/(1 + x^2) = [tan^−1 x] = π/4 − 0 = π/4
```

## 4.13 Applications of integration

**Area under a curve.** The area between y = f(x), the x-axis and the lines x = a and x = b is ∫ (a to b) f(x) dx. Example: area under y = x^2 from 0 to 3 = [x^3/3] from 0 to 3 = 9 square units.

**Area under the plasma concentration–time curve (AUC).** AUC measures the total amount of drug that reached the blood and is used to compare bioavailability. For an IV bolus with C = C0 e^(−kt):

```text
AUC (0 to ∞) = ∫ C0 e^(−kt) dt = C0 [−e^(−kt)/k] from 0 to ∞
             = C0 (0 + 1/k) = C0/k
C0 = 20 µg/ml, k = 0.2 per h → AUC = 100 µg·h/ml
```

**Trapezoidal rule (from lab data).** Area of each strip = (C1 + C2)/2 × (t2 − t1); add the strips.

```text
t (h):     0    1    2    4
C (µg/ml): 10   8    6    4
strips: (10 + 8)/2 × 1 = 9
        (8 + 6)/2 × 1  = 7
        (6 + 4)/2 × 2  = 10
AUC (0 to 4 h) = 26 µg·h/ml
```

**Other uses:** amount of drug released from a rate equation, total amount excreted in urine, work done, and the integrated rate laws of kinetics.

## Remember

- Quadrant signs: I (+, +), II (−, +), III (−, −), IV (+, −).
- Distance = √[(x2 − x1)^2 + (y2 − y1)^2]; slope = (y2 − y1)/(x2 − x1) = tan θ.
- Parallel: m1 = m2; perpendicular: m1m2 = −1; ax + by + c = 0 has slope −a/b.
- y = mx + c; y − y1 = m(x − x1).
- ∫x^n dx = x^(n + 1)/(n + 1) + c; ∫dx/x = ln|x|; ∫e^(ax) = e^(ax)/a.
- Substitution: ∫ f′/f dx = ln|f|; partial fractions for rational functions; parts: ILATE.
- Definite integral = F(b) − F(a); AUC (IV bolus) = C0/k; trapezoids = (C1 + C2)/2 × Δt.
