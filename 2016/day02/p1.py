#!/usr/bin/env python3
from collections import Counter
import sys


with open(sys.argv[1], 'r') as file:
    lines = [[c for c in l] for line in file if (l:=line.strip())]

code = ""
y, x = 1, 1
for line in lines:
    for c in line:
        if c in "UD":
            y = max(0, min(y+{'U': -1, 'D': 1}[c], 2))
        elif c in "LR":
            x = max(0, min(x+{'L': -1, 'R': 1}[c], 2))
    code += f"{y*3 + x + 1}"

print(code)