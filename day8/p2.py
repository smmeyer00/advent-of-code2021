d = {
    1: 2, # '1' uses 2 signals (light sections)
    4: 4, # '4' uses 4 signals (light sections)
    7: 3, # etc...
    8: 7
}

'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....       0000
b    c  .    c  .    c  .    c  b    c     1    2
b    c  .    c  .    c  .    c  b    c     1    2
 ....    ....    dddd    dddd    dddd       3333
e    f  .    f  e    .  .    f  .    f     4    5
e    f  .    f  e    .  .    f  .    f     4    5
 gggg    ....    gggg    gggg    ....       6666

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

'''

# we know what chars are in 1, 4, 7, 8 due to lengths 
# 

def solve_line(inp, out): # takes line and returns number the output represents
    full_set = set('abcdefg')
    pattern = ['']*7 # which character represents what line
    one = ''
    four = ''
    seven = ''
    eight = ''
    six = ''
    zero = ''
    nine = ''
    two = ''
    five = ''
    three = ''


    num_sets = []
    for e in inp:
        num_sets.append(set(e))
        if len(e) == 2:
            one = set(e)
        elif len(e) == 4:
            four = set(e) 
        elif len(e) == 3:
            seven = set(e) 
        elif len(e) == 7:
            eight = set(e)


    # print(one, four, seven, eight)

    six_zero_nine = [] # the one missing char in 1 is 6
    two_three_five = []

    for s in num_sets:
        if len(s) == 6:
            six_zero_nine.append(s)
        elif len(s) == 5:
            two_three_five.append(s)


    # find char for position 0 
    t = (set(seven)-set(one)).pop()
    pattern[0] = t 

    # find char for position 2
    temp_rem = None 
    for s in six_zero_nine:
        if len(one-s) == 1: # s is 6
            t = (one-s).pop()
            pattern[2] = t 
            temp_rem = s
            six = s
    six_zero_nine.remove(temp_rem)
    zero_nine = six_zero_nine 
    

    # find char for position 5
    t = seven - set(pattern[0]+pattern[2])
    pattern[5] = t 

    # find which is zero and which is nine 
    t1 = zero_nine[0] - four 
    t2 = zero_nine[1] - four 
    # set with 2 lights left is 9

    if len(t1) == 2:
        nine = zero_nine[0] 
        zero = zero_nine[1] 
    else:
        nine = zero_nine[1] 
        zero = zero_nine[0] 

    # find char for position 4 
    t = (eight-nine).pop()
    pattern[4] = t 


    # find char for position 3 
    t = (eight-zero).pop()
    pattern[3] = t 

    
    # find char for position 6 
    for s in two_three_five:
        # if len(set - pos[5]) == len(set) num must be two
        if len(s - set(pattern[5])) == len(s):
            two = s 
        elif len(s - set(pattern[2])) == len(s): # must be five
            five = s
        else:
            three = s 


    nums = [zero, one, two, three, four, five, six, seven, eight, nine]
    ret_val = ''
    print('++++++++++++++++++')
    print(nums)
    print('6 is ', six)
    print('9 is ', nine)
    print('0 is ', zero)
    for e in out:
        e = set(e)
        n = nums.index(e)
        ret_val += str(n)

    return int(ret_val)

        




ans = 0

with open('input.txt', 'r') as file:
    for line in file:
        t1, t2 = line.split(" | ")

        t1 = t1.split()
        t2 = t2.split()
        # print(solve_line(t1, t2))
        ans += solve_line(t1, t2)
        

print(f'Answer is {ans}')