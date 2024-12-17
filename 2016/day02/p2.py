#!/usr/bin/env python3
from collections import Counter
import sys


with open(sys.argv[1], 'r') as file:
    lines = [[c for c in l] for line in file if (l:=line.strip())]

NUMPAD = [
    "..1..",
    ".234.",
    "56789",
    ".ABC.",
    "..D..",
]
print(NUMPAD)
code = ""
y, x = 2, 0
for line in lines:
    for c in line:
        if c in "UD":
            ny = max(0, min(y+{'U': -1, 'D': 1}[c], 4))
            nx = x
        elif c in "LR":
            nx = max(0, min(x+{'L': -1, 'R': 1}[c], 4))
            ny = y
        if NUMPAD[ny][nx] == '.':
            ny, nx = y, x
        y, x = ny, nx
    code += NUMPAD[y][x]

print(code)