#! python3
import sys
import numpy as np
from itertools import permutations
import csv
from collections import deque,defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from Unit import Unit
from copy import copy

class Battle(object):

    def __init__(self, inp):
        self.grid = []
#        for line in inp:
#            self.grid.append(list(map(str,line)))

        self.units = []
        self.units_armies = defaultdict(list)
        self.still_to_play = []
        self.units_played = 0

        for x, row in enumerate(inp):
            self.grid.append(list(map(str,row)))
            for y, what in enumerate(row):

                if what == 'E' or what =='G':
                    my_unit = Unit((x,y),what)
                    self.units.append(my_unit)
                    self.units_armies[what].append(my_unit)

        self.rounds = 0

    def graph_battle(self,unit,unit2):
        gr_def = nx.Graph()
        
#        print("Graphing unit at ",unit.pos," type ",unit.type," enemy type ",unit.enemy_type)

        self.grid[unit.pos[0]][unit.pos[1]] = '.'
        self.grid[unit2.pos[0]][unit2.pos[1]] = '.'

        for x in range(0,len(self.grid)-1):
            for y in range(0,len(self.grid[x])-1):
                # add node if the moving unit or enemy
                if self.grid[x][y] != ".":
                    continue

                #ok_tiles = ['.',unit.enemy_type]
                ok_tiles = ['.']
 
                if (x > 0) and (self.grid[x-1][y] in ok_tiles) : gr_def.add_edge((x,y), (x-1,y))
                if (x < len(self.grid)-1) and (self.grid[x+1][y] in ok_tiles) : gr_def.add_edge((x,y), (x+1,y))

                if (y > 0) and (self.grid[x][y-1] in ok_tiles) : gr_def.add_edge((x,y), (x,y-1))
                if (y < len(self.grid)-1) and (self.grid[x][y+1] in ok_tiles): gr_def.add_edge((x,y), (x,y+1))
           
    
        self.grid[unit.pos[0]][unit.pos[1]] = unit.type
        self.grid[unit2.pos[0]][unit2.pos[1]] = unit2.type

#        print("Returning graph")
        #print(gr_def.nodes)
        return gr_def



def attack(unit,target):

    target.health -= unit.attack_power
#    print("Unit at ",unit.pos," Attacked ",target.pos, " health remaining ",target.health," target type ",target.type," at target grid is : ",b.grid[target.pos[0]][target.pos[1]])

    if target.health <= 0:
        b.grid[target.pos[0]][target.pos[1]] = '.'
        b.units.remove(target)
        b.units_armies[target.type].remove(target)
        #:input()

    return 1

def get_unit_at_coord(pos):

    for my_unit in b.units:
        if my_unit.pos == pos:
            return my_unit

    return None

def find_target_to_attack(enemy_candidates):
#    print(enemy_candidates)
    return(sorted(enemy_candidates[1], key=lambda a: (a.health, a.pos))[0])


def find_enemy(unit):

    distances = defaultdict(list)

    for unit2 in b.units_armies[unit.enemy_type]:
#        print("Considering ",unit2.type," at ",unit2.pos)
        g = b.graph_battle(unit,unit2)

        try:
            #print("Round ",b.rounds," Finding shortest path length")
 #           cur_p_len = nx.astar_path_length(g,unit.pos,unit2.pos)+1
            #cur_p_len = nx.shortest_path_length(g,unit.pos,unit2.pos)+1
            cur_p_len = nx.dijkstra_path_length(g,unit.pos,unit2.pos)+1
            #print("Found length ",cur_p_len)
            distances[cur_p_len].append(unit2)

        except Exception as e:
            #print('Error: %s' % e)
            continue

    if not distances:
        return None,None

    distances = sorted(distances.items())
    #print("Minimum distance :", distances[0])

    min_len = distances[0][0]

    #print("Min len ",min_len)

    paths = []
    obj = None

    if min_len == 2:
#        print(distances)
 #       print(distances[0])
      #  print("Processing attacking distance")
        obj = find_target_to_attack(distances[0])
 #       print("Unit at ",unit.pos," found target at ",obj.pos)
        return( obj, ( unit.pos, obj.pos) )

    else :
#        print("Processing all shortest paths...")

        for p in distances[0][1]:
            g = b.graph_battle(unit,p)       

            for d in nx.all_shortest_paths(g,unit.pos,p.pos):
                paths.append(d)

        #print("Finding done")
    
    if not paths:
        return None, None

    paths.sort(key=lambda x: x[1])

    obj = get_unit_at_coord(paths[0][min_len-1])

    return(obj,paths[0])

def check_if_done():
    if not b.units_armies['G'] or not b.units_armies['E']:
        print('combat finished')

        total_health = sum([u.health for u in b.units if u.health > 0])

        if b.units_played != len(b.still_to_play):
            b.rounds -= 1

        print("Rounds ",b.rounds," Total health ",total_health," Result :", (b.rounds) * total_health)
        print_grid()
        sys.exit()

def print_grid():
    for row in b.grid: # Part 2
        print(*row, sep='')
#    for unit in b.units:
 #      print(unit)
 #       print(unit.__dict__)

# ---------- MAIN --------

assert len(sys.argv) == 2

inp = open(sys.argv[1]).read().split('\n')

b = Battle(inp)

#print(b.__dict__)

# combat


while 1:
    b.rounds += 1
    print("Round : ",b.rounds)


#    if b.rounds >= 24 and b.rounds <= 30 :
#        input()


    # process units
    b.units.sort( key=lambda a: a.pos)
    print_grid()


    if b.rounds == 10:
        input()
    b.still_to_play = copy(b.units)
    b.units_played = 0

    # for finding if round is finished

    for unit in b.still_to_play:
        b.units_played += 1
        
        #print("**** UNIT ****")
        #print(unit)
        #print(b.still_to_play)

        if unit not in b.units:
#            print("Already killed unit at ",unit.pos)
            # the unit has been killed in between
            continue

#        print("--- PROCESSING ----")
 #       print(unit.__dict__)
        target, path = find_enemy(unit)

#        print("target : ",target)

        if path is None:
            continue

        if len(path) == 2:
            attack(unit, target)
            check_if_done()

        else:
            b.grid[unit.pos[0]][unit.pos[1]] = '.'
            b.grid[path[1][0]][path[1][1]] = unit.type

            unit.pos = path[1]
            #attack after move
            target, path = find_enemy(unit)
            if len(path) == 2:
                attack(unit,target)
                #print("1")
                check_if_done()

    check_if_done()
    #input()
