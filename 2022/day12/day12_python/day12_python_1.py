from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from pprint import pprint
from typing import Self

CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day12_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
# day_input = day_input_file.readlines()
day_input = day_input_file.read()

#grid[y][x]
grid = [i.strip() for i in day_input.split("\n") if i.strip()]

WIDTH = len(grid[0])
HEIGHT = len(grid)
starting_point = day_input.index("S") // WIDTH, day_input.index("S") % (WIDTH + 1)
end_point = day_input.index("E") // WIDTH, day_input.index("E") % (WIDTH + 1)

if grid[starting_point[0]][starting_point[1]] != 'S':
    raise Exception()

if grid[end_point[0]][end_point[1]] != 'E':
    raise Exception()
grid = [i.strip().replace("S", 'a').replace("E", 'z') for i in day_input.split("\n")]
grid = [i for i in grid if i]

pprint(grid)


# {pos: graph}
graphs = {}

@dataclass
class Pos:
    x: int
    y: int

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()


class Graph:
    _pool = {}
    pos: Pos
    heads: list[Graph]
    tails: list[Graph]
    def __new__(cls: type[Self], pos: Pos) -> Self:
        if pos in cls._pool:
            raise Exception("Already exists")
            return cls._pool[pos]
        new = super().__new__(cls)
        cls._pool[pos] = new
        return new

Graph(Pos(y=starting_point[0], x=starting_point[1]))

distances = {}
y=starting_point[0]
x=starting_point[1]
queue: list[tuple[int, tuple[int, int]]] = [(0, starting_point)]
while queue:
    dist, coords = queue.pop(0)
    if coords in distances:
        distances[coords] = min(dist, distances[coords])
        continue
    else:
        distances[coords] = dist

    y, x = coords
    for a, b in ((x+1,y), (x-1, y), (x, y+1), (x, y-1)):
        if a >= WIDTH or a < 0 or b < 0 or b >= HEIGHT:
            continue
        try:
            if ord(grid[b][a]) - ord(grid[y][x]) > 1:
                continue
            queue.append((dist+1, (b, a)))
        except:
            print(HEIGHT, WIDTH, b, a, len(grid[b]))
            raise Exception()

print(distances[end_point])