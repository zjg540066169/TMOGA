# -*- coding: utf-8 -*-
"""
Run the algorithm TMOGA

@auth: Jungang Zou
@date: 2018/06/11
"""

from tmoga.utils.NSGA2 import NSGA2
from tmoga.utils.evaluation import evaluation
from tmoga.utils.visualization import visualization
from tmoga.algorithm.Transfer_Initialization import Transfer_Initializer
from random import choice, randint
import networkx as nx
from tqdm import tqdm
import numpy as np
import time
__author__ = "Jungang Zou"
__contact__ = "jungang.zou@gmail.com"

class TMOGA:
    def __init__(self,graph_list,pop_size = 150, max_gen = 50, CID = 0.5, transfer_prob = 0.9, mutation_prob = 0.9, crossover_prob = 0.5, max_num_cliques = 5, first_round_generation = None, sde = False):
        self.graph_list = graph_list
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.CID = CID
        self.transfer_prob = transfer_prob
        self.mutation_prob = mutation_prob 
        self.crossover_prob = crossover_prob
        self.max_num_cliques = max_num_cliques
        self.sde = sde
        #self.evaluation = evaluation
        if first_round_generation is None:
            self.first_round_generation = max_gen
        else:
            self.first_round_generation = first_round_generation
        
    def __evaluate_solution(self,graph,solution):
        return evaluation.community_score(graph,solution)#evaluation.Modularity(graph,solution)## ### 

    
    
    def __random_init(self,graph,pop_size):
        population = []
        for i in range(pop_size):
            graph_label = [-1 for i in range(max(list(graph.nodes())) + 1)]
            for node in list(graph.nodes()):
                if len(list(graph.neighbors(node))) == 0:
                    graph_label[node] = node
                else:
                    locus = choice(list(graph.neighbors(node)))
                    graph_label[node] = locus
            population.append(graph_label)
        return population
    

    def get_cliques(self):
        return self.clique_list
    
    def get_initial_populations(self):
        return self.initial_population
        

    def start(self):
        transfer_time = 0
        part_solution = []
        solution_pop = []
        #1st round
        self.clique_list = []
        self.initial_population = []
        
        #next round
        for i in tqdm(range(len(self.graph_list))):
            if i == 0:
                #init_pop = self.__random_init(self.graph_list[i],self.pop_size)
                init_pop = self.__lp_init(self.graph_list[i],self.pop_size)
                #init_pop = sorted(init_pop, key = lambda x:self.evaluation(self.graph_list[i], x), reverse = True)[:self.pop_size]
                self.initial_population.append(init_pop)
                NG2 = NSGA2(evaluation.Modularity, init_pop, self.graph_list[i],max_gen = self.first_round_generation, mutation_prob = self.mutation_prob, crossover_prob = self.crossover_prob, sde = self.sde)
                solution = NG2.start()
                solution_values =  [self.__evaluate_solution(self.graph_list[i],solution[k]) for k in range(len(solution))]
                best_solution = solution[solution_values.index(max(solution_values))]
                #print("the best solur")
                part_solution.append(best_solution)
                solution_pop.append(solution)
            
            else:
                start = time.time()
                transfer_init = Transfer_Initializer(self.graph_list[i],self.graph_list[i-1],part_solution[i-1], CID = self.CID, transfer_prob = self.transfer_prob, max_num_cliques = self.max_num_cliques)
                init_pop = transfer_init.start(self.pop_size)
                end = time.time()
                transfer_time += (end - start)
                self.clique_list.append(transfer_init.get_cliques())
                self.initial_population.append(init_pop)
                #init_pop = sorted(init_pop, key = lambda x : self.__evaluate_solution(self.graph_list[i],x), reverse = False)
                    #visualization.visualize_locus_solution(self.graph_list[i], init_pop[0])
                    
                #init_pop = self.__random_init(self.graph_list[i],self.pop_size)
    
                #print(init_pop[0])
                #print(Evaluation().solution_to_part(init_pop[0]))
                #visualization.visualize_locus_solution(self.graph_list[i],init_pop[0])
    
    
                NG2 = NSGA2(evaluation.Modularity, init_pop, self.graph_list[i], best_solution,self.graph_list[i-1], max_gen = self.max_gen, mutation_prob = self.mutation_prob, crossover_prob = self.crossover_prob, sde = self.sde)
                solutions = NG2.start()
                solution_pop.append(solutions)
                solution_values = [self.__evaluate_solution(self.graph_list[i],solutions[k]) for k in range(len(solutions))]
                best_solution = solutions[solution_values.index(max(solution_values))]
                part_solution.append(best_solution)
        print("running time of feature transfer:", transfer_time)
        return part_solution, solution_pop


    def __lp_init(self,graph,pop_size, iters = 5):
        population = []
        for i in range(pop_size):
            #population.append(self.PGLP(graph, iters = 5))
            population.append(evaluation.direct_to_locus(graph, self.PGLP(graph, iters = 5)))
        return population

    def PGLP(self, graph, iters = 5):
        x = [i for i in range(max(list(graph.nodes())) + 1)]
        #print(len(x))
        x = self.__perturbation(x)
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
        x = self.__sorting(x)
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