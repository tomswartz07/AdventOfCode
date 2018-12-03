#!/usr/bin/python

with open('input.txt', 'r') as f:
    values = f.readlines()

two = 0
three = 0
for checksum in values:
    #print(checksum)
    two_done = False
    three_done = False
    for char in set(checksum):
        #print(char)
        if checksum.count(char) == 2 and not two_done:
            #print("two")
            two_done = True
            two += 1
        if checksum.count(char) == 3 and not three_done:
            #print("three")
            three_done = True
            three += 1
print(two * three)
