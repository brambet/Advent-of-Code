from __future__ import annotations

from typing import Callable, DefaultDict, Dict, List, NamedTuple, Optional, Set, Tuple, Union

import numpy as np
from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2022, day=7)

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class File:
    def __init__(self, name: str, size: str | int):
        self.name = name
        self.size = int(size)

    def __repr__(self) -> str:
        return f"{self.name}({self.size})"
    
    def __str__(self) -> str:
        return f"{self.name}({self.size})"


class Directory:
    def __init__(self, name: str, parent: Optional[Directory] = None):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

    def add_file(self, file_name, size):
        self.files.append(File(file_name, size))

    def add_subdirectory(self, dir_name):
        self.subdirs.append(Directory(dir_name, self))    

    @property
    def dir_size(self):
        return sum([file.size for file in self.files] + [subdir.dir_size for subdir in self.subdirs])

    def get_all_dir_sizes(self):
        for subdir in self.subdirs:
            yield from subdir.get_all_dir_sizes()
        yield self.dir_size

    def get_sum_of_sizes_max_100k(self):
        return sum([size for size in self.get_all_dir_sizes() if size <= 100_000])

    def get_smallest_to_delete(self):
        total_size = 70_000_000
        needed_free_space = 30_000_000
        candidates = [size for size in self.get_all_dir_sizes() if self.dir_size - size <= total_size - needed_free_space]
        return min(candidates)

    @staticmethod
    def parse_terminal_output(puzzle_intput: str) -> Directory:
        lines = puzzle_intput.split('\n')
        root = Directory('/')
        current = root
        for line in lines:
            # print(line)
            match line.split():
                case '$', 'cd', '/':
                    # print("changing to root")
                    current = root
                case '$', 'cd', '..':
                    # print(f"going one level up to {current.parent}")
                    current = current.parent
                case '$', 'cd', dir_name:
                    # print(f"changing to directiory {dir_name}")
                    current = [subdir for subdir in current.subdirs if subdir.name == dir_name][0]
                case 'dir', dir_name:
                    # print(f"adding {dir_name} as subdir to {current.name}")
                    current.add_subdirectory(dir_name)
                case size, file_name if size.isdigit():
                    # print(f"adding {file_name} as file in {current.name}")
                    current.add_file(file_name, int(size))
                case _:
                    # print("doing nothing")
                    pass
        return root


if __name__ == "__main__":

    # test pt 1
    root = Directory.parse_terminal_output(TEST_INPUT)
    print(root.get_sum_of_sizes_max_100k())

    #  pt 1
    root = Directory.parse_terminal_output(puzzle.input_data)
    print(root.get_sum_of_sizes_max_100k())

    # test pt 2
    root = Directory.parse_terminal_output(TEST_INPUT)
    print(root.get_smallest_to_delete())

    # test pt 2
    root = Directory.parse_terminal_output(puzzle.input_data)
    print(root.get_smallest_to_delete())
