#!/usr/bin/python

with open('input.txt') as f:
    data = f.readlines()

def passphrase(phrase):
    count = 0
    for line in phrase:
        if len(line.split()) == len(set(line.split())):
            count += 1
    return count

print(passphrase(data))
