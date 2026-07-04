# A test file for the twttr.py program, which removes vowels from a given string of text. This test file uses assertions to verify that the shorten function works correctly with various inputs, including uppercase and lowercase letters, as well as numbers and special characters.

from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"
    assert shorten("Hello123") == "Hll123"
