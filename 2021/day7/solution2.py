#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read().rstrip('\n').split(",")
    data = [int(i) for i in data]

diffs = []
def geo_sum(num: int):
    "Pre-compute sum of movements"
    return sum(i for i in range(num + 1))

# Create Look Up Table for the sums
geo_sum_lookup = {i: geo_sum(i) for i in range(min(data), max(data) + 1)}
#print(geo_sum_lookup)

for dist in range(min(data), max(data) + 1):
    diffs.append(
            sum(
                [geo_sum_lookup[abs(item-dist)] for item in data]
                )
            )
result = min(diffs)
print(result)
