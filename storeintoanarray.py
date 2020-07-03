7.write a python program to read a file line by line store it into a array.

In [110]:
f2=open("test1.txt","w")
f.close()
In [117]:
f2=open("test1.txt","w")
s='''how
     are
     You'''
f2.write(s)
f.close()
In [118]:
f2=("test1.txt")
content_array=open(f2).readlines()
print(content_array)