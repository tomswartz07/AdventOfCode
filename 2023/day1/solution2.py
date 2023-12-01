#!/usr/bin/python
import re

pattern = r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))'
digits = re.compile(pattern)
mapper = {'zero': 0, 'one': 1, 'two': 2,
          'three': 3, 'four': 4, 'five': 5,
          'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
          }
total = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for item in data:
        numbers = digits.findall(item)
        first, last = numbers[0], numbers[-1]
        if mapper.get(first):
            first = mapper[first]
        if mapper.get(last):
            last = mapper[last]
        total += int(f'{first}{last}')
print(total)
