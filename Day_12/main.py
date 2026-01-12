import sys

# เพิ่มขีดจำกัดของ Recursion (ปกติ Python จะจำกัดไว้ที่ 1000)
sys.setrecursionlimit(2000)

#------------------------------------1. Factorial---------------------------------------------------
def factorial(n):
    """
    คำนวณ n! โดยใช้ Recursion
    - Base Case: n คือ 0 หรือ 1 ให้คืนค่า 1
    - Recursive Step: n * factorial(n-1)
    """
    # ตรวจสอบกรณีเลขติดลบ (Error Handling)
    if n < 0:
        return "Error: Negative numbers not allowed"
    
    # [Base Case]
    if n <= 1:
        return 1
    
    # [Recursive Step]
    return n * factorial(n - 1)

"""
⏱ Time Complexity: O(n)
📦 Space Complexity: O(n) จาก Call Stack
"""
#---------------------------------------------------------------------------------------

#------------------------------------2. Tree Traversal----------------------------------------------
class Node:
    """Class สำหรับสร้าง Node ของ Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_inorder(node):
    """
    การเดินใน Tree แบบ In-order (ซ้าย -> กลาง -> ขวา)
    """
    if node:
        # เดินไปทางซ้ายสุด (Recursive)
        print_inorder(node.left)
        
        # พิมพ์ค่าปัจจุบัน
        print(f"[{node.value}]", end=" -> ")
        
        # เดินไปทางขวา (Recursive)
        print_inorder(node.right)

"""
⏱ Time Complexity: O(n) เมื่อ n คือจำนวน Node ทั้งหมด
💡 หัวใจสำคัญ: Recursion จะจดจำ "ทางกลับ" ให้เราโดยอัตโนมัติผ่าน Stack
"""
#---------------------------------------------------------------------------------------

#--------------------------------ทดลองใช้งาน (Main)-------------------------------------------------------
if __name__ == "__main__":
    print("--- 1. Testing Factorial ---")
    test_num = 5
    result = factorial(test_num)
    print(f"Result of {test_num}! is: {result}") 
    # ตัวอย่างการไล่สาย (Trace): 5 * 4 * 3 * 2 * 1 = 120
    

    print("\n--- 2. Testing Tree Traversal ---")
    # สร้างโครงสร้างต้นไม้จำลอง
    #        10
    #       /  \
    #      5    15
    #     / \
    #    2   7
    
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("In-order Traversal Path:")
    print_inorder(root)
    print("End")
    

#---------------------------------------------------------------------------------------