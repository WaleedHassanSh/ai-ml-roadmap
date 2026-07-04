# Asks the user for a greeting. If the greeting starts with "hello" (in any case), then output $0. If the greeting starts with an "h" (in any case), then output $20. Otherwise, output $100.


def main():
    greeting = input("Enter your greeting: ")

    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
