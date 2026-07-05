# CS50x Week 7 SQL

This folder contains my CS50x Week 7 SQL work. The week focuses on querying SQLite databases using `SELECT`, filtering, sorting, aggregation, joins, subqueries, pattern matching, and investigative SQL.

## Folder Structure

```text
week-07-sql/
├── songs/
│   ├── 1.sql
│   ├── 2.sql
│   ├── 3.sql
│   ├── 4.sql
│   ├── 5.sql
│   ├── 6.sql
│   ├── 7.sql
│   ├── 8.sql
│   ├── answers.txt
│   └── songs.db
│
├── movies/
│   ├── 1.sql
│   ├── 2.sql
│   ├── 3.sql
│   ├── 4.sql
│   ├── 5.sql
│   ├── 6.sql
│   ├── 7.sql
│   ├── 8.sql
│   ├── 9.sql
│   ├── 10.sql
│   ├── 11.sql
│   ├── 12.sql
│   ├── 13.sql
│   └── movies.db
│
├── fiftyville/
│   ├── answers.txt
│   ├── log.sql
│   └── fiftyville.db
│
└── README.md
```

## Problems Covered

### Songs

The `songs` problem uses a SQLite database containing Spotify data for the top 100 streamed songs of 2018.

Main SQL concepts practiced:

- Selecting specific columns
- Ordering rows with `ORDER BY`
- Limiting output with `LIMIT`
- Filtering rows with `WHERE`
- Combining conditions with `AND`
- Calculating averages with `AVG`
- Using subqueries
- Joining related tables
- Pattern matching with `LIKE`

### Movies

The `movies` problem uses an IMDb-style SQLite database containing movies, people, stars, directors, and ratings.

Main SQL concepts practiced:

- Filtering by year, title, rating, and name
- Counting rows with `COUNT`
- Calculating averages with `AVG`
- Joining tables using foreign keys
- Using nested subqueries
- Removing duplicates with `DISTINCT`
- Sorting results with multiple conditions
- Querying many-to-many relationships

### Fiftyville

The `fiftyville` problem is an SQL investigation problem. The goal is to identify:

- The thief
- The city the thief escaped to
- The accomplice

Main SQL concepts practiced:

- Exploring unknown database schemas
- Reading crime reports and interviews
- Building evidence through multiple queries
- Combining clues from multiple tables
- Using SQL comments to document reasoning
- Writing a clear investigation log

## How to Run

Open the relevant problem folder first.

Example:

```bash
cd projects/phase-02-computer-science-foundations/cs50x/week-07-sql/songs
```

Run a query file against the database:

```bash
cat 1.sql | sqlite3 songs.db
```

For the `movies` problem:

```bash
cd ../movies
cat 1.sql | sqlite3 movies.db
```

For the `fiftyville` problem:

```bash
cd ../fiftyville
sqlite3 fiftyville.db
```

## How to Test

Use CS50's `check50`.

### Songs

```bash
check50 cs50/problems/2026/x/songs
```

### Movies

```bash
check50 cs50/problems/2026/x/movies
```

### Fiftyville

```bash
check50 cs50/problems/2026/x/fiftyville
```

## How to Submit

### Songs

```bash
submit50 cs50/problems/2026/x/songs
```

### Movies

```bash
submit50 cs50/problems/2026/x/movies
```

### Fiftyville

```bash
submit50 cs50/problems/2026/x/fiftyville
```

## Notes

- Each `.sql` file should contain one SQL query for the required question.
- Do not hardcode IDs unless the specification explicitly allows it.
- Prefer subqueries or joins when matching related data across tables.
- Return only the columns required by the problem statement.
- Use `DISTINCT` when the problem requires each person or result to appear only once.
- For `fiftyville`, keep every investigative query inside `log.sql` with a clear SQL comment above it.

## Key Skills Practiced

- SQLite
- Relational databases
- Query design
- Joins
- Aggregation
- Subqueries
- Pattern matching
- Database investigation
- Evidence-based debugging
