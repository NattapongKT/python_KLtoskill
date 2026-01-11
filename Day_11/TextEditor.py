from collections import deque

# 1. นิยามคลาส TextEditor (ใช้ Stack สำหรับ Undo/Redo)
class TextEditor:
    def __init__(self):
        self.content = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_text(self, text):
        # เก็บสถานะปัจจุบันลงใน undo_stack ก่อนพิมพ์ใหม่
        self.undo_stack.append(self.content)
        self.redo_stack.clear()  # ถ้ามีการพิมพ์ใหม่ ต้องล้าง redo_stack
        self.content += text
        print(f"Typed: '{text}' | Current: '{self.content}'")

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.content)
            self.content = self.undo_stack.pop()
            print(f"Undo: '{self.content}'")
        else:
            print("Nothing to undo")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.content)
            self.content = self.redo_stack.pop()
            print(f"Redo: '{self.content}'")
        else:
            print("Nothing to redo")

# 2. นิยามฟังก์ชัน process_orders (ใช้ Queue สำหรับประมวลผลตามลำดับ)
def process_orders(orders_list):
    queue = deque(orders_list)
    while queue:
        current_order = queue.popleft()
        print(f"Processing: {current_order}")
    print("All orders processed!")

# --- ส่วนของการเรียกใช้งาน (ที่แก้ไข Syntax Error แล้ว) ---
"""
print("--- Undo/Redo Simulation ---")
editor = TextEditor()
editor.type_text("Hello ")
editor.type_text("World!")
editor.undo()
editor.redo()

print("\n--- Queue Processing ---")
process_orders(["Order #1", "Order #2", "Order #3"])
"""

