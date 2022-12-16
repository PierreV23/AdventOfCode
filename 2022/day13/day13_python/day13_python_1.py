from pathlib import Path
CURR_DIR = Path()

day_input_file = open(CURR_DIR / 'day13_input.txt')
# day_input_file = open(CURR_DIR / 'test.txt')

# day_input = day_input_file.readlines()
day_input = day_input_file.read()


def compare(a: int | list, b: int | list, *_) -> int:
    if isinstance(a, int) and isinstance(b, int):
        # return a-b #this method is smaller, but what i did below is more explicit
        k = a-b
        if k < 0:
            return -1
        elif k == 0:
            return 0
        elif k > 0:
            return 1

    elif isinstance(a, list) and isinstance(b, list):
        for x,y in zip(a, b):
            v = compare(x,y)
            if v:
                return v
        return len(a)-len(b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    else:
        raise Exception()

# \/\/ got this somewhere from stackoverflow, didnt use it anyway
# from collections.abc import Iterable
#
# def flatten(xs):
#     for x in xs:
#         if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
#             yield from flatten(x)
#         else:
#             yield x

valid = []
for idx, packet in enumerate(day_input.split("\n\n")):
    idx+=1
    try:
        a, b = packet.strip().split("\n")
    except:
        print(packet)
        raise Exception()
    a, b = a.strip(), b.strip()
    a, b = eval(a), eval(b)
    v = compare(a,b) < 0
    # flattened_a = flatten(a)
    # flattened_b = flatten(b)
    # if len([*flattened_b]) < len([*flattened_a]):
    #     v = False
    
    print(f"{idx} wowza {v}")
    if v:
        valid.append(idx)
print(sum(valid))

