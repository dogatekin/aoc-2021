import fileinput
from collections import Counter


heights = []

lines = [line.strip() for line in fileinput.input()]

m = len(lines)
n = len(lines[0])

heights.append([10]*(n+2))
for line in lines:
    heights.append([10] + list(map(int, line)) + [10])
heights.append([10]*(n+2))

low_points = []
p1 = 0
for i in range(1, 1+m):
    for j in range(1, 1+n):
        if all(heights[i][j] < heights[i+di][j+dj] for di, dj in ((0,1),(0,-1),(1,0),(-1,0))):
            low_points.append((i, j))
            p1 += heights[i][j] + 1

print(p1)

def find_neighbors(i, j, basins):
    neighbors = []
    for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
        ni, nj = i+di, j+dj
        if (ni, nj) in basins or heights[ni][nj] >= 9 or heights[ni][nj] <= heights[i][j]:
            continue
        neighbors.append((ni, nj))
    return neighbors
        

basins = {}
for basin, (i, j) in enumerate(low_points):
    basins[i, j] = basin
    stack = find_neighbors(i, j, basins)
    while stack:
        ni, nj = stack.pop()
        basins[ni, nj] = basin
        stack.extend(find_neighbors(ni, nj, basins))

p2 = 1
for basin, cnt in Counter(basins.values()).most_common(3):
    p2 *= cnt
print(p2)
        