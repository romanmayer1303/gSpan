import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import sys

graphs = []


def read_file(file, delimiter=' ', newline='\n'):
    with open(str(file), 'r') as f:
        g = nx.Graph(id=f.readline().strip(newline))  # first graph
        for line in f.readlines():
            line = line.strip(newline)
            l = line.split(delimiter)
            if l[0] == 'v':  # add node
                g.add_node(l[1], label=l[2])
            elif l[0] == 'e':  # add edge
                g.add_edge(l[1], l[2], label=l[3])
            elif l[0] == 't':  # next graph
                graphs.append(g)
                g = nx.Graph(id=line)
        graphs.append(g)


def print_number_of_nodes_and_edges():
    for i, graph in enumerate(graphs):
        print("graph " + str(i) + "'s #nodes: " + str(graph.number_of_nodes()))
        print("graph " + str(i) + "'s #edges: " + str(graph.number_of_edges()))


def draw_all_graphs():
    g0 = graphs[0]
    g1 = graphs[1]
    pos0 = nx.spring_layout(g0)
    pos1 = nx.spring_layout(g1)
    nx.draw_networkx_nodes(graphs[0], pos0, hold=True, node_color='r')
    nx.draw_networkx_nodes(graphs[1], pos1, hold=True, node_color='b')
    nx.draw_networkx_edges(graphs[0], pos0, hold=True, edge_color='r')
    nx.draw_networkx_edges(graphs[1], pos1, edge_color='b')
    plt.show()


read_file(str(sys.argv[1]))
print_number_of_nodes_and_edges()
draw_all_graphs()


