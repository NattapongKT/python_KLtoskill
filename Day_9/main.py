#-------------------------------------Python Linear search--------------------------------------------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
"""
⏱ Time Complexity
Best: O(1)
Average / Worst: O(n) ใช้ได้กับ list ที่ ไม่ต้องเรียงลำดับ
"""
#---------------------------------------------------------------------------------------

#------------------------------------Python Binary search---------------------------------------------------
#!!!ต้องเป็น array ที่เรียงแล้ว!!!
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
"""
⏱ Time Complexity
Best: O(1)
Worst: O(log n) เร็วมากสำหรับข้อมูลขนาดใหญ่
"""
#---------------------------------------------------------------------------------------


#--------------------------------ทดลองใช้งาน Search-------------------------------------------------------
data = list(range(1, 1000001))  # 1 ถึง 1,000,000
target = 999999
print("Linear Search:", linear_search(data, target))
print("Binary Search:", binary_search(data, target))
#---------------------------------------------------------------------------------------

#-------------------------------เปรียบเทียบ Performance (ใช้ time module)--------------------------------------------------------
import time

data = list(range(1, 1_000_000))
target = 999999

# Linear Search timing
start = time.time()
linear_search(data, target)
end = time.time()
print(f"Linear Search Time: {end - start:.6f} seconds")

# Binary Search timing
start = time.time()
binary_search(data, target)
end = time.time()
print(f"Binary Search Time: {end - start:.6f} seconds")
#---------------------------------------------------------------------------------------
