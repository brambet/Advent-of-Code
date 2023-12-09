from __future__ import annotations

import re
from dataclasses import dataclass
from math import lcm
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=8)

TEST_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


@dataclass
class Map:
    instructions: List[str]
    network: Dict[str, Tuple[str, str]]

    @staticmethod
    def parse_map(input_str) -> Map:
        instructions, network = input_str.split('\n\n')
        instructions = list(instructions)
        network = {line[:3]: (line[7:10], line[12:15]) for line in network.split('\n')}
        return Map(instructions, network)

    def steps_to_traverse_map(self, start_position='AAA', ends_with='ZZZ') -> int:
        no_of_instructions = len(self.instructions)
        step = 0
        position = start_position
        while not position.endswith(ends_with):
            instruction = self.instructions[step % no_of_instructions]
            if instruction == 'L':
                position = self.network[position][0]
            else:
                position = self.network[position][1]
            step += 1

        return step

    def steps_to_traverse_map_ghostlike(self) -> int:
        positions = [position for position in self.network.keys() if position.endswith('A')]
        return lcm(*[self.steps_to_traverse_map(position, 'Z') for position in positions])

        # below does not work - too slow, so I guessed the LCM method
        # while not all([position.endswith('Z') for position in positions]):
        #     instruction = self.instructions[step % no_of_instructions]
        #     if instruction == 'L':
        #         for i, position in enumerate(positions):
        #             positions[i] = self.network[position][0]
        #     else:
        #         for i, position in enumerate(positions):
        #             positions[i] = self.network[position][1]
        #     step += 1
        #     # print(positions)

        #     if step > 1e9:
        #         print('too long')
        #         break

        # print(positions)

        # return step


def part_one(input_str: str) -> int:
    return Map.parse_map(input_str).steps_to_traverse_map()


def part_two(input_str: str) -> int:
    return Map.parse_map(input_str).steps_to_traverse_map_ghostlike()


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))
    print(part_one(TEST_INPUT2))

    # # pt 1
    print(part_one(puzzle.input_data))

    # # test pt 2
    print(part_two(TEST_INPUT3))

    # # pt 2
    print(part_two(puzzle.input_data))
