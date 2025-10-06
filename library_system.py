#!/usr/bin/env python3
"""
Library System with Inheritance and Composition

This module demonstrates:
- Inheritance: EBook and PrintBook inherit from Book
- Composition: Library contains a collection of Book objects
"""

class Book:
    """
    Base class representing a generic book.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def get_info(self):
        """
        Return basic information about the book.
        
        Returns:
            str: Book information in format "Book: {title} by {author}"
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    
    Inherits from Book and adds file_size attribute.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def get_info(self):
        """
        Return information about the ebook including file size.
        
        Returns:
            str: EBook information with file size
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a physical printed book.
    
    Inherits from Book and adds page_count attribute.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def get_info(self):
        """
        Return information about the print book including page count.
        
        Returns:
            str: PrintBook information with page count
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class representing a library that manages a collection of books.
    
    Demonstrates composition by containing Book objects.
    
    Attributes:
        books (list): A list to store Book, EBook, and PrintBook instances
    """
    
    def __init__(self):
        """Initialize an empty library."""
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance to add to the library
            
        Raises:
            TypeError: If the provided object is not a Book instance
        """
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library")
        
        self.books.append(book)
        print(f"Added: {book.title}")
    
    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\n=== Library Collection ===")
        for book in self.books:
            print(book.get_info())
        print("==========================\n")
    
    def find_books_by_author(self, author):
        """
        Find all books by a specific author.
        
        Args:
            author (str): The author to search for
            
        Returns:
            list: List of books by the specified author
        """
        return [book for book in self.books if book.author.lower() == author.lower()]
    
    def get_total_books(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self.books)


# Demonstration code (optional - for testing the module directly)
if __name__ == "__main__":
    # Create a library instance
    library = Library()
    
    # Create different types of books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook1 = EBook("Digital Fortress", "Dan Brown", 1200)
    printbook1 = PrintBook("To Kill a Mockingbird", "Harper Lee", 281)
    
    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)
    
    # List all books
    library.list_books()
    
    # Show library statistics
    print(f"Total books in library: {library.get_total_books()}")
