#!/usr/bin/python

'''
Advent of Code
Day 5, Part 1
'''

from hashlib import md5

def find_code(door_id):
    '''
    Function to generate the Door Code Hashes
    '''
    i = 0
    code = ''
    while len(code) < 8:
        MD5SUM = md5(door_id + str(i).encode('utf-8')).hexdigest()
        if MD5SUM[:5] == '00000':
            print("{}: {}".format(door_id + str(i).encode('utf-8'), MD5SUM[:4] + '\x1b[31m' + MD5SUM[5] + '\x1b[0m' + MD5SUM[6:]))
            code += MD5SUM[5]
        i += 1
    return code

SAMPLE_CODE = 'abc'.encode('utf-8')
print('\nExample Solution: {}'.format(find_code(SAMPLE_CODE)[:8]))
INPUT = 'wtnhxymk'.encode('utf-8')
print('\nDoor Code: {}'.format(find_code(INPUT)))
