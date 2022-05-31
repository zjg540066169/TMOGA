#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
visualization

@auth: Jungang Zou
@date: 2018/06/02
"""
import community
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from tmoga.utils.evaluation import evaluation


class visualization(object):
    def __init__():
        pass
    
    @classmethod
    def visualize_locus_solution(self, graph, locus_solution, node_label = False):
        # visualize locus solutions on graph
        part = evaluation.parse_locus_solution(locus_solution)
        community_part = evaluation.community_nodes_to_node_community(part)
        values = [community_part.get(node) for node in graph.nodes()] 
        nx.draw(graph, cmap=plt.get_cmap('viridis'), node_color = values, node_size=100, with_labels=node_label,alpha = 0.8, pos = nx.spring_layout(graph, k=0.5 , seed = 123),width = 0.3, font_color='white') 
        plt.show()
        
    @classmethod
    def visualize_direct_solution(self, graph, direct_solution, node_label = False):
        # visualize direct solutions on graph
        part = evaluation.parse_direct_solution(direct_solution)
        community_part = evaluation.community_nodes_to_node_community(part)
        values = [community_part.get(node) for node in graph.nodes()] 
        nx.draw(graph, cmap=plt.get_cmap('viridis'), node_color = values, node_size=100, with_labels=node_label, alpha = 0.8, pos = nx.spring_layout(graph,k=0.5 , seed = 123),width = 0.3, font_color='white') 
        plt.show()
        
    @classmethod
    def visualize_clusters(self, graph, clusters):
        # visualize community on graph
        part = {}
        for i in range(len(clusters)):
            part[i] = clusters[i]
        community_part = evaluation.community_nodes_to_node_community(part)
        values = [community_part.get(node) for node in graph.nodes()] 
        
        nx.draw(graph, cmap=plt.get_cmap('viridis'), node_color = values, node_size=100, with_labels=False, alpha = 0.8, pos = nx.spring_layout(graph, k=0.5 , seed = 123),width = 0.3, font_color='white') 
        plt.show()
        
    @classmethod
    def visualize_cliques(self, graph, cliques):
        # visualize cliques on graph
        part = {}
        nx.draw(graph, node_size=100, node_color = "black", with_labels=False,  pos = nx.spring_layout(graph, k=0.5 , seed = 123),width = 0.3,font_color='white', alpha = 0.8)
        for i in range(len(cliques)):
            part[i] = cliques[i]
            color = [plt.get_cmap('viridis')(i / len(cliques))] * len(cliques[i])
            nx.draw_networkx_nodes(graph, nodelist = cliques[i], node_size=100, alpha = 0.8, pos = nx.spring_layout(graph, k=0.5 , seed = 123), node_color = color) 
        #nx.draw_networkx_edges(graph, alpha = 0.8, pos = nx.spring_layout(graph, k=0.5 , seed = 123),width = 0.3)
        #for i in graph.nodes:
        #    if i not in node_to_community:
        #        node_to_community[i] = 0
        #values = [node_to_community.get(node) + 1 for node in graph.nodes()] 
        #values = np.array(values) / max(values)
        
        plt.show()
    
    @classmethod
    def visualize_dynamic_criteria(self, list_graphs, list_solutions, locus = True,name = None, one_plot = True):
        dynamic_criteria = list(map(evaluation.Modularity, list_graphs, list_solutions, [locus] * len(list_graphs)))
        #print(dynamic_criteria)
        plt.plot(np.arange(len(list_graphs)), dynamic_criteria, label = name)
        if one_plot:
            plt.show()
        
    
        
    @classmethod
    def visualize_synthetic_locus(self, graph, locus_solution):
        community_to_node = evaluation.parse_locus_solution(locus_solution)
        node_to_community = evaluation.community_nodes_to_node_community(community_to_node)
        comm_affli = np.array([node_to_community[i] for i in range(len(node_to_community))])
        #colors = ["r","g","b","purple"]
        pos = nx.spring_layout(graph, seed = 123)
        for comm in range(np.max(comm_affli) + 1):
            node = np.where(comm_affli==comm)[0].tolist()
            color = [plt.get_cmap('tab20c')(comm / np.max(comm_affli) )] * len(node)
            
            nx.draw_networkx_nodes(graph, pos, nodelist=node,
                                   node_color=color, node_size=50)
        nx.draw_networkx_edges(graph, pos)
        plt.show()
        
    @classmethod
    def visualize_synthetic_label(self, graph, label):
        comm_affli = np.array([label[i] for i in label])
        #colors = ["r","g","blue", "purple"]
        pos = nx.spring_layout(graph, seed = 123)
        
        for comm in range(np.max(comm_affli) + 1):
            node = np.where(comm_affli==comm)[0].tolist()
            color = [plt.get_cmap('tab20c')(comm / np.max(comm_affli)) ] * len(node)
            
            nx.draw_networkx_nodes(graph, pos, nodelist=node,
                                   node_color=color, node_size=50)
        nx.draw_networkx_edges(graph, pos)
        plt.show()
        
    
    @classmethod
    def visualize_dynamic_NMI(self, solutions, truth, locus = True, name = None, one_plot = True):
        x = [i for i in range(len(solutions))]
        y = [evaluation.NMI_with_Truth(truth[i], solutions[i], locus = locus) for i in range(len(solutions))]
        sns.lineplot(data = time['Average NMI'], marker="o", sort = False, color = "r")
        plt.plot(x, y, label = name)
        if one_plot:
            plt.show()
        
        
    @classmethod
    def visualize_dynamic_adj_rs(self, solutions, truth, locus = True, name = None, one_plot = True):
        x = [i for i in range(len(solutions))]
        y = []
        for i in x:
            y.append(evaluation.adj_rs(truth[i], solutions[i], locus))
        #y = [evaluation.adj_rs(truth[i], solutions[i], locus = locus) for i in x]
        plt.plot(x, y, label = name)
        if one_plot:
            plt.show()
            
            
            
    @classmethod
    def visualize_population(self, graph, population, last_graph = None, last_solution = None ):
        # dotplot for modularity and NMI for the whole population
        x = [evaluation.Modularity(graph, i) for i in population]
        if last_solution is None:
            y = [0] * len(population)
        else:
            y = [evaluation.NMI(i, last_solution, graph, last_graph) for i in population]
        plt.scatter(x, y)
        plt.show()
        