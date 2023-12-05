from aocd.models import Puzzle

# get puzzle
puzzle = Puzzle(year=2021, day=1)


# parse input
input_list = [int(number) for number in puzzle.input_data.split('\n')]

# part 1
increasing = 0
for number, next_number in zip(input_list, input_list[1:]):
    if next_number > number:
        increasing += 1


print(increasing)

# part 2
increasing = 0
for number, fourth_number in zip(input_list, input_list[3:]):
    if fourth_number > number:
        increasing += 1

print(increasing)
