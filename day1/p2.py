arr = []

with open("input.txt", "r") as file:
    for line in file:
        arr.append(int(line[:-1]))


arr2 = []

for i in range(len(arr)-2):
    arr2.append(arr[i]+arr[i+1]+arr[i+2])


answer = 0

for i in range(1, len(arr2)):
    if arr2[i] > arr2[i-1]:
        answer+=1

print(f"Answer is {answer}")