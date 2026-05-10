# A file-based contact manager that stores, searches, updates, and deletes contacts using a CSV file.

import csv

FIELDNAMES = ["name", "phone number", "email"]


def show_menu():
    while True:
        try:
            option = int(
                input(
                    "Choose an option\n1. Add contact\n2. View contacts\n3. Search contact\n4. Update contact\n5. Delete contact\n6. Exit\n"
                )
            )

            if option not in [1, 2, 3, 4, 5, 6]:
                print("\nInvalid option!\nPlease try again\n")
                continue

            break

        except ValueError:
            print("\nInvalid option!\nPlease try again\n")
            continue

    return option


def get_contact():
    while True:
        name = input("\nName: ").strip().lower()
        phone_number = input("Phone Number: ").strip()
        email = input("Email: ").strip().lower()

        if not name or not phone_number or not email:
            print("\nInput field cannot be empty!\nPlease try again")
            continue

        break

    return {"name": name, "phone number": phone_number, "email": email}


def add_contact(contact):
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(contact)

    print("\nContact added!\n")


def view_contacts():
    with open("contacts.csv", newline="") as file:
        reader = list(csv.DictReader(file))

        if len(reader) < 1:
            raise ValueError

        return reader


def print_contacts(contacts):
    print()

    for i, contact in enumerate(contacts, start=1):
        print(
            f"{i}. Name: {contact['name'].capitalize()}, Phone Number: {contact['phone number']}, email: {contact['email']}"
        )

    print()


def search_contact(contacts):
    name = input("\nEnter name to search for contact: ").strip().lower()

    for contact in contacts:
        if name == contact["name"]:
            print("\nContact found!")
            print("\nContact details:")
            print(
                f"Name: {contact['name']}, Phone Number: {contact['phone number']}, Email: {contact['email']}\n"
            )
            break

    else:
        print("\nContact not found!\n")


def get_contact_number(contacts, prompt):
    while True:
        try:
            contact_number = int(input(f"{prompt}").strip())

            if contact_number < 1 or contact_number > len(contacts):
                print("\nInvalid contact number!\nPlease try again\n")
                continue

            break

        except ValueError:
            print("\nInvalid contact number!\nPlease try again\n")
            continue

    return contact_number


def save_contacts(contacts, message):
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        writer.writeheader()
        writer.writerows(contacts)

    print(f"\n{message}\n")


def update_contact(contacts):
    contact_number = get_contact_number(contacts, "Enter contact number to update: ")

    contact = get_contact()

    for i, cont in enumerate(contacts, start=1):
        if i == contact_number:
            cont["name"] = contact["name"]
            cont["phone number"] = contact["phone number"]
            cont["email"] = contact["email"]

    save_contacts(contacts, "Contact updated!")


def delete_contact(contacts):
    contact_number = get_contact_number(contacts, "Enter contact number to delete: ")

    del contacts[contact_number - 1]

    save_contacts(contacts, "Contact deleted!")


def main():
    while True:
        option = show_menu()

        if option == 1:
            contact = get_contact()
            add_contact(contact)

        elif option == 2:
            try:
                contacts = view_contacts()

            except (FileNotFoundError, ValueError):
                print("\nNo contacts available!\nPlease add some first\n")
                continue

            print_contacts(contacts)

        elif option == 3:
            try:
                contacts = view_contacts()

            except (FileNotFoundError, ValueError):
                print("\nNo contacts available!\nPlease add some first\n")
                continue

            search_contact(contacts)

        elif option == 4:
            try:
                contacts = view_contacts()

            except (FileNotFoundError, ValueError):
                print("\nNo contacts available!\nPlease add some first\n")
                continue

            print_contacts(contacts)
            update_contact(contacts)

        elif option == 5:
            try:
                contacts = view_contacts()

            except (FileNotFoundError, ValueError):
                print("\nNo contacts available!\nPlease add some first\n")
                continue

            print_contacts(contacts)
            delete_contact(contacts)

        elif option == 6:
            break


if __name__ == "__main__":
    main()
