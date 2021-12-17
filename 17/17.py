import fileinput

line = next(line.strip() for line in fileinput.input())
x_coords, y_coords = line[13:].split(', ')
x_min, x_max = map(int, x_coords[2:].split('..'))
y_min, y_max = map(int, y_coords[2:].split('..'))

y_best, cnt = 0, 0
for vx0 in range(300):
    for vy0 in range(-200, 200):
        x, y = 0, 0
        vx, vy = vx0, vy0
        maxy = 0
        while x < x_max and y > y_min:
            x += vx
            y += vy
            maxy = max(y, maxy)
            vx -= 1 if vx > 0 else -1 if vx < 0 else 0
            vy -= 1
            if x_max >= x >= x_min and y_min <= y <= y_max:
                cnt += 1
                if maxy > y_best:
                    y_best = maxy
                break

print(y_best)
print(cnt)