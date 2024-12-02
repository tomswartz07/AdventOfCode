#!/usr/bin/python
from collections import Counter

left, right = [], []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

count_right = Counter(right)
similarity_score = sum(a * count_right[a] for a in left)

print(f"Part 2: {similarity_score}")
