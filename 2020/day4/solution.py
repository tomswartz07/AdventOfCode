#!/usr/bin/python
import re

with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')

fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
total = 0

for i in data:
    check = [field in i for field in fields]
    if all(check):
        total += 1

print(total)
