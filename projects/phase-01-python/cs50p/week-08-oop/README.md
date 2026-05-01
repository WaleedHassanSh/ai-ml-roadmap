# CS50P Week 08 Object-Oriented Programming

This folder contains my solutions for object-oriented programming exercises from **CS50’s Introduction to Programming with Python**.

## Purpose

These exercises are part of my **Phase 01: Python** foundation in my AI/ML roadmap.  
The goal is to strengthen object-oriented programming, class design, method behavior, data validation, testing, date handling, third-party libraries, and PDF generation before moving to more advanced Python projects.

Object-oriented programming is useful for organizing code around objects that contain both data and behavior.  
It helps make programs more structured, reusable, testable, and easier to maintain.

## Exercises Included

### 1. Seasons of Love

**Folder:** `seasons/`  
**Files:** `seasons.py`, `test_seasons.py`

Converts a user’s date of birth into their age in minutes.

The program practices:

- accepting date input in `YYYY-MM-DD` format
- parsing dates safely
- using Python’s `datetime.date` class
- subtracting one date from another
- working with `timedelta` objects
- converting days into minutes
- converting numbers into English words
- using the `inflect` library
- handling invalid input with `sys.exit`
- writing testable helper functions

The test file checks date parsing, invalid formats, invalid dates, minute calculation, and word conversion using `pytest`.

---

### 2. Cookie Jar

**Folder:** `jar/`  
**Files:** `jar.py`, `test_jar.py`

Implements a cookie jar using a Python class.

The program practices:

- defining a custom class
- using `__init__`
- using `__str__`
- creating instance variables
- using instance methods
- using properties with `@property`
- using setters for validation
- validating object state
- raising `ValueError`
- depositing cookies
- withdrawing cookies
- preventing the jar from exceeding capacity
- preventing invalid withdrawals

The test file checks object initialization, string output, deposit behavior, withdrawal behavior, capacity validation, size validation, and invalid operations using `pytest`.

---

### 3. CS50 Shirtificate

**Folder:** `shirtificate/`  
**Files:** `shirtificate.py`, `shirtificate.png`, `shirtificate.pdf`

Generates a personalized CS50 shirtificate PDF using `fpdf2`.

The program practices:

- creating PDF files with Python
- using the `FPDF` class
- setting PDF orientation and page format
- adding pages to a PDF
- writing centered text
- adding images to a PDF
- positioning text and images
- setting font style and size
- setting text color
- creating a final output file
- working with external image assets

The program prompts the user for their name and places it on top of the CS50 shirt image in white text.

## Skills Practiced

- object-oriented programming
- defining classes
- creating objects
- using instance variables
- writing instance methods
- using `__init__`
- using `__str__`
- using `@property`
- using property setters
- validating data inside classes
- raising `ValueError`
- writing testable functions
- testing with `pytest`
- using `pytest.raises()`
- working with dates
- using `datetime.date`
- subtracting date objects
- working with `timedelta`
- converting numeric values into words
- using third-party Python libraries
- installing and using `inflect`
- installing and using `fpdf2`
- generating PDF files
- positioning text and images in PDFs
- preparing programs for `check50` and `submit50`

## Why This Matters

These exercises build the base for:

- designing clean Python classes
- modeling real-world objects in code
- keeping program state safe and valid
- separating logic into reusable functions
- writing tests for functions and classes
- handling dates and time-based calculations
- using third-party libraries effectively
- creating files programmatically
- generating reports, certificates, and documents with Python

In AI/ML work, object-oriented programming is useful because many machine learning tools are built around classes and objects.  
Models, datasets, data loaders, training configurations, pipelines, metrics, and experiment trackers often use object-oriented design.

These exercises also help build habits that matter in AI/ML engineering:

- validating input data
- testing behavior carefully
- organizing code into reusable components
- using external libraries instead of reinventing everything
- producing files and outputs programmatically

## Folder Structure

```text
week-08-oop/
│
├── seasons/
│   ├── seasons.py
│   └── test_seasons.py
│
├── jar/
│   ├── jar.py
│   └── test_jar.py
│
└── shirtificate/
    ├── shirtificate.py
    ├── shirtificate.png
    └── shirtificate.pdf
```
