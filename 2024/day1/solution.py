#!/usr/bin/python

left, right = [], []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()
sum_of_diffs = sum(abs(a - b) for a, b in zip(left, right))

print(f"Part 1: {sum_of_diffs}")
