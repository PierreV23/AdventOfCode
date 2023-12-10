from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
from typing import Iterable, TypeVar
from pprint import pprint


class BetterRange:
    start: int
    end: int
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __contains__(self, n: int) -> bool:
        return self.start<= n < self.end
        # return n in range(self.start, self.end)
    
    def __and__(self, other: BetterRange) -> None | BetterRange:
        if other.start in self or other.end-1 in self or self.start in other or self.end-1 in other:
            start = max(self.start, other.start)
            end = min(self.end, other.end)-1
            return BetterRange(start, end)
        return None
    
    def __repr__(self):
        return f"BetterRange({self.start}, {self.end})" 
    
    def __add__(self, n: int) -> BetterRange:
        return BetterRange(self.start +n , self.end+n)

    def __hash__(self) -> int:
        return (self.start, self.end).__hash__()
    
    def __copy__(self):
        return BetterRange(self.start, self.end)

class Collection:
    inv: list[BetterRange]
    def __init__(self, brs: list[BetterRange]):
        self.inv = brs
    
    def extract(self, other: BetterRange) -> list[BetterRange]:
        b = deepcopy(self.inv)
        self.inv = []
        ret = []
        for s in b:
            if s&other is None:
                self.inv.append(s)
            elif other.start <= s.start and s.end <= other.end:
                n = s&other
                if n is None: raise Exception("Da hell??", s, other)
                ret.append(n)
                ... # s completely inside o
            elif s.start <= other.start and other.start <= s.end:
                self.inv.append(BetterRange(s.start, other.start))
                n = s&other
                if n is None: raise Exception("Da hell??", s, other)
                ret.append(n)
                ... # s left to o
            elif other.end <= s.end:
                self.inv.append(BetterRange(other.end, s.end))
                n = s&other
                if n is None: raise Exception("Da hell??", s, other)
                ret.append(n)
                ... # s right to o
            elif other.start <= s.start and s.end <= other.end:
                n = s&other
                if n is None: raise Exception("Da hell??", s, other)
                ret.append(n)
                self.inv.append(BetterRange(s.start, other.start))
                self.inv.append(BetterRange(s.end, other.end))
                ... # o completely inside s
            else:
                raise Exception("bug")
        return ret
            




class Conv:
    dest_start: int
    dest_end: int
    dest_range: BetterRange
    sour_start: int
    sour_end: int
    sour_range: BetterRange
    length: int
    offset_from_sour: int
    # offset_from_dest: int
    def __init__(self, dest_start, sour_start, length):
        self.dest_start = dest_start
        self.dest_end = dest_start + length
        self.dest_range = BetterRange(self.dest_start, self.dest_end)
        self.sour_start = sour_start
        self.sour_end = sour_start + length
        self.sour_range = BetterRange(self.sour_start, self.sour_end)
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
    i = iter(inventory)
    for start in i:
        length = next(i)
        brs = [BetterRange(start ,start+length)]
        print(); print(brs)
        source = "seed"
        while source != "location":
            dest = extract_one([d for s, d in conversions.keys() if source == s])
            col = Collection(brs)
            extracted = []
            for c in conversions[source, dest]:
                extracted.extend(br+c.offset_from_sour for br in col.extract(c.sour_range))
            brs = extracted + col.inv
            # brs = [n+c.offset_from_sour if (n:=br&c.sour_range) else br for c in conversions[source, dest] for br in brs]
            # brs = [(n, n+c.offset_from_sour, c.offset_from_sour, c.sour_range) for c in conversions[source, dest] for br in brs if (n:=br&c.sour_range) is not None]
            # print((source, dest,  [(n,o,c) for n,_,o,c in brs], "NO OFFSET"))
            print((source, dest, brs))
            source = dest
        results.extend([*brs])
        # results.append(num)
        # print("eind", num)
    # print("eind", min(results))
    # print(min(br.start for br in brs))
    x = sorted(set(br.start for br in results))
    print(x)
    print(min(x))

def solver2(inventory: list[int], conversions: dict[tuple[str ,str], list[Conv]]):
    ...

if __name__ == '__main__':
    test = solver(*parser('test_input.txt'))
    print(test)
    assert test == None
    print(solver(*parser()))