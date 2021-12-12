import fileinput
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]

adj = defaultdict(list)
for line in lines:
    a, b = line.split('-')
    adj[a].append(b)
    adj[b].append(a)


def find_paths(path, visited):
    cur = path[-1]
    
    if cur == 'end':
        # print(path)
        return 1
    
    if cur[0].islower():
        visited.add(cur)
    
    paths = 0
    for neighbor in adj[cur]:
        if neighbor not in visited:
            path.append(neighbor)
            paths += find_paths(path, visited)
            path.pop()
    
    if cur[0].islower():
        visited.remove(cur)
    
    return paths


p1 = find_paths(['start'], {'start'})
print(p1)


def fp(path, visited, target):
    cur = path[-1]
    
    if cur == 'end' and target in path and f'{target}2' in path:
        # print(path)
        return 1
    
    if cur[0].islower():
        visited.add(cur)
    
    paths = 0
    for neighbor in adj[cur]:
        if neighbor not in visited:
            path.append(neighbor)
            paths += fp(path, visited, target)
            path.pop()
    
    if cur[0].islower():
        visited.remove(cur)
    
    return paths


smalls = [cave for cave in adj if cave[0].islower() and cave not in ('start', 'end')]

p2 = p1
for small in smalls:
    copy = f'{small}2'
    adj[copy] = adj[small].copy()
    for neighbor in adj[small]:
        adj[neighbor].append(copy)
    p2 += fp(['start'], {'start'}, small) // 2
    for neighbor in adj[small]:
        adj[neighbor].pop()
    del adj[copy]
print(p2)