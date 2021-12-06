"""
Advent of Code 2021: Day 4
"""

class BingoBoard:
    def __init__(self, numbers: str):
        numbers = numbers.strip()
        rows_str = numbers.split('\n')
        
        grid = [[int(n) for n in row.strip().split()] 
                for row in rows_str]
        self.row_totals = {i:0 for i in range(len(grid[0]))}
        self.col_totals = {i:0 for i in range(len(grid))}
        
        self.bingo = len(grid)
        self.unmarked = {grid[i][j]:(i,j) for i in range(len(grid))
                    for j in range(len(grid[0]))}
        
    def check_bingo(self, num: int):
        win = False
        if num in self.unmarked:
            row, col = self.unmarked[num]
            del self.unmarked[num]
            
            self.row_totals[row] += 1
            self.col_totals[col] += 1
            
            if self.row_totals[row] == self.bingo:
                win = True
                
            if self.col_totals[col] == self.bingo:
                win = True
                
        return(win)

def part1(call_numbers, bingo_boards):
    bingo = False
    winner = None
    i = 0
    
    while not bingo:
        for b in bingo_boards:
            check = b.check_bingo(call_numbers[i])
            
            if check:
                bingo = True
                winner = b
        
        i += 1
        
    return(sum(winner.unmarked.keys())*call_numbers[i-1])
    
def part2(call_numbers, bingo_boards):
    remaining = {i: bingo_boards[i] for i in range(len(bingo_boards))}
    i = 0
    
    while len(remaining.keys()) > 1:
        in_play = list(remaining.keys())
        for j in in_play:
            check = remaining[j].check_bingo(call_numbers[i])
            
            if check:
                del remaining[j]
                
        i += 1
        
    loser = remaining[list(remaining.keys())[0]]
    
    # find num that wins bingo for loser
    bingo = False
    while not bingo:
        bingo = loser.check_bingo(call_numbers[i])
        i += 1
    
    return(sum(loser.unmarked.keys())*call_numbers[i-1])
            

def d04(fn, file: str = "d04"):
    data = open(file).read().split("\n\n")
    
    call_numbers = [int(n) for n in data[0].strip().split(',')]
    
    bingo_boards = [BingoBoard(b) for b in data[1:]]
    
    return(fn(call_numbers, bingo_boards))
    
    