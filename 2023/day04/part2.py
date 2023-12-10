from typing import Iterable
from collections import defaultdict


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

def solver(lines: Iterable[str]):
    lines = [*lines]
    summed = 0
    stack = defaultdict(int)
    highest = int(lines[-1].split(": ")[0].split(' ')[1])
    print(highest)
    for line in lines:
        card_id, cards = line.split(": ")
        card_id = int(card_id.split(' ')[-1])
        wc, mc = cards.split(" | ")
        wc, mc = wc.split(' '), mc.split(' ')
        wc, mc = [c for c in wc if c], [c for c in mc if c]
        count = sum([c in mc for c in wc])
        print(count)
        stack[card_id] += 1
        if any(c in mc for c in wc):
            for n in range(card_id+1, card_id+count+1):
                if n <= highest:
                    stack[n] += max(stack[card_id], 1)
        print(stack)
    return sum(stack.values())


if __name__ == '__main__':
    test = solver(parser('test_input_p2.txt'))
    print(test)
    assert test == 30
    print(solver(parser()))