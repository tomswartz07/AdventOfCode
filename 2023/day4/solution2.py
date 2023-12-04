#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    total_cards = 0
    winning_cards = {}
    for idx, line in enumerate(data):
        left, right = line.split('|')
        left_nums = set(int(num) for num in left.split() if num.isdigit())
        right_nums = set(int(num) for num in right.split() if num.isdigit())
        matches = len(left_nums.intersection(right_nums))
        winning_cards[idx + 1] = [matches, 1]
    for i in range(1, len(data) + 1):
        points, nr = winning_cards[i]
        total_cards += nr
        for j in range(i + 1, i + 1 + points):
            winning_cards[j][1] += nr
print(total_cards)
