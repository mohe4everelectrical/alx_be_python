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


from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book

if __name__ == "__main__":
    main()

from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)
    print(repr(my_book))
    del my_book

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
Test script for the Library System

This script tests the inheritance and composition functionality
of the Book, EBook, PrintBook, and Library classes.
"""

from library_system import Book, EBook, PrintBook, Library

def main():
    """Test the library system functionality."""
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

def additional_tests():
    """Run additional tests to demonstrate more functionality."""
    print("\n=== Additional Tests ===")
    
    # Create another library
    test_library = Library()
    
    # Test adding more diverse books
    scifi_ebook = EBook("Dune", "Frank Herbert", 3500)
    fantasy_print = PrintBook("The Hobbit", "J.R.R. Tolkien", 310)
    classic_book2 = Book("1984", "George Orwell")
    
    test_library.add_book(scifi_ebook)
    test_library.add_book(fantasy_print)
    test_library.add_book(classic_book2)
    
    test_library.list_books()
    
    # Test finding books by author
    print("Books by George Orwell:")
    orwell_books = test_library.find_books_by_author("George Orwell")
    for book in orwell_books:
        print(f"  - {book.get_info()}")

if __name__ == "__main__":
    main()
    additional_tests()
