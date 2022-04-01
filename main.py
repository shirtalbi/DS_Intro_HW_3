#part 1
def read_line(n, file):
  try:
    file = open(file)
    count = 0
    for i in file:
      count = count + 1
      if count == n:
          return i
    if count < n:
      return "line " + str(n) + " doesn't exist"
    if type(n) != int:
      return ("invalid input detected")
    if count == n:
      return (i)
  except:
    return "file not found"


#Part 2
def longest_words(file):
 try:
    file_n = open(file)
    file_n=file_n.read()
    file_n=file_n.replace(',', ' ')
    file_n=file_n.replace('-',' ')
    file_n=file_n.replace('.',' ')
    file_w=file_n.split()
    l_sort=sorted(file_w,key=len,reverse=True)
    return l_sort[0:5]
 except:
    return "file not found"