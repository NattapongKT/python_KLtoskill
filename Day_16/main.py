#-------------------------------------1. Composition------------------------------------------------
class Address:
    """Class นี้จะถูกนำไปใช้เป็นส่วนประกอบ (Composition) ใน Class อื่น"""
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def get_full_address(self):
        return f"{self.street}, {self.city}"

#-------------------------------------2. Inheritance (Parent)---------------------------------------
class Employee:
    """Parent Class: เก็บคุณสมบัติพื้นฐานที่พนักงานทุกคนต้องมี (Is-a relationship)"""
    def __init__(self, name, emp_id, city, street):
        self.name = name
        self.emp_id = emp_id
        # Composition: พนักงาน 'มี' (Has-a) ที่อยู่
        self.address = Address(city, street)

    def show_profile(self):
        print(f"ID: {self.emp_id} | Name: {self.name}")
        print(f"Address: {self.address.get_full_address()}")

    def calculate_pay(self):
        # สร้างเป็นโครงไว้ให้ลูกๆ ไปใส่สูตรคำนวณเอง
        pass

#-------------------------------------3. Inheritance (Child)----------------------------------------
class FullTimeEmployee(Employee):
    """สืบทอดจาก Employee: สำหรับพนักงานเงินเดือนประจำ"""
    def __init__(self, name, emp_id, city, street, salary):
        # ดึงคุณสมบัติจาก Parent มาใช้
        super().__init__(name, emp_id, city, street)
        self.salary = salary

    def calculate_pay(self):
        return self.salary

class ContractEmployee(Employee):
    """สืบทอดจาก Employee: สำหรับพนักงานพาร์ทไทม์ (คิดตามชั่วโมง)"""
    def __init__(self, name, emp_id, city, street, hourly_rate, hours_worked):
        super().__init__(name, emp_id, city, street)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

#------------------------------------4. System Refactoring (Composition)-----------------------------
class Company:
    """Class หลักที่รวบรวมพนักงานทุกคนไว้ด้วยกัน"""
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = [] # เก็บ List ของ Object พนักงาน

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.company_name}")

    def show_all_payroll(self):
        print(f"\n--- Payroll for {self.company_name} ---")
        for emp in self.employees:
            emp.show_profile()
            print(f"Net Pay: {emp.calculate_pay():,.2f} THB")
            print("-" * 30)

#---------------------------------------5. ทดลองใช้งาน------------------------------------------------
if __name__ == "__main__":
    # สร้างบริษัท
    my_company = Company("Tech Solutions Co.")

    # สร้างพนักงานประเภทต่างๆ (ใช้คุณสมบัติ Inheritance และ Composition)
    emp1 = FullTimeEmployee("Somchai", "FT01", "Bangkok", "Sukhumvit Rd", 50000)
    emp2 = ContractEmployee("Lisa", "CT01", "Chiang Mai", "Nimman", 500, 80)

    # เพิ่มพนักงานลงในระบบของบริษัท
    my_company.add_employee(emp1)
    my_company.add_employee(emp2)

    # แสดงผลการคำนวณเงินเดือน
    my_company.show_all_payroll()

#---------------------------------------------------------------------------------------------------