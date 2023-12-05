from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, DefaultDict, Dict, List, NamedTuple, Set, Tuple, Union

from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2023, day=2)

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


@dataclass
class Draw:
    red: int
    green: int
    blue: int

    @staticmethod
    def parse_draw_string(draw_str) -> Draw:
        red, green, blue = 0, 0, 0
        for draw_part in draw_str.split(','):
            match draw_part:
                case str(x) if 'red' in x:
                    red = int(draw_part.replace('red', ''))
                case str(x) if 'green' in x:
                    green = int(draw_part.replace('green', ''))
                case str(x) if 'blue' in x:
                    blue = int(draw_part.replace('blue', ''))
        return Draw(red, green, blue)


@dataclass
class Game:
    id: int
    draws: List[Draw]

    @staticmethod
    def parse_game_string(game_str):
        id_str, moves_str = "".join(game_str.split()).split(":")
        id = int(id_str[4:])
        draws = [Draw.parse_draw_string(draw_str) for draw_str in moves_str.split(";")]
        return Game(id=id,draws=draws)

    def determine_possible_game(self, red: int, green:int, blue:int)->bool:
        for draw in self.draws:
            if any([draw.red > red, draw.green > green, draw.blue > blue]):
                return 0
        return self.id
    
    def determine_game_power(self):
        red, green, blue = self.draws[0].red, self.draws[0].green, self.draws[0].blue
        for draw in self.draws[1:]:
            if draw.red > red:
                red = draw.red
            if draw.green > green:
                green = draw.green
            if draw.blue > blue:
                blue = draw.blue

        return red*green*blue

def part_one(input_str: str, game_limit: Dict[str, int]) -> int:
    return sum([Game.parse_game_string(game_str).determine_possible_game(**game_limit) for game_str in input_str.split('\n')])

def part_two(input_str: str) -> int:
    # games = [Game.parse_game_string(game_str) for game_str in input_str.split('\n')]
    # return sum([game.determine_game_power(**game_limit) for game in games if game.determine_possible_game(**game_limit) > 0])
    return sum([Game.parse_game_string(game_str).determine_game_power() for game_str in input_str.split('\n')])


if __name__ == "__main__":

    game_limit = {"red": 12, "green": 13, "blue": 14}

    # test pt 1
    print(part_one(TEST_INPUT, game_limit))

    # pt 1
    print(part_one(puzzle.input_data, game_limit))

    # test pt 2
    print(part_two(TEST_INPUT))

    # pt 2 
    print(part_two(puzzle.input_data))
