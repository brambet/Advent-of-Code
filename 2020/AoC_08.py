from __future__ import annotations

from typing import NamedTuple, Tuple, List
import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=8)


TEST_PROGRAM = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

TEST_PROGRAM2 = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
nop -4
acc +6"""


class Instruction():
    operator: str
    value: int
    executed: int

    def __init__(self, operator: str, value: int, executed: int) -> Instruction:
        self.operator = operator
        self.value = value
        self.executed = executed

    @staticmethod
    def parse_line(line: str) -> Instruction:
        parts = line.split()
        return Instruction(operator=parts[0], value=int(parts[1]), executed=0)


    def swap_operator(self):
        if self.operator == 'jmp':
            self.operator = 'nop'
        elif self.operator == 'nop':
            self.operator = 'jmp' 


class Program():
    instructions: List[Instruction]

    def __init__(self, instructions):
        self.instructions = instructions

    @staticmethod
    def parse_program(raw: str) -> Program:
        instructions = [Instruction.parse_line(line) for line in raw.split('\n')]
        return Program(instructions)


    def run_program(self) -> Tuple[int,int]:
        index = 0
        accumulator = 0
        while index < len(self.instructions):
            instruction = self.instructions[index]
            
            if instruction.executed > 0:
                return index, accumulator
            if instruction.operator == 'nop':
                index += 1
            elif instruction.operator == 'acc':
                accumulator += instruction.value
                index += 1
            elif instruction.operator == 'jmp':
                index += instruction.value
            else:
                raise ValueError("Wrong instructions")
            
            instruction.executed += 1

        return index, accumulator


    def reset_count(self):
        for instruction in self.instructions:
            instruction.executed = 0



    def run_original_program(self):
        accumulator, _ = self.run_program()
        return accumulator


    def fix_program(self):
        for error_pos, instruction in enumerate(self.instructions):
            instruction.swap_operator()
            end_index, accumulator = self.run_program()
            if end_index == len(self.instructions):
                return error_pos, accumulator 
            else:
                instruction.swap_operator()
                self.reset_count()



if __name__ == "__main__":
    # pt 1
    assert Program.parse_program(TEST_PROGRAM).run_program()[1] == 5
    print(Program.parse_program(puzzle.input_data).run_program())

    # pt 2
    assert Program.parse_program(TEST_PROGRAM).fix_program()[1] == 8
    print(Program.parse_program(puzzle.input_data).fix_program())
