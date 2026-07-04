# A test suite for the program that determines whether a vanity license plate is valid according to the following rules:
# 1. All vanity plates must start with at least two letters.
# 2. Vanity plates may contain a maximum of 6 characters (letters or numbers).
# 3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, "AAA222" is valid, but "AA2AAA" is not valid.
# 4. The first number used cannot be a "0".

from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AA") == True
    assert is_valid("ABC123") == True


def test_beginning_letters():
    assert is_valid("50CS") == False
    assert is_valid("A123") == False
    assert is_valid("1ABC") == False


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_number_placement():
    assert is_valid("CS50P") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AB12C") == False


def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("ABC012") == False


def test_alphanumeric():
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("HELLO!") == False
