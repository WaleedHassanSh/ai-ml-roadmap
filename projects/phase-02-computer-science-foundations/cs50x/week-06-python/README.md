# CS50x Week 06 — Python

This folder contains my solutions for **CS50x Week 6: Python**.

## Folder Path

```text
projects/phase-02-computer-science-foundations/cs50x/week-06-python/
```

## Contents

```text
week-06-python/
├── README.md
├── sentimental-hello/
│   └── hello.py
├── sentimental-mario-less/
│   └── mario.py
├── sentimental-mario-more/
│   └── mario.py
├── sentimental-cash/
│   └── cash.py
├── sentimental-credit/
│   └── credit.py
├── sentimental-readability/
│   └── readability.py
└── dna/
    ├── dna.py
    ├── databases/
    │   ├── small.csv
    │   └── large.csv
    └── sequences/
        ├── 1.txt
        ├── 2.txt
        ├── ...
        └── 20.txt
```

## Problems Completed

| Problem | Folder | File | Description |
|---|---|---|---|
| Hello, Again | `sentimental-hello/` | `hello.py` | Prompts the user for their name and prints a greeting. |
| Mario Less | `sentimental-mario-less/` | `mario.py` | Prints a right-aligned half-pyramid of height 1 to 8. |
| Mario More | `sentimental-mario-more/` | `mario.py` | Prints two half-pyramids separated by two spaces. |
| Cash | `sentimental-cash/` | `cash.py` | Calculates the minimum number of coins needed for change. |
| Credit | `sentimental-credit/` | `credit.py` | Validates credit card numbers using Luhn’s algorithm. |
| Readability | `sentimental-readability/` | `readability.py` | Calculates reading grade level using the Coleman-Liau index. |
| DNA | `dna/` | `dna.py` | Identifies a DNA profile using STR counts from a CSV database. |

## Key Concepts Practiced

- Python input and output
- Loops and conditionals
- Exception handling
- String methods
- Arithmetic and rounding
- Greedy algorithms
- Luhn’s checksum algorithm
- File handling
- CSV parsing with `csv.DictReader`
- Command-line arguments with `sys.argv`
- Basic pattern matching in DNA sequences

## How to Run

Run each program from inside its own folder.

Example:

```bash
cd sentimental-hello
python hello.py
```

For DNA:

```bash
cd dna
python dna.py databases/small.csv sequences/1.txt
```

## Check50 Commands

```bash
check50 cs50/problems/2026/x/sentimental/hello
check50 cs50/problems/2026/x/sentimental/mario/less
check50 cs50/problems/2026/x/sentimental/mario/more
check50 cs50/problems/2026/x/sentimental/cash
check50 cs50/problems/2026/x/sentimental/credit
check50 cs50/problems/2026/x/sentimental/readability
check50 cs50/problems/2026/x/dna
```

## Style50 Commands

Run `style50` inside the relevant problem folder:

```bash
style50 hello.py
style50 mario.py
style50 cash.py
style50 credit.py
style50 readability.py
style50 dna.py
```

## Submit50 Commands

```bash
submit50 cs50/problems/2026/x/sentimental/hello
submit50 cs50/problems/2026/x/sentimental/mario/less
submit50 cs50/problems/2026/x/sentimental/mario/more
submit50 cs50/problems/2026/x/sentimental/cash
submit50 cs50/problems/2026/x/sentimental/credit
submit50 cs50/problems/2026/x/sentimental/readability
submit50 cs50/problems/2026/x/dna
```

## Notes

This README belongs directly inside the `week-06-python/` folder, not inside each individual problem folder.
