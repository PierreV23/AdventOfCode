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

LOSER_TABLE = {k:v for v, k in WINNER_TABLE.items()}

EXTRA_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3
}

score = 0
for line in day_input:
    move_opponent, action = line.strip().split()
    if action == 'X':
        move_self = WINNER_TABLE[move_opponent]
    elif action == 'Y':
        move_self = move_opponent
    elif action == 'Z':
        move_self = LOSER_TABLE[move_opponent]
    else:
        raise Exception()
    
    if move_opponent == move_self:
        score += 3
    elif WINNER_TABLE[move_self] == move_opponent:
        score += 6
    
    score += EXTRA_POINTS[move_self]
print(score)
