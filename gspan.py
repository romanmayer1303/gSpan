import networkx as nx
import numpy as np
import matplotlib.pyplot as pl
import sys

graphs = []


def read_file(file, delimiter=' ', newline='\n'):
    with open(str(file), 'r') as f:
        g = nx.Graph(id=f.readline().strip(newline))  # first graph
        for line in f.readlines():
            line = line.strip(newline)
            l = line.split(delimiter)
            if l[0] == 'v':  # add node
                g.add_node(l[1], label=l[2], id=-1)
            elif l[0] == 'e':  # add edge
                g.add_edge(l[1], l[2], label=l[3], direction=-1)
            elif l[0] == 't':  # next graph
                graphs.append(g)
                g = nx.Graph(id=line)
        graphs.append(g)

#   dfs_trees(nx.Graph(G), 0, [], [], 0)
def dfs(g, n0, trees, num=0):
    g.node[n0]['id'] = num
    for n in nx.all_neighbors(g, n0):
        if g.node[n]['id'] == -1:
            dfs(nx.Graph(g), n, trees, num+1)
    if num == nx.number_of_nodes(g)-1:
        trees.append(nx.Graph(g))

def label_edges(g, n0):
    index = g.node[n0]['id']
    for n in nx.all_neighbors(g, n0):
        if g.node[n]['id'] == index+1:
            g.edge[n0][n]['direction'] = 1
            label_edges(g, n)

def dfs_trees(g):
    ret = []
    for n in g.nodes_iter():
        trees = []
        dfs(nx.Graph(g), n, trees)
        for t in trees:
            label_edges(t, n)
            ret.append(nx.Graph(t))
    return ret


def print_number_of_nodes_and_edges():
    for i, graph in enumerate(graphs):
        print("graph " + str(i) + "'s #nodes: " + str(graph.number_of_nodes()))
        print("graph " + str(i) + "'s #edges: " + str(graph.number_of_edges()))


def draw_all_graphs():
    g0 = graphs[0]
    g1 = graphs[1]
    pos0 = nx.spring_layout(g0)
    pos1 = nx.spring_layout(g1)
    nx.draw_networkx_nodes(g0, pos0, hold=True, node_color='r')
    nx.draw_networkx_labels(g0,pos=pos0)
    nx.draw_networkx_nodes(g1, pos1, hold=True, node_color='b')
    nx.draw_networkx_edges(g0, pos0, hold=True, edge_color='r')
    nx.draw_networkx_labels(g1,pos=pos1)
    nx.draw_networkx_edges(g1, pos1, edge_color='b')
    pl.axis('off')
    pl.show()


read_file(str(sys.argv[1]))
print_number_of_nodes_and_edges()

trees = dfs_trees(nx.Graph(graphs[1]))
for t in trees:
    print t.nodes(data=True), t.edges(data=True)
draw_all_graphs()
