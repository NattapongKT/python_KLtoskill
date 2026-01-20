"""
❌ โค้ดที่มี Bug (The Broken Code)
มี Bug 3 จุด: 1. ลืมแปลง type, 2. หารด้วยศูนย์, 3. ลอจิกการตัดเกรดผิด

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score  # ถ้า score มาเป็น String จะพังตรงนี้
    return total / len(scores) # ถ้า scores ว่าง จะพัง (ZeroDivisionError)

def get_status(avg):
    if avg > 50: # ถ้าได้ 50 พอดีจะกลายเป็น Fail (ลอจิกผิด)
        return "Pass"
    else:
        return "Fail"
"""


#✅ โค้ดที่แก้แล้วพร้อมระบบ Logging (Clean & Safe)
import logging
from dataclasses import dataclass
from typing import Dict, Optional, List

# --- 1. Setup Logging Configuration ---
# ตั้งค่าให้บันทึกทั้งลงหน้าจอ และสามารถเก็บ Log Level ต่างๆ ได้
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@dataclass
class Student:
    id: int
    name: str
    score: int
    description: str

    @property
    def grade(self) -> str:
        if self.score >= 80: return "A"
        if self.score >= 70: return "B"
        if self.score >= 60: return "C"
        if self.score >= 50: return "D"
        return "F"

class StudentRegistry:
    def __init__(self):
        self._students: Dict[int, Student] = {}
        self._next_id = 1

    def add_student(self, name: str, score: int, description: str) -> Student:
        student = Student(self._next_id, name, score, description)
        self._students[self._next_id] = student
        
        # [LOG INFO]: บันทึกเมื่อมีการสร้างข้อมูลสำเร็จ
        logging.info(f"CREATE: เพิ่มนักเรียนใหม่ ID {self._next_id} - {name} สำเร็จ")
        
        self._next_id += 1
        return student

    def delete_student(self, student_id: int) -> bool:
        if student_id in self._students:
            name = self._students[student_id].name
            del self._students[student_id]
            
            # [LOG INFO]: บันทึกเมื่อมีการลบข้อมูล
            logging.info(f"DELETE: ลบนักเรียน ID {student_id} ({name}) ออกจากระบบ")
            return True
        
        logging.warning(f"DELETE FAIL: ไม่พบ ID {student_id} เพื่อลบ")
        return False

    def get_all_students(self) -> List[Student]:
        return list(self._students.values())

class ConsoleUI:
    @staticmethod
    def get_valid_int(prompt: str) -> int:
        while True:
            try:
                val = int(input(prompt))
                return val
            except ValueError as e:
                # [LOG ERROR]: บันทึกเมื่อ User พิมพ์สิ่งที่ไม่ใช่ตัวเลข
                logging.error(f"INPUT ERROR: ผู้ใช้พิมพ์ข้อมูลที่ไม่ใช่ตัวเลข - {e}")
                print("❌ กรุณาใส่เฉพาะตัวเลขเท่านั้น!")

# --- Main Application ---
def main():
    registry = StudentRegistry()
    ui = ConsoleUI()
    
    logging.info("SYSTEM: เริ่มต้นการทำงานของระบบ Registry")

    # จำลองการทำงาน
    print("\n--- Testing System with Logging ---")
    
    # 1. ทดสอบ Create
    registry.add_student("Somchai", 85, "Good Student")
    registry.add_student("Lisa", 45, "Needs Improvement")

    # 2. ทดสอบ Error Input (ลองนึกภาพว่าเราพิมพ์ 'abc' ในขั้นตอนนี้)
    print("\n[ลองพิมพ์ 'abc' เพื่อดู Error Log]")
    score = ui.get_valid_int("กรุณาลองใส่คะแนน (เป็นตัวอักษรเพื่อทดสอบ Log): ")

    # 3. ทดสอบ Delete
    registry.delete_student(1) # ลบ ID 1
    registry.delete_student(99) # ลบ ID ที่ไม่มีอยู่จริง (ควรขึ้น Warning)

    logging.info("SYSTEM: ปิดการทำงานของระบบ")

if __name__ == "__main__":
    main()