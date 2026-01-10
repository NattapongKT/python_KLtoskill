#-------------------------------------bubble_sort--------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    # วนรอบทั้งหมด (ทำซ้ำ n ครั้ง)
    for i in range(n):
        # ในแต่ละรอบ ตัวที่ใหญ่ที่สุดจะไปอยู่ท้ายสุดแล้ว จึงลบ i ออก
        for j in range(0, n - i - 1):
            # ถ้าตัวหน้า > ตัวหลัง ให้สลับ (Swap)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#---------------------------------------------------------------------------------------

#------------------------------------insertion_sort---------------------------------------------------
def insertion_sort(arr):
    # เริ่มที่ตัวที่ 2 (index 1) เพราะตัวแรกถือว่าเรียงแล้ว
    for i in range(1, len(arr)):
        key = arr[i] # เก็บค่าที่จะเอาไปแทรก
        j = i - 1
        
        # ถอยหลังไปดูทางซ้าย ถ้าเจอตัวที่มากกว่า key ให้ขยับมันไปทางขวา
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # วาง key ลงในช่องว่างที่เหมาะสม
        arr[j + 1] = key
    return arr
#---------------------------------------------------------------------------------------

#------------------------------------merge_sort---------------------------------------------------
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # แบ่งย่อยข้อมูล (Recursive)
        merge_sort(L)
        merge_sort(R)

        # ขั้นตอนการรวม (Merge)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # เก็บตกค่าที่เหลือ
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
#---------------------------------------------------------------------------------------
"""
AlgorithmTime (Worst)Spaceจุดเด่น
Bubble$O(n^2)$$O(1)$เขียนง่ายที่สุด เข้าใจง่าย
Insertion$O(n^2)$$O(1)$เร็วมากถ้าข้อมูลเกือบเรียงอยู่แล้ว
Merge$O(n \log n)$$O(n)$ประสิทธิภาพสูงมากสำหรับข้อมูลจำนวนมาก
"""

#--------------------------------ทดลองใช้งาน Search-------------------------------------------------------
test_data = [64, 34, 25, 12, 22, 11, 90]

print("Bubble Sort Result:", bubble_sort(test_data.copy()))
print("Insertion Sort Result:", insertion_sort(test_data.copy()))
print("Merge Sort Result:", merge_sort(test_data.copy()))
#---------------------------------------------------------------------------------------

#-------------------------------เปรียบเทียบ Performance (ใช้ time module)--------------------------------------------------------
import time
import random

# ใช้ข้อมูล 5,000 ตัว (ถ้า 1 ล้านตัว Bubble/Insertion จะรันนานเกินไป)
data = [random.randint(1, 10000) for _ in range(5000)]

# Bubble Sort timing
start = time.time()
bubble_sort(data.copy())
print(f"Bubble Sort Time: {time.time() - start:.6f} seconds")

# Insertion Sort timing
start = time.time()
insertion_sort(data.copy())
print(f"Insertion Sort Time: {time.time() - start:.6f} seconds")

# Merge Sort timing
start = time.time()
merge_sort(data.copy())
print(f"Merge Sort Time: {time.time() - start:.6f} seconds")
#---------------------------------------------------------------------------------------
