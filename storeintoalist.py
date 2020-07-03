6.write a program to read a file line by line store it into a list

In [97]:
infile=open("test.txt","w")
f.close()
In [103]:
infile=open("test1.txt","w")
infile.write("hello")
f.close()
In [104]:
infile = "test1.txt"
content_list = open(infile).readlines()
print (content_list)