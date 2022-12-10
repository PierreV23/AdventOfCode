
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day10_input.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()


x_register = 1
cycle = 0
signal_strength = 0

def tick_once():
    global cycle, signal_strength
    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        signal_strength += cycle * x_register

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

print(signal_strength)