def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    ...


if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == None
    print(solver(parser()))