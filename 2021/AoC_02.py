from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict


# get puzzle
puzzle = Puzzle(year=2021, day=2)

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class Instruction(NamedTuple):
    direction: str
    units: int

    def parse_instruction(instruction_line: str):
        direction, units = instruction_line.split()
        return Instruction(direction, int(units))


class Position():

    def __init__(self, horizontal_position, depth, aim=0):
        self.horizontal_position = horizontal_position
        self.depth = depth
        self.aim = aim

    def step(self, instruction: Instruction):
        match instruction.direction:
            case 'forward':
                self.horizontal_position += instruction.units
            case 'down':
                self.depth += instruction.units
            case 'up':
                self.depth -= instruction.units
            case _:
                raise ValueError(f'unknown instruction: "')

    def step_part_two(self, instruction: Instruction):
        match instruction.direction:
            case 'down':
                self.aim += instruction.units
            case 'up':
                self.aim -= instruction.units
            case 'forward':
                self.horizontal_position += instruction.units
                self.depth += self.aim * instruction.units
            case _:
                raise ValueError(f'unknown instruction: "')

    def final_answer(self):
        return self.horizontal_position * self.depth


# pt 1 test
test_position = Position(0, 0)
test_instructions = [Instruction.parse_instruction(
    line) for line in TEST_INPUT.split('\n')]
for instruction in test_instructions:
    test_position.step(instruction)
print(test_position.final_answer())


# pt 1
position = Position(0, 0)
instructions = [Instruction.parse_instruction(
    line) for line in puzzle.input_data.split('\n')]
for instruction in instructions:
    position.step(instruction)
print(position.final_answer())


# pt 2 test
test_position = Position(0, 0)
for instruction in test_instructions:
    test_position.step_part_two(instruction)
print(test_position.final_answer())

# pt 2
position = Position(0, 0)
for instruction in instructions:
    position.step_part_two(instruction)
print(position.final_answer())
