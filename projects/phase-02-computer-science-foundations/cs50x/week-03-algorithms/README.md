# CS50x Week 3 — Algorithms

This folder contains my CS50x Week 3 problem set work.

## Local Path

```bash
~/ai-ml-roadmap/projects/phase-02-cs50x/week-03-algorithms/
```

## Topics Covered

- Sorting algorithms
- Selection sort
- Bubble sort
- Merge sort
- Plurality voting
- Runoff voting
- Tideman ranked pairs voting
- Arrays
- Structs
- 2D arrays
- Graph cycle detection

## Problems

| Problem | File / Folder | Status |
|---|---|---|
| Sort | `sort/answers.txt` | Completed |
| Plurality | `plurality/plurality.c` | Completed |
| Runoff | `runoff/runoff.c` | Completed |
| Tideman | `tideman/tideman.c` | Completed |

## Folder Structure

```text
week-03-algorithms/
├── sort/
│   ├── answers.txt
│   ├── sort1
│   ├── sort2
│   ├── sort3
│   ├── random5000.txt
│   ├── random10000.txt
│   ├── random50000.txt
│   ├── reversed5000.txt
│   ├── reversed10000.txt
│   ├── reversed50000.txt
│   ├── sorted5000.txt
│   ├── sorted10000.txt
│   └── sorted50000.txt
│
├── plurality/
│   └── plurality.c
│
├── runoff/
│   └── runoff.c
│
├── tideman/
│   └── tideman.c
│
└── README.md
```

## Setup Commands

Run these commands from the root of the local repository:

```bash
cd ~/ai-ml-roadmap

mkdir -p projects/phase-02-cs50x/week-03-algorithms

cd projects/phase-02-cs50x/week-03-algorithms
```

Download the CS50x Week 3 distribution code:

```bash
wget https://cdn.cs50.net/2026/x/psets/3/sort.zip
unzip sort.zip
rm sort.zip

wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
unzip plurality.zip
rm plurality.zip

wget https://cdn.cs50.net/2026/x/psets/3/runoff.zip
unzip runoff.zip
rm runoff.zip

wget https://cdn.cs50.net/2026/x/psets/3/tideman.zip
unzip tideman.zip
rm tideman.zip
```

## Check Commands

```bash
check50 cs50/problems/2026/x/sort
check50 cs50/problems/2026/x/plurality
check50 cs50/problems/2026/x/runoff
check50 cs50/problems/2026/x/tideman
```

## Style Commands

```bash
style50 plurality.c
style50 runoff.c
style50 tideman.c
```

## Submit Commands

```bash
submit50 cs50/problems/2026/x/sort
submit50 cs50/problems/2026/x/plurality
submit50 cs50/problems/2026/x/runoff
submit50 cs50/problems/2026/x/tideman
```

## Notes

- `sort` is an analysis problem. The final answers go in `sort/answers.txt`.
- `plurality`, `runoff`, and `tideman` are C programming problems.
- `tideman` is the hardest problem in Week 3 because it requires graph cycle detection.
- Keep each CS50 problem in its original folder so `check50`, `style50`, and `submit50` work cleanly.
