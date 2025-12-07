import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

start = -1
lines = [line.strip() for line in lines]
line = lines[0]
for i in range(len(line)):
    if line[i] == 'S':
        start = i
        break

def addToQueue(row,col,seen,q):
    if (row, col) in seen:
        return
    seen.add((row,col))
    q.append((row,col))

def solveFirst(grid, start):
    from collections import deque
    seen = set()
    queue = deque()
    queue.append((0,start))
    total = 0
    while queue:
        nextStop = queue.popleft()
        row, col = nextStop
        if grid[row][col] == '^':
            total += 1
            addToQueue(row,col-1,seen,queue)
            addToQueue(row,col+1,seen, queue)
        else:
            if row+1 == len(grid):
                continue
            addToQueue(row+1,col,seen,queue)
    return total
print(f"First Problem: {solveFirst(lines, start)}")


def solveSecond(grid, start):
    # dynamic programming solution
    m,n = len(grid), len(grid[0])
    table = [[0 for i in range(n)] for k in range(m-1)]
    table.append([1 for i in range(n)])
    for r in range(m-2,-1,-1):
        for c in range(n):
            if grid[r][c] == '.' or grid[r][c] == 'S':
                table[r][c] = table[r+1][c]
            else:
                table[r][c] = table[r+1][c+1] + table[r+1][c-1]
    
    return table[0][start]
print(f"Second Problem: {solveSecond(lines, start)}")
