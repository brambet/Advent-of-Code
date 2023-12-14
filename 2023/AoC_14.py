from __future__ import annotations

import re
import time
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=14)

TEST_INPUT = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


@dataclass
class Rock:
    x: int
    y: int
    shape: str


@dataclass
class RockPlatform:
    X: int
    Y: int
    rocks: List[Rock]

    @staticmethod
    def parse_input(input_str: str) -> RockPlatform:
        lines = input_str.split('\n')
        X = len(lines)
        Y = len(lines[0])
        rocks = [Rock(x, y, shape) for x, line in enumerate(lines) for y, shape in enumerate(line) if shape != '.']
        return RockPlatform(X, Y, rocks)

    def move_rocks_up(self):
        moved = 0
        for rock in self.rocks:
            if (
                rock.shape == 'O'
                and rock.x > 0
                and len([other_rock for other_rock in self.rocks if rock.x - 1 == other_rock.x and rock.y == other_rock.y]) == 0
            ):
                rock.x -= 1
                moved += 1
        return moved

    def move_rocks_all_up(self) -> RockPlatform:
        total_moved = 0
        while moved := self.move_rocks_up():
            total_moved += moved

        return self

    def total_load(self):
        total_load = 0
        for rock in self.rocks:
            if rock.shape == 'O':
                total_load += self.X - rock.x

        return total_load


def part_one(input_str: str) -> int:
    return RockPlatform.parse_input(input_str).move_rocks_all_up().total_load()


if __name__ == "__main__":
    # test pt 1
    # print(RockPlatform.parse_input(TEST_INPUT))

    # rock_platform = RockPlatform.parse_input(TEST_INPUT)
    # print(rock_platform.move_rocks_all_up())
    # print(rock_platform.total_load())
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    """WAAAAY TO SLOW"""
    # # test pt 2
    # print(part_two(TEST_INPUT))

    # # pt 2
    # print(part_two(puzzle.input_data))
