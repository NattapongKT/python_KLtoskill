#-------------------------------------Define Class--------------------------------------------------
class Book:
    """
    Class สำหรับจำลองโมเดล 'หนังสือ'
    """
    # Constructor: ส่วนที่ใช้กำหนดค่าเริ่มต้นให้แต่ละ Object
    def __init__(self, title, author, isbn):
        self.title = title        # ชื่อหนังสือ
        self.author = author      # ผู้แต่ง
        self.isbn = isbn          # รหัสหนังสือ
        self.is_available = True  # สถานะ (เริ่มต้นเป็น True เสมอ)

    def borrow(self):
        """Method สำหรับการยืมหนังสือ"""
        if self.is_available:
            self.is_available = False
            print(f"✅ ยืมหนังสือ '{self.title}' สำเร็จ")
        else:
            print(f"❌ หนังสือ '{self.title}' ถูกยืมไปแล้ว")

    def return_book(self):
        """Method สำหรับการคืนหนังสือ"""
        self.is_available = True
        print(f"♻️ คืนหนังสือ '{self.title}' เรียบร้อย")

    def __str__(self):
        """Magic Method: ใช้กำหนดสิ่งที่จะแสดงเมื่อสั่ง print(object)"""
        status = "Available" if self.is_available else "Borrowed"
        return f"Book: {self.title:20} | Author: {self.author:15} | Status: {status}"

#---------------------------------------------------------------------------------------------------

#------------------------------------Model Data with Class------------------------------------------
# 1. การสร้าง Objects (Instances) จาก Class เดียวกัน
book1 = Book("Python 101", "John Doe", "978-01")
book2 = Book("Data Science", "Jane Smith", "978-02")
book3 = Book("Algorithm Basics", "Alan Turing", "978-03")

# 2. เก็บ Objects ไว้ใน List (Model Data)
library_shelf = [book1, book2, book3]

# 3. ทดลองใช้งาน Methods ของแต่ละ Object
print("--- 📚 Library System Simulation ---")

# แสดงรายชื่อหนังสือทั้งหมดในตอนแรก
for book in library_shelf:
    print(book)

print("\n--- 📖 Transaction History ---")
book1.borrow()      # ยืมเล่มแรก
book1.borrow()      # ลองยืมเล่มเดิมซ้ำ (ควร Error)
book2.borrow()      # ยืมเล่มสอง
book1.return_book() # คืนเล่มแรก

print("\n--- 📊 Final Status ---")
for book in library_shelf:
    print(book)

#---------------------------------------------------------------------------------------------------

"""
⏱ OOP Concept Review:
- Class: 'Book' คือพิมพ์เขียว (Blueprint)
- Object: 'book1', 'book2' คือตัวตนจริงๆ (Instances)
- Constructor: '__init__' ทำหน้าที่ตั้งค่า title, author ทันทีที่สร้าง
- Self: คือการอ้างถึง 'ตัวมันเอง' เพื่อให้จัดการข้อมูลถูก Object
"""