#!/usr/bin/python
import math

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n').split()

result = 0

for i in values:
    mass = int(i)
    fuel = (math.trunc(mass/3))-2
    print(fuel)
    result = result + fuel
print("Total fuel requirement:", result)
