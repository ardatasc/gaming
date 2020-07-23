row, column  = input().split()
row, column = int(row), int(column)
x = 0
hashCounter = 0

def Gaming(Xposition, Yposition):
    if(field[Xposition][Yposition] == "#"):



field = [''] * row

for i in range(row):
  field[i] = list(input())


for i in range(row):
 if (len(field[i]) == column):
  i = 0
  x += 1
 for x in range(column):
   if(len(field[x]) == row):
       i += 1
       x = 0
