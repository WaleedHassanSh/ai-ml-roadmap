# CS Foundations — Manual Tracing and Time/Space Practice

## Problem 1 — Change-Making Trace

**Topic:** Greedy algorithm, loops, arithmetic, time/space tradeoff.

**Problem:** Trace the greedy change-making process for **68 cents** using 25-cent, 10-cent, 5-cent, and 1-cent coins.

| Step | Coin type checked | Cents before | Coins added | Cents after | Total coins |
| ---- | ----------------: | -----------: | ----------: | ----------: | ----------: |
| 1    |          25 cents |           68 |           2 |          18 |           2 |
| 2    |          10 cents |           18 |           1 |           8 |           3 |
| 3    |           5 cents |            8 |           1 |           3 |           4 |
| 4    |            1 cent |            3 |           3 |           0 |           7 |

**Answers**

1. 25-cent coins used: 2
2. 10-cent coins used: 1
3. 5-cent coins used: 1
4. 1-cent coins used: 3
5. Total coins: 7
6. It is a greedy algorithm because it makes the best available choice at each step.
7. Informal time tradeoff: small work because it checks coin types one by one.
8. Informal space tradeoff: small extra memory because it stores only a few values, such as total coins and remaining cents.

**Lesson:** A greedy algorithm chooses the best available choice at each step and then moves to the next stage.

---

## Problem 2 — Linear Search Trace

**Topic:** Arrays, searching, loops, comparison, time/space tradeoff.

**Problem:** Trace linear search on `[4, 9, 2, 7, 5]` to find target `7`.

| Step | Index checked | Value checked | Is value equal to target? | Search status |
| ---- | ------------: | ------------: | ------------------------- | ------------- |
| 1    |             0 |             4 | No                        | Not found     |
| 2    |             1 |             9 | No                        | Not found     |
| 3    |             2 |             2 | No                        | Not found     |
| 4    |             3 |             7 | Yes                       | Found         |
| 5    |   Not checked |   Not checked | Not checked               | Found         |

**Answers**

1. Target found at index: 3
2. Values checked before finding: 3 before, 4 total including the found value
3. Does it check the whole list? No, not in this trace.
4. It is called linear search because it checks one value at a time.
5. Informal time tradeoff: can be slow for large lists because it checks values one by one.
6. Informal space tradeoff: low extra memory because it stores only search/find status.
7. It checks values one by one until the value is found or the end is reached.

**Lesson:** Linear search is a simple checking algorithm that checks one value at a time.

---

## Problem 3 — Binary Search Trace

**Topic:** Sorted arrays, searching, middle value, comparison, time/space tradeoff.

**Problem:** Trace binary search on `[2, 4, 7, 9, 12, 15, 18]` to find target `15`.

| Step | Low index | High index | Middle index | Middle value | Comparison with target | Search status |
| ---- | --------: | ---------: | -----------: | -----------: | ---------------------- | ------------- |
| 1    |         0 |          6 |            3 |            9 | 9 != 15                | Not found     |
| 2    |         4 |          6 |            5 |           15 | 15 == 15               | Found         |

**Answers**

1. Target found at index: 5
2. Middle values checked: 2
3. Does binary search check every value? No
4. It requires a sorted list so it can decide whether to search left or right.
5. Informal time tradeoff: small because it keeps dividing the search area in half.
6. Informal space tradeoff: small because it stores search status and index values such as low, high, and middle.
7. Binary search checks the middle value, then decides whether to move left or right.

**Lesson:** Binary search avoids checking every value by using the sorted order of the list.

---

## Problem 4 — Selection Sort Trace

**Topic:** Arrays, sorting, minimum value, swapping, time/space tradeoff.

**Problem:** Trace selection sort on `[5, 2, 9, 1, 4]`.

| Pass | Unsorted part starts at index | Smallest value found | Smallest value index | Swap made?            | List after pass   |
| ---- | ----------------------------: | -------------------: | -------------------: | --------------------- | ----------------- |
| 1    |                             0 |                    1 |                    3 | Yes                   | `[1, 2, 9, 5, 4]` |
| 2    |                             1 |                    2 |                    1 | Self-swap / no change | `[1, 2, 9, 5, 4]` |
| 3    |                             2 |                    4 |                    4 | Yes                   | `[1, 2, 4, 5, 9]` |
| 4    |                             3 |                    5 |                    3 | Self-swap / no change | `[1, 2, 4, 5, 9]` |

**Answers**

1. List after pass 1: `[1, 2, 9, 5, 4]`
2. List after pass 2: `[1, 2, 9, 5, 4]`
3. List after pass 3: `[1, 2, 4, 5, 9]`
4. Final sorted list: `[1, 2, 4, 5, 9]`
5. It is called selection sort because it selects the smallest value and swaps it with the current unsorted index.
6. Yes, selection sort checks many values even if the list is almost sorted.
7. Informal time tradeoff: large, because it repeatedly scans the remaining unsorted part.
8. Informal space tradeoff: small, because it sorts using the original list and a few variables.
9. Selection sort selects the smallest value from the unsorted part and swaps it into position.

**Lesson:** Selection sort cannot easily guess that a list is already sorted; it still scans the unsorted part.

---

## Problem 5 — Bubble Sort Trace

**Topic:** Arrays, sorting, adjacent comparison, swapping, time/space tradeoff.

**Problem:** Trace bubble sort on `[6, 3, 8, 2]`.

| Pass | Comparison made | Swap made? | List after comparison |
| ---- | --------------- | ---------- | --------------------- |
| 1    | 6 and 3         | Yes        | `[3, 6, 8, 2]`        |
| 1    | 6 and 8         | No         | `[3, 6, 8, 2]`        |
| 1    | 8 and 2         | Yes        | `[3, 6, 2, 8]`        |
| 2    | 3 and 6         | No         | `[3, 6, 2, 8]`        |
| 2    | 6 and 2         | Yes        | `[3, 2, 6, 8]`        |
| 3    | 3 and 2         | Yes        | `[2, 3, 6, 8]`        |

**Answers**

1. List after pass 1: `[3, 6, 2, 8]`
2. List after pass 2: `[3, 2, 6, 8]`
3. Final sorted list: `[2, 3, 6, 8]`
4. It is called bubble sort because larger values bubble toward the end.
5. Yes, it compares neighboring values.
6. Informal time tradeoff: high because it compares adjacent values repeatedly across passes.
7. Informal space tradeoff: low because it does not need a second full list.
8. Bubble sort compares adjacent values and moves larger values toward the end.

**Lesson:** Bubble sort works through repeated adjacent comparisons and swaps.

---

## Problem 6 — Merge Step Trace

**Topic:** Arrays, sorted lists, merging, comparison, time/space tradeoff.

**Problem:** Trace the merge step for left list `[2, 6]` and right list `[3, 8]`.

| Step | Left value checked | Right value checked | Smaller value selected | Merged list after step |
| ---- | -----------------: | ------------------: | ---------------------: | ---------------------- |
| 1    |                  2 |                   3 |                      2 | `[2]`                  |
| 2    |                  6 |                   3 |                      3 | `[2, 3]`               |
| 3    |                  6 |                   8 |                      6 | `[2, 3, 6]`            |
| 4    |                  - |                   8 |                      8 | `[2, 3, 6, 8]`         |

**Answers**

1. Final merged list: `[2, 3, 6, 8]`
2. Comparisons made: 3 comparisons; the last value is copied after one side becomes empty.
3. Both lists need to be sorted so the smaller front value can be safely chosen next.
4. Informal time tradeoff: small because the merge step moves through the lists in order.
5. Informal space tradeoff: high compared with in-place sorting because it creates a new merged list.
6. The merge step checks both lists and adds the smaller value into a new sorted list.

**Lesson:** Merging works by repeatedly choosing the smaller front value from two sorted lists.

---

## Problem 7 — Memory / Pointer Trace

**Topic:** Memory, addresses, values, pointers, dereferencing, time/space tradeoff.

| Variable | Address | Value stored |
| -------- | ------: | -----------: |
| `x`      |    1000 |           10 |
| `p`      |    2000 |         1000 |

| Step | Action                             | Value of x | Value stored in p | Value accessed through p | Explanation                                      |
| ---- | ---------------------------------- | ---------: | ----------------: | -----------------------: | ------------------------------------------------ |
| 1    | Read x                             |         10 |              1000 |                      N/A | Reading x value                                  |
| 2    | Read p                             |         10 |              1000 |                      N/A | Reading value stored in p                        |
| 3    | Read value pointed to by p         |         10 |              1000 |                       10 | Go to the address stored in p and read its value |
| 4    | Change value pointed to by p to 25 |         25 |              1000 |                       25 | Change the value to 25                           |
| 5    | Read x again                       |         25 |              1000 |                      N/A | Now x is 25                                      |

**Answers**

1. Value stored in x at the start: 10
2. Value stored in p: 1000
3. p points to x
4. After changing the value pointed to by p, x becomes 25
5. Pointer tracing helps understand how memory works under the hood.
6. Informal time tradeoff: small because it changes/accesses one value.
7. Informal space tradeoff: small because it stores one pointer.
8. It shows how addresses are stored and used to access values.

**Lesson:** A pointer stores an address, and dereferencing it accesses or changes the value at that address.

---

## Problem 8 — Linked List Traversal Trace

**Topic:** Linked structures, nodes, pointers, traversal, time/space tradeoff.

**Problem:** Trace linked list traversal on `10 → 20 → 30 → NULL` to find target `30`.

| Step | Current node value | Is it the target? | Move to next? | Search status |
| ---- | -----------------: | ----------------- | ------------- | ------------- |
| 1    |                 10 | No                | Yes           | Not found     |
| 2    |                 20 | No                | Yes           | Not found     |
| 3    |                 30 | Yes               | No            | Found         |
| 4    |               NULL | Not checked       | Not checked   | Not checked   |

**Answers**

1. Target found at node value: 30
2. Nodes checked: 3
3. Traversal does not need direct index access like arrays.
4. The pointer moves node by node because each node stores the address of the next node.
5. If current reaches NULL before finding the target, search ends as not found.
6. Informal time tradeoff: high for long lists because nodes are checked one by one.
7. Informal space tradeoff: small during traversal because only the current pointer is used.
8. Linked list traversal checks nodes one by one until the value is found or the end is reached.

**Lesson:** Linked list traversal is similar to linear search, but it follows next pointers instead of indexes.

---

## Problem 9 — Hash Table Trace

**Topic:** Hash tables, keys, buckets, collisions, lookup, time/space tradeoff.

**Problem:** Hash table has 5 buckets. Hash rule: `bucket number = key length % 5`.

| Step | Name inserted | Name length | Bucket number | Collision? | Bucket contents after insertion        |
| ---- | ------------- | ----------: | ------------: | ---------- | -------------------------------------- |
| 1    | Ali           |           3 |             3 | No         | `[Ali, NULL]`                          |
| 2    | Sara          |           4 |             4 | No         | `[Sara, NULL]`                         |
| 3    | Hamza         |           5 |             0 | No         | `[Hamza, NULL]`                        |
| 4    | Noor          |           4 |             4 | Yes        | `[Sara, next address], [Noor, NULL]`   |
| 5    | Bilal         |           5 |             0 | Yes        | `[Hamza, next address], [Bilal, NULL]` |

| Step | Name searched | Bucket checked | Values inside bucket | Found? |
| ---- | ------------- | -------------: | -------------------- | ------ |
| 1    | Noor          |              4 | `[Sara, Noor]`       | Yes    |

**Answers**

1. Ali goes into bucket 3
2. Sara goes into bucket 4
3. Hamza goes into bucket 0
4. Noor goes into bucket 4
5. Bilal goes into bucket 0
6. Yes, collisions happened
7. Bucket checked for Noor: 4
8. Hash table lookup can be faster than linear search because it goes to a bucket instead of scanning the whole list.
9. Informal time tradeoff: it can quickly go to a bucket, then may search inside that bucket/list.
10. Informal space tradeoff: high compared with a simple list because it stores buckets, values, and possible next pointers.
11. Hash tables break data into buckets and handle collisions using lists/chains.

**Lesson:** A hash table uses a hash rule to choose a bucket, which can reduce search work compared with linear search.

---

## Problem 10 — Binary Tree Search Trace

**Topic:** Trees basics, nodes, left/right child, traversal, search, time/space tradeoff.

```text
        8
       / \
      3   10
     / \    \
    1   6    14
```

Target: `6`

| Step | Current node value | Compare with target | Move left/right? | Search status |
| ---- | -----------------: | ------------------- | ---------------- | ------------- |
| 1    |                  8 | 8 > 6               | Move left        | Not found     |
| 2    |                  3 | 3 < 6               | Move right       | Not found     |
| 3    |                  6 | 6 = 6               | No               | Found         |

**Answers**

1. Target found at node 6
2. Nodes checked: 3
3. Does it check every node? No
4. A BST can skip nodes because it compares the target with the current node and decides left or right.
5. If the tree is not ordered, it cannot reliably decide whether to move left or right.
6. Informal time tradeoff: fast when the tree is balanced/ordered, but slower if badly shaped.
7. Informal space tradeoff: small because it tracks target, current node, and status.
8. BST search is similar in idea to binary search, but it moves through tree branches using left/right decisions.

**Lesson:** A binary search tree uses ordering to skip parts of the tree.

---

## Problem 11 — SQL/Data Filtering Trace

**Topic:** SQL basics, tables, rows, filtering, data handling, time/space tradeoff.

|  ID | Name  | Marks |
| --: | ----- | ----: |
|   1 | Ali   |    72 |
|   2 | Sara  |    88 |
|   3 | Hamza |    65 |
|   4 | Noor  |    91 |
|   5 | Bilal |    78 |

**Problem:** Find all students whose marks are 80 or above.

| Step | Row checked | Name  | Marks | Condition: marks >= 80? | Include in result? | Result so far |
| ---- | ----------: | ----- | ----: | ----------------------- | ------------------ | ------------- |
| 1    |           1 | Ali   |    72 | False                   | No                 | Empty         |
| 2    |           2 | Sara  |    88 | True                    | Yes                | Sara          |
| 3    |           3 | Hamza |    65 | False                   | No                 | Sara          |
| 4    |           4 | Noor  |    91 | True                    | Yes                | Sara, Noor    |
| 5    |           5 | Bilal |    78 | False                   | No                 | Sara, Noor    |

**Answers**

1. Final result: Sara, Noor
2. Rows checked: 5
3. Filtering is useful because it selects rows that match the user’s requirement.
4. This task does not change the original table.
5. Informal time tradeoff: can be like linear search if there is no index/optimization.
6. Informal space tradeoff: small because it stores only the matching result list.
7. Filtering returns only rows that satisfy the condition.

**Lesson:** SQL filtering selects matching rows without changing the original table.

---

## Problem 12 — Web/App Request Flow Trace

**Topic:** Basic web/app/software engineering perspective, input, processing, output, data flow, time/space tradeoff.

**Problem:** Trace a simple app request where the user submits `Name: Waleed` and `Action: View Profile`.

| Step | App action              | Input/data used | What the app checks/does                            | Output/result after step          |
| ---- | ----------------------- | --------------- | --------------------------------------------------- | --------------------------------- |
| 1    | Receive request         | request         | Receives request and decides the page/action        | Request received                  |
| 2    | Read form input         | form input      | Reads the data typed in the form                    | Input received                    |
| 3    | Validate input          | name and action | Checks whether required input is valid              | Input validated                   |
| 4    | Search for user profile | name + action   | Runs database query/search                          | User profile found or not         |
| 5    | Prepare response        | profile data    | Creates response based on whether profile was found | Profile data or not found message |
| 6    | Send response           | response data   | Sends response to the user                          | Output page shown                 |

**Answers**

1. Input received: name + action
2. Validation checks whether the user entered name and selected an action.
3. It searches for the profile of the user.
4. Final response should contain the user profile or not found message.
5. It is app/software flow because input is received, processed, checked, and returned as output.
6. Informal time tradeoff: small for simple cases, but can change depending on database size and structure.
7. Informal space tradeoff: small because it only keeps request data and response data.
8. The app receives input, validates it, searches in the database, and shows relevant results.

**Lesson:** A request flow shows how user input moves through validation, processing, database access, and response output.

---
