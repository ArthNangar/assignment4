import pytest
from app.calculation.calculation import CalculationFactory, Calculation

def test_calculation_perform_add():
    calc = CalculationFactory.create(2, 3, "add")
    assert calc.perform() == 5

def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create(2, 2, "power")

@pytest.mark.parametrize("a,b,op,expected", [
    (2, 3, "add", 5),
    (5, 2, "sub", 3),
    (3, 4, "mul", 12),
    (10, 2, "div", 5),
])
def test_factory_operations(a, b, op, expected):
    calc = CalculationFactory.create(a, b, op)
    assert calc.perform() == expected

def test_power_operation():
    calc = CalculationFactory.create(2, 3, "pow")
    assert calc.perform() == 8

def test_modulo_operation():
    calc = CalculationFactory.create(10, 3, "mod")
    assert calc.perform() == 1
