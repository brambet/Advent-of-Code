from __future__ import annotations
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=16)
from typing import NamedTuple, Tuple, List, Deque, DefaultDict
import time
import re

TEST_INPUT = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

TEST_INPUT2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

class Field(NamedTuple):
    name : str
    range : List[Tuple[int, int]]

    @staticmethod 
    def parse_field(field_line: str) -> Field:
        name = field_line.split(':')[0]
        boundaries = [int(x) for x in re.findall(r'\d+', field_line)]
        range = [(boundaries[0], boundaries[1]), (boundaries[2], boundaries[3])]
        return Field(name=name,range=range)


    def check_value_in_range(self, value:int)->bool:
        return any([lower <= value <= upper for lower, upper in self.range])



class FieldValidator():
    fields : List[Field]
    my_ticket : List[int]
    nearby_tickets : List[List[int]]

    def __init__(self, input_str):
        fields_str, ticket_str, nearby_tickets_str = input_str.split('\n\n')
        self.fields = [Field.parse_field(line) for line in fields_str.split('\n')]
        self.my_ticket = [int(x) for x in ticket_str.split('\n')[1].split(',')]
        self.nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_tickets_str.split('\n')[1:]]


    def error_rate_nearby_tickets(self):
        error_rate = 0
        for ticket in self.nearby_tickets:
            for ticket_field_value in ticket:
                if not any([field.check_value_in_range(ticket_field_value) for field in self.fields]):
                    error_rate += ticket_field_value
        return error_rate


    def select_valid_tickets(self):
        in_valid_tickets = []
        for ticket in self.nearby_tickets:
            for ticket_field_value in ticket:
                if not any([field.check_value_in_range(ticket_field_value) for field in self.fields]):
                    in_valid_tickets.append(ticket)
        self.valid_tickets = [ticket for ticket in self.nearby_tickets if ticket not in in_valid_tickets]          
        return self.valid_tickets


    def determine_possible_positions(self):
        self.select_valid_tickets()
        # self.correctly_ordered_fields = []
        possible_positions = DefaultDict(list)
        self.valid_tickets.append(self.my_ticket)
        transposed_fields = [list(field_values) for field_values in zip(*(self.valid_tickets))]
        for position, field_values in enumerate(transposed_fields):
            for field in self.fields:
                if all([field.check_value_in_range(value) for value in field_values]):
                    possible_positions[field.name].append(position)
                    # self.correctly_ordered_fields.append(field)
                    # self.fields.remove(field)

        return possible_positions #self.correctly_ordered_fields

    def determine_field_order(self):
        possible_positions = self.determine_possible_positions()

        determined_positions = {}
        i = 0
        while len(possible_positions) > 0 :#not all([len(posibilities) == 1 for posibilities in possible_positions.values()]):
            
            for name in possible_positions.keys():
                possible_positions[name] = [posibility for posibility in possible_positions[name] if posibility not in determined_positions.values()]

            singles = {name : value[0] for name,value in possible_positions.items() if len(value) == 1}
            determined_positions.update(singles)
            possible_positions = {key: value for key, value in possible_positions.items() if key not in singles.keys()}

        return determined_positions
                
    def pt2(self):
        determined_positions = self.determine_field_order()
        answer = 1
        for key, value in determined_positions.items():
            if key.startswith('departure'):
               answer *= self.my_ticket[value]

        return answer 
                


print(FieldValidator(TEST_INPUT2).determine_field_order())

print(FieldValidator(puzzle.input_data).pt2())
