#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().strip().split('\n')

# Number of Segments per display digit
# segs in 1, 4, 7, 8
digits = {2, 4, 3, 7}
digit_count = 0

for line in data:
    _, output_signal = line.split('|')
    output_signal = [set(x) for x in output_signal.strip().split()]
    digit_count += sum(1 for a in output_signal if len(a) in digits)
print(digit_count)
