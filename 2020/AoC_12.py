# from __future__ import annotations

from typing import NamedTuple, Tuple, List
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=12)
from math import cos, sin, pi, sqrt

TEST_INPUT = """F10
N3
F7
R90
F11"""


class Ship():
    instructions : List[str] 
    theta : int
    x : int
    y : int
    waypoint_x : int
    waypoint_y : int


    def __init__(self, input: str):
        self.instructions = input.split('\n')
        self.x = self.y = self.theta = 0
        self.waypoint_x = 10
        self.waypoint_y = 1
        

    def step(self, instruction):
        operator = instruction[0]
        stepsize = int(instruction[1:])

        if operator == 'N':
            self.y += stepsize
        elif operator == 'S':
            self.y -= stepsize
        elif operator ==  'E':
            self.x += stepsize
        elif operator == 'W':
            self.x -= stepsize
        elif operator == 'L':
            self.theta += stepsize
        elif operator == 'R':
            self.theta -= stepsize
        elif operator == 'F':
            self.x += int(stepsize*cos(2*pi*self.theta/360))
            self.y += int(stepsize*sin(2*pi*self.theta/360))


    def waypoint_step(self, instruction):
        operator = instruction[0]
        stepsize = int(instruction[1:])

        if operator == 'N':
            self.waypoint_y += stepsize
        elif operator == 'S':
            self.waypoint_y -= stepsize
        elif operator ==  'E':
            self.waypoint_x += stepsize
        elif operator == 'W':
            self.waypoint_x -= stepsize
        elif operator == 'L':
            self.waypoint_x, self.waypoint_y = int(self.waypoint_x*cos(2*pi*stepsize/360)) - int(self.waypoint_y*sin(2*pi*stepsize/360)), \
                                               int(self.waypoint_x*sin(2*pi*stepsize/360)) + int(self.waypoint_y*cos(2*pi*stepsize/360))
        elif operator == 'R':
            self.waypoint_x, self.waypoint_y = int(self.waypoint_x*cos(2*pi*-stepsize/360)) - int(self.waypoint_y*sin(2*pi*-stepsize/360)), \
                                               int(self.waypoint_x*sin(2*pi*-stepsize/360)) + int(self.waypoint_y*cos(2*pi*-stepsize/360))
        elif operator == 'F':
            self.x += stepsize*self.waypoint_x
            self.y += stepsize*self.waypoint_y

    
    def run_instructions(self):
        for instruction in self.instructions:
            self.step(instruction)
        return abs(self.x) + abs(self.y)

    
    def run_waypoint_instructions(self):
        for instruction in self.instructions:
            self.waypoint_step(instruction)
        return abs(self.x) + abs(self.y)



# test
assert Ship(TEST_INPUT).run_instructions() == 25

# pt 1
print(Ship(puzzle.input_data).run_instructions())

# test
assert Ship(TEST_INPUT).run_waypoint_instructions() == 286

# pt 2
print(Ship(puzzle.input_data).run_waypoint_instructions())
