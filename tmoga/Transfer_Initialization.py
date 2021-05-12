# -*- coding: utf-8 -*-
"""
Produce the initial solution of algorithm TMOGA

@auth: Jungang Zou
@date: 2018/05/12
"""
from tmoga.Feature_Extraction import Clique_Discover
from utils.evaluation import evaluation
from utils.visualization import visualization

import numpy as np
import networkx as nx
from random import choice, uniform
import community


class Transfer_Initializer:
    def __init__(self,G,G_previous,G_previous_label, CID = 1, transfer_prob = 0.9):
        self.graph = G
        self.previous_graph = G_previous
        self.previous_graph_label = G_previous_label
        self.CID = CID
        self.transfer_prob = transfer_prob
       

    def __feature_extract(self):
        cluster = evaluation.parse_locus_solution(self.previous_graph_label, dic = False)
        return Clique_Discover.clique_discover(self.previous_graph, cluster, self.CID)
    

    def __random_init(self):
        graph_label = [0 for i in range(len(list(self.graph.nodes())))]
        for node in list(self.graph.nodes()):
            if len(list(self.graph.neighbors(node))) == 0:
                graph_label[node] = node
            else:
                node_neighbor = [neighbor for neighbor in self.graph.neighbors(node)]
                graph_label[node] = choice(node_neighbor)
        return graph_label
    
    def __transfer_label(self, transfer_node_list):
        transfer_dic = {}
        for clique_result in transfer_node_list:
            if uniform(0, 1) > self.transfer_prob:
                continue
            for node in clique_result:
                if len(list(self.graph.neighbors(node))) == 0:
                    transfer_dic[node] = node
                else:
                    node_neighbor = [neighbor for neighbor in self.graph.neighbors(node)]
                    transfer_dic[node] = choice(list(set(node_neighbor).intersection(set(clique_result))))
        return transfer_dic
    
    def start(self, population_size):
        population = []
        transfer_node_list = self.__feature_extract()
        transfer_dic = self.__transfer_label(transfer_node_list)
        for i in range(population_size):
            random_init = self.__random_init()
            for node in transfer_dic:
                random_init[node] = transfer_dic[node]
            population.append(random_init)
        return population

    
if __name__ == '__main__':
    from compared_algorithm.DYNMOGA import DYNMOGA
    G2= nx.karate_club_graph()
    G1=nx.karate_club_graph()
    G1.add_edge(0,1) 
    G1.add_edge(0,2) 
    G1.add_edge(1,3) 
    G1.add_edge(0,3)
    G1.add_edge(2,3)
    G1.add_edge(2,1)
    dynmoga =  DYNMOGA([G2], 50, 10)
    pop_solutions = dynmoga.start()[0]

    
# =============================================================================
#     GI = Transfer_Initialization(G2,G1,[[1,2,3,0]])
#     solution = GI.start(5)
#     print(evaluation.Modularity(G2,solution[0]))
#     print(evaluation.NMI(solution[0],solution[1],G2,G2))
#     visualization.visualize_locus_solution(G2,solution[0])
# 
# =============================================================================
