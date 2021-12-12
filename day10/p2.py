lines = []

with open('input.txt', 'r') as file:
    for line in file:
        lines.append(line[:-1])

def is_incomplete(l):
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
                return False

    # if nothing in stack, line is complete
    return False if len(stack) == 0 else True  


def score(l):
    scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    stack = []
    for c in l:
        if c in pairs.keys():
            stack.append(c)
        else:
            stack.pop()

    # string incomplete, stack only contains opening parentheses
    score = 0
    while len(stack) > 0:
        t = scores[pairs[stack.pop()]]
        score *= 5
        score += t 

    return score 


scores = []

for line in lines:
    if is_incomplete(line): # incomplete but not corrupt
        scores.append(score(line))

scores.sort()
answer = scores[(len(scores)-1)//2]
print(f'Answer is {answer}')