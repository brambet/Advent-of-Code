from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=8)

TEST_INPUT = """30373
25512
65332
33549
35390"""


class TreeMap:
    def __init__(self, puzzle_input: str):
        self.tree_map = np.array([[int(tree) for tree in line] for line in puzzle_input.split('\n')])

    def __str__(self):
        return str(self.tree_map)

    def tree_is_visible(self, i, j):
        if min(i, j) == 0 or max(i, j) == self.tree_map.shape[0] - 1:  # edge trees are always visible
            return True
        tree_height = self.tree_map[i, j]
        line_of_sights = [
            np.max(self.tree_map[i, :j]) < tree_height,  # left
            np.max(self.tree_map[:i, j]) < tree_height,  # above
            np.max(self.tree_map[i + 1 :, j]) < tree_height,  # below
            np.max(self.tree_map[i, j + 1 :]) < tree_height,  # right
        ]
        return any(line_of_sights)

    def count_visible(self):
        return sum(self.tree_is_visible(*loc) for loc in np.ndindex(self.tree_map.shape))

    def scenic_score(self, i, j):
        if min(i, j) == 0 or max(i, j) == self.tree_map.shape[0] - 1:  # edge trees have at least one viewing distance
            return True
        tree_height = self.tree_map[i, j]
        # print(self.tree_map[i - 1 :: -1, j] >= tree_height)
        viewing_distances = []

        # above
        view_line = self.tree_map[i - 1 :: -1, j] >= tree_height
        viewing_distance = np.argmax(view_line) + 1 if any(view_line) else len(view_line)
        viewing_distances.append(viewing_distance)

        # left
        # print(f"left: {self.tree_map[i, j - 1 :: -1]}")
        view_line = self.tree_map[i, j - 1 :: -1] >= tree_height
        viewing_distance = np.argmax(view_line) + 1 if any(view_line) else len(view_line)
        viewing_distances.append(viewing_distance)

        # below
        view_line = self.tree_map[i + 1 : :, j] >= tree_height
        viewing_distance = np.argmax(view_line) + 1 if any(view_line) else len(view_line)
        viewing_distances.append(viewing_distance)

        # right
        view_line = self.tree_map[i, j + 1 : :] >= tree_height
        viewing_distance = np.argmax(view_line) + 1 if any(view_line) else len(view_line)
        viewing_distances.append(viewing_distance)

        return np.prod(viewing_distances)

    def get_max_scenic_score(self):
        return max(self.scenic_score(*loc) for loc in np.ndindex(self.tree_map.shape))


if __name__ == "__main__":

    # test pt 1
    tree_map = TreeMap(TEST_INPUT)
    print(tree_map.count_visible())

    #  pt 1
    tree_map = TreeMap(puzzle_input=puzzle.input_data)
    print(tree_map.count_visible())

    # test pt 2
    tree_map = TreeMap(TEST_INPUT)
    print(tree_map.get_max_scenic_score())

    #  pt 2
    tree_map = TreeMap(puzzle_input=puzzle.input_data)
    print(tree_map.get_max_scenic_score())
