# A program that converts a camelCase variable name to snake_case.

name = input("camelCase: ")

for s in name:
    if s.isupper():
        print(end="_")
        print(s.lower(), end="")
    else:
        print(s, end="")

print()
