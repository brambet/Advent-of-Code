from aocd.models import Puzzle
from typing import List, NamedTuple, Dict, Callable, DefaultDict, Tuple, Union, Set
from collections import Counter
from math import factorial
# get puzzle
puzzle = Puzzle(year=2021, day=8)

TEST_INPUT = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def convert_set_to_number(number_set) -> int:
    if set(number_set) == set('abcef'):
        return 0
    if set(number_set) == set('cf'):
        return 1
    if set(number_set) == set('acdeg'):
        return 2
    if set(number_set) == set('acdfg'):
        return 3
    if set(number_set) == set('bcdf'):
        return 4
    if set(number_set) == set('abdfg'):
        return 5
    if set(number_set) == set('abdefg'):
        return 6
    if set(number_set) == set('acf'):
        return 7
    if set(number_set) == set('abcdefg'):
        return 8
    if set(number_set) == set('abcdfg'):
        return 9


class SignalLine():

    def __init__(self, input_line: str):
        self.input_signals, self.output_signals = [{set(signal) for signal in part.split()}
                                                   for part in input_line.split('|')]

        self.mapping = dict()

    def count_unique_length_signals_in_output(self) -> int:
        counter = Counter([len(signal) for signal in self.output_signals])
        return counter[2] + counter[3] + counter[4] + counter[7]

    # def print_input_lengths(self):
    #     print([len(signal) for signal in self.input_signals])

    def deduce_a(self):


def part_one(input_str: str) -> int:
    return sum([SignalLine(line).count_unique_length_signals_in_output() for line in input_str.split('\n')])


if __name__ == '__main__':

    # test_line = SignalLine(TEST_INPUT.split('\n')[1])
    # print(test_line.output_signals)
    # test_line.print_input_lengths()
    # # lengths = [len(signal) for signal in test_line.output_signals]
    # # print(lengths)

    # print(test_line.count_unique_length_signals_in_output())
    # test pt 1
    print(part_one(TEST_INPUT))

    # pt 1
    # print(part_one(puzzle.input_data))

    #
    # print(set('cf') == set(set('cf')))
    print(convert_set_to_number('cf'))
