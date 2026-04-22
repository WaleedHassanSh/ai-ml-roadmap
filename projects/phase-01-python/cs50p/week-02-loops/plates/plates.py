# A program that determines whether a vanity license plate is valid according to the following rules:
# 1. All vanity plates must start with at least two letters.
# 2. Vanity plates may contain a maximum of 6 characters (letters or numbers).
# 3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, "AAA222" is valid, but "AA2AAA" is not valid.
# 4. The first number used cannot be a "0".


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            if not s[i:].isdigit():
                return False

    return True


main()
