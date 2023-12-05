from __future__ import annotations

from typing import NamedTuple
import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=5)

TEST1 = "BFFFBBFRRR"
TEST2 = "FFFBBBFRRR"
TEST3 = "BBFFBBFRLL"

# int("FBFBBFF".replace("F", "0").replace("B","1"),2)


# class Password(NamedTuple):
#     lo: int
#     hi: int
#     char: str
#     password: str


class BoardingPass(NamedTuple):
    row: int
    column: int
    ID: int

    @staticmethod
    def parse(raw: str) -> BoardingPass:
        row = int(raw[:7].replace("F", "0").replace("B","1"),2)
        column = int(raw[-3:].replace("R", "1").replace("L","0"),2)
        return BoardingPass(row, column, row*8 + column)


if __name__ == "__main__":
    #testing
    assert(BoardingPass.parse(TEST1) == BoardingPass(70,7,567))
    assert(BoardingPass.parse(TEST2) == BoardingPass(14,7,119))
    assert(BoardingPass.parse(TEST3) == BoardingPass(102,4,820))

    # define boarding passes
    boardingpasses = [BoardingPass.parse(line) for line in puzzle.input_data.split('\n')]

    seat_IDs = [boardingpass.ID for boardingpass in boardingpasses] 
    print(max(seat_IDs))

    # candidates = set(range(8,8*126+7)).difference(seat_IDs)
    # print([id for id in candidates if set([id+1, id-1]).issubset(seat_IDs)])

    seat = [id for id in range(8,8*126+7) if id+1 in seat_IDs and id-1 in seat_IDs and id not in seat_IDs]
    print(seat)
  