#!python3
import sys

from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy


@dataclass
class Computer:
    reg: list
    instr: list

    def ops(self, what):
        method_name=what
        method=getattr(self,method_name,lambda :'Invalid')
        return method()

    def addr(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] + self.reg[self.instr[2]]
    
    def addi(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] + self.instr[2]

    def mulr(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] * self.reg[self.instr[2]]
    
    def muli(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] * self.instr[2]

    def banr(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] & self.reg[self.instr[2]]
    
    def bani(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] & self.instr[2]

    def borr(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] | self.reg[self.instr[2]]
    
    def bori(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]] | self.instr[2]

    def setr(self):
        self.reg[self.instr[3]] = self.reg[self.instr[1]]
    
    def seti(self):
        self.reg[self.instr[3]] = self.instr[1]

    def gtir(self):
        self.reg[self.instr[3]] = 1 if self.instr[1] > self.reg[self.instr[2]] else 0
    
   
    def gtri(self):
        self.reg[self.instr[3]] = 1 if self.reg[self.instr[1]] > self.instr[2] else 0
        
   
    def gtrr(self):
        self.reg[self.instr[3]] = 1 if self.reg[self.instr[1]] > self.reg[self.instr[2]] else 0
        

    def eqir(self):
        self.reg[self.instr[3]] = 1 if self.instr[1] == self.reg[self.instr[2]] else 0

   
    def eqri(self):
        self.reg[self.instr[3]] = 1 if self.reg[self.instr[1]] == self.instr[2] else 0
        
   
    def eqrr(self):
        self.reg[self.instr[3]] = 1 if self.reg[self.instr[1]] == self.reg[self.instr[2]] else 0
        

    def is_reg_eq(self, cmp_reg):
        if self.reg == cmp_reg:
            return 1
        else:
            return 0


# ---------- MAIN --------

known_opcodes = defaultdict(str)
opcode_dir = defaultdict(int)

opcodes = ["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"]

assert len(sys.argv) == 2

inp = open(sys.argv[1]).read().split('\n')

result = 0

while len(known_opcodes) < 16:
#for i in range(1):
    

    emptycount = 0
    inp_reg = []
    out_reg = []
    instr = []

    for x, row in enumerate(inp):
        if row.startswith('Before'):
            inp_reg = list(map(int,row.split(': ')[1].strip('[').strip(']').strip(' ').split(',')))

        elif row.startswith('After'):
            out_reg = list(map(int,row.split(':  ')[1].strip('[').strip(']').strip(' ').split(',')))
            emptycount = 0

            matches = 0

            matching_codes = []

            for opcode in opcodes:
                if opcode not in opcode_dir:

                    comp = Computer(deepcopy(inp_reg),deepcopy(instr))
                    comp.ops(opcode)
                    if comp.is_reg_eq(out_reg):
                        matching_codes.append(opcode)

            if (len(matching_codes) == 1):
                known_opcodes[instr[0]] = matching_codes[0]
                opcode_dir[matching_codes[0]] = instr[0]

            #input()
        elif row == '':
            emptycount += 1

        else:
            # instr
            instr = list(map(int,row.split(' ')))

        if emptycount ==2 :
            break

emptycount = 0
do_program = 0
regs = [0,0,0,0]
comp = Computer(regs,[0,0,0,0])

for x, row in enumerate(inp):

    if do_program == 0:
        if row == '':
            emptycount+=1
        else:
            emptycount = 0

        if emptycount == 3:
            do_program = 1

    else:
        if row != '':
             instr = list(map(int,row.split(' ')))       
             comp = Computer(regs,instr)
             comp.ops(known_opcodes[instr[0]])

print(comp.reg[0])
