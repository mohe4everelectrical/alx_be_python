#!/usr/bin/env python3
"""
Demonstrating Class Methods and Static Methods in Python.
"""

class Calculator:
    """
    A class that includes examples of a class method and a static method
    to perform basic arithmetic operations.
    """
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: int, b: int) -> int:
        """
        Static Method: Returns the sum of two numbers.
        Does not access class or instance attributes/methods.
        """
        return a + b

    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        """
        Class Method: Returns the product of two numbers.
        Takes 'cls' as the first argument, allowing access to class attributes
        like 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Note: The provided main.py handles the testing logic.
