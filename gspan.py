import networkx as nx
import numpy as np
import matplotlib.pyplot as pl
import sys

graphs = []

def read_file(file, delimiter=' ', newline='\n'):
    with open(str(file), 'r') as f:
        g = nx.Graph(id=f.readline().strip(newline)) #first graph
        for line in f.readlines():
            line = line.strip(newline)
            l = line.split(delimiter)
            if l[0] == 'v': #add node
                g.add_node(l[1], label=l[2])
            elif l[0] == 'e': #add edge
                g.add_edge(l[1], l[2], label=l[3])
            elif l[0] == 't': #next graph
                graphs.append(g)
                g = nx.Graph(id=line)
        graphs.append(g)

read_file(str(sys.argv[1]))
