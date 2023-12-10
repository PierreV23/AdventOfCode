def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    summed = 0
    for line in lines:
        game, sets_raw = line.strip().split(": ")
        _, game_id = game.split(" ")
        sets = [{cube.split(' ')[1]:int(cube.split(' ')[0]) for cube in cubes.split(", ")} for cubes in sets_raw.split("; ")]
        max_on_key = lambda key: (lambda d: d.get(key, 0))
        max_red = max(sets, key=max_on_key("red"))["red"]
        max_green = max(sets, key=max_on_key("green"))["green"]
        max_blue = max(sets, key=max_on_key("blue"))["blue"]
        # print(max_red, max_green, max_blue)
        product = max_red * max_green * max_blue
        summed += product
    return summed



if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 2286
    print(solver(parser()))