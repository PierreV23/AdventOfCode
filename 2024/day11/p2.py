#!/usr/bin/env python3
from functools import cache
import sys
from math import log10


with open(sys.argv[1], 'r') as file:
    inp = [[int(c) for c in l.split()] for line in file if (l:=line.strip())][0]


@cache
def f(v, blinks):
    if blinks == 1:
        if v == 0:
            return 1
        return (1-((int(log10(v)) + 1) % 2)) + 1
    else:
        if v == 0:
            return f(1, blinks - 1)
        elif (numlength := int(log10(v)) + 1) % 2 == 1:
            return f(v * 2024, blinks - 1)
        elif numlength % 2 == 0:
            left = int(v // 10**(numlength / 2))
            right = int(v - left * 10**(numlength / 2))
            return f(left, blinks - 1) + f(right, blinks - 1)
    raise Exception()



blinks = 75
s = sum(
    f(v, blinks)
    for v in inp
)
print(s)