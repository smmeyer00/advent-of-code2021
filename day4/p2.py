class Board:

    def __init__(self, matrix):
        self.matrix = matrix 

    def print(self):
        for row in self.matrix:
            print(row)
        print()

    def has_won(self): 
        found_win = False 
        
        # check rows
        for row in self.matrix:
            if row == [-1, -1, -1, -1, -1]: # all marked
                found_win = True 

        # check cols 
        for i in range(len(self.matrix[0])):
            s = 0
            for j in range(len(self.matrix)):
                s += self.matrix[j][i]

            if s == -5: # all marked in col
                found_win = True 

        return found_win
    
    def mark(self, num):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == num:
                    self.matrix[i][j] = -1

    def score(self, num):
        s = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] >= 0:
                    s += self.matrix[i][j]

        return s*num 


# load data 

nums = []
boards = []
content = []
with open('input.txt', 'r') as file:
    for line in file:
        content.append(line[:-1])

for e in content[0].split(','):
    nums.append(int(e))     

for i in range(2, len(content), 6):
    m = []
    for offset in range(5): # each row of board
        row = []

        for e in content[i+offset].split():
            row.append(int(e))

        m.append(row)

    boards.append(Board(m))

# simulate game
for num in nums: # for each num called
    # mark each board
    for b in boards:
        b.mark(num)

    if len(boards) > 1:
        # only keep boards that have not won
        temp = []
        for b in boards:
            if b.has_won() == False: # board hasnt won
                temp.append(b)
        boards = temp 

    if len(boards) == 1 and boards[0].has_won():
        print(f'Answer is {boards[0].score(num)}')
        break




    
