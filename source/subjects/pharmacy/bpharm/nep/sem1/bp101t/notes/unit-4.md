# Unit 4: Data handling with Pandas

Lists, dictionaries and the csv module can handle small files, but they need loops for every task. **Pandas** is the standard Python library for working with **tables of data** — the same rows-and-columns layout you see in Excel. With Pandas you can load a pharmacokinetic (PK) study or a file of adverse drug reaction (ADR) reports, look at it, clean it, pick the rows you need and summarise it by group, usually in one line per step.

## 4.1 Introduction to Pandas

- Pandas is an open-source, third-party library built on top of NumPy. The name comes from "panel data", a term for multi-dimensional structured data sets.
- Install: `pip install pandas` (comes with Anaconda). Reading Excel files also needs `openpyxl` (`pip install openpyxl`).
- Standard import: `import pandas as pd`.

**What Pandas is used for**

| Task | Pandas tool |
| --- | --- |
| Load data from CSV, Excel, databases | `pd.read_csv()`, `pd.read_excel()` |
| Look at the data | `head()`, `tail()`, `info()`, `describe()`, `shape` |
| Clean data | `isna()`, `dropna()`, `fillna()`, `drop_duplicates()`, `astype()`, string methods |
| Select and filter | `df["col"]`, `loc[]`, `iloc[]`, conditions |
| Summarise | `mean()`, `value_counts()`, `groupby()` with `agg()` |
| Save results | `to_csv()`, `to_excel()` |
| Plot | `df.plot()` (uses Matplotlib, Unit 5) |

**Advantages over spreadsheets for data work**: handles very large files, every step is written down as code so the analysis can be **repeated and checked** (reproducibility), the same script works on next month's data, and it links directly to statistics and graph libraries.

## 4.2 Pandas data structures

```text
 Series (1-D)                 DataFrame (2-D)
 ------------                 ----------------------------------
 index  value                 index | batch  hardness_kg  friability_pct
 0.5 h  12.0                    0   |  B1        5.2          0.42
 1 h    18.5                    1   |  B2        4.8          0.65
 2 h    15.2                    2   |  B3        6.1          0.31
 4 h     9.8                            (each column is a Series)
```

### 4.2.1 Series

A **Series** is a one-dimensional labelled array: values plus an **index** (labels). Think of it as one column of a table.

```python
import pandas as pd

conc = pd.Series([12.0, 18.5, 15.2, 9.8], index=["0.5 h", "1 h", "2 h", "4 h"], name="conc_ug_ml")
print(conc)
print(conc["1 h"], conc.iloc[0])
print(conc.max(), conc.idxmax())
print(conc * 1000)
```

Output:

```text
0.5 h    12.0
1 h      18.5
2 h      15.2
4 h       9.8
Name: conc_ug_ml, dtype: float64
18.5 12.0
18.5 1 h
0.5 h    12000.0
1 h      18500.0
2 h      15200.0
4 h       9800.0
Name: conc_ug_ml, dtype: float64
```

- `conc["1 h"]` looks up by **label**; `conc.iloc[0]` by **position**.
- `idxmax()` returns the label of the largest value — here the time of the peak concentration.
- Arithmetic is applied to every value, as with NumPy arrays.

### 4.2.2 DataFrame

A **DataFrame** is a two-dimensional table with labelled rows (index) and labelled columns. Each column is a Series and can have its own data type. It can be built from a dictionary of lists, a list of dictionaries, a NumPy array, or read from a file.

```python
import pandas as pd

batches = pd.DataFrame({
    "batch": ["B1", "B2", "B3"],
    "hardness_kg": [5.2, 4.8, 6.1],
    "friability_pct": [0.42, 0.65, 0.31],
})
print(batches)
print(batches.shape)
print(batches.columns.tolist())
print(batches["hardness_kg"].mean())
```

Output:

```text
  batch  hardness_kg  friability_pct
0    B1          5.2            0.42
1    B2          4.8            0.65
2    B3          6.1            0.31
(3, 3)
['batch', 'hardness_kg', 'friability_pct']
5.366666666666667
```

| Series | DataFrame |
| --- | --- |
| One dimension (a single column) | Two dimensions (rows and columns) |
| One data type | Each column can have its own data type |
| Has an index | Has an index (rows) and column labels |
| `pd.Series([...])` | `pd.DataFrame({...})` |
| Selecting one column of a DataFrame gives a Series | Selecting several columns gives a DataFrame |

Useful attributes: `df.shape` (rows, columns), `df.columns`, `df.index`, `df.dtypes`, `len(df)` (number of rows).

## 4.3 Reading CSV and Excel files

| Function | Reads | Common options |
| --- | --- | --- |
| `pd.read_csv("file.csv")` | Comma-separated text | `sep=";"` for other separators, `usecols=[...]`, `na_values=["NA", "-"]`, `skiprows=2` |
| `pd.read_excel("file.xlsx", sheet_name="Sheet1")` | Excel workbook (needs openpyxl) | `sheet_name=0` (first sheet) or a name, `usecols`, `skiprows` |
| `df.to_csv("out.csv", index=False)` | Writes CSV | `index=False` avoids an extra index column |
| `df.to_excel("out.xlsx", index=False)` | Writes Excel | `sheet_name="Results"` |

### 4.3.1 A PK study dataset (CSV)

In a pharmacokinetic study, blood samples are taken at set times after a drug is given and the drug concentration in plasma is measured. The file below holds made-up practice data for two subjects; subject S2's 12-hour sample is missing (an empty cell).

```python
import pandas as pd

pk_text = """subject,time_h,conc_ug_ml
S1,0,0.0
S1,0.5,4.1
S1,1,7.9
S1,2,9.6
S1,4,7.2
S1,8,3.5
S1,12,1.6
S2,0,0.0
S2,0.5,3.2
S2,1,6.8
S2,2,10.4
S2,4,8.1
S2,8,4.0
S2,12,
"""
with open("pk_study.csv", "w") as f:
    f.write(pk_text)

pk = pd.read_csv("pk_study.csv")
print(pk.head())
print(pk.tail(3))
```

Output:

```text
  subject  time_h  conc_ug_ml
0      S1     0.0         0.0
1      S1     0.5         4.1
2      S1     1.0         7.9
3      S1     2.0         9.6
4      S1     4.0         7.2
   subject  time_h  conc_ug_ml
11      S2     4.0         8.1
12      S2     8.0         4.0
13      S2    12.0         NaN
```

The empty cell has been read as **NaN** ("Not a Number"), Pandas' marker for a missing value.

### 4.3.2 An ADR report dataset (Excel)

Pharmacovigilance centres collect ADR reports: which drug, what reaction, how serious, patient details. The practice file below (drug names are placeholders) has typical real-life problems: one report entered twice, one drug name typed in a different case with a trailing space, a missing age and a missing reaction. We save it as Excel and read it back.

```python
import pandas as pd

adr = pd.DataFrame({
    "report_id": [101, 102, 103, 104, 105, 105, 106, 107],
    "drug": ["Drug A", "drug a ", "Drug B", "Drug C", "Drug B", "Drug B", "Drug A", "Drug C"],
    "reaction": ["Rash", "Nausea", "Headache", "Rash", "Dizziness", "Dizziness", "Rash", None],
    "serious": ["No", "No", "Yes", "No", "Yes", "Yes", "No", "No"],
    "age": [34, 51, None, 29, 62, 62, 45, 38],
})
adr.to_excel("adr_reports.xlsx", index=False)
adr2 = pd.read_excel("adr_reports.xlsx")
print(adr2.shape)
print(adr2.head(3))
```

Output:

```text
(8, 5)
   report_id     drug  reaction serious   age
0        101   Drug A      Rash      No  34.0
1        102  drug a     Nausea      No  51.0
2        103   Drug B  Headache     Yes   NaN
```

## 4.4 Inspecting a dataset

Always look at a new dataset before analysing it.

| Function | Shows |
| --- | --- |
| `df.head(n)` | First n rows (default 5) |
| `df.tail(n)` | Last n rows (default 5) |
| `df.info()` | Number of rows, column names, **non-null count** per column, data type of each column, memory used |
| `df.describe()` | Summary statistics of numeric columns: count, mean, std, min, 25%, 50% (median), 75%, max |
| `df.shape`, `df.dtypes`, `df.columns` | Size, types, names |
| `df["col"].unique()`, `df["col"].value_counts()` | Distinct values and how often each occurs |

### info()

```python
import pandas as pd

pk = pd.read_csv("pk_study.csv")
pk.info()
```

Output:

```text
<class 'pandas.DataFrame'>
RangeIndex: 14 entries, 0 to 13
Data columns (total 3 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   subject     14 non-null     str
 1   time_h      14 non-null     float64
 2   conc_ug_ml  13 non-null     float64
dtypes: float64(2), str(1)
memory usage: 468.0 bytes
```

Read it like this: 14 rows (index 0–13); `conc_ug_ml` has only 13 non-null values, so **one value is missing**; `time_h` and `conc_ug_ml` are floats; `subject` is text. Text columns are shown as `str` in Pandas 3; older Pandas versions show them as `object`. Note that `info()` prints by itself — you do not wrap it in `print()`.

### describe()

```python
import pandas as pd

pk = pd.read_csv("pk_study.csv")
print(pk.describe().round(2))
```

Output:

```text
       time_h  conc_ug_ml
count   14.00       13.00
mean     3.93        5.11
std      4.32        3.48
min      0.00        0.00
25%      0.62        3.20
50%      2.00        4.10
75%      7.00        7.90
max     12.00       10.40
```

- `count` differs between columns because of the missing value.
- `50%` is the median; `25%` and `75%` are the quartiles.
- Text columns are left out by default; `describe(include="all")` adds counts of unique values for them.

## 4.5 Data cleaning and handling missing values

Real datasets contain gaps, repeated entries, spelling variations and wrong types. Analysing them without cleaning gives wrong results ("garbage in, garbage out").

### 4.5.1 Finding problems

```python
import pandas as pd

adr = pd.read_excel("adr_reports.xlsx")
print(adr.isna().sum())
print("Duplicate rows:", adr.duplicated().sum())
```

Output:

```text
report_id    0
drug         0
reaction     1
serious      0
age          1
dtype: int64
Duplicate rows: 1
```

`isna()` (same as `isnull()`) marks each missing cell `True`; `.sum()` counts them per column (True counts as 1).

### 4.5.2 Ways to handle missing values

| Method | Code | When to use |
| --- | --- | --- |
| Drop rows with any missing value | `df.dropna()` | Few missing rows, and losing them does not bias results |
| Drop only if a key column is missing | `df.dropna(subset=["reaction"])` | That column is essential |
| Drop a column that is mostly empty | `df.dropna(axis=1, thresh=n)` or `df.drop(columns=[...])` | Column has too little data |
| Fill with a fixed value | `df["col"].fillna(0)` or `fillna("Unknown")` | A sensible default exists |
| Fill with mean / median | `df["col"].fillna(df["col"].median())` | Numeric column; median is safer with outliers |
| Fill from neighbouring rows | `ffill()`, `bfill()`, `interpolate()` | Ordered data such as time series |

In clinical and PK data, **do not invent values casually**: a missing concentration is usually reported as missing, and any filling method must be stated in the report.

### 4.5.3 A cleaning pipeline

```python
import pandas as pd

adr = pd.read_excel("adr_reports.xlsx")
adr = adr.drop_duplicates()                                 # remove repeated report
adr["drug"] = adr["drug"].str.strip().str.title()           # "drug a " -> "Drug A"
adr["age"] = adr["age"].fillna(adr["age"].median())         # fill missing age
adr = adr.dropna(subset=["reaction"])                       # drop row with no reaction
adr["serious"] = adr["serious"].map({"Yes": True, "No": False})
adr = adr.rename(columns={"age": "age_years"})
print(adr)
adr.to_csv("adr_clean.csv", index=False)
```

Output:

```text
   report_id    drug   reaction  serious  age_years
0        101  Drug A       Rash    False       34.0
1        102  Drug A     Nausea    False       51.0
2        103  Drug B   Headache     True       41.5
3        104  Drug C       Rash    False       29.0
4        105  Drug B  Dizziness     True       62.0
6        106  Drug A       Rash    False       45.0
```

Other cleaning tools: `astype(int)` or `pd.to_numeric(df["col"], errors="coerce")` to fix types (bad entries become NaN), `pd.to_datetime()` for dates, `str.lower()`/`str.replace()` for text, `replace({"M": "Male"})` to standardise codes, `reset_index(drop=True)` to renumber rows after dropping.

## 4.6 Selecting and filtering data

### 4.6.1 Filtering rows with conditions (boolean indexing)

A condition on a column gives a Series of True/False; putting it inside `df[ ]` keeps only the True rows.

- Combine conditions with `&` (and), `|` (or), `~` (not), and put **each condition in brackets**. Python's words `and`/`or` do not work here.
- `isin([...])` keeps rows whose value is in a list.

```python
import pandas as pd

pk = pd.read_csv("pk_study.csv")
print(pk[pk["conc_ug_ml"] > 8])                                   # one condition
print(pk[(pk["subject"] == "S2") & (pk["time_h"] <= 1)])          # AND
print(pk[pk["time_h"].isin([0, 12])].shape)                       # several values
```

Output:

```text
   subject  time_h  conc_ug_ml
3       S1     2.0         9.6
10      S2     2.0        10.4
11      S2     4.0         8.1
  subject  time_h  conc_ug_ml
7      S2     0.0         0.0
8      S2     0.5         3.2
9      S2     1.0         6.8
(4, 3)
```

### 4.6.2 Selecting columns, loc and iloc

| Syntax | Selects |
| --- | --- |
| `df["col"]` | One column (Series) |
| `df[["col1", "col2"]]` | Several columns (DataFrame) — note the double brackets |
| `df.loc[row_label, col_label]` | By **labels**; slices include the end label |
| `df.iloc[row_pos, col_pos]` | By **positions** (0, 1, 2…); slices exclude the end, like lists |
| `df.loc[condition, ["col"]]` | Rows meeting a condition, chosen columns |
| `df.sort_values("col", ascending=False)` | Rows sorted by a column |

```python
import pandas as pd

pk = pd.read_csv("pk_study.csv")
print(pk[["time_h", "conc_ug_ml"]].head(2))          # select columns
print(pk.loc[2, "conc_ug_ml"])                       # label-based: row label 2
print(pk.iloc[0:2, 0:2])                             # position-based
print(pk.loc[pk["conc_ug_ml"] >= 9.6, ["subject", "time_h"]])
print(pk.sort_values("conc_ug_ml", ascending=False).head(2))
```

Output:

```text
   time_h  conc_ug_ml
0     0.0         0.0
1     0.5         4.1
7.9
  subject  time_h
0      S1     0.0
1      S1     0.5
   subject  time_h
3       S1     2.0
10      S2     2.0
   subject  time_h  conc_ug_ml
10      S2     2.0        10.4
3       S1     2.0         9.6
```

New columns can be made from old ones: `pk["conc_ng_ml"] = pk["conc_ug_ml"] * 1000`.

## 4.7 Grouping and aggregation

**Aggregation** turns many values into one summary value (sum, mean, count, min, max, median, std). **groupby** first splits the table into groups by one or more columns, then aggregates each group separately, then combines the results — the **split–apply–combine** idea.

```text
        split by drug            apply count            combine
 Drug A | 101 |                 Drug A -> 3
 Drug A | 102 |   ------->      Drug B -> 2      --->   one small table
 Drug B | 103 |                 Drug C -> 1
 ...
```

```python
import pandas as pd

adr = pd.read_csv("adr_clean.csv")
print(adr["drug"].value_counts())
print(adr.groupby("drug")["report_id"].count())
print(adr.groupby("drug")["age_years"].agg(["mean", "min", "max"]))
print(adr.groupby(["drug", "serious"]).size())
```

Output:

```text
drug
Drug A    3
Drug B    2
Drug C    1
Name: count, dtype: int64
drug
Drug A    3
Drug B    2
Drug C    1
Name: report_id, dtype: int64
             mean   min   max
drug
Drug A  43.333333  34.0  51.0
Drug B  51.750000  41.5  62.0
Drug C  29.000000  29.0  29.0
drug    serious
Drug A  False      3
Drug B  True       2
Drug C  False      1
dtype: int64
```

- `value_counts()` — quickest count of each category.
- `groupby("drug")["col"].count()` — same idea, choosing what to count.
- `agg([...])` — several summaries at once.
- Grouping by two columns gives a count for every combination (here serious and non-serious reports per drug).
- Drug B's mean age includes the median (41.5) that was filled in during cleaning — a reminder that filling choices change later results.

### 4.7.1 Summarising a PK study by subject

**Cmax** is the highest observed concentration and **Tmax** the time at which it occurs. **AUC** (area under the concentration–time curve) measures total exposure; the **trapezoidal rule** adds up the areas of the trapezia between consecutive points: area = (C1 + C2)/2 × (t2 − t1).

```python
import pandas as pd

pk = pd.read_csv("pk_study.csv")
summary = pk.groupby("subject").agg(
    cmax=("conc_ug_ml", "max"),
    samples=("conc_ug_ml", "count"),
)
summary["tmax_h"] = pk.loc[pk.groupby("subject")["conc_ug_ml"].idxmax(), "time_h"].values
print(summary)

s1 = pk[pk["subject"] == "S1"]
t = s1["time_h"].values
c = s1["conc_ug_ml"].values
auc = sum((c[i] + c[i + 1]) / 2 * (t[i + 1] - t[i]) for i in range(len(t) - 1))
print("AUC(0-12 h), subject S1 =", round(auc, 2), "ug.h/mL")
```

Output:

```text
         cmax  samples  tmax_h
subject
S1        9.6        7     2.0
S2       10.4        6     2.0
AUC(0-12 h), subject S1 = 61.18 ug.h/mL
```

Note `samples` = 6 for S2: `count` ignores the missing value. Aggregation functions skip NaN by default.

## 4.8 A complete workflow

```text
 1. Load        pd.read_csv / pd.read_excel
 2. Inspect     head, tail, info, describe, isna().sum()
 3. Clean       drop_duplicates, strip/title, fillna/dropna, astype, rename
 4. Select      columns, loc/iloc, conditions with & | ~
 5. Summarise   value_counts, groupby + agg
 6. Report      to_csv / to_excel, plots (Unit 5)
```

## Remember

- `import pandas as pd`; Pandas sits on NumPy and handles tables.
- Series = one labelled column; DataFrame = labelled table whose columns are Series.
- `read_csv`, `read_excel` (needs openpyxl) load data; `to_csv(index=False)` saves it.
- Inspect with `head()`, `tail()`, `info()` (non-null counts, types) and `describe()` (count, mean, std, min, quartiles, max).
- Missing values show as NaN: find with `isna().sum()`, handle with `dropna()` or `fillna()`; state what you did.
- Filter with conditions in brackets joined by `&`, `|`, `~`; `loc` uses labels, `iloc` uses positions.
- `groupby(...).agg(...)` = split–apply–combine; `value_counts()` counts categories.
- Cmax = highest concentration, Tmax = its time, AUC by the trapezoidal rule.
