#!/usr/bin/env python3
"""
Drawing Patterns with Nested Loops
Draws a square pattern of asterisks based on user input
"""

def main():
    # Prompt user for pattern size
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
        return
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        # Use for loop to print asterisks in each row
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1

if __name__ == "__main__":
    main()
