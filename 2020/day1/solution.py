#!/usr/bin/python

with open('input.txt', 'r') as f:
    data = f.read().rstrip('\n').split()
    data = [int(line) for line in data]

# Use set:
# https://docs.python.org/3.8/library/stdtypes.html#set
values = set(data)
for i in values:
    if 2020 - i in values:
        print("Value:", i)
        result = (i * (2020 - i))
print(result)
