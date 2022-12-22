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

filename = 'day{day}_input.txt'
# filename = 'day{day}_test.txt'
file = open(CURR_DIR / filename)
lines = open(CURR_DIR / filename).readlines()
whole = open(CURR_DIR / filename).read()
chunks = whole.split("\\n\\n")
def p1():
    ...

def p2():
    ...


print(p1())
print(p2())
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
    
    # day_folder = CURR_DIR / f'day{day}'
    # day_folder.mkdir(exist_ok=True)
    day_folder = CURR_DIR / f'day{day}'
    day_folder.mkdir(exist_ok=True)
    if inp == 'python':
        if not (f := day_folder / f'day{day}_python.py').exists():
            with open(f, 'w') as file:
                file.write(templates['python'])
    else:
        #  day_folder /= f'{inp}'
        ...
    with open(day_folder / f'day{day}_input.txt', 'w') as file:
        res = session.get(f'https://adventofcode.com/2022/day/{day}/input')
        file.write(res.text)
print("Exiting")