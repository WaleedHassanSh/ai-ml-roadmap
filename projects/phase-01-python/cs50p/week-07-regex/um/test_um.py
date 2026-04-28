# Tests for the program that counts how many times "um" appears in text as a standalone word.

from um import count


def test_0_count():
    assert count("yum") == 0
    assert count("yummy") == 0


def test_1_count():
    assert count("hello, um, world") == 1
    assert count("um...") == 1
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_2_count():
    assert count("um, hello, um, world") == 2
    assert count("Um, thanks, um...") == 2
