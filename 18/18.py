from copy import deepcopy
from math import floor, ceil
import fileinput

lines = [eval(line.strip()) for line in fileinput.input()]
lines2 = deepcopy(lines)

def explode(n: list, level=1):
    exploded, l_added, r_added = False, False, False
    l, r = None, None
    for i, x in enumerate(n):
        if not exploded and isinstance(x, list):
            if level == 4:
                l, r = n.pop(i)
                n.insert(i, 0)
                exploded = True
                if i > 0:
                    n[i-1] += l
                    l_added = True
            else:
                exploded, l, l_added, r, r_added = explode(x, level+1)
                if exploded and not l_added and i > 0:
                    if isinstance(n[i-1], int):
                        n[i-1] += l
                    elif isinstance(n[i-1], list):
                        y = n[i-1]
                        while isinstance(y[-1], list):
                            y = y[-1]
                        y[-1] += l
                    l_added = True
        elif exploded and not r_added:
            assert r is not None
            if isinstance(x, int):
                n[i] += r
            elif isinstance(x, list):
                y = x
                while isinstance(y[0], list):
                    y = y[0]
                y[0] += r
            r_added = True
            break
    return exploded, l, l_added, r, r_added

def split(n: list):
    splitted = False
    for i, x in enumerate(n):
        if isinstance(x, int) and x >= 10:
            n.pop(i)
            n.insert(i, [floor(x / 2), ceil(x / 2)])
            splitted = True
            break
        elif isinstance(x, list):
            splitted = split(x)
            if splitted:
                break
    return splitted

def mag(n: list | int):
    if isinstance(n, int):
        return n
    else:
        return 3*mag(n[0]) + 2*mag(n[1])

n = lines[0]
for line in lines[1:]:
    n = [n] + [line]
    exploded = True
    splitted = False
    while exploded or splitted:
        exploded, _, _, _, _ = explode(n)
        if not exploded:
            splitted = split(n)
print(mag(n))

mn = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            n = [deepcopy(lines2[i])] + [deepcopy(lines2[j])]
            exploded = True
            splitted = False
            while exploded or splitted:
                exploded, _, _, _, _ = explode(n)
                if not exploded:
                    splitted = split(n)
            mn = max(mn, mag(n))

print(mn)