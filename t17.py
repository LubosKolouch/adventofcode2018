#!python3

import sys
import numpy as np
from attr import attrs, attrib

@attrs
class Water_runner:
    field = attrib(default = None)
    work_q = attrib(default = None)
    min_x = attrib(default = None)
    min_y = attrib(default = None)
    max_x = attrib(default = None)
    max_y = attrib(default = None)


    def print_field(self,what):
        for x in range(self.min_x, self.max_x + 2):
            row = ''
            for y in range(self.min_y, self.max_y + 2):
                row += str(what.get((x, y), ' '))
            print(row)

        return 0


    def check_still(self,x,y):
        if self.field[x,y] == "|" :

            mod_water = dict()

            ok_water = 1
            pos_y = y

            # LEFT
            while ok_water:
                if self.field.get((x,pos_y),'.') == '.':
                    return 1
                if self.field.get((x,pos_y),'.') == '#': 
                    break
                
                mod_water[x,pos_y] = '~'
                pos_y -= 1

            pos_y = y
            # RIGHT
            while ok_water:
                if self.field.get((x,pos_y),'.') == '.':
                    return 1
                if self.field.get((x,pos_y),'.') == '#': 
                    break

                mod_water[x,pos_y] = '~'
                pos_y += 1
            if ok_water:
                for a, b in mod_water:
                    self.field[a,b] = '~'
                    if self.work_q.get((a,b),'') != '':
                        del self.work_q[a,b]
                    if self.field.get((a-1,b),'') == '|':
                        self.work_q[a-1,b] =1

        return 1

    def load_field(self,inp):

        self.max_x = self.max_y = 0
        self.min_x = self.min_y = 99999

        self.field = dict()

        for row in inp:
            first, second = row.split(', ')
            f1, f2 = first.split('=')
            s1, s2 = second.split('=')
            f2 = int(f2)
            sfr,sto = list(map(int,s2.split('..')))

            if f1 == 'y':
                for i in range(sfr,sto+1):
                    self.field[f2,i] = '#'

            else:
                for i in range(int(sfr),sto+1):
                    self.field[i,f2] = '#' 

        self.min_x = min([square[0] for square in self.field])
        self.max_x = max([square[0] for square in self.field])
        self.min_y = min([square[1] for square in self.field])
        self.max_y = max([square[1] for square in self.field])

        return 1


    def run_round(self):
        for x,y in list(self.work_q):

            if self.work_q.get((x,y),'') == '':
                continue

            if x >= self.max_x:
                del self.work_q[x,y]
                continue

            what_below = str(self.field.get((x+1,y),'.'))

            # drop down
            if what_below == '.':
                self.field[x+1,y] = '|'
                self.work_q[x+1,y] = 1
                if self.work_q.get((x,y),'') != '':
                        del self.work_q[x,y]
                continue

            if what_below == '#' or what_below == "~":
                # left
                if self.field.get((x,y-1),'.') == '.':
                    self.field[x,y-1] = '|'
                    self.work_q[x,y-1] = 1
                # right
                elif self.field.get((x,y+1),'.') == '.':
                    self.field[x,y+1] = '|'
                    self.work_q[x,y+1] = 1
                if self.field.get((x,y-1),'') in ['|','#'] and self.field.get((x,y+1),'') in ['|','#']:
                    del self.work_q[x,y]

                # check if the row is still
                self.check_still(x,y)
        return 1


    def main(self):

        assert len(sys.argv) == 2

        inp = open(sys.argv[1]).read().strip().split('\n')
        self.load_field(inp)
        orig_len = len(self.field)
        self.field[0,500] = '|'

        self.work_q = dict()
        self.work_q[0,500] = '|'
        i=0
        while len(self.work_q) != 0:
            i+=1
            prev_q = list(self.work_q)
            self.run_round()
            after_q = list(self.work_q)

            if prev_q == after_q:
                break

        cur_run2 = 0

        cur_run =  len([square for square in self.field if square[0] <= self.max_x and square[0] >= self.min_x and self.field[square] in ['|', '~']])
        curr_still =  len([square for square in self.field if self.field[square] == '~'])
        print("water : ",cur_run,'still ',curr_still)

wr = Water_runner()
wr.main()
