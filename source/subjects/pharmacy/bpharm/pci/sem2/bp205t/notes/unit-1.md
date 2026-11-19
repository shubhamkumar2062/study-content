# Unit 1: Number systems and the concept of information systems

A computer stores everything (a patient's name, a drug's dose, a chromatogram) as patterns of 0 and 1. The first half of this unit shows how numbers are written in the binary, octal, decimal and hexadecimal systems, how to convert between them and how a computer adds, subtracts, multiplies and divides in binary. The second half explains how a useful computer system is planned and built: gathering information, checking feasibility, drawing data flow diagrams, writing process specifications, designing inputs and outputs, and managing the project through its life cycle.

## 1.1 What a number system is

A **number system** is a way of writing numbers with a fixed set of symbols (digits). Every positional number system has a **base** (or radix): the number of different digits it uses. The value of a digit depends on its **position**: each position is a power of the base.

| System | Base | Digits used | Example | Where it is used |
| --- | --- | --- | --- | --- |
| Binary | 2 | 0, 1 | 1011₂ | Inside every computer (on/off, high/low voltage) |
| Octal | 8 | 0–7 | 157₈ | Short way of writing binary (3 bits per digit); file permissions in Unix |
| Decimal | 10 | 0–9 | 925₁₀ | Everyday counting |
| Hexadecimal | 16 | 0–9, A–F (A = 10 … F = 15) | 3F₁₆ | Memory addresses, colour codes in web pages (#FF0000), error codes |

**Key terms**

- **Bit** — one binary digit (0 or 1).
- **Nibble** — 4 bits. **Byte** — 8 bits (can hold 256 different values, 0–255).
- **MSB** (most significant bit) — the leftmost bit; **LSB** (least significant bit) — the rightmost bit.
- **Word** — the number of bits a processor handles at once (for example 32 or 64).

**Place values (weights)**

```text
Decimal   :  10^3  10^2  10^1  10^0 . 10^-1  10^-2
              1000   100    10     1 .  0.1    0.01

Binary    :   2^4   2^3   2^2   2^1   2^0 . 2^-1  2^-2  2^-3
               16     8     4     2     1 .  0.5  0.25  0.125

Octal     :   8^2   8^1   8^0          Hexadecimal :  16^2  16^1  16^0
               64     8     1                           256    16     1
```

Why binary? An electronic switch has two reliable states (on and off). Two states are easy to make, store and read without error, so the computer works in base 2. Octal and hexadecimal exist because long binary strings are hard for people to read: one octal digit stands for exactly 3 bits and one hexadecimal digit for exactly 4 bits.

**The first 16 numbers in all four systems** (learn this table; it makes every conversion quick):

| Decimal | Binary | Octal | Hex | Decimal | Binary | Octal | Hex |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0000 | 0 | 0 | 8 | 1000 | 10 | 8 |
| 1 | 0001 | 1 | 1 | 9 | 1001 | 11 | 9 |
| 2 | 0010 | 2 | 2 | 10 | 1010 | 12 | A |
| 3 | 0011 | 3 | 3 | 11 | 1011 | 13 | B |
| 4 | 0100 | 4 | 4 | 12 | 1100 | 14 | C |
| 5 | 0101 | 5 | 5 | 13 | 1101 | 15 | D |
| 6 | 0110 | 6 | 6 | 14 | 1110 | 16 | E |
| 7 | 0111 | 7 | 7 | 15 | 1111 | 17 | F |

## 1.2 Conversions

### Decimal to binary (whole number): repeated division by 2

Divide by 2, write the remainder, keep dividing the quotient until it becomes 0. Read the remainders **from bottom to top**.

**Example: 25₁₀ to binary**

```text
25 ÷ 2 = 12  remainder 1   (LSB)
12 ÷ 2 =  6  remainder 0
 6 ÷ 2 =  3  remainder 0
 3 ÷ 2 =  1  remainder 1
 1 ÷ 2 =  0  remainder 1   (MSB)
Read upward:  25₁₀ = 11001₂
Check: 16 + 8 + 0 + 0 + 1 = 25
```

### Decimal fraction to binary: repeated multiplication by 2

Multiply the fraction by 2; the whole-number part (0 or 1) is the next bit. Continue with the fraction part. Read the bits **from top to bottom**.

**Example: 0.625₁₀**: 0.625 × 2 = 1.25 → 1; 0.25 × 2 = 0.5 → 0; 0.5 × 2 = 1.0 → 1. So 0.625₁₀ = 0.101₂. Some fractions (like 0.1₁₀) never end in binary; stop after the number of places asked.

### Binary to decimal: multiply each bit by its weight and add

**Example: 101101₂** = 1×32 + 0×16 + 1×8 + 1×4 + 0×2 + 1×1 = **45₁₀**

**Example with a fraction: 1011.101₂** = 8 + 0 + 2 + 1 + 0.5 + 0 + 0.125 = **11.625₁₀**

### Decimal to octal and decimal to hexadecimal

Same as decimal to binary, but divide by 8 or by 16.

```text
156 to octal              2470 to hexadecimal
156 ÷ 8 = 19  r 4         2470 ÷ 16 = 154  r 6
 19 ÷ 8 =  2  r 3          154 ÷ 16 =   9  r 10 → A
  2 ÷ 8 =  0  r 2            9 ÷ 16 =   0  r 9
156₁₀ = 234₈              2470₁₀ = 9A6₁₆
Check: 2×64 + 3×8 + 4     Check: 9×256 + 10×16 + 6
       = 156                     = 2470
```

### Octal or hexadecimal to decimal

Multiply each digit by its place value and add. **1A3₁₆** = 1×256 + 10×16 + 3 = **419₁₀**. **234₈** = 2×64 + 3×8 + 4 = **156₁₀**.

### Octal ↔ binary (groups of 3)

- Octal to binary: write each octal digit as 3 bits. **357₈** → 011 101 111 → **11101111₂** (= 239₁₀).
- Binary to octal: group bits in threes **from the right** (add leading zeros), then write each group as one digit. **1101011₂** → 001 101 011 → **153₈** (= 107₁₀).

### Hexadecimal ↔ binary (groups of 4)

- Hex to binary: each hex digit becomes 4 bits. **2F₁₆** → 0010 1111 → **101111₂** (= 47₁₀).
- Binary to hex: group in fours from the right. **10111010₂** → 1011 1010 → **BA₁₆** (= 186₁₀).

### Octal ↔ hexadecimal

Go through binary. **745₈** → 111 100 101 → regroup in fours from the right: 0001 1110 0101 → **1E5₁₆**. Check: 745₈ = 448 + 32 + 5 = 485; 1E5₁₆ = 256 + 224 + 5 = 485.

## 1.3 Binary arithmetic

### Binary addition

| A | B | Sum | Carry |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 + 1 + 1 (with carry) | | 1 | 1 |

**Example: 1011 + 1101 (11 + 13)**

```text
  carry   1 1 1 1
            1 0 1 1
          + 1 1 0 1
          ---------
          1 1 0 0 0      = 24₁₀
```

**Example: 101101 + 11011 (45 + 27)** = **1001000₂** = 72₁₀.

### Binary subtraction (direct method)

Rules: 0 − 0 = 0, 1 − 0 = 1, 1 − 1 = 0, 0 − 1 = 1 with a **borrow** of 1 from the next column (a borrowed 1 is worth 2 in the current column). Example: 1101 − 1010 = 0011 (13 − 10 = 3).

Computers do not subtract this way. They **add the complement** of the number being subtracted, so the same adder circuit does both jobs.

### One's complement method

**One's complement** of a binary number = change every 0 to 1 and every 1 to 0. (1's complement of 1010 is 0101.)

To find A − B (both with the same number of bits):

1. Take the 1's complement of B.
2. Add it to A.
3. **If there is a carry out** of the leftmost bit, remove it and add 1 to the result (the **end-around carry**). The answer is positive.
4. **If there is no carry**, the answer is negative: take the 1's complement of the sum and put a minus sign.

```text
Example 1: 1101 − 1010  (13 − 10)
1's complement of 1010 = 0101
  1101 + 0101 = 1 0010   → carry 1
  0010 + 1 (end-around) = 0011  → +3

Example 2: 1010 − 1101  (10 − 13)
1's complement of 1101 = 0010
  1010 + 0010 = 1100     → no carry → negative
  1's complement of 1100 = 0011 → answer −0011 = −3
```

### Two's complement method

**Two's complement** = 1's complement + 1. (2's complement of 1010 is 0101 + 1 = 0110.) A quick way: copy bits from the right up to and including the first 1, then invert all the remaining bits.

To find A − B:

1. Take the 2's complement of B.
2. Add it to A.
3. **If there is a carry**, discard it; the result is positive.
4. **If there is no carry**, the result is negative: take the 2's complement of the sum and put a minus sign.

```text
Example 1: 110110 − 101011  (54 − 43)
2's complement of 101011 = 010100 + 1 = 010101
  110110 + 010101 = 1 001011  → discard carry → 001011 = +11

Example 2: 1010 − 1101  (10 − 13)
2's complement of 1101 = 0010 + 1 = 0011
  1010 + 0011 = 1101         → no carry → negative
  2's complement of 1101 = 0011 → answer −3
```

**Why 2's complement is preferred:** there is only one zero (1's complement has +0 and −0), and there is no end-around carry step, so the circuit is simpler. Modern computers store negative whole numbers in 2's complement form.

### Binary multiplication

Rules: 0 × 0 = 0, 0 × 1 = 0, 1 × 0 = 0, 1 × 1 = 1. Multiply as in decimal: write a shifted copy of the multiplicand for each 1 in the multiplier, then add.

```text
      1 0 1 1      (11)
    ×   1 0 1      (5)
    ---------
      1 0 1 1
    0 0 0 0        (shifted one place)
  1 0 1 1          (shifted two places)
  -----------
  1 1 0 1 1 1      = 55₁₀
```

### Binary division

Long division as in decimal: at each step, if the divisor fits into the bits brought down, write 1 and subtract; otherwise write 0 and bring down the next bit.

```text
Example: 110110 ÷ 110  (54 ÷ 6)
110 into 110 → 1, remainder 0
bring 1 → 1   → 0
bring 1 → 11  → 0
bring 0 → 110 → 1, remainder 0
Quotient = 1001 (9), remainder 0

Example: 11011 ÷ 101  (27 ÷ 5)
101 into 110 → 1, remainder 1
bring 1 → 11  → 0
bring 1 → 111 → 1, remainder 10
Quotient = 101 (5), remainder 10 (2)
```

Always check your answer by converting to decimal.

## 1.4 Data, information and information systems

- **Data** — raw facts with no context: "120", "Paracetamol", "15/03".
- **Information** — data that is processed, organised and given meaning: "Paracetamol 500 mg tablets: 120 strips in stock, expiring 15/03". Information helps in a decision.
- **System** — a set of parts working together towards a goal, with input, processing, output, feedback and control.
- **Information system (IS)** — an organised combination of **people, hardware, software, data, procedures and networks** that collects, processes, stores and distributes information to support operations and decisions.

```text
        INPUT  ───►  PROCESSING  ───►  OUTPUT
   (prescriptions,   (check, calculate,   (labels, bills,
    stock entries)    sort, store)         reports)
          ▲                                   │
          └──────────── FEEDBACK ◄────────────┘
                     (control and correction)
```

**Types of information systems**

| Type | Who uses it | Pharmacy example |
| --- | --- | --- |
| Transaction processing system (TPS) | Front-line staff | Billing and dispensing at the pharmacy counter |
| Management information system (MIS) | Middle managers | Monthly consumption and expiry reports |
| Decision support system (DSS) | Managers, clinicians | Choosing reorder quantity; dose-adjustment tools |
| Executive information system (EIS) | Top management | Sales dashboards of a pharma company |
| Expert system | Specialists | Drug–drug interaction alerts based on stored rules |

**Software** is the set of programs that tells the hardware what to do.

- **System software** runs the computer: operating systems (Windows, Linux, Android), device drivers, utilities, compilers.
- **Application software** does a user's job: word processors, spreadsheets, database programs, pharmacy billing software, hospital information systems.

## 1.5 Information gathering

Before building a system, the analyst must learn how the work is done now and what users need. Methods (fact-finding techniques):

| Method | How | Good for | Limitation |
| --- | --- | --- | --- |
| Interviews | Face-to-face questions with users and managers | Detailed, in-depth needs; clarifying doubts | Time-consuming; depends on the person |
| Questionnaires | Printed or online forms | Many users, spread out; anonymous opinions | Low response; no follow-up questions |
| Observation | Watching the work being done | Seeing the real process, not the described one | People may behave differently when watched |
| Record review | Studying existing forms, registers, reports | Knowing what data exist | Records may be out of date |
| Group meetings / joint application development (JAD) | Users and developers in workshops | Quick agreement on requirements | Needs good coordination |
| Prototyping | Showing a working model | Users see and correct the design early | Users may mistake it for the final system |

## 1.6 Requirement analysis and feasibility analysis

**Requirement analysis** turns the gathered facts into a clear list of what the system must do.

- **Functional requirements** — what the system does: "record each prescription", "warn when stock falls below the reorder level", "print a drug label".
- **Non-functional requirements** — how well it does it: speed, security (passwords, user levels), reliability, ease of use, backup.

The result is written in a **software requirement specification (SRS)** document, agreed by users and developers.

**Feasibility analysis** asks: *should this system be built?* A feasibility study looks at five areas (often remembered as **TELOS**):

| Feasibility | Question asked |
| --- | --- |
| Technical | Is the hardware, software and skill available to build and run it? |
| Economic (cost–benefit) | Do the benefits (saved time, fewer errors, less wastage) exceed the cost? |
| Legal | Does it follow laws on records, privacy and drug regulations? |
| Operational | Will the staff accept and use it? Does it fit the way they work? |
| Schedule | Can it be finished in the time available? |

The outcome is a **feasibility report** recommending go, change or stop.

## 1.7 Data flow diagrams (DFD)

A **DFD** is a picture of how data move through a system: where they come from, which processes change them, where they are stored and where they go. It shows **what** happens to data, not the order or timing.

**Four symbols** (Gane–Sarson or Yourdon–DeMarco notation):

| Symbol | Meaning | Drawn as |
| --- | --- | --- |
| External entity | A person or system outside that sends or receives data (patient, doctor, supplier) | Square or rectangle |
| Process | Work that changes data (verify prescription, calculate bill) | Circle (Yourdon) or rounded rectangle (Gane–Sarson), numbered |
| Data store | Data held for later use (drug master file, patient file) | Open-ended rectangle or two parallel lines |
| Data flow | Data moving between the others | Arrow with a label |

**Levels of DFD**

- **Context diagram (level 0)** — the whole system as one process, with all external entities.
- **Level 1** — the main process broken into its major sub-processes and data stores.
- **Level 2 and below** — each sub-process broken further, as needed.

**Rules:** every process must have at least one input and one output; data cannot flow directly between two entities or two stores without a process; label every flow.

```text
Context diagram: pharmacy dispensing system

 ┌─────────┐  prescription   ┌───────────────┐   bill, label   ┌─────────┐
 │ PATIENT │ ──────────────► │   0           │ ──────────────► │ PATIENT │
 └─────────┘                 │  PHARMACY     │                 └─────────┘
 ┌─────────┐ purchase order  │  DISPENSING   │  invoice, stock ┌──────────┐
 │SUPPLIER │ ◄────────────── │  SYSTEM       │ ◄────────────── │ SUPPLIER │
 └─────────┘                 └───────────────┘                 └──────────┘

Level 1 (part)
 prescription → (1.0 Verify Rx) → (2.0 Dispense and label) → (3.0 Prepare bill) → patient
                                         │                         │
                                ║ D1 Drug stock ║         ║ D2 Sales record ║
```

## 1.8 Process specifications

A **process specification** (process description) describes the logic inside each lowest-level process of the DFD so a programmer can code it. Tools:

1. **Structured English** — plain English with a few keywords (IF, THEN, ELSE, DO WHILE, REPEAT).

   ```text
   FOR each item on the prescription
       IF stock quantity >= quantity prescribed
           THEN dispense and reduce stock
           ELSE mark item "not available" and inform pharmacist
       IF stock quantity < reorder level
           THEN add item to purchase list
   ```

2. **Decision table** — a grid of conditions and actions for every combination (useful when many conditions apply).

   | Conditions / actions | Rule 1 | Rule 2 | Rule 3 |
   | --- | --- | --- | --- |
   | Valid prescription? | Y | Y | N |
   | Item in stock? | Y | N | — |
   | Dispense | X | | |
   | Offer substitute / order | | X | |
   | Return to patient | | | X |

3. **Decision tree** — the same logic drawn as branches.
4. **Pseudocode** — program-like steps without the exact syntax of a language.

## 1.9 Input and output design

**Input design** decides how data enter the system so that entry is fast and errors are few.

- Use screens that look like the paper form; group related fields.
- Use drop-down lists, check boxes and default values (today's date) instead of typing.
- **Validation checks:** range check (age 0–120), type check (numbers only in quantity), presence check (required fields), format check (date dd/mm/yyyy), lookup check (drug must exist in the drug master), check digits on codes.
- Use barcode scanners to avoid typing drug codes.

**Output design** decides what the user receives.

- Types: screen display, printed reports, labels, bills, alerts, e-mails, files for other systems.
- Good output is accurate, timely, short, clearly headed, and given only to people who need it (summary report for managers, detailed report for staff, exception report for expired stock).

## 1.10 Process life cycle (system development life cycle, SDLC)

The **SDLC** is the series of stages through which a system is planned, built, used and improved.

```text
 1 Planning / problem definition
          ↓
 2 Feasibility study
          ↓
 3 System analysis (information gathering, requirements, DFD)
          ↓
 4 System design (database, input/output screens, process specifications)
          ↓
 5 Development / coding
          ↓
 6 Testing (unit → integration → system → user acceptance)
          ↓
 7 Implementation (installation, data conversion, training, changeover)
          ↓
 8 Maintenance and review  ──► feeds back into planning for the next version
```

**Changeover methods during implementation:** direct (old system stopped at once), parallel (old and new run together for a time — safest), pilot (one department first), phased (part by part).

**Models of the SDLC:** the **waterfall model** (each stage finished before the next; simple, but late changes are costly), the **prototype model**, the **spiral model** (repeated cycles with risk analysis) and **agile** methods (small parts delivered every few weeks with user feedback).

**Types of maintenance:** corrective (fix errors), adaptive (adjust to new rules or hardware, such as a GST change), perfective (improve features) and preventive.

## 1.11 Planning and managing the project

A software project has limited time, money and people, so it must be managed.

- **Define scope** — what is included and what is not.
- **Break work into tasks** (work breakdown structure) and estimate time and cost for each.
- **Schedule** — a **Gantt chart** shows tasks as bars against a timeline; **PERT/CPM** network charts show which tasks depend on others and find the **critical path** (the longest chain, which decides the total time).
- **Allocate resources** — people, computers, budget.
- **Manage risk** — list what can go wrong (staff leave, data loss) and plan for it.
- **Monitor and control** — compare progress with the plan, hold review meetings, handle change requests.
- **Document** everything and close the project with a review.

```text
Gantt chart (weeks)        1   2   3   4   5   6   7   8
Analysis                  ███ ███
Design                            ███ ███
Coding                                    ███ ███
Testing                                           ███
Implementation and training                           ███
```

## Remember

- Base 2, 8, 10 and 16; 1 octal digit = 3 bits, 1 hex digit = 4 bits.
- Decimal to binary: divide by 2, read remainders upward; fraction: multiply by 2, read downward.
- 1's complement = invert bits; 2's complement = 1's complement + 1. In 1's complement subtraction add the end-around carry; in 2's complement discard it. No carry means the answer is negative.
- Information system = people + hardware + software + data + procedures + network.
- Feasibility: technical, economic, legal, operational, schedule (TELOS).
- DFD symbols: external entity, process, data store, data flow; levels start with the context diagram.
- Process specifications: structured English, decision tables, decision trees, pseudocode.
- SDLC: planning → feasibility → analysis → design → coding → testing → implementation → maintenance.
- Project management: scope, schedule (Gantt, PERT/CPM, critical path), resources, risk, monitoring.
