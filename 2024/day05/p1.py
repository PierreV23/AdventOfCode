#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as file:
    rules, pages = file.read().strip().split('\n\n')

rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
pages = [[*map(int, page.split(','))] for page in pages.splitlines()]

p1 = 0
for page in pages:
    b = all(
        (page[idx], page[idx+1]) in rules
        for idx in range(len(page) - 1)
    )
    if b:
        p1 += page[int(len(page) / 2)]

print(p1)