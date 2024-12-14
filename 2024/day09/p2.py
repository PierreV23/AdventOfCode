#!/usr/bin/env python3
import sys


with open(sys.argv[1], 'r') as file:
    inp = [[int(c) for c in l] for line in file if (l:=line.strip())][0]

unfragged = [(-1 if (idx % 2) else idx//2, size) for idx, size in enumerate(inp)]

# print(unfragged)

def pr(fr):
    print(
        ''.join(
            '.' if id == -1 else f"{id}"
            for id, size in fr
            for _ in range(size)
        )
    )

fragged = unfragged[::]
idx = -1
while (len(fragged) + idx) >= 0:
    print(len(fragged), idx)
    # print(fragged[idx])
    if fragged[idx][0] != -1:
        new_idx = 0
        while new_idx < (len(fragged) + idx):
            # pr(fragged)
            if fragged[new_idx][0] == -1:
                while fragged[new_idx+1][0] == -1:
                    fragged[new_idx:new_idx+2] = [(-1, fragged[new_idx][1] + fragged[new_idx+1][1])]
                if fragged[new_idx][1] >= fragged[idx][1]:
                    if fragged[new_idx][1] == fragged[idx][1]:
                        fragged[new_idx], fragged[idx] = fragged[idx], fragged[new_idx]
                    else:
                        fragged[new_idx:new_idx+1], fragged[idx] = [fragged[idx], (-1, fragged[new_idx][1]-fragged[idx][1])], (-1, fragged[idx][1])
                    break
            new_idx += 1
    idx -= 1

# print(fragged)
# pr(fragged)

fragged = [
    id
    for id, size in fragged
    for _ in range(size)
]

s = 0
for idx, id in enumerate(fragged):
    if id == -1:
        continue
    s += idx * id

print(s)

#0123456789 10
#00000000.. 10