
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day9_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
# day_input_file = open(CURR_DIR / 'test_2.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()
from numpy import array
from numpy import ndarray

def make_array_int(ar: ndarray) -> ndarray:
    return array([int(n) for n in ar])


places = set()
rope = [array([0, 0]) for _ in range(10)]
places.add(tuple(rope[9]))
print(places)
total_steps = 0
for move, steps in (line.strip().split() for line in day_input):
    steps = int(steps)
    for _ in range(steps):
        total_steps += 1
        match move:
            case "R":
                rope[0] [0] += 1
            case "U":
                rope[0] [1] += 1
            case "L":
                rope[0] [0] -= 1
            case "D":
                rope[0] [1] -= 1
        
        for i in range(9):
            head = rope[i]
            tail = rope[i+1]
            delta = tail - head
            if all(tail == head):
                pass
            elif all(delta == [-2, 0]):
                tail [0] += 1
            elif all(abs(delta) == [1, 1]):
                pass
            elif all(abs(delta) == [2, 1]):
                n_tail = head + [delta[0]/abs(delta[0]), 0]
                tail[0] = n_tail[0]
                tail[1] = n_tail[1]
            \
            elif all(delta == [0, -2]):
                tail [1] += 1
            elif all(abs(delta) == [1, 2]):
                n_tail = head + [0, delta[1]/abs(delta[1])]
                tail[0] = n_tail[0]
                tail[1] = n_tail[1]
            \
            elif all(delta == [2, 0]):
                tail [0] -= 1
            elif all(abs(delta) == [2, 1]):
                n_tail = head + [delta[0]/abs(delta[0]), 0]
                tail[0] = n_tail[0]
                tail[1] = n_tail[1]
            \
            elif all(delta == [0, 2]):
                tail [1] -= 1
            elif all(abs(delta) == [1, 2]):
                n_tail = head + [0, delta[1]/abs(delta[1])]
                tail[0] = n_tail[0]
                tail[1] = n_tail[1]
            \
            \
            elif all(abs(delta) == [2, 2]):
                tail -= make_array_int(make_array_int(tail - head) / 2)
            rope[i] = head
            rope[i+1] = tail
            rope = [make_array_int(knot) for knot in rope]
            places.add(tuple(rope[9]))
        # print(f"{total_steps:03d}", move, f"{_:02d}", *rope)
        # print(head, tail)

# print(sorted([*places]))
print(len(places))



