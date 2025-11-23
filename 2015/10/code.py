# Advent of code Year 2015 Day 10 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1


for i in range(40):
    count = 0
    active = None
    out=""
    for char in input:
        if char == active or active is None:
            count += 1
        else:
            out += str(count) + active
            active = char
            count = 1
        if active is None:
            active = char
    input = out + str(count) + active
    print(f"\r{'#'*(i+1) + '.'*(39-i)}", end="", flush=True)
print("\nPart One : "+ str(len(input)))

# Part 2

for i in range(10):
    progress = 0
    count = 0
    active = None
    out=""
    l=len(input)
    for char in input:
        if char == active or active is None:
            count += 1
        else:
            out += str(count) + active
            active = char
            progress += count
            count = 1
        if active is None:
            active = char
        print(f"\r{'#' * (i + 1) + '.' * (9 - i)}  ({progress}/{l})", end="", flush=True)
    input = out + str(count) + active


print("\nPart Two : "+ str(len(input)))