# Advent of code Year 2015 Day 7 solution
# Author = Akasha Mohan

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
resolved = {}
pending = {}
blockers = {}
process = []

def progress():
    r = len(resolved)//17
    b = len(blockers)//17
    p = len(process)
    print(f"\rWaiting:{'#'*b + '.'*(17-b)}({len(blockers)}) Ready:{'#'*p + '.'*(10-p)}({len(process)}) Done:{'#'*r + '.'*(17-r)}({len(resolved)})", end='', flush=True)

def tokenize(x):
    match x:
        case s1, operation, s2:
            return (operation, [s1, s2])
        case "NOT", source:
            return ("NOT", [source])
        case raw:
            return ("DIRECT", raw)

def resolve(x):
    if x.isnumeric():
        return int(x)
    else:
        return resolved[x]

lines = [line.split(" -> ") for line in input.splitlines()]
connections = [(wire, tokenize(source.split())) for source, wire in lines]
for wire, op in connections:
    if op[0] == "DIRECT" and op[1][0].isnumeric():
        process.append((wire, op))
    else:
        pending[wire] = ([source for source in op[1] if source.isalpha()], op)
        for blocker in op[1]:
            if blocker.isalpha():
                blockers.setdefault(blocker, []).append(wire)
print("Processing...")
progress()
while len(process) > 0:
    wire, op = process.pop()
    # print(f"\nProcessing {wire} -> {op}")
    op, source = op
    source = [resolve(s) for s in source]
    match op:
        case "DIRECT":
            resolved[wire] = source[0]
        case "NOT":
            resolved[wire] = ~source[0]
        case "RSHIFT":
            resolved[wire] = source[0] >> source[1]
        case "LSHIFT":
            resolved[wire] = source[0] << source[1]
        case "OR":
            resolved[wire] = source[0] | source[1]
        case "AND":
            resolved[wire] = source[0] & source[1]
        case operation:
            raise NotImplementedError(operation)
    # print(blockers[wire])
    if wire in blockers:
        for unblocked in blockers[wire]:
            pending[unblocked][0].remove(wire)
            # print(f"Removing {wire} from {unblocked}. Remaining blockers: {pending[unblocked][0]}")
            if len(pending[unblocked][0]) == 0:
                process.append((unblocked, pending.pop(unblocked)[1]))
        blockers.pop(wire)
    progress()


print("\nPart One : "+ str(resolved['a']))

# Part 2
answer_p1 = resolved['a']
resolved = {}
pending = {}
blockers = {}
process = []

for wire, op in connections:
    if op[0] == "DIRECT" and op[1][0].isnumeric():
        if wire == 'b':
            process.append(('b', ('DIRECT', [str(answer_p1)])))
        else:
            process.append((wire, op))
    else:
        pending[wire] = ([source for source in op[1] if source.isalpha()], op)
        for blocker in op[1]:
            if blocker.isalpha():
                blockers.setdefault(blocker, []).append(wire)
print(process)
print("Processing...")
progress()
while len(process) > 0:
    wire, op = process.pop()
    # print(f"\nProcessing {wire} -> {op}")
    op, source = op
    source = [resolve(s) for s in source]
    match op:
        case "DIRECT":
            resolved[wire] = source[0]
        case "NOT":
            resolved[wire] = ~source[0]
        case "RSHIFT":
            resolved[wire] = source[0] >> source[1]
        case "LSHIFT":
            resolved[wire] = source[0] << source[1]
        case "OR":
            resolved[wire] = source[0] | source[1]
        case "AND":
            resolved[wire] = source[0] & source[1]
        case operation:
            raise NotImplementedError(operation)
    # print(blockers[wire])
    if wire in blockers:
        for unblocked in blockers[wire]:
            pending[unblocked][0].remove(wire)
            # print(f"Removing {wire} from {unblocked}. Remaining blockers: {pending[unblocked][0]}")
            if len(pending[unblocked][0]) == 0:
                process.append((unblocked, pending.pop(unblocked)[1]))
        blockers.pop(wire)
    progress()

print("Part Two : "+ str(resolved['a']))