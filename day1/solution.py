#!/usr/bin/python

import sys

CurrentDirection = 0  # facing north
Location = {'x': 0, 'y': 0}

Factors = [{'x': 0, 'y': 1},   # turning right, N
           {'x': 1, 'y': 0},   # E
           {'x': 0, 'y': -1},  # S
           {'x': -1, 'y': 0}   # W
           ]
Facing = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x+4-1) % 4
        }

for line in sys.stdin:
    for turn in [x.strip() for x in line.split(',')]:
        d, c = turn[0], int(turn[1:])
        CurrentDirection = Facing[d](CurrentDirection)
        Location['x'] += Factors[CurrentDirection]['x'] * c
        Location['y'] += Factors[CurrentDirection]['y'] * c

print('Disatance Travelled: %d' % (abs(Location['x']) + abs(Location['y'])))
