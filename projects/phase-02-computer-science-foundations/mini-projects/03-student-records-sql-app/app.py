from cs50 import SQL

db = SQL("sqlite:///students.db")


def show_menu():
    while True:
        try:
            choice = int(
                input("""1. Add student
2. View all students
3. Search student by name
4. Update student marks
5. Delete student
6. Exit
""")
            )

            if choice not in [1, 2, 3, 4, 5, 6]:
                print("Please choose a valid option!")
                continue

            return choice

        except ValueError:
            print("Please choose a valid option!")
            continue


def get_student_name():
    while True:
        name = input("Name: ")

        if not name:
            print("Please enter correct data")
            continue

        return name


def get_student_marks():
    while True:
        try:
            marks = float(input("Marks: "))

            if not 0 <= marks <= 100:
                print("Please enter correct data")
                continue

            return marks

        except ValueError:
            print("Please enter correct data")
            continue


def add_student():
    name, marks = get_student_name(), get_student_marks()

    db.execute("INSERT INTO students(name, marks) VALUES (?, ?)", name, marks)

    print("Successfully added!")


def show_all_students():
    students = db.execute("SELECT * FROM students")

    print()

    if not students:
        print("There is no student to display")

    else:
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")


def show_student_by_name():
    name = get_student_name()

    students = db.execute("SELECT * FROM students WHERE name = ?", name)

    print()

    if not students:
        print("There is no student to display")

    else:
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")


def update_student_marks():
    name = get_student_name()
    marks = get_student_marks()

    students = db.execute("SELECT * FROM students WHERE name = ?", name)

    print()

    if not students:
        print("There is no student with this name to update marks")

    else:
        db.execute("UPDATE students SET marks = ? WHERE name = ?", marks, name)
        print("Successfully updated!")


def delete_student():
    name = get_student_name()

    students = db.execute("SELECT * FROM students WHERE name = ?", name)

    print()

    if not students:
        print("There is no student with this name to delete")

    else:
        db.execute("DELETE FROM students WHERE name = ?", name)
        print("Successfully deleted!")


def main():
    while True:
        choice = show_menu()

        if choice == 1:
            add_student()
        elif choice == 2:
            show_all_students()
        elif choice == 3:
            show_student_by_name()
        elif choice == 4:
            update_student_marks()
        elif choice == 5:
            delete_student()
        else:
            break


if __name__ == "__main__":
    main()
