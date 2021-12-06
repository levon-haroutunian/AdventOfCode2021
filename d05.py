"""
Advent of Code 2021: Day 5
"""
import re
from collections import Counter

# regex patterns
re_coords = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

class Vent:
    def __init__(self, coords: str):
        self.x1, self.y1, self.x2, self.y2 = [
            int(n) for n in re_coords.search(coords.strip()).groups()
            ]
        self.included_points = []
        
        if self.x1 == self.x2:
            self.vert = True
            
            ordered_y = sorted([self.y1, self.y2])
            for j in range(ordered_y[0], ordered_y[1]+1):
                self.included_points.append((self.x1, j))
            
        else:
            self.vert = False
            
        if self.y1 == self.y2:
            self.horiz = True
            
            ordered_x = sorted([self.x1, self.x2])
            for i in range(ordered_x[0], ordered_x[1]+1):
                self.included_points.append((i,self.y1))
            
        else:
            self.horiz = False
            
        if not self.vert and not self.horiz:
            x_ordered = list(range(self.x1, self.x2+1))
            x_reversed = list(range(self.x2, self.x1+1))
            
            if len(x_ordered) == 0:
                x_range = x_reversed[::-1]
                
            else:
                x_range = x_ordered
            
            y_ordered = list(range(self.y1, self.y2+1))
            y_reversed = list(range(self.y2, self.y1+1))
            
            if len(y_ordered) == 0:
                y_range = y_reversed[::-1]
                
            else:
                y_range = y_ordered
                
            self.included_points.extend(zip(x_range, y_range))
        

def part1(vents):
    grid = Counter()

    for v in vents:
        if v.horiz:
            ordered = sorted([v.x1, v.x2])
            for i in range(ordered[0], ordered[1]+1):
                grid[(i, v.y1)] += 1
                
        if v.vert:
            ordered = sorted([v.y1, v.y2])
            for j in range(ordered[0], ordered[1]+1):
                grid[(v.x1, j)] += 1
    return(sum([1 for i in grid.keys() if grid[i] > 1]))
                        

def part2(vents):
    grid = Counter()
    
    for v in vents:
        grid.update(v.included_points)
        
    return(sum([1 for i in grid.keys() if grid[i] > 1]))
            
def d05(fn, file: str = "d05"):
    data = open(file).readlines()
    vents = [Vent(line) for line in data]
    
    return(fn(vents))