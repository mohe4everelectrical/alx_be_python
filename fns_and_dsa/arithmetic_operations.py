#!/usr/bin/env python3
"""
Arithmetic Operations Module
Contains function to perform basic arithmetic operations
"""


def perform_operation(num1: float, num2: float, operation: str) -> float or str:
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the arithmetic operation or error message for division by zero
    """
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from: add, subtract, multiply, divide"

#!/usr/bin/env python3
"""
Arithmetic Operations Module
Contains function to perform basic arithmetic operations
"""


def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1: First number
        num2: Second number
        operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Result of the arithmetic operation or error message for division by zero
    """
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from: add, subtract, multiply, divide"


