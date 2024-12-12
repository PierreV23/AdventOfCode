#!/usr/bin/env python3
import sys
from math import log10


with open(sys.argv[1], 'r') as file:
    equations = []
    for line in file:
        if not line.strip(): continue
        l, r = line.strip().split(": ")
        res = int(l)
        vs = [int(n) for n in r.split()]
        equations.append((res, vs))


def rec(ns: list[int], res: int):
    merge = lambda a, b: a * 10**int(log10(b) + 1) + b
    if len(ns) == 2:
        a, b = ns
        if a + b == res or a * b == res or merge(a, b) == res:
            return True
    else:
        for op in (
            int.__mul__,
            int.__add__,
            merge
        ):
            ls = ns[1:]
            ls[0] = op(ns[0], ls[0])
            r = rec(ls, res)
            if r:
                return True
    return False

s = 0
for (res, ns) in equations:
    if rec(ns, res):
        s += res
        # print("possible", res, ns)
print(s)
