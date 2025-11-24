class Book:
    def __init__(self, title, author):
        """Initialize a Book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    @property
    def is_checked_out(self):
        """Get the checkout status (read-only access to private attribute)."""
        return self._is_checked_out

    def check_out(self):
        """Check out the book if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        """String representation of the book."""
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self._books = []  # Private list to store books

    def add_book(self, title, author):
        """Add a new book to the library."""
        book = Book(title, author)
        self._books.append(book)
        print(f"Added '{title}' by {author} to the library.")

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                    return True
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if not book.is_checked_out]
        
        if not available_books:
            print("No available books in the library.")
            return []
        
        print("Available books:")
        for book in available_books:
            print(f"  - '{book.title}' by {book.author}")
        
        return available_books

    def list_all_books(self):
        """List all books in the library with their status (for debugging)."""
        if not self._books:
            print("The library is empty.")
            return []
        
        print("All books in the library:")
        for book in self._books:
            print(f"  - {book}")
        
        return self._books