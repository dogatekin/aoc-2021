import fileinput
from inspect import getsource
from collections import Counter, defaultdict

lines = [line.strip() for line in fileinput.input()]

scanners = []
for line in lines:
    if line.startswith('---'):
        scanners.append(set())
    elif line:
        scanners[-1].add(tuple(map(int, line.split(','))))

transforms = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (y, -x, z),
    
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (y, x, -z),
    
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (y, z, x),
    
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (y, -z, -x),
    
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-z, -x, y),
    
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (z, -x, -y),
]

s0: set = scanners[0]
s1 = scanners[1]

appears = defaultdict(int)
for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        s1 = scanners[i]
        s2 = scanners[j]
        for transform in transforms:
            s2t = {transform(*point) for point in s2}
            cnts = Counter()
            for x1, y1, z1 in s1:
                for x2, y2, z2 in s2t:
                    cnts[(x1-x2, y1-y2, z1-z2)] += 1
            offset, matches = cnts.most_common(1)[0]
            if matches == 12:
                print(s2t)
                print(i, j, offset, getsource(transform))

# for transform in transforms:
#     s1t = {transform(*point) for point in s1}
#     cnts = Counter()
#     for x0, y0, z0 in s0:
#         for x1, y1, z1 in s1t:
#             cnts[(x0-x1, y0-y1, z0-z1)] += 1
#     offset, matches = cnts.most_common(1)[0]
#     if matches == 12:
#         print(offset)
#         print(transform(1, 2, 3))