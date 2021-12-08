
d = {
    1: 2, # '1' uses 2 signals (light sections)
    4: 4, # '4' uses 4 signals (light sections)
    7: 3, # etc...
    8: 7
}

def one_four_seven_eights(inp):
    s = 0
    for e in inp:
        if len(e) in [2, 4, 3, 7]:
            s += 1
    return s

ans = 0

with open('input.txt', 'r') as file:
    for line in file:
        t1, t2 = line.split(" | ")

        # t1 = t1.split()
        t2 = t2.split()
        
        ans += one_four_seven_eights(t2)

print(f'Answer is {ans}')