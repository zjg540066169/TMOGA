# -*- coding: utf-8 -*-
"""
Some functions to deal with dynamic network communities.

@auth: Jungang Zou
@date: 2018/05/05
"""
import community
import matplotlib.pyplot as plt
import networkx as nx
import math
import utils.disjoint_set as djs
import numpy as np

class evaluation:
    def __init__(self):
        pass
    
    @classmethod
    def Modularity(self,graph, locus_solution):
        # calculate modularity
        community_to_nodes = self.parse_locus_solution(locus_solution)
        #print(part)
        node_to_community = self.community_nodes_to_node_community(community_to_nodes)
        #print(community_part)
        return community.modularity(node_to_community, graph)

    @classmethod
    def parse_locus_solution(self, locus_solution, dic = True):
        # convert solution to dict of community_to_nodes
        
        
        # create disjoint-set
        ds = djs.disjoint_set(len(locus_solution))
    
        for x in range(0, len(locus_solution)):
            y = locus_solution[x]
            ds.union(x, y)
    
        # create community list, map node_index to node_id
        community_list = {}
        #print("GENE_TO_NODE",GENE_TO_NODE)
        for i in range(len(locus_solution)):
            node_id = i
            ri = ds.find_set(i)
    
            if ri in community_list:
                community_list[ri].append(node_id)
            else:
                community_list[ri] = [node_id]
        #print(list(community_list.values()))
        if dic:
            community_to_nodes = {}
            for i in range(len(list(community_list.values()))):
                key = list(community_list.values())[i][0]
                community_to_nodes[key] = list(community_list.values())[i]
        else:
            community_to_nodes = list(community_list.values())
        return community_to_nodes
        
    @classmethod
    def community_nodes_to_node_community(self, community_to_nodes):
        # convert partition to community(key:node_index, value:community_index)
        node_to_community = {}
        for community_num in community_to_nodes:
            community = community_to_nodes[community_num]
            for node in community:
                node_to_community[node] = community_num
        #print(community_result)
        return node_to_community

    @classmethod
    def NMI(self,solution1,solution2,graph1,graph2):
        # calculate NMI based on 2 solutions
        c_A = self.parse_locus_solution(solution1)
        c_B = self.parse_locus_solution(solution2)
        #print("cA:",c_A)
        #print("cB:",c_B)
        N_mA = len(c_A)
        N_mB = len(c_B)
        S = min(graph1.number_of_nodes(),graph2.number_of_nodes())
        #print(S)
        I_num = 0
        for i in c_A:
            for j in c_B:
                n_i = len(c_A[i])
                n_j = len(c_B[j])
                n_ij = len(set(c_A[i]) & set(c_B[j]))
                if n_ij == 0:
                    continue
                log_term = math.log((n_ij * S) / (n_i * n_j))
    
                I_num += n_ij * log_term
        I_num *= -2
    
        I_den = 0
        for i in c_A:
            n_i = len(c_A[i])
            I_den += n_i * math.log(n_i / S)
    
        for j in c_B:
            n_j = len(c_B[j])
            I_den += n_j * math.log(n_j / S)
        try:
            I = I_num / I_den
        except ZeroDivisionError:
            I = 1
        return I
    
    @classmethod
    def community_score(self, graph, locus_solution, order = 2, direct = False):
        # calculate community score
        def score(community):
            #  calculate score for each community
            adj = adj_matrix[community,:][:, community]
            first_term = np.power(adj.mean(1), order).mean()
            second_term = adj.sum()
            return first_term * second_term
                        
            
        c = self.parse_locus_solution(locus_solution)
        adj_matrix = nx.adj_matrix(graph).todense()
        total_score = map(score, list(c.values()))
        return sum(total_score)
    
    @classmethod
    def community_CID(self, graph, c):
        adj = nx.adj_matrix(graph).todense()[c,:][:, c]
        return (adj.sum() - adj.trace()[0, 0]) / (len(c) * (len(c) - 1))
        
        
    
        
        
        

        
