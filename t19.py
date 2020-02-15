#!python3
import sys

from attr import attrs, attrib


@attrs
class Computer:
    reg = attrib(default=None)
    ip_reg = attrib(default=None)
    program = attrib(default=None)

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


    def load_program(self):
        assert len(sys.argv) == 2

        self.program = dict()
        inp = open(sys.argv[1]).read().split('\n')

        for x, row in enumerate(inp):
            if x == 0:
                nothing, self.ip_reg = row.split(' ')
                self.ip_reg = int(self.ip_reg)

            elif row != '':
                self.instr = list(map(str,row.split(' ')))
                self.instr[1] = int(self.instr[1])
                self.instr[2] = int(self.instr[2])
                self.instr[3] = int(self.instr[3])

                self.program[x-1] = self.instr



    def run_program(self, to_print):

        ip = self.reg[self.ip_reg]
        print(ip)
        print(self.ip_reg)
        while ip < len(self.program) :
            self.reg[self.ip_reg] = ip
            self.instr = self.program[ip]
            self.ops(self.program[ip][0])
            ip = self.reg[self.ip_reg]
            ip += 1
            if to_print:
                print(ip, self.reg, self.reg[self.ip_reg])

    def main(self,to_print = None):
        self.load_program()
        print(self.program)

        self.run_program(to_print)

        return self.reg[0]

from math import sqrt

def divisors(n):
    divs = [1]
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))

if __name__ == '__main__':
    comp = Computer([0,0,0,0,0,0],0,None)
    print('Part 1 :',comp.main())

    print('Part 2 :',int(sum(divisors(10551282))))
