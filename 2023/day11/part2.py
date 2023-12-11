from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

def solver(lines: Iterable[str], tl = 1_000_000):
    lines = [*lines]
    cols = [tl if all(line[col_idx]=='.' for line in lines) else 1 for col_idx in range(len(lines))]
    rows = [tl if all(c=='.' for c in line) else 1 for line in lines]
    coords = []
        
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                coords.append((y, x))

    print('\n'.join(''.join(line) for line in lines))
    # print(coords)
    summed = 0
    # print(cols)
    # print(rows)
    for a, b in set(frozenset((a,b)) for a in range(len(coords)) for b in range(len(coords)) if a!=b):
        ay,ax = coords[a]
        by,bx = coords[b]
        ax = sum(cols[:ax])
        bx = sum(cols[:bx])
        ay = sum(rows[:ay])
        by = sum(rows[:by])
        dist = abs(ax-bx) + abs(ay-by)
        # if frozenset((a,b)) == frozenset((0,6)):
        #     assert dist == 15, f"{dist} {(a,b)} - {(ay, ax)}, {(by, bx)}"
        # elif frozenset((a,b)) == frozenset((2,5)):
        #     assert dist == 17, f"{dist} {(a,b)} - {(ay, ax)}, {(by, bx)}"
        # elif frozenset((a,b)) == frozenset((7,8)):
        #     assert dist == 5, f"{dist} {(a,b)} - {(ay, ax)}, {(by, bx)}"
        # elif frozenset((a,b)) == frozenset((4,8)):
        #     assert dist == 9, f"{dist} {(a,b)} - {(ay, ax)}, {(by, bx)}"
        summed += dist
    return summed




if __name__ == '__main__':
    test = solver(parser('test_input.txt'), 2)
    print(test)
    assert test == 374
    test = solver(parser('test_input.txt'), 10)
    print(test)
    assert test == 1030
    test = solver(parser('test_input.txt'), 100)
    print(test)
    assert test == 8410
    print(solver(parser()))