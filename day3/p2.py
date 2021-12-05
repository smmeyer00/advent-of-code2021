inp = []

with open('input.txt', 'r') as file:
    for line in file: 
        inp.append(line[:-1])

o2_filter = inp.copy()
co2_filter = inp.copy()

index = 0
while len(o2_filter) > 1: 
    ones, zeros = 0, 0

    for i in range(len(o2_filter)): # count zeros and ones
        if o2_filter[i][index] == '0':
            zeros += 1
        else:
            ones += 1

    temp = []
    if ones >= zeros: # only keep inputs with '1' at index
        for i in range(len(o2_filter)):
            if o2_filter[i][index] == '1': # keep
                temp.append(o2_filter[i])
    else: # keep inputs with '0' at index 
        for i in range(len(o2_filter)):
            if o2_filter[i][index] == '0':
                temp.append(o2_filter[i])

    o2_filter = temp 
    index += 1

index = 0
while len(co2_filter) > 1:
    ones, zeros = 0, 0

    for i in range(len(co2_filter)):
        if co2_filter[i][index] == '0':
            zeros += 1
        else:
            ones += 1


    temp = []
    if zeros <= ones: # keep inputs with '0' at index
        for i in range(len(co2_filter)):
            if co2_filter[i][index] == '0':
                temp.append(co2_filter[i])
    else: # keep inputs with '1' at index
        for i in range(len(co2_filter)):
            if co2_filter[i][index] == '1':
                temp.append(co2_filter[i])

    co2_filter = temp 
    index += 1

o2_rating = int(o2_filter[0], 2)
co2_rating = int(co2_filter[0], 2)

print(f'Answer is {o2_rating*co2_rating}')
