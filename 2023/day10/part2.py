from enum import Enum
from typing import Iterable

import numpy as np


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

def f(queue, dist, matrix, counter, curr, source):
    y, x = curr
    valid = {
        DOWN: '|JL',
        UP: '|F7',
        RIGHT: '-J7',
        LEFT: '-LF',
    }
    translate = {
        '|': {UP:UP, DOWN:DOWN},
        '-': {LEFT:LEFT, RIGHT:RIGHT},
        'J': {DOWN:LEFT, RIGHT:UP},
        'L': {DOWN:RIGHT, LEFT:UP},
        '7': {RIGHT:DOWN, UP:LEFT},
        'F': {LEFT:DOWN, UP:RIGHT}
    }
    char = matrix[y][x]
    # print(char)
    if char == 'S':
        for new in (LEFT, RIGHT, UP, DOWN):
            dy, dx = new
            ny, nx = y+dy, x+dx
            if not (0 <= ny < len(matrix) and 0 <= nx < len(matrix[0])):
                continue
            if matrix[ny][nx] not in valid[new]:
                continue
            if (ny, nx) not in dist:
                dist[(ny, nx)] = counter + 1
                queue.append((counter+1, (ny, nx), new))
            elif dist[(ny, nx)] > counter:
                dist[(ny, nx)] = counter + 1
                queue.append((counter+1, (ny, nx), new))
    else:
        # print("else")
        dy, dx = new = translate[char][source]
        ny, nx = y+dy, x+dx
        if not (0 <= ny < len(matrix) and 0 <= nx < len(matrix[0])):
            # print("not inside")
            return
        if matrix[ny][nx] not in valid[new]:
            # print("not valid", curr, (ny,nx),matrix[ny][nx], valid[new], char, translate[char][source])
            return
        if (ny, nx) not in dist:
            # print("Not in")
            dist[(ny, nx)] = counter + 1
            queue.append((counter+1, (ny, nx), new))
        elif dist[(ny, nx)] > counter:
            # print("In but count")
            dist[(ny, nx)] = counter + 1
            queue.append((counter+1, (ny, nx), new))
        else:
            print("Huh")
        # print(f"{source=}, {translate[char][source]=}")
    


def solver(matrix: Iterable[str]):
    matrix = [*matrix]
    starts = [(y, x) for y, _ in enumerate(matrix) for x, _ in enumerate(matrix[y]) if matrix[y][x] == 'S']
    print(starts)
    assert len(starts) == 1
    y, x = start = starts[0] # type: ignore
    dist = {start:0}
    queue= [(0, start, None)]
    print(dist, queue)
    for task in queue:
        _counter, (y, x), _source = task
        f(queue, dist, matrix, *task)
        # print(dist, queue, task)
        # break
    m  = max(dist.values())
    if m<= 9:
        print('\n'.join(''.join(str(dist.get((y, x), '.')) for x,_ in enumerate(matrix[y])) for y, _ in enumerate(matrix)))
    return m


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 4
    print(solver(parser()))