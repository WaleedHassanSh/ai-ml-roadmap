# A simple program that takes a list of names as input and outputs a farewell message using the `inflect` library to format the list of names correctly.

import inflect

p = inflect.engine()

names = []

while True:
    try:
        n = input("Input: ")
        names.append(n)

    except EOFError:
        break

print()
print(f"Adieu, adieu, to {p.join(names)}")
