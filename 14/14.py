import fileinput
from collections import Counter, defaultdict

lines = [line.strip() for line in fileinput.input()]

polymers = list(lines[0])

rules = {}
for line in lines[2:]:
    inp, out = line.split(' -> ')
    rules[tuple(inp)] = out

def solve(steps):
    cnts = Counter(zip(polymers, polymers[1:]))
    tot_cnts = Counter(polymers)
    
    for _ in range(steps):
        new_cnts = defaultdict(int)
        for pair, cnt in cnts.items():
            if pair in rules:
                out = rules[pair]
                tot_cnts[out] += cnt
                new_cnts[pair[0], out] += cnt
                new_cnts[out, pair[1]] += cnt
            else:
                new_cnts[pair] += cnt
        cnts = new_cnts

    tot_cnts = tot_cnts.most_common()
    return tot_cnts[0][1] - tot_cnts[-1][1]

print(solve(10))
print(solve(40))