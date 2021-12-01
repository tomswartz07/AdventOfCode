#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().rstrip('\n').split()
    data = [int(line) for line in data]

count = 0
for i in range(len(data) - 3):
    window1 = data[i] + data[i+1] + data[i+2]
    window2 = data[i+1] + data[i+2] + data[i+3]
    if window2 > window1:
        count += 1
print(f"{count} total")
