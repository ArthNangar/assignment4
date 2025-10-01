import pytest
from app.operation import operations

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert operations.add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 1, -1),
    (-1, -1, 0),
])
def test_subtract(a, b, expected):
    assert operations.subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 5, 0),
])
def test_multiply(a, b, expected):
    assert operations.multiply(a, b) == expected


def test_divide():
    assert operations.divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        operations.divide(5, 0)

def test_power():
    assert operations.power(2, 3) == 8

def test_modulo():
    assert operations.modulo(10, 3) == 1

def test_modulo_by_zero():
    with pytest.raises(ValueError):
        operations.modulo(5, 0)
