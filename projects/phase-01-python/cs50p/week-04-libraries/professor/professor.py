# A simple program that quizzes the user on addition problems. The user can choose a difficulty level, and the program will generate random addition problems accordingly. The user has three attempts to answer each problem correctly, and the program keeps track of the score.

import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        choice = 0

        while True:
            try:
                guess = int(input(f"{x} + {y} = "))

            except ValueError:
                if choice == 2:
                    break

                choice += 1
                print("EEE")
                continue

            if guess == answer:
                score += 1
                break

            elif choice == 2:
                print(f"{x} + {y} = {answer}")
                break

            else:
                choice += 1
                print("EEE")
                continue

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)

    if level == 2:
        return random.randint(10, 99)

    if level == 3:
        return random.randint(100, 999)

    else:
        raise ValueError


if __name__ == "__main__":
    main()
