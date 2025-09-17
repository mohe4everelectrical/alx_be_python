#!/usr/bin/env python3
"""
Multiplication Table Generator
Generates and prints the multiplication table for a given number from 1 to 10
"""

def main():
    # Prompt user for a number
    try:
        number = float(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    # Generate and print the multiplication table using a for loop
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
