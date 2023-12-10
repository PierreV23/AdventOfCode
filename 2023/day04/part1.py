from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

def solver(lines: Iterable[str]):
    lines = [*lines]
    summed = 0
    for line in lines:
        _card_id, cards = line.split(": ")
        wc, mc = cards.split(" | ")
        wc, mc = wc.split(' '), mc.split(' ')
        wc, mc = [c for c in wc if c], [c for c in mc if c]
        count = 0
        for idx, c in enumerate(wc):
            # if c in mc:
            #     if idx > 0:
            #         if w[idx-1]:
            #             w.append(w[idx-1]*2)
            #             w[idx-1] = 0
            #         else:
            #             w.append(1) 
            #     else:
            #         w.append(1)
            # else:
            #     w.append(0)
            count += c in mc
        print(2**(count-1) if count > 0 else 0)
        summed += 2**(count-1) if count > 0 else 0
    return summed


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 13
    print(solver(parser()))