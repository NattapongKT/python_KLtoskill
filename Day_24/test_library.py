import pytest
from library_system import Library, Book, BookStatus

# --- Test Cases ---

def test_add_book():
    """ทดสอบว่าเพิ่มหนังสือแล้วข้อมูลเข้าไปอยู่ในระบบจริงไหม"""
    # Arrange (เตรียม)
    lib = Library()
    book = Book("123", "Python Basic")
    
    # Act (ทำ)
    lib.add_book(book)
    
    # Assert (ยันยืน)
    assert len(lib.books) == 1
    assert lib.books["123"].title == "Python Basic"

def test_borrow_success():
    """ทดสอบการยืมหนังสือที่ว่างอยู่ (Success Case)"""
    lib = Library()
    lib.add_book(Book("123", "Clean Code"))
    
    # ยืมหนังสือ
    result = lib.borrow_book("123")
    
    assert result is True
    assert lib.books["123"].status == BookStatus.BORROWED

def test_borrow_fail_already_borrowed():
    """ทดสอบการยืมหนังสือที่มีคนยืมไปแล้ว (Fail Case)"""
    lib = Library()
    lib.add_book(Book("123", "Refactoring", BookStatus.BORROWED))
    
    # ลองยืมเล่มที่สถานะเป็น Borrowed อยู่แล้ว
    result = lib.borrow_book("123")
    
    assert result is False

def test_borrow_non_existent_book():
    """ทดสอบการยืมหนังสือที่ไม่มีในระบบ (Edge Case)"""
    lib = Library()
    
    result = lib.borrow_book("999") # ISBN ที่ไม่มีจริง
    
    assert result is False