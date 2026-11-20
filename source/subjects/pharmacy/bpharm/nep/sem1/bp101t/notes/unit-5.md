# Unit 5: Data visualization with Matplotlib

A table of 50 numbers is hard to understand; a graph of the same numbers shows the trend, the peak, the spread and any odd value at a glance. **Data visualization** means showing data as graphs so that patterns can be seen and decisions made. In pharmaceutical sciences graphs are used for plasma concentration–time curves, calibration curves, dissolution profiles, quality-control data and pharmacovigilance summaries. This unit uses **Matplotlib**, the most widely used Python plotting library.

## 5.1 Introduction to Matplotlib

- Third-party library, open source, created by John D. Hunter (first released 2003); install with `pip install matplotlib` (included in Anaconda).
- **pyplot** is its simple, MATLAB-like interface. Standard import: `import matplotlib.pyplot as plt`.
- Works with lists, NumPy arrays and Pandas columns; Pandas' own `df.plot()` uses Matplotlib underneath. Seaborn is another library built on top of Matplotlib for statistical graphics.
- Graphs can be shown on screen (`plt.show()`; in Jupyter they appear below the cell) or saved as image files (`plt.savefig("name.png", dpi=300)`) — PNG for reports and slides, PDF or SVG for sharp printing.

### Parts of a Matplotlib figure

```text
 +---------------------------------------- Figure (the whole window/page) ----+
 |                     Title  (ax.set_title / plt.title)                       |
 |   +---------------------------------- Axes (one plot area) --------------+ |
 |   |  y-tick labels                                    +--------------+   | |
 | y |  10 -|          *                                 | --- Oral     |   | |
 |   |      |       *     *          <- line / markers   | ... IV       |   | |
 | l |   5 -|    *           *                           +-- Legend ----+   | |
 | a |      |  *                 *     grid lines (optional)                 | |
 | b |   0 -+----+----+----+----+----                                       | |
 | e |      0    2    4    6    8    <- x-ticks                              | |
 | l |               x-axis label (plt.xlabel)                              | |
 |   +----------------------------------------------------------------------+ |
 +-----------------------------------------------------------------------------+
```

**Figure** = the whole picture; **Axes** = one plotting area inside it (a figure can hold several); **axis** = the x or y number line; **ticks**, **labels**, **title**, **legend** and **grid** describe the plot.

### Two ways of writing plots

| pyplot (state-based) style | Object-oriented style |
| --- | --- |
| `plt.plot(x, y)`, `plt.xlabel(...)`, `plt.title(...)` | `fig, ax = plt.subplots()`, then `ax.plot(x, y)`, `ax.set_xlabel(...)`, `ax.set_title(...)` |
| Quick and short for one plot | Clearer when a figure has several plots (subplots) |

## 5.2 The basic steps of any plot

```text
1. import matplotlib.pyplot as plt  (and numpy / pandas for data)
2. prepare x and y data
3. make the plot          plt.plot / plt.hist / plt.scatter / plt.boxplot / plt.bar
4. label it               plt.xlabel, plt.ylabel, plt.title, plt.legend, plt.grid
5. show or save it        plt.savefig("file.png", dpi=300) and/or plt.show()
```

## 5.3 Labelling axes, titles and legends

| Function | Purpose |
| --- | --- |
| `plt.xlabel("Time (h)")`, `plt.ylabel("Concentration (µg/mL)")` | Axis labels — always include **units** |
| `plt.title("...")` | Title of the plot |
| `plt.plot(x, y, label="Oral")` then `plt.legend()` | Legend identifies each line; `loc="upper right"` places it |
| `plt.grid(True)` | Background grid for reading values |
| `plt.xlim(0, 24)`, `plt.ylim(0, 12)` | Set axis ranges |
| `plt.xticks([...])` | Choose tick positions |
| `plt.yscale("log")` | Logarithmic y-axis (semi-log plot) |
| `plt.text(x, y, "note")`, `plt.annotate(...)` | Write text on the plot |
| `plt.figure(figsize=(6, 4))` | Size in inches |

**Line style shortcuts** in `plt.plot(x, y, "o-")`: markers `o` circle, `s` square, `^` triangle, `x` cross; lines `-` solid, `--` dashed, `:` dotted, `-.` dash-dot; colours `"b"`, `"r"`, `"g"`, `"k"` (or `color="tab:blue"`). Also `linewidth=2`, `markersize=6`.

## 5.4 Line plots — concentration–time curves for IV and oral administration

A **line plot** joins points in order; it is the right choice when x is continuous and ordered, such as time.

Two classic one-compartment shapes (practice numbers, not data of any real medicine):

- **IV bolus**: the whole dose enters the blood at once, so concentration is highest at time 0 and then falls exponentially: C = C0 × e^(−k·t), where k is the elimination rate constant.
- **Oral**: the drug must first be absorbed, so concentration rises from zero, reaches a peak (**Cmax** at **Tmax**) and then falls: C = A × (e^(−k·t) − e^(−ka·t)), where ka is the absorption rate constant.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 97)                 # 0 to 24 h every 15 min
k, ka = 0.2, 1.2                           # 1/h, practice values
iv = 10 * np.exp(-k * t)                   # C0 = 10 ug/mL
oral = 12 * (np.exp(-k * t) - np.exp(-ka * t))

plt.figure(figsize=(6, 4))
plt.plot(t, iv, "b-", label="IV bolus")
plt.plot(t, oral, "r--", label="Oral")
plt.xlabel("Time (h)")
plt.ylabel("Plasma concentration (ug/mL)")
plt.title("Concentration-time curves")
plt.legend()
plt.grid(True)
plt.savefig("conc_time.png", dpi=300)
plt.close()

i = oral.argmax()
print("Oral: Cmax =", round(oral[i], 2), "ug/mL at Tmax =", t[i], "h")
print("IV: highest at t = 0 h:", iv[0], "ug/mL")
print("Half-life = 0.693/k =", round(0.693 / k, 2), "h")
```

Output:

```text
Oral: Cmax = 6.99 ug/mL at Tmax = 1.75 h
IV: highest at t = 0 h: 10.0 ug/mL
Half-life = 0.693/k = 3.46 h
```

The sampled peak is at 1.75 h because the time grid has 15-minute steps; the exact one-compartment value, Tmax = ln(ka/k)/(ka − k) = ln 6 / 1.0 ≈ 1.79 h, falls between two grid points.

What the curves look like:

```text
 C |  IV
   |*                          Oral: rises (absorption > elimination),
   | *      .  .               peaks at Tmax (absorption = elimination),
   |  *  .        .            then falls (elimination > absorption)
   |  .*              .
   | .   *                .
   |.       *   *              IV: falls from the first moment
   +-------------------------- t
```

### Semi-log plot

Plotting the IV data with a **logarithmic y-axis** turns the exponential fall into a **straight line**; its slope gives the elimination rate constant (slope = −k/2.303 on log10 scale). This is how first-order elimination is recognised.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.5, 1, 2, 4, 6, 8])
c = 10 * np.exp(-0.2 * t)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.5))
ax1.plot(t, c, "o-")
ax1.set_title("Linear scale")
ax2.semilogy(t, c, "o-")
ax2.set_title("Semi-log scale")
for ax in (ax1, ax2):
    ax.set_xlabel("Time (h)")
    ax.set_ylabel("Conc (ug/mL)")
fig.tight_layout()
fig.savefig("semilog.png")
plt.close(fig)

slope = np.polyfit(t, np.log10(c), 1)[0]
print("slope of log10(C) vs t =", round(slope, 4))
print("k = -2.303 x slope =", round(-2.303 * slope, 3), "per h")
```

Output:

```text
slope of log10(C) vs t = -0.0869
k = -2.303 x slope = 0.2 per h
```

`plt.subplots(1, 2)` makes one figure with two Axes side by side; `tight_layout()` stops labels overlapping. `semilogy()` is a shortcut for a plot with `yscale("log")`.

## 5.5 Histograms — distribution of tablet weights

A **histogram** divides a range of values into intervals (**bins**) and draws a bar whose height is the number of values in each bin. It shows the **distribution**: centre, spread, symmetry or skewness and outliers. It is used for one continuous variable (tablet weight, particle size, assay results). Unlike a bar chart, the bars touch because the bins are continuous.

```python
import matplotlib.pyplot as plt

weights = [248, 251, 249, 252, 250, 247, 253, 250, 251, 249,
           246, 252, 250, 254, 248, 250, 251, 249, 250, 262]   # mg, 20 tablets

counts, edges, bars = plt.hist(weights, bins=8, edgecolor="black")
plt.xlabel("Tablet weight (mg)")
plt.ylabel("Number of tablets")
plt.title("Weight distribution of 20 tablets")
plt.axvline(sum(weights) / len(weights), color="red", linestyle="--", label="Mean")
plt.legend()
plt.savefig("weights_hist.png")
plt.close()

print("Mean weight:", sum(weights) / len(weights), "mg")
print("Counts per bin:", counts.astype(int).tolist())
print("Bin edges:", [round(float(e), 1) for e in edges])
```

Output:

```text
Mean weight: 250.6 mg
Counts per bin: [2, 5, 8, 3, 1, 0, 0, 1]
Bin edges: [246.0, 248.0, 250.0, 252.0, 254.0, 256.0, 258.0, 260.0, 262.0]
```

Interpretation: most tablets cluster around 250 mg in a roughly symmetrical heap; the lone bar at the right end (262 mg) is an **outlier** that should be investigated. Too few bins hide the shape; too many make it ragged — try a few values of `bins`.

## 5.6 Scatter plots — calibration curve

A **scatter plot** shows each pair of values (x, y) as a separate point, without joining them. It is used to see the **relationship** (correlation) between two variables. A calibration curve in UV spectroscopy plots absorbance against known concentrations; by Beer–Lambert's law it should be a straight line, and the fitted line is used to find the concentration of an unknown.

```python
import numpy as np
import matplotlib.pyplot as plt

conc = np.array([2, 4, 6, 8, 10])                     # ug/mL standards
absb = np.array([0.105, 0.212, 0.318, 0.421, 0.530])

slope, intercept = np.polyfit(conc, absb, 1)         # straight-line fit y = mx + c
r = np.corrcoef(conc, absb)[0, 1]

plt.scatter(conc, absb, color="navy", label="Standards")
plt.plot(conc, slope * conc + intercept, "r-", label="Fitted line")
plt.xlabel("Concentration (ug/mL)")
plt.ylabel("Absorbance")
plt.title("Calibration curve")
plt.legend()
plt.savefig("calibration.png")
plt.close()

print(f"y = {slope:.4f}x {intercept:+.4f}")
print(f"r^2 = {r**2:.4f}")
unknown_abs = 0.365
print("Unknown concentration =", round((unknown_abs - intercept) / slope, 2), "ug/mL")
```

Output:

```text
y = 0.0529x -0.0005
r^2 = 0.9999
Unknown concentration = 6.9 ug/mL
```

Interpretation: points lie almost exactly on the line, r² is very close to 1 (good linearity), the intercept is near zero, and the unknown's concentration is read back from the equation x = (y − c)/m. Points bending away at high concentration would show deviation from Beer–Lambert's law; such a sample should be diluted.

## 5.7 Box plots — comparing batches

A **box plot** (box-and-whisker plot) summarises a distribution with five numbers and shows outliers:

```text
        o            <- outlier (beyond 1.5 x IQR from the box)
        |            <- upper whisker (largest value within the limit)
     +-----+         <- Q3 (75th percentile)
     |     |
     |-----|         <- median (Q2, 50th percentile)
     |     |
     +-----+         <- Q1 (25th percentile)
        |            <- lower whisker
   IQR = Q3 - Q1 (height of the box) = spread of the middle 50%
```

It is ideal for comparing the spread of several groups side by side, such as hardness or dissolution of three batches.

```python
import numpy as np
import matplotlib.pyplot as plt

batch_a = [5.1, 5.3, 5.0, 5.2, 5.4, 5.1, 5.2, 5.3]      # hardness, kg/cm2
batch_b = [4.6, 5.2, 4.9, 5.5, 4.4, 5.0, 5.3, 4.7]
batch_c = [5.9, 6.0, 6.2, 5.8, 6.1, 6.0, 7.4, 5.9]

plt.boxplot([batch_a, batch_b, batch_c])
plt.xticks([1, 2, 3], ["Batch A", "Batch B", "Batch C"])
plt.ylabel("Hardness (kg/cm2)")
plt.title("Tablet hardness by batch")
plt.savefig("hardness_box.png")
plt.close()

for name, data in [("A", batch_a), ("B", batch_b), ("C", batch_c)]:
    q1, med, q3 = np.percentile(data, [25, 50, 75])
    print(f"Batch {name}: median {med:.2f}, IQR {q3 - q1:.3f}")
```

Output:

```text
Batch A: median 5.20, IQR 0.200
Batch B: median 4.95, IQR 0.550
Batch C: median 6.00, IQR 0.225
```

Interpretation: Batch A is the most uniform (smallest box), Batch B varies most (tall box — check mixing or compression), and Batch C has a higher median with one outlying tablet (7.4) shown as a separate point.

## 5.8 Bar charts — ADR reporting rates across drugs

A **bar chart** compares a value across **categories** (drugs, batches, hospitals). Bars are separate because categories are not continuous. A **reporting rate** puts counts on a common scale, for example reports per 1,000 prescriptions, so drugs used by different numbers of patients can be compared.

```python
import matplotlib.pyplot as plt

drugs = ["Drug A", "Drug B", "Drug C", "Drug D"]
reports = [18, 42, 9, 30]                    # ADR reports received (practice data)
prescriptions = [6000, 7000, 4500, 12000]    # prescriptions in the same period
rates = [r / p * 1000 for r, p in zip(reports, prescriptions)]

plt.bar(drugs, rates, color="tab:orange", edgecolor="black")
plt.ylabel("ADR reports per 1,000 prescriptions")
plt.title("ADR reporting rate by drug")
plt.savefig("adr_rates.png")
plt.close()

for d, rate in sorted(zip(drugs, rates), key=lambda x: x[1], reverse=True):
    print(f"{d}: {rate:.1f}")
```

Output:

```text
Drug B: 6.0
Drug A: 3.0
Drug D: 2.5
Drug C: 2.0
```

Interpretation: Drug B has the highest **rate**, although Drug D had more reports in raw numbers than Drug A — Drug D is simply prescribed more. Reporting rates show a **signal** worth looking into, not proof that a drug causes harm: spontaneous reporting depends on awareness, under-reporting and publicity. `plt.barh()` draws horizontal bars, useful when names are long.

## 5.9 Dissolution profiles

A **dissolution profile** plots the cumulative percentage of drug released against time for a solid dosage form. Comparing a test product with a reference product is a routine use. The **similarity factor f2** is commonly used to compare two profiles:

f2 = 50 × log10 { [1 + (1/n) Σ (Rt − Tt)²]^(−0.5) × 100 }

where Rt and Tt are the percentages dissolved for reference and test at each time point and n is the number of time points. f2 between 50 and 100 means the profiles are considered similar (100 = identical).

```python
import numpy as np
import matplotlib.pyplot as plt

time_min = [5, 10, 15, 30, 45, 60]
reference = [22, 41, 58, 79, 90, 95]       # % released
test = [18, 36, 55, 77, 89, 96]

plt.plot(time_min, reference, "o-", label="Reference")
plt.plot(time_min, test, "s--", label="Test")
plt.xlabel("Time (min)")
plt.ylabel("Cumulative drug released (%)")
plt.title("Dissolution profiles")
plt.ylim(0, 105)
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.savefig("dissolution.png")
plt.close()

r, t = np.array(reference), np.array(test)
f2 = 50 * np.log10(100 / np.sqrt(1 + np.mean((r - t) ** 2)))
print("f2 =", round(f2, 1))
print("Released at 30 min: reference", reference[3], "%, test", test[3], "%")
```

Output:

```text
f2 = 74.6
Released at 30 min: reference 79 %, test 77 %
```

Interpretation: both curves rise quickly then level off (plateau) as the drug is used up; the test product is slightly slower at the start but the curves nearly overlap later, and f2 above 50 indicates similar profiles.

## 5.10 Plotting directly from Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"time_h": [0, 1, 2, 4, 8], "conc": [0, 6.5, 8.9, 6.8, 3.1]})
ax = df.plot(x="time_h", y="conc", marker="o", legend=False, title="PK profile")
ax.set_xlabel("Time (h)")
ax.set_ylabel("Conc (ug/mL)")
plt.savefig("pk_pandas.png")
plt.close()
print("Peak:", df["conc"].max(), "at", df.loc[df["conc"].idxmax(), "time_h"], "h")
```

Output:

```text
Peak: 8.9 at 2 h
```

`df.plot(kind="line" | "bar" | "hist" | "box" | "scatter")` covers the common chart types in one line.

## 5.11 Choosing the right plot

| Question | Plot | Pharmacy example |
| --- | --- | --- |
| How does a value change over time? | Line plot | Concentration–time curve, dissolution profile, stability over months |
| How are values spread? | Histogram | Tablet weights, particle sizes |
| Is there a relationship between two variables? | Scatter plot (with fitted line) | Calibration curve, dose–response data |
| How do groups compare in median and spread? | Box plot | Hardness or assay of several batches |
| How do categories compare? | Bar chart | ADR reporting rate by drug, sales by product |

## 5.12 Scientific interpretation of plots

Making a graph is half the job; reading it correctly is the other half.

1. **Read the axes first** — what is plotted, in which units, on what scale (linear or log)? A log axis changes the visual shape.
2. **Describe the overall pattern** — rising, falling, linear, exponential, plateau, peak.
3. **Note key values** — maximum (Cmax), time of maximum (Tmax), slope, intercept, median, IQR, r².
4. **Compare groups** — which line is higher, which box is wider, do the curves overlap?
5. **Look for outliers or odd points** and give a possible reason (weighing error, sampling error, a faulty tablet).
6. **Relate to science** — absorption and elimination, Beer–Lambert's law, batch uniformity, signal detection.
7. **State limits** — small sample, practice data, correlation is not causation, reporting bias in ADR data.

**Good graph practice**: label both axes with units; give a title; add a legend when there is more than one series; start the y-axis at zero for bar charts (a cut axis exaggerates differences); use a log scale only when it helps and say so; avoid 3-D effects and too many colours; save at adequate resolution (`dpi=300` for print).

## Remember

- `import matplotlib.pyplot as plt`; Figure = whole picture, Axes = one plot area.
- Steps: data → `plot`/`hist`/`scatter`/`boxplot`/`bar` → `xlabel`, `ylabel`, `title`, `legend`, `grid` → `savefig`/`show`.
- Line plot for time courses (IV falls from time 0; oral rises to Cmax at Tmax then falls); semi-log plot makes first-order elimination a straight line.
- Histogram shows distribution with touching bars (bins); bar chart compares categories with separate bars.
- Scatter + `np.polyfit` gives the calibration line y = mx + c and r² for linearity; unknown x = (y − c)/m.
- Box plot: median, Q1, Q3, IQR, whiskers and outliers — best for comparing batches.
- Dissolution profile = % released vs time; f2 of 50–100 means similar profiles.
- Interpret: axes and units, pattern, key values, comparison, outliers, scientific meaning, limitations.
