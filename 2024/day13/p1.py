#!/usr/bin/env python3
import sys
import re

with open(sys.argv[1], 'r') as file:
    machines = []
    for machine in file.read().strip().split('\n\n'):
        a, b, prize = (tuple(map(int, m)) for m in re.findall(r"X.(\d+)..Y.(\d+)", machine))
        # mach = a, b, prize
        C = 0
        if any("p2" in a for a in sys.argv):
            C = 10000000000000
        mach = a, b, (prize[0] + C, prize[1] + C)
        machines.append(mach)

from dataclasses import dataclass

@dataclass
class Coord:
    x: int
    y: int

s = 0
for machine in machines:
    A, B, P = (Coord(*m) for m in machine)
    # A.x * a + B.x * b = P.x
    # A.y * a + B.y * b = P.y
    Bx, Px = B.x * A.y, P.x * A.y
    By, Py = B.y * A.x, P.y * A.x
    pd = Px-Py
    bd = Bx-By
    # print(pd, bd, pd / bd, pd % bd)
    if (pd % bd) == 0:
        b = pd // bd
        a1 = P.x-B.x*b
        assert a1 > 0
        # print(P.x, B.x*b, a1, a1 % A.x)
        if (a1 % A.x) == 0:
            a = a1 // A.x
            # print(a, b)
            s += a*3 + b
print(s)