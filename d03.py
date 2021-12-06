"""
Advent of Code 2021: Day 3
"""

from collections import Counter

# constants
ONE = "1"
ZERO = "0"

def binary_decoder(num: str) -> int:
    digits = list(num)
    digits = digits[::-1]
    integer = 0
    
    for i in range(len(digits)):
        if digits[i] == ONE:
            integer += 2**i
            
    return(integer)

def build_trie(data):
    trie = {}
    
    for datum in data:
        curr_trie = trie
        for pos in datum[:-1]:
            if pos not in curr_trie:
                curr_trie[pos] = {}
            curr_trie = curr_trie[pos]
            
        curr_trie[datum[-1]] = "".join([str(i) for i in datum])
        
    return(trie)
                   

def split_by_ith(data: list, i: int = 0):
    results = {0: [], 1: []}
    
    for datum in data:
        results[datum[i]].append(datum)
        
    if len(results[1]) >= len(results[0]):
        return([results[1], results[0]])
    else:
        return([results[0], results[1]])
        

def part1(data):
    half = len(data)/2
    num_length = len(data[0])
    
    gamma = ""
    epsilon = ""
    
    for i in range(num_length):
        total = sum([num[i] for num in data])
        
        if total >= half:
            gamma += "1"
            epsilon += "0"
            
        else:
            gamma +="0"
            epsilon += "1"
            
    return(binary_decoder(gamma)*binary_decoder(epsilon))

def part2(data):
    o2, co2 = split_by_ith(data, 0)
    
    i = 1
    while len(o2) > 1:
        o2 = split_by_ith(o2,i)[0]
        i += 1
      
    i = 1    
    while len(co2) > 1:
        co2 = split_by_ith(co2,i)[1]
        i += 1
        
    o2 = "".join([str(i) for i in o2[0]])
    co2 = "".join([str(i) for i in co2[0]])
    
    return(binary_decoder(o2)* binary_decoder(co2))
    


def d03(fn, data: str = "d03p1"):
    lines = open(data).readlines()
    
    ints = []
    
    for l in lines:
        l = l.strip()
        l = [int(i) for i in l]
        ints.append(l)
        
    return(fn(ints))
    