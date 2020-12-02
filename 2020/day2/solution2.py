#!/usr/bin/python
import re

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

valid = 0
for line in data:
    match = re.search("(\d+)-(\d+) ([a-zA-Z]): (.*)", line)
    pos1 = match.group(1)
    pos2 = match.group(2)
    char = match.group(3)
    password = match.group(4)
    if (password[int(pos1) - 1] == char) != (password[int(pos2) - 1] == char):
        valid += 1
print(valid)
