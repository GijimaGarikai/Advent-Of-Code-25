import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

total = 0
cur = 50
for line in lines:
    direction = 1 if line[0] == 'R' else -1
    turns = int(line[1:])
    cur = (cur + (direction*turns)) % 100
    if cur == 0:
        total += 1
        
print(f"First Problem: {total}")

total = 0
cur = 50
for line in lines:
    direction = 1 if line[0] == 'R' else -1
    turns = int(line[1:])
    interimVal = cur + (direction*turns)
    # Count how many times we do a full rotation
    passes = abs(interimVal // 100)
    # If we start at 0 going left we double count our initial position as a click
    # so we have to decrement
    if cur == 0 and line[0] == 'L':
        passes -= 1
    cur = interimVal % 100
    total += passes
    # If we end at 0 going left we don't count our last position as a click 
    # so we have to increment
    if cur == 0 and line[0] == 'L':
        total += 1

print(f"Second Problem: {total}")
    