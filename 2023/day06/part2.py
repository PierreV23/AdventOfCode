from typing import Iterable
from numpy import array, ceil, sqrt, sort
from math import prod


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return [[int(''.join(line.split(':')[1].replace(' ', '')))] for line in file.readlines()]

def solver(lines: Iterable[str]):
    for t,d in zip(*lines):
        a = (-t+sqrt(t**2-4*-1*-d))/2
        b = (-t-sqrt(t**2-4*-1*-d))/2
        c = [*map(int, ceil(sort(abs((array([-sqrt(t**2-4*d), sqrt(t**2-4*d)]) -t) / 2))+[0.00001, 0]))]
        print(a, b, c, range(*c), len(range(*c)))
    return prod(len(range(*map(int, ceil(sort(abs((array([-sqrt(t**2-4*d), sqrt(t**2-4*d)]) -t) / 2))+[0.00001, 0])))) for t,d in zip(*lines))


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 71503
    print(solver(parser()))