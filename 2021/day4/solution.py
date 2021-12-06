#!/usr/bin/python

with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()

bingo_numbers = [int(num) for num in data.pop(0).split(",")]

assert len(data) % 6 == 0
n_boards = len(data) // 6

bingo_boards = [
        [[int(num) for num in line.split()] for line in data[6 * i + 1 : 6 * (i +1)]]
        for i in range(n_boards)
        ]


def has_won(board, called_numbers):
    winner = any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])
    return winner

def score(board, called_numbers, last_number):
    board_score = last_number * sum(num for line in board for num in line if num not in called_numbers)
    return board_score

def find_score_of_first_bingo_winner(numbers, boards):
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        for board in boards:
            if has_won(board, called_numbers):
                return score(board, called_numbers, num)

print(find_score_of_first_bingo_winner(bingo_numbers, bingo_boards))
