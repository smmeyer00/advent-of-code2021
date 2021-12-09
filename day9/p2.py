h_map = []

with open('input.txt', 'r') as file:
    for line in file:
        h_map.append([int(i) for i in list(line[:-1])])



def traverse(row, col, s):
    if h_map[row][col] == 9:
        return 

    to_visit = []

    if (row-1) >= 0:
        to_visit.append([row-1, col])
    if (row+1) < len(h_map):
        to_visit.append([row+1, col])
    if (col-1) >= 0:
        to_visit.append([row, col-1])
    if (col+1) < len(h_map[0]):
        to_visit.append([row, col+1])

    s[0] = s[0] + 1
    h_map[row][col] = 9 # set as visited

    for p in to_visit:
        r, c = p
        traverse(r, c, s)
    


sizes = []

for row in range(len(h_map)):
    for col in range(len(h_map[0])):
        s = [0]
        traverse(row, col, s)
        sizes.append(s[0])

sizes.sort()

print(f'Answer is {sizes[-1] * sizes[-2] * sizes[-3]}')