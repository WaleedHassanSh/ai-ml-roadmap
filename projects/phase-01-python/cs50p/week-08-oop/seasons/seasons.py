# A program that converts a birthdate into age in minutes written in English words.

import sys
from datetime import date

import inflect

p = inflect.engine()


def parse_birthdate(dob):
    try:
        year, month, day = dob.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Invalid Format")


def minutes_since_birth(birth_date, today=date.today()):
    difference = today - birth_date
    return difference.days * 24 * 60


def words(minutes):
    return p.number_to_words(minutes, andword="")


def main():
    dob = input("Date of Birth: ")

    try:
        birth_date = parse_birthdate(dob)
    except ValueError:
        sys.exit("Invalid Format")

    minutes = minutes_since_birth(birth_date)
    print(f"{words(minutes).capitalize()} minutes")


if __name__ == "__main__":
    main()
