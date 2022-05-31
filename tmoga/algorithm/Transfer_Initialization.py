# -*- coding: utf-8 -*-
"""
Produce the initial solution of algorithm TMOGA (feature migration)

@auth: Jungang Zou
@date: 2018/05/12
"""
from tmoga.algorithm.Feature_Extraction import Clique_Discover
from tmoga.utils.evaluation import evaluation
from tmoga.utils.visualization import visualization
from tmoga.utils.disjoint_set import disjoint_set

import numpy as np
import networkx as nx
from random import choice, uniform, randint
import community


class Transfer_Initializer:
    def __init__(self,G,G_previous,G_previous_label, CID = 1, transfer_prob = 0.9, max_num_cliques = 5):
        self.graph = G
        self.previous_graph = G_previous
        self.previous_graph_label = G_previous_label
        self.CID = CID
        self.transfer_prob = transfer_prob
        self.max_num_cliques = max_num_cliques
        self.cliques = None
        
        
    def get_cliques(self):
        return self.cliques
       

    def __feature_extract(self, locus = True):
        if locus == False:
            return Clique_Discover.clique_discover(self.previous_graph, self.previous_graph_label, self.CID, self.max_num_cliques)
        cluster = evaluation.parse_locus_solution(self.previous_graph_label, dic = False)
        
        return  Clique_Discover.clique_discover(self.previous_graph, cluster, self.CID, self.max_num_cliques)
    

    def __random_init(self):
        graph_label = [-1 for i in range(max(list(self.graph.nodes())) + 1)]
        for node in list(self.graph.nodes()):
            if len(list(self.graph.neighbors(node))) == 0:
                graph_label[node] = node
            else:
                node_neighbor = [neighbor for neighbor in self.graph.neighbors(node)]
                graph_label[node] = choice(node_neighbor)
        return graph_label
    
    
    def __lp_init(self, iters = 5):
        return evaluation.direct_to_locus(self.graph, self.PGLP(self.graph, iters = 5))
    
    
    def __transfer_label(self, transfer_node_list):
        transfer_dic = {}
        for clique_result in transfer_node_list:
            #if uniform(0, 1) > self.transfer_prob:
            #    continue
            
            for node in clique_result:
                if node not in self.graph:
                    continue
                node_neighbor = [neighbor for neighbor in self.graph.neighbors(node)]
                if len(node_neighbor) == 0:
                    transfer_dic[node] = [node]
                else:
                    transfer_candidate = list(set(node_neighbor).intersection(set(clique_result)))
                    if len(transfer_candidate) == 0:
                        transfer_dic[node] = [node]
                    else:
                        transfer_dic[node] = transfer_candidate
        return transfer_dic
    
    def start(self, population_size, random = False, iters = 5, locus = True):
        population = []
        if random:
            for i in range(population_size):
                random_init = self.__random_init()#self.__lp_init()
                #lp_init = self.__lp_init(iters)
                #random_init = lp_init
                population.append(random_init)
            return population
        
        transfer_node_list = self.__feature_extract(locus)
        self.cliques = transfer_node_list
        #visualization.visualize_cliques(self.graph, transfer_node_list)
        #print(transfer_node_list)
        #visualization.visualize_cliques(self.previous_graph, transfer_node_list)
        transfer_dic = self.__transfer_label(transfer_node_list)
        for i in range(population_size):
            random_init = self.__random_init()
            #lp_init = self.__lp_init()
            #random_init = lp_init
            #random_init = max([random_init, lp_init], key = lambda x : self.evaluation(self.graph, x))
            for node in transfer_dic:
                if uniform(0, 1) <= self.transfer_prob:
                    random_init[node] = choice(transfer_dic[node])
            #population.append(random_init)
            #visualization.visualize_locus_solution(self.graph, random_init)
            population.append(self.Locus_PGLP(self.graph, random_init, iters))
            #visualization.visualize_locus_solution(self.graph, population[-1])
        return population
    
    def Locus_PGLP(self, graph, locus_solution, iters = 5):
        for i in range(iters):
            ds = disjoint_set(len(locus_solution))
            for x in range(0, len(locus_solution)):
                y = locus_solution[x]
                if y == -1:
                    continue
                ds.union(x, y)
            for j in range(len(locus_solution)):
                if j not in graph:
                    locus_solution[j] = -1
                    continue
                neighbor = list(graph.neighbors(j))
                nb_labels = []
                for neigh in neighbor:
                    nb_labels.append(ds.find_set(neigh))
                if len(neighbor) > 0:
                   max_nb_labels = np.argmax(np.bincount(nb_labels))
                   locus_solution[j] = neighbor[nb_labels.index(max_nb_labels)]
        return locus_solution   
                
                   
          
                   
        
    
    def PGLP(self, graph, iters = 5):
        x = [i for i in range(max(list(graph.nodes())) + 1)]
        #x = self.__perturbation(x)
        for i in range(iters):
            temp_x = np.array(x.copy())
            for j in range(len(x)):
                if j not in graph:
                    x[j] = -1
                    continue
                neighbor = list(graph.neighbors(j))
                nb_labels = temp_x[neighbor]
            
                
                if len(neighbor) > 0:
                   max_nb_labels = np.argmax(np.bincount(nb_labels))
                   x[j] = max_nb_labels
                   #print(max_nb_labels)
        #x = self.__sorting(x)
        return x

    def __perturbation(self, x):
        n = len(x)
        i = n - 1
        while  i >= 0:
            index = randint(0, n - 1) 
            x[i], x[index] = x[index],x[i]
            i = i - 1
        return x

    def __sorting(self, X):
        flag = 1
        tempX = X.copy()
        for i in range(len(X)):
            if tempX[i] != -1:
                 for j in range(i + 1, len(X)):
                     if  tempX[i] ==  tempX[j]:
                         X[j] = flag;
                         tempX[j] = -1;
                    
                 tempX[i] = -1;
                 X[i] = flag;
                 flag  = flag + 1;
        return X

