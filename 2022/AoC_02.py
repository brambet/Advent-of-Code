from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=2)

TEST_INPUT = """A Y
B X
C Z"""

move_mapping = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}


def game_round_score(opponent_move: int, move: int) -> int:
    match (opponent_move, move):
        case (1, 1) | (2, 2) | (3, 3):
            return 3
        case (2, 1) | (3, 2) | (1, 3):
            return 0
        case (1, 2) | (2, 3) | (3, 1):
            return 6


def game_total_score(puzzle_input: str) -> int:
    game_moves = [
        [move_mapping[move] for move in line.split(" ")]
        for line in puzzle_input.split("\n")
    ]
    game_scores = [
        game_round_score(*round_moves) + round_moves[1] for round_moves in game_moves
    ]
    return sum(game_scores)


def part_2_move_score(opponent_move: int, objective: int) -> int:
    match (opponent_move, objective):
        case (1, 1):
            # opp plays rock, lose with scissors (3)
            return 0 + 3
        case (1, 2):
            # opp plays rock, draw with rock (1)
            return 3 + 1
        case (1, 3):
            # opp plays rock, win with paper (2)
            return 6 + 2
        case (2, 1):
            # opp plays paper, lose with rock (1)
            return 0 + 1
        case (2, 2):
            # opp plays paper, draw with paper (2)
            return 3 + 2
        case (2, 3):
            # opp plays paper, win with scissors (3)
            return 6 + 3
        case (3, 1):
            # opp plays scissors, lose with paper (2)
            return 0 + 2
        case (3, 2):
            # opp plays scissors, draw with scissors (3)
            return 3 + 3
        case (3, 3):
            # opp plays scissors, win with rock (1)
            return 6 + 1


def part_two_total(puzzle_input: str) -> int:
    game_moves = [
        [move_mapping[move] for move in line.split(" ")]
        for line in puzzle_input.split("\n")
    ]
    game_scores = [part_2_move_score(*round_moves) for round_moves in game_moves]
    # print(game_scores)
    return sum(game_scores)


if __name__ == "__main__":

    # test pt 1
    print(game_total_score(TEST_INPUT))

    # pt 1
    print(game_total_score(puzzle.input_data))

    # test pt 2
    print(part_two_total(TEST_INPUT))

    # pt 2
    print(part_two_total(puzzle.input_data))
