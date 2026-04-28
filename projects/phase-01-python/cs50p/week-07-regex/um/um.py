# A program that counts how many times "um" appears in text as a standalone word.

import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"
    counts = re.findall(pattern, s, re.IGNORECASE)

    return len(counts)


if __name__ == "__main__":
    main()
