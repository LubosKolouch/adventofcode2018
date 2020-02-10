#!python3

import sys
from collections import defaultdict
import numpy as np
from attr import attrs, attrib

@attrs
class Water_runner:
    water = attrib(default = None)
    field = attrib(default = None)
    min_x = attrib(default = None)
    min_y = attrib(default = None)
    max_x = attrib(default = None)
    max_y = attrib(default = None)


    def print_field(self,what):
        #print(what.items())

        for x in range(self.min_x, self.max_x + 1):
            row = ''
            for y in range(self.min_y, self.max_y + 1):
                row += what.get((x, y), ' ')
            print(row)

        return 0


    def check_still(self,x,y):

    #    print("WAT TEST ",x,y)
        if self.water[(x,y)] == "|" :

            mod_water = defaultdict(str)

            ok_water = 1
            pos_y = y

            # LEFT
            while ok_water:
    #           print("Testing left",x,pos_y)
                if self.field.get((x,pos_y),'.') == '.':
                    return 1
                if self.field.get((x,pos_y),'.') == '#': 
                    break
                
                mod_water[x,pos_y] = '~'
                pos_y -= 1

            pos_y = y
            # RIGHT
            while ok_water:
                #print("Testing right",x,pos_y)
                if self.field.get((x,pos_y),'.') == '.':
                    return 1
                if self.field.get((x,pos_y),'.') == '#': 
                    break

                mod_water[x,pos_y] = '~'
                pos_y += 1

            if ok_water:
                for x, y in mod_water:
                    self.water[x,y] = mod_water[x, y]
                    self.field[x,y] = mod_water[x, y]

        return 1

    def load_field(self,inp):

        self.max_x = self.max_y = 0
        self.min_x = self.min_y = 99999

        self.field = defaultdict(str)

        for row in inp:
            first, second = row.split(', ')
            f1, f2 = first.split('=')
            s1, s2 = second.split('=')
            f2 = int(f2)
            sfr,sto = list(map(int,s2.split('..')))

            if f1 == 'y':
                for i in range(sfr,sto+1):
                    self.field[(f2,i)] = '#'

            else:
                for i in range(int(sfr),int(sto)+1):
                    self.field[(i,f2)] = '#' 

        self.min_x = min([square[0] for square in self.field])
        self.max_x = max([square[0] for square in self.field])
        self.min_y = min([square[1] for square in self.field])
        self.max_y = max([square[1] for square in self.field])

        return 1


    def run_round(self):

        self.water[(0,500)] = '+'
    #    print_self.field(self.field_c,self.max_x,self.max_y,self.min_x,self.min_y)
        sq = [square for square in self.water if square[1] <= self.max_y and square[1] >= self.min_y and self.water[square] in ['|','+']]
        for x,y in sq:
            if x > self.max_x or y > self.max_y:
                break
            what_below = str(self.field.get((x+1,y),'.'))

            # drop down
            if what_below == '.':
                self.water[(x+1,y)] = "|"
                self.field[(x+1,y)] = '|'
                continue

            if what_below == '#' or what_below == "~":
                # left
                if self.field.get((x,y-1),'.') == '.':
                    #print("LEFT")
                    self.field[(x,y-1)] = '|'
                    self.water[(x,y-1)] = '|'
                elif self.field.get((x,y+1),'.') == '.':
                    self.field[(x,y+1)] = '|'
                    self.water[(x,y+1)] = '|'

                # can't drop down, check surroundings
                self.check_still(x,y)

        return 1


    def main(self):

        assert len(sys.argv) == 2

        inp = open(sys.argv[1]).read().strip().split('\n')
        self.load_field(inp)

        self.water = defaultdict(str)
        self.water[(0,500)] = '+'
        self.field[(0,500)] = '+'

        i=0
        while 1:
            i+=1
            if i % 100 == 0:
                print("**** ROUND ****",i) 
            
            prev_still =  len([square for square in self.field if square[1] <= self.max_y and square[1] >= self.min_y and self.field[square] == '~'])
            prev_run =  len([square for square in self.field if square[1] <= self.max_y and square[1] >= self.min_y and self.field[square] in ['|','+']])
            self.run_round()
            cur_run =  len([square for square in self.field if square[1] <= self.max_y and square[1] >= self.min_y and self.field[square] in ['|','+']])
            #print_self.field(self.field,self.max_x,self.max_y,self.min_x,self.min_y)
            curr_still =  len([square for square in self.field if square[1] <= self.max_y and square[1] >= self.min_y and self.field[square] == '~'])

            #print("water : ",cur_run,'self.max_x',self.max_x,'self.max_y',self.max_y,'self.min_x',self.min_x,'self.min_y',self.min_y,'still ',curr_still)
            if cur_run == prev_run and curr_still == prev_still:
                print("END...",len(self.water)-2)
            #    print_self.field(self.field,self.max_x,self.max_y,self.min_x,self.min_y)
                print("water : ",cur_run,'self.max_x',self.max_x,'self.max_y',self.max_y,'self.min_x',self.min_x,'self.min_y',self.min_y,'still ',curr_still)
                break

            #input()

wr = Water_runner()
wr.main()
