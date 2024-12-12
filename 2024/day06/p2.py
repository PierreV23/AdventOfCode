#!/usr/bin/env python3
from enum import Enum
from itertools import product
import sys
from bisect import bisect_left, bisect_right
from typing import Literal

class Dir(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

DIRS = {
    '^': Dir.UP,
    'v': Dir.DOWN,
    '<': Dir.LEFT,
    '>': Dir.RIGHT,
}
DIRSREV = {
    Dir.UP: '^',
    Dir.DOWN: 'v',
    Dir.LEFT: '<',
    Dir.RIGHT: '>',
}
Coord = tuple[int, int]
start: Coord = None # type: ignore
startdir: Dir = None # type: ignore
rowmap: dict[int, list[int]] = {}
colmap: dict[int, list[int]] = {}
blockades = set()
with open(sys.argv[1], 'r') as file:
    for y, line in enumerate(file):
        if not line: continue
        rowtemp = rowmap.setdefault(y, [])
        for x, c in enumerate(line):
            coltemp = colmap.setdefault(x, [])
            if c in '^><v':
                startdir = DIRS[c]
                start = y, x
            elif c == '#':
                coltemp.append(y)
                rowtemp.append(x)
                blockades.add((y,x))

print(start)

curr: tuple[int, int] = start # type: ignore



with open(sys.argv[1], 'r') as file:
    matrix = [
        [c for c in line.strip()]
        for line in file
        if line.strip()
    ]
WIDTH = len(matrix[0])
HEIGHT = len(matrix)
del line
del x
del y
del c
del matrix

def pr(visited, dir, curr, blockades):
    visited = set((b for _a, b in visited))
    s = \
'\n'.join(
    ''.join(
        # (("P") if ((y, x) in visited) else DIRSREV[dir]) if (y, x)==curr else ("X" if (y, x) in visited else ("#" if (y, x) in blockades else "."))
        DIRSREV[dir] if (y, x)==curr else ("X" if (y, x) in visited else ("#" if (y, x) in blockades else "."))
        for x in range(WIDTH)
    )
    for y in range(HEIGHT)
)
    print(s)



def is_loop(
    visited_w_dir: set[tuple[Dir, Coord]],
    curr: Coord,
    dir: Dir,
    *,
    on_map = True,
    deb = False
):
    while on_map:
        cy, cx = curr
        prev_dir = dir
        match dir:
            case Dir.UP:
                idx = bisect_right(colmap[cx], cy)
                on_map ^= idx == 0
                ny = (colmap[cx][idx - 1] + 1) if on_map else 0
                to_visit = ((y, cx) for y in range(cy, ny - 1, -1))
                curr = ny, cx
                dir = Dir.RIGHT
            case Dir.DOWN:
                idx = bisect_right(colmap[cx], cy)
                on_map ^= idx == len(colmap[cx])
                ny = (colmap[cx][idx] - 1) if on_map else (HEIGHT - 1)
                to_visit = ((y, cx) for y in range(cy, ny + 1))
                curr = ny, cx
                dir = Dir.LEFT
            case Dir.LEFT:
                idx = bisect_right(rowmap[cy], cx)
                on_map ^= idx == 0
                nx = (rowmap[cy][idx - 1] + 1) if on_map else 0
                to_visit = ((cy, x) for x in range(cx, nx - 1, -1))
                curr = cy, nx
                dir = Dir.UP
            case Dir.RIGHT:
                idx = bisect_right(rowmap[cy], cx)
                on_map ^= idx == len(rowmap[cy])
                nx = (rowmap[cy][idx] - 1) if on_map else (WIDTH - 1)
                to_visit = ((cy, x) for x in range(cx, nx + 1))
                curr = cy, nx
                dir = Dir.DOWN
        for coord in to_visit:
            if deb: print(prev_dir, coord, on_map)
            combi = (prev_dir, coord)
            if combi in visited_w_dir:
                return -1
            visited_w_dir |= {combi,}
            if deb: pr(visited_w_dir, prev_dir, coord, blockades)
    return len(visited_w_dir), len(set((b for _a, b in visited_w_dir)))

# import time
# starttime = time.perf_counter()

# dir = startdir
# visited: set[tuple[int, int]] = {curr,}
# on_map = True
# while on_map:
#     cy, cx = curr
#     match dir:
#         case Dir.UP:
#             idx = bisect_right(colmap[cx], cy)
#             on_map ^= idx == 0
#             ny = (colmap[cx][idx - 1] + 1) if on_map else 0
#             to_visit = ((y, cx) for y in range(ny, cy + 1))
#             curr = ny, cx
#             dir = Dir.RIGHT
#         case Dir.DOWN:
#             idx = bisect_right(colmap[cx], cy)
#             on_map ^= idx == len(colmap[cx])
#             ny = (colmap[cx][idx] - 1) if on_map else (HEIGHT - 1)
#             to_visit = ((y, cx) for y in range(cy, ny + 1))
#             curr = ny, cx
#             dir = Dir.LEFT
#         case Dir.LEFT:
#             idx = bisect_right(rowmap[cy], cx)
#             on_map ^= idx == 0
#             nx = (rowmap[cy][idx - 1] + 1) if on_map else 0
#             to_visit = ((cy, x) for x in range(nx, cx + 1))
#             curr = cy, nx
#             dir = Dir.UP
#         case Dir.RIGHT:
#             idx = bisect_right(rowmap[cy], cx)
#             on_map ^= idx == len(rowmap[cy])
#             nx = (rowmap[cy][idx] - 1) if on_map else (WIDTH - 1)
#             to_visit = ((cy, x) for x in range(cx, nx + 1))
#             curr = cy, nx
#             dir = Dir.DOWN
    
#     for coord in to_visit:
#         visited |= {coord,}
#         # pr()

# endtime = time.perf_counter()

# print(len(visited))

# elapsed_time = endtime - starttime
# print(f"Elapsed time: {elapsed_time:.6f} seconds")

# print(is_loop({(startdir, start), }, start, startdir))
by, bx = 6, 3
bidx_x = bisect_right(rowmap[by], bx)
bidx_y = bisect_right(colmap[bx], by)
print(rowmap[by], bidx_x)
print(colmap[bx], bidx_y)
rowmap[by].insert(bidx_x, bx)
colmap[bx].insert(bidx_y, by)
print(is_loop(set(), start, startdir,))
rowmap[by].pop(bidx_x)
colmap[bx].pop(bidx_y)
print(is_loop(set(), start, startdir,))

loops = set()
for by, bx in product(range(HEIGHT), range(WIDTH)):
    print(by, bx)
    if (by, bx) == start:
        continue
    if (bx in rowmap[by]) and (by in colmap[bx]):
        continue
    bidx_x = bisect_right(rowmap[by], bx)
    bidx_y = bisect_right(colmap[bx], by)
    # print(rowmap[by], bidx_x)
    # print(colmap[bx], bidx_y)
    rowmap[by].insert(bidx_x, bx)
    colmap[bx].insert(bidx_y, by)
    l = is_loop(set(), start, startdir)
    rowmap[by].pop(bidx_x)
    colmap[bx].pop(bidx_y)
    if l == -1:
        loops.add((by, bx))

print(len(loops))