#!/usr/bin/python

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n')

total = 0
for n in range(0, len(values)):
    buffer = n - len(values) // 2
    if values[n] != values[buffer]:
        continue
    total += int(values[n])
print(total)
