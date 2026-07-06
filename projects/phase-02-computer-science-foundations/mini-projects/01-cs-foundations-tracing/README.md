# CS Foundations Tracing

This mini-project is part of **Phase 2: Computer Science Foundations** in my AI/ML roadmap.

It focuses on manually tracing code, understanding how variables change step by step, and explaining basic time and space tradeoffs informally.

## Purpose

The purpose of this mini-project is to build strong problem-solving foundations before moving deeper into algorithms, data structures, SQL, and larger software projects.

This project helps me practice:

- Reading code carefully
- Tracing code manually
- Tracking variable changes
- Understanding loops and conditionals
- Predicting program output
- Explaining time complexity informally
- Explaining space usage informally
- Writing clear step-by-step reasoning

## Project Folder

```text
01-cs-foundations-tracing/
```

## Folder Structure

```text
01-cs-foundations-tracing/
├── README.md
└── tracing-practice.md
```

## File Descriptions

| File | Purpose |
|---|---|
| `README.md` | Explains the purpose, structure, and learning goals of this mini-project |
| `tracing-practice.md` | Contains manual code tracing exercises and explanations |

## What to Practice

This mini-project should include small examples where I trace code by hand before running it.

Practice areas:

1. Variables and assignment
2. Conditional statements
3. Loops
4. Nested loops
5. Functions
6. Lists and arrays
7. Strings
8. Dictionaries
9. Recursion basics
10. Simple algorithm patterns

## Recommended Tracing Format

For each exercise, use this format:

```markdown
## Exercise 01: Loop Trace

### Code

```python
x = 0

for i in range(3):
    x = x + i

print(x)
```

### Manual Trace

| Step | i | x | Explanation |
|---|---:|---:|---|
| Start | - | 0 | Initial value of x |
| 1 | 0 | 0 | x = 0 + 0 |
| 2 | 1 | 1 | x = 0 + 1 |
| 3 | 2 | 3 | x = 1 + 2 |

### Final Output

```text
3
```

### Time Complexity

The loop runs 3 times here. In general, if the loop runs `n` times, the time complexity is:

```text
O(n)
```

### Space Complexity

Only a few variables are used, so the space complexity is:

```text
O(1)
```
```

## Time and Space Tradeoff Notes

For each tracing exercise, also write a short informal explanation:

- How many times does the loop run?
- Does the program create a new list, dictionary, or other data structure?
- Does it use extra memory?
- Is the solution faster because it uses more memory?
- Is the solution slower because it saves memory?

## Example Topics

Good exercises for this mini-project:

- Sum of numbers
- Count even numbers
- Find maximum in a list
- Reverse a string
- Count characters in a string
- Search for an item in a list
- Nested loop pair checking
- Simple frequency dictionary
- Basic recursion trace
- Compare two small approaches to the same problem

## Expected Learning Outcomes

By completing this mini-project, I should be able to:

- Trace small programs manually
- Predict output before running code
- Explain how variables change during execution
- Understand the behavior of loops and nested loops
- Describe time complexity in simple language
- Describe space complexity in simple language
- Build stronger foundations for algorithms and data structures

## Notes

This project belongs to:

```text
projects/phase-02-computer-science-foundations/mini-projects/01-cs-foundations-tracing/
```

It should stay inside `mini-projects/` because it is an independent CS foundations practice project, not official CS50x coursework.
