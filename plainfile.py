9.write a python program to get the file size of a plain file.

In [124]:
file=open("test.txt","w")
f.close()
In [134]:
file=open("test.txt","w")
file.write("good night")
f.close()
In [135]:
import os
os.path.getsize("test.txt")