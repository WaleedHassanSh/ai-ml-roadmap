# A command-line to-do list manager that saves, views, updates, and deletes tasks using a CSV file.

import csv


def show_menu():
    while True:
        try:
            option = int(
                input(
                    "Choose an option\n1. Add task\n2. View tasks\n3. Mark task as complete\n4. Delete task\n5. Exit\n"
                )
            )

            if option not in [1, 2, 3, 4, 5]:
                print("\nPlease choose a valid option!\n")
                continue

            return option

        except ValueError:
            print("\nPlease choose a valid option!\n")
            continue


def get_task():
    while True:
        task_title = input("\nTask Title: ")
        print()

        if not task_title.strip():
            print("\nPlease enter Task Title!")

        else:
            break

    return {"task_title": task_title.strip(), "task_status": "pending"}


def add_task(task):
    with open("tasks.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["task_title", "task_status"])

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(task)


def view_tasks():
    with open("tasks.csv") as file:
        reader = list(csv.DictReader(file))

        if len(reader) == 0:
            raise ValueError

        return reader


def print_tasks(tasks):
    print()

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task_title']} - {task['task_status']}")

    print()


def get_option(tasks, prompt):
    while True:
        try:
            option = int(input(f"{prompt}"))

            if option > len(tasks) or option < 1:
                print("\nPlease choose a valid task number!")
                continue

            break

        except ValueError:
            print("\nPlease choose a valid task number!")
            continue

    return option


def update_file(tasks, message):
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["task_title", "task_status"])

        writer.writeheader()
        writer.writerows(tasks)

    print(f"\n{message}\n")


def mark_task_complete(tasks):
    option = get_option(tasks, "Enter task number to mark as complete: ")

    for i, task in enumerate(tasks, start=1):
        if option == i:
            task["task_status"] = "complete"
            break

    update_file(tasks, "Task marked as complete")


def delete_task(tasks):
    option = get_option(tasks, "Enter task number to delete: ")

    del tasks[option - 1]

    update_file(tasks, "Task deleted")


def main():
    while True:
        option = show_menu()

        if option == 1:
            task = get_task()
            add_task(task)

        elif option == 2:
            try:
                tasks = view_tasks()

            except (ValueError, FileNotFoundError):
                print("\nThere are no tasks, please add some tasks!\n")
                continue

            print_tasks(tasks)

        elif option == 3:
            try:
                tasks = view_tasks()

            except (ValueError, FileNotFoundError):
                print("\nThere are no tasks, please add some tasks!\n")
                continue

            print_tasks(tasks)
            mark_task_complete(tasks)

        elif option == 4:
            try:
                tasks = view_tasks()

            except (ValueError, FileNotFoundError):
                print("\nThere are no tasks, please add some tasks!\n")
                continue

            print_tasks(tasks)
            delete_task(tasks)

        else:
            break


if __name__ == "__main__":
    main()
