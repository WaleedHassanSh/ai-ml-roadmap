# Asks for the user's name and greets them, replacing :) with 🙂 and :( with 🙁.


def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")

    return x


def main():
    name = input("What's your name? ")
    name = convert(name)

    print(f"Hello, {name}!")


main()
