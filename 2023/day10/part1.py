from enum import Enum
from typing import Iterable

import numpy as np


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')



def f(queue, dist, matrix, counter, curr, source):
    y, x = curr
    valid = {
        (1, 0): '|JL',
        (-1, 0): '|F7',
        (0, 1): '-J7',
        (0, -1): '-LF',
    }
    translate = {
        '|': {(1,0):(1,0), (-1,0):(-1,0)},
        '-': {(0,-1):(0,-1), (0,1):(0,1)},
        'J': {(-1, 0):(0, -1), (0, 1):(1, 0)},
        
    }
    char = matrix[y][x]
    if char == 'S':
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y+dy, x+dx
            if not (0 <= ny < len(matrix) and 0 <= nx < len(matrix[0])):
                continue
            if matrix[ny][nx] not in valid[(dy, dx)]:
                continue
            if (ny, nx) not in dist:
                dist[(ny, nx)] = counter
                queue.append((counter+1, (ny, nx), (dy, dx)))
            elif dist[(ny, nx)] > counter:
                dist[(ny, nx)] = counter
                queue.append((counter+1, (ny, nx), (dy, dx)))
    else:
        sdy, sdx = source
        print(source, translate[char][(sdy, sdx)])


def solver(matrix: Iterable[str]):
    matrix = [*matrix]
    starts = [(y, x) for y, _ in enumerate(matrix) for x, _ in enumerate(matrix[y]) if matrix[y][x] == 'S']
    print(starts)
    assert len(starts) == 1
    y, x = start = starts[0] # type: ignore
    dist = {}
    queue= [(0, start, None)]
    print(dist, queue)
    for task in queue:
        _counter, (y, x), _source = task
        f(queue, dist, matrix, *task)
        print(dist, queue, task)


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == None
    # print(solver(parser()))