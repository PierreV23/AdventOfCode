#!/usr/bin/env python3
import sys


with open(sys.argv[1], 'r') as file:
    rows = [
        [('~' if c == '.' else int(c)) for c in l]
        for line in file if (l:=line.strip())
    ]

HEIGHT = len(rows)
WIDTH = len(rows[0])

starting_points = [(y, x) for y in range(HEIGHT) for x in range(WIDTH) if rows[y][x] == 0]
s = 0
# print(starting_points)
for start in starting_points:
    visited = set()
    queue = [(0, *start)]
    for v, cy, cx in queue:
        dirs = (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        )
        for dy, dx in dirs:
            oy, ox = cy + dy, cx + dx
            if not ((0 <= oy < HEIGHT) and (0 <= ox < WIDTH)):
                continue
            if (oy, ox) in visited:
                continue
            if v + 1 != rows[oy][ox]:
                continue
            n = (v + 1, oy, ox)
            queue.append(n)
            visited.add(n)
    s += sum(
        1
        for v, _, _ in visited
        if v == 9
    )


print(s)
