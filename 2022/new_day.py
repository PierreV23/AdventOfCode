from datetime import datetime

day = datetime.now().date().day

templates = {
    "python":\
f"""
from pathlib import Path
CURR_DIR = Path()

day_input_file = file.open(CURR_DIR / 'day{day}_input.txt')
# day_input = day_input_file.readlines()
# day_input = day_input_file.read()
"""
}

print("What languages do you want?")
while (inp := input().lower()):
    if inp == 'python':
        ...
    elif inp == 'rust':
        ...
    else:
        print("Invalid language")