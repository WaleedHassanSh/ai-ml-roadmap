# A program that prints a half-pyramid of a specified height, using hashes (#) for blocks and spaces for padding.

while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break

    except ValueError:
        continue

for i in range(1, height + 1):
    height -= 1
    print(" " * height, end="")
    print("#" * i)
