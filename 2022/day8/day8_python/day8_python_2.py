from functools import reduce
from pathlib import Path
CURR_DIR = Path()
from pprint import pprint
day_input_file = open(CURR_DIR / 'day8_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

grid = [[int(number) for number in line.strip()] for line in day_input]
if len(grid) < 20: pprint(grid)
height = len(grid)
width = len(grid[0])
on_the_edge = lambda my, mx: (0 in (my,mx)) or (my == height - 1) or (mx == width - 1)
all_scores = []
for y in range(height):
    for x in range(width):
        if on_the_edge(y, x): # on the edge
            continue
        
        self = grid[y][x]
        scores = []

        # up
        local_score = 1
        for i in range(y-1, -1, -1):
            if grid[i][x] >= self or on_the_edge(i, x):
                break
            local_score += 1
        scores.append(local_score)

        # right
        local_score = 1
        for i in range(x+1, width, 1):
            if grid[y][i] >= self or on_the_edge(y, i):
                break
            local_score += 1
        scores.append(local_score)

        # left
        local_score = 1
        for i in range(x-1, -1, -1):
            if grid[y][i] >= self or on_the_edge(y, i):
                break
            local_score += 1
        scores.append(local_score)
        
        # down
        local_score = 1
        for i in range(y+1, height, 1):
            if grid[i][x] >= self or on_the_edge(i, x):
                break
            local_score += 1
        scores.append(local_score)

        all_scores.append((reduce((lambda x, y: x * y), (scores)), y, x, scores))
print(max(all_scores, key=lambda s_y_x: s_y_x[0]))
print([*filter(lambda s_y_x_sm: s_y_x_sm[1] == 3 and s_y_x_sm[2] == 2, all_scores)])
