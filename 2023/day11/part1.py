from typing import Iterable


def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        for line in file:
            yield line.strip('\n')

def solver(lines_i: Iterable[str]):
    lines_i = [*lines_i]
    lines_i2 = []
    lines=[[] for _ in lines_i]
    coords = []
    c = 0
    for line in lines_i:
        if line.count('.') == len(line):
            lines_i2.append([*line])
            lines.append([])
        lines_i2.append([*line])
    for col_idx in range(len(lines_i2[0])):
        is_empty = all(line[col_idx]=='.' for line in lines_i2)
        if is_empty: print("empty", col_idx)
        for y, line in enumerate(lines_i2):
            lines[y].append(line[col_idx])
            if is_empty:
                lines[y].append('.')
        
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                coords.append((y, x))

    print('\n'.join(''.join(line) for line in lines))
    print(coords)
    summed = 0
    for a, b in set(frozenset((a,b)) for a in range(len(coords)) for b in range(len(coords)) if a!=b):
        ay,ax = coords[a]
        by,bx = coords[b]
        dist = abs(ax-bx) + abs(ay-by)
        # if frozenset((a,b)) == frozenset((0,6)):
        #     assert dist == 15, f"{dist}"
        # elif frozenset((a,b)) == frozenset((2,5)):
        #     assert dist == 17, f"{dist}"
        # elif frozenset((a,b)) == frozenset((7,8)):
        #     assert dist == 5, f"{dist}"
        # elif frozenset((a,b)) == frozenset((4,8)):
        #     assert dist == 9, f"{dist}"
        summed += dist
    return summed




if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 374
    print(solver(parser()))