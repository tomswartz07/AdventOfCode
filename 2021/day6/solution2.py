#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().split(",")
    data = [int(line) for line in data]

def population(newIn, days):
    n = [newIn.count(i) for i in range(9)]
    for _ in range(days):
        z = n[0]
        n[0:8] = n[1:9]
        n[6] += z
        n[8] = z
    return sum(n)

print(population(data,256))
