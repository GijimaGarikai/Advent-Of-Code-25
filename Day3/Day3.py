import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

def getMax(line):
    best = -1
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            val = int(line[i] + line[j])
            if val > best:
                best = val
    return best
def solve_first(input):
    total = 0
    for line in input:
        total += getMax(line)
    return total

print(f"First Problem: {solve_first(lines)}")


def getMax12(s,k=12):
    # monotonic stack approach
    stack = []
    # how many digits we are allowed to remove
    drops = len(s) - k

    for c in s:
        while drops > 0 and stack and stack[-1] < c:
            stack.pop()
            drops -= 1
        stack.append(c)

    # if we didn't remove enough digits, trim from the end
    return int("".join(stack[:k]))

def solve_second(input):
    total = 0
    for line in input:
        total += getMax12(line.strip())
    return total

print(f"Second Problem: {solve_second(lines)}")

