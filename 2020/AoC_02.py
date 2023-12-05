from aocd.models import Puzzle
from typing import NamedTuple


# get puzzle
puzzle = Puzzle(year=2020, day=2)


input_list = puzzle.input_data.split('\n')

INPUTS = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]


class PassWord():
    line : str
    low : int
    high : int
    char : str
    password : str

    def __init__(self, line):
        self.line = line

        counts, self.char, self.password = line.strip().split()
        self.char = self.char[0]
        self.low = int(counts.split('-')[0])
        self.high = int(counts.split('-')[1])
        
    
    def is_valid(self):

        return self.low <= self.password.count(self.char) <= self.high


    def is_valid2(self):

        return ((self.password[self.low-1] == self.char) !=  (self.password[self.high-1] == self.char)) 



print([PassWord(line).is_valid() for line in INPUTS].count(True))

print([PassWord(line).is_valid() for line in input_list].count(True))

print([PassWord(line).is_valid2() for line in INPUTS].count(True))

print([PassWord(line).is_valid2() for line in input_list].count(True))