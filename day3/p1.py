inp = []

with open('input.txt', 'r') as file:
    for line in file: 
        inp.append(line[:-1])

gamma = '' # most common bit 
epsilon = '' # least common bit 

for i in range(len(inp[0])): # for each bit
    ones, zeros = 0, 0
    for j in range(len(inp)): # for each input 
        if inp[j][i] == '0':
            zeros += 1
        else:
            ones += 1

    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f'Answer is {gamma*epsilon}')