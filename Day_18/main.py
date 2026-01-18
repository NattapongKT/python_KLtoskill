from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from datetime import datetime

#-------------------------------------1. Enum---------------------------------------------------
class Priority(Enum):
    """กำหนดลำดับความสำคัญ (ป้องกันการระบุค่าผิด)"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"

class TaskStatus(Enum):
    """กำหนดสถานะของงาน"""
    TODO = "To Do"
    DOING = "In Progress"
    DONE = "Completed"

#------------------------------------2. Dataclass-----------------------------------------------
@dataclass
class Task:
    """
    ใช้ dataclass เพื่อเก็บข้อมูลงาน 
    - ไม่ต้องเขียน __init__ เอง
    - มี __repr__ สวยๆ ให้เลยอัตโนมัติ
    """
    id: int
    title: str
    priority: Priority = Priority.MEDIUM
    status: TaskStatus = TaskStatus.TODO
    # ใช้ Optional เพราะบางงานอาจจะยังไม่มีคนรับผิดชอบ
    assignee: Optional[str] = None 

@dataclass
class Project:
    name: str
    # ใช้ field(default_factory=list) เพื่อป้องกันปัญหา List ที่ใช้ร่วมกันในทุุก instance
    tasks: List[Task] = field(default_factory=list)

    #--------------------------------3. Type Hinting--------------------------------------------
    def add_task(self, task: Task) -> None:
        """Type hint ระบุชัดเจนว่ารับ Task object และไม่ return ค่า"""
        self.tasks.append(task)
        print(f"➕ Task '{task.title}' added to project '{self.name}'")

    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """คืนค่าเป็น List ของ Task ตามสถานะที่ระบุ"""
        return [t for t in self.tasks if t.status == status]

    def show_summary(self) -> None:
        print(f"\n--- Project Summary: {self.name} ---")
        for t in self.tasks:
            print(f"[{t.status.value}] {t.title} | Priority: {t.priority.value} | Assignee: {t.assignee}")

#------------------------------------4. Improve Readability (Usage)-----------------------------

def initialize_project() -> Project:
    """ฟังก์ชันเริ่มต้นสร้างโปรเจกต์จำลอง"""
    my_project = Project("AI Development")

    # การสร้าง Object Task พร้อมระบุสถานะผ่าน Enum
    t1 = Task(1, "Data Collection", Priority.HIGH, TaskStatus.DONE, "Alice")
    t2 = Task(2, "Model Training", Priority.URGENT, TaskStatus.DOING, "Bob")
    t3 = Task(3, "UI Design", Priority.LOW, TaskStatus.TODO) # assignee เป็น None โดยปริยาย

    my_project.add_task(t1)
    my_project.add_task(t2)
    my_project.add_task(t3)

    return my_project

#---------------------------------------Main Execution------------------------------------------

if __name__ == "__main__":
    # เรียกใช้ฟังก์ชันที่ระบุ Type Hint ไว้ชัดเจน
    it_project: Project = initialize_project()

    # ลองดึงเฉพาะงานที่เสร็จแล้วมาดู
    completed_tasks: List[Task] = it_project.get_tasks_by_status(TaskStatus.DONE)
    
    print(f"\nCompleted Tasks Count: {len(completed_tasks)}")
    
    # แสดงภาพรวมทั้งหมด
    it_project.show_summary()

#---------------------------------------------------------------------------------------------------