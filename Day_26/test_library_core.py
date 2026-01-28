import pytest
from library_core import BookManager

@pytest.fixture
def manager():
    return BookManager()

def test_add_book_success(manager):
    assert manager.add_book("123", "Python 101") is True

def test_add_book_fail_empty_data(manager):
    # ทดสอบกรณีข้อมูลว่าง (Edge Case)
    assert manager.add_book("", "") is False

def test_borrow_success(manager):
    manager.add_book("123", "Clean Code")
    assert manager.borrow_book("123") is True
    assert manager.books["123"]["available"] is False

def test_borrow_fail_not_found(manager):
    # ทดสอบกรณีหาหนังสือไม่เจอ
    assert manager.borrow_book("999") is False

def test_borrow_fail_already_borrowed(manager):
    manager.add_book("123", "Refactoring")
    manager.borrow_book("123") # ยืมครั้งแรก
    assert manager.borrow_book("123") is False # ยืมซ้ำต้องไม่ได้