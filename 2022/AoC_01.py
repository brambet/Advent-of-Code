from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=1)

TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def calories_per_elve(puzzle_input: str) -> List[int]:
    return [
        sum([int(snack_calories) for snack_calories in elve_packet.split("\n")])
        for elve_packet in puzzle_input.split("\n\n")
    ]


def get_max_calories_on_elve(puzzle_input: str) -> int:
    return max(calories_per_elve(puzzle_input))


def get_top_three_calories(puzzle_input: str) -> int:
    return sum(sorted(calories_per_elve(puzzle_input), reverse=True)[:3])


if __name__ == "__main__":

    # test pt 1
    print(get_max_calories_on_elve(TEST_INPUT))

    # puzzle pt 1
    print(get_max_calories_on_elve(puzzle.input_data))

    # test pt 2
    print(get_top_three_calories(TEST_INPUT))

    # puzzle pt 2
    print(get_top_three_calories(puzzle.input_data))
