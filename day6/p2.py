fish = {}

with open('input.txt', 'r') as file:
    t = [int(i) for i in file.read().split(',')]
    for e in t:
        if e in fish.keys():
            fish[e] += 1
        else:
            fish[e] = 1

    for i in range(9):
        if not (i in fish.keys()):
            fish[i] = 0


def day_sim(fish):
    temp = fish[0]

    # 8's move to 7's, 7's to 6's, ..., 0's to 6's and 8's (same num)
    for i in range(8):
        fish[i] = fish[i+1]

    fish[6] = fish[6] + temp # fish at zero reset to 6
    fish[8] = temp # fish at 0 each spawn new child fish at 8


for i in range(256): # simulate 80 days
    day_sim(fish)

answer = 0
for k, v in fish.items():
    answer += v


print(f'There are {answer} fish after 256 days.')