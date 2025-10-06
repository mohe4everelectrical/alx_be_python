#!/usr/bin/env python3
"""
Book Class Implementation with Magic Methods

This module defines a Book class that demonstrates the use of Python magic methods
including __init__, __del__, __str__, and __repr__.
"""

class Book:
    """
    A class to represent a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    
    Magic Methods:
        __init__: Constructor to initialize book attributes
        __del__: Destructor that prints a message when object is deleted
        __str__: Returns user-friendly string representation
        __repr__: Returns developer-friendly string representation
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance with title, author, and publication year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
            
        Raises:
            TypeError: If title or author is not string, or year is not integer
        """
        # Input validation
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        
        # Initialize instance attributes
        self.title = title
        self.author = author
        self.year = year
        
        print(f"Book '{self.title}' created successfully!")
    
    def __del__(self):
        """
        Destructor method that prints a message when the object is deleted.
        
        This method is automatically called when the object is about to be destroyed
        or when there are no more references to the object.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the Book.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the Book.
        
        The returned string should be a valid Python expression that could be used
        to recreate the object with the same state.
        
        Returns:
            str: String in format "Book('Title', 'Author', Year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    # Additional utility methods for better functionality
    def get_age(self, current_year: int = 2024) -> int:
        """
        Calculate the age of the book in years.
        
        Args:
            current_year (int): The current year to calculate age from
            
        Returns:
            int: Age of the book in years
        """
        return current_year - self.year
    
    def is_classic(self, threshold_year: int = 1950) -> bool:
        """
        Check if the book is considered a classic based on publication year.
        
        Args:
            threshold_year (int): Year threshold for classic status
            
        Returns:
            bool: True if book is older than threshold, False otherwise
        """
        return self.year < threshold_year


# Additional demonstration functions
def demonstrate_book_operations():
    """Demonstrate various operations with the Book class."""
    print("\n=== Book Class Demonstration ===")
    
    # Create multiple book instances
    books = [
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("Pride and Prejudice", "Jane Austen", 1813),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    ]
    
    print("\n--- String Representations ---")
    for book in books:
        print(f"str:  {book}")
        print(f"repr: {repr(book)}")
        print(f"Age: {book.get_age()} years")
        print(f"Classic: {book.is_classic()}")
        print("-" * 40)
    
    return books


if __name__ == "__main__":
    # Run demonstration when script is executed directly
    books = demonstrate_book_operations()
    
    # Explicitly delete books to trigger __del__ method
    print("\n--- Cleaning up books ---")
    del books
    print("All books deleted!")



#!/usr/bin/env python3
"""
Test script for the Book class

This script demonstrates the functionality of the Book class
including all implemented magic methods.
"""

from book_class import Book

def main():
    """
    Main function to test Book class functionality.
    """
    print("=== Testing Book Class Magic Methods ===\n")
    
    # Creating an instance of Book
    print("1. Creating a Book instance:")
    my_book = Book("1984", "George Orwell", 1949)
    print()
    
    # Demonstrating the __str__ method
    print("2. Testing __str__ method:")
    print(my_book)  # Expected to use __str__
    print()
    
    # Demonstrating the __repr__ method
    print("3. Testing __repr__ method:")
    print(repr(my_book))  # Expected to use __repr__
    print()
    
    # Testing additional functionality
    print("4. Testing utility methods:")
    print(f"Book age: {my_book.get_age()} years")
    print(f"Is classic: {my_book.is_classic()}")
    print()
    
    # Creating another book for comparison
    print("5. Creating another book:")
    modern_book = Book("The Hunger Games", "Suzanne Collins", 2008)
    print(f"Book age: {modern_book.get_age()} years")
    print(f"Is classic: {modern_book.is_classic()}")
    print()
    
    # Demonstrating object recreation from repr
    print("6. Demonstrating object recreation from __repr__:")
    book_repr = repr(my_book)
    print(f"Repr string: {book_repr}")
    
    # Note: In practice, you could use eval(book_repr) to recreate the object
    # but we avoid eval for security reasons in production code
    print("(Object can be recreated using the repr string)")
    print()
    
    # Deleting book instances to trigger __del__
    print("7. Triggering destructors:")
    del my_book
    del modern_book

def test_edge_cases():
    """
    Test edge cases and error handling for the Book class.
    """
    print("\n=== Testing Edge Cases ===\n")
    
    try:
        # Test with invalid title type
        bad_book = Book(123, "George Orwell", 1949)
    except TypeError as e:
        print(f"Error caught: {e}")
    
    try:
        # Test with invalid author type
        bad_book = Book("1984", 123, 1949)
    except TypeError as e:
        print(f"Error caught: {e}")
    
    try:
        # Test with invalid year type
        bad_book = Book("1984", "George Orwell", "1949")
    except TypeError as e:
        print(f"Error caught: {e}")

if __name__ == "__main__":
    main()
    test_edge_cases()
    print("\n=== All tests completed ===")

=== Testing Book Class Magic Methods ===

1. Creating a Book instance:
Book '1984' created successfully!

2. Testing __str__ method:
1984 by George Orwell, published in 1949

3. Testing __repr__ method:
Book('1984', 'George Orwell', 1949)

4. Testing utility methods:
Book age: 75 years
Is classic: True

5. Creating another book:
Book 'The Hunger Games' created successfully!
Book age: 16 years
Is classic: False

6. Demonstrating object recreation from __repr__:
Repr string: Book('1984', 'George Orwell', 1949)
(Object can be recreated using the repr string)

7. Triggering destructors:
Deleting 1984
Deleting The Hunger Games

=== Testing Edge Cases ===

Error caught: Title must be a string
Error caught: Author must be a string
Error caught: Year must be an integer

=== All tests completed ===


# You can extend the Book class with more magic methods:

def __eq__(self, other):
    """Check if two books are equal."""
    if not isinstance(other, Book):
        return False
    return (self.title == other.title and 
            self.author == other.author and 
            self.year == other.year)

def __lt__(self, other):
    """Compare books by publication year."""
    if not isinstance(other, Book):
        return NotImplemented
    return self.year < other.year

def __hash__(self):
    """Make Book objects hashable."""
    return hash((self.title, self.author, self.year))


#!/usr/bin/env python3
"""
Book Class Implementation with Magic Methods

This module defines a Book class that demonstrates the use of Python magic methods
including __init__, __del__, __str__, and __repr__.
"""

class Book:
    """
    A class to represent a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        year (int): The publication year of the book
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance with title, author, and publication year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return a user-friendly string representation of the Book.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return a developer-friendly string representation of the Book.
        
        Returns:
            str: String in format "Book('Title', 'Author', Year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"





class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"



from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()



