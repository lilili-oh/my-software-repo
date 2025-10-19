import pytest
from calculator import add
from calculator import subtract

def test_add_normal():

    assert add(2, 3) == 5


def test_add_with_zero():

    assert add(0, 5) == 5


def test_add_invalid_type():

    with pytest.raises(TypeError):
        add("a", 1)

# tests/test_subtract.py

def test_subtract_normal():
    assert subtract(5, 3) == 2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_negative():
    assert subtract(3, 5) == -2
