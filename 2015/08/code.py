# Advent of code Year 2015 Day 8 solution
# Author = Akasha Mohan
import codecs

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    
# Part 1
lines = [[line, eval(line)] for line in input.splitlines()]
counts = [len(a) - len(b) for a, b in lines]
print(counts)
print("Part One : "+ str(sum(counts)))

# Part 2
extras = [2 + line.count('\\') + line.count('"') for line in input.splitlines()]
print(extras)
print("Part Two : "+ str(sum(extras)))