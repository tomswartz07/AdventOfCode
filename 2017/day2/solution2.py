#!/usr/bin/python
import itertools

def evens(rows):
    for row in rows:
        for a, b in itertools.combinations(sorted(row), 2):
            if b % a == 0:
                yield a, b

def digits(data):
    for line in data:
        if line.strip():
            yield list(map(int, line.split()))

with open("input.txt") as f:
    checksum = sum(b//a for a, b in evens(digits(f)))
    print(checksum)
