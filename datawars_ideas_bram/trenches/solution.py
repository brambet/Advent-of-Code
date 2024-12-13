from __future__ import annotations

from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt
from shapely import buffer
from shapely.geometry import LineString, Polygon

TEST_INPUT = """O 6
Z 5
W 2
Z 2
O 2
Z 2
W 5
N 2
W 1
N 2
O 2
N 3
W 2
N 2"""


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    @property
    def coordinates(self):
        return (self.x, self.y)

    def step(self, direction: str, size: int = 1) -> Position:
        match direction:
            case "N":
                return Position(self.x, self.y + size)
            case "Z":
                return Position(self.x, self.y - size)
            case "W":
                return Position(self.x - size, self.y)
            case "O":
                return Position(self.x + size, self.y)
            case _:
                raise ValueError("Unknown direction")


@dataclass
class DigPlan:
    trench_vertices: List[Position]

    @staticmethod
    def parse_dig_plan(digplan: str) -> DigPlan:
        current_pos = Position(0, 0)

        vertices = [current_pos]
        for line in digplan.split("\n"):
            direction, length = line.split()
            length = int(length)
            current_pos = current_pos.step(direction, length)
            vertices.append(current_pos)

        return DigPlan(vertices)
   
    @property
    def trench_center_line(self):
        return LineString([pos.coordinates for pos in self.trench_vertices])
     
    @property
    def trench(self):
        """Trench is one meter wide, so buffer with 0.5"""
        return buffer(self.trench_center_line, 0.5, join_style="mitre")

    def plot_trench(self):
        p = gpd.GeoSeries(self.trench)
        p.plot()
        plt.show()

    @property
    def inner_roof(self):
        return Polygon(self.trench.exterior)
    
    def plot_inner_roof(self):
        p = gpd.GeoSeries(self.inner_roof)
        p.plot()
        plt.show()




if __name__ == '__main__':
    print(f"Answer test part one: {int(DigPlan.parse_dig_plan(TEST_INPUT).trench.area)}")

    with open('input.txt', 'r') as f:
        print(f"Anwer part one: {int(DigPlan.parse_dig_plan(f.read()).trench.area)}")


    print(f"Answer test part two: {int(DigPlan.parse_dig_plan(TEST_INPUT).inner_roof.area)}")

    with open('input.txt', 'r') as f:
        print(f"Anwer part two: {int(DigPlan.parse_dig_plan(f.read()).inner_roof.area)}")
