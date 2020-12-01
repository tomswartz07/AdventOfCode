#!/usr/bin/python

with open('input.txt', 'r') as f:
    data = f.read().rstrip('\n').split()
    data = [int(line) for line in data]

value = sorted(data)
valueset = set(data)
# Use set:
# https://docs.python.org/3.8/library/stdtypes.html#set
for i in value:
    for j in value[1:]:
        if 2020 - (i + j) in valueset:
            result = (i * j * (2020 - (i + j)))
print(result)
