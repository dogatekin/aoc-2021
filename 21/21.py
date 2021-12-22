import fileinput
from collections import Counter, defaultdict

lines = [line.strip() for line in fileinput.input()]

positions = [int(line[-1]) for line in lines]
scores = [0, 0]
die = 1
player = 0
rolls = 0
while True:
    x = 0
    for _ in range(3):
        x += die
        die = (die % 100) + 1
        rolls += 1
    positions[player] = ((positions[player] - 1 + x) % 10) + 1
    scores[player] += positions[player]
    
    if scores[player] >= 1000:
        break
    
    player = 1 - player
    
print(rolls * scores[1 - player])

p1, p2 = [int(line[-1]) for line in lines]
states = {(p1, p2, 0, 0): 1}
player = 0
rolls = Counter(x+y+z for x in range(1,4) for y in range(1,4) for z in range(1,4))
wins = [0, 0]
while True:
    new_states = defaultdict(int)
    for (p1, p2, s1, s2), universes in states.items():
        for roll, cnt in rolls.items():
            ps = [p1, p2]
            ss = [s1, s2]
            ps[player] = ((ps[player] - 1 + roll) % 10) + 1
            ss[player] += ps[player]
            if ss[player] >= 21:
                wins[player] += universes * cnt
            else:
                new_states[(*ps, *ss)] += universes * cnt
    player = 1 - player
    if not new_states:
        break
    states = new_states

print(max(wins))