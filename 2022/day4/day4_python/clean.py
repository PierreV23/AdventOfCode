from io import TextIOWrapper

def p1(f: TextIOWrapper):
    c = 0
    day_input = f.readlines()
    for line in day_input:
        m1, m2 = line.split(",")
        a, b = map(int, m1.split('-'))
        x, y = map(int, m2.split('-'))
        g = set(range(a, b+1))
        h = set(range(x, y+1))
        g = set(g)
        h = set(h)
        if len(g & h) in (len(g), (len(h))):
            c += 1
    return c

def p2(f: TextIOWrapper):
    day_input = f.readlines()
    c = 0
    for line in day_input:
        m1, m2 = line.split(",")
        a, b = map(int, m1.split('-'))
        x, y = map(int, m2.split('-'))
        g = set(range(a, b+1))
        h = set(range(x, y+1))
        if g & h:
            c += 1
    return c



from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day4_input.txt')

print(p1(day_input_file))
day_input_file = open(CURR_DIR / 'day4_input.txt')
print(p2(day_input_file))


print(sum(map(lambda m: not not set.__and__(*map(lambda mn: (lambda a, b: set(range(a, b+1)))(*map(int, mn.split('-'))), m)), map(lambda line: line.strip().split(','), open('day4_input.txt')))))
print(sum(map(lambda m: [ls:=[*map(lambda mn: (lambda a, b: set(range(a, b+1)))(*map(int, mn.split('-'))), m)], g:=ls[0], h:=ls[1], len(g&h) in (len(g), len(h))][-1], map(lambda line: line.strip().split(','), open('day4_input.txt')))))