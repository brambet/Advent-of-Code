from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set
import numpy as np

# get puzzle
puzzle = Puzzle(year=2021, day=4)

TEST_INPUT = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class BingoBoard():

    @staticmethod
    def _get_line_numbers(line, i):
        return [int(line[0:2]), int(line[3:5]), int(line[6:8]), int(line[9:11]), int(line[12:14])]

    def __init__(self, board_string: str):
        self.board_string = board_string
        self.board = {int(number): (i, j) for i, line in enumerate(
            board_string.split('\n')) for j, number in enumerate(self._get_line_numbers(line, i))}

        self.row_counts = 5*[0]
        self.column_counts = 5*[0]

    def mark_number(self, number: int):
        row, column = self.board.pop(number, (None, None))
        if row is not None and column is not None:
            self.row_counts[row] += 1
            self.column_counts[column] += 1

        if self.board_wins():
            numbers_unmarked = sum(self.board.keys())
            return numbers_unmarked * number
        else:
            return False

    def board_wins(self):
        return any(count == 5 for count in self.row_counts + self.column_counts)

    def sum_of_remaining_numbers(self):
        return sum(self.board.keys())


def parse_input(input_text: str):
    number_string, *board_strings = input_text.split('\n\n')

    numbers = [int(number) for number in number_string.split(',')]

    bingo_boards = {BingoBoard(board_string) for board_string in board_strings}

    return numbers, bingo_boards


def play_bingo_game(numbers: List[int], boards: Set[BingoBoard]):
    for number in numbers:
        for board in bingo_boards:
            if (result := board.mark_number(number)):
                return result


def get_last_winnnig_board(numbers: List[int], boards: Set[BingoBoard]):
    for number in numbers:
        winning_boards = {board for board in boards if (
            board.mark_number(number))}

        if len(winning_boards) > 0:
            boards = boards - winning_boards

        if len(boards) == 0:
            last_board = winning_boards.pop()
            return last_board.sum_of_remaining_numbers()*number


if __name__ == '__main__':

    # test pt 1
    numbers, bingo_boards = parse_input(TEST_INPUT)
    print(play_bingo_game(numbers, bingo_boards))

    # pt 1
    numbers, bingo_boards = parse_input(puzzle.input_data)
    print(play_bingo_game(numbers, bingo_boards))

    # test pt 2
    numbers, bingo_boards = parse_input(TEST_INPUT)
    print(get_last_winnnig_board(numbers, bingo_boards))

    # pt 2
    numbers, bingo_boards = parse_input(puzzle.input_data)
    print(get_last_winnnig_board(numbers, bingo_boards))
