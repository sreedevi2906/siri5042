4.Write a Python program to read last n lines of a file.

In [56]:
def LastNlines(fname, N):
  with open(fname) as file:
    for line in (file.readlines() [-N:]):
      print(line, end ='')
if __name__ == '__main__':
  fname = 'File1.txt'
  N = 3
  try:
   LastNlines(fname, N) 
  except:
   print('File not found')