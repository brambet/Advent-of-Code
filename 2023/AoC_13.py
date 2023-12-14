from __future__ import annotations

import itertools
import re
from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=13)

TEST_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


@dataclass(eq=True, frozen=True)
class Rock:
    x: int
    y: int


@dataclass
class Note:
    X: int
    Y: int
    rocks: Set[Tuple[int, int]]

    @staticmethod
    def parse_note(input_str: str) -> Note:
        lines = input_str.split('\n')
        X = len(lines)
        Y = len(lines[0])
        rocks = {Rock(x, y) for x, line in enumerate(lines, start=1) for y, symbol in enumerate(line, start=1) if symbol == '#'}
        return Note(X, Y, rocks)

    def _rock_on_note(self, rock: Rock) -> bool:
        return (0 < rock.x <= self.X) and (0 < rock.y <= self.Y)

    def horizontal_mirror_line(self):
        for y_line in [0.5 + i for i in range(1, self.Y)]:
            mirror_image = {Rock(rock.x, y_line + (y_line - rock.y)) for rock in self.rocks if self._rock_on_note(Rock(rock.x, y_line + (y_line - rock.y)))}
            if (self.rocks & mirror_image) == mirror_image:
                return y_line
        return 0

    def vertical_mirror_line(self):
        for x_line in [0.5 + i for i in range(1, self.X)]:
            mirror_image = {Rock(x_line + (x_line - rock.x), rock.y) for rock in self.rocks if self._rock_on_note(Rock(x_line + (x_line - rock.x), rock.y))}

            if (self.rocks & mirror_image) == mirror_image:
                return x_line
        return 0

    def note_summary(self, note_number=None) -> int:
        if self.vertical_mirror_line() and self.horizontal_mirror_line():
            print(f'both! on note number {note_number}')
        return 100 * int(self.vertical_mirror_line()) + int(self.horizontal_mirror_line())

    def fix_smudge(self) -> Tuple[int, int, int]:
        old_h = self.horizontal_mirror_line()
        old_v = self.vertical_mirror_line()

        for x, y in itertools.product(range(1, self.X + 1), range(1, self.Y + 1)):
            # old_rocks = self.rocks.copy()
            if Rock(x, y) not in self.rocks:
                self.rocks.add(Rock(x, y))
                new_v = self.vertical_mirror_line()
                new_h = self.horizontal_mirror_line()

                if new_v > 0 and new_v != old_v:
                    return 100 * int(new_v)
                if new_h > 0 and new_h != old_h:
                    return int(new_h)

                # new_summary = self.note_summary() - old_summary
                # if summary > 0:
                #     print(f"Added {Rock(x,y)}")
                #     return x, y, summary
                self.rocks.discard(Rock(x, y))
            else:
                self.rocks.discard(Rock(x, y))
                # summary = self.note_summary() - old_summary
                # if summary > 0:
                #     print(f"Removed {Rock(x,y)}")
                #     print(f"horizontal line: {self.horizontal_mirror_line()}")
                #     print(f"vertical line: {self.vertical_mirror_line()}")

                #     return x, y, summary
                new_v = self.vertical_mirror_line()
                new_h = self.horizontal_mirror_line()

                if new_v > 0 and new_v != old_v:
                    return 100 * int(new_v)
                if new_h > 0 and new_h != old_h:
                    return int(new_h)
                self.rocks.add(Rock(x, y))
        # return 0


def part_one(input_str: str) -> int:
    return sum([Note.parse_note(note).note_summary(i) for i, note in enumerate(input_str.split('\n\n'))])


def part_two(input_str: str) -> int:
    return sum([Note.parse_note(note).fix_smudge() for _, note in enumerate(input_str.split('\n\n'))])


if __name__ == "__main__":
    # print(notes[1].note_summary())
    # # test pt 1
    # print(part_one(TEST_INPUT))

    # # # pt 1
    # print(part_one(puzzle.input_data))

    # note_strings = TEST_INPUT.split('\n\n')

    # print(note_strings[1])

    # note = Note.parse_note(note_strings[0])

    # note.rocks.add(Rock(2, 5))

    # print(note.note_summary())

    # print(note.fix_smudge())

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2
    print(part_two(puzzle.input_data))
