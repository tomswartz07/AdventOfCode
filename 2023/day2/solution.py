#!/usr/bin/python
import re

total = 0
games = []

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for game in data:
        idx = int(re.search(r'Game (\d+)', game).group(1))
        maxReds = max(map(int, re.findall(r'(\d+) red', game)))
        maxBlues = max(map(int, re.findall(r'(\d+) blue', game)))
        maxGreens = max(map(int, re.findall(r'(\d+) green', game)))
        games.append((idx, maxReds, maxGreens, maxBlues))

for i in games:
    if i[1] <= 12 and i[2] <= 13 and i[3] <= 14:
        total += i[0]
print(total)
