# A CSV reader that loads tabular data and prints simple summaries from selected columns.

import csv


def show_menu():
    while True:
        try:
            option = int(
                input(
                    "Menu:\n1. Read CSV file\n2. View rows\n3. Show column names\n4. Show number of rows\n5. Count values in a column\n6. Exit\n"
                ).strip()
            )

            if option not in [1, 2, 3, 4, 5, 6]:
                print("\nInvalid option!\nPlease try again\n")
                continue

            return option

        except ValueError:
            print("\nInvalid option!\nPlease try again\n")
            continue


def get_file_name():
    return input("\nEnter csv filename: ").strip()


def read_csv_file():
    filename = get_file_name()

    with open(filename, newline="") as file:
        reader = list(csv.DictReader(file))

        if len(reader) < 1:
            raise ValueError

        return reader


def view_rows(students):
    print()

    for i, student in enumerate(students, start=1):
        for value in student:
            print(f"{value}: {student[value]}", end=", ")

        print()

    print()


def show_column_names(students):
    for student in students:
        print("\nColumns:")

        for columns in student:
            print(columns)

        print()
        break


def show_number_of_rows(students):
    print(f"\nTotal rows: {len(students)}\n")


def get_column_name(students):
    while True:
        student = students[0]
        column = input("\nEnter column name: ").strip()

        if column not in student:
            print("\nInvalid column entered!\nPlease try again\n")
            continue

        return column


def summarize_columns(students, column):
    values = {}

    for student in students:
        value = student[column]

        if value not in values:
            values[value] = 1

        else:
            values[value] = values.get(value, 0) + 1

    return values


def print_summaries(items):
    print()

    for item in items:
        print(f"{item}: {items[item]}")

    print()


def count_values_in_a_column(students):
    column = get_column_name(students)

    values = summarize_columns(students, column)

    print_summaries(values)


def main():
    students = None

    while True:
        option = show_menu()

        if option == 1:
            try:
                students = read_csv_file()
                print()

            except FileNotFoundError:
                print("\nFile does not exist!\n")

            except ValueError:
                print("\nFile is empty!\n")

        elif option == 2:
            if not students:
                print("\nPlease read csv file first!\n")
                continue

            view_rows(students)

        elif option == 3:
            if not students:
                print("\nPlease read csv file first!\n")
                continue

            show_column_names(students)

        elif option == 4:
            if not students:
                print("\nPlease read csv file first!\n")
                continue

            show_number_of_rows(students)

        elif option == 5:
            if not students:
                print("\nPlease read csv file first!\n")
                continue

            count_values_in_a_column(students)

        elif option == 6:
            break


if __name__ == "__main__":
    main()
