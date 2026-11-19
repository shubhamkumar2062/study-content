# Unit 1: Partial fractions, logarithms, functions, limits and continuity

This unit gives you the basic tools that the rest of the course keeps using. Partial fractions come back in integration and in the Laplace transform; logarithms are needed for pH, half-life and every first-order equation; limits are the starting point of differentiation. Work every example with a pen as you read.

**How maths is written in these notes:** x^2 means "x squared", x^3 "x cubed", √x "square root of x", log x is the common log (base 10), ln x is the natural log (base e), and a/b means a divided by b. Brackets show what is on top and what is below: (3x + 5)/((x + 2)(x − 1)).

## 1.1 Polynomials and rational fractions

A **polynomial** in x is a sum of terms of the form a·x^n, where n is 0 or a positive whole number.

| Example | Degree (highest power) | Name |
| --- | --- | --- |
| 7 | 0 | Constant |
| 3x − 2 | 1 | Linear |
| x^2 − 5x + 6 | 2 | Quadratic |
| 2x^3 + x − 1 | 3 | Cubic |

A **rational fraction** is one polynomial divided by another, P(x)/Q(x), with Q(x) not zero.

- **Proper fraction:** degree of top < degree of bottom. Example: (2x + 3)/(x^2 + x − 2).
- **Improper fraction:** degree of top ≥ degree of bottom. Example: (x^2 + 1)/(x^2 − 3x + 2). First divide (long division) to get a polynomial plus a proper fraction.

## 1.2 Partial fractions

Adding fractions joins them: 1/(x − 1) + 1/(x + 1) = 2x/(x^2 − 1). **Resolving into partial fractions** is the reverse: breaking one fraction into simpler ones. We need it to integrate rational functions and to find inverse Laplace transforms.

**Rules for the form of the partial fractions** (fraction must be proper first):

| Factor in the denominator | Partial fraction to write |
| --- | --- |
| Linear (x − a), not repeated | A/(x − a) |
| Repeated linear (x − a)^2 | A/(x − a) + B/(x − a)^2 |
| (x − a)^3 | A/(x − a) + B/(x − a)^2 + C/(x − a)^3 |
| Quadratic that cannot be factorised (x^2 + bx + c) | (Ax + B)/(x^2 + bx + c) |

**Method:** write the form, multiply both sides by the full denominator, then (1) put x equal to the roots of the linear factors to get constants quickly, and (2) compare coefficients of equal powers of x for the rest. Always check your answer at one more value of x.

### Example 1: two different linear factors

Resolve (3x + 5)/((x + 2)(x − 1)).

```text
(3x + 5)/((x + 2)(x − 1)) = A/(x + 2) + B/(x − 1)
Multiply by (x + 2)(x − 1):
  3x + 5 = A(x − 1) + B(x + 2)
Put x = 1:   8 = 3B      → B = 8/3
Put x = −2: −1 = −3A     → A = 1/3
Answer:
  1/(3(x + 2)) + 8/(3(x − 1))
Check at x = 0:
  left  = 5/(2 × −1) = −5/2
  right = 1/6 − 8/3 = 1/6 − 16/6 = −15/6 = −5/2 ✓
```

### Example 2: a repeated factor

Resolve (3x + 1)/((x − 1)^2 (x + 2)).

```text
= A/(x − 1) + B/(x − 1)^2 + C/(x + 2)
3x + 1 = A(x − 1)(x + 2) + B(x + 2) + C(x − 1)^2
x = 1:   4 = 3B    → B = 4/3
x = −2: −5 = 9C    → C = −5/9
Compare x^2 terms: 0 = A + C → A = 5/9
Answer:
  5/(9(x − 1)) + 4/(3(x − 1)^2) − 5/(9(x + 2))
Check x = 0: left = 1/(1 × 2) = 1/2
  right = −5/9 + 4/3 − 5/18
        = −10/18 + 24/18 − 5/18 = 9/18 = 1/2 ✓
```

### Example 3: a quadratic factor

Resolve x/((x + 1)(x^2 + 1)).

```text
= A/(x + 1) + (Bx + C)/(x^2 + 1)
x = A(x^2 + 1) + (Bx + C)(x + 1)
x = −1:  −1 = 2A        → A = −1/2
x^2:      0 = A + B     → B = 1/2
constant: 0 = A + C     → C = 1/2
x terms:  1 = B + C = 1 ✓
Answer: −1/(2(x + 1)) + (x + 1)/(2(x^2 + 1))
```

### Example 4: an improper fraction

Resolve (x^2 + 1)/(x^2 − 3x + 2).

```text
Divide first: (x^2 + 1) ÷ (x^2 − 3x + 2) = 1,
  remainder (x^2 + 1) − (x^2 − 3x + 2) = 3x − 1
So = 1 + (3x − 1)/((x − 1)(x − 2))
3x − 1 = A(x − 2) + B(x − 1)
x = 1: 2 = −A → A = −2
x = 2: 5 = B
Answer: 1 − 2/(x − 1) + 5/(x − 2)
Check x = 0: left = 1/2; right = 1 + 2 − 5/2 = 1/2 ✓
```

### Application in chemical kinetics and pharmacokinetics

**Second-order reaction with unequal concentrations.** For A + B → products with starting concentrations a and b, the rate is dx/dt = k(a − x)(b − x). To integrate, split the fraction:

```text
1/((a − x)(b − x)) = [1/(b − a)] × [1/(a − x) − 1/(b − x)]
Check: 1/(a − x) − 1/(b − x)
     = (b − x − a + x)/((a − x)(b − x))
     = (b − a)/((a − x)(b − x)) ✓
Integrating (Unit 4) and using x = 0 at t = 0 gives
  kt = [1/(b − a)] ln[ a(b − x) / (b(a − x)) ]
```

**Pharmacokinetics.** After an oral dose the amount in the body comes out (Unit 5) as a constant times 1/((s + ka)(s + k)). Partial fractions split it into 1/(s + k) and 1/(s + ka), which turn into e^(−kt) and e^(−ka·t). That is how the familiar curve of absorption followed by elimination is obtained.

## 1.3 Logarithms

**Definition:** if a^x = N (a > 0, a ≠ 1), then x = log_a N. The logarithm is the power to which the base must be raised to give the number.

| Exponential form | Log form |
| --- | --- |
| 10^2 = 100 | log 100 = 2 |
| 2^5 = 32 | log_2 32 = 5 |
| 10^−3 = 0.001 | log 0.001 = −3 |
| e^0 = 1 | ln 1 = 0 |

- **Common logarithm:** base 10, written log x. Used in pH and in log tables.
- **Natural logarithm:** base e (e ≈ 2.718), written ln x. Used in calculus and kinetics.
- **Change of base:** log_a N = log_b N / log_b a. In particular ln x = 2.303 log x.
- Log of zero or a negative number is not defined.

### Laws (theorems) of logarithms

| Law | Statement |
| --- | --- |
| Product | log(mn) = log m + log n |
| Quotient | log(m/n) = log m − log n |
| Power | log(m^n) = n log m |
| Base | log_a a = 1 |
| One | log_a 1 = 0 |
| Inverse | a^(log_a N) = N |

**Proof of the product law (asked often):** let log_a m = x and log_a n = y, so m = a^x and n = a^y. Then mn = a^x · a^y = a^(x + y), so log_a(mn) = x + y = log_a m + log_a n.

### Worked examples on the laws

Given log 2 = 0.3010 and log 3 = 0.4771:

```text
log 12  = log(2^2 × 3) = 2(0.3010) + 0.4771 = 1.0791
log 1.5 = log 3 − log 2 = 0.4771 − 0.3010 = 0.1761
log 72  = log(2^3 × 3^2) = 0.9030 + 0.9542 = 1.8572
log √27 = (3/2) log 3 = 0.7157
```

**Solve:** log(x + 2) + log(x − 1) = 1.

```text
log[(x + 2)(x − 1)] = 1 → (x + 2)(x − 1) = 10
x^2 + x − 12 = 0 → (x + 4)(x − 3) = 0
x = 3 or x = −4
x = −4 makes log(x − 1) the log of a negative
number, so reject it. Answer: x = 3
```

**Solve:** log_8 x = 2/3 → x = 8^(2/3) = (8^(1/3))^2 = 2^2 = 4.

### Characteristic and mantissa

A common log has two parts: the **characteristic** (whole-number part) and the **mantissa** (decimal part, always positive, read from tables).

| Number | Characteristic rule | Example |
| --- | --- | --- |
| Greater than 1 | (number of digits before the decimal point) − 1 | 3456 → 3 |
| Between 0 and 1 | −(number of zeros just after the decimal point + 1) | 0.0345 → −2 |

The mantissa depends only on the digits, not on the decimal point: log 3.456 = 0.5386, so log 3456 = 3.5386 and log 345.6 = 2.5386.

A negative characteristic is written with a bar over it so the mantissa stays positive:

```text
log 0.0345 = 2̄.5378   (means −2 + 0.5378 = −1.4622)
log 0.000589 = 4̄.7701 (means −4 + 0.7701 = −3.2299)
```

**Antilogarithm** is the reverse: antilog 2.5386 = 345.6 (put the decimal point so that there are 3 digits before it).

### Application of logarithms to pharmaceutical problems

**pH.** pH = −log[H+].

```text
[H+] = 3.2 × 10^−4 M
pH = −(log 3.2 + log 10^−4) = −(0.5051 − 4)
   = 3.4949 ≈ 3.49

pH = 5.6 → [H+] = 10^−5.6 = 10^0.4 × 10^−6
   = 2.51 × 10^−6 M
```

**Buffer pH (Henderson–Hasselbalch).** pH = pKa + log([salt]/[acid]). Acetic acid 0.1 M with sodium acetate 0.2 M, pKa 4.76: pH = 4.76 + log 2 = 4.76 + 0.301 = 5.06.

**First-order decomposition and half-life.** k = (2.303/t) log(C0/C), t½ = 0.693/k and shelf life t90 = 0.105/k.

```text
A drug solution falls from 500 to 350 units in 40 days.
k = (2.303/40) × log(500/350)
  = (2.303/40) × 0.1549 = 0.00892 per day
t½  = 0.693/0.00892 = 77.7 days
t90 = 0.105/0.00892 = 11.8 days
```

## 1.4 Functions

A **function** f from set A to set B is a rule that gives **each** element x of A **exactly one** element f(x) of B. A is the **domain**, the set of values f(x) actually takes is the **range**. If both are sets of real numbers, f is a **real valued function** of a real variable.

**Finding the domain:**

- f(x) = 1/(x − 2): bottom cannot be zero, so domain = all real numbers except 2.
- f(x) = √(x − 3): inside the root cannot be negative, so x ≥ 3.
- f(x) = log(x + 1): needs x + 1 > 0, so x > −1.

### Classification of real valued functions

| Type | Rule | Example / note |
| --- | --- | --- |
| Constant | f(x) = c | f(x) = 5; graph is a horizontal line |
| Identity | f(x) = x | Line through origin at 45° |
| Polynomial | a0 + a1x + … + anx^n | x^2 − 5x + 6 |
| Rational | P(x)/Q(x) | (x + 1)/(x − 2) |
| Modulus | f(x) = \|x\| | x if x ≥ 0, −x if x < 0 |
| Signum | 1, 0, −1 for x > 0, = 0, < 0 | Shows the sign of x |
| Greatest integer | [x] | [2.7] = 2, [−1.2] = −2 |
| Exponential | a^x, e^x | First-order drug decline C0e^(−kt) |
| Logarithmic | log_a x | Inverse of the exponential |
| Trigonometric | sin x, cos x, tan x … | Periodic |

Other ways to classify:

- **Algebraic** (built from x by +, −, ×, ÷, roots) and **transcendental** (exponential, log, trigonometric).
- **Even:** f(−x) = f(x), e.g. x^2, cos x (graph symmetric about the y-axis). **Odd:** f(−x) = −f(x), e.g. x^3, sin x.
- **Explicit** y = f(x), and **implicit** f(x, y) = 0, e.g. x^2 + y^2 = 25.
- **One-one** (different x give different f(x)) and **onto** (every element of B is reached).

## 1.5 Limits

**Idea:** lim (x → a) f(x) = L means f(x) gets as close as we like to L when x is close enough to a (x itself need not equal a).

**ε–δ definition:** lim (x → a) f(x) = L if for every ε > 0 there is a δ > 0 such that |f(x) − L| < ε whenever 0 < |x − a| < δ.

**Example (prove with ε–δ):** lim (x → 2) (3x + 1) = 7.

```text
|f(x) − 7| = |3x + 1 − 7| = 3|x − 2|
We want 3|x − 2| < ε, i.e. |x − 2| < ε/3.
Choose δ = ε/3. Then 0 < |x − 2| < δ gives
|f(x) − 7| < 3(ε/3) = ε. Hence the limit is 7.
```

**Left and right limits:** the limit exists only if the left-hand limit (x → a−) and right-hand limit (x → a+) are equal. For f(x) = |x|/x at x = 0, LHL = −1 and RHL = +1, so the limit does not exist.

**Limit laws:** the limit of a sum, difference, product or quotient (bottom limit not zero) is the sum, difference, product or quotient of the limits.

### Two standard limits from the syllabus

```text
1)  lim (x → a) (x^n − a^n)/(x − a) = n·a^(n − 1)
2)  lim (θ → 0) sin θ / θ = 1   (θ in radians)
```

Consequences: lim (x → 0) tan x / x = 1 and lim (x → 0) (1 − cos x)/x^2 = 1/2.

### Worked examples

```text
(a) lim (x → 2) (x^2 − 4)/(x − 2)
    = lim (x + 2)(x − 2)/(x − 2) = 2 + 2 = 4

(b) lim (x → 3) (x^4 − 81)/(x − 3)
    = 4 × 3^3 = 108      (formula 1 with n = 4, a = 3)

(c) lim (x → a) (x^5 − a^5)/(x^3 − a^3)
    divide top and bottom by (x − a):
    = (5a^4)/(3a^2) = (5/3)a^2

(d) lim (x → 0) sin 5x / x
    = 5 × lim sin 5x / 5x = 5 × 1 = 5

(e) lim (x → 0) sin 3x / sin 2x
    = (3x/2x) × 1 = 3/2

(f) lim (x → 0) (1 − cos x)/x^2
    1 − cos x = 2 sin^2(x/2)
    = 2 sin^2(x/2)/x^2 = (1/2)[sin(x/2)/(x/2)]^2
    → 1/2

(g) lim (x → 0) (√(1 + x) − 1)/x
    multiply top and bottom by (√(1 + x) + 1):
    = x / [x(√(1 + x) + 1)] = 1/(1 + 1) = 1/2

(h) lim (x → ∞) (3x^2 + 2x)/(5x^2 − 1)
    divide by x^2: (3 + 2/x)/(5 − 1/x^2) → 3/5

(i) lim (x → 2) (x^3 − 9)/(x − 3)
    bottom is not zero at x = 2, so substitute:
    (8 − 9)/(2 − 3) = 1
```

Tip (i): always try direct substitution first. Only when you get 0/0 do you factorise, rationalise or use a standard limit.

## 1.6 Continuity

A function f is **continuous at x = a** if three things hold:

1. f(a) is defined.
2. lim (x → a) f(x) exists (LHL = RHL).
3. lim (x → a) f(x) = f(a).

If any one fails, f is **discontinuous** at a. Polynomials, e^x, sin x and cos x are continuous everywhere; a rational function is continuous except where its bottom is zero.

**Example:** f(x) = (x^2 − 1)/(x − 1) for x ≠ 1, and f(1) = 2.

```text
lim (x → 1) (x − 1)(x + 1)/(x − 1) = 2 = f(1)
→ continuous at x = 1.
If instead f(1) = 3, the limit (2) ≠ f(1),
→ discontinuous at x = 1.
```

**Example:** find k so that f(x) = kx + 1 (x ≤ 2) and 3x − 1 (x > 2) is continuous at x = 2.

```text
LHL = f(2) = 2k + 1; RHL = 3(2) − 1 = 5
2k + 1 = 5 → k = 2
```

## Remember

- Make the fraction proper before splitting; use A/(x − a) for linear, add B/(x − a)^2 for a repeated factor, (Ax + B)/(quadratic) for a quadratic factor.
- Find constants by putting x = roots, then compare coefficients; always check at x = 0.
- log(mn) = log m + log n, log(m/n) = log m − log n, log m^n = n log m; ln x = 2.303 log x.
- Characteristic: digits before decimal − 1 (number > 1); −(zeros after decimal + 1) for 0 < number < 1; mantissa is always positive.
- pH = −log[H+]; t½ = 0.693/k; k = (2.303/t) log(C0/C).
- A function gives each x exactly one value; check domain for division by zero, roots of negatives and logs.
- lim (x^n − a^n)/(x − a) = n·a^(n − 1); lim sin θ/θ = 1 (θ in radians).
- Continuous at a: f(a) defined, LHL = RHL, and limit = f(a).
