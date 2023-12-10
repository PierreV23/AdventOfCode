from itertools import cycle
from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        path, link = file.read().strip().split("\n\n")
        p = lambda s: s.strip('(').strip(')').split(", ")
        links = {l.split(' = ')[0]:l.split(' = ')[1].strip('(').strip(')').split(", ") for l in link.split('\n')}
        return path, links

def solver(path, links):
    pos = "AAA"
    for counter, step in enumerate(cycle(path)):
        # print(counter, step, pos)
        if pos == "ZZZ":
            break
        pos = links[pos]["LR".index(step)]
    else:
        print("nuh uh")
    return counter


if __name__ == '__main__':
    test = solver(*parser('test_input.txt'))
    print(test)
    assert test == 2
    test = solver(*parser('test_input_2.txt'))
    print(test)
    assert test == 6
    print(solver(*parser()))