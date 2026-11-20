# How to use this guide

BP101T is a programming subject, so you learn it by **typing and running code**, not only by reading. Install Python with Jupyter Notebook (Anaconda is the easiest route) or use VS Code, then study one unit at a time: read the notes, type every code example yourself, check that your output matches the output shown, change a number and predict the new output before running it. After that, answer the question bank on paper — in the exam you write code by hand, so practise writing it neatly with correct indentation.

Every code example in these notes was run in Python 3 and its output is copied exactly. Pandas examples were run with Pandas 3; with Pandas 2 the only visible difference is that `info()` shows text columns as `object` instead of `str`. All concentration, weight and dosage numbers are made-up practice values chosen to show the arithmetic — they are not doses or data of any real medicine.

The five units follow the five units of the PCI B.Pharm Syllabus 2026 (NEP 2020) for BP101T exactly; no unit has been split or merged.

**End-semester paper (30 marks, 1.5 hours).** This follows the PCI end-semester question paper pattern for 2-credit courses (Table XV of the 2026 syllabus). Confirm the exact pattern with your university.

| Section | What it asks | Marks |
| --- | --- | --- |
| A | Multiple choice questions — answer all 10 | 10 × 1 = 10 |
| B | Short answers — answer any 5 of 7 | 5 × 2 = 10 |
| C | Long answers — answer any 2 of 3 | 2 × 5 = 10 |

The course carries 50 marks in all: 20 for sessional (internal) assessment and 30 for this end-semester paper. In the question bank "short" questions are worth 2 marks and "long" questions 5 marks, matching the paper.

**Probability ratings**

- **High** — a core topic that is very likely to be asked in some form; prepare a full answer with a code example.
- **Medium** — likely as part of a question or as an MCQ.
- **Low** — less common, but good for MCQs and as a backup choice.

These ratings are estimates from syllabus weight and the kind of questions usually set in introductory programming papers. This is a new course from 2026-27, so there are no past papers yet; treat the ratings as a guide, not a promise.

**Where the marks are likely to come from**

| Unit | Topics to prepare first |
| --- | --- |
| 1 Introduction | Features of Python, IDEs and their advantages, data types and type casting, operators (`/`, `//`, `%`, `**`), `input()` returning a string, string methods and slicing, pip install/uninstall |
| 2 Control structures | if / if-else / if-elif-else with a program, for vs while, break vs continue, defining a function with arguments and return, BMI and dosage-calculation programs |
| 3 Data structures | List vs tuple vs dictionary, indexing and slicing, list and dictionary methods, NumPy arrays vs lists, reading and writing CSV files, structured datasets |
| 4 Pandas | Series vs DataFrame, `read_csv`/`read_excel`, `head`/`tail`/`info`/`describe`, missing values (`isna`, `dropna`, `fillna`), filtering with conditions, `groupby` |
| 5 Matplotlib | Steps of a plot, labels/titles/legends, line, histogram, scatter and box plots with uses, concentration–time curves (oral vs IV), calibration curve, dissolution profile, interpreting a plot |

**Scoring tips for this subject**

1. **Write code inside your answer.** A 5-mark answer should have a definition, 3–5 points of explanation, a short program with correct indentation, and its output. Examiners give marks for working code.
2. **Show the output** under each program (write "Output:" and the result). Trace loops step by step if asked to predict output.
3. **Indent consistently** (4 spaces) and end `if`, `for`, `while` and `def` lines with a colon — the most common errors in handwritten code.
4. **Use pharmacy examples**: BMI, unit conversion, calibration curve, tablet weights, PK data, ADR counts. They show you understand why the course is taught.
5. **Learn the comparison tables** (list vs tuple, for vs while, break vs continue, Series vs DataFrame, `loc` vs `iloc`, histogram vs bar chart, `dropna` vs `fillna`). "Differentiate" questions are common for 2 and 5 marks.
6. **Name functions exactly** (`describe()`, `value_counts()`, `groupby()`, `plt.xlabel()`); small spelling differences lose marks in MCQs.
7. For plot questions, **sketch the expected graph** with labelled axes and units, then write the code and a two-line interpretation.
8. 2-mark answers: one-line definition + one example or the syntax. Do not write a page.
