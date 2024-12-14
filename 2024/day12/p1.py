#!/usr/bin/env python3
from collections import defaultdict
from pprint import pprint
import sys


with open(sys.argv[1], 'r') as file:
    lines = [[c for c in l] for line in file if (l:=line.strip())]

grid = {
    (y,x): c
    for y, line in enumerate(lines)
    for x, c in enumerate(line)
}

HEIGHT = len(lines)
WIDTH = len(lines[0])
Coord = tuple[int, int]

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
ids = 0
idmap = {}
plots = {}

def get_around(coord: Coord):
    y, x = coord
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        nc = ny, nx
        yield nc

def is_inside(coord: Coord):
    y, x = coord
    return ((0 <= y < HEIGHT) and (0 <= x < WIDTH))

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        coord = y, x
        if coord in plots:
            continue
        id = max((0, *(i+1 for i in idmap)))
        idmap[id] = c
        queue_s = {coord,}
        queue = [*queue_s]
        for q in queue:
            plots[q] = id
            for nc in get_around(q):
                if nc in plots:
                    continue
                if not is_inside(nc):
                    continue
                if nc in queue_s:
                    continue
                if grid[nc] != grid[coord]:
                    continue
                queue.append(nc)
                queue_s.add(nc)
        print(queue)
        # for dy, dx in dirs:
        #     ny, nx = y + dy, x + dx
        #     if not :
        #         continue
        #     nc = ny, nx
        #     if nc in plots:
        #         oid = plots[nc]
        #         if idmap[oid] == c:
        #             plots[coord] = oid
        #             break
        # else:
        #     plots[coord] = ids
        #     idmap[ids] = c
        #     ids += 1

del line
del c

pprint(plots)
pprint(idmap)
perim = defaultdict(int)
area = defaultdict(int)
for y, line in enumerate(lines):
    for x, _c in enumerate(line):
        c = plots[y, x]
        area[c] += 1
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if not ((0 <= ny < HEIGHT) and (0 <= nx < WIDTH)):
                perim[c] += 1
            elif plots[ny, nx] != c:
                perim[c] += 1

price = 0
for plant in perim.keys():
    print(idmap[plant], perim[plant], area[plant])
    price += perim[plant] * area[plant]

print(perim, area)
print(price)