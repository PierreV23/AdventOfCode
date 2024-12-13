#!/usr/bin/env python3
import sys


with open(sys.argv[1], 'r') as file:
    inp = [[int(c) for c in l] for line in file if (l:=line.strip())][0]

unfragged = [-1 if (idx % 2) else idx // 2 for idx, size in enumerate(inp) for n in range(size)]

fragged = unfragged[::]
for idx, e in enumerate(fragged):
    if e == -1:
        while fragged[-1] == -1:
            fragged.pop()
        if len(fragged) == idx:
            break
        fragged[idx] = fragged.pop()

while fragged[-1] == -1:
            fragged.pop()

# print(fragged)

s = 0
for idx, n in enumerate(fragged):
    s += idx * n

print(s)

#0123456789 10
#00000000.. 10