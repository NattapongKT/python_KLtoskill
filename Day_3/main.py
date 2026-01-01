#โปรแกรมคำนวณคะแนนพื้นฐาน จาก Day 2
"""
for i in range(1, 4):
    numberT = input("Hello input your score : ")
    number = int(numberT)
    if number < 50:
        print(f"your score is {number} and you got a F!!\n")
    elif number < 55:
        print(f"your score is {number} and you got a D!\n")
    elif number < 60:
        print(f"your score is {number} and you got a D+.\n")
    elif number < 65:
        print(f"your score is {number} and you got a C.\n")
    elif number < 70:
        print(f"your score is {number} and you got a C+.\n")
    elif number < 75:
        print(f"your score is {number} and you got a B.\n")
    elif number < 80:
        print(f"your score is {number} and you got a B+!\n")
    elif number <= 100:
        print(f"your score is {number} and congratulations! you got an A.\n")
    else:
        print("error input your score again\n")
    i += 1
"""

#โปรแกรมคำนวณคะแนนพื้นฐาน refactor แล้ว
#logic โปรแกรม 1รับคะแนน 2แปลงคะแนนเป็นเกรด 3ปริ้นเกรดออกมา
#รวม 1 กับ 2 เป็น function

def changeScoreToGrade(score):
    if score < 50:
        grade = "F"
    elif score < 55:
        grade = "D"
    elif score < 60:
        grade = "D+"
    elif score < 65:
        grade = "C"
    elif score < 70:
        grade = "C+"
    elif score < 75:
        grade = "B"
    elif score < 80:
        grade = "B+"
    elif score <= 100:
        grade = "A"
    else:
        grade = "Error can't calulate the grade!"
    return grade

def loopYesNo(value):
    if value == "y" or value == "Y" or value == "Yes" or value == "yes" or value == "YEs" or value == "YES": #if value.lower() == "y": แบบนี้ก็ได้นะ สั้นสะดวก
        result = True
    elif value.lower() == "n" or value == "no":
        result = False
    else:
        result = False
    return result

print("-------------------------Program----------------------------") 
switch = True
while switch == True:
    print("Hello welcome to gradeCalculator program")
    score = int(input("Enter your score to calulate(0-100) : ")) # อย่าลืมเปลี่ยน print เป็น input ล่ะ 555+
    print(f"your grade is {changeScoreToGrade(score)}")
    again = input("you wanna calculate grade again?(y/n) : ")
    switch = loopYesNo(again)
print("-------------------------Program----------------------------")

for i in range (1,10):
    print(changeScoreToGrade(72))

switch2 = True
while switch2 == True:
    print("Loop")
    loopOrNot = input("y/Y/Yes/yes or n/N/No/no : ")
    switch2 = loopYesNo(loopOrNot)
#สรุป
#จาก 22 บรรทัด เหลือ 7 ไม่ รวม function
#เอาเกรดออกมาใช้ได้เลยไม่ต้องผ่าน program เหมือนเมื่อก่อน อยากได้ B ก็แค่เรียก function C D F อะไรก็ได้ กี่ตัวก็ได้