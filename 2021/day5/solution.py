#!/usr/bin/python

# https://docs.python.org/3.8/library/stdtypes.html#set

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()

lines = [[int(num) for xy in line.split(" -> ") for num in xy.split(",")] for line in data]

def get_vent_locations(x1, y1, x2, y2):
    "Geometry, babey"
    dx = int(x2 > x1) - int(x2 < x1)
    dy = int(y2 > y1) - int(y2 < y1)
    line_points = [(x1 + n * dx, y1 + n * dy) for n in range(max(abs(x2 - x1), abs(y2 - y1)) + 1)]
    return line_points

def find_overlaps(vent_lines):
    "Uses set() to build overlaps"
    vent_locations = set()
    overlaps = set()
    for line in vent_lines:
        for x, y in get_vent_locations(*line):
            if (x, y) in vent_locations:
                overlaps.add((x, y))
            else:
                vent_locations.add((x,y))
    return overlaps

def vert_line(x1, y1, x2, y2):
    "Determines if line is vert or horiz"
    return x1 == x2 or y1 == y2

def find_line_overlaps(vent_lines):
    "Uses set() to build list of overlapping lines"
    vent_locations = set()
    overlaps = set()
    for line in vent_lines:
        for x, y in get_vent_locations(*line):
            if (x, y) in vent_locations:
                overlaps.add((x, y))
            else:
                vent_locations.add((x, y))
    return overlaps

print(len(find_line_overlaps([l for l in lines if vert_line(*l)])))
