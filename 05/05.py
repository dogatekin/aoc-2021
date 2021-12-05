import fileinput
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]

hits = defaultdict(int)
for line in lines:
    p1, p2 = line.split(' -> ')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            hits[x1, y] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            hits[x, y1] += 1
    else:
        x = x1
        y = y1
        x_delta = 1 if x1 < x2 else -1
        y_delta = 1 if y1 < y2 else -1
        for _ in range(abs(x2 - x1) + 1):
            hits[x, y] += 1
            x += x_delta
            y += y_delta

print(sum(hit > 1 for hit in hits.values()))
