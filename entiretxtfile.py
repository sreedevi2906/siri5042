1.write a python program to read an entire text file

In [2]:
f=open("python.txt","w")
f.close()
In [3]:
f=open("python1.txt","w")
f.write("hey how do you do")
f.close()
In [4]:
f=open("python1.txt","r")
str=f.read()
print(str)
f.close()