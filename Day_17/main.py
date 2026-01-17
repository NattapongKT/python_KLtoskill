#โค้ดที่ "ผิด" หลักการ (Violating SOLID)
class OrderManager:
    # ผิด SRP: คลาสเดียวทำทั้งคำนวณเงิน, บันทึก DB, และส่ง Email
    def process_order(self, order):
        # 1. คำนวณภาษี
        total = order.price * 1.07
        # 2. บันทึกลง Database (ยึดติดกับ MySQL ตรงๆ - ผิด DIP)
        print(f"Saving {order.name} to MySQL Database...")
        # 3. ส่ง Email
        print(f"Sending email to customer...")

#โค้ดที่ "ถูก" ตามหลัก SOLID (Refactored)
from abc import ABC, abstractmethod

#--- 1. SRP: แยกหน้าที่กันชัดเจน ---

class TaxCalculator:
    def calculate(self, price):
        return price * 1.07
    
class EmailService:
    def send_notification(self, message):
        print(f"Email: {message}")

#--- 2. DIP & OCP: สร้าง Abstraction (Interface) สำหรับ Database ---

class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLStorage(Storage): # Module ระดับล่าง
    def save(self, data):
        print(f"Saved {data} to MySQL.")

class MongoDBStorage(Storage): # เพิ่ม Database ใหม่ได้โดยไม่ต้องแก้โค้ดเก่า (OCP)
    def save(self, data):
        print(f"Saved {data} to MongoDB.")

#--- 3. การรวมร่าง (High-level Module) ---

class OrderProcessor:
    def __init__(self, storage: Storage, notifier: EmailService):
        self.storage = storage      # DIP: รับ Abstraction เข้ามา
        self.notifier = notifier
        self.tax_calc = TaxCalculator()

    def process(self, order_name, price):
        total = self.tax_calc.calculate(price)
        self.storage.save(order_name)
        self.notifier.send_notification(f"Order {order_name} processed. Total: {total}")

#---------------------------------------ใช้งานจริง------------------------------------------------
if __name__ == "__main__":
    # เราเลือกได้ว่าจะใช้ DB อะไร โดยที่ OrderProcessor ไม่ต้องเปลี่ยนโค้ดภายในเลย (OCP/DIP)
    db = MySQLStorage()
    email = EmailService()
    
    app = OrderProcessor(db, email)
    app.process("Laptop", 30000)