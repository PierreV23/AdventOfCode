from pathlib import Path
CURR_DIR = Path()

print([*CURR_DIR.iterdir()])

with open(CURR_DIR / 'TXT.txt', 'r') as file:
    print(sum(sorted([sum(map(int, i.split())) for i in file.read().split("\n\n")])[-3:]))