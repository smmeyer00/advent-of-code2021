end_pts = []

with open('input.txt', 'r') as file:
    for line in file:
        t = line.split(' -> ')

        p1 = [int(i) for i in t[0].split(',')]
        p2 = [int(i) for i in t[1].split(',')]


        end_pts.append([p1, p2])


def parse_line(start, end, dict):
    if start[0] == end[0]: # vertical line
        offset = 1 if start[1] < end[1] else -1
        for i in range(start[1], end[1]+offset, offset):
            p = str([start[0], i]) # new point as string
            if p in dict.keys():
                dict[p] += 1
            else:
                dict[p] = 1
    elif start[1] == end[1]: # horizontal line
        offset = 1 if start[0] < end[0] else -1
        for i in range(start[0], end[0]+offset, offset):
            p = str([i, start[1]]) 
            if p in dict.keys():
                dict[p] += 1
            else:
                dict[p] = 1


pt_dict = {}

for line in end_pts:
    start = line[0]
    end = line[1]

    if start[0] == end[0] or start[1] == end[1]: # vertical or horizontal
        parse_line(start, end, pt_dict)


intersections = 0

for k in pt_dict.keys():
    if pt_dict[k] > 1:
        intersections += 1

print(f'Answer is {intersections}')
