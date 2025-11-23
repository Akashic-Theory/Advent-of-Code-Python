# Advent of code Year 2015 Day 9 solution
# Author = Akasha Mohan
from itertools import permutations, pairwise

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
memo = {}
lines = [line for line in input.splitlines()]
distances = {frozenset(locations.split(" to ")):int(dist) for locations, dist in [line.split(' = ') for line in lines]}
print(distances)
locations = set((line.split()[2] for line in lines))
locations.add(lines[0].split()[0])
print(locations)
best = None
worst = None
for perm in permutations(locations):
    links = [frozenset(pair) for pair in pairwise(perm)]
    dist = sum(distances[link] for link in links)
    if best is None or dist < best[1]:
        print(f"New best! {perm, dist}")
        best = perm, dist
# Part 2
    if worst is None or dist > worst[1]:
        print(f"New worst! {perm, dist}")
        worst = perm, dist
print("Part One : "+ str(best))

print("Part Two : "+ str(worst))