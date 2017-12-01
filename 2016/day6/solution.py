#!/usr/bin/python

'''
Advent of Code
Day 6, Part 1
'''

from collections import Counter

with open('test.txt') as fd:
    TEST = fd.read().strip()

with open('input.txt') as f:
    DATA = f.read().strip()

def count_data(counter_data):
    '''
    Function to calculate most common char in input
    '''
    data_counted = [Counter(x).most_common() for x in zip(*counter_data.split('\n'))]
    message = ''.join(x[0][0] for x in data_counted)
    return message

print('Validation: {}\nMessage: {}'.format(count_data(TEST), count_data(DATA)))
