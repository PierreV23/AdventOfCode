from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

def solver(lines: Iterable[str]):
    lines = [*lines]


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == None
    print(solver(parser()))