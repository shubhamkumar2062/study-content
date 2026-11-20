# Last-night revision sheet

If you only have an hour, be able to write from memory: **an if-elif-else program (BMI category)**, **a for loop and a while loop with break/continue**, **a function with arguments and return (dosage or BMI)**, **list vs tuple vs dictionary with methods**, **reading a CSV with Pandas and cleaning missing values**, **groupby**, and **a labelled Matplotlib plot (line, histogram, scatter, box)** with its interpretation.

**Unit 1 — basics**

| Item | Key fact |
| --- | --- |
| Python | High-level, interpreted, dynamically typed, free, indentation-based; use Python 3 |
| IDEs | Jupyter (cells, `.ipynb`), PyCharm, VS Code, Spyder, IDLE; give highlighting, auto-complete, error marks, run button, debugger |
| Data types | `int`, `float`, `str`, `bool`; `type(x)` |
| Casting | `int("25")`, `float("2.5")`, `str(5)`; `int(3.99)` = 3 (truncates); `bool(0)` = False |
| Operators | `/` 3.4, `//` 3, `%` 2, `**` power (for 17 and 5); `==` compare, `=` assign; `and`, `or`, `not` |
| Precedence | `()` → `**` → `* / // %` → `+ -` |
| I/O | `input()` returns a **string**; `print(a, b, sep=" ", end="\n")`; `f"{x:.2f}"` |
| Strings | index from 0, `s[-1]` last, `s[a:b]` excludes b, immutable; `upper lower strip replace split join find count len in` |
| Libraries | standard (math, statistics, csv, random, datetime) vs third-party (numpy, pandas, matplotlib); `pip install x`, `pip uninstall x`, `pip list`, `pip show x` |

**Unit 2 — control and functions**

| Item | Key fact |
| --- | --- |
| if / if-else / if-elif-else | colon + indented block; only the first true branch runs |
| for | over a sequence; `range(start, stop, step)`, stop excluded |
| while | while condition true; update the variable or it becomes infinite |
| break / continue / pass | leave loop / skip to next iteration / do nothing |
| loop `else` | runs only if no `break` |
| Function | `def f(a, b=2): return a * b`; positional, keyword, default arguments; returns `None` if no return |
| Scope | local (inside function) vs global |
| Formulas | BMI = kg/m²; BSA (Mosteller) = √(cm × kg / 3600); Clark: kg/70 × adult dose; Young: age/(age + 12) × adult dose |

**Unit 3 — data structures and files**

| Structure | Syntax | Mutable | Key methods |
| --- | --- | --- | --- |
| List | `[1, 2]` | Yes | append, insert, remove, pop, sort, reverse, index, count |
| Tuple | `(1, 2)` | No | count, index; unpacking `a, b = t` |
| Dictionary | `{"k": v}` | Yes | `d[k]`, get, keys, values, items, update, del |
| NumPy array | `np.array([..])` | Yes | one dtype, vectorised; `arange`, `linspace`, `zeros`, `reshape`, `mean`, `std`, `a[a > 5]` |

- `[1, 2] * 2` → `[1, 2, 1, 2]`; `np.array([1, 2]) * 2` → `[2 4]`.
- Files: `with open("f.csv", "r"/"w"/"a", newline="") as f:`; `w` overwrites, `a` appends.
- csv module: `csv.reader` (rows as lists), `csv.DictReader` (rows as dicts), `csv.writer.writerows`; values read back are strings.
- Structured data: rows = records, columns = variables, IDs, units in column names, de-identified.

**Unit 4 — Pandas**

| Task | Code |
| --- | --- |
| Load | `pd.read_csv("f.csv")`, `pd.read_excel("f.xlsx")` (openpyxl) |
| Look | `head()`, `tail()`, `info()` (non-null count, dtypes), `describe()` (count, mean, std, min, 25%, 50%, 75%, max), `shape` |
| Missing | `isna().sum()`, `dropna()`, `dropna(subset=[..])`, `fillna(value / median)` |
| Clean | `drop_duplicates()`, `str.strip().str.title()`, `astype()`, `rename()`, `map()` |
| Select | `df["c"]`, `df[["a", "b"]]`, `loc` (labels), `iloc` (positions) |
| Filter | `df[(df["a"] > 5) & (df["b"] == "X")]`, `isin([..])` — brackets around each condition |
| Group | `df.groupby("drug")["x"].agg(["mean", "count"])`, `value_counts()` |
| Save | `to_csv("out.csv", index=False)` |

PK terms: Cmax = highest concentration, Tmax = its time, AUC by trapezoidal rule = Σ (C1 + C2)/2 × (t2 − t1).

**Unit 5 — Matplotlib**

| Plot | Function | Use |
| --- | --- | --- |
| Line | `plt.plot(x, y, "o-", label=..)` | Time courses: conc–time, dissolution |
| Histogram | `plt.hist(data, bins=8)` | Distribution of one variable (tablet weights) |
| Scatter | `plt.scatter(x, y)` + `np.polyfit(x, y, 1)` | Relationship; calibration curve y = mx + c, r² |
| Box | `plt.boxplot([a, b, c])` | Median, Q1, Q3, IQR, whiskers, outliers; compare batches |
| Bar | `plt.bar(cats, values)` | Compare categories: ADR reporting rate per drug |

- Labels: `xlabel`, `ylabel` (with units), `title`, `legend`, `grid`, `xlim/ylim`, `yscale("log")`; save with `savefig("f.png", dpi=300)`; `plt.subplots(1, 2)` for side-by-side plots.
- IV bolus: highest at t = 0, falls exponentially (straight line on semi-log). Oral: rises to Cmax at Tmax, then falls.
- Dissolution profile: % released vs time; f2 = 50 log10{100/√[1 + (1/n)Σ(R − T)²]}; 50–100 = similar.
- Interpret: axes and units → pattern → key values → comparison → outliers → scientific meaning → limitations.
