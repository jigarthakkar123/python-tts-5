file=open("tops1.txt","w")
file.write("This is file input//output demo using python.")
file.close()
print("File Written Successfully")

print("*"*60)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*60)

file=open("tops1.txt","a")
file.write("\nNow This file is appended.")
file.close()

print("*"*60)

file=open("tops1.txt","r")
print(file.read())
file.close()

print("*"*60)

file=open("tops2.txt","w+")
file.write("This is read/write operation using w+ mode.")
print("Current File Position : ",file.tell())
file.seek(20)
print(file.read())
file.close()

print("*"*60)
