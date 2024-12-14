#!/usr/bin/env python3
import sys
from math import log10


with open(sys.argv[1], 'r') as file:
    inp = [[int(c) for c in l.split()] for line in file if (l:=line.strip())][0]

PRV, VAL, NXT = 0, 1, 2

ll = [[None, v, None] for v in inp]
ll[0][NXT] = ll[1]
ll[-1][PRV] = ll[-2]
for idx in range(1, len(ll)-1):
    ll[idx][PRV] = ll[idx-1]
    ll[idx][NXT] = ll[idx+1]

def f(ll):
    startnode = ll[0]
    while startnode[PRV]:
        startnode = startnode[PRV]
    node = startnode
    values = []
    while node:
        values.append(node[VAL])
        node = node[NXT]
    return values

# print(ll)
begin_node = ll[0]
for _ in range(25):
    while begin_node[PRV]:
        begin_node = begin_node[PRV]
    node = begin_node
    while node:
        
        if node[VAL] == 0:
            node[VAL] = 1
        elif (numlength := int(log10(node[VAL])) + 1) % 2 == 1:
            node[VAL] *= 2024
        elif numlength % 2 == 0:
            left = int(node[VAL] // 10**(numlength / 2))
            right = int(node[VAL] - left * 10**(numlength / 2))
            new_node = [node[PRV], left, node]
            if node[PRV]:
                node[PRV][NXT] = new_node
            node[PRV] = new_node
            node[VAL] = right
            ll.append(new_node)

        node = node[NXT]

    # print(f(ll))

print(len(ll))