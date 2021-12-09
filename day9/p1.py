h_map = []

with open('input.txt', 'r') as file:
    for line in file:
        h_map.append([int(i) for i in list(line[:-1])])

risk = 0

for i in range(len(h_map)):
    for j in range(len(h_map[0])):
        if (i == 0 and j == 0):
            # top left corner 
            if h_map[i][j] < h_map[i+1][j] and h_map[i][j] < h_map[i][j+1]:
                # low point 
                risk += (h_map[i][j] + 1)

        elif (i == 0 and j == len(h_map[0])-1):
            # top right corner
            if h_map[i][j] < h_map[i][j-1] and h_map[i][j] < h_map[i+1][j]:
                # low point
                risk += (h_map[i][j] + 1)

        elif (i == len(h_map)-1 and j == 0):
            # bottom left corner
            if h_map[i][j] < h_map[i-1][j] and h_map[i][j] < h_map[i][j+1]:
                # low point
                risk += (h_map[i][j] + 1)

        elif (i == len(h_map)-1 and j == len(h_map[0])-1):
            # bottom right corner
            if h_map[i][j] < h_map[i-1][j] and h_map[i][j] < h_map[i][j-1]:
                # low point
                risk += (h_map[i][j] + 1)

        elif i == 0:
            # top row but not corner
            if h_map[i][j] < h_map[i][j-1] and h_map[i][j] < h_map[i][j+1] and h_map[i][j] < h_map[i+1][j]:
                # low point
                risk += (h_map[i][j] + 1)

        elif j == 0:
            # left column but not corner
            if h_map[i][j] < h_map[i-1][j] and h_map[i][j] < h_map[i+1][j] and h_map[i][j] < h_map[i][j+1]:
                # low point
                risk += (h_map[i][j] + 1)

        elif i == len(h_map)-1:
            # bottom row but not corner
            if h_map[i][j] < h_map[i][j-1] and h_map[i][j] < h_map[i][j+1] and h_map[i][j] < h_map[i-1][j]:
                # low point
                risk += (h_map[i][j] + 1)

        elif j == len(h_map[0])-1:
            # right column but not corner
            if h_map[i][j] < h_map[i-1][j] and h_map[i][j] < h_map[i+1][j] and h_map[i][j] < h_map[i][j-1]:
                # low point
                risk += (h_map[i][j] + 1)

        else:
            # all other points
            if h_map[i][j] < h_map[i+1][j] and h_map[i][j] < h_map[i-1][j] and h_map[i][j] < h_map[i][j+1] and h_map[i][j] < h_map[i][j-1]:
                # low point
                risk += (h_map[i][j] + 1)


print(f'Answer is {risk}')