#!/usr/bin/python

import sys

CurrentDirection = 0
Location = {'x': 0, 'y': 0}
All = []

Factors = [{'x': 0, 'y': 1},
           {'x': 1, 'y': 0},
           {'x': 0, 'y': -1},
           {'x': -1, 'y': 0}
           ]
Facing = {'R': lambda x: (x+1) % 4,
        'L': lambda x: (x+4-1) % 4
        }

for line in sys.stdin:
    for turn in [x.strip() for x in line.split(',')]:
        d, c = turn[0], int(turn[1:])
        CurrentDirection = Facing[d](CurrentDirection)
        for _ in range(c):
            Location['x'] += Factors[CurrentDirection]['x']
            Location['y'] += Factors[CurrentDirection]['y']
            encode = '%d|%d' % (Location['x'], Location['y'])
            if encode in All:
                print('Distance: %d' % (abs(Location['x']) + abs(Location['y'])))
                sys.exit(0)
            All.append(encode)
