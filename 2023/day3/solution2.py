#!/usr/bin/python
import re

SYMBOLS = set()
NUMBERS = {}
GEARS = {}
ratio_sum = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    LEN = len(data)
    for i, line in enumerate(data):
        matches = re.finditer(r'(\d+|[^.\n])', line)

        for match in matches:
            if not match.group().isdigit():
                SYMBOLS.add(i * LEN + match.start())
                if match.group() == '*':
                    GEARS[i * LEN + match.start()] = -1
            else:
                NUMBERS[(i * LEN + match.start(), i * LEN + match.end() - 1)] = int(match.group())
    for n in NUMBERS:
        for x in (n[0] - 1, n[1] + 1, *list(range(n[0] - 1 - LEN, n[1] + 2 - LEN)),
                  *list(range(n[0] - 1 + LEN, n[1] + 2 + LEN))):
            if x in GEARS:
                if GEARS[x] < 0:
                    GEARS[x] = NUMBERS[n]
                else:
                    ratio_sum += GEARS[x] * NUMBERS[n]

print(ratio_sum)
