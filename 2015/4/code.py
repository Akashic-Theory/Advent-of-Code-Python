# Advent of code Year 2015 Day 4 solution
# Author = Akasha Mohan
import hashlib

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
i=0
while True:
    if hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()[:5] == "00000":
        break
    i+=1

print("Part One : "+ str(i))

# Part 2
i=0
while True:
    if hashlib.md5((input+str(i)).encode("utf-8")).hexdigest()[:6] == "000000":
        break
    i+=1

print("Part Two : "+ str(i))