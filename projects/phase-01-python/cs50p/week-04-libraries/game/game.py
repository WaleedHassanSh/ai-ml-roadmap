# A simple number guessing game where the user is prompted to guess a randomly generated number within a specified range. The user can choose the difficulty level, which determines the range of the random number. The program provides feedback on whether the user's guess is too low, too high, or correct, and continues until the user guesses the number correctly.

import random

while True:
    try:
        level = int(input("Level: ").strip())

        if level < 1:
            continue
        break

    except ValueError:
        continue

value = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: ").strip())

        if guess < 1:
            continue

        elif guess < value:
            print("Too small!")

        elif guess > value:
            print("Too large!")

        else:
            print("Just right!")
            break

    except ValueError:
        continue
