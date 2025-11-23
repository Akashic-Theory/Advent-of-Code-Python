# Advent of code Year 2015 Day 5 solution
# Author = Akasha Mohan
import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
nice = 0
for line in input.splitlines():
    if re.search(r"([aeiou].*){3,}", line) is None:
        continue
    if re.search(r"(?P<a>.)(?P=a)", line) is None:
        continue
    if re.search(r"(ab)|(cd)|(pq)|(xy)", line) is None:
        nice += 1
print("Part One : "+ str(nice))

# Part 2
nice = 0
for line in input.splitlines():
    if re.search(r"(?P<a>..).*(?P=a)", line) is None:
        continue
    if re.search(r"(?P<a>.).(?P=a)", line) is None:
        continue
    nice += 1

print("Part Two : "+ str(nice))