# Asks for the user's name and greets them with spaces replaced by ellipses.

name = input("What's your name? ")
name = name.replace(" ", "...")

print(f"Hello, {name}")
