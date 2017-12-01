#!/usr/bin/python

'''
Advent of Code
Day 5, Part 2
'''

from hashlib import md5

def find_code(door_id):
    '''
    Function to generate the Door Code Hashes
    '''
    s = [None] * 8
    i = 0
    while None in s:
        MD5SUM = md5(door_id + str(i).encode('utf-8')).hexdigest()
        if MD5SUM[:5] == '00000':
            location = int(MD5SUM[5], 16)
            #print("{}: {}".format(door_id + str(i).encode('utf-8'), MD5SUM[:4] + '\x1b[31m' + MD5SUM[5] + '\x1b[32m' + MD5SUM[6] + '\x1b[0m' + MD5SUM[7:]))
            if location in range(8) and s[location] is None:
                s[location] = MD5SUM[6]
        i += 1
        if i % 1000 == 0:
            faker = (''.join(MD5SUM[:8]))[:8]
            print("Door Code: {}".format(faker), end='\r')
    return ''.join(s)

SAMPLE_CODE = 'abc'.encode('utf-8')
print('Example Solution: {}'.format(find_code(SAMPLE_CODE)))

print('\n')

INPUT = 'wtnhxymk'.encode('utf-8')
print('Door Code: {}'.format(find_code(INPUT)))
