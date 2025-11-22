# Advent of code Year 2015 Day 3 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
x=0
y=0
visited = set()
visited.add((x, y))

for char in input:
    match char:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1
    visited.add((x, y))

print("Part One : "+ str(len(visited)))

# Part 2

x=[0,0]
y=[0,0]
visited = set()
visited.add((0,0))

for i, char in enumerate(input):
    parity = i%2
    match char:
        case '^':
            y[parity] += 1
        case 'v':
            y[parity] -= 1
        case '>':
            x[parity] += 1
        case '<':
            x[parity] -= 1
    visited.add((x[parity], y[parity]))

print("Part Two : "+ str(len(visited)))