# Tests for the program that converts a birthdate into age in minutes.

from datetime import date

import pytest
from seasons import minutes_since_birth, parse_birthdate, words


def test_parse_birthdate_valid():
    assert parse_birthdate("2000-01-01") == date(2000, 1, 1)


def test_parse_birthdate_invalid_format():
    with pytest.raises(ValueError):
        parse_birthdate("January 1, 2000")


def test_parse_birthdate_invalid_date():
    with pytest.raises(ValueError):
        parse_birthdate("2000-13-01")


def test_minutes_since_birth():
    birth_date = date(2000, 1, 1)
    today = date(2001, 1, 1)
    assert minutes_since_birth(birth_date, today) == 525600


def test_words():
    assert words(525600) == "five hundred twenty-five thousand, six hundred"
