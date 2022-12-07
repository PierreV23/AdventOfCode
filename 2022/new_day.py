from datetime import datetime
from pathlib import Path
import requests
import os

CURR_DIR = Path()

day = datetime.now().date().day

templates = {
    "python":\
f"""
from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day{day}_input.txt')
# day_input = day_input_file.readlines()
# day_input = day_input_file.read()
"""
}
languages = [
    'python',
    'rust'
]

session = requests.Session()
session.cookies.set( # type: ignore
    name = 'session',
    value = os.environ['AOC_SESSION_COOKIE'],
    domain = 'adventofcode.com'
)

print("What languages do you want?")
while (inp := input().lower()):
    if inp not in languages:
        print("Invalid language")
        continue
    elif inp == "\n":
        break
    
    day_folder = CURR_DIR / f'day{day}'
    day_folder.mkdir(exist_ok=True)
    if inp == 'python' and not (lang_folder := day_folder / f'day{day}_{inp}').exists():
        lang_folder.mkdir(exist_ok=True)
        for i in (1, 2):
            with open(lang_folder / f'day{day}_{inp}_{i}.py', 'w') as file:
                file.write(templates['python'])
    else:
        ...
    with open(lang_folder / f'day{day}_input.txt', 'w') as file:
        res = session.get(f'https://adventofcode.com/2022/day/{day}/input')
        file.write(res.text)
print("Exiting")