
f = open("demofile.txt")
print("------------------1--------------------")
print(f.readline())

with open("demofile.txt") as f:
  print("------------------2--------------------")
  print(f.read(5))

#loop
print("------------------3--------------------")
with open("demofile.txt") as f:
  for x in f:
    print(x)

f = open("D:\Github-Project\python_KLtoskill\Day_6\demofile.txt")
print("------------------4--------------------")
print(f.read())

"""
Close Files
It is a good practice to always close the file when you are done with it.

If you are not using the with statement, you must write a close statement in order to close the file:
"""
f.close()

#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
#-----------------------------------------------------------
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print("------------------5--------------------")
  print(f.read())

#-----------------------------------------------------------
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print("------------------6--------------------")
  print(f.read())

#-----------------------------------------------------------
with open("demofile.json", "w") as f:
  f.write("{\"name\": \"John\",\"age\": 30,\"city\": \"New York\"}")

#open and read the file after the overwriting:
with open("demofile.json") as f:
  print("------------------6--------------------")
  print(f.read())

#"x" - Create - will create a file, returns an error if the file exists
try:
  f = open("myfile.txt", "x")
except:
  print("error file exists: 'myfile.txt'")