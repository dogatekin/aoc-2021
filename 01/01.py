import fileinput

xs = [int(x) for x in fileinput.input()]

part1 = sum(x2 > x1 for x1, x2 in zip(xs[:-1], xs[1:]))
print(part1)

part2 = sum(sum(xs[i+1:i+4]) > sum(xs[i:i+3]) for i in range(len(xs)-3))
print(part2)