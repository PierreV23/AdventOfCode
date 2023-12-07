from typing import Iterable
from collections import Counter
from functools import cmp_to_key

def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n').split(' ')

deck = "AKQT98765432J"

def get_type(card):
    d = Counter(card)
    c = [count for t, count in d.items() if t != 'J']
    c.sort()
    if not c:
        return 6
    c[-1] += d.get('J', 0)
    if max(c) == 5:
        return 6
    elif max(c) == 4:
        return 5
    elif max(c) == 3 and min(c) == 2:
        return 4
    elif max(c) == 3 and min(c) == 1:
        return 3
    elif c.count(2) == 2:
        return 2
    elif c.count(2) == 1 and max(c) == 2:
        return 1
    elif max(c) == 1:
        return 0
    else:
        raise Exception("bad card", card)

# return negative if card2 is bigger
def cmp(card1, card2):
    card1 = card1[0]
    card2 = card2[0]
    c1, c2 = get_type(card1), get_type(card2)
    c = c1-c2
    if c != 0:
        return c
    for a,b in zip(card1, card2):
        if a==b:
            continue
        else:
            return deck.index(b) - deck.index(a)
    else:
        print("HUH")
        return 0
    raise Exception()

def solver(lines: Iterable[str]):
    lines = [*lines]
    lines.sort(key=cmp_to_key(cmp))
    print(lines)
    return sum(idx*int(bid) for idx, (_, bid) in enumerate(lines, start=1))


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 5905
    print(solver(parser()))