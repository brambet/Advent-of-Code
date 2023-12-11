from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=9)

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


# @dataclass
# class IntegerPolynomialFitter:
#     sequence: List[int]

#     @staticmethod
#     def parse_history(input_str: str) -> IntegerPolynomialFitter:
#         return IntegerPolynomialFitter([int(x) for x in input_str.split()])

#     def _fit_polynomial(self):
#         self.x = [x for x in range(len(self.sequence))]

#         degree = -1  # to start at 0 below
#         residual = 1
#         while np.linalg.norm(residual) > 1e-3:
#             degree += 1
#             p, residual, *dont_care = np.polyfit(self.x, self.sequence, deg=degree, full=True)
#             # if not residual.size > 0:
#             #     print(f"residual: {residual}")
#             #     print(f"sequence:{self.sequence}")
#             #     print(f"degree: {degree}")
#             #     print(f"p: {p}")

#         self.p = p

#     def next_value(self):
#         self._fit_polynomial()
#         next_x = len(self.x)
#         return int(round(np.poly1d(self.p)(next_x)))


@dataclass
class IntegerPolynomialFitter:
    sequence: np.array[int]

    @staticmethod
    def parse_history(input_str: str) -> IntegerPolynomialFitter:
        return IntegerPolynomialFitter(np.asarray([int(x) for x in input_str.split()]))

    def extrapolate_end(self):
        degree = 0
        diffs = [self.sequence]
        while not (diffs[degree] == 0).all():
            diffs.append(np.diff(diffs[degree]))
            degree += 1

        for d in range(degree - 1, -1, -1):
            # print(d)
            diffs[d] = np.concatenate([diffs[d], [diffs[d][-1] + diffs[d + 1][-1]]])

        return diffs[0][-1]

    def extrapolate_start(self):
        degree = 0
        diffs = [self.sequence]
        while not (diffs[degree] == 0).all():
            diffs.append(np.diff(diffs[degree]))
            degree += 1

        for d in range(degree - 1, -1, -1):
            # print(d)
            diffs[d] = np.concatenate([[diffs[d][0] - diffs[d + 1][0]], diffs[d]])

        return diffs[0][0]


@dataclass
class OASIS:
    histories: List[List[int]]

    @staticmethod
    def parse_input(input_str: str) -> OASIS:
        return OASIS([[int(x) for x in line.split()] for line in input_str.split('\n')])

    def next_values(self):
        return [IntegerPolynomialFitter(np.asarray(history)).extrapolate_end() for history in self.histories]

    def zeroth_values(self):
        return [IntegerPolynomialFitter(np.asarray(history)).extrapolate_start() for history in self.histories]

    def sum_of_next_values(self):
        return sum(self.next_values())

    def sum_of_prev_values(self):
        return sum(self.zeroth_values())


def part_one(input_str: str) -> int:
    return OASIS.parse_input(input_str).sum_of_next_values()


def part_two(input_str: str) -> int:
    return OASIS.parse_input(input_str).sum_of_prev_values()


if __name__ == "__main__":
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    print(part_one(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))

    # # pt 2
    print(part_two(puzzle.input_data))
