#-----------------------------------example--------------------------------------------
#❌ โค้ดที่ "สกปรก" (Dirty Code)
# ชื่อตัวแปรแย่, ฟังก์ชันใหญ่เกินไปและทำหลายอย่าง
def p(data):
    for i in range(len(data)):
        # คำนวณภาษี
        t = data[i]['p'] * 0.07
        # คำนวณส่วนลด
        if data[i]['p'] > 1000:
            d = data[i]['p'] * 0.1
        else:
            d = 0
        final = data[i]['p'] + t - d
        # พิมพ์ใบเสร็จ
        print(f"Item: {data[i]['n']} Price: {final}")

#✅ โค้ดที่ "สะอาด" (Clean Code Refactored)
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    price: float

class ReceiptProcessor:
    TAX_RATE = 0.07
    DISCOUNT_THRESHOLD = 1000
    DISCOUNT_RATE = 0.1

    def get_tax(self, price: float) -> float:
        return price * self.TAX_RATE

    def get_discount(self, price: float) -> float:
        if price > self.DISCOUNT_THRESHOLD:
            return price * self.DISCOUNT_RATE
        return 0.0

    def calculate_final_price(self, price: float) -> float:
        # แยก Logic การคำนวณออกมาเป็นส่วนย่อย
        tax = self.get_tax(price)
        discount = self.get_discount(price)
        return price + tax - discount

    def print_receipt(self, products: List[Product]) -> None:
        """ฟังก์ชันหลักที่อ่านแล้วเข้าใจได้ทันทีเหมือนอ่านหนังสือ"""
        for product in products:
            final_price = self.calculate_final_price(product.price)
            print(f"Item: {product.name:15} | Final Price: {final_price:>8,.2f}")

#---------------------------------------การใช้งานจริง------------------------------------------------

if __name__ == "__main__":
    items = [
        Product(name="Keyboard", price=1200.0),
        Product(name="Mouse", price=500.0)
    ]
    
    processor = ReceiptProcessor()
    processor.print_receipt(items)
#----------------------------------------จบ example---------------------------------------------------

#---------------------------------refactor code day 1 3 5 รวมกัน------------------------------------------
from dataclasses import dataclass
from typing import Dict, Optional

# --- 1. Models (ใช้ Dataclass เพื่อความสะอาดของข้อมูล) ---

@dataclass
class Student:
    id: int
    name: str
    score: int
    description: str

    @property
    def grade(self) -> str:
        """Logic การตัดเกรดแยกมาอยู่ที่ Model (Single Responsibility)"""
        if self.score >= 80: return "A"
        if self.score >= 75: return "B+"
        if self.score >= 70: return "B"
        if self.score >= 65: return "C+"
        if self.score >= 60: return "C"
        if self.score >= 55: return "D+"
        if self.score >= 50: return "D"
        return "F"

# --- 2. Service Logic (แยกส่วนการจัดการข้อมูลออกจากส่วนแสดงผล) ---

class StudentRegistry:
    def __init__(self):
        self._students: Dict[int, Student] = {}
        self._next_id = 1

    def add_student(self, name: str, score: int, description: str) -> Student:
        student = Student(self._next_id, name, score, description)
        self._students[self._next_id] = student
        self._next_id += 1
        return student

    def get_student(self, student_id: int) -> Optional[Student]:
        return self._students.get(student_id)

    def update_student(self, student_id: int, name: str, score: int, description: str) -> bool:
        if student_id not in self._students:
            return False
        self._students[student_id] = Student(student_id, name, score, description)
        return True

    def delete_student(self, student_id: int) -> bool:
        if student_id in self._students:
            del self._students[student_id]
            return True
        return False

    def get_all_students(self):
        return list(self._students.values())

# --- 3. UI Helper (แยก Logic ของการรับ Input และ Loop) ---

class ConsoleUI:
    @staticmethod
    def ask_yes_no(prompt: str) -> bool:
        choice = input(f"{prompt} (y/n): ").lower()
        return choice in ['y', 'yes']

    @staticmethod
    def get_valid_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ กรุณาใส่เฉพาะตัวเลขครับ")

# --- 4. Main Application Loop ---

def main():
    registry = StudentRegistry()
    ui = ConsoleUI()
    
    print("=== 🎓 ระบบจัดการข้อมูลนักเรียนระดับมืออาชีพ ===")
    
    is_running = True
    while is_running:
        choice = input("\n[C]reate | [R]ead | [U]pdate | [D]elete | [A]ll | [Q]uit: ").lower()

        if choice == 'c':
            name = input("ชื่อนักเรียน: ")
            score = ui.get_valid_int("คะแนน (0-100): ")
            desc = input("คำอธิบาย: ")
            s = registry.add_student(name, score, desc)
            print(f"✅ บันทึกแล้ว! ID: {s.id} เกรดที่ได้: {s.grade}")

        elif choice == 'r':
            sid = ui.get_valid_int("ใส่ ID ที่ต้องการดู: ")
            s = registry.get_student(sid)
            if s:
                print(f"🔍 ข้อมูล: {s.name} | คะแนน: {s.score} | เกรด: {s.grade} | โน้ต: {s.description}")
            else:
                print("❌ ไม่พบข้อมูล")

        elif choice == 'a':
            print("\nรายชื่อนักเรียนทั้งหมด:")
            for s in registry.get_all_students():
                print(f"ID: {s.id} | {s.name:15} | เกรด: {s.grade}")

        elif choice == 'q':
            is_running = False
            print("👋 ปิดโปรแกรม... สวัสดีครับ")

if __name__ == "__main__":
    main()
