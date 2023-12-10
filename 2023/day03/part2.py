def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    lines = [line.strip() for line in lines]
    queue = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*':
                temp_queue = []
                lookaround = ((-1, 1), (1, 1), (1, 0), (0, 1), (1, -1), (-1, -1), (-1, 0), (0, -1))
                for ly, lx in lookaround:
                    ny, nx = y + ly, x + lx
                    if not (0 <= ny < len(lines) and 0 <= nx < len(lines[0])):
                        continue
                    try:
                        if lines[ny][nx].isdecimal():
                            temp_queue.append((ny, nx))
                    except:
                        print(y, x, ny, nx)
                if len(temp_queue) >= 2:
                    queue.append(temp_queue)
    print(queue)
    summed = 0
    for mid_queue in queue:
        print(mid_queue)
        collection = {}
        for y, x in mid_queue:
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
        numbers = [*map(int, collection.values())]
        if len(numbers) != 2:
            continue
        a, b = numbers
        summed += a*b
        print(collection)
    return summed




if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 467835
    print(solver(parser()))