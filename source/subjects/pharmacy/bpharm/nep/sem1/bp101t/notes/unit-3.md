# Unit 3: Data structures and file handling

One variable holds one value. Laboratory and clinical work produces many values at once: twenty tablet weights, a calibration series, a list of patients with age and blood pressure. **Data structures** hold many values under one name and let you add, remove, sort and look them up. This unit covers Python's lists, tuples and dictionaries, NumPy arrays for fast arithmetic, and reading and writing CSV files that hold structured healthcare data.

## 3.1 Overview of Python data structures

| Structure | Brackets | Ordered | Changeable (mutable) | Duplicates | Accessed by | Example |
| --- | --- | --- | --- | --- | --- | --- |
| List | `[ ]` | Yes | Yes | Allowed | Index (0, 1, 2…) | `[251, 248, 255]` |
| Tuple | `( )` | Yes | **No** | Allowed | Index | `("S-01", 0.421)` |
| Dictionary | `{key: value}` | Yes (insertion order) | Yes | Keys must be unique | Key | `{"batch": "B-101"}` |
| Set | `{ }` | No | Yes | **Not** allowed | — (membership only) | `{"F", "M"}` |

**Mutable** = can be changed after creation; **immutable** = cannot. Strings and tuples are immutable; lists, dictionaries and sets are mutable.

## 3.2 Lists

A **list** is an ordered, changeable collection written in square brackets. It can hold mixed types, though usually all items are of one kind (all weights, all drug names).

### 3.2.1 Indexing and slicing

Indexing works exactly as for strings: first item index 0, last item index −1. Slicing `list[start:stop:step]` returns a new list; `stop` is not included.

```python
weights = [251, 248, 255, 249, 252, 247]   # tablet weights in mg
print(weights[0], weights[-1])             # first and last
print(weights[1:4])                        # index 1, 2, 3
print(weights[:3], weights[3:])
print(weights[::2])                        # every second item
print(len(weights), min(weights), max(weights), sum(weights))
```

Output:

```text
251 247
[248, 255, 249]
[251, 248, 255] [249, 252, 247]
[251, 255, 252]
6 247 255 1502
```

```text
 value:   251   248   255   249   252   247
 index:    0     1     2     3     4     5
          -6    -5    -4    -3    -2    -1
 weights[1:4]  ->  248 255 249   (index 4 not included)
```

An index outside the list (e.g. `weights[10]`) gives `IndexError`; a slice outside the list just returns fewer items.

### 3.2.2 Basic list operations

| Method / operation | What it does |
| --- | --- |
| `lst.append(x)` | Add `x` at the end |
| `lst.insert(i, x)` | Add `x` at position `i` |
| `lst.extend(other)` or `lst + other` | Add all items of another list |
| `lst.remove(x)` | Remove the first item equal to `x` |
| `lst.pop()` / `lst.pop(i)` | Remove and return the last item / item at `i` |
| `del lst[i]` | Delete item at `i` |
| `lst.sort()` / `sorted(lst)` | Sort in place / return a new sorted list (`reverse=True` for descending) |
| `lst.reverse()` | Reverse in place |
| `lst.index(x)`, `lst.count(x)` | Position of `x`, number of times `x` occurs |
| `x in lst` | Membership test |
| `len`, `min`, `max`, `sum` | Built-in functions that work on lists |
| `lst * 3` | Repeat the list |

```python
drugs = ["Drug B", "Drug A"]
drugs.append("Drug D")          # add at the end
drugs.insert(2, "Drug C")       # add at index 2
print(drugs)
drugs.sort()                    # sort in place
print(drugs)
removed = drugs.pop()           # remove and return the last item
print(removed, drugs)
drugs.remove("Drug A")          # remove by value
print(drugs)
drugs[0] = "Drug X"             # lists are mutable
print(drugs, "Drug C" in drugs)
print(drugs + ["Drug Y"], [0] * 3)
```

Output:

```text
['Drug B', 'Drug A', 'Drug C', 'Drug D']
['Drug A', 'Drug B', 'Drug C', 'Drug D']
Drug D ['Drug A', 'Drug B', 'Drug C']
['Drug B', 'Drug C']
['Drug X', 'Drug C'] True
['Drug X', 'Drug C', 'Drug Y'] [0, 0, 0]
```

### 3.2.3 List comprehension

A short way to build a new list from an old one: `[expression for item in list if condition]`.

```python
conc = [2, 4, 6, 8, 10]                    # ug/mL
doubled = [c * 2 for c in conc]            # list comprehension
high = [c for c in conc if c > 5]          # with a condition
print(doubled)
print(high)
```

Output:

```text
[4, 8, 12, 16, 20]
[6, 8, 10]
```

## 3.3 Tuples

A **tuple** is an ordered collection that **cannot be changed** once made. Written with round brackets (a one-item tuple needs a comma: `(5,)`).

Uses: fixed records (a sample's ID, reading and temperature), coordinates, values returned from a function, dictionary keys. Being fixed protects data from accidental change and makes them slightly faster than lists.

```python
sample = ("S-01", 0.421, 24.5)     # id, absorbance, temperature
print(sample[1])
sample_id, absorbance, temp = sample   # unpacking
print(sample_id, absorbance, temp)
print(sample.count(0.421), sample.index(24.5))
try:
    sample[1] = 0.5
except TypeError as e:
    print("Error:", e)
```

Output:

```text
0.421
S-01 0.421 24.5
1 2
Error: 'tuple' object does not support item assignment
```

| List | Tuple |
| --- | --- |
| Square brackets `[ ]` | Round brackets `( )` |
| Mutable: items can be added, removed, changed | Immutable |
| Many methods (append, sort, remove…) | Only `count()` and `index()` |
| For data that grows or changes | For fixed records, function returns, dictionary keys |

## 3.4 Dictionaries

A **dictionary** stores **key: value** pairs. You look up a value by its key, the way you look up a word in a dictionary, instead of by position. Keys must be unique and immutable (usually strings or numbers); values can be anything, including lists and other dictionaries.

### 3.4.1 Basic operations

| Operation | Example |
| --- | --- |
| Read a value | `d["product"]` (KeyError if the key is missing) |
| Safe read with default | `d.get("expiry", "not recorded")` |
| Add or change | `d["expiry"] = "2028-06"` |
| Delete | `del d["passed"]` or `d.pop("passed")` |
| Keys, values, pairs | `d.keys()`, `d.values()`, `d.items()` |
| Merge another dictionary | `d.update(other)` |
| Membership (checks keys) | `"tablets" in d` |
| Number of pairs | `len(d)` |

```python
batch = {"batch_no": "B-101", "product": "Tablet X", "tablets": 1000, "passed": True}
print(batch["product"])
print(batch.get("expiry", "not recorded"))   # safe lookup with a default
batch["tablets"] = 950                         # change a value
batch["expiry"] = "2028-06"                    # add a new key
del batch["passed"]                            # delete a key
print(batch)
print(list(batch.keys()))
print(len(batch), "tablets" in batch)
for key, value in batch.items():
    print(key, "->", value)
```

Output:

```text
Tablet X
not recorded
{'batch_no': 'B-101', 'product': 'Tablet X', 'tablets': 950, 'expiry': '2028-06'}
['batch_no', 'product', 'tablets', 'expiry']
4 True
batch_no -> B-101
product -> Tablet X
tablets -> 950
expiry -> 2028-06
```

### 3.4.2 Counting with a dictionary — ADR reports per drug

```python
adr_reports = ["Drug A", "Drug B", "Drug A", "Drug C", "Drug A", "Drug B"]
counts = {}
for drug in adr_reports:
    counts[drug] = counts.get(drug, 0) + 1
print(counts)
```

Output:

```text
{'Drug A': 3, 'Drug B': 2, 'Drug C': 1}
```

`counts.get(drug, 0)` returns 0 the first time a drug is seen, so the count starts from 1.

### 3.4.3 Nested dictionaries — a small patient table

```python
patients = {
    "P01": {"age": 34, "weight": 62.0},
    "P02": {"age": 51, "weight": 78.5},
}
print(patients["P02"]["weight"])
print([pid for pid, info in patients.items() if info["age"] > 40])
```

Output:

```text
78.5
['P02']
```

## 3.5 String manipulation for data cleaning

Data read from files arrives as **text**. Before calculating you must split it into parts, strip spaces and convert types.

```python
line = "S-03, 0.318 ,  6"
parts = [p.strip() for p in line.split(",")]
print(parts)
sample_id, absorbance, conc = parts[0], float(parts[1]), int(parts[2])
print(sample_id, absorbance * 2, conc + 1)
print("-".join(["2026", "11", "20"]))
print("IBUPROFEN".capitalize())
```

Output:

```text
['S-03', '0.318', '6']
S-03 0.636 7
2026-11-20
Ibuprofen
```

Useful cleaning steps: `strip()` extra spaces, `lower()`/`upper()`/`capitalize()` to make spellings consistent, `replace()` to fix symbols, `split(",")` to break a line, `",".join(list)` to build one.

## 3.6 NumPy arrays

**NumPy** (Numerical Python) is the base library for scientific computing in Python. Its main object is the **ndarray** (n-dimensional array): a grid of values, **all of the same type**, stored compactly in memory. Install with `pip install numpy`; import with the standard alias `import numpy as np`.

**Why NumPy arrays instead of lists**

| Python list | NumPy array |
| --- | --- |
| Items can be of different types | One data type for all items (`int64`, `float64`…) |
| Arithmetic needs a loop | **Vectorised**: one operation acts on every element |
| `[1, 2] * 2` repeats the list → `[1, 2, 1, 2]` | `np.array([1, 2]) * 2` multiplies → `[2 4]` |
| Slower for large numeric data | Much faster, less memory |
| No built-in statistics | `mean()`, `std()`, `sum()`, `min()`, `max()`… |

### 3.6.1 Creating arrays and basic arithmetic

```python
import numpy as np

conc = np.array([2, 4, 6, 8, 10])          # ug/mL
absb = np.array([0.105, 0.212, 0.318, 0.421, 0.530])
print(conc.ndim, conc.shape, conc.dtype)
print(absb.dtype, absb.size)
print(conc * 1000)                          # ug/mL to ng/mL, every element
print(absb / conc)                          # element by element
print(conc + 1, conc ** 2)
print(round(absb.mean(), 3), round(absb.std(), 4), absb.max())
```

Output:

```text
1 (5,) int64
float64 5
[ 2000  4000  6000  8000 10000]
[0.0525   0.053    0.053    0.052625 0.053   ]
[ 3  5  7  9 11] [  4  16  36  64 100]
0.317 0.1498 0.53
```

Attributes: `ndim` (number of dimensions), `shape` (size along each dimension), `dtype` (data type), `size` (total elements). Arrays of the same shape combine **element by element**; `absb / conc` gives absorbance per µg/mL for each standard — nearly constant, as Beer–Lambert's law expects. (`std()` here is the population standard deviation; use `std(ddof=1)` for the sample standard deviation.)

### 3.6.2 Other ways to create arrays; 2-D arrays; boolean indexing

```python
import numpy as np

print(np.arange(0, 25, 5))            # start, stop (excluded), step
print(np.linspace(0, 1, 5))           # 5 evenly spaced values, stop included
print(np.zeros(3), np.ones(2))
grid = np.arange(6).reshape(2, 3)     # 2 rows x 3 columns
print(grid)
print(grid[1, 2], grid[:, 0])
weights = np.array([251, 248, 263, 249, 238])
print(weights[weights > 250])         # boolean indexing
print([1, 2] * 2, np.array([1, 2]) * 2)
```

Output:

```text
[ 0  5 10 15 20]
[0.   0.25 0.5  0.75 1.  ]
[0. 0. 0.] [1. 1.]
[[0 1 2]
 [3 4 5]]
5 [0 3]
[251 263]
[1, 2, 1, 2] [2 4]
```

| Function | Purpose |
| --- | --- |
| `np.array(list)` | Array from a list |
| `np.arange(start, stop, step)` | Evenly stepped values (like `range`, allows decimals) |
| `np.linspace(start, stop, n)` | `n` evenly spaced values including both ends (good for time points) |
| `np.zeros(n)`, `np.ones(n)` | Arrays filled with 0 or 1 |
| `a.reshape(r, c)` | Change shape (rows × columns) |
| `a[r, c]`, `a[:, 0]` | Element at row r, column c; whole first column |
| `a[a > 250]` | Keep only elements meeting a condition |
| `np.mean`, `np.median`, `np.std`, `np.sum`, `np.min`, `np.max` | Summary statistics |
| `np.sqrt`, `np.log`, `np.log10`, `np.exp` | Maths on every element |

## 3.7 File handling and CSV files

### 3.7.1 Opening files

`open(filename, mode)` connects your program to a file. The **with** statement closes the file automatically when the block ends, even if an error happens — always prefer it.

| Mode | Meaning |
| --- | --- |
| `"r"` | Read (default); error if the file does not exist |
| `"w"` | Write; creates the file or **erases** an existing one |
| `"a"` | Append; adds to the end, keeps old content |
| `"r+"` | Read and write |
| `"b"` added (`"rb"`, `"wb"`) | Binary files (images, Excel) |

Reading methods: `f.read()` (whole file as one string), `f.readline()` (one line), `f.readlines()` (list of lines), or loop `for line in f:`. Writing: `f.write(text)`.

### 3.7.2 What is a CSV file

**CSV (comma-separated values)** is a plain-text table: each line is one row (record) and values within a row are separated by commas. The first line usually holds the column names (header). Excel, LIMS software, instruments and data portals can all export CSV.

```text
sample,conc_ug_ml,absorbance        <- header row
S1,2,0.105                          <- one record per line
S2,4,0.212
S3,6,0.318
```

Python's standard **csv** module reads and writes such files correctly, including values that contain commas inside quotes. Open CSV files with `newline=""` so the module controls line endings (otherwise blank lines can appear on Windows).

### 3.7.3 Writing a CSV file

```python
import csv

rows = [
    ["sample", "conc_ug_ml", "absorbance"],
    ["S1", 2, 0.105],
    ["S2", 4, 0.212],
    ["S3", 6, 0.318],
]
with open("calibration.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print("File written")
```

Output:

```text
File written
```

### 3.7.4 Reading a CSV file — csv.reader

Each row comes as a **list of strings**.

```python
import csv

with open("calibration.csv") as f:
    reader = csv.reader(f)
    header = next(reader)          # first row = column names
    print(header)
    for row in reader:
        print(row)
```

Output:

```text
['sample', 'conc_ug_ml', 'absorbance']
['S1', '2', '0.105']
['S2', '4', '0.212']
['S3', '6', '0.318']
```

Note that numbers come back as strings (`'2'`, `'0.105'`) — convert them with `int()` or `float()` before calculating.

### 3.7.5 Reading with csv.DictReader

Each row comes as a **dictionary** keyed by the column names, which makes code easier to read.

```python
import csv

with open("calibration.csv", newline="") as f:
    for row in csv.DictReader(f):
        ratio = float(row["absorbance"]) / float(row["conc_ug_ml"])
        print(row["sample"], round(ratio, 4))
```

Output:

```text
S1 0.0525
S2 0.053
S3 0.053
```

| csv.reader / csv.writer | csv.DictReader / csv.DictWriter |
| --- | --- |
| Row = list; access by position `row[2]` | Row = dictionary; access by name `row["absorbance"]` |
| Header is just the first row | Header used automatically as keys |
| Shorter for very simple files | Clearer and safer if column order changes |

## 3.8 Understanding structured healthcare datasets

**Structured data** is organised in a fixed table format: rows and columns with a defined meaning, so it can be searched and calculated easily (patient registers, lab results, PK sampling sheets, ADR databases). **Unstructured data** has no fixed format: free-text clinical notes, scanned prescriptions, images.

Key terms:

| Term | Meaning | Example |
| --- | --- | --- |
| Record / observation (row) | One unit being described | One patient, one sample, one ADR report |
| Variable / field (column) | One property measured for every record | Age, sex, drug, concentration |
| Identifier (ID) | Unique code for each record | `P01`, report number |
| Numerical (quantitative) variable | Continuous (weight, concentration) or discrete (number of doses) | 62.5 kg |
| Categorical (qualitative) variable | Nominal (sex, drug name) or ordinal (mild/moderate/severe) | "F" |
| Missing value | Not recorded | Empty cell, `NA` |
| Data dictionary (metadata) | Document describing each column, its unit and allowed values | "sbp = systolic blood pressure, mmHg" |

Good practice with healthcare data:

- One row per record, one column per variable, one value per cell (**tidy data**).
- Units stated in column names (`weight_kg`, `conc_ug_ml`).
- Patient data must be **de-identified** (no names, phone numbers or addresses) and used only with permission and for the stated purpose; follow ethics committee rules and data protection law.
- Typical public sources for practice: data.gov.in, WHO data, clinical trial registries such as CTRI and ClinicalTrials.gov, and open datasets on Kaggle.

## 3.9 Importing a small dataset and basic data access and manipulation

The program below writes a small, de-identified patient file, reads it back, skips a missing value, filters by a category, and then **appends** a new record.

```python
import csv

data = [
    {"patient_id": "P01", "sex": "F", "age": "34", "sbp": "118"},
    {"patient_id": "P02", "sex": "M", "age": "51", "sbp": "142"},
    {"patient_id": "P03", "sex": "F", "age": "47", "sbp": ""},
    {"patient_id": "P04", "sex": "M", "age": "29", "sbp": "126"},
]
with open("patients.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["patient_id", "sex", "age", "sbp"])
    writer.writeheader()
    writer.writerows(data)

with open("patients.csv", newline="") as f:
    records = list(csv.DictReader(f))

print("Records:", len(records))
sbp = [int(r["sbp"]) for r in records if r["sbp"] != ""]
print("Valid SBP values:", sbp, "mean", round(sum(sbp) / len(sbp), 1))
males = [r["patient_id"] for r in records if r["sex"] == "M"]
print("Male patients:", males)

with open("patients.csv", "a", newline="") as f:
    csv.writer(f).writerow(["P05", "F", "38", "121"])
with open("patients.csv") as f:
    print(f.read())
```

Output:

```text
Records: 4
Valid SBP values: [118, 142, 126] mean 128.7
Male patients: ['P02', 'P04']
patient_id,sex,age,sbp
P01,F,34,118
P02,M,51,142
P03,F,47,
P04,M,29,126
P05,F,38,121
```

Steps shown: create → read (`DictReader`) → count records → handle a missing value → compute a mean → filter by a category → append (`"a"` mode) → read the whole file. For larger tables the Pandas library (Unit 4) does all of this in fewer lines.

## Remember

- List `[ ]` mutable; tuple `( )` immutable; dictionary `{key: value}` looked up by key; set `{ }` unique items.
- Index from 0, negative index from the end; slice `[start:stop:step]` excludes `stop`.
- List methods: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`, `index`, `count`.
- Dictionary: `d[key]`, `d.get(key, default)`, `keys()`, `values()`, `items()`, `update()`, `del`.
- NumPy arrays hold one data type and do vectorised (element-wise) arithmetic; create with `np.array`, `np.arange`, `np.linspace`, `np.zeros`.
- `np.array([1, 2]) * 2` gives `[2 4]`; `[1, 2] * 2` gives `[1, 2, 1, 2]`.
- Use `with open(...)` so files close automatically; modes `r`, `w` (overwrites), `a` (appends).
- CSV = plain-text table; `csv.reader` gives lists, `csv.DictReader` gives dictionaries; values come back as strings.
- Structured data: rows = records, columns = variables; keep units in names and de-identify patient data.
