from collections import deque
from pprint import pprint
from typing import Iterable, TypeVar


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

T = TypeVar('T')

def pairs(ls: list[T]) -> Iterable[tuple[T, T]]:
    a,b = iter(ls), iter(ls)
    next(b)
    return zip(a,b)

def difference(numbers):
    return [int(b)-int(a) for a,b in pairs(numbers)]



def solver(lines: Iterable[str]):
    lines = iter(lines)
    # next(lines)
    ans = 0
    for line in lines:
        numbers = [*map(int, line.split(' '))]
        # print(numbers)
        history = []
        diff = numbers
        history.append(diff)
        while any(diff):
            diff = difference(diff)
            history.append(diff)
        history = [deque(h) for h in history]
        # print(history)
        for diff, up in pairs(history[::-1]):
            up.appendleft(up[0] - diff[0])
        # print(history[0], history[0][-1])
        ans += history[0][0]
    return ans






if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 2
    print(solver(parser()))