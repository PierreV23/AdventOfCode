from copy import copy
import numpy as np
from pathlib import Path
CURR_DIR = Path()

filename = 'day15_input.txt'
# filename = 'day15_test.txt'
file = open(CURR_DIR / filename)
lines = open(CURR_DIR / filename).readlines()
whole = open(CURR_DIR / filename).read()
chunks = whole.split("\n\n")

def print_grid(g, join = True, join_c = ""):
    for li, r in enumerate(g):
        print(f'{li:02} {join_c.join(r) if join else r}')

def replace_2d(ls, d):
    return [[n if (n:= d.get(s)) else s for s in t] for t in ls]


def p1_0():
    beacons = set()
    sensors = set()
    s_b = {}
    b_s = {}
    for l, m, r in (line.split(", ") for line in lines):
        m = m.split("=")
        sx = l.split("=")[-1]
        sy = m[1].split(":")[0]
        bx = m[-1]
        by = r.strip().split("=")[-1]
        # print("||".join((sx, sy, bx, by)))
        sx, sy, bx, by = map(int, (sx, sy, bx, by))
        sensor = sx, sy
        beacon = bx, by
        sensors.add(sensor)
        beacons.add(beacon)
        s_b[sensor] = beacon
        if beacon not in b_s:
            b_s[beacon] = []
        b_s[beacon].append(sensor)
    key_x = lambda x_y: x_y[0]
    key_y = lambda x_y: x_y[1]
    bs = beacons | sensors
    # print(bs)
    min_x = min(bs, key=key_x)[0]
    max_x = max(bs, key=key_x)[0]
    min_y = min(bs, key=key_y)[1]
    max_y = max(bs, key=key_y)[1]
    print(min_x, max_x, min_y, max_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    real = lambda x, y: (x + min_x, y + min_y)
    fake = lambda x, y: (x - min_x, y - min_y)
    f = lambda x, y :(1 if real(x, y) in sensors else 2) if real(x, y) in bs else 0
    grid = [[f(x, y) for x in range(width)] for y in range(height)]
    print_grid(replace_2d(grid, {0:'.', 1:'S', 2:'B'}))
    print()
    c = set()
    # ts = (25, 7)
    # tb = ts[0]-1, ts[1]
    # sensors.add(ts)
    # s_b[ts] = tb
    # bs.add(ts)
    # bs.add(tb)
    # for m in range(-2, max_y + 1, 1):
    for m in range(min_y, max_y + 1, 1):
        covered = set()
        for sensor in sensors:
            beacon = s_b[sensor]
            # sensor = [sensor[0], sensor[1]]
            # beacon = [beacon[0], beacon[1]]
            beacon = np.array(beacon)
            sensor = np.array(sensor)
            sx, sy = sensor
            bx, by = beacon
            # sy -= 1
            if fake(sx, sy)[1] == m:
                covered.add(sx)
            if fake(bx, by)[1] == m:
                covered.add(bx)
            dx, dy =  sensor - beacon
            # l = dx + dy
            l = abs(dx) + abs(dy)
            dsy = abs(m - (sy))
            if dsy <= l:
                # print(sensor, beacon, l,)
                for x in range(sx - (l - dsy), sx + (l - dsy) + 1, 1):
                    # if [sx, sy] == [8, 7]:
                        covered.add(x) # beacons shouldnt be counted
        for beacon in beacons:
            x, y = beacon
            if y == m and x in covered:
                covered.remove(x)
        print(f'{m:02} '+"".join(({1: 'S', 2:'B'}[f(n-min_x, m)] if f(n-min_x, m) in (1,2) else ('#' if n in covered else '.')) for n in range(min_x, max_x+1, 1)))
        # print(f'{m:02} '+"".join(('#' if n in covered else '.') for n in range(min_x, max_x+1, 1)))
        if m == 7:
            c = copy(covered)
    print()
    
    print(covered)
    print(c, len(c))
    return len(c)
    ...


def p1():
    beacons = set()
    sensors = set()
    s_b = {}
    b_s = {}
    for l, m, r in (line.split(", ") for line in lines):
        m = m.split("=")
        sx = l.split("=")[-1]
        sy = m[1].split(":")[0]
        bx = m[-1]
        by = r.strip().split("=")[-1]
        # print("||".join((sx, sy, bx, by)))
        sx, sy, bx, by = map(int, (sx, sy, bx, by))
        sensor = sx, sy
        beacon = bx, by
        sensors.add(sensor)
        beacons.add(beacon)
        s_b[sensor] = beacon
        if beacon not in b_s:
            b_s[beacon] = []
        b_s[beacon].append(sensor)
    key_x = lambda x_y: x_y[0]
    key_y = lambda x_y: x_y[1]
    bs = beacons | sensors
    # print(bs)
    min_x = min(bs, key=key_x)[0]
    max_x = max(bs, key=key_x)[0]
    min_y = min(bs, key=key_y)[1]
    max_y = max(bs, key=key_y)[1]
    print(min_x, max_x, min_y, max_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    real = lambda x, y: (x + min_x, y + min_y)
    fake = lambda x, y: (x - min_x, y - min_y)
    f = lambda x, y :(1 if real(x, y) in sensors else 2) if real(x, y) in bs else 0
    # grid = [[f(x, y) for x in range(width)] for y in range(height)]
    # print("GRID MADE")
    # print_grid(replace_2d(grid, {0:'.', 1:'S', 2:'B'}))
    print()
    
    covered = set()
    H = 10
    # H = 2_000_000
    print("GOING THROUGH SENSORS")
    for sensor in sensors:
        beacon = s_b[sensor]
        sensor = np.array(sensor)
        beacon = np.array(beacon)
        sx, sy = sensor
        bx, by = beacon
        if sy == H:
            covered.add(sx)
        dx, dy =  sensor - beacon
        l = abs(dx) + abs(dy)
        dsy = abs(H - (sy))
        if dsy <= l:
            for x in range(sx - (l - dsy), sx + (l - dsy) + 1, 1):
                covered.add(x)
    print("GOING THROUGH BEACONS")
    for beacon in beacons:
        x, y = beacon
        if y == H and x in covered:
            covered.remove(x)
    # print(sorted(covered), len(covered))
    return len(covered)

file = open(CURR_DIR / filename)

def sp():
    beacons = set()
    sensors = set()
    s_b = {}
    b_s = {}
    for l, m, r in (line.split(", ") for line in lines):
        m = m.split("=")
        sx = l.split("=")[-1]
        sy = m[1].split(":")[0]
        bx = m[-1]
        by = r.strip().split("=")[-1]
        # print("||".join((sx, sy, bx, by)))
        sx, sy, bx, by = map(int, (sx, sy, bx, by))
        sensor = sx, sy
        beacon = bx, by
        sensors.add(sensor)
        beacons.add(beacon)
        s_b[sensor] = beacon
        if beacon not in b_s:
            b_s[beacon] = []
        b_s[beacon].append(sensor)
    key_x = lambda x_y: x_y[0]
    key_y = lambda x_y: x_y[1]
    bs = beacons | sensors
    # print(bs)
    min_x = min(bs, key=key_x)[0]
    max_x = max(bs, key=key_x)[0]
    min_y = min(bs, key=key_y)[1]
    max_y = max(bs, key=key_y)[1]
    print(min_x, max_x, min_y, max_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    real = lambda x, y: (x + min_x, y + min_y)
    fake = lambda x, y: (x - min_x, y - min_y)
    f = lambda x, y :(1 if real(x, y) in sensors else 2) if real(x, y) in bs else 0
    # grid = [[f(x, y) for x in range(width)] for y in range(height)]
    # print("GRID MADE")
    # print_grid(replace_2d(grid, {0:'.', 1:'S', 2:'B'}))
    print()
    return sensors, s_b


"""
het punt moet net buiten een sensors bereik liggen, op het "oppervlak" ervan dus.
dus ik kan door elke sensoor gaan en dan elk punt op het "oppervlak" van het beriek checken of hij niet "bezet" is ('#')


functie die coordinaten van het oppervlak extract
    Het is handig als deze allemaal in één set worden gedaan

"""
def afstand(a, b):
    x1, y1 = a
    x2, y2 = b
    return x1-x2, y1-y2

def abs_d(m):
    a, b = m
    return abs(a), abs(b)

def abs_afstand(a, b):
    return sum(abs_d(afstand(a, b)))


def oppervlakte_coords(afstanden):
    print("SEARCHING COORDS")
    # MI, MA = 0, 20
    MI, MA = 0, 4_000_000
    coords = set()
    for sensor, afstand in afstanden.items():
        sx, sy = sensor
        if sensor != (8, 7):
            # continue
            ...
        print(afstand, len(coords))
        # coords.add((sx, sy+afstand))
        # coords.add((sx, sy-afstand))
        # top, bot = -afstand+1+sy, afstand+sy
        valid = lambda x, y: (MI <= x <= MA) and (MI <= y <= MA)
        for dy in range(1-afstand, afstand+1, 1):
        # for ny in range(max(top, MI), min(bot, MA), 1):
            # if abs(dy) % afstand == 0 and dy != 0:
            if abs(dy) - afstand == 0:
                n = (sx, sy+afstand)
                if valid(*n):
                    coords.add(n)
                n = (sx, sy-afstand)
                if valid(*n):
                    coords.add(n)
            else:
                inv = afstand - abs(dy)
                ny = dy + sy
                nx = sx - inv
                n = (nx, ny)
                if valid(*n):
                    coords.add(n)
                nx = sx + inv
                n = (nx, ny)
                if valid(*n):
                    coords.add(n)
    print("DONE SEARCHING COORDS")
    return coords


def p2():
    sensors, s_b = sp()
    afstanden = {sensor:sum(abs(np.array(sensor) - np.array(s_b[sensor])))+1 for sensor in sensors}
    # layers = {}
    # mi, ma = 0, 20
    # mi, ma = 0, 4_000_000
    # rang = range(mi, ma + 1, 1)
    # for sensor in sensors:
    #     beacon = s_b[sensor]
    #     sx, sy = sensor
    #     dx, dy = np.array(sensor) - np.array(beacon)
    #     l = abs(dx) + abs(dy)
    #     for H in range(max(-l, mi), min(l+1, ma), 1):
    #         H += sy
    #         dsy = abs(H - (sy))
    #         if not dsy <= l:
    #             raise Exception()
    #         for x in range(max(sx - (l - dsy), mi), min(sx + (l - dsy) + 1, ma), 1):
    #             if H not in layers:
    #                 layers[H] = set()
    #             layers[H].add(x)
    # print(sorted(set((y, len(v), print(y, v)) for y,v in layers.items())))
    bs = sensors | set(s_b.values())
    c = oppervlakte_coords(afstanden)
    # print(f"   {''.join(str(_%10) for _ in range(21))}")
    # for y in range(-3, 21, 1):
    #     # print(f'{y:02}'+"".join(('#' if (x,y) in c else '.') for x in range(21)))
    #     f = lambda x, y :(1 if (x, y) in sensors else 2) if (x, y) in bs else 0
    #     print(f'{y:02} '+"".join(({1: 'S', 2:'B'}[f(x, y)] if f(x, y) in (1,2) else ('#' if (x, y) in c else '.')) for x in range(21)))
    print("Going through coords")
    i = 0
    while c:
        coord = c.pop()
        i += 1
        if not i%1_000_000:
            print(f"reached {i} coords")
        if all(abs_afstand(coord, sensor) >= afstand for sensor, afstand in afstanden.items()):
            print(coord)


# p1_0()
# print(p1())


print(p2())
