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
    for op in (
        int.__mul__,
        int.__add__,
        merge
    ):
        ls = ns[1:]
        ls[0] = op(ns[0], ls[0])
        if len(ls) == 1:
            if ls[0] == res:
                return True
            continue
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
