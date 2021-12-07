arr = []

with open('input.txt', 'r') as file:
    arr = [int(i) for i in file.read().split(',')]

arr.sort()

m = arr[(len(arr)-1)//2] # median (middle) value of arr

fuel = 0

for e in arr:
    fuel += abs(e-m)

print(f'Answer is {fuel}')
