from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day4_input.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

c = 0
# day_input = ['49-51,51-51']
for line in day_input:
    m1, m2 = line.split(",")
    a, b = sorted([*map(int, m1.split('-'))])
    x, y = sorted([*map(int, m2.split('-'))])
    g = set(range(a, b+1))
    h = set(range(x, y+1))
    # if (a <= x and y <= b) or (x <= a and b <= y):
    # if ((x in g) and (y in g)) or ((a in h) and (b in h)):
    # ^ part 1
    if g & h:
        c += 1
print(c)
