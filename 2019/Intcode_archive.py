import pandas as pd
import numpy as np
import aocd
import timeit
import os
from aocd.models import Puzzle
os.environ['AOC_SESSION'] = '53616c7465645f5fda624994231306c055524663b055568600cbd7a8e885d012db0c35ac4c420439e127563fce396857'






def get_digit(number, n):
    return number // 10**n % 10

def get_opcode_and_modes(opcode_input):
    opcode_string = str(opcode_input)

    opcode = opcode_input % 100
    mode1 = get_digit(opcode_input, 2)
    mode2 = get_digit(opcode_input, 3)
    mode3 = get_digit(opcode_input, 4)

    return opcode, mode1, mode2, mode3


def get_parameter_value(input_array, pointer, mode1):
    
    parameter1 = input_array[pointer+1]
    
    if mode1: 
        parameter_value1 = parameter1
    else:
        parameter_value1 = input_array[parameter1]

    return parameter1, parameter_value1


def get_parameter_values(input_array, pointer, mode1, mode2):
    
    parameter1 = input_array[pointer+1]
    
    if mode1: 
        parameter_value1 = parameter1
    else:
        parameter_value1 = input_array[parameter1]
    
    parameter2 = input_array[pointer+2]
    
    if mode2: 
        parameter_value2 = parameter2
    else:
        parameter_value2 = input_array[parameter2]
    
    return parameter1, parameter_value1, parameter2, parameter_value2


def run_opcode99(input_array, pointer, mode1, mode2):
    #pointer = -99
    return -1


def run_opcode1(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    write_location = input_array[pointer+3]
    input_array[write_location] = parameter_value1 + parameter_value2
    #pointer += 4
    return pointer + 4


def run_opcode2(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    write_location = input_array[pointer+3]
    input_array[write_location] = parameter_value1 * parameter_value2
    #pointer += 4
    return pointer + 4


def run_opcode3(input_array, pointer, mode1, mode2, input_values):
    if input_values is None:
        input_value = input("Give input:") 
    else:
        input_value = next(input_values)
    write_location = input_array[pointer+1]
    input_array[write_location] = input_value
    #pointer += 4
    return pointer + 2


def run_opcode4(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1 = get_parameter_value(input_array, pointer, mode1)
    print(parameter_value1)
    #pointer += 2
    return pointer + 2


def run_opcode5(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    if parameter_value1 != 0:
        return parameter_value2
    else:
        #pointer += 4
        return pointer+3


def run_opcode6(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    if parameter_value1 == 0:
        #pointer = parameter_value2
        return parameter_value2
    else:
        #pointer += 4
        return pointer+3

    
def run_opcode7(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    write_location = input_array[pointer+3]
    if parameter_value1 < parameter_value2:
        input_array[write_location] = 1
    else: 
        input_array[write_location] = 0
    
    #pointer += 4
    return pointer + 4
    

def run_opcode8(input_array, pointer, mode1, mode2):
    parameter1, parameter_value1, parameter2, parameter_value2 = get_parameter_values(input_array, pointer, mode1, mode2)
    write_location = input_array[pointer+3]
    if parameter_value1 == parameter_value2:
        input_array[write_location] = 1
    else: 
        input_array[write_location] = 0
    #pointer += 4
    return pointer + 4

   
    
def run_opcode(input_array, pointer, input_values=None, print_opcode=False):
    
    opcode, mode1, mode2, mode3 = get_opcode_and_modes(input_array[pointer])
    
    if print_opcode:
        print(opcode)
    
    if opcode == 99:
        return run_opcode99(input_array, pointer, mode1, mode2)

    elif opcode == 1:
        return run_opcode1(input_array, pointer, mode1, mode2)
    
    elif opcode == 2:
        return run_opcode2(input_array, pointer, mode1, mode2)
    
    elif opcode == 3:
        return run_opcode3(input_array, pointer, mode1, mode2, input_values)
    
    elif opcode == 4:
        return run_opcode4(input_array, pointer, mode1, mode2)
    
    elif opcode == 5:
        return run_opcode5(input_array, pointer, mode1, mode2)
    
    elif opcode == 6:
        return run_opcode6(input_array, pointer, mode1, mode2)
    
    elif opcode == 7:
        return run_opcode7(input_array, pointer, mode1, mode2)
    
    elif opcode == 8:
        return run_opcode8(input_array, pointer, mode1, mode2)

    else:
        print('unknown opcode')


def run_Intcode(inp_array, input_values=None, print_opcodes=False):
    
    input_array = inp_array.copy()
    
    if input_values is not None:
        if type(input_values) is int:
            input_values = [input_values]
        print(input_values)
        input_values = iter(input_values)
    
    pointer = 0
    while pointer > -1:
        #print(pointer)
        pointer = run_opcode(input_array, pointer, input_values, print_opcodes)
        
        #index += 4
    return input_array
