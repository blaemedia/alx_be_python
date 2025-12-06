class Book:
    """Base class for all types of books"""
    
    def __init__(self, title: str, author: str):
        """
        Initialize a book with title and author
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation of the book"""
        return f"'{self.title}' by {self.author}"
    
    def get_info(self):
        """Return basic book information as a string"""
        return str(self)


class EBook(Book):
    """Derived class for electronic books"""
    
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize an ebook with title, author, and file size
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in kilobytes
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation of the ebook"""
        return f"{super().__str__()} [EBook, Size: {self.file_size}KB]"
    
    def get_info(self):
        """Return ebook information including file size"""
        return str(self)


class PrintBook(Book):
    """Derived class for physical printed books"""
    
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize a print book with title, author, and page count
        
        Args:
:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation of the print book"""
        return f"{super().__str__()} [Print Book, Pages: {self.page_count}]"
    
    def get_info(self):
        """Return print book information including page count"""
        return str(self)


class Library:
    """Library class demonstrating composition by managing a collection of books"""
    
    def __init__(self, name: str):
        """
        Initialize a library with a name
        
        Args:
            name (str): The name of the library
        """
        self.name = name
        self.books = []  # This demonstrates composition - Library HAS-A collection of Books
    
    def __str__(self):
        """String representation of the library"""
        return f"Library: {self.name} ({len(self.books)} books)"
    
    def add_book(self, book):
        """
        Add a book to the library collection
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        if not isinstance(book, Book):
            raise TypeError(f"Cannot add object of type {type(book).__name__}. Must be a Book, EBook, or PrintBook.")
        
        self.books.append(book)
        print(f"Added: {book}")
    
    def list_books(self):
        """Print details of all books in the library"""
        if not self.books:
            print(f"The library '{self.name}' has no books.")
            return
        
        print(f"\n=== Books in '{self.name}' Library ===\n")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print(f"\nTotal books: {len(self.books)}")
    
    def get_books_by_type(self):
        """Count books by type (for demonstration)"""
        counts = {
            "Book": 0,
            "EBook": 0,
            "PrintBook": 0
        }
        
        for book in self.books:
            if isinstance(book, EBook):
                counts["EBook"] += 1
            elif isinstance(book, PrintBook):
                counts["PrintBook"] += 1
            else:
                counts["Book"] += 1
        
        return counts