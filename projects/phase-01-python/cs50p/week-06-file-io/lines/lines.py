# A program that counts the number of lines of code in a Python file, excluding blank lines and comments.

import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        count = 0

        for line in file:
            stripped_line = line.strip()

            if stripped_line and not stripped_line.startswith("#"):
                count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
