# CS50P Week 05 Unit Tests

This folder contains my solutions and test files for unit-testing exercises from **CS50’s Introduction to Programming with Python**.

## Purpose

These exercises are part of my **Phase 01: Python** foundation in my AI/ML roadmap.  
The goal is to strengthen function-based programming, automated testing, assertions, exception testing, and debugging with `pytest` before moving to more advanced programming concepts.

## Exercises Included

### 1. Testing my twttr

**Folder:** `test_twttr/`  
**Files:** `twttr.py`, `test_twttr.py`

Reimplements the `twttr` program using a `shorten()` function and tests whether vowels are removed correctly from text.

### 2. Back to the Bank

**Folder:** `test_bank/`  
**Files:** `bank.py`, `test_bank.py`

Reimplements the bank greeting program using a `value()` function and tests whether greetings return the correct dollar amount.

### 3. Re-requesting a Vanity Plate

**Folder:** `test_plates/`  
**Files:** `plates.py`, `test_plates.py`

Reimplements the vanity plate validator using an `is_valid()` function and tests whether license plates follow all required rules.

### 4. Refueling

**Folder:** `test_fuel/`  
**Files:** `fuel.py`, `test_fuel.py`

Reimplements the fuel gauge program using `convert()` and `gauge()` functions and tests valid fractions, invalid input, rounding, and gauge output.

## Skills Practiced

- writing testable functions
- separating program logic from input/output
- returning values instead of printing inside helper functions
- importing functions from another Python file
- using `pytest`
- writing test functions that begin with `test_`
- using `assert` statements
- testing normal cases
- testing edge cases
- testing invalid input
- testing exceptions with `pytest.raises`
- checking whether tests catch intentional bugs
- preparing programs for `check50` and `submit50`

## Why This Matters

These exercises build the base for:

- writing more reliable Python programs
- checking code automatically instead of testing manually every time
- catching bugs early
- improving debugging skills
- designing cleaner function-based programs
- preparing for larger software projects
- writing safer scripts for automation, data science, and AI/ML workflows

In AI/ML work, unit testing is useful for checking data preprocessing, metrics, helper functions, API responses, and experiment logic before trusting the final results.

## How to Run

Open a terminal in the relevant folder and run:

```bash
pytest test_filename.py
```
