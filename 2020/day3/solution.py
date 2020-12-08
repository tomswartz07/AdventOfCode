#!/usr/bin/python

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

def solution(maps: list, slope: tuple) -> int:
    trees = 0
    right,down = (0,0)
    while down < len(maps):
        if data[down][right % len(maps[0])] == '#':
            trees += 1
        right += slope[0]
        down += slope[1]
    return trees

def main():
    slope = (3, 1)
    print(solution(data,slope))


if __name__ == '__main__':
    main()
