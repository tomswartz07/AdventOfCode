#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().rstrip('\n').split(",")
    data = [int(i) for i in data]

diffs = []
for dist in range(min(data), max(data) + 1):
    diffs.append(sum([abs(item - dist) for item in data]))
result = min(diffs)
print(result)
