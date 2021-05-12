# -*- coding: utf-8 -*-
"""
Run the algorithm DYNMOGA.

@auth: Jungang Zou
@date: 2018/06/10
"""
from utils.NSGA2 import NSGA2
from utils.evaluation import evaluation
from utils.visualization import visualization
from random import choice
import networkx as nx

class DYNMOGA:
    # graph_list: a list of graph in networkx
    # pop_size: the number of individuals in each generation
    # max_gen: the number of generations in iterations
    def __init__(self,graph_list,pop_size = 50, max_gen = 10, mutation_prob = 0.9, crossover_prob = 0.5):
        self.graph_list = graph_list
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.mutation_prob = mutation_prob
        self.crossover_prob = crossover_prob
        
    def __evaluate_solution(self,graph,solution):
        # return the modularity of solution at current snapshot
        #return evaluation.community_score(graph,solution)
        return evaluation.Modularity(graph, solution)

    
    
    def __random_init(self,graph,pop_size):
        # initial populations based on locus coding
        population = []
        for i in range(pop_size):
            graph_label = [0 for i in range(len(list(graph.nodes())))]
            for node in list(graph.nodes()):
                # if no neighbors, assign to itself
                if len(list(graph.neighbors(node))) == 0:
                    graph_label[node] = node
                    
                # if has neighbors, randomly assign to one of neighbors
                else:
                    locus = choice(list(graph.neighbors(node)))
                    graph_label[node] = locus
            population.append(graph_label)
        return population

    def start(self):
        # gather solution
        part_solution = []
        
        #1st round
        init_pop = self.__random_init(self.graph_list[0],self.pop_size)
        
        # test on first individual
        print(init_pop[0])
        print(evaluation.parse_locus_solution(init_pop[0]))
        visualization.visualize_locus_solution(self.graph_list[0],init_pop[0])
        
        # run for first network
        NG2 = NSGA2(evaluation.community_score, init_pop, self.graph_list[0], max_gen = self.max_gen, mutation_prob=self.mutation_prob, crossover_prob=self.crossover_prob)
        solution = NG2.start()
        # calculate community score for all final individuals
        solution_values =  [self.__evaluate_solution(self.graph_list[0],solution[i]) for i in range(len(solution))]
        print(solution_values)
        # get best result for community score
        best_solution = solution[solution_values.index(max(solution_values))]
        # gather best result
        part_solution.append(best_solution)
        
        
        
        #next round
        for i in range(1,len(self.graph_list)):
            init_pop = self.__random_init(self.graph_list[i],self.pop_size)
            NG2 = NSGA2(evaluation.community_score,init_pop, self.graph_list[i],best_solution,self.graph_list[i-1], max_gen = self.max_gen, mutation_prob=self.mutation_prob, crossover_prob=self.crossover_prob)
            solutions = NG2.start()
            solution_values = [self.__evaluate_solution(self.graph_list[i],solutions[k]) for k in range(len(solutions))]
            print(solution_values)
            best_solution = solutions[solution_values.index(max(solution_values))]
            part_solution.append(best_solution)
        return part_solution
    
if __name__ =="__main__":
    G2 = nx.karate_club_graph()
    G2 =  nx.convert_node_labels_to_integers(G2)
    seed = []
    for i in range(50):
        graph_label = []
        for node in list(G2.nodes()):
            node_neighbor = [neighbor for neighbor in G2.neighbors(node)]
            graph_label.append(choice(node_neighbor))
        seed.append(graph_label)
    dynmoga =  DYNMOGA([G2], 50, 10)
    pop_solutions = dynmoga.start()
    #print(evaluation.Visualization(G2, result[0]))
    import time

    #time_start=time.time()
    #evaluation.Modularity(G2, seed[0])
    #evaluation.community_score(G2, seed[0])
    #time_end=time.time()
    #print('totally cost',time_end-time_start)
    #print()
    #print(evaluation.community_score(G2, seed[0]))
        
        