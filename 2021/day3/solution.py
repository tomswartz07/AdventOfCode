#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()

counter = [0 for i in range(len(data[0].strip()))]
for line in data:
    for i,c in enumerate(line.strip()):
        if c == '0':
            counter[i] += 1

gamma,epsilon = 0,0
for i in range(len(counter)):
    if counter[i] > len(data)/2:
        epsilon += 2**(len(counter)-1 - i)
    else:
        gamma += 2**(len(counter)-1 - i)

print("Final:",gamma*epsilon)
