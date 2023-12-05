from __future__ import annotations

from typing import NamedTuple, Tuple, List
import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=7)

TEST_RULES = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def parse_line(line: str) -> Tuple(str, List[str]):
    parsed_line = line.strip('.').split()

    bag_color = parsed_line[0] + parsed_line[1]
    contain_list = []

    for index, word in enumerate(parsed_line):
        if word.isnumeric():
            count = int(word)
            contain_list = contain_list + count*[parsed_line[index+1]+parsed_line[index+2]]

    return bag_color, contain_list 


def parse_rules(raw: str) -> dict:
    return dict([parse_line(line) for line in raw.split('\n')])


def search_color_tree(target_bag_color: str, outer_bag_color: str, bag_rules: dict) -> bool:
    if target_bag_color in bag_rules[outer_bag_color]:
        return True
    elif bag_rules[outer_bag_color] == []:
        return False
    else:
        # note the set here to speed up things, no need for redundant checks
        return any([search_color_tree(target_bag_color, bag_color, bag_rules) for bag_color in set(bag_rules[outer_bag_color])])
        


def count_possible_outer_colors(target_bag_color: str, bag_rules: dict):
    checks = [search_color_tree(target_bag_color, outer_bag_color, bag_rules) for outer_bag_color in bag_rules.keys()]
    return checks.count(True)


def count_number_of_subbags(target_bag_color: str, bag_rules: dict, count: int =0) -> int:
    for bag_color in bag_rules[target_bag_color]:
            count = count_number_of_subbags(bag_color, bag_rules, count + 1)  
    return count


if __name__ == "__main__":
    assert count_possible_outer_colors('shinygold', parse_rules(TEST_RULES)) == 4

    print(count_possible_outer_colors('shinygold', parse_rules(puzzle.input_data)))

    assert count_number_of_subbags('shinygold', parse_rules(TEST_RULES)) == 32

    print(count_number_of_subbags('shinygold', parse_rules(puzzle.input_data)))
