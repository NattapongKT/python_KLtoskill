#สำหรับใช้ deque (หลัก FIFO)
from collections import deque
#สำหรับใช้ time
import time

from TextEditor import TextEditor, process_orders

#หลักการ: LIFO (Last-In, First-Out) - มาทีหลัง ออกก่อน (เหมือนกองจาน)
#--------------------------------------------Python Stack--------------------------------------------------------------
stack = []

# Push (เพิ่มข้อมูล)
stack.append("A")
stack.append("B")
stack.append("C")

# Pop (เอาข้อมูลออก - ออกจากด้านบนสุด)
top_item = stack.pop() 

def printResult():
    print(f"stack : {stack}, top_item {top_item}")
    return stack, top_item

printResult()

""" ⏱ Time Complexity: Push/Pop เป็น O(1) 💡 Use Case:
Undo (ยกเลิกการกระทำ)
การทำงานของปุ่ม Back ใน Browser
การตรวจสอบวงเล็บในทางคณิตศาสตร์ """
#----------------------------------------------------------------------------------------------------------

#หลักการ: FIFO (First-In, First-Out) - มาก่อน ออกก่อน (เหมือนแถวซื้อของ)
#-----------------------------------------------Python Queue-----------------------------------------------------------
queue = deque([])

queue.append("A")
queue.append("B")
queue.append("C")

first_item = queue.popleft() 

def printResult2():
    print(f"stack : {queue}, first_item {first_item}")
    return queue, first_item

# Dequeue (เอาข้อมูลออก - ออกจากหน้าสุด)
printResult2()

""" ⏱ Time Complexity: Enqueue/Dequeue เป็น O(1) 💡 Use Case:
การจัดการคิวพิมพ์เอกสาร (Printer)
ระบบ Call Center
การส่งข้อความ (Message Queue) """
#----------------------------------------------------------------------------------------------------------

#-------------------------Do: Undo/Redo Simulation (Stack)-------------------------------------- class TextEditor: def init(self): self.text = "" self.undo_stack = [] self.redo_stack = []

def type_text(self, new_text):
    self.undo_stack.append(self.text) # เก็บค่าปัจจุบันไว้ก่อนพิมพ์
    self.text += new_text
    self.redo_stack.clear() # พิมพ์ใหม่แล้ว ต้องล้าง redo
    print(f"Current: '{self.text}'")

def undo(self):
    if self.undo_stack:
        self.redo_stack.append(self.text) # เก็บค่าปัจจุบันเข้า redo
        self.text = self.undo_stack.pop() # ดึงค่าเก่าคืนมา
        print(f"Undo to: '{self.text}'")

def redo(self):
    if self.redo_stack:
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print(f"Redo to: '{self.text}'")
#-------------------------Do: Queue Processing Simulation--------------------------------------- def process_orders(orders): order_queue = deque(orders) print(f"\nStarting queue process: {list(order_queue)}")
order_queue = deque(["A", "B", "C"])

while order_queue:
    current_order = order_queue.popleft()
    print(f"Processing: {current_order}... Done!")
    time.sleep(0.5) # จำลองเวลาทำงาน
print("All orders processed.")

#--------------------------------ทดลองใช้งาน-------------------------------------------------------

print("--- Undo/Redo Simulation ---") 
editor = TextEditor() 
editor.type_text("Hello ") 
editor.type_text("World!") 
editor.undo() 
editor.redo()

print("\n--- Queue Processing ---") 
process_orders(["Order #1", "Order #2", "Order #3"])
#----------------------------------------------------------------------------------------------------------