#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().rstrip('\n').split()
    data = [int(line) for line in data]

count = 0
for i in range(len(data) - 1):
    if data[i] < data[i+1]:
        count += 1
print(f"{count} total")
