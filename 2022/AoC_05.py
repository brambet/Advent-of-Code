from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=5)

TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_input(puzzle_input):
    layout, instructions = puzzle_input.split("\n\n")

    print([(line) for line in layout.split("\n")])


class Crane9000:
    def __init__(self, puzzle_input: str):
        layout, instructions = puzzle_input.split("\n\n")

        # parse layout
        self.layout_lines = [line for line in layout.split("\n")[::-1]]
        self.number_of_stacks = int((len(self.layout_lines[0]) + 1) / 4)

        self.stacks = [[] for _ in range(self.number_of_stacks)]

        for layout_line in self.layout_lines[1:]:
            for i in range(self.number_of_stacks):
                crate = layout_line[1 + 4 * i]
                if crate != " ":
                    self.stacks[i].append(crate)

        # parse instructions
        self.instructions = [
            [int(x) for x in instructions_line.split(" ") if x.isdigit()]
            for instructions_line in instructions.split("\n")
        ]

    def execute_instruction(self, instruction: List[int]):
        number, source, target = instruction
        for _ in range(number):
            self.stacks[target - 1].append(self.stacks[source - 1].pop())

    def execute_instructions(self):
        for instruction in self.instructions:
            self.execute_instruction(instruction)

    def final_answer(self):
        self.execute_instructions()
        tops = [stack[-1] for stack in self.stacks]
        print("".join(tops))


class Crane9001(Crane9000):
    def execute_instruction(self, instruction: List[int]):
        number, source, target = instruction
        for idx in sorted(range(number), reverse=True):
            self.stacks[target - 1].append(self.stacks[source - 1].pop(-idx - 1))


if __name__ == "__main__":

    # test pt 1
    crane_layout = Crane9000(TEST_INPUT)
    crane_layout.final_answer()

    # pt 1
    crane_layout = Crane9000(puzzle_input=puzzle.input_data)
    crane_layout.final_answer()

    # test pt 2
    crane_layout = Crane9001(TEST_INPUT)
    crane_layout.final_answer()

    # pt 2
    crane_layout = Crane9001(puzzle_input=puzzle.input_data)
    crane_layout.final_answer()
