from __future__ import annotations

from typing import NamedTuple
import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=6)

TEST_INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def count_questions(raw: str) -> int:
    #groups = raw.strip().split('\n\n')
    #sum([len(set(group.replace("\n", ""))) for group in groups])
    return sum([len(set(group.replace("\n", ""))) for group in raw.strip().split('\n\n')])


def count_collective_question(group: str) -> int:
    answer_set_list = [set(answers) for answers in group.split('\n')]
    return len(set.intersection(*answer_set_list))


def count_questions2(raw: str) -> int:
    groups = raw.strip().split('\n\n')
    return sum([count_collective_question(group) for group in groups])
   


if __name__ == "__main__":
    assert count_questions(TEST_INPUT) == 11

    print(count_questions(puzzle.input_data))

    assert count_questions2(TEST_INPUT) == 6

    print(count_questions2(puzzle.input_data))