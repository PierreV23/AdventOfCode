import itertools
import functools

with open("inputs/day06/input.txt") as file:
    text = file.read().strip("\n")

*lines, ops = text.split("\n")
ops = ops.replace(" ", "")
width = len(max(lines, key=len))
lines = [line.ljust(width) for line in lines]
t = ["".join(number).strip() or "," for number in zip(*lines)]

cols = [
    list(map(int, group))
    for key, group in itertools.groupby(t, ",".__eq__)
    if not key
]

ans = sum(
    functools.reduce(int.__mul__ if op == "*" else int.__add__, col)
    for op, col in zip(ops, cols)
)

print(ans)
