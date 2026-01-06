import json
import os

# --- Global Configuration ---
data_storage = {}
next_id = 1
FILE_NAME = "studentFile.txt"

# --- 1. Create (สร้าง) ---
def create_item(name, description):
    global next_id
    item = {
        "id": next_id,
        "name": name,
        "description": description
    }
    data_storage[next_id] = item
    
    # Save the current state to the file
    save_all_to_file()
    
    next_id += 1
    print(f"สร้างรายการสำเร็จ: {item}")
    return item

# --- 2. Read (อ่าน) ---
def read_item(item_id):
    if item_id in data_storage:
        print(f"ดึงข้อมูลสำเร็จ: {data_storage[item_id]}")
        return data_storage[item_id]
    else:
        print(f"ไม่พบข้อมูล ID: {item_id}")
        return None

def read_all_items():
    if not data_storage:
        print("ไม่มีข้อมูลในระบบ")
        return []
    print("\n--- รายการทั้งหมด ---")
    for item in data_storage.values():
        print(f"ID: {item['id']} | Name: {item['name']} | Description: {item['description']}")
    return list(data_storage.values())

# --- 3. Update (อัปเดต) ---
def update_item(item_id, new_name, new_description):
    if item_id in data_storage:
        data_storage[item_id]["name"] = new_name
        data_storage[item_id]["description"] = new_description
        save_all_to_file()
        print(f"อัปเดตข้อมูลสำเร็จ: {data_storage[item_id]}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับอัปเดต")

# --- 4. Delete (ลบ) ---
def delete_item(item_id):
    if item_id in data_storage:
        del data_storage[item_id]
        save_all_to_file()
        print(f"ลบข้อมูลสำเร็จ ID: {item_id}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับลบ")

# --- 5. File Management (การจัดการไฟล์) ---
def save_all_to_file():
    """Saves the entire dictionary to the file as JSON lines."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for item in data_storage.values():
                f.write(json.dumps(item) + "\n")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_data_from_file():
    """Loads data from the file into data_storage on startup."""
    global next_id
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        item = json.loads(line)
                        data_storage[item["id"]] = item
                        if item["id"] >= next_id:
                            next_id = item["id"] + 1
            print(f"โหลดข้อมูลสำเร็จ ({len(data_storage)} รายการ)")
        except Exception as e:
            print(f"Error loading file: {e}")

# --- Main Program Loop ---
print("---------------------- Student Management --------------------------")
load_data_from_file()

while True:
    print("\n" + "="*50)
    typeCRUD = input("Select Action: [C]reate, [R]ead, [U]pdate, [D]elete, [L]ist All, [E]xit: ").lower()

    if typeCRUD == "e":
        print("----------- Closing CRUD Student Program -------------")
        break

    elif typeCRUD == "c":
        print("------------------- Create ----------------------")
        name = input("Enter the name: ")
        desc = input("Enter the description: ")
        create_item(name, desc)

    elif typeCRUD == "r":
        print("------------------- Read ----------------------")
        try:
            read_id = int(input("Enter ID: "))
            read_item(read_id)
        except ValueError:
            print("Error: Please enter a valid number for ID.")

    elif typeCRUD == "u":
        print("------------------- Update ----------------------")
        try:
            u_id = int(input("Enter ID to update: "))
            if u_id in data_storage:
                u_name = input("Enter new name: ")
                u_desc = input("Enter new description: ")
                update_item(u_id, u_name, u_desc)
            else:
                print("ID not found.")
        except ValueError:
            print("Error: Invalid input.")

    elif typeCRUD == "d":
        print("------------------- Delete ----------------------")
        try:
            d_id = int(input("Enter ID to delete: "))
            delete_item(d_id)
        except ValueError:
            print("Error: Please enter a number.")

    elif typeCRUD == "l":
        read_all_items()

    else:
        print("Invalid selection. Please try again.")

    # Continue prompt
    cont = input("\nPerform another action? (y/n): ").lower()
    if cont != 'y':
        print("----------- Closing CRUD Student Program -------------")
        break