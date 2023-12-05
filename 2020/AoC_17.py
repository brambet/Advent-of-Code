from __future__ import annotations
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=17)
from typing import NamedTuple, Tuple, List, Deque, DefaultDict, Set
import time
import re
from itertools import product

TEST_INPUT = """.#.
..#
###"""

class Coordinate(NamedTuple):
    x : int
    y : int
    z : int

    def get_neighbours(self):
        return {Coordinate(self.x + dx, self.y + dy, self.z + dz) for (dx, dy, dz) in product(*(3*[[-1,0,1]])) if not (dx == dy == dz == 0)}


class Coordinate4(NamedTuple):
    x : int
    y : int
    z : int
    w : int

    def get_neighbours(self):
        return {Coordinate4(self.x + dx, self.y + dy, self.z + dz, self.w + dw) for (dx, dy, dz, dw) in product(*(4*[[-1,0,1]])) if not (dx == dy == dz == dw == 0)}



class PocketDimension():
    active_state : Set[Coordinate]

    def __init__(self, input: str) -> PocketDimension:
        lines = input.split('\n')
        self.active_state = set([Coordinate(x, y, 0) for y, line in enumerate(lines) for x, sign in enumerate(line) if sign == '#'])


    def get_all_neighbours(self):
        all_neighbour_list = [point.get_neighbours() for point in self.active_state]
        return set().union(*all_neighbour_list)

    
    def new_active_state(self):
        new_active_state = set()
        changing_coordinates = self.get_all_neighbours().union(self.active_state)
        for coordinate in changing_coordinates:
            active_neighbours = self.active_state.intersection(coordinate.get_neighbours())
            if coordinate in self.active_state and len(active_neighbours) in [2, 3]:
                new_active_state.add(coordinate)
            elif len(active_neighbours) == 3:
                new_active_state.add(coordinate)
        
        return new_active_state


    def run_simulation(self, Ncycles = 6):
        for _ in range(Ncycles):
            self.active_state = self.new_active_state()
        
        return len(self.active_state)


class PocketDimension4(PocketDimension):
    active_state : Set[Coordinate4]

    def __init__(self, input: str) -> PocketDimension:
        lines = input.split('\n')
        self.active_state = set([Coordinate4(x, y, 0, 0) for y, line in enumerate(lines) for x, sign in enumerate(line) if sign == '#'])




# pt 1
print(PocketDimension(TEST_INPUT).run_simulation())
print(PocketDimension(puzzle.input_data).run_simulation())

#pt2
print(PocketDimension4(TEST_INPUT).run_simulation())
print(PocketDimension4(puzzle.input_data).run_simulation())
