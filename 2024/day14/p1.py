#!/usr/bin/env python3
from collections import defaultdict
from pprint import pprint
import sys
import re


with open(sys.argv[1], 'r') as file:
    robots = [
        [
            int(n)
            for n in m
        ]
        for m in re.findall(r"p=(\d+),(\d+).v=(-?\d+),(-?\d+)", file.read())
    ]
    print(robots)

if any("test" in a for a in sys.argv):
    HEIGHT = 7
    WIDTH = 11
else:
    HEIGHT = 103
    WIDTH = 101

SEC = 100
HL = HEIGHT // 2
WL = WIDTH // 2
posses = defaultdict(list)
LU = RU = RD = LD = 0
for rob in robots:
    x, y, dx, dy = rob
    nx = (x + dx*SEC) % WIDTH
    ny = (y + dy*SEC) % HEIGHT
    # posses[nx, ny].append(rob)
    LU += (nx < WL) and (ny < HL)
    RU += (WL < nx) and (ny < HL)
    LD += (nx < WL) and (HL < ny)
    RD += (WL < nx) and (HL < ny)


# pprint(posses)
print(LU, RU, RD, LD)
print(LU * RU * RD * LD)


# for y in range(HEIGHT):
#     print(
#         ''.join(
#             ' ' if (y==HL or x==WL) else (f"{len(posses[x, y])}" if (x, y) in posses else '.')
#             for x in range(WIDTH)
#         )
#     )