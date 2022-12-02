from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day2_input.txt')
day_input = day_input_file.readlines()
# day_input = day_input_file.read()

# Key wins of Value
WINNER_TABLE = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

EXTRA_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3
}

score = 0
for line in day_input:
    move_opponent, move_self = line.strip().split()
    move_self = "".join({'X': 'A', 'Y': 'B', 'Z': 'C'}[i] for i in move_self)
    if move_opponent == move_self:
        score += 3
    elif WINNER_TABLE[move_self] == move_opponent:
        score += 6
    
    score += EXTRA_POINTS[move_self]
print(score)
