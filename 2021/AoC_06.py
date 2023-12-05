from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set
from collections import Counter
# get puzzle
puzzle = Puzzle(year=2021, day=6)

TEST_INPUT = """3,4,3,1,2"""


class LanternFish():

    def __init__(self, internal_timer: int):
        self.internal_timer = internal_timer

    def __repr__(self) -> str:
        return str(self.internal_timer)

    def next_day(self):
        if self.internal_timer == 0:
            self.internal_timer = 6
            return [self, LanternFish(internal_timer=8)]
        else:
            self.internal_timer -= 1
            return [self]


class SchoolOfLanterFishes():

    def __init__(self, input_str: str):
        self.school = [LanternFish(int(timer))
                       for timer in input_str.split(',')]

    def simulate(self, last_day):
        day = 0
        while day < last_day:
            day += 1
            nested_school = [fish.next_day() for fish in self.school]
            self.school = [fish for nest in nested_school for fish in nest]


class AggregatedSchoolOfLanterFishes():

    def __init__(self, input_str: str):
        initial_school = [int(timer) for timer in input_str.split(',')]
        self.school_counts = Counter(initial_school)

    def next_day(self):
        new_counts = {t: self.school_counts.get(t+1, 0) for t in range(8)}
        new_counts[6] += self.school_counts[0]
        new_counts[8] = self.school_counts[0]
        self.school_counts = new_counts

    def simulate(self, last_day: int):

        for _ in range(last_day):
            self.next_day()

        return sum(self.school_counts.values())


if __name__ == '__main__':

    # test pt 1
    school = AggregatedSchoolOfLanterFishes(TEST_INPUT)
    print(school.simulate(80))

    # pt 1
    school = AggregatedSchoolOfLanterFishes(puzzle.input_data)
    print(school.simulate(80))

    # test pt 2
    school = AggregatedSchoolOfLanterFishes(puzzle.input_data)
    print(school.simulate(256))
