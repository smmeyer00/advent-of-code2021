fish = []

with open('input.txt', 'r') as file:
    fish = [int(i) for i in file.read().split(',')]
    print(fish)


def day_sim(fish):
    to_add = 0

    for i in range(len(fish)):
        if fish[i] == 0:
            to_add += 1
            fish[i] = 6
        else:
            fish[i] = fish[i] - 1

    for i in range(to_add):
        fish.append(8)


for i in range(80): # simulate 80 days
    day_sim(fish)

print(f'There are {len(fish)} fish after 80 days.')
    