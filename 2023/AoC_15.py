from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=15)

TEST_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


def hash_algorithm(input_str: str) -> int:
    current_value = 0
    for character in input_str:
        current_value += ord(character)
        current_value *= 17
        current_value = current_value % 256

    return current_value


def part_one(input_str: str) -> int:
    return sum([hash_algorithm(step.strip()) for step in input_str.split(',')])


# class Lens


@dataclass
class LensBoxes:
    boxes: Dict[int, List[Tuple[str, int]]]

    def parse_instructions(input_str: str) -> LensBoxes:
        boxes = {}
        for instruction in input_str.spit(','):
            if instruction.endswith('-'):
                label = instruction[:-1]
                box = hash_algorithm(label)

            else:
                label


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # # test pt 2
    # print(part_two(TEST_INPUT))

    # # pt 2
    # print(part_two(puzzle.input_data))
