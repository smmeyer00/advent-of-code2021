lines = []

with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line[:-1])

def line_score(l):
    score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    stack = []

    for c in l:
        if c in pairs.values():
            stack.append(c)
        else:
            t = stack.pop()
            if pairs[c] != t:
                # corrupt chunk, c is illegal
                return score[c]

    return 0


score = 0

for line in lines:
    score += line_score(line)

print(f'Answer is {score}')