#!/usr/bin/env python3
"""
Library System: Demonstrating Inheritance and Composition in Python.

Classes defined:
- Book (Base Class)
- EBook (Derived Class)
- PrintBook (Derived Class)
- Library (Composition Class)
"""

class Book:
    """
    Base class for all book types.
    """
    def __init__(self, title, author):
        """
        Initializes the common attributes of a book.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Provides a basic string representation for the Book class.
        """
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook, calling the base class constructor first.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            file_size (int): The size of the book file in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Provides a specific string representation for the EBook class.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """
    Represents a physical printed book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook, calling the base class constructor first.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            page_count (int): The number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Provides a specific string representation for the PrintBook class.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Represents a library that manages a collection of books (Composition).
    """
    def __init__(self):
        """
        Initializes the Library with an empty list to hold book instances.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.

        Args:
            book (Book): An instance of Book or any derived class.
        """
        if isinstance(book, Book):
            self.books.append(book)
        # else: # Optional: add validation/error handling

    def list_books(self):
        """
        Prints the details of every book in the library using the __str__ method
        of each book object.
        """
        for book in self.books:
            print(book)
