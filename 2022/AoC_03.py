import string
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=3)

TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


def get_priority(x: str):
    if x.isupper():
        return ord(x) - ord("A") + 27
    else:
        return ord(x) - ord("a") + 1


def part_one(puzzle_input: str):

    rugsacks = [
        (set(rugsack[: int(len(rugsack) / 2)]), set(rugsack[int(len(rugsack) / 2) :]))
        for rugsack in puzzle_input.split("\n")
    ]

    double_items = [rugsack[0].intersection(rugsack[1]).pop() for rugsack in rugsacks]
    # print(double_items)
    priorities = [get_priority(x) for x in double_items]
    # print(priorities)
    return sum(priorities)


def get_groups(puzzle_input: str) -> List[Set[str]]:
    rugsacks = [set(rugsack) for rugsack in puzzle_input.split("\n")]
    rugsack_groups = [rugsacks[idx : idx + 3] for idx in range(0, len(rugsacks), 3)]
    return rugsack_groups


def get_rugsack_intersections(rugsack_groups: List[List[set[str]]]) -> List[str]:
    return [set.intersection(*rugsack_group).pop() for rugsack_group in rugsack_groups]


def part_two(puzzle_input):
    rugsack_groups = get_groups(puzzle_input)
    rugsack_intersections = get_rugsack_intersections(rugsack_groups)
    intersection_priorities = [get_priority(item) for item in rugsack_intersections]
    return sum(intersection_priorities)


if __name__ == "__main__":

    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # pt 2 test
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
