#!/usr/bin/env python3
"""
temp_conversion_tool.py
Temperature conversion tool demonstrating global variable scope.
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
TEMPERATURE_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius
    """
    # Access global conversion factor (reading only, no need for global keyword)
    celsius = (fahrenheit - TEMPERATURE_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature converted to Fahrenheit
    """
    # Access global conversion factor (reading only, no need for global keyword)
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + TEMPERATURE_OFFSET
    return fahrenheit

def get_temperature_input():
    """
    Get and validate temperature input from user.
    
    Returns:
        float: Validated temperature value
    
    Raises:
        ValueError: If input cannot be converted to float
    """
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """
    Get and validate temperature unit input from user.
    
    Returns:
        str: Validated unit ('C' or 'F')
    
    Raises:
        ValueError: If input is not 'C' or 'F'
    """
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit

def main():
    """Main function to run the temperature conversion tool."""
    print("=== Temperature Conversion Tool ===")
    print("Converts between Celsius and Fahrenheit")
    print("=" * 40)
    
    try:
        # Get temperature input
        temperature = get_temperature_input()
        
        # Get unit input
        unit = get_unit_input()
        
        # Perform conversion based on unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Alternative simpler version without separate input validation functions
def simple_version():
    """Simpler version without separate validation functions."""
    print("=== Temperature Conversion Tool (Simple Version) ===")
    
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError:
        print("Error: Invalid temperature. Please enter a numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the main version (you can change this to simple_version() if preferred)
    main()
