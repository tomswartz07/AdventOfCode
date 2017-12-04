#!/usr/bin/python

with open('input.txt') as f:
    data = int(f.read().rstrip())

coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

def spiralmath(goal):
    x = y = dx = 0
    dy = -1
    grid = {}

    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if (x+ox, y+oy) in grid:
                total += grid[(x+ox, y+oy)]
        if total > goal:
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

print(spiralmath(data))
