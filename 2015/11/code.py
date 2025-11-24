# Advent of code Year 2015 Day 11 solution
# Author = Akasha Mohan
import re

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

# Part 1
chars="abcdefghjkmnpqrstuvwxyz" # No I O or L
idx={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'j':8,'k':9,'m':10,'n':11,'p':12,'q':13,'r':14,'s':15,'t':16,'u':17,'v':18,'w':19,'x':20,'y':21,'z':22}
pwd = input
def next_inc(password:str):
    badIndex=[6,7,8,9,10,11]
    i=-3
    j=0
    while True:
        curidx = idx[password[i]] + j
        if curidx in badIndex:
            j+=1
            continue
        if (curidx < len(chars) - 2                                         # This isnt one of last 2 letters
                and (j > 0 or (idx[password[i+1]] <= curidx                 # and following letter can become next in seq
                    or (idx[password[i+1]] == curidx + 1                    # OR following letter is already next in seq
                        and idx[password[i+2]] <= idx[password[i+1]])))):   # and 3rd letter can become the last in seq
            return password[:i] + chars[curidx:curidx+3] + chars[0] * (-3 - i)
        if curidx < len(chars) - 2:
            j+=1
            continue
        if i < -3 and idx[password[i-1]] < len(idx) - 1:
            return password[:i-1] + chars[idx[password[i-1]] + 1] + 'a' * (- 3 - i) + 'abc'
        i -= 1
        j = 0
def next_pair(password:str):
    end = chars[0]*2
    while True:
        if re.search(r"(?P<a>.)(?P=a)",password[:-2]) is not None and idx[password[-1]] < idx[password[-2]]:
            return password[:-2] + password[-2] * 2
        if re.search(r"(?P<a>.)(?P=a)",password[:-3]) is not None:
            return password[:-3] + chars[idx[password[-3]]+1] + end
        if idx[password[-3]] < idx[password[-4]]:
            return password[:-4] + password[-4]*2 + end
        if password[-4] != chars[-1]:
            return password[:-4] + chars[idx[password[-4]] + 1]*2 + end
        else:
            return password[:-5] + chars[idx[password[-5]]+1] + end * 2

valid_subs = [chars[i:i+3] for i in list(range(6)) + list(range(12,21))]
while True:
    if len([sub for sub in valid_subs if sub in pwd]) == 0:
        pwd = next_inc(pwd)
        continue
    elif len(re.findall(r"(?P<a>.)(?P=a)", pwd)) < 2:
        pwd = next_pair(pwd)
        continue
    break

print("Part One : "+ str(pwd))

# Part 2
pwd = next_inc(pwd)
while True:
    if len([sub for sub in valid_subs if sub in pwd]) == 0:
        pwd = next_inc(pwd)
        continue
    elif len(re.findall(r"(?P<a>.)(?P=a)", pwd)) < 2:
        pwd = next_pair(pwd)
        continue
    break

print("Part Two : "+ str(pwd))