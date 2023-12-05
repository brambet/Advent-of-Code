from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=9)

TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST_INPUT2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


@dataclass
class Position:
    x: int
    y: int

    def __sub__(self, other: Position):
        # manhattan distance
        return max(abs(self.x - other.x), abs(self.y - other.y))


class Instruction(NamedTuple):
    direction: str
    stepsize: int

    @staticmethod
    def parse_instruction(instruction: str):
        direction, stepsize = instruction.split()
        return Instruction(direction=direction, stepsize=int(stepsize))


class RopeMovement:
    def __init__(self, puzzle_input: str, rope_length: int, map_width = 6, map_height = 5):
        self.instructions = [Instruction.parse_instruction(instruction) for instruction in puzzle_input.split('\n')]
        self.rope_length = rope_length
        self.knot_positions = [Position(0, 0) for _ in range(rope_length)]
        self.head_position = Position(0,0)
        self.tail_position = Position(0,0)
        self.tail_visited_positions = {(0, 0)}
        self.map_width = map_width
        self.map_height = map_height 

    def move_knot_one_step(self, knot, direction: str):
        match direction:
            case 'R':
                knot.x += 1
            case 'L':
                knot.x -= 1
            case 'U':
                knot.y += 1
            case 'D':
                knot.y -= 1

    def execute_instruction(self, instruction: Instruction):
        
        for _ in range(instruction.stepsize):
            old_positions = deepcopy(self.knot_positions)
            # old_head_position = deepcopy(self.head_position)
            # self.move_knot_one_step(self.head_position, instruction.direction)
            for i, _ in enumerate(self.knot_positions):
                if i == 0:
                    self.move_knot_one_step(self.knot_positions[0], instruction.direction)
                else:
                    if (self.knot_positions[i-1] - self.knot_positions[i]) > 1:
                        self.knot_positions[i] = deepcopy(old_positions[i-1])
                self.tail_visited_positions.add((self.knot_positions[-1].x, self.knot_positions[-1].y))
            self.print_positions()
            # print(self.knot_positions[0] - self.knot_positions[-1])
            # old_head_position = deepcopy(self.head_position)
            # self.move_head_one_step(instruction.direction)
            # if (self.head_position - self.tail_position) > 1:
            #     self.tail_position = old_head_position
            #     self.tail_visited_positions.add((self.tail_position.x, self.tail_position.y))

    def print_positions(self):
        map_locations =  [['.' for _ in  range(self.map_width)] for _ in range(self.map_height)]
        for i, knot in reversed(list(enumerate(self.knot_positions))):
            if i == 0:
                map_locations[knot.y][knot.x] = 'H'
            else: 
                map_locations[knot.y][knot.x] = str(i)

        map_print = '\n'.join([' '.join(line) for line in reversed(map_locations)]) 
        print(map_print)
        print('\n')



    def execute_instructions(self):
        self.print_positions()
        for instruction in self.instructions:
            self.execute_instruction(instruction)
            # self.print_positions()
        return len(self.tail_visited_positions)

if __name__ == "__main__":

    # test pt 1
    # head_tail_movement = RopeMovement(TEST_INPUT, rope_length=2)
    # print(head_tail_movement.execute_instructions())
    # # print(head_tail_movement.knot_positions)

    # #  pt 1
    # head_tail_movement = RopeMovement(puzzle_input=puzzle.input_data, rope_length=2)
    # print(head_tail_movement.execute_instructions())

     # test pt 2
    head_tail_movement = RopeMovement(TEST_INPUT, rope_length=10)
    print(head_tail_movement.execute_instructions())
    # print(head_tail_movement.knot_positions)
    
    # head_tail_movement.print_positions()

    # pt 2
    # head_tail_movement = RopeMovement(puzzle.input_data, rope_length=10)
    # print(head_tail_movement.execute_instructions())
