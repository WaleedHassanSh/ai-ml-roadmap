# A test file for the bank.py program, which calculates the value of a given string of text based on specific rules. This test file uses assertions to verify that the value function works correctly with various inputs, including different words, numbers, whitespace, and case sensitivity.

from bank import value


def test_text():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("what's up?") == 100


def test_numbers():
    assert value("123") == 100
    assert value("h123") == 20
    assert value("hello123") == 0


def test_whitespace():
    assert value("   hello   ") == 0
    assert value("   hi   ") == 20
    assert value("   what's up?   ") == 100


def test_case_insensitivity():
    assert value("Hello") == 0
    assert value("HI") == 20
    assert value("hEy") == 20
    assert value("WHAT'S UP?") == 100
