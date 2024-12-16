#!/usr/bin/env python3
from collections import defaultdict
from pprint import pprint
import sys

from p1 import idmap, plots, get_around, dirs

edges = {}

for coord in plots:
    for other_coord in get_around(coord):
        if plots.get(other_coord, '!') != plots[coord]:
            id = plots[coord]
            edges.setdefault(id, set()).add(other_coord)

print({k:sorted(v) for k,v in edges.items()})


for id, coords in edges.items():
    a = idmap[id]
    min_x = min(coord[1] for coord in coords)  # For x coordinates
    max_x = max(coord[1] for coord in coords)
    min_y = min(coord[0] for coord in coords)  # For y coordinates
    max_y = max(coord[0] for coord in coords)
    # print(min_x, max_x, min_y, max_y)
    # Create a grid to represent the coordinates
    for y in range(min_y, max_y + 1):  # Loop from top to bottom (max_y to min_y)
        row = ""
        for x in range(min_x, max_x + 1):  # Loop from left to right (min_x to max_x)
            # if x == -1: print((y, x), (y, x) in coords)
            if (y, x) in coords:
                row += f"{a}"  # Coordinate is present
            else:
                row += " "  # Coordinate is not present
        print(row)  # Print the row


Dir = tuple[int, int]
Coord = tuple[int, int]
edges_w: dict[int, dict[Dir, set[Coord]]] = {}
for coord in plots:
    y, x = coord
    for delta in dirs:
        dy, dx = delta
        ny, nx = y + dy, x + dx
        other_coord = ny, nx
        if plots.get(other_coord, '!') != plots[coord]:
            id = plots[coord]
            edges_w\
                .setdefault(id, {})\
                .setdefault(delta, set())\
                .add(other_coord)

print(idmap)
pprint(edges_w)

edges_c = {}

for id, d in edges_w.items():
    t = 0
    for dir in d:
        s = d[dir]
        while s:
            r = s.pop()
            t += 1
            if not s:
                continue
            dix, diy = dir
            queue = [(r, (diy, dix)), (r, (-diy, -dix))]
            for (x, y), (dx, dy) in queue:
                # print(idmap[id], queue)
                new_coord = x + dx, y + dy
                if new_coord in s:
                    s.remove(new_coord)
                    queue.append((new_coord, (dx, dy)))
    print(idmap[id], t)
    edges_c[id] = t


area = defaultdict(int)
for id in plots.values():
    area[id] += 1

s = 0
for id, edges in edges_c.items():
    a = area[id]
    s += a * edges
    print(a, edges, a*edges)

print(s)