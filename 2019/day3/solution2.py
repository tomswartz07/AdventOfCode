#!/usr/bin/python
from collections import defaultdict

with open('input.txt', 'r') as f:
    wires = f.read().splitlines()

points = defaultdict(list)
i = 0

for l in wires:
    movements = l.split(",")
    x = 0
    y = 0

    for m in movements:
        unit = int(m[1:])
        if   "R" in m:
            for u in range(1, unit+1):
                x += 1
                points[i].append((x, y))

        elif "L" in m:
            for u in range(1, unit+1):
                x -= 1
                points[i].append((x, y))


        elif "U" in m:
            for u in range(1, unit+1):
                y += 1
                points[i].append((x, y))


        elif "D" in m:
            for u in range(1, unit+1):
                y -= 1
                points[i].append((x, y))
    i = i + 1

result = set(points[0]) & set(points[1])
minx = min([points[0].index(point) + points[1].index(point) + 2 for point in result])
print("Result is:", minx)
