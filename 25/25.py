import fileinput

grid = [list(line.strip()) for line in fileinput.input()]

def pp(grid):
    for row in grid:
        print(''.join(row))
        
m, n = len(grid), len(grid[0])
steps = 0 
while True:
    rights = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '>' and grid[i][(j+1) % n] == '.':
                rights.append((i, j))
    
    for i, j in rights:
        grid[i][j] = '.'
        grid[i][(j+1) % n] = '>'

    downs = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'v' and grid[(i+1) % m][j] == '.':
                downs.append((i, j))
         
    for i, j in downs:
        grid[i][j] = '.'
        grid[(i+1) % m][j] = 'v'
    
    steps += 1
    if not (rights or downs):
        break
        
print(steps)