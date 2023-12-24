from collections import defaultdict
from pathlib import Path
from pprint import pprint
from typing import Callable, Iterable
import sys
sys.setrecursionlimit(10_000)

def parser(file = 'input.txt'):
    with open(Path(__file__).parent / file, 'r') as file:
        return file.read().strip().split('\n')
        # return file.read().strip().split('\n\n')

Point = tuple[int, int]
DeltaPoint = tuple[int, int]

def solver(lines: list[str]):
    print('after solver call')
    lines = [*lines]
    grid = {(y,x):c for y, row in enumerate(lines) for x, c in enumerate(row)}
    start = next((0, x) for x, cell in enumerate(lines[0]) if cell == '.')
    end = next((len(lines)-1, x) for x, cell in enumerate(lines[-1]) if cell == '.')
    ht: Callable[[Point, Point], tuple[Point, Point]] = lambda a, b: tuple(sorted((a, b))) # type: ignore
    graph: defaultdict[Point, list[tuple[Point, Point]]] = defaultdict(list)
    queue: list[tuple[Point, Point, DeltaPoint, int]] = [(start, start, (1, 0), 0)]
    segments: dict[tuple[Point, Point], int] = {}
    seen: set[Point] = set()
    # segment = {tuple(sorted((start_pos, end_pos))) : length}
    # graph = {point:[segment, ...]}
    for start_pos, (y, x), (dy, dx), length in queue:
        seen.add((y, x))
        if (y, x) == end:
            end_pos = (y, x)
            segment = ht(start_pos, end_pos)
            segments[segment] = length
            graph[start_pos].append(segment)
            graph[end_pos].append(segment)
        if len(queue) == 9:
            ...
        neighbours = []
        for ndy, ndx in (n for n in ((0, 1), (0, -1), (1, 0), (-1, 0)) if n != (-dy, -dx)):

            ny, nx = y + ndy, x + ndx
            if (ny, nx) not in grid:
                continue
            elif grid[ny, nx] == '#':
                continue
            neighbours.append((ndy, ndx))
        
        if len(neighbours) > 1:
            end_pos = (y, x)
            segment = ht(start_pos, end_pos)
            segments[segment] = length + 1
            if segment in graph[end_pos]:
                continue
            graph[start_pos].append(segment)
            graph[end_pos].append(segment)
            for ndy, ndx in neighbours:
                ny, nx = y + ndy, x + ndx
                if (ny, nx) in seen:
                    continue
                queue.append((end_pos, (ny, nx), (ndy, ndx), 0))
        elif len(neighbours) == 1:
            (ndy, ndx), = neighbours
            ny, nx = y + ndy, x + ndx
            queue.append((start_pos, (ny, nx), (ndy, ndx), length + 1))
        else:
            continue
    
    segments_to_graph = {
        segment:tuple([
            g
            for g, sgmnts in graph.items()
            if segment in sgmnts
        ])
        for segment in segments
    }
    assert all(len(gs)==2 for gs in segments_to_graph.values())

    # assert len(segments) == len(set(map(tuple, map(sorted, segments))))
    print(segments)
    print(graph)
    pprint(segments_to_graph)
    def r(seen: set, pos: Point, steps: int):
        if pos == end:
            return steps
        highest = -1

        segs = graph[pos]
        for seg in segs:
            new_pos = next(p for p in segments_to_graph[seg] if p != pos)
            if new_pos in seen:
                continue
            seen.add(new_pos)
            highest = max(highest, r(seen, new_pos, steps + segments[seg]))
            seen.remove(new_pos)
        return highest
    
    seen = set()
    seen.add(start)
    highest = r(seen, start, 0)
    
    return highest
    




test_p1 = solver(parser('test_input.txt'))
print(test_p1)
assert test_p1 == 154, test_p1
# print(solver(parser()))

# test_p2 = solver(parser('test_input.txt'))
# test_p2 = solver(parser('test_input_p2.txt'))
# print(test_p2)
# assert test_p2 == None, test_p2
inp = parser()
print('before solver call')
ans = solver(inp)
print(ans)


...

