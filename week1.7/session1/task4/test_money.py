# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"


def test_invalid_type_pence():
    # complete the test implementation for 
    # invalid type for pence
    with pytest.raises(TypeError) as info:
        Money(2, "alot")
    assert str(info.value) == "pence must be an integer"

def test_invalid_value_pence():
    # complete the test implementation for 
    # invalid value for pence
    with pytest.raises(ValueError) as info:
        Money(2, 300)
    assert str(info.value) == "pence must be in range 0-99"
    

def test_valid_add():
    # complete the test implementation for
    # valid add between money objects
    # Hint: you can compare using the __str()__ (
    # e.g., str(m1 + m2) == "£2.04"
    assert str(Money(2, 5) + Money(3, 2)) == str(Money(5, 7))