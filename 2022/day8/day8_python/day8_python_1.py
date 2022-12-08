from pathlib import Path
CURR_DIR = Path()
from pprint import pprint
day_input_file = open(CURR_DIR / 'day8_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()

grid = [[int(number) for number in line.strip()] for line in day_input]
if len(grid) < 20: pprint(grid)
height = len(grid)
width = len(grid[0])
edge = height*2 + (width-2) * 2
def f(transformer):
    unique = set()
    for y in range(height):
        ma = -1
        temp = []
        for x in range(width):
            a, b = transformer(y, x)
            temp.append(grid[a][b])
            if grid[a][b] > ma:
                ma = grid[a][b]
                unique.add((height+a if a < 0 else a, width+b if b < 0 else b))
    return unique

def left_right(y, x):
    return y, x

def top_down(y, x):
    return x, y

def right_left(y, x):
    return y, -x - 1

def down_top(y, x):
    return -x - 1, y

t = set()
for func in (left_right, top_down, right_left, down_top):
    t.update(f(func))

print(len(t))