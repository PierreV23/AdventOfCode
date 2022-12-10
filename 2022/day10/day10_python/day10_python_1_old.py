from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day10_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()
# day_input = [
#     "noop",
#     "addx 3",
#     "addx -5"
# ]
cycle_counter = 0
total_cycles = 0
x_register = 1
signal_strengths = []
line_number = 0
pipe = []
while line_number < len(day_input):
    if cycle_counter:
        total_cycles += 1
        cycle_counter -= 1
        if cycle_counter == 0:
            if pipe:
                dest, func = pipe.pop()
                if dest:
                    locals()[dest] = func()
            line_number += 1
    
    if (total_cycles - 20) % 40 == 0:
        print(f"{total_cycles}th * {x_register} ; {line_number}")
        signal_strengths.append((total_cycles, x_register))
        # total_cycles = 0
        # x_register = 1
        # print(total_cycles, cycle_counter, x_register)

    
    if line_number >= len(day_input):
        break

    if not cycle_counter:
        line = day_input[line_number]
        instruction, *data = line.rstrip('\n').split()
        match instruction:
            case 'noop':
                cycle_counter += 1
            case 'addx':
                cycle_counter += 2
                pipe.append(
                    ("x_register",
                    lambda: x_register + int(data[0]))
                )
    
    # print(total_cycles, cycle_counter, x_register)
ans = 0
for idx, (a, b) in enumerate(signal_strengths):
    if idx == len(signal_strengths) - 1:
        b -= 1
    ans += a * b

print(ans)

