# -*- coding: utf-8 -*-
"""
Run the algorithm NSGA2

@auth: Jungang Zou
@date: 2018/06/02
"""

from tmoga.utils.evaluation import evaluation
import networkx as nx
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from random import choice, choices
from tmoga.utils.SDE import SDE
import math
import time

class NSGA2:
    def __init__(self, objective_func, init_population,graph, last_solution=None, last_graph = None, max_gen = 999, mutation_prob = 0.9, crossover_prob = 0.5, sde = False):
        self.objective_func = objective_func
        self.init_pop = init_population
        self.graph = graph
        self.last_solution = last_solution
        self.last_graph = last_graph
        self.pop_size = len(init_population)
        self.max_gen = max_gen
        self.mutation_prob = mutation_prob
        self.crossover_prob = crossover_prob
        self.sde = sde
        
    
    def function1(self,solution):#modularity
        value = self.objective_func(self.graph, solution)
        return value


    def function2(self,solution):#NMI
        #return random.gauss(0, 1)
        if self.last_solution is None:
            return 0
        value = evaluation.NMI(solution,self.last_solution,self.graph,self.last_graph)
        return value


    def index_of(self,a,list):
        for i in range(0,len(list)):
            if list[i] == a:
                return i
        return -1


    def sort_by_values(self, list1, values):
        return sorted(list1, key = lambda x:values[x])
         
    
    def fast_non_dominated_sort(self,values1, values2, return_rank = False):
        S=[[] for i in range(0,len(values1))]
        front = [[]]
        n=[0 for i in range(0,len(values1))]
        rank = [0 for i in range(0, len(values1))]
    
        for p in range(0,len(values1)):
            S[p]=[]
            n[p]=0
            for q in range(0, len(values1)):
                if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
                    if q not in S[p]:
                        S[p].append(q)
                elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
                    n[p] = n[p] + 1
            if n[p]==0:
                rank[p] = 0
                if p not in front[0]:
                    front[0].append(p)
    
        i = 0
        while(front[i] != []):
            Q=[]
            for p in front[i]:
                for q in S[p]:
                    n[q] =n[q] - 1
                    if( n[q]==0):
                        rank[q]=i+1
                        if q not in Q:
                            Q.append(q)
            i = i+1
            front.append(Q)
    
        del front[len(front)-1]
        if return_rank:
            return front, rank
        return front
    
    def get_neighbors(self, point, values):
        #values.append(point)
        left = min(values)
        right = max(values)
        zeros = False
        for i in values:
            if  i == point:
                if not zeros:
                    left = point
                    zeros = True
                else:
                    right = point
                    return left, right
            elif i < point:
                if i >= left:
                    left = i
            else:
                if i <= right:
                    right = i
        if left > point:
            return -math.inf, right
        if right < point:
            return left, math.inf
        return left, right

#Function to calculate crowding distance
    def crowding_distance(self,values1, values2, front, sde = False):

        distance = [0 for i in range(0,len(front))]
        #distance[0] = math.inf
        #distance[len(front) - 1] = math.inf
        if sde == True:
            shifted_dict = SDE(front, values1, values2)
            for k in range(0, len(front)):
                current_node = front[k]
                current_situation = shifted_dict[current_node]
                values1 = [i[0] for i in current_situation[1]]
                values2 = [i[1] for i in current_situation[1]]
                try:
                    left1, right1 = self.get_neighbors(current_situation[0][0], values1)
                    distance[k] = distance[k]+ right1 - left1
                
                except Exception:
                    pass
                try:
                    left2, right2 = self.get_neighbors(current_situation[0][1], values2)
                    distance[k] = distance[k]+ right2 - left2
                except Exception:
                    pass
            return distance
                
                
                
        sorted1 = self.sort_by_values(front, values1[:])
        sorted2 = self.sort_by_values(front, values2[:])
        distance[front.index(sorted1[0])] = math.inf
        distance[front.index(sorted1[-1])] = math.inf
        distance[front.index(sorted2[0])] = math.inf
        distance[front.index(sorted2[-1])] = math.inf
        for i in range(0, len(front)):
            k = front[i]
            try:
                sorted1_index = sorted1.index(k)
                
                distance[i] = distance[i]+ (values1[sorted1[sorted1_index+1]] - values1[sorted1[sorted1_index-1]])/(max(values1)-min(values1)) 
            except Exception:
                pass
            try:
                sorted2_index = sorted2.index(k)
                distance[i] = distance[i]+ (values2[sorted2[sorted2_index+1]] - values2[sorted2[sorted2_index-1]])/(max(values2)-min(values2))
            except Exception:
                pass
        return distance


    def crossover(self,a,b):
        r = np.random.binomial(1, self.crossover_prob, len(a))
        return self.mutation(np.where(r == 0, a, b).tolist()), self.mutation(np.where(r == 1, a, b).tolist())

    def mutation(self,solution):
        
        if random.random() < self.mutation_prob:    
            mutation_pos = random.randint(0,len(solution)-1)
            if solution[mutation_pos] == -1 or len(list(self.graph.neighbors(mutation_pos))) == 0:
                solution = self.mutation(solution)
            else:
                
                solution[mutation_pos] = choice(list(self.graph.neighbors(mutation_pos)))
   
                
        return solution

    





    def start(self):
        solution= self.init_pop
        gen_no=0
       
        while(gen_no< self.max_gen):
            #print(gen_no)
            
            function1_values = list(map(self.function1, solution))
            function2_values = list(map(self.function2, solution))
            
            non_dominated_sorted_solution, non_dominated_rank = self.fast_non_dominated_sort(function1_values[:],function2_values[:], return_rank=True)
            
           
            non_dominated_rank = (1 / (np.array(non_dominated_rank) + 1))
            solution2 = solution[:]
            #Generating offsprings
            while(len(solution2)<2*self.pop_size):
                a1 = choices(range(self.pop_size), weights = non_dominated_rank)[0]
                b1 = choices(range(self.pop_size), weights = non_dominated_rank)[0]
                new_a1, new_a2 = self.crossover(solution[a1],solution[b1])
                solution2.append(new_a1)
                solution2.append(new_a2)
            
            function1_values2 = list(map(self.function1, solution2))
            function2_values2 = list(map(self.function2, solution2))
            
            non_dominated_sorted_solution2 = self.fast_non_dominated_sort(function1_values2[:],function2_values2[:])
            #print(non_dominated_sorted_solution2)
            
            new_solution= []
            i = 0
            while len(new_solution + [solution2[k] for k in non_dominated_sorted_solution2[i]]) <= self.pop_size:
                new_solution += [solution2[k] for k in non_dominated_sorted_solution2[i]]
                i += 1
            if self.pop_size - len(new_solution) > 0:
                crowd_distance_i = self.crowding_distance(function1_values2,function2_values2,non_dominated_sorted_solution2[i], sde = self.sde)
                
                #print(gen_no, crowd_distance_i)
                zip_data = list(zip(non_dominated_sorted_solution2[i], crowd_distance_i))
                a = sorted(zip_data, key = lambda x:x[1], reverse = True)
                #print(a)
                
                #sorted(non_dominated_sorted_solution2[i], key = lambda x:crowd_distance_i[non_dominated_sorted_solution2[i].index(x)],reverse = True)
                #print(a)
                #print(len(new_solution), a, [solution2[k] for k in a[0:(self.pop_size - len(new_solution))]])
                new_solution += [solution2[k[0]] for k in a[0:(self.pop_size - len(new_solution))]]
            
            
            solution = new_solution
            gen_no = gen_no + 1
        #print(len(solution[0]))
        return solution

    def Visualization(self,solutions):
        function1_values = [self.function1(solutions[i])for i in range(self.pop_size)]
        function2_values = [self.function2(solutions[i])for i in range(self.pop_size)]

        function1 = [i  for i in function1_values]
        function2 = [j  for j in function2_values]
        plt.xlabel('Function 1', fontsize=15)
        plt.ylabel('Function 2', fontsize=15)
        plt.scatter(function1, function2)
        plt.show()


if __name__ =="__main__":
    #pass
    G2 = nx.karate_club_graph()
    G2 =  nx.convert_node_labels_to_integers(G2)

    G1=nx.karate_club_graph()
    G1 =  nx.convert_node_labels_to_integers(G1)
    G1.add_edge(0,1) 
    G1.add_edge(0,2) 
    G1.add_edge(1,3) 
    G1.add_edge(0,3)
    G1.add_edge(2,3)
    G1.add_edge(2,1)
    
    seed = []
    for i in range(50):
        graph_label = []
        for node in list(G1.nodes()):
            node_neighbor = [neighbor for neighbor in G1.neighbors(node)]
            graph_label.append(choice(node_neighbor))
        seed.append(graph_label)
    NG2 = NSGA2(evaluation.Modularity, seed,G1,max_gen=100, sde = False)
    solution = NG2.start()
    solution_values =  [evaluation.community_score(G1,solution[k]) for k in range(len(solution))]
    best_solution = solution[solution_values.index(max(solution_values))]
    
    
    seed = []
    for i in range(50):
        graph_label = []
        for node in list(G2.nodes()):
            node_neighbor = [neighbor for neighbor in G2.neighbors(node)]
            graph_label.append(choice(node_neighbor))
        seed.append(graph_label)
    NG2 = NSGA2(evaluation.Modularity, seed,G2,max_gen=100, last_solution=best_solution, last_graph = G1, sde = False)
    solution2 = NG2.start()
    solution_values2 =  [evaluation.community_score(G2,solution2[k]) for k in range(len(solution2))]
    best_solution2 = solution2[solution_values.index(max(solution_values))]


