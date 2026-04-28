# CS50P Week 07 Regular Expressions

This folder contains my solutions for regular expression exercises from **CS50’s Introduction to Programming with Python**.

## Purpose

These exercises are part of my **Phase 01: Python** foundation in my AI/ML roadmap.  
The goal is to strengthen pattern matching, input validation, text parsing, data extraction, testing, and working with third-party validation libraries before moving to more advanced programming concepts.

Regular expressions are useful for finding, validating, and extracting structured patterns from text, such as IP addresses, URLs, timestamps, words, and email addresses.

## Exercises Included

### 1. NUMB3RS

**Folder:** `numb3rs/`  
**Files:** `numb3rs.py`, `test_numb3rs.py`

Validates whether an input string is a valid IPv4 address.

The program checks:

- correct IPv4 format
- exactly four numeric parts
- dots between each part
- each number between `0` and `255`
- invalid values above `255`
- invalid text input
- invalid leading zeros
- valid local and public-style IPv4 addresses

The test file checks valid and invalid IPv4 address cases using `pytest`.

---

### 2. Watch on YouTube

**Folder:** `watch/`  
**File:** `watch.py`

Extracts a YouTube embed URL from an HTML iframe and converts it into a shorter shareable `youtu.be` URL.

The program practices:

- searching HTML text with regular expressions
- matching iframe elements
- extracting the `src` attribute
- identifying YouTube embed URLs
- using capturing groups
- returning `None` when no valid YouTube embed URL exists
- converting long embed URLs into short YouTube URLs

---

### 3. Working 9 to 5

**Folder:** `working/`  
**Files:** `working.py`, `test_working.py`

Converts time ranges from 12-hour format to 24-hour format.

The program accepts formats such as:

- `9:00 AM to 5:00 PM`
- `9 AM to 5 PM`
- `9:00 AM to 5 PM`
- `9 AM to 5:00 PM`

The program checks:

- correct input format
- valid hour values
- valid minute values
- missing minutes
- AM to PM conversion
- PM to AM conversion
- `12 AM` conversion to `00`
- `12 PM` remaining as `12`
- invalid separators
- invalid time ranges

The test file checks valid conversions and invalid inputs using `pytest`.

---

### 4. Regular, um, Expressions

**Folder:** `um/`  
**Files:** `um.py`, `test_um.py`

Counts how many times `"um"` appears in text as a standalone word.

The program practices:

- using word boundaries with `\b`
- matching whole words only
- ignoring case with `re.IGNORECASE`
- avoiding substring matches inside larger words
- counting regex matches with `re.findall()`

The program should count:

- `um`
- `um?`
- `hello, um, world`
- `Um, thanks, um...`

The program should not count:

- `yummy`
- `album`
- `umbrella`

The test file checks zero, one, and multiple valid matches using `pytest`.

---

### 5. Response Validation

**Folder:** `response/`  
**File:** `response.py`

Validates whether an input email address is syntactically valid using a third-party Python library instead of regular expressions.

The program practices:

- validating email input
- using external Python packages
- handling validation errors
- printing `Valid` or `Invalid`
- avoiding manual email regex patterns
- using library-based validation for cleaner code

This exercise uses the `validator-collection` package.

## Skills Practiced

- using the `re` module
- writing raw regex strings with `r"..."`
- using `re.search()`
- using `re.findall()`
- using capturing groups
- using optional groups
- using anchors `^` and `$`
- using word boundaries `\b`
- using character classes
- using quantifiers such as `{1,3}` and `?`
- using non-capturing groups `(?:...)`
- validating structured text input
- extracting data from strings
- parsing URLs from HTML
- converting text formats
- raising `ValueError`
- testing with `pytest`
- using `pytest.raises()`
- installing and using third-party libraries
- validating email addresses with `validator-collection`
- preparing programs for `check50` and `submit50`

## Why This Matters

These exercises build the base for:

- validating user input
- cleaning text data
- extracting useful information from strings
- parsing logs, URLs, emails, and structured text
- writing safer command-line programs
- testing functions properly
- using libraries instead of manually solving every validation problem
- preparing for automation, data processing, and AI/ML workflows

In AI/ML work, regular expressions are useful because raw datasets often contain messy text, file paths, logs, URLs, timestamps, email addresses, labels, and inconsistent formatting.  
These exercises help build the foundation for cleaning text data, validating inputs, extracting patterns, and preparing raw data before analysis or model training.

## Folder Structure

```text
cs50p-week7-regex/
│
├── numb3rs/
│   ├── numb3rs.py
│   └── test_numb3rs.py
│
├── watch/
│   └── watch.py
│
├── working/
│   ├── working.py
│   └── test_working.py
│
├── um/
│   ├── um.py
│   └── test_um.py
│
└── response/
    └── response.py
```
