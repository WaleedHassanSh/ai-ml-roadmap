# Asks for the user's name and greets them, replacing :) with 🙂 and :( with 🙁.


def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text


def main():
    text = input()

    print(convert(text))


main()
