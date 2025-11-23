# Advent of code Year 2015 Day 1 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1

print("Part One : "+ str(input.count('(') - input.count(')')))

# Part 2

floor = 0
for i, c in enumerate(input):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    if floor < 0:
        step = i + 1
        break

print("Part Two : "+ str(step))