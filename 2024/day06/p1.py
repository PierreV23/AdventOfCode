#!/usr/bin/env python3
from enum import Enum
import sys
from bisect import bisect_left, bisect_right, bisect
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
start = None
dir: Dir = None # type: ignore
rowmap = {}
colmap = {}
with open(sys.argv[1], 'r') as file:
    for y, line in enumerate(file):
        if not line: continue
        rowtemp = rowmap.setdefault(y, [])
        for x, c in enumerate(line):
            coltemp = colmap.setdefault(x, [])
            if c in '^><v':
                dir = DIRS[c]
                start = y, x
            elif c == '#':
                coltemp.append(y)
                rowtemp.append(x)

# print(rowmap)
# print(colmap)
print(start)

ranges = []
rowranges = {}
colranges = {}
curr: tuple[int, int] = start # type: ignore
on_map = True
# print(ranges)

with open(sys.argv[1], 'r') as file:
    matrix = [
        [c for c in line.strip()]
        for line in file
        if line.strip()
    ]
width = len(matrix[0])
height = len(matrix)
i = 0
while on_map:
    i += 1
    # print(curr, ranges)
    # grid = ' ' + ''.join(map(str, range(width))) + '\n' + \
    #     '\n'.join(
    #         f"{y}" + ''.join(
    #             DIRSREV[dir] if ((y, x) == curr) else ("X" if (any(x in r for r in rowranges.get(y, [])) or any(y in r for r in colranges.get(x, []))) else c)
    #             for x, c in enumerate(line)
    #         )
    #         for y, line in enumerate(matrix)
    #     )
    # with open(f"f/{i}.txt", 'w') as file:
    #     file.write(grid)
    # print(grid)
    cy, cx = curr
    match dir:
        case Dir.UP:
            idx = bisect_right(colmap[cx], cy)
            on_map ^= idx == 0
            ny = (colmap[cx][idx - 1] + 1) if on_map else 0
            ranges.append(('y', range(ny, cy + 1)))
            colranges.setdefault(cx, []).append(range(ny, cy + 1))
            curr = ny, cx
            dir = Dir.RIGHT
        case Dir.DOWN:
            idx = bisect_right(colmap[cx], cy)
            on_map ^= idx == len(colmap[cx])
            ny = (colmap[cx][idx] - 1) if on_map else (height - 1)
            ranges.append(('y', range(cy, ny + 1)))
            colranges.setdefault(cx, []).append(range(cy, ny + 1))
            curr = ny, cx
            dir = Dir.LEFT
        case Dir.LEFT:
            idx = bisect_right(rowmap[cy], cx)
            on_map ^= idx == 0
            nx = (rowmap[cy][idx - 1] + 1) if on_map else 0
            ranges.append(('x', range(nx, cx + 1)))
            rowranges.setdefault(cy, []).append(range(nx, cx + 1))
            curr = cy, nx
            dir = Dir.UP
        case Dir.RIGHT:
            idx = bisect_right(rowmap[cy], cx)
            on_map ^= idx == len(rowmap[cy])
            nx = (rowmap[cy][idx] - 1) if on_map else (width - 1)
            ranges.append(('x', range(cx, nx + 1)))
            rowranges.setdefault(cy, []).append(range(cx, nx + 1))
            curr = cy, nx
            dir = Dir.DOWN
            # if i == 2:
            #     print(rowmap[cy][idx - 1], idx, rowmap[cy])



# grid = '   ' + ''.join(str(n) for n in range(width)) + '\n' + \
#         '\n'.join(
#             f"{y:03}" + ''.join(
#                 '!' if ((y, x) == curr) else ("X" if (any(x in r for r in rowranges.get(y, [])) or any(y in r for r in colranges.get(x, []))) else c)
#                 for x, c in enumerate(line)
#             )
#             for y, line in enumerate(matrix)
#         )
# print(grid)

print(curr)

for v in rowranges.values():
    v.sort(key=lambda r: r.start)

for v in colranges.values():
    v.sort(key=lambda r: r.start)


# print(rowranges)
# print(colranges)
newrowranges = {}
newcolranges = {}

def merge(d: dict, nd: dict):
    for k in d:
        nl = nd.setdefault(k, [])
        for r in d[k]:
            if nl and r.start in nl[-1]:
                print("Extending")
                nl[-1] = range(nl[-1].start, r.stop)
            else:
                nl.append(r)

merge(rowranges, newrowranges)
merge(colranges, newcolranges)

# print(newrowranges)

s = sum(
    sum(len(r) for r in ranges)
    for ranges in newrowranges.values()
)
s+= sum(
    sum(len(r) - sum(sum(x in rowr for rowr in newrowranges.get(ty, [])) for ty in r) for r in ranges)
    for x, ranges in newcolranges.items()
)
print(s)

se = set(
    (y, x)
    for x, ranges in newcolranges.items()
    for r in ranges
    for y in r
) | set(
    (y, x)
    for y, ranges in newrowranges.items()
    for r in ranges
    for x in r
)

print(len(se))