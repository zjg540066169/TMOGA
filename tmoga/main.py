# -*- coding: utf-8 -*-

from TMOGA import TMOGA
from DYNMOGA import DYNMOGA
import networkx as nx


if __name__=='__main__':
    network_list = []

    g = nx.Graph()
    with open(r"results\100_100_15_0.6_0.8_0.2_1\graph-1.txt",'r') as f:
        for i in f:
            g.add_edge(int(i.split()[0]),int(i.split()[1]))
    #network_list.append(g)
    network_list.append(nx.convert_node_labels_to_integers(g,ordering='decreasing degree').copy())
    g = nx.Graph()
    with open(r"results\100_100_15_0.6_0.8_0.2_1\graph-99.txt",'r') as f:
        for i in f:
            g.add_edge(int(i.split()[0]),int(i.split()[1]))
    network_list.append(nx.convert_node_labels_to_integers(g,ordering='decreasing degree').copy())
    #network_list.append(g)

    tmoga = TMOGA(network_list,IDM = 1).start()
    dynmoga = DYNMOGA(network_list).start()
    
    