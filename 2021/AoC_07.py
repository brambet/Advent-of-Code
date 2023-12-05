from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set

import numpy as np

# get puzzle
puzzle = Puzzle(year=2021, day=7)

TEST_INPUT = """16,1,2,0,4,2,7,1,2,14"""


def parse_input(input_str: str) -> np.ndarray:
    return np.array([int(x) for x in input_str.split(',')])


def best_position(a: np.ndarray):
    possible_positions = np.arange(np.min(a), np.max(a))
    i, j = np.indices((a.shape[0], possible_positions.shape[0]))
    x = a[i]
    y = possible_positions[j]
    gap = np.abs(x - y)
    differences = np.sum(gap, axis=0)
    return np.min(differences), possible_positions[np.argmin(differences)]


def new_best_position(a: np.ndarray):
    possible_positions = np.arange(np.min(a), np.max(a))
    i, j = np.indices((a.shape[0], possible_positions.shape[0]))
    x = a[i]
    y = possible_positions[j]
    gaps = np.abs(x - y)
    new_gaps = 0.5*gaps*(gaps+1)
    differences = np.sum(new_gaps, axis=0)
    return np.min(differences), possible_positions[np.argmin(differences)]


if __name__ == '__main__':

    # test pt 1
    print(best_position(parse_input(TEST_INPUT)))

    # pt 1
    print(best_position(parse_input(puzzle.input_data)))

    # test pt 2
    print(new_best_position(parse_input(TEST_INPUT)))

    #  pt 2
    print(new_best_position(parse_input(puzzle.input_data)))
