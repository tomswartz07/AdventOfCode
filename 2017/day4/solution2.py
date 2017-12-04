#!/usr/bin/python

with open('input.txt') as f:
    data = f.readlines()

def passphrase(phrase):
    count = 0
    for line in phrase:
        anagrams = list(map(lambda x: ('').join(sorted(list(x))), line.split()))
        print(anagrams)
        if len(line.split()) == len(set(anagrams)):
            count += 1
    return count

print(passphrase(data))
