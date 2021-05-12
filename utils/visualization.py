#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:31:28 2021

@author: jungang
"""
import community
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from utils.evaluation import evaluation


class visualization(object):
    def __init__():
        pass
    
    @classmethod
    def visualize_population():
        pass
    
    @classmethod
    def visualize_locus_solution(self, graph, locus_solution):
        # visualize community on graph
        part = evaluation.parse_locus_solution(locus_solution)
        community_part = evaluation.community_nodes_to_node_community(part)
        values = [community_part.get(node) for node in graph.nodes()] 
        nx.draw(graph, cmap=plt.get_cmap('jet'), node_color = values, node_size=100, with_labels=True, pos = nx.spring_layout(graph, seed = 123)) 
        plt.show()
        
    @classmethod
    def visualize_clusters(self, graph, clusters):
        # visualize community on graph
        part = {}
        for i in range(len(clusters)):
            part[i] = clusters[i]
        community_part = evaluation.community_nodes_to_node_community(part)
        values = [community_part.get(node) for node in graph.nodes()] 
        nx.draw(graph, cmap=plt.get_cmap('jet'), node_color = values, node_size=100, with_labels=True, pos = nx.spring_layout(graph, seed = 123)) 
        plt.show()
        
    @classmethod
    def visualize_cliques(self, graph, cliques):
        # visualize community on graph
        part = {}
        for i in range(len(cliques)):
            part[i] = cliques[i]
        node_to_community = evaluation.community_nodes_to_node_community(part)
        for i in graph.nodes:
            if i not in node_to_community:
                node_to_community[i] = -5
        values = [node_to_community.get(node) for node in graph.nodes()] 
        nx.draw(graph, cmap=plt.get_cmap('jet'), node_color = values, node_size=100, with_labels=True, pos = nx.spring_layout(graph, seed = 123)) 
        plt.show()
    
    @classmethod
    def visualize_dynamic_criteria(self, list_graphs, list_locus_solutions):
        dynamic_criteria = list(map(evaluation.Modularity, list_graphs, list_locus_solutions))
        print(dynamic_criteria)
        plt.plot(np.arange(len(list_graphs)), dynamic_criteria)
        plt.show()
        
        
        
        
        