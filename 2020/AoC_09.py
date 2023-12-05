from __future__ import annotations

from typing import NamedTuple, Tuple, List
import re
from aocd.models import Puzzle
from itertools import combinations_with_replacement, combinations, product

puzzle = Puzzle(year=2020, day=9)

TEST_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def parse(raw: str) -> List[int]:
    return [int(number) for number in raw.split('\n')]


def find_first_non_sum(input: List[int], preamble_length):
    for i in range(preamble_length, len(input)):
        target = input[i]
        subset = input[i-preamble_length:i]
        if not any([(i + j == target) for i,j in combinations(subset, 2)]):
            return target


def find_summing_contiguous_subset(input: List[int], target_sum: int) -> List[int]:
    for i in range(len(input)):
        j = 0
        while sum(input[i:i+j])<= target_sum:
            if sum(input[i:i+j]) == target_sum:
                return input[i:i+j]
            else:
                j += 1


def answer_pt_2(input: List[int], preamble_length)->int:
    target_sum = find_first_non_sum(input,preamble_length)
    summing_subset = find_summing_contiguous_subset(input,target_sum)
    return min(summing_subset) + max(summing_subset)



if __name__ == "__main__":
    # pt 1
    assert find_first_non_sum(parse(TEST_INPUT),5) == 127
    print(find_first_non_sum(parse(puzzle.input_data),25))

    # pt 2
    assert answer_pt_2(parse(TEST_INPUT),5) == 62
    print(answer_pt_2(parse(puzzle.input_data),25))
