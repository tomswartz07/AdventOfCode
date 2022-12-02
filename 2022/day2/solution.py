#!/usr/bin/python
with open('input.txt', 'r', encoding="utf-8") as f:
    indata = f.read().splitlines()


def part_one(data):
    '''
    A, X = Rock 1 point
    B, Y = Paper 2 points
    C, Z = Scissors 3 points
    win = 6 points
    lose = 0 points
    draw = 3 points
    '''
    guide = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
             'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
             'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3
             }
    return sum(guide[rnd] for rnd in data)


def main():
    print(part_one(indata))


if __name__ == "__main__":
    main()
