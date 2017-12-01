#!/usr/bin/python

'''
Advent of Code
Day 4, Part 2
'''

import re
import collections
import string

def caesar_cipher(number):
    '''
    Function to rotate the chars and decode the string
    '''
    az = string.ascii_lowercase
    x = number % len(az)
    return str.maketrans(az, az[x:] + az[:x])

REGEX = r'([a-z-]+)(\d+)\[(\w+)\]'
with open('input.txt') as fp:
    for code, sid, checksum in re.findall(REGEX, fp.read()):
        sid = int(sid)
        letters = ''.join(c for c in code if c in string.ascii_lowercase)
        tops = [(-number, c) for c, number in collections.Counter(letters).most_common()]
        ranked = ''.join(c for number, c in sorted(tops))
        if ranked.startswith(checksum):
            decoded = code.translate(caesar_cipher(sid))
            if 'north' in decoded:
                print(decoded + str(sid))
