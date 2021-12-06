"""
Advent of Code 2021: Day 2
"""

# constants
FORWARD = "forward"
DOWN = "down"
UP = "up"

def part1(curr_position: list[int,int], update: str):
    direction, n = update.split()
    n = int(n)
    
    if direction == FORWARD:
        return([curr_position[0]+ n, curr_position[1]])
    elif direction == UP:
        return([curr_position[0], curr_position[1]-n])
    elif direction == DOWN:
        return([curr_position[0], curr_position[1]+n])
    
def part2(curr_postion: list[int, int], update: str):
    direction, n = update.split()
    n = int(n)
    
    if direction == FORWARD:
        return([curr_postion[0]+n, curr_postion[1]+ n*curr_postion[2], 
                curr_postion[2]])
    elif direction == UP:
        return([curr_postion[0],curr_postion[1], curr_postion[2]-n])
    elif direction == DOWN:
        return([curr_postion[0], curr_postion[1], curr_postion[2]+n])

def traverse(fn, file: str = "d02p1"):
    directions = open(file).readlines()
    
    # x, y, aim
    position = [0,0,0]
    
    for line in directions:
        position = fn(position, line)
        
    return(position[0]*position[1])
