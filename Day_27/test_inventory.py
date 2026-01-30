import pytest
from inventory_system import Inventory

@pytest.fixture
def store():
    return Inventory()

def test_add_stock_correctly(store):
    # เรามีแอปเปิ้ล 10 เพิ่มอีก 5 ต้องเป็น 15
    store.add_stock("apple", 5)
    assert store.stocks["apple"] == 15  # <--- จุดนี้จะ FAIL เพราะ BUG 1

def test_remove_stock_exact_amount(store):
    # เรามีส้ม 5 ลูก ถ้าเอาออก 5 ลูกพอดี ต้องทำได้ (เหลือ 0)
    result = store.remove_stock("orange", 5)
    assert result is True            # <--- จุดนี้จะ FAIL เพราะ BUG 2
    assert store.stocks["orange"] == 0