class EmailService:
    def send_notification(self, message: str):
        # ในความเป็นจริงตรงนี้ต้องเชื่อมต่อ Server และใช้เวลาส่งจริง
        print(f"Sending real email: {message}")
        return True

class LibraryService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
        self.books = {"978": {"title": "Python 101", "available": True}}

    def borrow_book(self, isbn: str):
        if isbn not in self.books:
            return "Book not found"
        
        book = self.books[isbn]
        if book["available"]:
            book["available"] = False
            self.email_service.send_notification(f"You borrowed {book['title']}")
            return "Success"
        return "Already borrowed"