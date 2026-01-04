"""------------------------Dat_4_code----------------------------------
data_storage = {} #dict
next_id = 1

# --- 1. Create (สร้าง) ---
def create_item(name, description):
    global next_id
    item = {
        "id": next_id,
        "name": name,
        "description": description
    }
    data_storage[next_id] = item
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
    print("ดึงข้อมูลทั้งหมด:")
    for item_id, item in data_storage.items():
        print(f"  {item}")
    return list(data_storage.values())

# --- 3. Update (อัปเดต) ---
def update_item(item_id, new_name, new_description):
    if item_id in data_storage:
        data_storage[item_id]["name"] = new_name
        data_storage[item_id]["description"] = new_description
        print(f"อัปเดตข้อมูลสำเร็จ: {data_storage[item_id]}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับอัปเดต")

# --- 4. Delete (ลบ) ---
def delete_item(item_id):
    if item_id in data_storage:
        del data_storage[item_id]
        print(f"ลบข้อมูลสำเร็จ ID: {item_id}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับลบ")

print("----------------------ระบบเก็บข้อมูลนักเรียน--------------------------")
again = True
again2 = True
while again == True:
    typeCRUD = input("Select : Create / Read / Update / Delete (TYPE C/R/U/D) : ")
    while again2 == True:
        if typeCRUD.lower() == "c":
            print("-------------------create----------------------")
            typeCreateName = input("enter the name : ")
            typeCreateDescription = input("enter the description : ")
            create_item(typeCreateName, typeCreateDescription)
        elif typeCRUD.lower() == "r":
            print("-------------------read----------------------")
            typeReadId = int(input("enter the number id (1 - x) : "))
            read_item(typeReadId)
        elif typeCRUD.lower() == "u":
            print("-------------------update----------------------")
            typeUpdateId = int(input("enter the id (1 - x) : "))
            typeUpdateName = input("enter the name : ")
            typeUpdateDescription = input("enter the description : ")
            update_item(typeUpdateId, typeUpdateName, typeUpdateDescription)
            read_all_items()
        elif typeCRUD.lower() == "d":
            print("-------------------delete----------------------")
            typeUpdateId = int(input("enter the id (1 - x) : "))
            delete_item(typeUpdateId)
            read_all_items()
        else:
            print("Error input pls select c/r/u/d again.")

        againYN2 = input("Want to continue? y/n : ")
        if againYN2.lower() == "y":
            again2 = True
        elif againYN2.lower() == "n":
            again2 = False
        else:
            print("Error")
            again2 = False

    againYN = input("Want to continue system? y/n : ")
    if againYN.lower() == "y":
        again = True
        again2 = True
    elif againYN.lower() == "n":
        again = False
        print("-----------Closing CRUD Student Program-------------")
        print("Success close the program")
    else:
        print("Error")
        again = False
"""
data_storage = {} #dict
next_id = 1

# --- 1. Create (สร้าง) ---
def create_item(name, description):
    global next_id
    item = {
        "id": next_id,
        "name": name,
        "description": description
    }
    data_storage[next_id] = item
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
    print("ดึงข้อมูลทั้งหมด:")
    for item_id, item in data_storage.items():
        print(f"  {item}")
    return list(data_storage.values())

# --- 3. Update (อัปเดต) ---
def update_item(item_id, new_name, new_description):
    if item_id in data_storage:
        data_storage[item_id]["name"] = new_name
        data_storage[item_id]["description"] = new_description
        print(f"อัปเดตข้อมูลสำเร็จ: {data_storage[item_id]}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับอัปเดต")

# --- 4. Delete (ลบ) ---
def delete_item(item_id):
    if item_id in data_storage:
        del data_storage[item_id]
        print(f"ลบข้อมูลสำเร็จ ID: {item_id}")
    else:
        print(f"ไม่พบข้อมูล ID: {item_id} สำหรับลบ")

print("----------------------ระบบเก็บข้อมูลนักเรียน--------------------------")
again = True
again2 = True
while again == True:
    typeCRUD = input("Select : Create / Read / Update / Delete (TYPE C/R/U/D) : ")
    while again2 == True:
        if typeCRUD.lower() == "c":
            print("-------------------create----------------------")
            try:
                typeCreateName = input("enter the name : ")
                typeCreateDescription = input("enter the description : ")
                try:
                    create_item(typeCreateName, typeCreateDescription)
                except:
                    print("something when wrong to create item!!")
            except:
                print("something when wrong input name or description error?")
        elif typeCRUD.lower() == "r":
            print("-------------------read----------------------")
            try:
                typeReadId = int(input("enter the number id (1 - x) : "))
                try:
                    read_item(typeReadId)
                except:
                    print("something when wrong to read item!!")
            except:
                print("something when wrong like inuput not a number? Exam : 1 2 3 ... 999?")
        elif typeCRUD.lower() == "u":
            print("-------------------update----------------------")
            try:
                typeUpdateId = int(input("enter the id (1 - x) : "))
                typeUpdateName = input("enter the name : ")
                typeUpdateDescription = input("enter the description : ")
                try:
                    update_item(typeUpdateId, typeUpdateName, typeUpdateDescription)
                    read_all_items()
                except:
                    print("something when wrong with update_item or read_all_item function pls contact with Developer")
            except:
                print("something when wrong in id or name or description.")
        elif typeCRUD.lower() == "d":
            print("-------------------delete----------------------")
            try:
                typeUpdateId = int(input("enter the id (1 - x) : "))
                try:
                    delete_item(typeUpdateId)
                    read_all_items()
                except:
                    print("some thing when wrong with function pls contract Developer")
            except:
                print("something when wrong like inuput not a number? Exam : 1 2 3 ... 999?")
        else:
            print("Error input pls select c/r/u/d again.")

        againYN2 = input("Want to continue? y/n : ")
        if againYN2.lower() == "y":
            again2 = True
        elif againYN2.lower() == "n":
            again2 = False
        else:
            print("Error")
            again2 = False

    againYN = input("Want to continue system? y/n : ")
    if againYN.lower() == "y":
        again = True
        again2 = True
    elif againYN.lower() == "n":
        again = False
        print("-----------Closing CRUD Student Program-------------")
        print("Success close the program")
    else:
        print("Error")
        again = False