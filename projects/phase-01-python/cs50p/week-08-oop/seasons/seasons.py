# A program that converts a birthdate into age in minutes written in English words.

import sys
from datetime import date
from typing import Any, cast

import inflect

p = inflect.engine()


def parse_birthdate(dob: str) -> date:
    try:
        year, month, day = dob.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        raise ValueError("Invalid Format")


def minutes_since_birth(birth_date: date, today: date | None = None) -> int:
    if today is None:
        today = date.today()

    difference = today - birth_date
    return difference.days * 24 * 60


def words(minutes: int) -> str:
    engine = cast(Any, p)
    return cast(str, engine.number_to_words(minutes, andword=""))


def main() -> None:
    dob = input("Date of Birth: ")

    try:
        birth_date = parse_birthdate(dob)
    except ValueError:
        sys.exit("Invalid Format")

    minutes = minutes_since_birth(birth_date)
    minute_words = words(minutes)

    print(f"{minute_words.capitalize()} minutes")


if __name__ == "__main__":
    main()
