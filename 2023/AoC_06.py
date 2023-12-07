from __future__ import annotations

import re
from dataclasses import dataclass
from math import ceil, floor
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# import sympy
from sympy import solve, symbols

# get puzzle
puzzle = Puzzle(year=2023, day=6)

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


def final_distance(push_T: int, total_T: int) -> int:
    return push_T * (total_T - push_T)


def number_of_strategies(T_race: int, s_record: int) -> int:
    t = symbols('t')
    # be at least record +  1, strict better
    solutions = solve(t * (T_race - t) - s_record - 1, t, dict=True)
    t1, t2 = t.subs(solutions[0]), t.subs(solutions[1])
    return floor(max(t1, t2)) - ceil(min(t1, t2)) + 1


def parse_race_sheet(input_str: str) -> Tuple[List[int], List[int]]:
    times, records = input_str.split('\n')
    return map(int, re.findall(r'\d+', times)), map(int, re.findall(r'\d+', records))


def parse_race_sheet_two(input_str: str) -> Tuple[int, int]:
    times, records = input_str.split('\n')
    time = int("".join(re.findall(r'\d+', times)))
    record = int("".join(re.findall(r'\d+', records)))
    return time, record


def part_one(input_str: str) -> int:
    times, records = parse_race_sheet(input_str)
    return np.prod([number_of_strategies(race_time, record) for race_time, record in zip(times, records)])


def part_two(input_str: st) -> int:
    race_time, record = parse_race_sheet_two(input_str)
    return number_of_strategies(race_time, record)


if __name__ == "__main__":
    # # test pt 1
    print(part_one(TEST_INPUT))

    # # pt 1
    print(part_one(puzzle.input_data))

    # # test pt 2
    print(part_two(TEST_INPUT))

    # # pt 2
    print(part_two(puzzle.input_data))
