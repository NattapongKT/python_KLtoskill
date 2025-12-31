""""
Text Type:      str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""

#Data Type
x1 = "Hello World!"                               #str
x2 = 10                                           #int
x3 = 10.2                                         #float
x4 = 2j                                           #complex
x5 = ["apple", "banana", "cherry"]                #tuple
x6 = ("apple", "banana", "cherry")                #list
x7 = range(6)                                     #range
x8 = {"name" : "John", "age" : 36}                #dict
x9 = {"apple", "banana", "cherry"}                #set
x10 = frozenset({"apple", "banana", "cherry"})    #frozenset
x11 = True                                        #bool
x12 = b"Hello"                                    #bytes
x13 = bytearray(5)                                #bytesarray
x14 = memoryview(bytes(5))	                      #memoryview
x15 = None                                        #NoneType

#for loop
allx = [f"x{i}" for i in range(1, 16)]
print(allx)

#for loop2
for x in allx:
    print(x)

#while loop
j = 1
while j <= 7:
    print(f"Hello J : {j}")
    j += 1

#โปรแกรมคำนวณคะแนนพื้นฐาน
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