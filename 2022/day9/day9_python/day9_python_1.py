
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day9_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()
from numpy import array

places = set()
tail = array([0, 0])
head = array([0, 0])
places.add(tuple([int(n) for n in tail]))
print(places)
for move, steps in (line.strip().split() for line in day_input):
    steps = int(steps)
    for _ in range(steps):
        delta = tail - head
        # print("pre", head, tail)
        match move:
            case "R":
                head [0] += 1
                delta = tail - head
                if all(tail == head):
                    pass
                elif all(delta == [-2, 0]):
                    tail [0] += 1
                elif all(abs(delta) == [1, 1]):
                    pass
                elif all(abs(delta) == [2, 1]):
                    tail = head + [delta[0]/abs(delta[0]), 0]
            case "U":
                head [1] += 1
                delta = tail - head
                if all(tail == head):
                    pass
                elif all(delta == [0, -2]):
                    tail [1] += 1
                elif all(abs(delta) == [1, 1]):
                    pass
                elif all(abs(delta) == [1, 2]):
                    tail = head + [0, delta[1]/abs(delta[1])]
                    # print("new", head, tail, delta[1]/abs(delta[1]))
            case "L":
                head [0] -= 1
                delta = tail - head
                if all(tail == head):
                    pass
                elif all(delta == [2, 0]):
                    tail [0] -= 1
                elif all(abs(delta) == [1, 1]):
                    pass
                elif all(abs(delta) == [2, 1]):
                    tail = head + [delta[0]/abs(delta[0]), 0]
                
            case "D":
                head [1] -= 1
                delta = tail - head
                if all(tail == head):
                    pass
                elif all(delta == [0, 2]):
                    tail [1] -= 1
                elif all(abs(delta) == [1, 1]):
                    pass
                elif all(abs(delta) == [1, 2]):
                    tail = head + [0, delta[1]/abs(delta[1])]
        head = array([int(n) for n in head])
        tail = array([int(n) for n in tail])
        places.add(tuple(tail))
        # print(head, tail)

print(len(places))
# print(sorted([*places]))


