# A series of unit tests for the fuel module, testing both the convert and gauge functions.

import pytest
from fuel import convert, gauge


def test_convert_valid_fractions():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("1/6") == 17


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1.5/4")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("-1/4")


def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_percentage():
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
