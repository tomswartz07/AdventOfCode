#!/usr/bin/python

def digits(data):
    for line in data:
        if line.strip():
            yield list(map(int, line.split()))

with open("input.txt") as f:
    checksum = sum(b-a for a, *_, b in map(sorted, digits(f)))
    print(checksum)
