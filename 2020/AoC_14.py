from __future__ import annotations
from typing import NamedTuple, Tuple, List
from aocd.models import Puzzle
import re
puzzle = Puzzle(year=2020, day=14)
from itertools import combinations

from itertools import chain, combinations,count


def subset_complement_pairs(iterable):
    s = set(iterable)
    pairs = []
    for r in range(len(s)+1):
        pairs += [(set(subset), s.difference(subset)) for subset in combinations(s, r)]
    return pairs


TEST_INPUT = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


TEST_PROGRAM2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


TEST_PROGRAM3 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100"""

def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)


def apply_zero_masks(value, zero_masks):
    for bit_index in zero_masks:
        value = value & ~(1 << bit_index)
    return value


def apply_one_masks(value, one_masks):
    for bit_index in one_masks:
        value = value | (1 << bit_index)
    return value



def apply_bit_masks(value, zero_masks, one_masks):
    for bit_index in zero_masks:
            value = value & ~(1 << bit_index)
    for bit_index in one_masks:
        value = value | (1 << bit_index)
    return value


class MemoryInsert(NamedTuple):
    address : int
    value : int


class ProgramStep():
    mask : str
    zero_masks : List[int]
    one_masks : List[int]
    memory_inserts : List[Tuple[int,int]]

    def __init__(self):
        self.memory_inserts = []

    @staticmethod
    def parse_mask(mask_string):
        step = ProgramStep()
        step.mask = mask_string.split(' = ')[1]
        step.zero_masks = [x.start() for x in re.finditer('0',step.mask[::-1])] # reverse mask string order because bit index is from the right
        step.one_masks = [x.start() for x in re.finditer('1',step.mask[::-1])]
        step.floating_masks = [x.start() for x in re.finditer('X',step.mask[::-1])]

        return step

    def parse_memory_insert(self, memory_insert_string):
        address, value = [int(x) for x in re.findall(r'\d+', memory_insert_string)]
        self.memory_inserts.append(MemoryInsert(address, value))

    
    def apply_bit_masks(self, value):
        for bit_index in self.zero_masks:
                value = value & ~(1 << bit_index)
        for bit_index in self.one_masks:
            value = value | (1 << bit_index)
        return value


    def apply_bit_masks_v2(self, address_value):
        new_addresses = []
        for bit_index in self.one_masks:
            address_value = address_value | (1 << bit_index)

        for subset, complement in subset_complement_pairs(self.floating_masks):
            new_address_value = apply_zero_masks(address_value, subset)
            new_address_value = apply_one_masks(new_address_value, complement)
            new_addresses.append(new_address_value)
        
        return new_addresses


    def insert_memory_values(self, memory):
        for address, value in self.memory_inserts:
            memory[address] = self.apply_bit_masks(value)
    

    def insert_memory_values_v2(self, memory):
        for address, value in self.memory_inserts:
            for new_address in self.apply_bit_masks_v2(address):
                memory[new_address] = value



class Program():
    program : List[ProgramStep]
    memory : List[int]

    def __init__(self, input: str):
        self.program = []
        input_lines = input.split('\n')
        step = ProgramStep.parse_mask(input_lines[0])
        for line in input_lines[1:]:
            if line.startswith('mask'):
                self.program.append(step)
                step = ProgramStep.parse_mask(line)
            elif line.startswith('mem'):
                step.parse_memory_insert(line)
        self.program.append(step)

        self.memory = {}


    def run_program(self):
        for step in self.program:
            step.insert_memory_values(self.memory)

        return sum(self.memory.values())


    def run_program_v2(self):
        for step in self.program:
            step.insert_memory_values_v2(self.memory)

        return sum(self.memory.values())


assert Program(TEST_INPUT).run_program() == 165
print(Program(puzzle.input_data).run_program())


assert Program(TEST_PROGRAM2).run_program_v2() == 208
print(Program(puzzle.input_data).run_program_v2())

