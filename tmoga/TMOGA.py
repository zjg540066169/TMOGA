# -*- coding: utf-8 -*-
"""
Run the algorithm TMOGA

@auth: Jungang Zou
@date: 2018/06/11
"""

from utils.NSGA2 import NSGA2
from utils.evaluation import evaluation
from utils.visualization import visualization
from tmoga.Transfer_Initialization import Transfer_Initializer
from random import choice
import networkx as nx

class TMOGA:
    def __init__(self,graph_list,pop_size = 150, max_gen = 50, CID = 0.5, transfer_prob = 0.9, mutation_prob = 0.9, crossover_prob = 0.5):
        self.graph_list = graph_list
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.CID = CID
        self.transfer_prob = transfer_prob
        self.mutation_prob = mutation_prob 
        self.crossover_prob = crossover_prob
        
    def __evaluate_solution(self,graph,solution):
        return evaluation.Modularity(graph,solution)

    
    
    def __random_init(self,graph,pop_size):
        population = []
        for i in range(pop_size):
            graph_label = [0 for i in range(len(list(graph.nodes())))]
            for node in list(graph.nodes()):
                if len(list(graph.neighbors(node))) == 0:
                    graph_label[node] = node
                else:
                    locus = choice(list(graph.neighbors(node)))
                    graph_label[node] = locus
            population.append(graph_label)
        return population

    def start(self):
        part_solution = []
        #1st round
        init_pop = self.__random_init(self.graph_list[0],self.pop_size)
        #print(init_pop[0])
        #print(Evaluation().solution_to_part(init_pop[0]))
        visualization.visualize_locus_solution(self.graph_list[0],init_pop[0])
        
        
        
        
        NG2 = NSGA2(evaluation.community_score, init_pop, self.graph_list[0],max_gen = self.max_gen, mutation_prob = self.mutation_prob, crossover_prob = self.crossover_prob)
        solution = NG2.start()
        solution_values =  [self.__evaluate_solution(self.graph_list[0],solution[i]) for i in range(len(solution))]
        best_solution = solution[solution_values.index(max(solution_values))]
        part_solution.append(best_solution)
        #next round
        for i in range(1,len(self.graph_list)):
            #print(self.graph_list[i].nodes())
            transfer_init = Transfer_Initializer(self.graph_list[i],self.graph_list[i-1],part_solution[i-1], CID = self.CID, transfer_prob = self.transfer_prob)
            init_pop = transfer_init.start(self.pop_size)
            #init_pop = self.__random_init(self.graph_list[i],self.pop_size)

            #print(init_pop[0])
            #print(Evaluation().solution_to_part(init_pop[0]))
            visualization.visualize_locus_solution(self.graph_list[i],init_pop[0])


            NG2 = NSGA2(evaluation.community_score, init_pop, self.graph_list[i], best_solution,self.graph_list[i-1], max_gen = self.max_gen, mutation_prob = self.mutation_prob, crossover_prob = self.crossover_prob)
            solutions = NG2.start()
            solution_values = [self.__evaluate_solution(self.graph_list[i],solutions[k]) for k in range(len(solutions))]
            best_solution = solutions[solution_values.index(max(solution_values))]
            part_solution.append(best_solution)
        return part_solution

if __name__ == '__main__':
    from compared_algorithm.DYNMOGA import DYNMOGA
    import random
    random.seed(1)
    G2= nx.karate_club_graph()
    G1=nx.karate_club_graph()
    G1.add_edge(0,1) 
    G1.add_edge(0,2) 
    G1.add_edge(1,3) 
    G1.add_edge(0,3)
    G1.add_edge(2,3)
    G1.add_edge(2,1)
    dynmoga =  DYNMOGA([G2, G1], 150, 50)
    pop_solutions_dynmoga = dynmoga.start()
    
    tmoga = TMOGA([G2, G1], 150, 50, CID = 0.8)
    pop_solutions_tmoga = tmoga.start()
    visualization.visualize_locus_solution(G2, pop_solutions_dynmoga[0])
    visualization.visualize_locus_solution(G2, pop_solutions_tmoga[0])
    #visualization.visualize_dynamic_criteria([G2, G1], pop_solutions_tmoga)
    #visualization.visualize_dynamic_criteria([G2, G1], pop_solutions_dynmoga)
        