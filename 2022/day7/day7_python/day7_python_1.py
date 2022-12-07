from pathlib import Path
from pprint import pprint
from typing import Tuple
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day7_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
# day_input = day_input_file.readlines()
# day_input = day_input_file.read()


directories = {}
lines = day_input_file.readlines()
curr_dir = directories
depth = []

for idx, line in enumerate(lines):
    line = line.strip("\n")
    if line.startswith('$'):
        _, cmd, *data = line.split()
        if cmd == 'cd':
            data = data[0]
            if data == '/':
                curr_dir = directories
                depth = []
            elif data == '..':
                curr_dir = directories
                for dir in depth[:-1]:
                    curr_dir = curr_dir[dir]
                depth = depth[:-1]
            else:
                curr_dir = curr_dir[data]
                depth.append(data)
        elif cmd == 'ls':
            idx += 1
            while idx < len(lines) and (not lines[idx].startswith('$')):
                first, second = lines[idx].split()
                if first == 'dir':
                    if second not in curr_dir:
                        curr_dir[second] = {}
                elif first.isnumeric():
                    curr_dir[second] = int(first)
                else:
                    raise Exception()
                idx += 1
        else:
            raise Exception()


def get_size(dictionary) -> Tuple[int, int]:
    child_sizes = []
    self_size = 0
    for value in dictionary.values():
        if isinstance(value, dict):
            child_size, child_childs = get_size(value)
            child_sizes.extend(child_childs)
            self_size += child_size
        elif isinstance(value, int):
            self_size += value
        else:
            raise Exception()
    child_sizes.append(self_size)
    return (self_size, child_sizes)



_total, folders = get_size(directories)
print( sum(filter(lambda a: a <= 100_000, folders)) )