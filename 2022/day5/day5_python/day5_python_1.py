from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day5_input.txt')
# day_input = day_input_file.readlines()
day_input = day_input_file.read()
from string import ascii_uppercase
from pprint import pprint

stacks, movesets = day_input.split("\n\n")
stacks = stacks.split("\n")[:-1]
pprint(stacks)
stacks_i = [[] for _ in range(9)]
for x in range(9):
    for y in range(8):
        y = 7 - y
        try:
            char = stacks[y][4*(x)+1]
        except:
            print(y, x)
            raise Exception()
        if char in ascii_uppercase:
            print(char)
            stacks_i[x].append(char)
pprint(stacks_i)
# pprint(movesets)
print(movesets.split("\n")[0])
print(movesets.split("\n")[-1])
for idx, line in enumerate(movesets.split("\n")):
    # print(line)
    line = line.strip("\n")
    
    try:
        _, a, _, s, _, t = line.split(" ")
    except:
        print(line, line.split(" "), idx)
        raise Exception()
    for _ in range(int(a)):
        if stacks_i[int(s)-1]:
            stacks_i[int(t)-1].append( stacks_i[int(s)-1].pop(-1) )

print("".join(i[-1] if i else '' for i in stacks_i))