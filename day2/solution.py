#!/bin/python
'''
Advent of Code
Day 2, Part 1
'''

import sys

PAD = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
      ]

CURRENTLOCATION = (1, 1)  # start at '5'

INSTR = {"U": (0, -1), "D": (0, 1),
         "L": (-1, 0), "R": (1, 0),
        }

for line in sys.stdin:
    for d in line.strip():
        CURRENTLOCATION = (max(0, min(CURRENTLOCATION[0] + INSTR[d][0], 2)),
                           max(0, min(CURRENTLOCATION[1] + INSTR[d][1], 2)))
    print(PAD[CURRENTLOCATION[1]][CURRENTLOCATION[0]])
