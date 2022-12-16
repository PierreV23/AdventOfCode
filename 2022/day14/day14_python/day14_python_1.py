# ignore all the useless bloat, i was trying some stuff out for a future AOC library
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from pprint import pprint
CURR_DIR = Path()

# day_input_file = open(CURR_DIR / 'day14_input.txt')
day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

c = [[int(n) for n  in coords.split(",")] for line in day_input for coords in line.split(" -> ")]
# print(c)  
HEIGHT = max(c, key=lambda x_y: x_y[1])[1]
X_START = min(c, key=lambda x_y: x_y[0])[0]
X_END = max(c, key=lambda x_y: x_y[0])[0]
grid = [['.' for _ in range(X_END - X_START + 1)] for _ in range(HEIGHT + 1)]

def print_grid(g, join = True, join_c = ""):
    for r in g:
        print(join_c.join(r) if join else r)

def uno(n: int):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    return 0


@dataclass
class Boundaries(tuple):
    height: int
    width: int

    def __hash__(self) -> int:
        return (self.height, self.width).__hash__()

@dataclass
class Pos:
    y: int
    x: int

    def __add__(self, other):
        return Pos(self.y + other.y, self.x + other.x)
    
    def __sub__(self, other):
        return Pos(self.y - other.y, self.x - other.x)
    
    def inside(self, b: Boundaries):
        y, x = self.y, self.x
        h, w = b.height, b.width
        if y < 0 or y >= h  or x < 0 or x >= w:
            return False
        return True
    
    def __hash__(self) -> int:
        return (self.y, self.x).__hash__()
    
    def __iter__(self):
        return (i for i in (self.y, self.x))
    
    def flip(self):
        self.x, self.y = self.y, self.x
        return self
    
    def down(self, m = 1):
        self.y -= m
        return self
    
    def up(self, m = 1):
        self.y += m
        return self
    
    def right(self, m = 1):
        self.x += m
        return self
    
    def left(self, m = 1):
        self.x -= m
        return self


def index_2d(a: list | tuple, i) -> Pos | None:
    try:
        return next((Pos(y, s.index(i)) for y, s in enumerate(a) if i in s))
    except StopIteration:
        raise Exception("Thing not found")

def indexes(a, i) -> list[int] | None:
    return [idx for idx, thing in enumerate(a) if thing == i]

def indexes_2d(a, i) -> list[Pos] | None:
    return [Pos(y, s.index(i)) for y, s in enumerate(a) if i in s]

def iter_double_offset(a: list | tuple):
    for idx in range(len(a) - 1):
        head, tail = a[idx], a[idx+1]
        yield head, tail
    return


for line_idx, line in enumerate(day_input):
    coords = [Pos(*map(int, c.split(","))).flip() for c in line.split(" -> ")]
    z = [*iter_double_offset(coords)]
    print(z)
    for head, tail in z:
        head -= Pos(0, X_START)
        tail -= Pos(0, X_START)
        # y, x = head - tail # this was the original, i feel so dumb L
        y, x = tail - head
        if x and y:
            raise Exception()
        curr = Pos(*head)
        try:
            f = None
            match uno(x):
                case -1:
                    f = Pos.left
                case 1:
                    f = Pos.right
            match uno(y):
                case -1:
                    f = Pos.down
                case 1:
                    f = Pos.up
            
            # curr -= Pos(0, 1)
            grid[curr.y][curr.x] = '#'
            for _ in range(abs(x)+abs(y)):
                f(curr)
                grid[curr.y][curr.x] = '#'

        except:
            print(curr, HEIGHT, X_START, X_END, X_END - X_START, curr + Pos(0, X_START), head + Pos(0, X_START), tail +Pos(0, X_START))
            print_grid(grid)
            raise Exception()


print_grid(grid)
spawn = Pos(0, 500) - Pos(0, X_START)