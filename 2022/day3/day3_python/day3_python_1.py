
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day3_input.txt')
day_input = day_input_file.readlines()
# lines = day_input_file.readlines()
# day_input = [lines[i] for i in range(0, len(lines)-1, 3)]
# day_input = day_input_file.read()

priorities = 0
for line in day_input:
    left, right = line[:len(line)//2], line[len(line)//2:]
    s = set(left).intersection(set(right))
    if len(s) > 1: print(" UH OH! ", s)
    m = [*s][0]
    if m.islower():
        priorities += ord(m) - 96
    else:
        priorities += ord(m) - 38
print(priorities)