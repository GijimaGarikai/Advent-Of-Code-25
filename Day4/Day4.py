import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    matrix = f.readlines()
    for i in range(len(matrix)):
       # make matrix into list of lists for mutability in part 2 lol
       matrix[i] = list(matrix[i])

def isAtSign(table, x,y):
   rows, cols = len(table), len(table[0])
   if x < 0 or x >= rows or y < 0 or y >= cols:
      return False
   if table[x][y] == '@':
      return True
   return False
   

def countNeighs(x,y,table):
  total = 0
  for row in range(x-1, x+2):
     for col in range(y-1, y+2):
        if row == x and col == y:
           continue
        if isAtSign(table, row, col):
           total += 1
  return total

def getTotal(table, isPartTwo=False):
    totalRows = len(table)
    totalCols = len(table[0])
    ans = 0
    for i in range(totalRows):
        for j in range(totalCols):
            if table[i][j] != '@':
               continue
            neighs = countNeighs(i,j,table)
            if neighs < 4:
                ans += 1
                if isPartTwo:
                    table[i][j] = '.'
    return ans
def first_problem(matrix):
   return getTotal(matrix)

def second_problem(matrix):
    total = 0
    cur = getTotal(matrix, isPartTwo=True)
    while cur > 0:
        total += cur
        cur = getTotal(matrix, isPartTwo=True)
    return total

print(f"First Problem: {first_problem(matrix)}")
print(f"Second Problem: {second_problem(matrix)}")
