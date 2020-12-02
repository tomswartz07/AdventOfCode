#!/usr/bin/python
import re

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

valid = 0
for line in data:
    match = re.search("(\d+)-(\d+) ([a-zA-Z]): (.*)", line)
    minimum = match.group(1)
    maximum = match.group(2)
    char = match.group(3)
    password = match.group(4)
    if int(minimum) <= password.count(char) <= int(maximum):
        valid += 1
print(valid)
