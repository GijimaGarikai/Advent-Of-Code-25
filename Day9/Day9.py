import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

points = []

for line in lines:
    if line.strip():
        parts = line.strip().split(',')
        points.append((int(parts[0]), int(parts[1])))

def getArea(p1,p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height
def solveFirst(points):
    maxA = -1
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]
            maxA = max(maxA, getArea(p1,p2))
    return maxA


def isPointInside(x, y, edges):
    inside = False
    for (x1, y1), (x2, y2) in edges:
        if x1 == x2 and x1 > x:
            if min(y1, y2) <= y < max(y1, y2):
                inside = not inside
    return inside

def edgesIntersectRect(rMinX, rMaxX, rMinY, rMaxY, edges):
    for (x1, y1), (x2, y2) in edges:
        edgeMinX, edgeMaxX = min(x1, x2), max(x1, x2)
        edgeMinY, edgeMaxY = min(y1, y2), max(y1, y2)

        if x1 == x2:
            # Vertical edge intersection
            if rMinX < x1 < rMaxX:
                if max(rMinY, edgeMinY) < min(rMaxY, edgeMaxY):
                    return True
        elif y1 == y2:
            # Horizontal edge intersection
            if rMinY < y1 < rMaxY:
                if max(rMinX, edgeMinX) < min(rMaxX, edgeMaxX):
                    return True
    return False

def solveSecond(points):
    n = len(points)
    edges = []
    for i in range(n):
        edges.append((points[i], points[(i + 1) % n]))

    candidates = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            area = getArea(p1,p2)
            
            minX, maxX = min(p1[0], p2[0]), max(p1[0], p2[0])
            minY, maxY = min(p1[1], p2[1]), max(p1[1], p2[1])
            
            candidates.append((area, minX, maxX, minY, maxY))

    candidates.sort(key=lambda x: x[0], reverse=True)

    for rect in candidates:
        area, rMinX, rMaxX, rMinY, rMaxY = rect
        
        centerX = (rMinX + rMaxX) / 2
        centerY = (rMinY + rMaxY) / 2

        if not isPointInside(centerX, centerY, edges):
            continue

        if edgesIntersectRect(rMinX, rMaxX, rMinY, rMaxY, edges):
            continue

        return area

    return 0

print(f"First Problem: {solveFirst(points)}")

print(f"Second Problem: {solveSecond(points)}")
