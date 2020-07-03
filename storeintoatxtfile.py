.Write a Python program to count the number of lines in a text file.

In [120]:
f3=open("file.txt","w")
f3.close()
In [121]:
f3=open("file.txt","w")
s='''i
     love to
     Code'''
f3.write(s)
f3.close()
In [122]:
f3=open("file.txt","r")
s=f3.read()
print(len(s.split('\n')))
f.close()