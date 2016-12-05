#!/usr/bin/python

'''
Advent of Code
Day 3, Part 2
'''

import sys
from itertools import zip_longest

TOTAL = 0
TRIPLETS = [[int(x) for x in line.split()] for line in sys.stdin]

ARGS = [iter(TRIPLETS)] * 3
for x in zip_longest(*ARGS):
    for tri in zip(*x):
        tri = sorted(tri)
        if tri[0] + tri[1] > tri[2]:
            TOTAL += 1

print(TOTAL)
