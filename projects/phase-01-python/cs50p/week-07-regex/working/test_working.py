# Tests for the program that converts times from 12-hour format to 24-hour format.

import pytest
from working import convert


def test_valid_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_12_am_pm():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
