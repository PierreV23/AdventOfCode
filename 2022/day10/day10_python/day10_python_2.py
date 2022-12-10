
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day10_input.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()


x_register = 1
cycle = 0

def tick_once():
    global cycle
    
    if cycle % 40 in range(x_register-1, x_register+2):
        print('#', end='')
    else:
        print('.', end='')
    cycle += 1
    if cycle % 40 == 0:
        print()

def tick_x(x):
    for _ in range(x):
        tick_once()

for line in day_input:
    instruction, *data = line.rstrip('\n').split()
    match instruction:
        case 'noop':
            tick_once()
        case 'addx':
            tick_x(2)
            x_register += int(data[0])

