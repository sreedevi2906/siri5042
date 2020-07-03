10.write a python program to copy the contents of a file into another.

In [154]:
file1=open("f1.txt","w")
file1.close()
In [173]:
file1=open("f1.txt","w")
s='''welcome 
     to gitam 
     University'''
file1.write(s)
file1.close()
In [174]:
file2=open("f2.txt","w")
file1=open("f1.txt","r")
for line in file1:
  file2.write(line)
file1.close()
file2.close()