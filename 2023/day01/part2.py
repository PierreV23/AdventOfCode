def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        return file.readlines()

WORDS = {
    "one": "1",
    "two": "2",
    "three": "3 ",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def solver(lines: list[str]):
    new_lines = []
    for line in lines:
        new_line = ""
        for idx, c in enumerate(line):
            if c.isnumeric():
                new_line += c
            else:
                for word, n in WORDS.items():
                    if line[idx:idx+len(word)] == word:
                        new_line += n
        new_lines.append(new_line)
    lines = ["".join(filter(str.isnumeric, line)) for line in new_lines]
    print(lines)
    return sum(int(line[0]+line[-1]) for line in lines)



if __name__ == '__main__':
    test = solver(parser('test_input_p2.txt'))
    print(test)
    assert test == 281
    print(solver(parser()))