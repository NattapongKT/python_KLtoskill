import logging
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

# --- 1. Configuration & Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- 2. Enums & Models ---
class BookStatus(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"
    MAINTENANCE = "Maintenance"

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    status: BookStatus = BookStatus.AVAILABLE

    def __str__(self) -> str:
        return f"[{self.isbn}] {self.title:20} | {self.author:15} | {self.status.value}"

# --- 3. Library Service (Business Logic) ---
class Library:
    def __init__(self):
        self._books: Dict[str, Book] = {} # Key คือ ISBN

    def add_book(self, book: Book) -> None:
        self._books[book.isbn] = book
        logging.info(f"ADD: เพิ่มหนังสือใหม่ '{book.title}' (ISBN: {book.isbn})")

    def find_book(self, isbn: str) -> Optional[Book]:
        return self._books.get(isbn)

    def borrow_book(self, isbn: str, member_name: str) -> bool:
        book = self.find_book(isbn)
        
        if not book:
            logging.error(f"BORROW FAIL: ไม่พบหนังสือ ISBN {isbn}")
            return False
            
        if book.status == BookStatus.AVAILABLE:
            book.status = BookStatus.BORROWED
            logging.info(f"BORROW: '{member_name}' ยืมหนังสือ '{book.title}' สำเร็จ")
            return True
        
        logging.warning(f"BORROW FAIL: '{book.title}' ไม่พร้อมให้ยืม (สถานะ: {book.status.value})")
        return False

    def return_book(self, isbn: str) -> bool:
        book = self.find_book(isbn)
        if book and book.status == BookStatus.BORROWED:
            book.status = BookStatus.AVAILABLE
            logging.info(f"RETURN: คืนหนังสือ '{book.title}' เข้าชั้นวางสำเร็จ")
            return True
        logging.error(f"RETURN FAIL: ไม่สามารถคืนหนังสือ ISBN {isbn} ได้")
        return False

    def get_all_books(self) -> List[Book]:
        return list(self._books.values())

# --- 4. UI / Main Controller ---
def main():
    my_lib = Library()
    
    # Mock Data
    my_lib.add_book(Book("978-1", "Clean Code", "Robert C. Martin"))
    my_lib.add_book(Book("978-2", "The Pragmatic Programmer", "Andrew Hunt"))
    my_lib.add_book(Book("978-3", "Python Crash Course", "Eric Matthes"))

    while True:
        print("\n=== 📚 Smart Library System ===")
        print("1. ดูหนังสือทั้งหมด")
        print("2. ยืมหนังสือ")
        print("3. คืนหนังสือ")
        print("4. ออกจากระบบ")
        
        choice = input("เลือกเมนู (1-4): ")

        if choice == "1":
            print("\n" + "-"*50)
            for b in my_lib.get_all_books():
                print(b)
            print("-"*50)

        elif choice == "2":
            isbn = input("ใส่ ISBN หนังสือที่ต้องการยืม: ")
            name = input("ชื่อผู้ยืม: ")
            if not my_lib.borrow_book(isbn, name):
                print("❌ การยืมไม่สำเร็จ ตรวจสอบสถานะหนังสือหรือ ISBN อีกครั้ง")

        elif choice == "3":
            isbn = input("ใส่ ISBN หนังสือที่ต้องการคืน: ")
            if not my_lib.return_book(isbn):
                print("❌ การคืนไม่สำเร็จ ตรวจสอบ ISBN อีกครั้ง")

        elif choice == "4":
            logging.info("SYSTEM: ปิดระบบห้องสมุด")
            break
        else:
            print("❌ ตัวเลือกไม่ถูกต้อง")

if __name__ == "__main__":
    main()