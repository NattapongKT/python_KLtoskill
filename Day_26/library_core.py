class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title):
        if not isbn or not title:
            return False
        self.books[isbn] = {"title": title, "available": True}
        return True

    def borrow_book(self, isbn):
        if isbn in self.books and self.books[isbn]["available"]:
            self.books[isbn]["available"] = False
            return True
        return False