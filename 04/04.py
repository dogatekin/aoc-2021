import fileinput

lines = [line.strip() for line in fileinput.input()]

nums = lines[0]
boards = []
for line in lines[1:]:
    if not line:
        boards.append([])
    else:
        boards[-1].append(list(map(int, line.split())))

def mark_board(board, num):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == int(num):
                board[i][j] = -1

def is_bingo(board):
    for row in board:
        if all(x == -1 for x in row):
            return True
    for j in range(len(board[0])):
        if all(board[i][j] == -1 for i in range(len(board))):
            return True
    return False

bingoes = set()
for num in nums.split(','):
    num = int(num)
    for i, board in enumerate(boards):
        if i not in bingoes:
            mark_board(board, num)
            if is_bingo(board):
                score = num * sum(x for row in board for x in row if x != -1)
                bingoes.add(i)
                if len(bingoes) == 1:
                    part1 = score
                if len(bingoes) == len(boards):
                    part2 = score

print(part1)
print(part2)