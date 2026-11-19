# Unit 3: Calculus — differentiation, maxima and minima

Differentiation measures **how fast one quantity changes when another changes**. In pharmacy the rate at which a drug's concentration falls, the rate of a reaction and the time of the highest blood level are all derivatives. The syllabus asks for the rules without proof; what the examiner wants is correct, neat working.

Notation: dy/dx (or y′, f′(x)) is the derivative of y with respect to x. d²y/dx² (or y″) is the second derivative.

## 3.1 Derivative of a function

If y = f(x) and x changes by a small amount h, y changes by f(x + h) − f(x). The average rate is [f(x + h) − f(x)]/h. Its limit as h → 0 is the **derivative**:

```text
dy/dx = lim (h → 0) [f(x + h) − f(x)] / h
```

This is called differentiation **from first principles**. Geometrically, dy/dx is the **slope of the tangent** to the curve y = f(x) at the point x.

**Example (first principles):** y = x^2.

```text
f(x + h) − f(x) = (x + h)^2 − x^2 = 2xh + h^2
divide by h: 2x + h
limit as h → 0: 2x
So d/dx (x^2) = 2x
```

## 3.2 Standard derivatives (learn by heart)

| Function | Derivative |
| --- | --- |
| c (constant) | 0 |
| x^n (n any rational number) | n·x^(n − 1) |
| √x | 1/(2√x) |
| 1/x | −1/x^2 |
| e^x | e^x |
| a^x | a^x · ln a |
| ln x (log_e x) | 1/x |
| log_a x | 1/(x ln a) |
| sin x | cos x |
| cos x | −sin x |
| tan x | sec^2 x |
| cot x | −cosec^2 x |
| sec x | sec x · tan x |
| cosec x | −cosec x · cot x |

## 3.3 Rules of differentiation

| Rule | Formula |
| --- | --- |
| Constant times a function | d/dx [c·f] = c·f′ |
| Sum or difference | d/dx [u ± v] = u′ ± v′ |
| Product (uv rule) | d/dx [uv] = u·v′ + v·u′ |
| Quotient (u/v rule) | d/dx [u/v] = (v·u′ − u·v′)/v^2 |
| Function of a function (chain) | dy/dx = (dy/du)·(du/dx) |

Memory line for the quotient rule: "bottom times derivative of top, minus top times derivative of bottom, all over bottom squared".

### Worked examples: basic rules

```text
(1) y = 3x^4 − 5x^2 + 7x − 2
    dy/dx = 12x^3 − 10x + 7

(2) y = √x + 1/x = x^(1/2) + x^(−1)
    dy/dx = (1/2)x^(−1/2) − x^(−2)
          = 1/(2√x) − 1/x^2

(3) y = 5e^x + 3 ln x − 2^x
    dy/dx = 5e^x + 3/x − 2^x ln 2

(4) y = 4 sin x − 3 cos x + tan x
    dy/dx = 4 cos x + 3 sin x + sec^2 x
```

### Worked examples: product rule

```text
(5) y = x^2 sin x
    u = x^2, v = sin x
    dy/dx = x^2 cos x + sin x · 2x
          = x^2 cos x + 2x sin x

(6) y = x^4 · e^x · ln x   (three factors)
    dy/dx = 4x^3 e^x ln x + x^4 e^x ln x + x^4 e^x (1/x)
          = x^3 e^x (4 ln x + x ln x + 1)

(7) y = e^x ln x
    dy/dx = e^x (1/x) + ln x · e^x = e^x (1/x + ln x)
```

For three factors, differentiate one at a time and keep the other two: (uvw)′ = u′vw + uv′w + uvw′.

### Worked examples: quotient rule

```text
(8) y = (x^2 + 1)/(x − 1)
    u = x^2 + 1, u′ = 2x; v = x − 1, v′ = 1
    dy/dx = [(x − 1)(2x) − (x^2 + 1)(1)]/(x − 1)^2
          = (2x^2 − 2x − x^2 − 1)/(x − 1)^2
          = (x^2 − 2x − 1)/(x − 1)^2

(9) y = sin x/(1 + cos x)
    dy/dx = [(1 + cos x)cos x − sin x(−sin x)]/(1 + cos x)^2
          = (cos x + cos^2 x + sin^2 x)/(1 + cos x)^2
          = (1 + cos x)/(1 + cos x)^2 = 1/(1 + cos x)

(10) y = ln x / x
    dy/dx = [x(1/x) − ln x(1)]/x^2 = (1 − ln x)/x^2
```

### Worked examples: chain rule

```text
(11) y = (2x + 3)^5
     dy/dx = 5(2x + 3)^4 × 2 = 10(2x + 3)^4

(12) y = e^(−kt)      (differentiate with respect to t)
     dy/dt = e^(−kt) × (−k) = −k e^(−kt)

(13) y = sin(x^2)
     dy/dx = cos(x^2) × 2x = 2x cos(x^2)

(14) y = ln(x^2 + 1)
     dy/dx = 2x/(x^2 + 1)
```

## 3.4 Successive differentiation

Differentiating again gives the second derivative d²y/dx², then the third d³y/dx³, and so on.

```text
(15) y = x^3 + e^(2x)
     y′  = 3x^2 + 2e^(2x)
     y″  = 6x + 4e^(2x)
     y‴  = 6 + 8e^(2x)

(16) y = e^(ax): nth derivative = a^n e^(ax)

(17) y = sin 2x. Show y″ + 4y = 0.
     y′ = 2 cos 2x;  y″ = −4 sin 2x = −4y
     so y″ + 4y = 0 ✓

(18) y = A e^(mx) + B e^(−mx). Show y″ = m^2 y.
     y′ = mA e^(mx) − mB e^(−mx)
     y″ = m^2 A e^(mx) + m^2 B e^(−mx) = m^2 y ✓
```

Physical meaning: if s is distance and t time, ds/dt is velocity and d²s/dt² is acceleration.

## 3.5 Maxima and minima

At a highest point (**maximum**) or lowest point (**minimum**) of a smooth curve, the tangent is horizontal, so dy/dx = 0. Such points are **stationary (critical) points**.

```text
        max
        __
       /  \          dy/dx = 0 at both turning points
      /    \     /   left of max: rising (dy/dx > 0)
     /      \__ /    left of min: falling (dy/dx < 0)
               min
```

**Conditions (second-derivative test):**

| At x = a | Result |
| --- | --- |
| f′(a) = 0 and f″(a) < 0 | Maximum at a |
| f′(a) = 0 and f″(a) > 0 | Minimum at a |
| f′(a) = 0 and f″(a) = 0 | Test fails; check the sign of f′ on both sides |

**Steps:** (1) find f′(x); (2) solve f′(x) = 0; (3) find f″(x) at each root; (4) decide max or min; (5) put x back into f(x) for the maximum or minimum value.

### Example 1

Find the maximum and minimum values of f(x) = 2x^3 − 15x^2 + 36x + 10.

```text
f′(x) = 6x^2 − 30x + 36 = 6(x^2 − 5x + 6)
      = 6(x − 2)(x − 3) = 0 → x = 2 or 3
f″(x) = 12x − 30
x = 2: f″ = −6 < 0 → maximum
       f(2) = 16 − 60 + 72 + 10 = 38
x = 3: f″ = 6 > 0 → minimum
       f(3) = 54 − 135 + 108 + 10 = 37
Maximum value 38 (at x = 2);
minimum value 37 (at x = 3).
```

### Example 2

f(x) = x^3 − 3x^2 − 9x + 5.

```text
f′(x) = 3x^2 − 6x − 9 = 3(x − 3)(x + 1) = 0
x = 3 or −1;  f″(x) = 6x − 6
x = −1: f″ = −12 → maximum, f(−1) = −1 − 3 + 9 + 5 = 10
x = 3:  f″ = 12  → minimum, f(3) = 27 − 27 − 27 + 5 = −22
```

### Example 3: when there is no maximum or minimum

f(x) = x^3/3 − 10x^2 + 300x.

```text
f′(x) = x^2 − 20x + 300
f′ = 0 → discriminant = 20^2 − 4(1)(300)
                      = 400 − 1200 = −800 < 0
No real roots. Also f′(x) = (x − 10)^2 + 200 > 0
for every x, so f is always increasing:
it has no maximum and no minimum.
```

Learn this trap: when f′(x) = 0 has no real roots, say clearly "no stationary point, so no maximum or minimum".

### Example 4: a word problem

Of all rectangles with perimeter 40 cm, which has the largest area?

```text
Sides x and (20 − x).  A = x(20 − x) = 20x − x^2
dA/dx = 20 − 2x = 0 → x = 10
d²A/dx² = −2 < 0 → maximum
Sides 10 cm and 10 cm (a square), area 100 cm^2.
```

## 3.6 Applications in pharmacy

**1. Rate of elimination.** For first-order elimination C = C0 e^(−kt):

```text
dC/dt = −k C0 e^(−kt) = −kC
The rate of fall is proportional to the
concentration present (first-order process).
```

**2. Time of peak plasma concentration (tmax) after an oral dose.** In a one-compartment model with first-order absorption, C = A(e^(−kt) − e^(−ka·t)), where ka is the absorption rate constant and k the elimination rate constant.

```text
dC/dt = A(−k e^(−kt) + ka e^(−ka·t)) = 0
ka e^(−ka·t) = k e^(−kt)
ka/k = e^((ka − k)t)
tmax = ln(ka/k) / (ka − k)

Example: ka = 1.0 per h, k = 0.2 per h
tmax = ln 5 / 0.8 = 1.609/0.8 = 2.01 h
```

**3. Rates of reaction.** In kinetics, the rate of a reaction is −d[A]/dt; the order of reaction describes how this derivative depends on concentration (zero, first or second order).

**4. Other uses:** sensitivity of a response to a small change in dose; finding the best (optimum) value of a formulation or process variable, such as the concentration that gives the highest response.

## Remember

- dy/dx = lim (h → 0) [f(x + h) − f(x)]/h = slope of the tangent.
- d/dx x^n = n x^(n − 1); e^x → e^x; a^x → a^x ln a; ln x → 1/x.
- sin → cos; cos → −sin; tan → sec^2; cot → −cosec^2; sec → sec tan; cosec → −cosec cot.
- Product: uv′ + vu′; quotient: (vu′ − uv′)/v^2; chain: multiply by the derivative of the inside.
- Maximum: f′ = 0, f″ < 0; minimum: f′ = 0, f″ > 0. If f′ = 0 has no real roots, there is no max or min.
- First-order elimination: dC/dt = −kC; tmax = ln(ka/k)/(ka − k).
