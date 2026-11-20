# Unit 1: Introduction to Python programming

Pharmacy produces a lot of numbers: absorbance readings, tablet weights, plasma concentrations, stability results, adverse drug reaction (ADR) reports. Python is a free programming language that lets you calculate, sort, clean and plot such data in a few lines. This unit covers setting up Python, the basic building blocks (variables, data types, operators, input and output), working with text, and adding extra libraries.

## 1.1 What Python is and why pharmacy students learn it

**Program** — a set of instructions that a computer follows step by step.
**Programming language** — a set of words and rules used to write those instructions.

Python (created by Guido van Rossum, first released in 1991) is a **high-level, interpreted, general-purpose** language.

| Feature | What it means for you |
| --- | --- |
| High-level | Reads almost like English (`print`, `if`, `for`, `import`); you do not manage memory yourself |
| Interpreted | Code runs line by line through the Python interpreter; no separate compile step, so errors show straight away |
| Dynamically typed | You do not declare a type; Python decides the type from the value |
| Free and open source | No licence fee; runs on Windows, macOS and Linux |
| Huge library collection | NumPy, Pandas, Matplotlib, SciPy and thousands more for science and data |
| Indentation-based | Blocks of code are marked by spaces, not brackets, which keeps code neat |

**Uses in pharmaceutical sciences**

- Calculations: unit conversions, dilutions, BMI, body surface area, pharmacokinetic parameters.
- Laboratory data: calibration curves, assay results, dissolution profiles, stability data.
- Clinical and pharmacovigilance data: sorting and summarising ADR reports, patient records.
- Automation: reading hundreds of instrument files, making reports and graphs in one go.
- Research: statistics, cheminformatics and machine learning (later semesters).

## 1.2 Installing Python and an IDE

### Installing Python

1. **From python.org** — download the latest Python 3 installer for your operating system. On Windows, tick **"Add python.exe to PATH"** on the first screen so that the `python` command works in the Command Prompt.
2. **Through Anaconda (or Miniconda)** — a distribution that installs Python together with Jupyter Notebook, NumPy, Pandas, Matplotlib and the `conda` package manager. Convenient for students because the scientific libraries come ready.
3. Check the installation in a terminal / Command Prompt:

```text
python --version          (Windows)
python3 --version         (macOS / Linux)
Python 3.x.y              <- a version number means Python is installed
```

Always use **Python 3**. Python 2 reached end of life in 2020 and its code differs (for example, `print` was a statement there).

### Two ways to run Python

| Mode | How | Good for |
| --- | --- | --- |
| Interactive (shell / REPL) | Type `python`, see the `>>>` prompt, type one line, get the answer at once | Quick checks and small calculations |
| Script mode | Write many lines in a file ending in `.py`, then run `python file.py` | Real programs you want to save and run again |

REPL = Read–Evaluate–Print Loop.

```python
print("Welcome to pharmaceutical computing")
print(2 + 3)
```

Output:

```text
Welcome to pharmaceutical computing
5
```

### Integrated Development Environment (IDE)

An **IDE** is one application that combines a code editor, a way to run code, error messages, a debugger and file management.

| IDE / tool | Key points |
| --- | --- |
| **Jupyter Notebook / JupyterLab** | Runs in a web browser; code is written in **cells** that run one at a time; output, tables and graphs appear just below each cell; text notes (Markdown) can sit between cells. Ideal for data analysis and lab-style reports. Files end in `.ipynb` |
| **PyCharm** (JetBrains) | Full IDE for larger projects; smart code completion, error underlining, refactoring, built-in debugger; free Community edition |
| **VS Code** (Microsoft) | Light, free editor that becomes a Python IDE with the Python extension; can also open Jupyter notebooks |
| Spyder | Comes with Anaconda; MATLAB-like layout with a variable explorer, popular with scientists |
| IDLE | Very simple editor that installs with Python from python.org |
| Google Colab | Jupyter-style notebooks in the browser with nothing to install (needs internet and a Google account) |

### Advantages of an IDE over a plain text editor

A plain text editor (Notepad, TextEdit) only stores characters. An IDE understands Python.

| Feature | Text editor | IDE |
| --- | --- | --- |
| Syntax highlighting (keywords, strings, numbers in different colours) | No | Yes |
| Auto-completion of names and functions | No | Yes |
| Automatic indentation | No | Yes |
| Error and warning marks while typing | No | Yes |
| Run the program with one click / key | No (needs a terminal) | Yes |
| Debugger (pause, step through, watch variables) | No | Yes |
| Variable explorer, project files, terminal in one window | No | Yes |
| Install and manage packages / virtual environments | No | Often built in |

Result: fewer mistakes, faster writing, easier finding of errors (**debugging**) and better organisation.

## 1.3 Basic rules of writing Python

- **Comments** start with `#`; Python ignores them. Use them to explain your code.
- **Indentation** (usually 4 spaces) marks a block of code after `if`, `for`, `def` and so on. Wrong indentation gives an `IndentationError`.
- Python is **case-sensitive**: `Dose`, `dose` and `DOSE` are three different names.
- **Keywords** are reserved words with a fixed meaning and cannot be used as names: `if`, `else`, `elif`, `for`, `while`, `def`, `return`, `True`, `False`, `None`, `and`, `or`, `not`, `import`, `in`, `break`, `continue`, `class`.
- **Identifiers** (names of variables and functions):
  - may contain letters, digits and underscore `_`;
  - must not start with a digit (`2dose` is invalid, `dose2` is valid);
  - no spaces or symbols like `-`, `%`, `@`;
  - convention: lower case words joined by underscores, e.g. `tablet_weight_mg` (called snake_case).

## 1.4 Variables

A **variable** is a name that refers to a value stored in memory. The `=` sign is the **assignment operator**: the value on the right is stored under the name on the left.

```text
tablet_weight_mg = 250
      |          |   |
     name   assignment value
```

A variable can be given a new value later, even of a different type (dynamic typing). Several variables can be set in one line: `x, y = 3, 4`.

## 1.5 Data types

| Type | Name in Python | Examples | Pharmacy example |
| --- | --- | --- | --- |
| Integer | `int` | `10`, `-3`, `0` | Number of tablets, patient count |
| Floating-point number | `float` | `0.25`, `7.4`, `1e-7` | Weight in g, pH, absorbance |
| String (text) | `str` | `"NaCl"`, `'B-2026-014'` | Drug name, batch number |
| Boolean | `bool` | `True`, `False` | Passed test or not, batch released or not |

Other built-in types (Unit 3): `list`, `tuple`, `dict`, `set`, and `None` (means "no value").

The function `type()` tells you the type of any value:

```python
batch_no = "B-2026-014"     # string
tablets_per_strip = 10      # integer
tablet_weight_g = 0.25      # float
is_released = True          # boolean

print(type(batch_no))
print(type(tablets_per_strip))
print(type(tablet_weight_g))
print(type(is_released))
```

Output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Notes:

- Strings can use single or double quotes; triple quotes `"""..."""` allow several lines.
- `1e-7` is scientific notation for 1 × 10⁻⁷ (useful for molar concentrations).
- `True` and `False` must start with a capital letter.

## 1.6 Type casting (type conversion)

**Type casting** means changing a value from one data type to another.

- **Implicit conversion** — Python does it by itself, e.g. `3 + 2.5` gives `5.5` (int is promoted to float).
- **Explicit conversion (casting)** — you ask for it with `int()`, `float()`, `str()`, `bool()`.

```python
print(int("25"))        # string to integer
print(float("2.5"))     # string to float
print(str(500) + " mg") # number to string, then join
print(int(3.99))        # float to integer: cuts off the decimal
print(round(3.99))      # rounding is different from int()
print(float(7))
print(bool(0), bool(12), bool(""), bool("NaCl"))
```

Output:

```text
25
2.5
500 mg
3
4
7.0
False True False True
```

Points to remember:

- `int()` **truncates** (drops the decimal part); it does not round.
- `bool()` gives `False` for `0`, `0.0` and an empty string `""`; anything else is `True`.
- `int("2.5")` gives a `ValueError` because "2.5" is not a whole number; use `float("2.5")` first.
- Adding a number to a string (`500 + " mg"`) gives a `TypeError`; convert the number with `str()` first.

## 1.7 Operators

### Arithmetic operators

| Operator | Meaning | Result for a = 17, b = 5 |
| --- | --- | --- |
| `+` | Addition | 22 |
| `-` | Subtraction | 12 |
| `*` | Multiplication | 85 |
| `/` | Division (always a float) | 3.4 |
| `//` | Floor division (whole-number part) | 3 |
| `%` | Modulus (remainder) | 2 |
| `**` | Exponent (power) | `17 ** 2` = 289 |

```python
a = 17
b = 5
print(a + b, a - b, a * b)
print(a / b)    # true division always gives a float
print(a // b)   # floor division
print(a % b)    # remainder (modulus)
print(a ** 2)   # power
print(2 + 3 * 4, (2 + 3) * 4)
```

Output:

```text
22 12 85
3.4
3
2
289
14 20
```

**Order of operations (precedence)**: brackets `()` → power `**` → `*`, `/`, `//`, `%` → `+`, `-`. Use brackets whenever in doubt. A pharmacy use of `//` and `%`: 17 tablets in strips of 5 make 3 full strips (`17 // 5`) with 2 left over (`17 % 5`).

### Comparison (relational) operators

They compare two values and always give `True` or `False`: `==` equal to, `!=` not equal to, `>` greater than, `<` less than, `>=` greater than or equal to, `<=` less than or equal to.

Do not confuse `=` (store a value) with `==` (check if equal).

### Logical operators

| Operator | Result is `True` when | Example |
| --- | --- | --- |
| `and` | both conditions are true | temperature in range: `t >= 15 and t <= 25` |
| `or` | at least one is true | out of range: `t < 15 or t > 25` |
| `not` | reverses True/False | `not passed` |

```python
ph = 7.4
print(ph == 7.4, ph != 7.4)
print(ph > 7, ph <= 7)
temp_c = 30
print(temp_c >= 15 and temp_c <= 25)   # inside 15-25 degrees C?
print(temp_c < 15 or temp_c > 25)      # outside the range?
print(not True)
print(0.1 + 0.2 == 0.3)                # a floating-point surprise
print(round(0.1 + 0.2, 2) == 0.3)
```

Output:

```text
True False
True False
False
True
False
False
True
```

The last two lines show that computers store most decimals only approximately (0.1 + 0.2 is stored as 0.30000000000000004). When comparing calculated results, round them or check that the difference is very small.

### Assignment operators

`=` assigns; shortcuts update a value: `x += 2` (same as `x = x + 2`), `x -= 2`, `x *= 2`, `x /= 2`. Example: `total_tablets += 10` after counting each strip.

## 1.8 Input and output

- **`print()`** shows output. It can take several items separated by commas; by default it puts a space between them (`sep=" "`) and a new line at the end (`end="\n"`).
- **`input()`** waits for the user to type something and press Enter. **It always returns a string**, so convert it with `int()` or `float()` before doing arithmetic.

```python
weight = float(input("Enter body weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / height ** 2
print("BMI is", round(bmi, 1))
print(f"BMI = {bmi:.2f} kg/m2")
```

A run of this program (the user types 60 and 1.65):

```text
Enter body weight in kg: 60
Enter height in m: 1.65
BMI is 22.0
BMI = 22.04 kg/m2
```

### Formatting output

| Method | Example | Gives |
| --- | --- | --- |
| Joining strings | `"conc: " + str(conc)` | conc: 12.3456 |
| `format()` method | `"{:.2f}".format(conc)` | 12.35 |
| **f-string** (preferred) | `f"{conc:.2f} ug/mL"` | 12.35 ug/mL |

In `{conc:.2f}`, `.2f` means "a float with 2 decimal places". `{name:<8}` pads to 8 characters aligned left, `{x:>6}` aligns right — useful for neat tables.

```python
drug = "Drug A"
conc = 12.3456
print("Drug: " + drug + ", conc: " + str(conc))
print("Drug: {}, conc: {:.2f}".format(drug, conc))
print(f"Drug: {drug}, conc: {conc:.2f} ug/mL")
print(f"{'Sample':<8}|{'Abs':>6}")
print(f"{'S1':<8}|{0.412:>6.3f}")
```

Output:

```text
Drug: Drug A, conc: 12.3456
Drug: Drug A, conc: 12.35
Drug: Drug A, conc: 12.35 ug/mL
Sample  |   Abs
S1      | 0.412
```

### A unit-conversion example

```python
mass_mg = 250
print(mass_mg / 1000, "g")          # mg to g
print(mass_mg * 1000, "microgram")  # mg to microgram
conc_mg_per_ml = 5
volume_ml = 2.5
print("Amount in", volume_ml, "mL =", conc_mg_per_ml * volume_ml, "mg")
```

Output:

```text
0.25 g
250000 microgram
Amount in 2.5 mL = 12.5 mg
```

(1 g = 1000 mg; 1 mg = 1000 µg. Amount = concentration × volume.)

## 1.9 Strings and string operations

A **string** is an ordered sequence of characters. Each character has a position number called an **index**, starting from 0. Negative indexes count from the end (`-1` is the last character).

```text
 P   a   r   a   c   e   t   a   m   o   l
 0   1   2   3   4   5   6   7   8   9   10      (positive index)
-11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1       (negative index)
```

**Slicing** `s[start:stop]` gives the characters from `start` up to, but **not including**, `stop`. `s[:3]` = first three characters; `s[3:]` = from index 3 to the end; `s[::-1]` = reversed.

Strings are **immutable**: you cannot change one character in place; string methods return a new string.

| Operation / method | What it does |
| --- | --- |
| `+` | Join (concatenate) two strings |
| `*` | Repeat a string |
| `len(s)` | Number of characters |
| `s.upper()`, `s.lower()`, `s.title()` | Change case |
| `s.strip()` | Remove spaces (and new lines) at both ends; `lstrip`, `rstrip` for one end |
| `s.replace(old, new)` | Replace text |
| `s.split()` | Break into a list of words (or split at a given separator, e.g. `","`) |
| `" ".join(list)` | Join a list of strings with a separator |
| `s.find(x)` | Index of first occurrence (−1 if absent) |
| `s.count(x)` | Number of occurrences |
| `x in s` | `True` if `x` occurs in `s` |
| `s.startswith(x)`, `s.endswith(x)` | Check the beginning or end |
| `s.isdigit()`, `s.isalpha()` | Check the kind of characters |

```python
name = "  Paracetamol Tablets IP  "
clean = name.strip()
print(clean)
print(len(clean))
print(clean.upper())
print(clean.lower())
print(clean[0], clean[-1])
print(clean[0:11])
print(clean.replace("Tablets", "Suspension"))
print(clean.split())
print("Tablets" in clean)
print(clean.find("IP"))
print(clean.count("a"))
print("Batch " + "A" * 3)
print(clean.startswith("Para"), clean.endswith("BP"))
```

Output:

```text
Paracetamol Tablets IP
22
PARACETAMOL TABLETS IP
paracetamol tablets ip
P P
Paracetamol
Paracetamol Suspension IP
['Paracetamol', 'Tablets', 'IP']
True
20
4
Batch AAA
True False
```

Why string cleaning matters: in real data the same drug may be typed as "paracetamol", "Paracetamol " and "PARACETAMOL". Using `strip()` and `lower()` makes them identical before counting.

## 1.10 Libraries: standard and third-party

A **module** is a `.py` file of ready-made functions; a **package** is a collection of modules; a **library** is the general word for such reusable code. Using libraries saves you from writing everything yourself.

### Standard library

Comes **with Python**; nothing to install. Just `import` it.

| Module | Used for |
| --- | --- |
| `math` | `sqrt`, `log`, `log10`, `exp`, `pi` |
| `statistics` | `mean`, `median`, `stdev` |
| `random` | Random numbers, random sampling |
| `datetime` | Dates and times (expiry dates, sampling times) |
| `csv` | Reading and writing CSV files |
| `os` | Files and folders |

Ways to import: `import math` (then `math.sqrt(16)`), `from math import sqrt` (then `sqrt(16)`), `import numpy as np` (a short alias).

```python
import math
from statistics import mean, stdev

print(math.sqrt(16))
print(math.log10(1000))
print(round(math.pi, 4))
print(math.exp(0))
readings = [0.212, 0.215, 0.210, 0.214]
print(round(mean(readings), 4), round(stdev(readings), 4))
```

Output:

```text
4.0
3.0
3.1416
1.0
0.2127 0.0022
```

A small chemistry use: pH = −log10[H⁺].

```python
h = 1e-7          # hydrogen ion concentration, mol/L
import math
ph = -math.log10(h)
print("pH =", ph)
```

Output:

```text
pH = 7.0
```

### Third-party libraries

Written by others and **installed separately** from the Python Package Index (PyPI) using **pip** (the package installer). Examples: **NumPy** (fast numeric arrays), **Pandas** (tables of data), **Matplotlib** (graphs), SciPy (scientific functions), openpyxl (Excel files), scikit-learn (machine learning).

Commands are typed in the terminal / Command Prompt, not inside Python:

| Task | pip command | conda command (Anaconda) |
| --- | --- | --- |
| Install | `pip install pandas` | `conda install pandas` |
| Install a set version | `pip install pandas==2.2.2` | `conda install pandas=2.2.2` |
| Upgrade | `pip install --upgrade pandas` | `conda update pandas` |
| Uninstall | `pip uninstall pandas` | `conda remove pandas` |
| List installed | `pip list` | `conda list` |
| Details of one package | `pip show pandas` | `conda list pandas` |

In a Jupyter notebook cell you can write `%pip install pandas`. On macOS/Linux use `pip3` or `python3 -m pip` if `pip` points to an old Python. If `import pandas` gives `ModuleNotFoundError`, the library is not installed in the Python you are using.

**Virtual environment** (`python -m venv myenv`) — a separate folder with its own Python and libraries, so projects needing different versions do not clash.

## 1.11 Common errors at this stage

| Error | Typical cause |
| --- | --- |
| `SyntaxError` | Missing bracket, colon or quote |
| `IndentationError` | Wrong or mixed spaces |
| `NameError` | Using a variable before giving it a value, or a spelling/case mistake |
| `TypeError` | Mixing incompatible types, e.g. `"5" + 2` |
| `ValueError` | Right type but wrong value, e.g. `int("abc")` |
| `ZeroDivisionError` | Dividing by 0 |
| `ModuleNotFoundError` | Library not installed or misspelled |

Read the last line of the error message first: it names the error and the line number.

## Remember

- Python is high-level, interpreted, dynamically typed, free and indentation-based; use Python 3.
- Run code interactively (`>>>`) or as a `.py` script; Jupyter runs code in cells with output underneath.
- IDEs give syntax highlighting, auto-completion, error marking, one-click running and a debugger.
- Four basic data types: `int`, `float`, `str`, `bool`; check with `type()`, convert with `int()`, `float()`, `str()`, `bool()`.
- `/` gives a float, `//` the whole-number part, `%` the remainder, `**` the power.
- `=` assigns, `==` compares; `and`, `or`, `not` combine conditions.
- `input()` always returns a string; f-strings like `f"{x:.2f}"` format output.
- Strings are indexed from 0, sliced with `[start:stop]` (stop excluded) and cannot be changed in place.
- Standard library: import directly. Third-party: `pip install name`, `pip uninstall name`.
