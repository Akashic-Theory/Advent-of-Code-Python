# Advent of code Year 2015 Day 2 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
dims = [line.split('x') for line in input.splitlines()]
sides = [(int(a),int(b),int(c)) for a,b,c in dims]
areas = [(a*b, b*c, a*c) for a, b, c in sides]
area = [sum(area)*2 + min(area) for area in areas]


print("Part One : "+ str(sum(area)))
ribbons = [(a+b+c-max(a,b,c))*2 + a*b*c for a,b,c in sides]

print("Part Two : "+ str(sum(ribbons)))