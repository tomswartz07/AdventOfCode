#!/usr/bin/python
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    sums = []
    acc = 0
    for line in data:
        line = line.strip()
        if line:
            acc += int(line)
        else:
            sums.append(acc)
            acc = 0
    sums.append(acc)
    print(sum(sorted(sums)[-3:]))
