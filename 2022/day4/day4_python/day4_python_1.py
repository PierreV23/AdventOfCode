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
    g = range(a, b+1)
    h = range(x, y+1)
    # if (a <= x and y <= b) or (x <= a and b <= y):
    # ^ still not quite sure why that didnt work, after careful examination, this is actually right.
    # ^ on my first couple of runs i was accidently running the old script of day3, which made me give a wrong output.
    # ^ that made me assume this if satement didnt work
    # i wish i had it done it like this:
    # g = set(g)
    # h = set(h)
    # if len(g & h) in (len(g), (len(h)))
    if ((x in g) and (y in g)) or ((a in h) and (b in h)):
        c += 1
print(c)
