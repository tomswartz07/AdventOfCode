#!/usr/bin/python

with open('input.txt') as f:
    data = int(f.read().rstrip())

def spiral(value):
    # Start at center, zero distance
    x = y = dx = 0
    dy = -1
    step = 1

    while True:
        step += 1
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
        if value == step:
            return abs(x) + abs(y)

print(spiral(data))
