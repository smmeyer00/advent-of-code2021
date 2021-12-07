arr = []

with open('input.txt', 'r') as file:
    arr = [int(i) for i in file.read().split(',')]

avg = round(sum(arr)/len(arr))

def fuel_cost(n):
    s = 0
    for i in range(1, n+1):
        s += i

    return s 


def align_cost(pos):
    fuel = 0
    for e in arr:
        fuel += fuel_cost(abs(e-pos))
    return fuel 

align_at = avg 
curr = align_cost(align_at)
while 1:
    left_cost = align_cost(align_at-1)
    right_cost  = align_cost(align_at+1)
    if left_cost < curr:
        align_at -= 1
        curr = left_cost
    elif right_cost < curr:
        align_at += 1
        curr = right_cost
    else:
        # neither are less, curr is optimal alignment value
        break



print(f'Answer is {curr}')
