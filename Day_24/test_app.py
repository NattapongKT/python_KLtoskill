import pytest
from app import add_numbers, is_adult

# ทดสอบเคสปกติ
def test_add_numbers_positive():
    assert add_numbers(10, 20) == 30
    assert add_numbers(1.5, 2.5) == 4.0

# ทดสอบ Boolean
def test_is_adult():
    assert is_adult(20) is True
    assert is_adult(17) is False

# ทดสอบ Error (Exception) ว่ามีการ raise ออกมาจริงๆ ไหม
def test_is_adult_negative_error():
    with pytest.raises(ValueError):
        is_adult(-1)