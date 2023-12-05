import re
from collections import deque
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import regex
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=1)

TEST_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


TEST_INPUT2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def part_one(input_str: str) -> int:
    total = 0
    for line in input_str.split('\n'):
        line_numbers = [char for char in line if char.isdigit()]
        total += int(line_numbers[0] + line_numbers[-1])

    return total


NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "10",
}

pattern = r'({}|\d)'.format('|'.join(NUMBER_MAPPING.keys()))


def get_line_number_pt2(line_str: str) -> int:
    matches = regex.findall(pattern, line_str, overlapped=True)
    return int(''.join([matches[idx] if matches[idx].isdigit() else NUMBER_MAPPING[matches[idx]] for idx in [0, -1]]))


def part_two(input_str: str) -> int:
    return sum([get_line_number_pt2(line_str) for line_str in input_str.split("\n")])


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT2))

    # pt 2
    print(part_two(puzzle.input_data))
