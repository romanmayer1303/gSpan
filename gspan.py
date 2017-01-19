import networkx as nx
import numpy as np
import matplotlib.pyplot as pl
import sys

graphs = []

def read_file(file):
    with open(file, 'r') as f:
        g = nx.Graph(id=f.readline().strip('\n')) #first graph
        for line in f.readlines():
            line = line.strip('\n')
            l = line.split(' ')
            if l[0] == 'v': #add node
                g.add_node(int(l[1]), label=l[2])
            elif l[0] == 'e': #add edge
                g.add_edge(int(l[1]), int(l[2]), label=l[3])
            elif l[0] == 't': #next graph
                graphs.append(g)
                g = nx.Graph(id=line)
        graphs.append(g)

read_file(str(sys.argv[1]))
