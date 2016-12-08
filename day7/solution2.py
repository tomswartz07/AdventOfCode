#!/usr/bin/python

'''
Advent of Code
Day 7, Part 2
'''

import re

TLS = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
HYPERNET = re.compile(r'\[.*?\]')
SSL = re.compile(r'(?=((.)(?!\2)(.)\2))')
COUNTER = 0
with open('input.txt') as fd:
    for line in fd:
        possible = [m[0] for m in re.findall(SSL, line)]
        pairs = [(p1, p1[1]+p1[0]+p1[1]) for p1 in possible if p1[1]+p1[0]+p1[1] in possible]
        if [pair for pair in pairs if pair[0] in
                HYPERNET.sub('|', line) and pair[1] in ''.join(re.findall(HYPERNET, line))]:
            COUNTER += 1
print('Number of Valid IPs with SSL: {}'.format(COUNTER))
