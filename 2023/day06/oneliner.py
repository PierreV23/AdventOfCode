from numpy import array, ceil, sqrt, sort
from math import prod
print(prod(len(range(*map(int, ceil(sort(abs((array([-sqrt(t**2-4*(d+1)), sqrt(t**2-4*(d+1))]) -t) / 2)))))) for t,d in zip(*[[int(''.join(line.split(':')[1].replace(' ', '')))] for line in open('input.txt').readlines()])))