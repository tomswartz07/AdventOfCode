#!/usr/bin/python
import re

pattern = r'(\d)'
digits = re.compile(pattern)
total = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for item in data:
        numbers = digits.findall(item)
        first = numbers[0]
        last = numbers[-1]
        total += int(f'{first}{last}')
print(total)
