# CS50x Week 01 C

This folder contains my solutions for **CS50x Week 1: C** as part of **Phase 02: Computer Science Foundations** in my AI/ML roadmap.

Week 1 introduces the C programming language and builds the foundation for understanding how programs work closer to the machine. The main focus is on compiling code, using header files, writing functions, working with loops, conditionals, variables, input/output, and basic algorithmic problem solving.

## Purpose

The purpose of this week is to build a strong foundation in C programming before moving deeper into arrays, algorithms, memory, and data structures.

This week helps me practice:

- Writing and compiling C programs
- Understanding `main`, header files, and function prototypes
- Using `printf` for output
- Getting user input with CS50 functions like `get_string`, `get_int`, and `get_long`
- Using loops, conditionals, and functions
- Solving small problems step by step
- Applying basic greedy algorithms
- Validating numeric input and output formatting
- Preparing for lower-level CS topics useful for AI/ML systems, performance, and memory understanding

## Folder Structure

```text
week-01-c/
├── README.md
├── world/
│   └── hello.c
├── me/
│   └── hello.c
├── mario-less/
│   └── mario.c
├── mario-more/
│   └── mario.c
├── cash/
│   └── cash.c
└── credit/
    └── credit.c
```

## Problems Completed

| Problem | Folder | File | Main Concept |
|---|---|---|---|
| Hello, World | `world` | `hello.c` | Basic C program structure and output |
| Hello, It’s Me | `me` | `hello.c` | User input and formatted output |
| Mario Less | `mario-less` | `mario.c` | Loops, nested loops, and right-aligned patterns |
| Mario More | `mario-more` | `mario.c` | Nested loops and double pyramid construction |
| Cash | `cash` | `cash.c` | Greedy algorithm for minimum coins |
| Credit | `credit` | `credit.c` | Luhn’s algorithm and card type validation |

## Concepts Practiced

### Basic C Program Structure

Practiced writing C programs using:

- `#include <stdio.h>`
- `#include <cs50.h>`
- `int main(void)`
- Curly braces `{ }`
- Semicolons `;`
- `printf`

Example idea:

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

### Input and Output

Practiced taking input from the user and printing formatted output.

Important functions:

```c
get_string()
get_int()
get_long()
printf()
```

Example format specifiers:

```c
%s   // string
%i   // integer
%li  // long integer
```

### Loops

Used loops to repeat actions.

Types practiced:

```c
for loop
while loop
do while loop
```

The `do while` loop was especially useful for input validation because it runs at least once before checking the condition.

Example:

```c
int height;

do
{
    height = get_int("Height: ");
}
while (height < 1);
```

### Functions

Used helper functions to split programs into smaller parts.

Examples:

```c
void print_row(int spaces, int bricks);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);
```

This makes code easier to read, debug, and reuse.

### Greedy Algorithm

The `cash` problem used a greedy algorithm.

A greedy algorithm chooses the best immediate option at each step. For the cash problem, this means using the largest possible coin first:

1. Quarters: 25¢
2. Dimes: 10¢
3. Nickels: 5¢
4. Pennies: 1¢

For example, for 41 cents:

```text
41 - 25 = 16
16 - 10 = 6
6 - 5 = 1
1 - 1 = 0
```

Total coins:

```text
1 quarter + 1 dime + 1 nickel + 1 penny = 4 coins
```

### Luhn’s Algorithm

The `credit` problem used Luhn’s algorithm to validate credit card numbers.

Basic steps:

1. Starting from the second-to-last digit, multiply every other digit by 2.
2. Add the digits of those products.
3. Add the digits that were not multiplied by 2.
4. If the final total ends in 0, the number is valid.

The program then checks the card type:

- American Express: 15 digits, starts with `34` or `37`
- MasterCard: 16 digits, starts with `51`, `52`, `53`, `54`, or `55`
- Visa: 13 or 16 digits, starts with `4`

## How to Compile and Run

Go inside a problem folder first.

Example:

```bash
cd world
make hello
./hello
```

For Mario:

```bash
cd mario-less
make mario
./mario
```

For Cash:

```bash
cd cash
make cash
./cash
```

For Credit:

```bash
cd credit
make credit
./credit
```

## CS50 Commands Used

### Compile

```bash
make hello
make mario
make cash
make credit
```

### Run

```bash
./hello
./mario
./cash
./credit
```

### Check Correctness

```bash
check50 cs50/problems/2026/x/world
check50 cs50/problems/2026/x/me
check50 cs50/problems/2026/x/mario/less
check50 cs50/problems/2026/x/mario/more
check50 cs50/problems/2026/x/cash
check50 cs50/problems/2026/x/credit
```

### Check Style

```bash
style50 hello.c
style50 mario.c
style50 cash.c
style50 credit.c
```

### Submit

```bash
submit50 cs50/problems/2026/x/me
submit50 cs50/problems/2026/x/mario/less
submit50 cs50/problems/2026/x/mario/more
submit50 cs50/problems/2026/x/cash
submit50 cs50/problems/2026/x/credit
```

Note: `world` is only a practice exercise and does not need submission.

## Problem Notes

### `world/hello.c`

Prints:

```text
hello, world
```

Main lesson:

- Basic C structure
- `printf`
- Newline character `\n`
- Compiling and running a C program

### `me/hello.c`

Prompts the user for their name and prints a greeting.

Example:

```text
What's your name? Waleed
hello, Waleed
```

Main lesson:

- User input with `get_string`
- String formatting with `%s`
- Including `cs50.h`

### `mario-less/mario.c`

Prints a right-aligned pyramid.

Example for height `4`:

```text
   #
  ##
 ###
####
```

Main lesson:

- Nested loops
- Spaces before hashes
- Pattern printing
- Input validation

### `mario-more/mario.c`

Prints two side-by-side pyramids.

Example for height `4`:

```text
   #  #
  ##  ##
 ###  ###
####  ####
```

Main lesson:

- Nested loops
- Multiple pattern sections per row
- Fixed two-space gap
- Validating height from 1 to 8

### `cash/cash.c`

Calculates the minimum number of coins needed for a given amount of change.

Example:

```text
Change owed: 70
4
```

Because:

```text
25 + 25 + 10 + 10 = 70
```

Main lesson:

- Greedy algorithms
- Helper functions
- Integer arithmetic
- Repeated subtraction
- Clean step-by-step problem solving

### `credit/credit.c`

Checks whether a card number is valid and identifies its type.

Possible outputs:

```text
AMEX
MASTERCARD
VISA
INVALID
```

Main lesson:

- Working with long numbers
- Extracting digits using `% 10`
- Removing digits using `/ 10`
- Luhn’s algorithm
- Conditional card type checking

## Common Mistakes to Avoid

- Forgetting semicolons
- Forgetting `#include <cs50.h>` when using CS50 input functions
- Forgetting `#include <stdio.h>` when using `printf`
- Using `int` for credit card numbers instead of `long`
- Missing the newline `\n` in final output
- Printing extra text when CS50 expects exact output
- Incorrect spaces in Mario problems
- Not validating user input properly
- Forgetting function prototypes before `main`
- Mixing up assignment `=` and comparison `==`

## AI/ML Connection

Even though Week 1 is not directly about machine learning, C is important for understanding the lower-level foundations behind AI/ML systems.

This week connects to AI/ML because:

- C helps explain how programs interact with memory and hardware.
- Loops and conditionals are the base of algorithms.
- Greedy thinking appears in optimization problems.
- Integer arithmetic and validation are common in data preprocessing.
- Understanding compiled languages helps later when studying performance, GPUs, CUDA, PyTorch internals, and systems for machine learning.

## Status

Completed as part of:

```text
AI/ML Roadmap
└── Phase 02: Computer Science Foundations
    └── CS50x
        └── Week 01: C
```
