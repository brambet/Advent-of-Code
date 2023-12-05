from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2020, day=1)

# parse input
input_list = [int(number) for number in puzzle.input_data.split('\n')]

answer = 0

for n1 in input_list:
    for n2 in input_list:
        if n1 + n2 == 2020:
            answer = n1*n2




print(answer)

answer2 = 0

for n1 in input_list:
    for n2 in input_list:
        for n3 in input_list:        
            if n1 + n2 + n3 == 2020:
                answer2 = n1*n2*n3


print(answer2)