# Advent of code Year 2015 Day 6 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# input = "turn on 4,4 through 5,5"

def pgrid(grid):
    for i, row in enumerate(grid):
        print(["1" if x else "0" for x in row])
def separate(command_string:str):
    a,b = command_string.split('through')
    command, a = a.strip().rsplit(' ', 1)
    a = tuple((int(x)) for x in a.split(','))
    b = tuple((int(x)) for x in b.split(','))
    match command:
        case "turn off":
            command = False
        case "turn on":
            command = True
        case "toggle":
            command = None
    return command,a,b

# Part 1
commands = [separate(line) for line in input.splitlines()]
grid = [[False for _ in range(1000)] for _ in range(1000)]

for command, a, b in commands:
    # print(command, a, b)
    for i,row in enumerate(grid[a[0]:b[0]+1]):
        # print(row)
        for j,light in enumerate(row[a[1]:b[1]+1]):
            # print(f"({i}, {j}) - {light}")
            grid[i+a[0]][j+a[1]] = not light if command is None else command
lights = 0
# pgrid(grid)
for row in grid:
    for item in row:
        if item == True:
            lights += 1
print("Part One : "+ str(lights))

# Part 2
def separate2(command_string:str):
    a,b = command_string.split('through')
    command, a = a.strip().rsplit(' ', 1)
    a = tuple((int(x)) for x in a.split(','))
    b = tuple((int(x)) for x in b.split(','))
    match command:
        case "turn off":
            command = -1
        case "turn on":
            command = 1
        case "toggle":
            command = 2
    return command,a,b

commands = [separate2(line) for line in input.splitlines()]
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for command, a, b in commands:
    for i,row in enumerate(grid[a[0]:b[0]+1]):
        for j,light in enumerate(row[a[1]:b[1]+1]):
            bright = light + command
            grid[i+a[0]][j+a[1]] = 0 if bright < 0 else bright
lights = 0
for row in grid:
    for item in row:
        lights += item
print("Part Two : "+ str(lights))