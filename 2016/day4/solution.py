#!/usr/bin/python

'''
Advent of Code
Day 4, Part 1
'''

import re
import collections
import string

SUM = 0
REGEX = r'([a-z-]+)(\d+)\[(\w+)\]'
with open('input.txt') as fp:
    for code, sid, checksum in re.findall(REGEX, fp.read()):
        sid = int(sid)
        letters = ''.join(c for c in code if c in string.ascii_lowercase)
        tops = [(-number, c) for c, number in collections.Counter(letters).most_common()]
        ranked = ''.join(c for number, c in sorted(tops))
        if ranked.startswith(checksum):
            SUM += sid

print(SUM)
