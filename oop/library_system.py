# Base Class - Book
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Derived Class - EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)        # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} - EBook ({self.file_size}MB)"


# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} - Print ({self.page_count} pages)"


# Composition - Library Class
class Library:
    def __init__(self):
        self.books = []       # Stores Book, EBook, PrintBook instances

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
