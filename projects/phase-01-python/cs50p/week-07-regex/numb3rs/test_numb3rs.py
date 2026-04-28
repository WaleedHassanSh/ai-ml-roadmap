# Tests for the program that validates whether an input is a valid IPv4 address.

from numb3rs import validate


def test_numbers_validate():
    assert validate("127.0.0.1")
    assert validate("255.255.255.255")
    assert not validate("512.512.512.512")
    assert not validate("1.2.3.1000")
    assert not validate("192.168.001.1")
    assert validate("1.2.3.4")
    assert validate("255.255.255.0")
    assert not validate("275.3.6.28")


def test_strings_validate():
    assert not validate("cat")
