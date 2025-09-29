def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.
    
    Args:
        numerator: The numerator as a string (to be converted to float)
        denominator: The denominator as a string (to be converted to float)
        
    Returns:
        str: Either the division result as a string or an error message
    """
    try:
        # Try to convert inputs to floats
        num_float = float(numerator)
        den_float = float(denominator)
        
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
    
    try:
        # Try to perform division
        result = num_float / den_float
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

# Alternative implementation with more detailed error messages:
"""
def safe_divide(numerator, denominator):
    # Check if inputs can be converted to numbers
    try:
        num_float = float(numerator)
    except ValueError:
        return f"Error: '{numerator}' is not a valid numeric value."
    
    try:
        den_float = float(denominator)
    except ValueError:
        return f"Error: '{denominator}' is not a valid numeric value."
    
    # Check for division by zero
    if den_float == 0:
        return "Error: Cannot divide by zero."
    
    # Perform division
    result = num_float / den_float
    return f"The result of the division is {result}"
"""

import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly 2 arguments are provided (plus the script name)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
