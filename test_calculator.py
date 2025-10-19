import pytest
from calculator import add

def test_add_normal():

    assert add(2, 3) == 5


def test_add_with_zero():

    assert add(0, 5) == 5


def test_add_invalid_type():

    with pytest.raises(TypeError):
        add("a", 1)

