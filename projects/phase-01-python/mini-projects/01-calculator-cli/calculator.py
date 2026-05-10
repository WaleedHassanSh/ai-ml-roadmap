# A command-line calculator that performs basic arithmetic operations with input validation.


def show_menu():
    while True:
        try:
            option = int(
                input(
                    "Choose an option\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n"
                )
            )

            if option not in [1, 2, 3, 4, 5]:
                print("\nPlease choose a valid option!\n")
                continue

            return option

        except ValueError:
            print("\nPlease choose a valid option!\n")
            continue


def get_numbers():
    while True:
        try:
            a = float(input("\nEnter 1st Number: "))
            b = float(input("Enter 2nd Number: "))
            return a, b

        except ValueError:
            print("Please enter valid numbers!")
            continue


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError()

    return a / b


def main():
    result = None

    while True:
        option = show_menu()

        if option == 5:
            break

        a, b = get_numbers()

        if option == 1:
            result = add_numbers(a, b)

        elif option == 2:
            result = subtract_numbers(a, b)

        elif option == 3:
            result = multiply_numbers(a, b)

        elif option == 4:
            try:
                result = divide_numbers(a, b)

            except ZeroDivisionError:
                print(
                    "\nDivision by zero is not possible.\nPlease choose a valid number!\n"
                )
                continue

        print(f"\nResult: {result:.2f}\n")


if __name__ == "__main__":
    main()
