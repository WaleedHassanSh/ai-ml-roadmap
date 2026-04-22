# A program that takes a string of text as input and outputs the same text but with all vowels removed.

text = input("Enter a string of text: ")

for c in text:
    if c.lower() not in "aeiou":
        print(c, end="")

print()
