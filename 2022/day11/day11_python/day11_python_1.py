
from copy import copy
from pathlib import Path
from pprint import pprint
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day11_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
# day_input = day_input_file.readlines()
day_input = day_input_file.read().split("\n\n")

monkeys = []
for monkey in day_input:
    _,  starting_items, operation, test, true, false = [l.lstrip() for l in monkey.split('\n')]
    starting_items = [*map(int, starting_items.split(': ')[1].split(", "))]
    operation = operation.split(" = ")[1]
    test = int(test.split(' ')[-1])
    true = int(true.split(' ')[-1])
    false = int(false.split(' ')[-1])
    monkeys.append([
        starting_items,
        operation,
        test,
        true,
        false,
    ])

pprint(monkeys)

def exe_operation(operation, old):
    operation = operation.replace("old", f"{old}")
    a, op, b = operation.split(' ')
    a, b = int(float(a)), int(float(b))
    match op:
        case '*':
            return a * b
        case '+':
            return a + b
        case _:
            raise Exception()

inspections = {k:0 for k in range(len(monkeys))}

for _ in range(20):
    for idx, monkey in enumerate(monkeys):
        items, operation, test, true, false = monkey
        n_items = copy(items)
        for item in n_items:
            inspections[idx] += 1
            items.pop()
            worry = exe_operation(operation, item)
            worry = worry // 3
            if worry % test == 0:
                monkeys[true][0].append(worry)
            else:
                monkeys[false][0].append(worry)

# for idx, monkey in enumerate(monkeys):
#     print(f"monkey {idx}: {', '.join(map(str, monkey[0]))}")

x, y = sorted([*inspections.values()])[-2:]
print(x, y, x*y)
