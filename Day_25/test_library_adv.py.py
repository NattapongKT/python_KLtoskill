import pytest
from unittest.mock import MagicMock
from library_service import LibraryService, EmailService

# --- [Fixture]: สร้าง Object เริ่มต้นไว้ใช้ในทุกๆ Test ---
@pytest.fixture
def mock_email_service():
    return MagicMock(spec=EmailService)

@pytest.fixture
def library(mock_email_service):
    # ฉีด (Inject) Mock เข้าไปแทนที่ EmailService จริง
    return LibraryService(mock_email_service)


# --- [Test Cases with Edge Cases] ---

def test_borrow_success_and_send_email(library, mock_email_service):
    """Edge Case: ยืมสำเร็จและต้องมั่นใจว่ามีการเรียกใช้ EmailService จริงๆ"""
    result = library.borrow_book("978")
    
    assert result == "Success"
    assert library.books["978"]["available"] is False
    # ตรวจสอบว่าฟังก์ชันส่ง Email ถูกเรียกใช้ 1 ครั้งพอดี (Mock check)
    mock_email_service.send_notification.assert_called_once()

def test_borrow_book_not_found(library, mock_email_service):
    """Edge Case: ยืมหนังสือที่ไม่มีในระบบ"""
    result = library.borrow_book("000")
    
    assert result == "Book not found"
    # ต้องมั่นใจว่าถ้าหาหนังสือไม่เจอ ห้ามมีการส่ง Email เด็ดขาด
    mock_email_service.send_notification.assert_not_called()

def test_borrow_already_borrowed_edge_case(library, mock_email_service):
    """Edge Case: ยืมหนังสือที่มีคนยืมไปแล้ว"""
    library.borrow_book("978") # ยืมครั้งแรก
    mock_email_service.reset_mock() # รีเซ็ตการนับของ Mock
    
    result = library.borrow_book("978") # พยายามยืมครั้งที่สอง
    
    assert result == "Already borrowed"
    mock_email_service.send_notification.assert_not_called()