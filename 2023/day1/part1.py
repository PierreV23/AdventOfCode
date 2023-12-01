#part 1
from itertools import islice
def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    lines = ["".join(filter(str.isnumeric, line)) for line in lines]
    print(lines)
    return sum(int(line[0]+line[-1]) for line in lines)
    

if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 142
    print(solver(parser()))