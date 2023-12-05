# from __future__ import annotations

from typing import NamedTuple, Tuple, List
from aocd.models import Puzzle
from collections import Counter
from operator import itemgetter
import numpy as np
from itertools import combinations, product
import math
puzzle = Puzzle(year=2020, day=13)
import time
from math import cos, sin, pi, sqrt, floor, ceil

TEST_INPUT = """939
7,13,x,x,59,x,31,19"""

TEST_INPUT2 = """
17,x,13,19"""

TEST_OUTPUT2 = 3417

TEST_INPUT3 = """
67,7,59,61"""

TEST_OUTPUT3 = 754018

TEST_INPUT4 = """
67,x,7,59,61"""

TEST_OUTPUT4 = 779210

TEST_INPUT5 = """
67,7,x,59,61"""

TEST_OUTPUT5 = 1261476

TEST_INPUT6 = """
1789,37,47,1889"""

TEST_OUTPUT6 = 1202161486

def parse(input: str):
    depart_time, notes = input.split('\n')
    ids = [int(id) for id in notes.split(',') if id != 'x']
    return int(depart_time), ids


def parse2(input: str):
    depart_time, notes = input.split('\n')
    id_and_difs = [(int(id), idx) for idx,id in enumerate(notes.split(',')) if id != 'x']
    return id_and_difs


depart_time, ids = parse(TEST_INPUT)

def get_first_departures(depart_time, ids):
    return [(floor(depart_time/id)+ 1)*id for id in ids]


def pt1(input):
    depart_time, ids = parse(input)
    first_departures = get_first_departures(depart_time, ids)
    minimum = min(enumerate(first_departures), key = itemgetter(1))
    return (minimum[1]-depart_time)*ids[minimum[0]]


assert pt1(TEST_INPUT) == 295

print(pt1(puzzle.input_data))


def check_if_fits_requirements(start_number, id_and_difs):
    return all([(start_number + dif)%id == 0 for id,dif in id_and_difs])


def pt2(input):
    id_and_difs = parse2(input)
    time, increment = 1, 1
    for id, dif in id_and_difs:
        while (time + dif) % id != 0:
            time += increment
        increment *= id
    return time

    # for i in range(len(id_and_difs)):
    #     result = False
    #     while not result:
    #         result = check_if_fits_requirements(time, id_and_difs[:i+1])
    #         time += increment
    #     increment *= id_and_difs[i][0]
    # return time
    # leading_id = id_and_difs[0][0]
    # iter = floor(start_order_of_magnitude / leading_id)
    # in
    # result = False
    # while not result:
    #     iter += 1
    #     result = check_if_fits_requirements(iter*leading_id, id_and_difs)
    # return iter*leading_id


# print(check_if_fits_requirements(1068781, parse2(TEST_INPUT)))


# print(pt2(puzzle.input_data, 100000000000000))


tic = time.perf_counter()
assert pt2(TEST_INPUT2) == TEST_OUTPUT2
toc = time.perf_counter()
print(f"Simulation step  took {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# assert pt2(TEST_INPUT3, 0) == TEST_OUTPUT3
# toc = time.perf_counter()
# print(f"Simulation step  took {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# assert pt2(TEST_INPUT4, 0) == TEST_OUTPUT4
# toc = time.perf_counter()
# print(f"Simulation step  took {toc - tic:0.4f} seconds")

# tic = time.perf_counter()
# assert pt2(TEST_INPUT5, 0) == TEST_OUTPUT5
# toc = time.perf_counter()
# print(f"Simulation step  took {toc - tic:0.4f} seconds")


# tic = time.perf_counter()
# assert pt2(TEST_INPUT6, 0) == TEST_OUTPUT6
# toc = time.perf_counter()
# print(f"Simulation step  took {toc - tic:0.4f} seconds")

tic = time.perf_counter()
print(pt2(puzzle.input_data))
toc = time.perf_counter()
print(f"Simulation step  took {toc - tic:0.4f} seconds")


from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
print(chinese_remainder([id for id,_ in parse2(TEST_INPUT)], [dif for _,dif in parse2(TEST_INPUT)]))