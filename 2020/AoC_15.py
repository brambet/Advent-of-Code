# from __future__ import annotations
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=15)
from typing import NamedTuple, Tuple, List, Deque, DefaultDict
import time
# import re
# from itertools import combinations

# from itertools import chain, combinations

TEST_NUMBERS = [0,3,6]
TEST_NUMBERS2 = [1,3,2]

PUZZLE_NUMBERS = [8,11,0,19,1,2]


def play_game(starting_numbers, n_turns):
    n_start = len(starting_numbers)
    announced_number_turns = DefaultDict(Deque[int])
    previous_number = 0

    for turn in range(n_start):
        new_number = starting_numbers[turn]
        # print(new_number)
        announced_number_turns[new_number].appendleft(turn)
        previous_number = new_number

    for turn in range(n_start, n_turns):
        # print(f"turn: {turn}")
        # print(f"previous_number: {previous_number}")
        previous_turns = announced_number_turns.get(previous_number, Deque[int])
        # print(f"previous_turns: {previous_turns}")
        if len(previous_turns) < 2:
            new_number = 0
        else:
            new_number = previous_turns[0] - previous_turns[1]
        # print(f"new number: {new_number}")
        announced_number_turns[new_number].appendleft(turn)
        previous_number = new_number

    return previous_number


print(play_game(TEST_NUMBERS2, 2020))

print(play_game(PUZZLE_NUMBERS, 2020))

tic = time.perf_counter()
print(play_game(TEST_NUMBERS, 30000000))
toc = time.perf_counter()
print(f"Test game took {toc - tic:0.4f} seconds")


tic = time.perf_counter()
print(play_game(PUZZLE_NUMBERS, 30000000))
toc = time.perf_counter()
print(f"Puzzle game took {toc - tic:0.4f} seconds")


# tic = time.perf_counter()
# assert pt2(TEST_INPUT3, 0) == TEST_OUTPUT3
# toc = time.perf_counter()
# print(f"Simulation step  took {toc - tic:0.4f} seconds")

# print(announced_number_turns.get(0)[2])
# sequence = Deque

# sequence.appendleft()