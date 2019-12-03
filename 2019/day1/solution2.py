#!/usr/bin/python
import math

with open('input.txt', 'r') as f:
    values = f.read().rstrip('\n').split()

result = 0

for i in values:
    mass = int(i)
    fuel = (math.trunc(mass/3))-2
    fuelTotal = fuel
    while fuel > 0:
        fuel = (math.trunc(fuel/3))-2
        if fuel > 0:
            fuelTotal = fuelTotal + fuel
    result = result + fuelTotal
print("Total fuel requirement:", result)
