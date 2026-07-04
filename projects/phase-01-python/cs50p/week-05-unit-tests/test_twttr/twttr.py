# A program that takes a string of text as input and outputs the same text but with all vowels removed.


def main():
    text = input("Enter a string of text: ")

    print(shorten(text))


def shorten(word):
    final = ""

    for v in word:
        if v.lower() not in ["a", "e", "i", "o", "u"]:
            final += v

    return final


if __name__ == "__main__":
    main()
