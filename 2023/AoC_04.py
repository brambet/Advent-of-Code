from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=4)


TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


@dataclass
class Card:
    id: int
    winning_numbers: Set[int]
    numbers: Set[int]

    @staticmethod
    def parse_line(line_str: str) -> Card:
        game_id_str, winning_numbers_str, numbers_str = re.split(r': | \|', line_str)
        id = re.findall(r'\d+', game_id_str)[0]
        winning_numbers = set(map(int, re.findall(r'\d+', winning_numbers_str)))
        numbers = set(map(int, re.findall(r'\d+', numbers_str)))
        return Card(id, winning_numbers, numbers)

    def has_number_of_winning_numbers(self) -> int:
        return len(self.numbers.intersection(self.winning_numbers))

    def card_points(self) -> int:
        if self.has_number_of_winning_numbers():
            return 2 ** (self.has_number_of_winning_numbers() - 1)
        return 0


def part_one(input_str: str) -> int:
    return sum([Card.parse_line(line).card_points() for line in input_str.split('\n')])


def part_two(input_str: str) -> int:
    cards = [Card.parse_line(line) for line in input_str.split('\n')]
    multipliers = [1 for _ in range(len(cards))]
    for i, card in enumerate(cards):
        for j in range(card.has_number_of_winning_numbers()):
            multipliers[i + j + 1] += multipliers[i]

    return sum(multipliers)


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
