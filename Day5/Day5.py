import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")
ranges = []
with open(file_path, "r") as f:
    lines = f.readlines()


ranges = []
isIds = False
idArr = []

# create range array and id array
for line in lines:
    line = line.strip()
    if not line:
        isIds = True
        continue

    if isIds:
        idArr.append(int(line))
    else:
        low, high = line.split('-')
        low = int(low)
        high = int(high)
        ranges.append((low,high))

# sort both arrays for ease of computing
idArr.sort()
ranges.sort()

def solveFirst(idArr, ranges): 
    rangePos = 0
    idPos = 0
    total = 0

    while idPos < len(idArr):
        if rangePos >= len(ranges):
            break
        # Below minimum range, consider next id
        if idArr[idPos] < ranges[rangePos][0]:
            idPos += 1 
        # Above current range, consider next range
        elif idArr[idPos] > ranges[rangePos][1]:
            rangePos += 1
        # Just right
        elif ranges[rangePos][0] <= idArr[idPos] <= ranges[rangePos][1]:
            total += 1
            idPos += 1
    return total

# Merge all intervals for ease of computing
def merge(intervals):
    # Assume intervals are sorted
    prevstart = intervals[0][0]
    prevend = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        curstart = intervals[i][0]
        curend = intervals[i][1]
        if curstart <= prevend:
            if curend > prevend:
                prevend = curend
            continue
        intervals[count] = [prevstart, prevend]
        count += 1
        prevend = curend
        prevstart = curstart
    intervals[count] = [prevstart, prevend]
    count += 1
    for i in range(len(intervals)-count):
        intervals.pop()
    return intervals

def solveSecond(ranges):
    ranges = merge(ranges)

    total = 0
    for lo, hi in ranges:
        total += ((hi-lo) +1)
    return total

print(f"First Problem: {solveFirst(idArr, ranges)}")
print(f"Second Problem: {solveSecond(ranges)}")