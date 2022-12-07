#!/usr/bin/python
with open('input.txt', 'r', encoding="utf-8") as f:
    indata = f.read().splitlines()


def letter_values():
    letters = {}
    for letter_value in range(ord('a'), ord('z')+1):
        # subtract 96 to make a=1, b=2, etc.
        letters[chr(letter_value)] = letter_value - 96
    for letter_value in range(ord('A'), ord('Z')+1):
        # subtract 64 and add 26 to make A=27, B=28, etc.
        letters[chr(letter_value)] = letter_value - 64 + 26
    return letters


def part_one(data):
    letter_priority = letter_values()
    total_priority = 0
    for rucksack in data:
        half_item_count = int(len(rucksack)/2)
        compartment_one = rucksack[:half_item_count]
        compartment_two = rucksack[half_item_count:]
        matches = set()
        for item in compartment_one:
            if item in compartment_two:
                matches.add(item)
        for match in matches:
            total_priority += letter_priority[match]
    return total_priority


def main():
    print(part_one(indata))


if __name__ == "__main__":
    main()
