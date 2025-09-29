class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
    
    def find_book(self, title):
        """
        Find a book by title (case-insensitive).
        
        Args:
            title (str): The title to search for
            
        Returns:
            Book or None: The book if found, None otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def get_total_books(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def get_available_books_count(self):
        """
        Get the number of available books.
        
        Returns:
            int: Number of available books
        """
        return len([book for book in self._books if book.is_available()])



# Additional test script: test_library.py
from library_management import Book, Library

def additional_tests():
    library = Library()
    
    # Add multiple books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    
    print("Initial available books:")
    library.list_available_books()
    
    # Test checking out a book
    print("\nChecking out 'The Great Gatsby'...")
    library.check_out_book("The Great Gatsby")
    library.list_available_books()
    
    # Test checking out same book again
    print("\nTrying to check out 'The Great Gatsby' again...")
    library.check_out_book("The Great Gatsby")
    
    # Test returning the book
    print("\nReturning 'The Great Gatsby'...")
    library.return_book("The Great Gatsby")
    library.list_available_books()
    
    # Test returning a book that wasn't checked out
    print("\nTrying to return a book that wasn't checked out...")
    library.return_book("Pride and Prejudice")
    
    # Test non-existent book
    print("\nTrying to check out non-existent book...")
    library.check_out_book("Non-existent Book")

if __name__ == "__main__":
    additional_tests()
