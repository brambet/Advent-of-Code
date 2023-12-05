# from __future__ import annotations

from typing import NamedTuple, Tuple, List
from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2020, day=10)

TEST_INPUT1 = """16
10
15
5
1
11
7
19
6
12
4"""

TEST_INPUT2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def parse_input(raw: str) -> List[int]:
    return [int(number) for number in raw.split('\n')]

def calc_differences(input: List[int]) -> List[int]:
    input.sort()
    return [(next - previous) for  next, previous in zip(input + [input[-1]+3], [0] + input)]


def count_differences(input: List[int]) -> Counter:
    return Counter(calc_differences(input))


def answer_pt_1(input: List[int]) -> int:
    counted_differences = count_differences(input)
    return counted_differences[1]*counted_differences[3]


def count_lengths_of_one_sublists(difference_list: List[int]) -> List[int]:
    counter = 0
    length_list = []
    for elt in difference_list:
        if elt == 1:
            counter += 1
        if elt == 3:
            length_list.append(counter)
            counter = 0
    return length_list


# possible combinations to choose subsets with <= 3 differences between the elements
# quick check on the inputs show that a sequence of differences 1 has max lenght 4.
# in this case, leaving out all intermediates is not allowed, so you have 2^3 - 1 = 7 combinations
# e.g. for [1 2 3 4 5] is [1 5] is not allowed, you have to choose at least one from [2 3 4]
POSSIBLE_COMBINATIONS = {4 : 7, 3: 4, 2: 2, 1: 1, 0: 1}


def count_possibilities(counted_one_subsets: List[int]) -> int:
    number_of_combinations = 1
    for lengths in counted_one_subsets:
        number_of_combinations *= POSSIBLE_COMBINATIONS[lengths]
    return number_of_combinations


def answer_pt_2(input: List[int]) -> int:
    difference_list = calc_differences(input)
    one_sublists = count_lengths_of_one_sublists(difference_list)
    return count_possibilities(one_sublists)
    
    
if __name__ == "__main__":
    # pt 1
    assert answer_pt_1(parse_input(TEST_INPUT1)) == 7*5
    assert answer_pt_1(parse_input(TEST_INPUT2)) == 22*10
    print(answer_pt_1(parse_input(puzzle.input_data)))

    # pt 2
    assert answer_pt_2(parse_input(TEST_INPUT1)) == 8
    assert answer_pt_2(parse_input(TEST_INPUT2)) == 19208
    print(answer_pt_2(parse_input(puzzle.input_data)))
