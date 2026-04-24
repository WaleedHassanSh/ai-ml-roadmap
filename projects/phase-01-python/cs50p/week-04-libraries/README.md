# CS50P Week 04 Libraries

This folder contains my solutions for library-based exercises from **CS50’s Introduction to Programming with Python**.

## Purpose

These exercises are part of my **Phase 01: Python** foundation in my AI/ML roadmap.  
The goal is to strengthen the use of Python libraries, command-line arguments, randomness, API requests, JSON parsing, and third-party packages before moving to more advanced programming concepts.

## Exercises Included

### 1. Emojize

**Folder:** `emojize/`  
**File:** `emojize.py`

Prompts the user for text and converts emoji codes or aliases such as `:thumbs_up:` into actual emoji using the `emoji` library.

### 2. FIGlet

**Folder:** `figlet/`  
**File:** `figlet.py`

Generates ASCII art from user input using the `pyfiglet` library. Supports random fonts or a specific font provided through command-line arguments.

### 3. Adieu

**Folder:** `adieu/`  
**File:** `adieu.py`

Prompts the user for names until end-of-input and then formats them into a grammatically correct farewell sentence using the `inflect` library.

### 4. Guessing Game

**Folder:** `game/`  
**File:** `game.py`

Prompts the user for a level, randomly generates a number, and repeatedly asks the user to guess until the correct answer is entered.

### 5. Little Professor

**Folder:** `professor/`  
**File:** `professor.py`

Generates ten random addition problems based on a selected difficulty level and scores the user based on correct answers.

### 6. Bitcoin Price Index

**Folder:** `bitcoin/`  
**File:** `bitcoin.py`

Uses a command-line argument and the CoinCap API to calculate the current USD value of a given number of Bitcoins.

## Skills Practiced

- importing and using Python libraries
- installing third-party packages with `pip`
- using `sys.argv` for command-line arguments
- validating command-line input
- using `sys.exit()` for controlled program exits
- generating random values with the `random` module
- using third-party libraries such as `emoji`, `pyfiglet`, and `inflect`
- making HTTP requests with the `requests` library
- handling `requests.RequestException`
- parsing JSON responses
- formatting currency output with commas and decimal places
- writing more modular programs with functions

## Why This Matters

These exercises build the base for:

- using external Python packages confidently
- writing command-line programs
- working with APIs and real-world data
- handling network/API failures safely
- parsing structured data such as JSON
- improving input validation and error handling
- preparing for later scripting, automation, data science, and AI/ML workflows

## How to Run

Open a terminal in the relevant folder and run:

```bash
python filename.py
```
