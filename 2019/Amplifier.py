import pandas as pd
import numpy as np
import aocd
import timeit
import os
from aocd.models import Puzzle
from collections import deque
os.environ['AOC_SESSION'] = '53616c7465645f5fda624994231306c055524663b055568600cbd7a8e885d012db0c35ac4c420439e127563fce396857'

class Amplifier():

    def __init__(self, program, phase):
        self.original_program = program
        self.program = self.original_program.copy()
        self.input_values = deque([phase])
        self.output_value = 0
        self.pointer = 0
        self.opcode = 0
        self.modes = []

    def run_opcode(self):
        
        #opcode, mode1, mode2, mode3 = self.get_opcode_and_modes()
        self.get_opcode_and_modes()

        if self.opcode == 99:
             self.run_opcode99()

        elif self.opcode == 1:
            self.run_opcode1()
        
        elif self.opcode == 2:
            self.run_opcode2()
        
        elif self.opcode == 3:
            self.run_opcode3()
        
        elif self.opcode == 4:
            self.run_opcode4()
        
        elif self.opcode == 5:
            self.run_opcode5()
        
        elif self.opcode == 6:
            self.run_opcode6()
        
        elif self.opcode == 7:
            self.run_opcode7()
        
        elif self.opcode == 8:
            self.run_opcode8()

        else:
            print('unknown opcode')


    def run_program(self, input_value=None):
        
        self.input_values.append(input_value)
        self.output_values = []
        self.pointer = 0
        
        while self.pointer > -1:
            self.run_opcode()
            if self.opcode == 4:
                return self.output_value
        
        return None


    def reset_program(self):
        self.program = self.original_program
        

    def get_digit(self, number, n):
        return number // 10**n % 10 


    def get_opcode_and_modes(self):

        opcode_input = self.program[self.pointer]

        self.opcode = opcode_input % 100
        mode1 = self.get_digit(opcode_input, 2)
        mode2 = self.get_digit(opcode_input, 3)
        mode3 = self.get_digit(opcode_input, 4)
        self.modes = [mode1, mode2, mode3]
        #return opcode, mode1, mode2, mode3

    def get_parameter_value(self):
        
        parameter1 = self.program[self.pointer+1]
        
        if self.modes[0]: 
            parameter_value1 = parameter1
        else:
            parameter_value1 = self.program[parameter1]

        return parameter1, parameter_value1


    def get_parameter_values(self):
        
        parameter1 = self.program[self.pointer+1]
        
        if self.modes[0]: 
            parameter_value1 = parameter1
        else:
            parameter_value1 = self.program[parameter1]
        
        parameter2 = self.program[self.pointer+2]
        
        if self.modes[1]: 
            parameter_value2 = parameter2
        else:
            parameter_value2 = self.program[parameter2]
        
        return parameter1, parameter_value1, parameter2, parameter_value2


    def run_opcode99(self):
        self.pointer = -99


    def run_opcode1(self):
        _, parameter_value1, _, parameter_value2 = self.get_parameter_values()
        write_location = self.program[self.pointer+3]
        self.program[write_location] = parameter_value1 + parameter_value2
        self.pointer += 4
        #eturn pointer + 4


    def run_opcode2(self):
        _, parameter_value1, _, parameter_value2 = self.get_parameter_values()
        write_location = self.program[self.pointer+3]
        self.program[write_location] = parameter_value1 * parameter_value2
        self.pointer += 4
        

    def run_opcode3(self):
        #try:
        input_value = self.input_values.popleft()
        #except:
        #    input_value = int(input("Not enough input values given, give input:"))
        #print(input_value)
        write_location = self.program[self.pointer+1]
        self.program[write_location] = input_value
        self.pointer += 2


    def run_opcode4(self):
        parameter1, parameter_value1 = self.get_parameter_value()
        #print(parameter_value1)
        #self.output_value.append(parameter_value1)
        self.output_value = parameter_value1
        self.pointer += 2
        #return pointer + 2


    def run_opcode5(self):
        parameter1, parameter_value1, parameter2, parameter_value2 = self.get_parameter_values()
        if parameter_value1 != 0:
            self.pointer = parameter_value2
        else:
            self.pointer += 3


    def run_opcode6(self):
        parameter1, parameter_value1, parameter2, parameter_value2 = self.get_parameter_values()
        if parameter_value1 == 0:
            self.pointer = parameter_value2
            #return parameter_value2
        else:
            self.pointer += 3
            #pointer += 4
            #return pointer+3

    
    def run_opcode7(self):
        parameter1, parameter_value1, parameter2, parameter_value2 = self.get_parameter_values()
        write_location = self.program[self.pointer+3]
        if parameter_value1 < parameter_value2:
            self.program[write_location] = 1
        else: 
            self.program[write_location] = 0
        
        self.pointer += 4
        #return pointer + 4
    

    def run_opcode8(self):
        parameter1, parameter_value1, parameter2, parameter_value2 = self.get_parameter_values()
        write_location = self.program[self.pointer+3]
        if parameter_value1 == parameter_value2:
            self.program[write_location] = 1
        else: 
            self.program[write_location] = 0
        self.pointer += 4
        #return pointer + 4

   
    

