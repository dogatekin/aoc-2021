import fileinput
from collections import Counter, defaultdict

line = next(fileinput.input())
xs = list(map(int, line.split(',')))

median = sorted(xs)[len(xs)//2]
print(sum(abs(median - x) for x in xs))

mean = sum(xs) // len(xs)

def calc_fuel(x, y):
    d = abs(x - y)
    return d * (d + 1) // 2

print(sum(calc_fuel(x, mean) for x in xs))

best = 10e9
for pos in range(min(xs), max(xs)+1):
    fuel = sum(calc_fuel(x, pos) for x in xs)
    best = min(best, fuel)

print(best)