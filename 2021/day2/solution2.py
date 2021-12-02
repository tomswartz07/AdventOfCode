#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = [{line.strip().split(" ")[0]:int(line.strip().split(" ")[1])} for line in f]

hrange, depth, aim = 0, 0, 0

for line in data:
    for direction, distance in line.items():
        if direction in 'forward':
            hrange += distance
            depth += aim * distance
        elif direction in 'down':
            aim += distance
        elif direction in 'up':
            aim -= distance
print(hrange * depth)
