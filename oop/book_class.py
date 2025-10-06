#!/usr/bin/env python3
"""
Book Class Implementation
A class demonstrating the use of Python magic methods:
__init__ (constructor), __del__ (destructor),
__str__ (string representation), and __repr__ (official representation).
"""

class Book:
    """
    Models a book with a title, author, and publication year.
    """
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional line for tracking creation

    def __del__(self):
        """
        Destructor: Called when the Book instance is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Provides a readable string for the user.

        Returns:
            str: A formatted string: "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Provides an unambiguous string that could
        recreate the object.

        Returns:
            str: A formatted string: f"Book('{self.title}', '{self.author}', {self.year})".
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: The provided main.py handles the testing logic.
# The following is just to demonstrate the class works in isolation.
# if __name__ == '__main__':
#     b = Book("Dune", "Frank Herbert", 1965)
#     print(str(b))
#     print(repr(b))
#     del b
