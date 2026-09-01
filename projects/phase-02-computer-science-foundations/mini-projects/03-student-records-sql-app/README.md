# Student Records SQL App

This mini-project is part of **Phase 2: Computer Science Foundations** in my AI/ML roadmap.

It is a small SQL-backed application for storing, viewing, searching, updating, and deleting student records using Python and SQLite.

## Purpose

The purpose of this project is to practice using SQL with a real mini-application instead of only writing isolated SQL queries.

This project helps me practice:

- Creating a database table
- Inserting records
- Reading records
- Searching records
- Updating records
- Deleting records
- Using Python with SQLite
- Organizing a small database-backed project
- Separating schema, sample data, and application logic

## Project Folder

```text
03-student-records-sql-app/
```

## Folder Structure

```text
03-student-records-sql-app/
├── README.md
├── app.py
├── schema.sql
├── seed.sql
├── requirements.txt
```

## File Descriptions

| File               | Purpose                                                |
| ------------------ | ------------------------------------------------------ |
| `README.md`        | Explains the project, setup, usage, and learning goals |
| `app.py`           | Main Python application                                |
| `schema.sql`       | Defines the database structure                         |
| `seed.sql`         | Adds sample student records                            |
| `requirements.txt` | Lists Python dependencies, if any                      |

## Database Design

The app uses a simple `students` table.

Example table structure:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL NOT NULL
);
```

## Example Data

Sample data can be stored in `seed.sql`.

Example:

```sql
INSERT INTO students (name, marks)
VALUES
('Ali Khan', 85),
('Sara Ahmed', 92),
('Usman Tariq', 76);
```

## Features

The app should allow the user to:

1. Add a new student
2. View all students
3. Search student by name
4. Update student marks
5. Delete a student
6. Exit the program

## How to Set Up the Database

Run these commands inside the project folder:

```bash
sqlite3 students.db < schema.sql
sqlite3 students.db < seed.sql
```

This creates the database and inserts sample records.

## How to Run

Run the Python app:

```bash
python app.py
```

## Example Menu

```text
1. Add student
2. View all students
3. Search student
4. Update student marks
5. Delete student
6. Exit
```

## Expected Learning Outcomes

By completing this mini-project, I should be able to:

- Understand the difference between `schema.sql` and `seed.sql`
- Create and initialize a SQLite database
- Write basic SQL queries
- Connect Python code with a database
- Perform CRUD operations
- Validate user input
- Organize a small SQL-backed application cleanly

## Notes

This project belongs to:

```text
projects/phase-02-computer-science-foundations/mini-projects/03-student-records-sql-app/
```

It should stay inside `mini-projects/` because it is an independent practice project, not official CS50x coursework.
