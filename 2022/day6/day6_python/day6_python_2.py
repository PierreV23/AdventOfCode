
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day6_input.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

stack = []
for idx, char in enumerate(day_input[0]):
    stack.append(char)
    if len(stack) == 14:
        if len(set(stack)) == 14:
            print(idx+1, print(stack))
            break
        else:
            stack.pop(0)