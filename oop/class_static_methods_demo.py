#!/usr/bin/env python3
"""
Demonstrating Class Methods and Static Methods in Python.
"""

class Calculator:
    """
    A class that includes a static method and a class method to perform
    arithmetic operations, illustrating the difference between the two.
    """
    # Class Attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Returns the sum of two numbers.
        It operates independently and does not access class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Returns the product of two numbers.
        It takes 'cls' (the class itself) as the first argument, allowing
        it to access and print class attributes like 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
