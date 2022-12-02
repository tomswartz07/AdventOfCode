#!/usr/bin/python
with open('input.txt', 'r', encoding="utf-8") as f:
    indata = f.read().splitlines()


def part_one(data):
    '''
    A = Rock 1 point
    B = Paper 2 points
    C = Scissors 3 points
    X (lose) = 0 points
    Y (draw) = 3 points
    Z (win) = 6 points
    '''
    guide = {'A X': 3 + 0, 'A Y': 1 + 3, 'A Z': 2 + 6,
             'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
             'C X': 2 + 0, 'C Y': 3 + 3, 'C Z': 1 + 6
             }
    return sum(guide[rnd] for rnd in data)


def main():
    print(part_one(indata))


if __name__ == "__main__":
    main()
