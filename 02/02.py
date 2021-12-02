import fileinput

cmds = [line.strip() for line in fileinput.input()]

x, y1, y2, aim = 0, 0, 0, 0

for cmd in cmds:
    d, delta = cmd.split()
    delta = int(delta)
    
    if d == 'forward':
        x += delta
        y2 += aim * delta
    elif d == 'up':
        y1 -= delta
        aim -= delta
    elif d == 'down':
        y1 += delta
        aim += delta

part1 = x * y1
print(part1)

part2 = x * y2
print(part2)