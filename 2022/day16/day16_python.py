
from pathlib import Path
CURR_DIR = Path()

filename = 'day16_input.txt'
filename = 'test.txt'
file = open(CURR_DIR / filename)
lines = open(CURR_DIR / filename).readlines()
whole = open(CURR_DIR / filename).read()
chunks = whole.split("\n\n")
from functools import cache

@cache
def solve(a_id, minutes_passed):
    rate, valves = tunnels[a_id]
    if minutes_passed >= 30:
        print("end")
        return 0
    # s = {a_id:(30-minutes_passed-1)*rate}
    # o = {v:solve(v, minutes_passed+1) for v in valves}
    # a = o | s
    # i  =max(a.items(), key=lambda k_v: k_v[1])[0]
    # return {i: o[i]}
    s = (30-minutes_passed-1)*rate
    m = max([s] + [max(solve(v, minutes_passed+3) + s, solve(v, minutes_passed+2))   for v in valves])
    return m

def p1():
    global tunnels
    tunnels = {}
    for line in lines:
        line = line.strip()
        left, right = line.split("; ")
        _, a_id, _, _, rate = left.split(" ")
        rate = int(rate.split("=")[1])
        valves = right.split(", ")
        valves[0] = valves[0][23:] if len(valves[0]) == 25 else valves[0][22:]
        if a_id in tunnels:
            raise Exception()
        tunnels[a_id] = (rate, valves)
    return solve('AA', 1)

def p2():
    ...


print(p1())
print(p2())
