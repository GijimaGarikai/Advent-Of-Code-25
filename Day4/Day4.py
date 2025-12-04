import os
from collections import deque

# Read input
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

def getTotal(table):
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
    return ans
def first_problem(matrix):
   return getTotal(matrix)

def second_problem(table):
    rows, cols = len(table), len(table[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


    # Precompute neighbor counts
    neigh = [[0]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if table[r][c] != '@':
                continue
            count = 0
            for dr, dc in dirs:
                # get num of neighbors
                curRow, curCol = r + dr, c + dc
                if isAtSign(table, curRow, curCol):
                    count += 1
            neigh[r][c] = count

    q = deque()
    
    # Initialize queue: all accessible rolls
    for r in range(rows):
        for c in range(cols):
            if table[r][c] == '@' and neigh[r][c] < 4:
                q.append((r, c))

    removed = 0

    while q:
        r, c = q.popleft()

        # If already removed, skip
        if table[r][c] != '@':
            continue

        # Remove it
        table[r][c] = '.'
        removed += 1

        # Update neighbors
        for dr, dc in dirs:
            curRow, curCol = r + dr, c + dc
            if isAtSign(table, curRow, curCol):
                neigh[curRow][curCol] -= 1
                if neigh[curRow][curCol] < 4:
                    q.append((curRow, curCol))

    return removed


print(f"First Problem: {first_problem(matrix)}")
print(f"Second Problem: {second_problem(matrix)}")
