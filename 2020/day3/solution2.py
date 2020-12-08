#!/usr/bin/python
import math

with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')

def gen(data: list, slope: tuple) -> int:
    trees = 0
    right, down = (0, 0)
    while down < len(data):
        if data[down][right % len(data[0])] == '#':
            trees += 1
        right += slope[0]
        down += slope[1]
    return trees

def solution(data: list, slopes: tuple) -> int:
    return math.prod(gen(data, slope) for slope in slopes)

def main():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(solution(data, slopes))


if __name__ == '__main__':
    main()
