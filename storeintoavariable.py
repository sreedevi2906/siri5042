5.Write a Python program to read a file line by line store it into a variable.

In [105]:
f1=open("test.txt","w")
f.close()
In [106]:
f1=open("test1.txt","w")
f1.write("hi")
f.close()
In [109]:
f1=open('test1.txt').readlines()
print(f1)