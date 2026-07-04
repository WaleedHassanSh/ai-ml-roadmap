# CS50x Week 05 — Data Structures

This folder contains my CS50x Week 05 Data Structures problem set solutions.

## Folder Structure

```text
week-05-data-structures/
├── README.md
├── inheritance/
│   └── inheritance.c
└── speller/
    ├── dictionary.c
    ├── dictionary.h
    ├── speller.c
    ├── Makefile
    ├── dictionaries/
    ├── keys/
    └── texts/
```

## Problems

### 1. Inheritance

**Folder:** `inheritance/`

**Main file:** `inheritance.c`

This problem simulates genetic inheritance of blood type alleles through a family tree.

#### Main concepts practiced

- Structs
- Pointers
- Dynamic memory allocation using `malloc`
- Recursive function calls
- Recursive memory freeing using `free`
- Tree-like data structures
- Random allele assignment

#### Main functions

- `create_family(int generations)`
  - Recursively creates a family tree.
  - Allocates memory for each person.
  - Assigns parents and alleles.

- `free_family(person *p)`
  - Recursively frees the memory allocated for each person and their ancestors.

- `print_family(person *p, int generation)`
  - Prints the family tree with indentation.

#### How to run

```bash
cd inheritance
make inheritance
./inheritance
```

#### Check correctness and style

```bash
check50 cs50/problems/2026/x/inheritance
style50 inheritance.c
```

---

### 2. Speller

**Folder:** `speller/`

**Main files:**

- `dictionary.c`
- `dictionary.h`
- `speller.c`
- `Makefile`

This problem implements a spell checker using a hash table.

The program loads a dictionary into memory, checks words from a text file, reports misspelled words, and frees all allocated memory.

#### Main concepts practiced

- Hash tables
- Linked lists
- Structs
- Pointers
- Dynamic memory allocation
- File I/O
- String comparison
- Case-insensitive checking
- Memory management
- Runtime performance

#### Main functions implemented in `dictionary.c`

- `load(const char *dictionary)`
  - Opens the dictionary file.
  - Reads each word.
  - Stores each word in a hash table.

- `hash(const char *word)`
  - Converts a word into a hash table index.

- `check(const char *word)`
  - Checks whether a word exists in the loaded dictionary.
  - Must be case-insensitive.

- `size(void)`
  - Returns the number of words loaded from the dictionary.

- `unload(void)`
  - Frees all memory allocated for the hash table.

#### How to compile

```bash
cd speller
make
```

#### How to run with the large dictionary

```bash
./speller texts/lalaland.txt
```

#### How to run with the small dictionary

```bash
./speller dictionaries/small texts/cat.txt
```

#### Compare with staff solution

```bash
./speller texts/lalaland.txt > student.txt
./speller50 texts/lalaland.txt > staff.txt
diff -y student.txt staff.txt
```

#### Check memory leaks

```bash
valgrind ./speller texts/cat.txt
```

Or with help50:

```bash
help50 valgrind ./speller texts/cat.txt
```

#### Check correctness and style

```bash
check50 cs50/problems/2026/x/speller
style50 dictionary.c
```

## Key Notes

- `inheritance` mainly tests recursion and memory management.
- `speller` mainly tests hash tables, linked lists, file reading, and performance.
- Do not edit `speller.c` or `Makefile` for Speller.
- Most Speller changes should be made in `dictionary.c`.
- Always run `valgrind` for Speller to confirm there are no memory leaks.

## Local Repo Path

```text
~/ai-ml-roadmap/projects/phase-02-computer-science-foundations/cs50x/week-05-data-structures/
```

## Status

| Problem | Status |
|---|---|
| Inheritance | Completed |
| Speller | Completed |
