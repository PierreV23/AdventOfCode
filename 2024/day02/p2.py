#!/usr/bin/env python3
from collections import Counter
import sys


with open(sys.argv[1], 'r') as file:
    lines = [[*map(int, line.split())] for line in file if line.strip()]


s = 0
for rep in lines:
    a = False
    for idx in range(len(rep)):
        cop = rep[:]
        cop.pop(idx)
        i = [*zip(cop, cop[1:])]
        R = range(1, 4)
        inc = True
        dec = True
        for a,b in i:
            inc &= (b-a) in R
            dec &= (a-b) in R
        a = inc | dec
        if a: break
    s += a

print(s)