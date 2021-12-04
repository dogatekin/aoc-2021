import fileinput
from collections import Counter

xs = [x.strip() for x in fileinput.input()]

num_bits = len(xs[0])

mcs = []
lcs = []
for i in range(num_bits):
    cnts = Counter(x[i] for x in xs)
    mc, lc = cnts.most_common()
    mcs.append(mc[0])
    lcs.append(lc[0])

part1 = int(''.join(mcs), 2) * int(''.join(lcs), 2)

oxy = xs.copy()
co2 = xs.copy()

for i in range(num_bits):
    cnts = Counter(num[i] for num in oxy)
    most_common, cnt = cnts.most_common(1)[0]
    if cnt == len(oxy) / 2:
        most_common = '1' 
    oxy = [num for num in oxy if num[i] == most_common]
    if len(oxy) == 1:
        break

for i in range(num_bits):
    cnts = Counter(num[i] for num in co2)
    most_common, cnt = cnts.most_common()[-1]
    if cnt == len(co2) / 2:
        most_common = '0' 
    co2 = [num for num in co2 if num[i] == most_common]
    if len(co2) == 1:
        break

part2 = int(oxy[0], 2) * int(co2[0], 2)

print(part1)
print(part2)