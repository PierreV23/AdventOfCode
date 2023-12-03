def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    lines = [line.strip() for line in lines]
    collection = {}
    queue = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (not char.isdecimal()) and (not char == '.'):
                lookaround = ((-1, 1), (1, 1), (1, 0), (0, 1), (1, -1), (-1, -1), (-1, 0), (0, -1))
                for ly, lx in lookaround:
                    ny, nx = y + ly, x + lx
                    if not (0 <= ny < len(lines) and 0 <= nx < len(lines[0])):
                        continue
                    try:
                        if lines[ny][nx].isdecimal():
                            queue.append((ny, nx))
                    except:
                        print(y, x, ny, nx)
    # print(queue)
    for y, x in queue:
        nx = x
        number = ""
        while nx < len(lines[0]) and lines[y][nx].isdecimal():
            number += lines[y][nx]
            nx += 1
        nx = x - 1
        while nx >= 0 and lines[y][nx].isdecimal():
            number = lines[y][nx] + number
            nx -= 1
        collection[(y, nx+1)] = number
    # print(collection)
    print(sum(map(int, collection.values())))




if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == None
    print(solver(parser()))