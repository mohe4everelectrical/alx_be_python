#!/usr/bin/env python3
"""
explore_datetime.py
Demonstrates the use of Python's datetime module for handling dates and times.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    Returns the current date and time as a datetime object.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days_to_add, start_date=None):
    """
    Calculate a future date by adding days to a given start date.
    
    Args:
        days_to_add (int): Number of days to add
        start_date (datetime, optional): Starting date. Defaults to current date.
    
    Returns:
        datetime: The future date
    """
    if start_date is None:
        start_date = datetime.now()
    
    future_date = start_date + timedelta(days=days_to_add)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")
    return future_date

def main():
    """Main function to run the datetime exploration."""
    # Part 1: Display current date and time
    print("=== Part 1: Current Date and Time ===")
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    print("\n=== Part 2: Future Date Calculation ===")
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        calculate_future_date(days_to_add, current_date)
        
    except ValueError:
        print("Error: Please enter a valid integer number of days.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
