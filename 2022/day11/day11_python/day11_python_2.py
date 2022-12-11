
from copy import copy
from functools import reduce
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
    operation = operation.split(" = ")[1].split(' ')
    operation[0] = int(operation[0]) if operation[0].isnumeric() else operation[0]
    operation[2] = int(operation[2]) if operation[2].isnumeric() else operation[2]
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
    a, op, b = operation
    if a == 'old':
        a = old
    if b == 'old':
        b = old
    # if isinstance(a, str):
    #     print(a)
    #     raise Exception()
    # if isinstance(b, str):
    #     print(b)
    #     raise Exception()
    
    # a, b = int(a), int(b)
    match op:
        case '*':
            return a * b
        case '+':
            return a + b
        case _:
            raise Exception()

inspections = {k:0 for k in range(len(monkeys))}
test_smallifier = reduce(lambda x, y: x*y, (m[2] for m in monkeys))
for monkey_slinging_round in range(1, 10_000+1):
    # print(f"round{monkey_slinging_round} {sum(len(m[0]) for m in monkeys)}")
    for idx, monkey in enumerate(monkeys):
        items, operation, test, true, false = monkey
        
        for item in items:
            inspections[idx] += 1
            worry = exe_operation(operation, item)
            worry %= test_smallifier
            if worry % test == 0:
                monkeys[true][0].append(worry)
            else:
                monkeys[false][0].append(worry)
        monkey[0] = []
    if monkey_slinging_round % 1000 == 0 or monkey_slinging_round in (1, 20):
        print(f"== after round {monkey_slinging_round} ==")
        for idx, monkey in enumerate(monkeys):
            print(f"monkey {idx} inspected items {inspections[idx]} times")
        # for idx, monkey in enumerate(monkeys):
        #     print(f"monkey {idx}: {', '.join(map(str, monkey[0]))}")
        print()
    


# for idx, monkey in enumerate(monkeys):
#     print(f"monkey {idx}: {', '.join(map(str, monkey[0]))}")

x, y = sorted([*inspections.values()])[-2:]
print(x, y, x*y)
