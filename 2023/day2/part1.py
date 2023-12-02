def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

def solver(lines: list[str]):
    summed = 0
    for line in lines:
        game, sets_raw = line.strip().split(": ")
        _, game_id = game.split(" ")
        sets = [{cube.split(' ')[1]:int(cube.split(' ')[0]) for cube in cubes.split(", ")} for cubes in sets_raw.split("; ")]
        if all((cubes.get("red", 0)<=12 and cubes.get("green", 0)<=13 and cubes.get("blue", 0)<=14) for cubes in sets):
        # cubes = {colour:sum(cubes.get(colour, 0) for cubes in sets) for colour in ("red", "blue", "green")}
        # if (cubes.get("red", 0)<=12 and cubes.get("green", 0)<=13 and cubes.get("blue", 0)<=14):
            summed += int(game_id)
    return summed



if __name__ == '__main__':
    test = solver(parser('test_input.txt'))
    print(test)
    assert test == 8
    print(solver(parser()))