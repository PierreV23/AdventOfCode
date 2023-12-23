from typing import Iterable
import sys
sys.setrecursionlimit(10_000)

def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.read().strip().split('\n')
        # return file.read().strip().split('\n\n')

def solver(lines: list[str]):
    print('after solver call')
    lines = [*lines]
    grid = {(y,x):c for y, row in enumerate(lines) for x, c in enumerate(row)}
    start = next((0, x) for x, cell in enumerate(lines[0]) if cell == '.')
    end = next((len(lines)-1, x) for x, cell in enumerate(lines[-1]) if cell == '.')

    def r(seen: list, pos: tuple[int, int], steps: int):
        # print(len(seen))
        if pos == end:
            # lol stel je voor bug hebben omdat je perongelijk uppercase V gebruikte
            # s = '\n'.join(
            #     ''.join('O' if (y, x) in seen and c not in '><v^' else c for x, c in enumerate(row))
            #     for y, row in enumerate(lines)
            # )
            # print(steps, seen)
            # print(steps)
            # print(s)
            return steps
        char = grid[pos]
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        slopes = {
                '>': (0, 1),
                '<': (0, -1),
                '^': (-1, 0),
                'v': (1, 0),
            }
        if char in '><v^':
            dirs = (slopes[char],)
        highest = -1
        y, x = pos
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if (ny, nx) not in grid:
                continue
            new_char = grid[ny, nx]
            if new_char == '#' or (ny, nx) in seen:
                continue
            if new_char in '><v^' and (dy, dx) != slopes[new_char]:
                continue
            highest = max(highest, r(seen[::] + [(ny, nx)], (ny, nx), steps + 1))
        return highest
    
    print(start, end)
    ans = r([start], start, steps=0)
    print(f"{ans=}")
    return ans
    




test_p1 = solver(parser('test_input.txt'))
print(test_p1)
assert test_p1 == 94, test_p1
# print(solver(parser()))

# test_p2 = solver(parser('test_input.txt'))
# test_p2 = solver(parser('test_input_p2.txt'))
# print(test_p2)
# assert test_p2 == None, test_p2
inp = parser()
print('before solver call')
ans = solver(inp)
print(ans)


...

