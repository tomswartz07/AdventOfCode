#!/usr/bin/python
from collections import Counter

with open('input.txt', 'r') as f:
    code = f.read().strip('\n').split('-')

low, hi = [int(i) for i in code]
print("Testing between:", code[0], code[1])

count = 0
count2 = 0
nums = []

for i in range(low, hi):
    st = str(i)
    f1 = any([st[i] < st[i-1] for i in range(1, len(st))])
    f2 = any([st[i] == st[i-1] for i in range(1, len(st))])

    if f2 and not f1:
        nums.append(st)
        count += 1

for n in nums:
    if 2 in Counter(n).values():
        count2 += 1

print("Result is:", count2)
