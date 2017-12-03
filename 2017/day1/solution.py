#!/usr/bin/python

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n')

total = 0
buffer = int(values[len(values)-1])
for n in values:
    total += (1 - bool(buffer - int(n)))*int(n)
    buffer = int(n)
print(total)
