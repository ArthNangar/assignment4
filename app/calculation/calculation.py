"""
Author: Arth Nangar
Date: 2025-09-30
Calculation classes & factory
"""
from app.operation import operations

class Calculation:
    """Represents a calculation with two operands and an operation."""

    def __init__(self, a, b, func):
        self.a = float(a)
        self.b = float(b)
        self.func = func

    def perform(self):
        return self.func(self.a, self.b)


class CalculationFactory:
    """Factory to create Calculation objects."""

    @staticmethod
    def create(a, b, operation: str):
        ops = {
            "add": operations.add,
            "sub": operations.subtract,
            "mul": operations.multiply,
            "div": operations.divide,
            "pow": operations.power,
            "mod": operations.modulo,  
        }
        if operation not in ops:
            raise ValueError(f"Unsupported operation: {operation}")
        return Calculation(a, b, ops[operation])
