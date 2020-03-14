#!python

import networkx as nx
import sys
from collections import deque

assert len(sys.argv) == 2

inp = open(sys.argv[1]).read().strip()[1:-1]

x = y = 0
gr = nx.Graph()

move = {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
pos = (0,0)
gr.add_node(pos)

q = deque()

for char in inp:

    if char == '(':
        q.append(pos)
    elif char == '|':
        pos = q[-1]
    elif char == ')':
        q.pop()
    else:
        newpos = (pos[0] + move[char][0], pos[1] + move[char][1])
        gr.add_edge(pos, newpos)
        pos = newpos

paths = nx.single_source_dijkstra_path_length(gr, (0, 0))
ans = max(paths.values())
print(f'Part1: {ans}')

over_1000 = 0

for p in paths.values():
    if p >= 1000:
        over_1000 += 1

print(f'Part2: {over_1000}')

