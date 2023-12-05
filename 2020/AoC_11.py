# from __future__ import annotations

from typing import NamedTuple, Tuple, List
from aocd.models import Puzzle
from collections import Counter
import numpy as np
from itertools import combinations, product
import math
puzzle = Puzzle(year=2020, day=11)
import time


TEST_INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

TEST_INPUT2 = """.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

TEST_INPUT3 = """.............
.L.L.#.#.#.#.
............."""

TEST_INPUT4 = """.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##."""


class SeatMap():
    seat_map: str
    occupation : dict
    seats : set
    width : int
    length : int
    
    def __init__(self, input:str):
        self.seat_map = input
        self.occupation = {(i,j) : 'L' for j, line in enumerate(input.split('\n')) for i, letter in enumerate(line) if letter == 'L'}
        self.occupation.update({(i,j) : '#' for j, line in enumerate(input.split('\n')) for i, letter in enumerate(line) if letter == '#'})
        self.seats = set(self.occupation.keys())
        self.length = len(input.split('\n'))
        self.width = len(input.split('\n')[0])


    def print_map(self):
        print_map = "\n".join(["".join([self.occupation.get((i,j),'.') for i in range(self.width)]) for j in range(self.length)])
        print(print_map)


    def count_adjacent_occupied(self, position):
        neighbours = product([position[0]-1, position[0], position[0]+1], [position[1]-1, position[1], position[1]+1])
        return [self.occupation.get(seat) for seat in neighbours if seat != position].count('#')

   
    def seat_step(self, position):
        # print('seat_step')
        occupied_neighbours =self.count_adjacent_occupied(position)

        if occupied_neighbours == 0 and self.occupation[position] == 'L':
            # self.occupation[position] = '#'
            return '#'
        elif occupied_neighbours >= 4 and self.occupation[position] == '#':
            return 'L' #self.occupation[position] = 'L'
        else:
            return self.occupation[position]


    def seat_map_step(self):
        new_occupation = {seat: self.seat_step(seat) for seat in self.seats}
        if new_occupation == self.occupation:
            return False
        else:
            self.occupation = new_occupation
            return True

    def count_occupied(self):
        return list(self.occupation.values()).count('#')


    def simulate(self):
        changes = True
        iteration = 0
        while changes:
            changes = self.seat_map_step()
            iteration += 1
            #print(iteration)
        return iteration, self.count_occupied()

    def count_occupied_in_sight(self, position):
        occupied = 0

        for dx,dy in product([-1,0,1], [-1,0,1]):
            # print(dx, dy)
            if dx == dy == 0:
                pass
            else:
                for r in range(1, max(self.width, self.length)):
                    # print(r)
                    # print((position[0]+r*dx, position[1]+r*dy))
                    seat_occupation = self.occupation.get((position[0]+r*dx, position[1]+r*dy))
                    # print(seat_occupation)
                    if seat_occupation is not None:
                        # print(seat_occupation)
                        occupied += int(seat_occupation == '#')
                        break

        return occupied               


    def seat_step_new(self, position):
    # print('seat_step')
        occupied_neighbours =self.count_occupied_in_sight(position)

        if occupied_neighbours == 0 and self.occupation[position] == 'L':
            # self.occupation[position] = '#'
            return '#'
        elif occupied_neighbours >= 5 and self.occupation[position] == '#':
            return 'L' #self.occupation[position] = 'L'
        else:
            return self.occupation[position]

    def seat_map_step_new(self):
        new_occupation = {seat: self.seat_step_new(seat) for seat in self.seats}
        if new_occupation == self.occupation:
            return False
        else:
            self.occupation = new_occupation
            return True


    def simulate_new(self):
        changes = True
        iteration = 0
        while changes:
            changes = self.seat_map_step_new()
            iteration += 1
            #print(iteration)
        return iteration, self.count_occupied()    


if __name__ == "__main__":
    # # test
    # tic = time.perf_counter()
    # testmap = SeatMap(TEST_INPUT)
    # print(testmap.simulate())
    # toc = time.perf_counter()
    # print(f"Test simulation took {toc - tic:0.4f} seconds")
    
    # # pt 1
    # tic = time.perf_counter()
    # seatmap = SeatMap(puzzle.input_data)
    # # print(seatmap.seat_map_step())
    # print(seatmap.simulate())
    # toc = time.perf_counter()
    # print(f"Simulation step  took {toc - tic:0.4f} seconds")
    
     # test
    tic = time.perf_counter()
    testmap = SeatMap(TEST_INPUT)
    print(testmap.simulate_new())
    toc = time.perf_counter()
    print(f"Test simulation took {toc - tic:0.4f} seconds")

    # pt 2
    tic = time.perf_counter()
    seatmap = SeatMap(puzzle.input_data)
    print(seatmap.simulate_new())
    toc = time.perf_counter()
    print(f"Simulation step  took {toc - tic:0.4f} seconds")

  
