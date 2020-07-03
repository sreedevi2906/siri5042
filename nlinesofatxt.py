2.write a python program to read first n lines of a file

In [62]:
a_file=open("file_name.txt","w")
f.close()
In [66]:
a_file = open("file_name.txt")
number_of_lines = 3
for i in range(number_of_lines):
    line = a_file.readline()
print(line)