from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import matplotlib.pyplot as plt
from aocd.models import Puzzle
from shapely import buffer
from shapely.geometry import Polygon

# get puzzle
puzzle = Puzzle(year=2023, day=18)

TEST_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    @property
    def coordinates(self):
        return (self.x, self.y)

    def step(self, direction: str, size: int = 1) -> Position:
        match direction:
            case "U":
                return Position(self.x, self.y + size)
            case "D":
                return Position(self.x, self.y - size)
            case "L":
                return Position(self.x - size, self.y)
            case "R":
                return Position(self.x + size, self.y)

            case _:
                raise ValueError("Unknown direction")


@dataclass
class DigPlan:
    trench_vertices: Dict[Position, str]

    @property
    def polygon(self):
        polygon = Polygon([pos.coordinates for pos in self.trench_vertices.keys()])
        return buffer(polygon, 0.5, join_style="mitre")

    @staticmethod
    def parse_dig_plan(digplan: str) -> DigPlan:
        vertices = {}
        current_pos = Position(0, 0)
        for line in digplan.split("\n"):
            direction, length, color = line.split()
            length = int(length)
            color = color.replace("(", "").replace(")", "")
            vertices[current_pos] = color
            current_pos = current_pos.step(direction, length)

        return DigPlan(vertices)

    def parse_dig_plan_new(digplan: str) -> DigPlan:
        direction_map = {"0": "R", "1": "D", "2": "L", "3": "U"}
        vertices = {}
        current_pos = Position(0, 0)
        for line in digplan.split("\n"):
            _, _, instruction = line.split()
            instruction = instruction.replace("(", "").replace(")", "").replace("#", "")
            direction = direction_map[instruction[-1]]
            length = int(instruction[:-1], 16)
            vertices[current_pos] = ""
            current_pos = current_pos.step(direction, length)

        return DigPlan(vertices)


def part_one(input_str: str) -> int:
    return int(DigPlan.parse_dig_plan(input_str).polygon.area)


def part_two(input_str: str) -> int:
    return int(DigPlan.parse_dig_plan_new(input_str).polygon.area)


def plot_polygon(input_str: str):
    polygon = DigPlan.parse_dig_plan_new(input_str).polygon
    plt.plot(*polygon.exterior.xy)
    plt.show()


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))

    plot_polygon(puzzle.input_data)
