#!/usr/bin/python

'''
Advent of Code
Day 7, Part 1
'''

import re

TLS = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
HYPERNET = re.compile(r'\[.*?\]')
COUNTER = 0
with open('input.txt') as fd:
    for line in fd:
        valid = bool(re.search(TLS, line))
        for match in re.finditer(HYPERNET, line):
            valid = valid and not bool(re.search(TLS, match.group()))
        if valid:
            COUNTER += 1
print('Number of Valid IPs: {}'.format(COUNTER))
