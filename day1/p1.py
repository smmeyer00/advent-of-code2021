arr = []

with open("input.txt", "r") as file:
    for line in file:
        arr.append(int(line[:-1]))


answer = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        answer += 1


print(f"{answer} increases")
