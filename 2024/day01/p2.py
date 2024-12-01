#!/usr/bin/env python3
from collections import Counter
import sys


with open(sys.argv[1], 'r') as file:
    lines = [[*map(int, line.split())] for line in file if line]

cols = zip(*lines)


r1 = next(cols)
r2 = next(cols)

c = Counter(r2)

s = sum(n * c.get(n, 0) for n in r1)

print(s)