# A program that converts times from 12-hour format to 24-hour format.

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if match:
        hour1 = int(match.group(1))

        if match.group(2):
            minutes1 = int(match.group(2))

            if not 0 <= minutes1 < 60:
                raise ValueError

        else:
            minutes1 = 0

        hour2 = int(match.group(4))

        if match.group(5):
            minutes2 = int(match.group(5))

            if not 0 <= minutes2 < 60:
                raise ValueError

        else:
            minutes2 = 0

        if not 0 < hour1 < 13:
            raise ValueError

        if not 0 < hour2 < 13:
            raise ValueError

        if match.group(3) == "AM" and hour1 == 12:
            hour1 = 0

        if match.group(3) == "PM" and hour1 != 12:
            hour1 = hour1 + 12

        if match.group(6) == "AM" and hour2 == 12:
            hour2 = 0

        if match.group(6) == "PM" and hour2 != 12:
            hour2 = hour2 + 12

        return f"{hour1:02}:{minutes1:02} to {hour2:02}:{minutes2:02}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
