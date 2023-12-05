from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=4)

TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def part_one(puzzle_input: str) -> int:
    pairs = [line.split(",") for line in puzzle_input.split("\n")]
    pairs_start_stop = [
        [[int(x) for x in assignment.split("-")] for assignment in pair]
        for pair in pairs
    ]
    pairs_ranges = [
        [set(range(start_stop[0], start_stop[1] + 1)) for start_stop in pair]
        for pair in pairs_start_stop
    ]
    is_subset = [pair[0] <= pair[1] or pair[1] <= pair[0] for pair in pairs_ranges]
    return sum(is_subset)


def part_two(puzzle_input: str) -> int:
    pairs = [line.split(",") for line in puzzle_input.split("\n")]
    pairs_start_stop = [
        [[int(x) for x in assignment.split("-")] for assignment in pair]
        for pair in pairs
    ]
    pairs_ranges = [
        [set(range(start_stop[0], start_stop[1] + 1)) for start_stop in pair]
        for pair in pairs_start_stop
    ]
    overlaps = [len(pair[0].intersection(pair[1])) > 0 for pair in pairs_ranges]
    return sum(overlaps)


if __name__ == "__main__":

    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
