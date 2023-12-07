from __future__ import annotations

import re
from collections import ChainMap
from dataclasses import dataclass
from functools import reduce
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=5)

TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


@dataclass
class MapLine:
    destination_range_start: int
    source_range_start: int
    range_length: int

    @staticmethod
    def parse_map_line(line_str: str) -> MapLine:
        return MapLine(*[int(x) for x in re.findall(r'\d+', line_str)])

    def map(self, seed: int) -> int:
        return self.destination_range_start + (seed - self.source_range_start)


@dataclass
class Map:
    source_category: str
    destination_category: str
    map_lines: List[MapLine]

    @staticmethod
    def parse_map(map_str: str) -> Map:
        map_header, *map_cntnt = map_str.split('\n')
        source_cat, _, dest_cat, _ = re.split(r'-|\s', map_header)
        return Map(source_cat, dest_cat, [MapLine.parse_map_line(line) for line in map_cntnt])

    def map(self, seed: int) -> int:
        for i, map_line in enumerate(self.map_lines):
            if map_line.source_range_start <= seed < (map_line.source_range_start + map_line.range_length):
                return map_line.map(seed)
        return seed


@dataclass
class Almanac:
    seeds: List[int]
    maps: List[Map]

    @staticmethod
    def parse_almanac(input_str: str) -> Almanac:
        seed_str, *maps_str = input_str.split('\n\n')
        return Almanac([int(x) for x in re.findall(r'\d+', seed_str)], [Map.parse_map(map_str) for map_str in maps_str])

    def map_seed(self, seed: int) -> int:
        return reduce(lambda t, f: f(t), [map.map for map in self.maps], seed)

    @property
    def mapped_seeds(self):
        return map(self.map_seed, self.seeds)


class NewAlmanac(Almanac):
    @staticmethod
    def parse_almanac(input_str: str) -> Almanac:
        almanac = Almanac.parse_almanac(input_str)
        starts = almanac.seeds[::2]
        ranges = almanac.seeds[1::2]

        almanac.seeds = [k for (s, r) in zip(starts, ranges) for k in range(s, s + r)]
        return almanac


def part_one(input_str: str) -> int:
    almanac = Almanac.parse_almanac(input_str)
    return min(almanac.mapped_seeds)


def part_two(input_str: str) -> int:
    almanac = NewAlmanac.parse_almanac(input_str)
    return min(almanac.mapped_seeds)


if __name__ == "__main__":
    # test pt 1
    # print(Almanac.parse_almanac(TEST_INPUT).maps[0])
    # print(Almanac.parse_almanac(TEST_INPUT).maps[0].map(13))

    # a = 98

    # print(98 <= 98 < )
    # print(Almanac.parse_almanac(TEST_INPUT).map_seed(14))

    # # test pt 1
    # print(part_one(TEST_INPUT))

    # # pt 1
    # print(part_one(puzzle.input_data))

    # almanac = NewAlmanac.parse_almanac(TEST_INPUT)

    # print(almanac.seeds)
    # print(len(almanac.seeds))

    # almanac = Almanac.parse_almanac(puzzle.input_data)

    # almanac.maps[0].mapping_dict

    # # test pt 2
    # print(NewAlmanac.parse_almanac(TEST_INPUT).seeds)

    print(part_two(TEST_INPUT))

    # # pt 2
    # print(part_two(puzzle.input_data))
    almanac = Almanac.parse_almanac(puzzle.input_data)
    print(almanac.seeds)
