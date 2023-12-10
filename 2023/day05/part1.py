from collections import defaultdict
from typing import Iterable, TypeVar
from pprint import pprint

class Conv:
    dest_start: int
    dest_end: int
    dest_range: range
    sour_start: int
    sour_end: int
    sour_range: range
    length: int
    offset_from_sour: int
    # offset_from_dest: int
    def __init__(self, dest_start, sour_start, length):
        self.dest_start = dest_start
        self.dest_end = dest_start + length
        self.dest_range = range(self.dest_start, self.dest_end)
        self.sour_start = sour_start
        self.sour_end = sour_start + length
        self.sour_range = range(self.sour_start, self.sour_end)
        self.length = length
        # offset_from_sour + sour = dest
        self.offset_from_sour = dest_start - sour_start
        # # offset_from_dest + dest = sour
        # self.offset_from_dest =
    
    def __repr__(self):
        return str((self.dest_start, self.dest_end, self.dest_range, self.sour_start, self.sour_end, self.sour_range, self.length, self.offset_from_sour))

def parser(file = 'input.txt'):
    with open(file, 'r') as file:
        inventory, *conversions = file.read().strip().split("\n\n")
        inventory = [*map(int, inventory.lstrip("seeds: ").strip().split(' '))]
        n_c = defaultdict(list)
        for conversion in conversions:
            conversion = conversion.strip().split('\n')
            header = conversion[0]
            lines = conversion[1:]
            s, d = header.strip(" map:").split("-to-")
            n_c[(s,d)] = [Conv(*[int(n) for n in line.split(' ')]) for line in lines]
        return inventory, n_c

T = TypeVar('T')
def extract_one(a: list[T]) -> T:
    if len(a) != 1:
        raise Exception("was niet een enkel element", a)
    return a[0]

def solver(inventory: list[int], conversions: dict[tuple[str ,str], list[Conv]]):
    pprint(conversions)
    # for _, _, conv in converions:
    #     print([*map(str, conv)])
    print(inventory)
    
    results = []
    for num in inventory:
        source = "seed"
        while source != "location":
            dest = extract_one([d for s, d in conversions.keys() if source == s])
            c = [c for c in conversions[source, dest] if num in c.sour_range]
            print(source, dest, num, c)
            if c:
                conv = extract_one(c)
                num = conv.offset_from_sour + num
            source = dest
        results.append(num)
        print("eind", num)
    print("eind", min(results))


if __name__ == '__main__':
    test = solver(*parser('test_input.txt'))
    print(test)
    assert test == None
    print(solver(*parser()))