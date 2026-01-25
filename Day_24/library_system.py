from dataclasses import dataclass
from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"

@dataclass
class Book:
    isbn: str
    title: str
    status: BookStatus = BookStatus.AVAILABLE

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def borrow_book(self, isbn: str) -> bool:
        if isbn not in self.books:
            return False
        book = self.books[isbn]
        if book.status == BookStatus.AVAILABLE:
            book.status = BookStatus.BORROWED
            return True
        return False