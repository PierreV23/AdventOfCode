from itertools import cycle
from typing import Iterable
from math import lcm

def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        path, link = file.read().strip().split("\n\n")
        p = lambda s: s.strip('(').strip(')').split(", ")
        links = {l.split(' = ')[0]:l.split(' = ')[1].strip('(').strip(')').split(", ") for l in link.split('\n')}
        return path, links

def solver(path, links):
    finished = []
    pos = [l for l in links.keys() if l[-1] == 'A']
    for counter, step in enumerate(cycle(path)):
        # print(counter, step, pos)
        if not pos:
            break
        # print(len([p for p in pos if p[-1] =='Z']), len(pos), pos)
        c = pos[::]
        pos = []
        for p in c:
            if p[-1] == 'Z':
                finished.append(counter)
            else:
                pos.append(links[p]["LR".index(step)])
    else:
        print("nuh uh")
    print(finished, counter)
    return finished


if __name__ == '__main__':
    test = lcm(*solver(*parser('test_input_p2.txt')))
    print(test)
    assert test == 6
    print(lcm(*solver(*parser())))