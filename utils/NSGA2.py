# -*- coding: utf-8 -*-
"""
Run the algorithm NSGA2

@auth: Jungang Zou
@date: 2018/06/02
"""

from utils.evaluation import evaluation
import networkx as nx
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from random import choice

class NSGA2:
    def __init__(self, objective_func, init_population,graph, last_solution=None, last_graph = None, max_gen = 999, mutation_prob = 0.9, crossover_prob = 0.5):
        self.objective_func = objective_func
        self.init_pop = init_population
        self.graph = graph
        self.last_solution = last_solution
        self.last_graph = last_graph
        self.pop_size = len(init_population)
        self.max_gen = max_gen
        self.mutation_prob = mutation_prob
        self.crossover_prob = crossover_prob
    
    def function1(self,solution):#modularity
        value = self.objective_func(self.graph, solution)
        return value

    #Second function to optimize
    def function2(self,solution):#NMI
        if self.last_solution is None:
            return 0
        value = evaluation.NMI(solution,self.last_solution,self.graph,self.last_graph)
        return value

    #Function to find index of list
    def index_of(self,a,list):
        for i in range(0,len(list)):
            if list[i] == a:
                return i
        return -1

#Function to sort by values
    def sort_by_values(self, list1, values):
        sorted_list = []
        while(len(sorted_list)!=len(list1)):
            if self.index_of(min(values),values) in list1:
                sorted_list.append(self.index_of(min(values),values))
            values[self.index_of(min(values),values)] = math.inf
        return sorted_list

#Function to carry out NSGA-II's fast non dominated sort
    def fast_non_dominated_sort(self,values1, values2):
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
        return front

#Function to calculate crowding distance
    def crowding_distance(self,values1, values2, front):
        distance = [0 for i in range(0,len(front))]
        sorted1 = self.sort_by_values(front, values1[:])
        sorted2 = self.sort_by_values(front, values2[:])
        distance[0] = math.inf
        distance[len(front) - 1] = math.inf
        for k in range(1,len(front)-1):
            try:
                distance[k] = distance[k]+ (values1[sorted1[k+1]] - values2[sorted1[k-1]])/(max(values1)-min(values1))
            except ZeroDivisionError:
                continue
   
        
        for k in range(1,len(front)-1):
            try:
                distance[k] = distance[k]+ (values1[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
            except ZeroDivisionError:
                continue
        return distance

#Function to carry out the crossover
    def crossover(self,a,b):
        r = np.random.binomial(1, self.crossover_prob, len(a)).tolist()
        solution = []
        for i in r:
            if i == 0:
                solution.append(a[i])
            elif i==1:
                solution.append(b[i])
            else:
                raise Exception
        return self.mutation(solution)


#Function to carry out the mutation operator
    def mutation(self,solution):
        if random.random() < self.mutation_prob:    
            mutation_pos = random.randint(0,len(solution)-1)
            if len(list(self.graph.neighbors(mutation_pos))) == 0:
                solution[mutation_pos] = mutation_pos
            else:
                solution[mutation_pos] = choice(list(self.graph.neighbors(mutation_pos)))
        return solution

    
#Main program starts here



#Initialization
    def start(self):
        solution= self.init_pop
        gen_no=0
        while(gen_no< self.max_gen):
            function1_values = [self.function1(solution[i])for i in range(self.pop_size)]
            function2_values = [self.function2(solution[i])for i in range(self.pop_size)]
            non_dominated_sorted_solution = self.fast_non_dominated_sort(function1_values[:],function2_values[:])
            print("The best front for Generation number ",gen_no, " is")
            for valuez in non_dominated_sorted_solution[0]:
                print((round(self.function1(solution[valuez]),3),round(self.function2(solution[valuez]),3)),end=" ")
            print("\n")
            crowding_distance_values=[]
            for i in range(0,len(non_dominated_sorted_solution)):
                crowding_distance_values.append(self.crowding_distance(function1_values[:],function2_values[:],non_dominated_sorted_solution[i][:]))
            solution2 = solution[:]
            #Generating offsprings
            while(len(solution2)!=2*self.pop_size):
                a1 = random.randint(0,self.pop_size-1)
                b1 = random.randint(0,self.pop_size-1)
                solution2.append(self.crossover(solution[a1],solution[b1]))
            function1_values2 = [self.function1(solution2[i])for i in range(0,2*self.pop_size)]
            function2_values2 = [self.function2(solution2[i])for i in range(0,2*self.pop_size)]
            non_dominated_sorted_solution2 = self.fast_non_dominated_sort(function1_values2[:],function2_values2[:])
            crowding_distance_values2=[]
            for i in range(0,len(non_dominated_sorted_solution2)):
                crowding_distance_values2.append(self.crowding_distance(function1_values2[:],function2_values2[:],non_dominated_sorted_solution2[i][:]))
            new_solution= []
            for i in range(0,len(non_dominated_sorted_solution2)):
                non_dominated_sorted_solution2_1 = [self.index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i] ) for j in range(0,len(non_dominated_sorted_solution2[i]))]
                front22 = self.sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
                front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
                front.reverse()
                for value in front:
                    new_solution.append(value)
                    if(len(new_solution)== self.pop_size):
                        break
                if (len(new_solution) == self.pop_size):
                    break
            solution = [solution2[i] for i in new_solution]
            gen_no = gen_no + 1
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
    G2 = nx.karate_club_graph()
    G2 =  nx.convert_node_labels_to_integers(G2)
    seed = []
    for i in range(50):
        graph_label = []
        for node in list(G2.nodes()):
            node_neighbor = [neighbor for neighbor in G2.neighbors(node)]
            graph_label.append(choice(node_neighbor))
        seed.append(graph_label)
    NG2 = NSGA2(evaluation.Modularity, seed,G2,max_gen=100)
    solution = NG2.start()
