#!/usr/bin/python

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n').split()

print(sum(map(int, values)))
