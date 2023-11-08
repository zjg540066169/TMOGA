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
import tmoga.utils.disjoint_set as djs
import numpy as np
from sklearn.metrics import adjusted_rand_score
from random import choice, uniform
class evaluation:
    def __init__(self):
        pass
    
    @classmethod
    def Modularity(self,graph, solution, locus = True, truth = False):
        # calculate modularity
        if truth:
            community_to_nodes = solution
        else:
            
            if locus:
                community_to_nodes = self.parse_locus_solution(solution)
            else:
                community_to_nodes = self.parse_direct_solution(solution)
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
            if y == -1:
                continue
            ds.union(x, y)
    
        # create community list, map node_index to node_id
        community_list = {}
        #print("GENE_TO_NODE",GENE_TO_NODE)
        for i in range(len(locus_solution)):
            if locus_solution[i] == -1:
                continue
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
                key = i
                community_to_nodes[key] = list(community_list.values())[i]
        else:
            community_to_nodes = list(community_list.values())
        return community_to_nodes
    
    @classmethod
    def parse_direct_solution(self, direct_solution, dic = True):
        community_list = {}
        direct_solution = np.array(direct_solution)
        for i in np.unique(direct_solution):
            if i == -1:
                continue
            community_list[i] = np.where(direct_solution == i)[0].tolist()
        if dic:
            return community_list
        return list(community_list.values)
    
    @classmethod
    def direct_to_locus(self, graph, direct_solution):
        direct_solution = np.array(direct_solution)
        locus_solution = []
        for i in range(len(direct_solution)):
            if direct_solution[i] == -1:
                locus_solution.append(-1)
            else:
                candidate = set(graph.neighbors(i)).intersection(np.where(direct_solution == direct_solution[i])[0])
                if len(candidate) == 0:
                    locus_solution.append(i)
                else:
                    #print(i, sorted(candidate))
                    locus_solution.append(min(list(candidate)))
        return locus_solution
    
    
    @classmethod
    def locus_to_direct(self, locus_solution):
        community_to_nodes = self.parse_locus_solution(locus_solution)
        return self.community_node_to_direct(community_to_nodes)
    
    @classmethod
    def community_node_to_direct(self, community_node):
        node_community = self.community_nodes_to_node_community(community_node)
        return [node_community[i] if i in node_community else -1 for i in range(max(node_community) + 1)]
        
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
    def NMI(self,solution1,solution2,graph1 = None,graph2 = None):
        # calculate NMI based on 2 solutions
        c_A = self.parse_locus_solution(solution1)
        c_B = self.parse_locus_solution(solution2)
        #print("cA:",c_A)
        #print("cB:",c_B)
        N_mA = len(c_A)
        N_mB = len(c_B)
        
        S = max(graph1.number_of_nodes(),graph2.number_of_nodes())
        
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
    def NMI_direct(self,solution1,solution2,node_n):
        c_A = self.parse_direct_solution(solution1)
        c_B = self.parse_direct_solution(solution2)
        #print("cA:",c_A)
        #print("cB:",c_B)
        N_mA = len(c_A)
        N_mB = len(c_B)
        S = node_n
        
        
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
    def NMI_with_Truth(self, truth, solution, locus = True):
        # calculate NMI based on 2 solutions
        if locus:
            c_A = self.parse_locus_solution(solution)
        else:
            c_A = self.parse_direct_solution(solution)
        c_B = truth
        #print("cA:",c_A)
        #print("cB:",c_B)
        N_mA = len(c_A)
        N_mB = len(c_B)
        S = max(map(max, list(truth.values()))) + 1
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
            adj = nx.adjacency_matrix(graph, nodelist = community).todense()
            first_term = np.power(adj.mean(1), order).mean()
            second_term = adj.sum()
            return first_term * second_term
                        
        if not direct:
            c = self.parse_locus_solution(locus_solution)
        else:
            c = self.parse_direct_solution(locus_solution)
        total_score = map(score, list(c.values()))
        return sum(total_score)
    
    @classmethod
    def community_CID(self, graph, c):
        adj = nx.adjacency_matrix(graph, nodelist = c).todense()
        return (adj.sum() - adj.trace()) / (len(c) * (len(c) - 1))
        
        
    
    @classmethod
    def adj_rs(self, truth, solution, locus = True):
        if type(truth) is not list:
                truth = self.community_node_to_direct(truth)
        #print(truth)
        if locus:
            community_node = self.parse_locus_solution(solution)
            d = self.community_node_to_direct(community_node)
            #print(len(d))
            return adjusted_rand_score(truth, d)
        return adjusted_rand_score(truth, solution)
        
        

        
