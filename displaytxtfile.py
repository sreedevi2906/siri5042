Write a Python program to append text to a file and display the text.
In [164]:
f=open("python.txt","w")
f.close()
In [165]:
f=open("python1.txt","w")
f.write("hey how do you do")
f.close()
In [166]:
f=open("python1.txt","r")
print(f.read())
f.close()
hey how do you do
In [167]:
f=open("python1.txt","a")
s='''am 
   Fine'''
f.write(s)
f.close()