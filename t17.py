#!python3
import sys
from collections import defaultdict
import numpy as np
from copy import deepcopy

def print_field(field):
    print(field.items())

    arr=np.zeros([20,507],dtype=str)

    for a in range(20):
        for b in range(507):
            arr[a][b] =  field.get((a,b),'.')

    for row in arr: # Part 2
        print(*row, sep='')

    return 0


def check_still(field,x,y):
    pass

def load_field(inp):

    maxx = maxy = 0
    field = defaultdict(str)

    for row in inp:
        first, second = row.split(', ')
        f1, f2 = first.split('=')
        s1, s2 = second.split('=')
        f2 = int(f2)
        sfr,sto = list(map(int,s2.split('..')))

        if f1 == 'y':
            if f2 > maxx : maxx = f2
            if sto > maxy: maxy = sto
            for i in range(sfr,sto+1):
                field[(f2,i)] = '#'
        else:
            if f2 > maxy: maxy = f2
            if sto > maxx: maxx = sto
            for i in range(int(sfr),int(sto)+1):
                field[(i,f2)] = '#'

    return field, maxx, maxy

def run_round(field, water, maxx, maxy):

    field_c = defaultdict(str)
    field_c = deepcopy(field)
    water[(0,500)] = '+'
    field[(0,500)] = '+'

    water_c = deepcopy(water)

    for x,y in water:
        if x == maxx or y == maxy:
            continue
        what = str(field.get((x,y),'.'))
        if any(ele in what for ele in ['+','|']) :
            # there is empty space
            water_c[(x,y)] = '.'
            field_c[(x,y)] = '.'
            what_below = str(field.get((x+1,y),'.'))

            # drop down
            if what_below == '.':
                water_c[(x+1,y)] = "|"
                field_c[(x+1,y)] = '|'
                continue

            # can't drop down, check surroundings
            check_still(field_c,x,y)

    print(len(water_c))

    return field_c, water_c


def main():

    assert len(sys.argv) == 2

    inp = open(sys.argv[1]).read().strip().split('\n')
    field, maxx, maxy = load_field(inp)

    water = defaultdict(str)


    # move
    print(maxx,maxy)

    for i in range(17):
        field, water = run_round(field, water, maxx, maxy)
        print_field(field)
        print_field(water)

        input()

main()
