#!python3
import sys

from dataclasses import dataclass
from collections import defaultdict
from copy import deepcopy


@dataclass
class Computer:
    reg: list
    instr: list


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
#        print("Comparing ",self.reg," and ",cmp_reg)
        if self.reg == cmp_reg:
            return 1
        else:
            return 0


# ---------- MAIN --------

result = 0 

assert len(sys.argv) == 2

inp = open(sys.argv[1]).read().split('\n')

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

        # ADD
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.addr()
        if comp.is_reg_eq(out_reg):
            print("addr behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.addi()
        print(comp)
        print("returned ",comp.is_reg_eq(out_reg))
        if comp.is_reg_eq(out_reg):
            print("addi behaves")
        matches += comp.is_reg_eq(out_reg)

        # MULTIPLY
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.mulr()
        if comp.is_reg_eq(out_reg):
            print("mulr behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.muli()
        if comp.is_reg_eq(out_reg):
            print("muli behaves")
        matches += comp.is_reg_eq(out_reg)

        # AND
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.banr()
        if comp.is_reg_eq(out_reg):
            print("banr behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.bani()
        if comp.is_reg_eq(out_reg):
            print("bani behaves")
        matches += comp.is_reg_eq(out_reg)       

        # OR
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.borr()
        if comp.is_reg_eq(out_reg):
            print("borr behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.bori()
        if comp.is_reg_eq(out_reg):
            print("bori behaves")
        matches += comp.is_reg_eq(out_reg)

        # SET 
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.setr()
        if comp.is_reg_eq(out_reg):
            print("setr behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.seti()
        if comp.is_reg_eq(out_reg):
            print("seti behaves")
        matches += comp.is_reg_eq(out_reg)

        # GT
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.gtir()
        if comp.is_reg_eq(out_reg):
            print("gtir behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.gtri()
        if comp.is_reg_eq(out_reg):
            print("gtri behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.gtrr()
        if comp.is_reg_eq(out_reg):
            print("gtrr behaves")
        matches += comp.is_reg_eq(out_reg)

        # EQ
        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.eqir()
        if comp.is_reg_eq(out_reg):
            print("eqir behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.eqri()
        if comp.is_reg_eq(out_reg):
            print("eqri behaves")
        matches += comp.is_reg_eq(out_reg)

        comp = Computer(deepcopy(inp_reg),deepcopy(instr))
        comp.eqrr()
        if comp.is_reg_eq(out_reg):
            print("eqrr behaves")
        matches += comp.is_reg_eq(out_reg)

        print(instr, ' ',matches,' ',result,' ',end='')

        if matches >= 3:
            result += 1
        
        print(matches >= 3)
        #input()
    elif row == '':
        emptycount += 1

    else:
        # instr
        instr = list(map(int,row.split(' ')))

    if emptycount ==2 :
        break

print("Part 1 ",result)
