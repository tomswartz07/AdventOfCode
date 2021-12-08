#!/usr/bin/python
from itertools import permutations
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().strip().split('\n')

# Number of Segments per display digit
# 'correct' mapping to actual segments
display = {
        '0': 'abcefg',
        '1': 'cf',
        '2': 'acdeg',
        '3': 'acdfg',
        '4': 'bcdf',
        '5': 'abdfg',
        '6': 'abdefg',
        '7': 'acf',
        '8': 'abcdefg',
        '9': 'abcdfg'
        }
display_r = {v:k for k, v in display.items()}
digit_sum = 0

for line in data:
    input_signal, output_signal = line.split('|')
    input_signal = [set(x) for x in input_signal.strip().split()]
    output_signal = [set(x) for x in output_signal.strip().split()]
    for p in permutations('abcdefg'):
        mapping = dict(zip(p, list('abcdefg')))
        for i in input_signal:
            digit = ''.join(sorted(mapping[x] for x in i))
            if digit not in display.values():
                break
        else:
            break
    digit_sum += int(
            ''.join(display_r[
            ''.join(sorted(mapping[x] for x in o))
            ]
        for o in output_signal)
        )
print(digit_sum)
