# CS50P Week 06 File I/O

This folder contains my solutions for file input/output exercises from **CS50’s Introduction to Programming with Python**.

## Purpose

These exercises are part of my **Phase 01: Python** foundation in my AI/ML roadmap.  
The goal is to strengthen command-line argument handling, file reading/writing, CSV processing, image processing, error handling, and working with external Python libraries before moving to more advanced programming concepts.

## Exercises Included

### 1. Lines of Code

**Folder:** `lines/`  
**File:** `lines.py`

Counts the number of lines of code in a Python file, excluding blank lines and comments.

The program checks:

- too few command-line arguments
- too many command-line arguments
- invalid file extension
- missing file
- blank lines
- comment lines
- actual lines of code

### 2. Pizza Py

**Folder:** `pizza/`  
**File:** `pizza.py`

Reads a CSV file containing pizza menu data and prints it as a formatted ASCII table using the `tabulate` library.

The program practices:

- reading CSV files
- storing rows in a list
- separating headers from data
- formatting output with `tabulate`
- handling missing files
- validating `.csv` input

### 3. Scourgify

**Folder:** `scourgify/`  
**File:** `scourgify.py`

Cleans a CSV file by converting student names from `"last, first"` format into separate `first`, `last`, and `house` columns.

The program practices:

- reading CSV files with `csv.DictReader`
- writing CSV files with `csv.DictWriter`
- writing headers with `writeheader()`
- splitting and cleaning string data
- creating a new cleaned CSV file
- handling missing input files

### 4. CS50 P-Shirt

**Folder:** `shirt/`  
**File:** `shirt.py`

Overlays `shirt.png` on top of an input image after resizing and cropping the input image to match the shirt size.

The program practices:

- working with image files
- using the Pillow library
- opening images with `Image.open()`
- resizing and cropping with `ImageOps.fit()`
- overlaying transparent images with `paste()`
- saving processed images
- validating image extensions
- checking matching input/output extensions

## Skills Practiced

- reading files with `open()`
- writing files with `open(..., "w")`
- using `with` to safely handle files
- handling `FileNotFoundError`
- using `sys.argv`
- exiting programs with `sys.exit()`
- validating command-line arguments
- checking file extensions
- using `os.path.splitext()`
- reading CSV files with `csv.reader`
- reading structured CSV data with `csv.DictReader`
- writing CSV files with `csv.DictWriter`
- installing and using third-party libraries
- formatting tables with `tabulate`
- processing images with Pillow
- resizing, cropping, pasting, and saving images
- preparing programs for `check50` and `submit50`

## Why This Matters

These exercises build the base for:

- working with real files instead of only keyboard input
- cleaning and transforming structured data
- validating user input and file paths
- writing scripts that can be run from the terminal
- handling errors safely
- using external Python packages
- preparing for automation, data processing, and AI/ML workflows

In AI/ML work, file I/O is important because datasets are commonly stored in files such as CSV, JSON, images, text files, and logs.  
These exercises help build the foundation for reading datasets, cleaning data, validating files, preprocessing images, and saving processed outputs.

## How to Run

Open a terminal in the relevant folder and run the program with the required command-line arguments.

### Lines of Code

```bash
python lines.py filename.py
```
