#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    points = 0
    for line in data:
        left, right = line.split('|')
        left_nums = set(int(num) for num in left.split() if num.isdigit())
        right_nums = set(int(num) for num in right.split() if num.isdigit())
        # print(f"{sorted(left_nums)} | {sorted(right_nums)}")
        # print("Matches:", left_nums.intersection(right_nums))
        matches = len(left_nums.intersection(right_nums))
        # print(matches)
        if matches - 1 >= 0:
            points += 2 ** (matches - 1)
            # print(f"Adding: {2 ** (matches - 1) } points")
print(points)
