#!/usr/bin/env python3
from itertools import product
import sys


with open(sys.argv[1], 'r') as file:
    lines = [l for line in file if (l:=line.strip())]

HEIGHT = len(lines)
WIDTH = len(lines[0])

antennas = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            antennas.setdefault(c, []).append((y, x))

# print(antennas)

antinodes = {}
for freq in antennas:
    antinodes[freq] = set()
    coords = antennas[freq]
    for lc, rc in product(coords, coords):
        if lc == rc: continue
        dy, dx = rc[0] - lc[0] , rc[1] - lc[1] 
        anti = lc[0] - dy, lc[1] - dx
        if (0 <= anti[0] < HEIGHT) and (0 <= anti[1] < HEIGHT):
            antinodes[freq].add(anti)

# print(antinodes)
a = set()
for v in antinodes.values():
    a |= set(v)

print(len(a))