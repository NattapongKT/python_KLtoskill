#-----------------------------------------------question 1-------------------------------------------------
print("\n--------------------------------Question 1----------------------------------------\n")
from collections import deque

class RestaurantQueue:
    def __init__(self):
        self.queue = deque()

    def add_customer(self, name):
        self.queue.append(name)
        print(f"เพิ่ม '{name}' เข้าคิวเรียบร้อย")

    def call_next(self):
        if self.queue:
            customer = self.queue.popleft()
            print(f"เชิญคุณ '{customer}' ไปที่โต๊ะครับ")
        else:
            print("ตอนนี้ไม่มีลูกค้าในคิวครับ")

# ทดสอบ
shop = RestaurantQueue()
shop.add_customer("Alice")
shop.add_customer("Bob")
shop.call_next() # Alice
shop.call_next() # Bob
#----------------------------------------------------------------------------------------------------------


#-----------------------------------------------question 2-------------------------------------------------
print("\n--------------------------------Question 2----------------------------------------\n")
def find_price(products, target_id):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2
        if products[mid]['id'] == target_id:
            return f"สินค้า ID {target_id} ราคา {products[mid]['price']} บาท"
        elif products[mid]['id'] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return "ไม่พบรหัสสินค้านี้"

# ข้อมูลตัวอย่าง (ต้องเรียงตาม ID)
inventory = [
    {"id": 101, "price": 50},
    {"id": 205, "price": 120},
    {"id": 450, "price": 300},
    {"id": 500, "price": 1000}
]

print(find_price(inventory, 450))
#----------------------------------------------------------------------------------------------------------

#-----------------------------------------------question 3-------------------------------------------------
print("\n--------------------------------Question 3----------------------------------------\n")
players = [
    {"name": "Mumu", "score": 85},
    {"name": "Zaza", "score": 98},
    {"name": "Koko", "score": 72},
    {"name": "Nana", "score": 91}
]

# เรียงจากมากไปน้อย (reverse=True) ตาม key "score"
sorted_players = sorted(players, key=lambda x: x['score'], reverse=True)

print("--- Leaderboard ---")
for i, p in enumerate(sorted_players, 1):
    print(f"{i}. {p['name']}: {p['score']} pts")

#-----------------------------------------------question 4-------------------------------------------------
print("\n--------------------------------Question 4----------------------------------------\n")
import heapq

def shortest_path(graph, start):
    # เก็บระยะทางที่สั้นที่สุดจากจุดเริ่มไปยังทุกจุด (ค่าเริ่มต้นคือ Infinity)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] # (ระยะทางรวม, จุดปัจจุบัน)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# แผนผังเมือง (จุด: {เพื่อนบ้าน: ระยะทาง})
map_data = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4},
    'C': {'B': 1, 'D': 9},
    'D': {}
}

print(f"ระยะทางจาก A ไปจุดต่างๆ: {shortest_path(map_data, 'A')}")

#-----------------------------------------------question 5-------------------------------------------------
print("\n--------------------------------Question 5----------------------------------------\n")
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            # ถ้า stack ว่าง หรือวงเล็บล่าสุดไม่คู่กัน
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

# ทดสอบ
print(is_balanced("(5 + 2) * [3 - 1]")) # True
print(is_balanced("(5 + 2] * 3"))       # False
#----------------------------------------------------------------------------------------------------------