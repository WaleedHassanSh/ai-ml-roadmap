# CS50x Week 02 — Arrays

## Overview

This folder contains my solutions for **CS50x Week 02: Arrays** as part of my **AI/ML Roadmap — Phase 02: Computer Science Foundations**.

The goal of this week is to strengthen core C programming skills related to arrays, strings, command-line arguments, character processing, and modular problem solving. These concepts are important because C exposes low-level details that later help in understanding memory, data representation, algorithms, and efficient systems used in AI/ML engineering.

## Folder Structure

```text
week-02-arrays/
├── README.md
├── scrabble/
│   └── scrabble.c
├── readability/
│   └── readability.c
├── caesar/
│   └── caesar.c
└── substitution/
    └── substitution.c
```

## Problems Completed

### 1. Scrabble

**File:** `scrabble/scrabble.c`

This program calculates the Scrabble score of two players' words and prints the winner.

**Main concepts practiced:**

- Arrays
- Strings
- Character indexing
- ASCII arithmetic
- Functions
- Loops
- Conditional statements
- `isupper()` and `islower()`

**Key idea:**

Each alphabet letter has a fixed score stored in an integer array. The program converts each character into an array index by subtracting `'A'` for uppercase letters or `'a'` for lowercase letters.

Example:

```c
score += POINTS[word[i] - 'A'];
```

This maps:

```text
A -> 0
B -> 1
C -> 2
...
Z -> 25
```

---

### 2. Readability

**File:** `readability/readability.c`

This program calculates the approximate U.S. grade level needed to understand a text using the Coleman-Liau index.

**Main concepts practiced:**

- Strings
- Loops
- Helper functions
- Counting letters, words, and sentences
- Floating-point division
- Type casting
- `round()`
- `isalpha()` and `isspace()`

**Formula used:**

```text
index = 0.0588 * L - 0.296 * S - 15.8
```

Where:

- `L` = average number of letters per 100 words
- `S` = average number of sentences per 100 words

**Important detail:**

Integer division must be avoided when calculating `L` and `S`.

Correct approach:

```c
float L = (letters / (float) words) * 100;
float S = (sentences / (float) words) * 100;
```

---

### 3. Caesar

**File:** `caesar/caesar.c`

This program encrypts plaintext using Caesar's cipher. The user provides the encryption key as a command-line argument.

**Main concepts practiced:**

- Command-line arguments
- `argc` and `argv`
- Input validation
- `atoi()`
- Modular arithmetic
- Character rotation
- Case preservation
- Helper functions

**Key idea:**

Letters are rotated by the given key while wrapping around the alphabet using `% 26`.

Example:

```c
return ((((c - 'A') + key) % 26) + 'A');
```

This converts an uppercase character into a 0–25 range, applies the key, wraps it around, and converts it back to an uppercase ASCII character.

---

### 4. Substitution

**File:** `substitution/substitution.c`

This program encrypts plaintext using a substitution cipher. The user provides a 26-character key as a command-line argument.

**Main concepts practiced:**

- Command-line arguments
- Key validation
- Nested loops
- Duplicate checking
- Character substitution
- Case preservation
- `isalpha()`, `tolower()`, `toupper()`

**Key requirements:**

The key must:

- Contain exactly 26 characters
- Contain only alphabetic characters
- Contain each letter exactly once
- Work regardless of uppercase or lowercase key input

**Key idea:**

Each plaintext letter is converted into an index from 0 to 25, then replaced by the character at the same index in the key.

Example:

```c
return toupper(key[c - 'A']);
```

---

## Commands Used

### Compile

Run these commands inside each problem folder:

```bash
make scrabble
make readability
make caesar
make substitution
```

### Run

```bash
./scrabble
./readability
./caesar 13
./substitution NQXPOMAFTRHLZGECYJIUWSKDVB
```

### Check Correctness

```bash
check50 cs50/problems/2026/x/scrabble
check50 cs50/problems/2026/x/readability
check50 cs50/problems/2026/x/caesar
check50 cs50/problems/2026/x/substitution
```

### Check Style

```bash
style50 scrabble.c
style50 readability.c
style50 caesar.c
style50 substitution.c
```

### Submit

```bash
submit50 cs50/problems/2026/x/scrabble
submit50 cs50/problems/2026/x/readability
submit50 cs50/problems/2026/x/caesar
submit50 cs50/problems/2026/x/substitution
```

## What I Learned

- How strings work as arrays of characters in C
- How to access individual characters using index notation
- How ASCII values can be used in character arithmetic
- How arrays can store structured data such as letter scores
- How to validate command-line arguments
- How to write helper functions for cleaner program design
- How to preserve uppercase and lowercase letters during encryption
- How to use modular arithmetic for wraparound behavior
- How to use nested loops to detect duplicate characters
- How to break a larger problem into smaller functions

## Common Mistakes to Avoid

- Forgetting that strings are indexed from `0`
- Accessing an array outside its valid range
- Using integer division when floating-point division is required
- Forgetting to include required header files
- Not checking `argc` before accessing `argv[1]`
- Forgetting to validate every character in the key
- Not preserving letter case in Caesar and Substitution
- Accidentally changing non-alphabetic characters during encryption
- Forgetting the final newline after printing output

## AI/ML Connection

Although these programs are beginner C exercises, the concepts are directly useful for future AI/ML engineering.

Arrays and strings are fundamental data structures. Character processing appears in text preprocessing, tokenization, parsing, and data cleaning. Modular arithmetic is used in hashing, cryptography, indexing, and cyclic data structures. Command-line arguments are important for building reproducible scripts and machine learning experiments.

Understanding these low-level foundations makes it easier to reason about how data is stored, transformed, validated, and processed before it reaches higher-level AI/ML tools.

## Status

Completed as part of:

```text
AI/ML Roadmap
└── Phase 02 — Computer Science Foundations
    └── CS50x
        └── Week 02 — Arrays
```
