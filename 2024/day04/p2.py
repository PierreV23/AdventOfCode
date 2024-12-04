#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as file:
    lines = [l for line in file if (l:=line.strip())]

width, height = len(lines[0]), len(lines)

c = 0
for y in range(1, height - 1):
    for x in range(1, width - 1):
        d1 = f"{ lines[y-1][x-1] }{ lines[y][x] }{ lines[y+1][x+1] }"
        d2 = f"{ lines[y+1][x-1] }{ lines[y][x] }{ lines[y-1][x+1] }"
        c += d1 in "SAM MAS" and d2 in "SAM MAS"

print(c)
