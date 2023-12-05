from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union
import numpy as np

# get puzzle
puzzle = Puzzle(year=2021, day=3)

TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def parse_input(puzzle_input: str) -> np.ndarray:
    return np.array([[int(bit) for bit in line] for line in puzzle_input.split('\n')])


def most_and_least_common_bit(input_array: np.array, bit_position: int = None) -> Union[np.ndarray, np.ndarray]:
    if bit_position is not None:
        bit_mean = np.mean(input_array[:, bit_position])
        if bit_mean == 0.5:
            return 1, 0
        most_common_bit = round(bit_mean)
        # if most_common_bit ==
        return most_common_bit, 1-most_common_bit
    # with small tweak to prevent rounding down of 0.5
    bit_means = np.mean(input_array, axis=0) + 1E-16
    most_common_bits = np.round(bit_means)
    return most_common_bits, 1-most_common_bits


def bit_row_to_int(bits: np.ndarray) -> int:
    binary_number = ''.join([str(int(x)) for x in bits])
    decimal_number = int(binary_number, 2)
    return decimal_number


def gamma_epsilon_rate(most_common_bits: np.array, least_common_bits: np.array) -> Union[int]:
    # binary_most_common = ''.join([str(int(x)) for x in most_common_bits])
    gamma = bit_row_to_int(most_common_bits)
    epsilon = bit_row_to_int(least_common_bits)
    return gamma, epsilon


def pt1(puzzle_input: str) -> int:
    input_array = parse_input(puzzle_input)
    most_common, least_common = most_and_least_common_bit(input_array)
    gamma, epsilon = gamma_epsilon_rate(most_common, least_common)
    return gamma*epsilon


def drill_down_most_common(input_array):
    _, array_width = input_array.shape
    bit_position = 0
    search_array = np.copy(input_array)

    while search_array.shape[0] > 1:
        most_common_bit, _ = most_and_least_common_bit(
            search_array, bit_position)
        matching_rows = np.flatnonzero(search_array[:, bit_position]
                                       == most_common_bit)
        search_array = search_array[matching_rows, :]
        bit_position += 1

    return search_array.flatten()


def drill_down_least_common(input_array):
    _, array_width = input_array.shape
    bit_position = 0
    search_array = np.copy(input_array)

    while search_array.shape[0] > 1:
        _, least_common_bit = most_and_least_common_bit(
            search_array, bit_position)
        matching_rows = np.flatnonzero(search_array[:, bit_position]
                                       == least_common_bit)
        search_array = search_array[matching_rows, :]
        bit_position += 1

    return search_array.flatten()


def oxygen_generator_rating(input_array):
    bits = drill_down_most_common(input_array)
    return bit_row_to_int(bits)


def CO2_scrubber_rating(input_array):
    bits = drill_down_least_common(input_array)
    return bit_row_to_int(bits)


def part_two(puzzle_input):
    input_array = parse_input(puzzle_input)
    return oxygen_generator_rating(input_array) * CO2_scrubber_rating(input_array)


if __name__ == '__main__':

    # test pt 1
    print(pt1(TEST_INPUT))
    # pt 1
    print(pt1(puzzle.input_data))

    # test pt 2
    print(part_two(TEST_INPUT))
    # pt 2
    print(part_two(puzzle.input_data))
