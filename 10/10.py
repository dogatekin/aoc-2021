import fileinput

lines = [line.strip() for line in fileinput.input()]

opener = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

scores2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

p1 = 0
incomplete = []
for line in lines:
    stack = []
    for c in line:
        if c not in opener:
            stack.append(c)
        elif stack[-1] != opener[c]:
            p1 += scores[c]
            break
        else:
            stack.pop()
    else:
        incomplete.append(stack)
print(p1)

scores = []
for stack in incomplete:
    score = 0
    for c in reversed(stack):
        score = score*5 + scores2[c]
    scores.append(score)
print(sorted(scores)[len(scores)//2])