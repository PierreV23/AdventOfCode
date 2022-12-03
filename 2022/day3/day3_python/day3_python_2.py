
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day3_input.txt')
# lines = day_input_file.readlines()
# day_input = [lines[i] for i in range(0, len(lines)-1, 3)]
# day_input = day_input_file.read()

priorities = 0
for line in day_input_file:
    second = day_input_file.readline().strip()
    third = day_input_file.readline().strip()
    s = set(line).intersection(set(second)).intersection(set(third))
    if len(s) > 1: print(" UH OH! ", s)
    m = [*s][0]
    
    if m.islower():
        priorities += ord(m) - 96
    else:
        priorities += ord(m) - 38
print(priorities)