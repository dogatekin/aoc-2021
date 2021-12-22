from collections import defaultdict
import fileinput

lines = [line.strip() for line in fileinput.input()]

iea = lines[0]

pixels = defaultdict(lambda: '.')
grid = lines[2:]
m, n = len(grid), len(grid[0])
for i in range(m):
    for j in range(n):
        if grid[i][j] == '#':
            pixels[i, j] = '#'

def new_state(i, j, even=False, imin=-1e9, imax=1e9, jmin=-1e9, jmax=1e9):
    n = []
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ni, nj = i+di, j+dj
            if even and (ni <= imin or ni >= imax-1 or nj <= jmin or nj >= jmax-1):
                n.append('#')    
            else:
                n.append(pixels[ni, nj])
    ind = int(''.join(['0' if d == '.' else '1' for d in n]), 2)
    return iea[ind]

for step in range(1, 51):
    light_ups = []

    for i in range(-step, m+step):
        for j in range(-step, n+step):
            if new_state(i, j, step % 2 == 0, -step, m+step, -step, n+step) == '#':
                light_ups.append((i, j))
    pixels = defaultdict(lambda: '.')
    for coord in light_ups:
        pixels[coord] = '#'
        
    if step == 2:
        print(len(light_ups))

print(len(light_ups))