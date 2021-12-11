import fileinput

octopi = [[int(c) for c in line.strip()] for line in fileinput.input()]
m, n = len(octopi), len(octopi[0])

DR = [-1, -1, -1, 0, 0, 1, 1, 1]
DC = [-1, 0, 1, -1, 1, -1, 0, 1]

p1 = 0
for step in range(1000):
    octopi = [[x+1 for x in row] for row in octopi]
    flashers = set()
    new_flashers = {(i, j) for i in range(m) for j in range(n) if octopi[i][j] > 9}
    while new_flashers:
        for i, j in new_flashers:
            for ni, nj in [(i+DR[d], j+DC[d]) for d in range(8)]:
                if 0 <= ni < m and 0 <= nj < n:
                    octopi[ni][nj] += 1
        flashers.update(new_flashers)
        new_flashers = {(i, j) for i in range(m) for j in range(n) if octopi[i][j] > 9 and (i, j) not in flashers}
    for i, j in flashers:
        octopi[i][j] = 0
        
    if step < 100:
        p1 += len(flashers)

    if len(flashers) == m * n:
        p2 = step + 1
        break

print(p1)
print(p2)