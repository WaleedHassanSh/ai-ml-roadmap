# A regex-based text cleaner that cleans messy text and extracts emails and numbers.

import re


def show_menu():
    while True:
        try:
            option = int(
                input(
                    "Menu:\n1. Enter text manually\n2. Clean extra spaces\n3. Remove unwanted symbols\n4. Extract emails\n5. Extract numbers\n6. Exit\n"
                ).strip()
            )

            if option not in [1, 2, 3, 4, 5, 6]:
                print("\nInvalid option selected!\nPlease try again\n")
                continue

            return option

        except ValueError:
            print("\nInvalid option selected!\nPlease try again\n")
            continue


def get_text():
    while True:
        text = input("\nEnter messy text: ").strip()

        if not text:
            print("\nInput field cannot be empty!\nPlease enter some text first")
            continue

        return text


def clean_extra_spaces(text):
    text = re.sub(r"\s+", " ", text)

    return text


def remove_unwanted_symbols(text):
    text = re.sub(r"[^\w]+", " ", text)

    return text


def extract_emails(text):
    emails = re.findall(r"[^,@ ]+@[^@]+\.\w+", text)

    return emails


def print_values(values):
    print()

    for value in values:
        print(value)

    print()


def extract_numbers(text):
    numbers = re.findall(r"\d+", text)

    return numbers


def main():
    text = None

    while True:
        option = show_menu()

        if option == 1:
            text = get_text()
            print()

        elif option == 2:
            if not text:
                print("\nPlease enter some text first!\n")
                continue

            text = clean_extra_spaces(text)
            print(f"{text}\n")

        elif option == 3:
            if not text:
                print("\nPlease enter some text first!\n")
                continue

            text = remove_unwanted_symbols(text)
            print(f"{text}\n")

        elif option == 4:
            if not text:
                print("\nPlease enter some text first!\n")
                continue

            emails = extract_emails(text)

            if not emails:
                print("\nNo emails found in text!\n")
                continue

            print_values(emails)

        elif option == 5:
            if not text:
                print("\nPlease enter some text first!\n")
                continue

            numbers = extract_numbers(text)

            if not numbers:
                print("\nNo numbers found in text!\n")
                continue

            print_values(numbers)

        else:
            break


if __name__ == "__main__":
    main()
