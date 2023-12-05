from typing import List

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)

INPUTS = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


SLOPES = [(1,1), 
(3,1), 
(5,1), 
(7,1), 
(1,2)]

class TreeMap():
    width : int
    height : int
    map : List[List[int]]

    def __init__(self, input_str: str):
        self.map = [[char for char in line] for line in input_str.split('\n')]
        self.width = len(self.map[0])
        self.height = len(self.map)


    def count_trees(self, dx: int, dy: int):
        x, y, count = 0, 0, 0

        while y < self.height:
            count += int(self.map[y][x] == "#")
            x = (x + dx) % self.width
            y = (y + dy)

        return count

    def multiply_counts(self, slope_list):
        product = 1
        for dx, dy in slope_list:
            product *= self.count_trees(dx, dy)

        return product


if __name__ == "__main__":
    # part 1
    assert(TreeMap(INPUTS).count_trees(3,1) == 7)
    print(TreeMap(puzzle.input_data).count_trees(3,1))

    # part 2
    assert(TreeMap(INPUTS).multiply_counts(SLOPES) == 336)
    print(TreeMap(puzzle.input_data).multiply_counts(SLOPES))