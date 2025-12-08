#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy",
# ]
# ///
import numpy as np
import sys

lines = [*sys.stdin]
points = np.array([
    [int(n) for n in point.strip().split(',')]
    for point in lines
    if point.strip()
])

# print(points)

diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
distances = np.sqrt(np.sum(diff**2, axis=2))

i_indices, j_indices = np.triu_indices(len(points), k=1)

Point = tuple[int, int, int]

pairwise_distances: list[tuple[Point, Point, float]] = sorted(
    ((tuple(map(int, points[i])), tuple(map(int, points[j])), float(distances[i, j]))
        for i, j in zip(i_indices, j_indices)),
    key=lambda p_p_d: p_p_d[2]
)

# from pprint import pprint
# pprint(results)
# print(f"\nTotal pairs: {len(results)}")

connections_to_make = int(sys.argv[1])

circuits: dict[int, set[Point]] = {}
points: dict[Point, int] = {}

circuit_counter = 0

for _, (point1, point2, _) in zip(range(connections_to_make), pairwise_distances):
    circuit_counter += 1 # lazy lol
    match point1 in points, point2 in points:
        case True, True:
            c1 = points[point1]
            c2 = points[point2]
            if c1==c2: continue
            assert c1!=c2
            circuit1 = circuits.pop(c1)
            circuit2 = circuits.pop(c2)
            circuits[circuit_counter] = circuit1 | circuit2
            for point in (*circuit1, *circuit2, point1, point2):
                points[point] = circuit_counter
        case True, False:
            c = points[point1]
            circuits[c].add(point2)
            points[point2] = c
        case False, True:
            c = points[point2]
            circuits[c].add(point1)
            points[point1] = c
        case False, False:
            circuits[circuit_counter] = {point1, point2}
            points[point1] = circuit_counter
            points[point2] = circuit_counter


# print(circuits)
from functools import reduce
length = map(len, circuits.values())
longest_3 = sorted(length, reverse=True)[:3]
print(longest_3)
ans = reduce(int.__mul__, longest_3)
print(ans)
