import fileinput
import numpy as np
from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in fileinput.input()]


def dijkstra(grid):
    m, n = len(grid), len(grid[0])

    def neighbors(i, j):
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n:
                yield (ni, nj)

    dist = {}
    heap = [(0, (0, 0))]

    while heap:
        d, (i, j) = heappop(heap)
        
        if i == m-1 and j == n-1:
            print(d)
            break

        if (i, j) not in dist:
            dist[i, j] = d
            for ni, nj in neighbors(i, j):
                if (ni, nj) not in dist:
                    heappush(heap, (d + grid[ni][nj], (ni, nj)))

dijkstra(grid)

grid = np.array(grid)
plus = {}
for i in range(9):
    added = grid + i
    added[added > 9] -= 9
    plus[i] = added

extended = np.vstack(tuple(np.hstack(tuple(plus[i] for i in range(row, row+5))) for row in range(5)))
dijkstra(extended)