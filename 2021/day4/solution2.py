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
    "Returns bool if the board wins or not"
    winner = any(all(num in called_numbers for num in line) for line in [*board, *zip(*board)])
    return winner

def score(board, called_numbers, last_number):
    "Calculates score of board"
    board_score = last_number * sum(
            num for line in board for num in line if num not in called_numbers
            )
    return board_score

def find_score_of_last_bingo_winner(numbers, boards):
    "Find Score of last winning board"
    called_numbers = set()
    for num in numbers:
        called_numbers.add(num)
        if len(boards) == 1 and has_won(boards[0], called_numbers):
            return score(boards[0], called_numbers, num)
        boards = [board for board in boards if not has_won(board, called_numbers)]

print(find_score_of_last_bingo_winner(bingo_numbers, bingo_boards))
