#!/usr/bin/env python3
from functools import cmp_to_key
import sys

with open(sys.argv[1], 'r') as file:
    rules, pages = file.read().strip().split('\n\n')

rules = [[*map(int, rule.split('|'))] for rule in rules.splitlines()]
pages = [[*map(int, page.split(','))] for page in pages.splitlines()]

rules_index = {}
for l, r in rules:
    rules_index[l, r] = -1
    rules_index[r, l] = 1

p1 = p2 = 0
for page in pages:
    b = all(
        rules_index[page[idx], page[idx+1]] == -1
        for idx in range(len(page) - 1)
    )
    if b:
        p1 += page[int(len(page) / 2)]
    else:
        page.sort(
            key=cmp_to_key(lambda a, b: rules_index[a, b])
        )
        p2 += page[int(len(page) / 2)]

print(p1, p2)