from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=6)

TEST_INPUT = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
TEST_INPUT2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
TEST_INPUT3 = "nppdvjthqldpwncqszvftbrmjlhg"


def part_one(puzzle_input: str):
    for idx, char in enumerate(puzzle_input[3:]):
        if len(set(puzzle_input[idx - 3 : idx + 1])) == 4:
            return idx + 1


def part_two(puzzle_input: str):
    for idx, char in enumerate(puzzle_input[13:]):
        if len(set(puzzle_input[idx - 13 : idx + 1])) == 14:
            return idx + 1


if __name__ == "__main__":

    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2 does not work??
    print(part_two(TEST_INPUT3))

    # pt 2 but this produces the correct answer??
    print(part_two(puzzle.input_data))
