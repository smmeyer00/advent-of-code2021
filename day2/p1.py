cmds = []

with open('input.txt', 'r') as file:
    for line in file:
        cmds.append(line[:-1])

x, y = 0, 0

for e in cmds:
    d = e.split()

    if d[0] == 'forward':
        x += int(d[1]) 
    elif d[0] == 'down':
        y += int(d[1]) 
    elif d[0] == 'up':
        y -= int(d[1])


print(f'Answer is {x*y}')

