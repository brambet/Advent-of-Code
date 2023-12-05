from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set
import numpy as np
import re
from collections import Counter
import numpy as np
# get puzzle
puzzle = Puzzle(year=2021, day=5)

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_line_part_one(line_instruction_string: str) -> List[Tuple[int, int]]:
    x1, y1, x2, y2 = [int(z)
                      for z in re.findall(r'\d+', line_instruction_string)]
    if x1 == x2:
        ys1, ys2 = sorted([y1, y2])
        return [(x1, y) for y in range(ys1, ys2+1)]
    elif y1 == y2:
        xs1, xs2 = sorted([x1, x2])
        return [(x, y1) for x in range(xs1, xs2+1)]
    else:
        return []


def parse_line_part_two(line_instruction_string: str) -> List[Tuple[int, int]]:
    x1, y1, x2, y2 = [int(z)
                      for z in re.findall(r'\d+', line_instruction_string)]

    dx = np.sign(x2-x1)
    dy = np.sign(y2-y1)

    if dx == 0:
        return [(x1, y) for y in range(y1, y2+dy, dy)]
    elif dy == 0:
        return [(x, y1) for x in range(x1, x2+dx, dx)]
    else:
        return list(zip(range(x1, x2+dx, dx), range(y1, y2+dy, dy)))

    # if x1 == x2:
    #     ys1, ys2 = sorted([y1, y2])
    #     return [(x1, y) for y in range(ys1, ys2+1)]
    # elif y1 == y2:
    #     xs1, xs2 = sorted([x1, x2])
    #     return [(x, y1) for x in range(xs1, xs2+1)]
    # else:
    #     return []


def part_one(input_string: str) -> List[Tuple[int, int]]:
    coordinates = []
    for line in input_string.split('\n'):
        coordinates += parse_line_part_one(line)

    counter = Counter(coordinates)

    intersections = {(coord, count)
                     for coord, count in counter.items() if count > 1}

    return len(intersections)


def part_two(input_string: str) -> List[Tuple[int, int]]:
    coordinates = []
    for line in input_string.split('\n'):
        coordinates += parse_line_part_two(line)

    counter = Counter(coordinates)

    intersections = {(coord, count)
                     for coord, count in counter.items() if count > 1}

    return len(intersections)


if __name__ == '__main__':

    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 1
    print(part_two(puzzle.input_data))
