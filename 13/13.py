import fileinput

lines = [line.strip() for line in fileinput.input()]

points = set()
instructions = []

def pp(points):
    xmax = max(p[0] for p in points)
    ymax = max(p[1] for p in points)
    for r in range(ymax+1):
        for c in range(xmax+1):
            print('█' if (c, r) in points else ' ', end='')
        print()

flag = False
for line in lines:
    if line == '':
        flag = True
        continue
    
    if not flag:
        points.add(tuple(map(int, line.split(','))))
    else:
        instructions.append(line.split()[2])

for fold, instruction in enumerate(instructions):
    axis, num = instruction.split('=')
    axis = 0 if axis == 'x' else 1
    num = int(num)
    
    to_del = {p for p in points if p[axis] > num}
    to_add = {(2*num - p[0], p[1]) if axis == 0 else (p[0], 2*num - p[1]) for p in to_del}
    points |= to_add
    points -= to_del
    
    if fold == 0:
        print(len(points))

pp(points)