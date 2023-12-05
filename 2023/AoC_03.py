from __future__ import annotations

import re
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=3)

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class Position(NamedTuple):
    x: int
    y: int

    def is_adjacent(self, other: Position) -> bool:
        return (abs(self.x - other.x) < 2) and (abs(self.y - other.y) < 2)


class Symbol(NamedTuple):
    symbol: str
    position: List[Position]


class Number(NamedTuple):
    value: int
    positions: List[Position]

    def adjacent_symbol(self, symbol: Symbol) -> bool:
        for position in self.positions:
            if position.is_adjacent(symbol.position):
                return True
        return False


def parse_input(input_str: str) -> Tuple[List[Number], List[Symbol]]:
    numbers = []
    symbols = []
    for x, line in enumerate(input_str.split('\n')):
        # parse numbers
        for m in re.finditer(r'\d+', line):
            value = int(m.group())
            positions = [Position(x, y) for y in range(*m.span())]
            numbers.append(Number(value, positions))
        # parse symbols
        for y, character in enumerate(line):
            if not (character.isdigit() or character == '.'):
                symbols.append(Symbol(character, Position(x, y)))

    return numbers, symbols


def part_one(input_str: str) -> int:
    numbers, symbols = parse_input(input_str=input_str)

    sum_part_numbers = 0
    for number in numbers:
        for symbol in symbols:
            if number.adjacent_symbol(symbol):
                sum_part_numbers += number.value

    return sum_part_numbers


def part_two(input_str: str) -> int:
    numbers, symbols = parse_input(input_str=input_str)

    sum_gear_ratios = 0

    for symbol in symbols:
        adjacent_number_values = [number.value for number in numbers if number.adjacent_symbol(symbol)]
        if len(adjacent_number_values) == 2:
            sum_gear_ratios += np.prod(adjacent_number_values)

    return sum_gear_ratios


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
