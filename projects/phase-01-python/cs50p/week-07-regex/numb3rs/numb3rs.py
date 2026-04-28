# A program that validates whether an input is a valid IPv4 address.

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
    match = re.search(pattern, ip)

    if match:
        parts = match.group().split(".")

        for part in parts:
            if len(part) > 1 and part.startswith("0"):
                return False

            number = int(part)
            if not 0 <= number <= 255:
                return False

        return True

    else:
        return False


if __name__ == "__main__":
    main()
