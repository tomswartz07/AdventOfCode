#!/usr/bin/python
import itertools

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n').split()

freq = 0
seen = {0}
# https://docs.python.org/3/library/itertools.html#itertools.cycle
for num in itertools.cycle(values):
    print(num)
    freq += int(num)
    if freq in seen:
        print("Result: ", freq)
        break
    seen.add(freq)
