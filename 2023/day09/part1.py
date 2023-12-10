from pprint import pprint
from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')


def pairs(ls):
    a,b = iter(ls), iter(ls)
    next(b)
    return zip(a,b)

def difference(numbers):
    return [int(b)-int(a) for a,b in pairs(numbers)]



def solver(lines: Iterable[str]):
    # l = iter(lines)
    # next(l)
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
            # print(diff)
        # print("traceback")
        # pprint(history)
        for diff, up in pairs(history[::-1]):
            # print("before", diff, up)
            # while len(diff) + 1 <= len(up):
            up.append(diff[-1] + up[-1])
            # print("after", diff, up)
        # pprint(history)
        ans += history[0][-1]
    return ans






if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 114
    print(solver(parser()))