def main():
    with open('day6_input.txt', 'r') as f:
        data = ''.join(line.strip('\n') for line in f)
    print([x + 4 for x in range(len(data)) if len(set(data[x:x + 4])) == 4][0])
# ^^^ van rutger


main()
# print(next(open('day6_input.txt')))
# [][0]
# d=next(open('i.txt'));print(next(x+4 for x in range(len(d)) if len(set(d[x:x+4]))==4))
# d=next(open('i.txt'));print([x+4 for x in range(len(d)) if len(set(d[x:x+4]))==4][0])
# n=next;d=n(open('i.txt'));print(n(x+4 for x in range(len(d)) if len(set(d[x:x+4]))==4))
# print(open('day6_input.txt')[0])
# d=next(open('day6_input.txt'));print((f:=lambda s,x=0:x+4 if len(set(d[x:x+4]))==4 else f(s,x+1))\
#         (open('day6_input.txt', 'r').readlines()[0].strip())\
# )


d=next(open('i'));print([x+4 for x in range(len(d)) if len(set(d[x:x+4]))==4][0])