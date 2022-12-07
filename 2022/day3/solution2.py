#!/usr/bin/python
with open('input.txt', 'r', encoding="utf-8") as f:
    indata = f.read().splitlines()


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def find_badge(group):
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()


def letter_values():
    letters = {}
    for letter_value in range(ord('a'), ord('z')+1):
        # subtract 96 to make a=1, b=2, etc.
        letters[chr(letter_value)] = letter_value - 96
    for letter_value in range(ord('A'), ord('Z')+1):
        # subtract 64 and add 26 to make A=27, B=28, etc.
        letters[chr(letter_value)] = letter_value - 64 + 26
    return letters


def part_two(data):
    badge_sum = 0
    letter_priority = letter_values()
    for group in chunker(data, 3):
        badge_sum += letter_priority[find_badge(group)]
    return badge_sum


def main():
    print(part_two(indata))


if __name__ == "__main__":
    main()

