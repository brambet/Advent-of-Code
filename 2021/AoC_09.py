from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set
from itertools import product
# get puzzle
puzzle = Puzzle(year=2021, day=9)

TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def parse_input(input_str: str) -> Dict:
    map = dict()

    for i, row in enumerate(input_str.split('\n')):
        for j, value in enumerate(row):
            map[(i, j)] = int(value)

    return map


def get_neighbours(coordinates, map, existing_cluster=set()):
    x, y = coordinates
    neighbours = set()
    candidate_neighbours = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
    neighbours = candidate_neighbours.intersection(
        set(map.keys())) - existing_cluster

    return neighbours


def get_low_points(map: dict) -> List[Tuple[int, int]]:

    low_points = set()
    # print(map)
    for (x, y), value in map.items():
        # comparison = [(map.get((x + dx, y + dy), 10) > value)
        #               for (dx, dy) in zip([-1, 1, 0, 0], [0, 0, -1, 1])]

        comparison = [(map.get(neighbour, 10) >
                      value) for neighbour in get_neighbours((x, y), map)]
        # if (x, y) == (0, 1):
        # print(comparison)

        if all(comparison):
            # print(f"Low point at {(x,y)} with value {value}")
            low_points.add((x, y))

    return low_points


def part_one(input_str: str) -> int:
    map = parse_input(input_str)
    total_risk_level = 0

    for low_point in get_low_points(map):
        total_risk_level += map[low_point] + 1

    return total_risk_level


if __name__ == '__main__':

    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))
