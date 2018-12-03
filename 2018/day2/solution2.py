#!/usr/bin/python

with open('input.txt', 'r') as f:
    values = f.read().splitlines()

for line1 in values:
    for line2 in values:
        common = ""
        for a, b in zip(line1, line2):
            if a == b:
                #print(a, b, common)
                common += a
        if len(common) == len(line1) - 1:
            print("Result: ", common)
