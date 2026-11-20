# Unit 2: Control structures and functions

So far every line of a program ran once, from top to bottom. Real programs must **decide** (is this result within limits?), **repeat** (do the same calculation for 50 samples) and be **organised** into reusable pieces. Decisions use conditional statements, repetition uses loops, and organisation uses functions. Together they are called **control structures** because they control the order in which statements run (the **flow of control**).

```text
 Sequence            Selection (decision)          Iteration (loop)
 --------            --------------------          ----------------
 statement 1              condition?                  +--> condition? --no--> exit
 statement 2             /         \                  |        | yes
 statement 3          True        False               |     body of loop
                      block A     block B             +--------+
```

## 2.1 Conditional statements

A conditional statement runs a block of code only if a condition is `True`. The condition is any expression that gives `True` or `False`, usually built with comparison (`<`, `>=`, `==`) and logical (`and`, `or`, `not`) operators.

**Syntax rules** (asked often):

- The line with `if`, `elif` or `else` ends with a **colon** `:`.
- The block under it is **indented** (4 spaces by convention). All lines of a block must have the same indentation.
- The block ends when the indentation returns to the earlier level.

### 2.1.1 if statement

Runs the block only when the condition is true; otherwise skips it.

```python
ph = 5.8
if ph < 7:
    print("Acidic solution")
print("Check finished")
```

Output:

```text
Acidic solution
Check finished
```

The last line is not indented, so it runs in every case.

### 2.1.2 if-else statement

Chooses between two blocks: one for `True`, one for `False`.

```python
assay_percent = 93.5
if assay_percent >= 95 and assay_percent <= 105:
    print("Assay within limits")
else:
    print("Assay out of limits - investigate")
```

Output:

```text
Assay out of limits - investigate
```

(The 95–105% limit here is only a practice value; each monograph states its own.) Python also allows the shorter chained form `95 <= assay_percent <= 105`.

### 2.1.3 if-elif-else ladder

Tests several conditions in order. **Only the first true block runs**; the rest are skipped. `else` at the end catches everything not matched. `elif` means "else if".

Adult BMI classes commonly used (WHO): below 18.5 underweight, 18.5–24.9 normal, 25–29.9 overweight, 30 or more obese.

```python
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

for value in [17.2, 22.0, 27.5, 31.4]:
    print(value, bmi_category(value))
```

Output:

```text
17.2 Underweight
22.0 Normal
27.5 Overweight
31.4 Obese
```

Because the tests run in order, `elif bmi < 25` does not need `bmi >= 18.5` — that case was already caught above. Order the conditions carefully.

### 2.1.4 Nested conditions

An `if` placed inside another `if` (or `else`). Useful when the second question depends on the answer to the first.

Example — uniformity of weight of uncoated tablets as in the Indian Pharmacopoeia: the allowed deviation from the average weight depends on that average (80 mg or less: 10%; more than 80 mg and less than 250 mg: 7.5%; 250 mg or more: 5%).

```python
avg_weight_mg = 300
deviation_percent = 6.2

if avg_weight_mg <= 80:
    limit = 10
else:
    if avg_weight_mg < 250:
        limit = 7.5
    else:
        limit = 5

print("Allowed deviation:", limit, "%")
if deviation_percent > limit:
    print("Tablet outside limit")
else:
    print("Tablet within limit")
```

Output:

```text
Allowed deviation: 5 %
Tablet outside limit
```

Deep nesting is hard to read; an `if-elif-else` ladder or `and` often does the same job more clearly.

| Form | When to use |
| --- | --- |
| `if` | Do something only in one case |
| `if-else` | Exactly two possible paths |
| `if-elif-else` | Three or more mutually exclusive cases (grades, categories, ranges) |
| Nested `if` | A second decision that only makes sense after the first |

## 2.2 Loops

A **loop** repeats a block of code. Each repetition is called an **iteration**.

### 2.2.1 for loop

Repeats once for **each item in a sequence** (list, string, tuple, range, rows of a file). Use it when you know what you are looping over.

```text
for variable in sequence:
    block            <- runs once per item; variable holds the current item
```

**range()** produces a sequence of whole numbers:

| Call | Numbers produced |
| --- | --- |
| `range(5)` | 0, 1, 2, 3, 4 (stop value excluded) |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 (start, stop, step) |
| `range(10, 0, -3)` | 10, 7, 4, 1 (counting down) |

```python
for i in range(5):
    print(i, end=" ")
print()
print(list(range(2, 11, 2)))
print(list(range(10, 0, -3)))
```

Output:

```text
0 1 2 3 4
[2, 4, 6, 8, 10]
[10, 7, 4, 1]
```

(`end=" "` keeps the numbers on one line; the empty `print()` then moves to a new line.)

**Looping over data — mean of absorbance readings**

```python
absorbances = [0.105, 0.212, 0.318, 0.421, 0.530]
total = 0
for a in absorbances:
    total = total + a
print("Number of readings:", len(absorbances))
print("Mean absorbance:", round(total / len(absorbances), 3))
```

Output:

```text
Number of readings: 5
Mean absorbance: 0.317
```

Here `total` is an **accumulator**: it starts at 0 and grows inside the loop.

**Building a dilution table**

```python
stock_conc = 100      # ug/mL
for dilution_factor in [2, 5, 10, 20]:
    print(f"1 in {dilution_factor:>2} dilution -> {stock_conc / dilution_factor:6.1f} ug/mL")
```

Output:

```text
1 in  2 dilution ->   50.0 ug/mL
1 in  5 dilution ->   20.0 ug/mL
1 in 10 dilution ->   10.0 ug/mL
1 in 20 dilution ->    5.0 ug/mL
```

### 2.2.2 while loop

Repeats **as long as a condition stays true**. Use it when you do not know in advance how many repetitions are needed.

Example — how many half-lives until a concentration falls below 10% of the start? (Each half-life halves the amount.)

```python
conc = 100.0        # starting concentration (any unit)
half_lives = 0
while conc >= 10:
    conc = conc / 2
    half_lives += 1
print("Half-lives needed:", half_lives)
print("Concentration left:", conc)
```

Output:

```text
Half-lives needed: 4
Concentration left: 6.25
```

Trace: 100 → 50 → 25 → 12.5 → 6.25; after the fourth halving the condition `conc >= 10` is false and the loop stops.

**Infinite loop warning**: if nothing inside the loop changes the condition (for example you forget `conc = conc / 2`), it never ends. Stop it with Ctrl + C, or the stop (■) button in Jupyter.

| for loop | while loop |
| --- | --- |
| Runs over a known sequence | Runs while a condition is true |
| Number of iterations known in advance | Number of iterations not known in advance |
| Loop variable updated automatically | You must update the variable yourself |
| Rarely becomes infinite | Becomes infinite if the condition never turns false |
| Example: every sample in a list | Example: titrate until end point, halve until below a limit |

### 2.2.3 Nested loops

A loop inside a loop: the inner loop runs completely for each turn of the outer loop.

```python
for strip in range(1, 4):
    for tablet in range(1, 3):
        print(f"strip {strip} tablet {tablet}")
```

Output:

```text
strip 1 tablet 1
strip 1 tablet 2
strip 2 tablet 1
strip 2 tablet 2
strip 3 tablet 1
strip 3 tablet 2
```

Total iterations = 3 × 2 = 6.

## 2.3 break and continue

| Statement | Effect | Typical use |
| --- | --- | --- |
| `break` | Leaves the loop **at once**; remaining items are not processed | Stop searching once the first failing sample is found |
| `continue` | Skips the **rest of the current iteration** and goes to the next one | Skip missing or impossible readings |
| `pass` | Does nothing; a placeholder where a statement is required | Empty block you will write later |

**break** — find the first result above 105%:

```python
results = [99.1, 101.4, 96.8, 108.2, 100.3]
for position, value in enumerate(results, start=1):
    if value > 105:
        print("First out-of-limit result at sample", position, ":", value)
        break
else:
    print("All samples within limit")
```

Output:

```text
First out-of-limit result at sample 4 : 108.2
```

Notes: `enumerate()` gives the position and the value together. The `else` attached to a `for` loop runs only if the loop finished **without** a `break` — here it does not run, because sample 4 triggered the break and sample 5 was never checked.

**continue** — skip missing (`None`) and impossible (negative) absorbance values:

```python
readings = [0.42, None, 0.45, -1, 0.44]
valid = []
for r in readings:
    if r is None or r < 0:
        continue          # skip missing or impossible values
    valid.append(r)
print(valid)
```

Output:

```text
[0.42, 0.45, 0.44]
```

## 2.4 Functions

A **function** is a named, reusable block of code that does one task. You have already used built-in functions: `print()`, `len()`, `type()`, `round()`, `sum()`, `max()`, `input()`. Now you write your own (**user-defined functions**).

**Why use functions**

- **Reuse** — write once, call many times (for every patient, every sample).
- **Modularity** — a big problem is broken into small, separate parts.
- **Readability** — `bmi(70, 1.75)` says what it does.
- **Easier testing and correction** — fix an error in one place.

### 2.4.1 Defining and calling a function

```text
def function_name(parameter1, parameter2):     <- header: def, name, (parameters), colon
    """Docstring: what the function does."""   <- optional description
    statements                                 <- indented body
    return result                              <- value sent back to the caller

answer = function_name(argument1, argument2)  <- call
```

- **Parameters** — names in the function definition.
- **Arguments** — actual values passed when calling.
- A function does nothing until it is **called**.
- **return** sends a value back and ends the function. A function without `return` gives back `None`.
- **print vs return**: `print` only shows a value on screen; `return` hands it back so it can be stored and used in further calculations.

```python
def greet(name):
    """Print a greeting for the given name."""
    print("Hello,", name)

greet("Pharmacy student")

def concentration(amount_mg, volume_ml):
    return amount_mg / volume_ml

c = concentration(50, 25)
print("Concentration:", c, "mg/mL")
```

Output:

```text
Hello, Pharmacy student
Concentration: 2.0 mg/mL
```

### 2.4.2 Passing arguments

| Kind | How | Example |
| --- | --- | --- |
| Positional | Matched to parameters by order | `amount_needed(2, 50)` |
| Keyword | Matched by name; order does not matter | `amount_needed(volume=50, conc=2)` |
| Default | Parameter has a value used when no argument is given | `def f(conc, volume, unit="mg")` |

```python
def amount_needed(conc, volume, unit="mg"):
    return f"{conc * volume} {unit}"

print(amount_needed(2, 50))                   # positional arguments
print(amount_needed(volume=50, conc=2))       # keyword arguments
print(amount_needed(2, 50, unit="g"))         # overriding the default
```

Output:

```text
100 mg
100 mg
100 g
```

Parameters with defaults must come after those without defaults.

### 2.4.3 Returning values (including several at once)

A function can return several values separated by commas; they come back as a tuple and can be **unpacked** into separate variables.

```python
def stats(values):
    n = len(values)
    mean = sum(values) / n
    return min(values), max(values), round(mean, 2)

low, high, avg = stats([250, 248, 253, 251, 249])
print(low, high, avg)
```

Output:

```text
248 253 250.2
```

### 2.4.4 Scope of variables

- **Local variable** — created inside a function; exists only while the function runs.
- **Global variable** — created outside all functions; can be read inside functions.

```python
factor = 1000           # global variable

def mg_to_ug(mg):
    result = mg * factor    # 'result' is local to this function
    return result

print(mg_to_ug(0.5))
# print(result) here would give NameError: result exists only inside the function
```

Output:

```text
500.0
```

Good practice: pass what a function needs as parameters and get results through `return`, rather than relying on global variables.

### 2.4.5 Lambda (one-line) functions

`square = lambda x: x ** 2` makes a tiny unnamed function; `square(4)` gives 16. Used mainly as a quick argument to other functions, for example as a sort key.

## 2.5 Writing modular programs for pharmaceutical applications

A **modular program** is built from small functions, each doing one job, plus a short main part that calls them. Below is a calculator for common patient and dosage arithmetic. The formulas are the standard textbook ones:

| Calculation | Formula |
| --- | --- |
| BMI (kg/m²) | weight (kg) ÷ height (m)² |
| Body surface area, Mosteller (m²) | √[height (cm) × weight (kg) ÷ 3600] |
| Weight-based dose | dose per kg × body weight (kg) |
| Clark's rule (child) | (weight in kg ÷ 70) × adult dose |
| Young's rule (child, 1–12 years) | age ÷ (age + 12) × adult dose |
| Volume to measure | required amount ÷ concentration |

**Important**: the numbers in the program are made-up practice values to show the arithmetic. They are not doses of any real medicine. In practice doses come only from official references and a prescriber; age- and weight-based rules are approximations.

```python
import math

def bmi(weight_kg, height_m):
    """Body mass index in kg/m2."""
    return weight_kg / height_m ** 2

def bmi_category(value):
    if value < 18.5:
        return "Underweight"
    elif value < 25:
        return "Normal"
    elif value < 30:
        return "Overweight"
    return "Obese"

def bsa_mosteller(weight_kg, height_cm):
    """Body surface area in m2: square root of (height x weight / 3600)."""
    return math.sqrt(height_cm * weight_kg / 3600)

def weight_based_dose(dose_per_kg, weight_kg):
    """Dose = dose per kg x body weight (same mass unit as dose_per_kg)."""
    return dose_per_kg * weight_kg

def clark_rule(adult_dose, child_weight_kg):
    """Child dose = (weight in kg / 70) x adult dose."""
    return child_weight_kg / 70 * adult_dose

def young_rule(adult_dose, age_years):
    """Child dose = age / (age + 12) x adult dose."""
    return age_years / (age_years + 12) * adult_dose

def volume_to_give(dose_mg, conc_mg_per_ml):
    return dose_mg / conc_mg_per_ml

# --- main program (all numbers are made-up practice values, not real doses) ---
w, h = 70, 1.75
b = bmi(w, h)
print(f"BMI: {b:.1f} ({bmi_category(b)})")
print(f"BSA: {bsa_mosteller(w, 175):.2f} m2")
print("Weight-based dose:", weight_based_dose(2, 20), "units")
print("Clark's rule:", clark_rule(100, 14), "units")
print("Young's rule:", round(young_rule(100, 6), 1), "units")
print("Volume to measure:", volume_to_give(40, 8), "mL")
```

Output:

```text
BMI: 22.9 (Normal)
BSA: 1.84 m2
Weight-based dose: 40 units
Clark's rule: 20.0 units
Young's rule: 33.3 units
Volume to measure: 5.0 mL
```

How to explain this program in an exam answer:

1. Each formula is a separate function with a docstring (modularity).
2. Functions take inputs as parameters and `return` the result (reusable for any patient).
3. A decision function (`bmi_category`) uses an if-elif ladder.
4. The main part only calls functions and prints formatted output.
5. Improvements: read values with `input()`, check that weight and height are positive (`if weight_kg <= 0: ...`), loop over a list of patients, save results to a file.

**Checking input (validation)** — a good program refuses impossible values:

```python
def bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        return None          # or raise ValueError("values must be positive")
    return weight_kg / height_m ** 2

print(round(bmi(70, 1.75), 1), bmi(-5, 1.6))
```

Output:

```text
22.9 None
```

**Handling errors with try/except** — code that may fail goes under `try`; what to do on failure goes under `except`. Here two typed entries are tested (with `input()` the typed text would arrive the same way, as a string):

```python
for typed in ["62.5", "sixty"]:
    try:
        weight = float(typed)
        print("Weight accepted:", weight)
    except ValueError:
        print("Please type a number, not", typed)
```

Output:

```text
Weight accepted: 62.5
Please type a number, not sixty
```

## 2.6 Algorithms and flowcharts (quick note)

An **algorithm** is a step-by-step method to solve a problem; a **flowchart** draws it with standard symbols: oval (start/stop), parallelogram (input/output), rectangle (process), diamond (decision). Writing the algorithm first, then the code, avoids logic errors.

```text
          ( Start )
              |
     / Input weight, height /
              |
     [ BMI = weight / height^2 ]
              |
        < BMI < 18.5 ? > --yes--> / Print "Underweight" /
              | no
        < BMI < 25 ?  > --yes--> / Print "Normal" /
              | no
             ...
              |
          ( Stop )
```

## Remember

- Control structures: sequence, selection (`if`) and iteration (loops).
- `if`, `elif`, `else`, `for`, `while`, `def` lines end with a colon; their blocks are indented.
- In an if-elif-else ladder only the first true block runs.
- `for` loops over a sequence (`range(start, stop, step)`, stop excluded); `while` repeats while a condition is true and can become infinite.
- `break` leaves the loop; `continue` skips to the next iteration; `pass` does nothing.
- A loop's `else` block runs only when the loop ends without `break`.
- Functions: `def name(parameters):`, called with arguments, `return` sends back a value (default `None`).
- Arguments can be positional, keyword or default; several values can be returned and unpacked.
- Local variables live only inside their function.
- Modular programs = small single-purpose functions + a short main part (BMI, BSA, Clark's and Young's rules, volume to measure).
