import os

base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "input.txt")

with open(file_path, "r") as f:
    lines = f.readlines()

boxes = []
for line in lines:
    x,y,z = line.split(',')
    boxes.append((int(x),int(y),int(z)))

n = len(lines)
parent = list(range(n))
size = [1] * n

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        return False
    if size[pa] < size[pb]:
        pa, pb = pb, pa
    parent[pb] = pa
    size[pa] += size[pb]
    return True

def getDist(p1,p2):
    x = p1[0]-p2[0]
    y = p1[1]-p2[1]
    z = p1[2]-p2[2]
    return (x*x + y*y + z*z)**0.5

weights = []
for i in range(n):
    for j in range(i+1,n):
        dist = getDist(boxes[i], boxes[j])
        weights.append((dist, (i, j)))

weights.sort()

for i in range(1000):
    _, (a, b) = weights[i]
    union(a, b)

componentSizes = {}

for i in range(n):
    root = find(i)
    componentSizes[root] = componentSizes.get(root, 0) + 1

sizesSorted = sorted(componentSizes.values())
big1, big2, big3 = sizesSorted[-1], sizesSorted[-2], sizesSorted[-3]
solution1 = big1 * big2 * big3

# reset for neater looping
parent = list(range(n))
size = [1] * n
components = n

last_product = None

for dist, (a, b) in weights:
    merged = union(a, b)
    if merged:
        components -= 1
        if components == 1:
            x1 = boxes[a][0]
            x2 = boxes[b][0]
            last_product = x1 * x2
            break

solution2 = last_product

print(f"First Problem: {solution1}")

print(f"Second Problem: {solution2}")


    