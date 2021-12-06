"""
Advent of Code 2021: day 1
"""

def part1(file: str = 'd01p1'):
    input_values = [int(n) for n in open(file).readlines()]
    
    prev = input_values[0]
    counter = 0
    
    for i in range(1, len(input_values)):
        if input_values[i] > prev:
            counter += 1
            
        prev = input_values[i]
            
    return(counter)

def part2(file: str = 'd01p1'):
    vals = [int(n) for n in open(file).readlines()]
    
    # build summed windows
    windows = [vals[i] + vals[i+1] + vals[i+2] 
               for i in range(len(vals)-2)]
    
    prev = windows[0]
    counter = 0
    
    for i in range(1, len(windows)):
        if windows[i] > prev:
            counter += 1
        prev = windows[i]
        
    return(counter)