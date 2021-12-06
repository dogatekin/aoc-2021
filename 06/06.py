import fileinput
from collections import Counter, defaultdict

line = next(fileinput.input())
xs = list(map(int, line.split(',')))

timers = defaultdict(int)
for x in xs:
    timers[x] += 1

def reproduce(timers, days):
    for _ in range(days):
        new_timers = timers.copy()
        for time, cnt in timers.items():
            new_timers[time] -= cnt
            if time == 0:
                new_timers[8] += cnt
                new_timers[6] += cnt
            else:
                new_timers[time-1] += cnt
        timers = new_timers
    return sum(timers.values())

print(reproduce(timers, 80))
print(reproduce(timers, 256))