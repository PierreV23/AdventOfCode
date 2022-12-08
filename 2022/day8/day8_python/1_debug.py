from pathlib import Path
CURR_DIR = Path()
from pprint import pprint
day_input_file = open(CURR_DIR / 'day8_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

grid = [[int(number) for number in line.strip()] for line in day_input]
pprint(grid)
def f(transformer):
    edge = (len(grid) + 1) * 2 + (len(grid[0])+1-2)*2
    print(edge)
    input()
    unique = set()
    counter = 0
    for y in range(len(grid)):
        ma = -1
        temp = []
        for x in range(len(grid[y])):
            
            if (y, x) == (4, 4):
                print(123)
            a, b = transformer(y, x)
            temp.append(grid[a][b])
            if grid[a][b] > ma:
                ma = grid[a][b]
                # print(ma)
                unique.add((len(grid)+a if a < 0 else a, len(grid[0])+b if b < 0 else b))
            else:
                if (len(grid)+a if a < 0 else a, len(grid[0])+b if b < 0 else b) == (4, 4):
                    print("huh", ma, grid[a][b])
                    print(temp, transformer, y, x, a, b, transformer(a, b))
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
t.update(f(left_right))
print(sorted([*t]), len(t))
t.update(f(top_down))
print(sorted([*t]), len(t))
t.update(f(right_left))
print(sorted([*t]), len(t))
t.update(f(down_top))
print(sorted([*t]), len(t))

print(len(t))