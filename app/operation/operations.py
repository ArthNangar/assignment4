"""
Author: Arth Nangar
Date: 2025-09-30
Arithmetic operations
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b
