#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main function

@auth: Jungang Zou
@date: 2021/08/23
"""

import networkx as nx
import random
import argparse



from tmoga.algorithm.TMOGA import TMOGA

from tmoga.utils.file_parser import *
from tmoga.utils.visualization import visualization
from tmoga.utils.evaluation import evaluation





if __name__ == '__main__':
    random.seed(123)
    
    
    # parse parameters
    parser = argparse.ArgumentParser(description='Run TMOGA on some datasets')
    
    parser.add_argument("output", help = "indicate the directory of output", type = str)
    parser.add_argument("-d", "--dataset", help = "specify which the dataset to use", default = "synfix3", choices = ["synfix3", "synfix6", "synvar3", "synvar6", "birth_death", "expansion_contraction", "intermittent", "merge_split", "mobile_phone_call"])
    parser.add_argument("-g", "--generation", help = "indicate the number of generations on each snapshot", type = int, default = 100)
    parser.add_argument("-p", "--population", help = "indicate the size of population", type = int, default = 200)
    parser.add_argument("--CID", help = "indicate the CID threshold", type = float, default = 0.8)
    parser.add_argument("--Md", help = "indicate the max depth of search tree", type = int, default = 5)
    parser.add_argument("--Tp", help = "indicate the transfer probability", type = float, default = 0.5)
    parser.add_argument("--Cp", help = "indicate the crossover probability", type = float, default = 0.8)
    parser.add_argument("--Mp", help = "indicate the mutation probability", type = float, default = 0.2)
    

    args = parser.parse_args()
    
    
    # check parameters.
    if args.generation <= 0:
        raise ValueError("Number of generation must be larger than 0")
    if args.population <= 0:
        raise ValueError("Population size must be larger than 0")
    if args.CID < 0 or args.CID > 1:
        raise ValueError("CID must be value between [0, 1]")
    if args.Md <= 0:
        raise ValueError("The max depth of search tree must be larger than 0")
    if args.Tp < 0 or args.Tp > 1:
        raise ValueError("Transfer probability must be value between [0, 1]")
    if args.Cp < 0 or args.Cp > 1:
        raise ValueError("Crossover probability must be value between [0, 1]")
    if args.Mp < 0 or args.Mp > 1:
        raise ValueError("Mutation probability must be value between [0, 1]")
        
        
    
    # specify dataset
    if args.dataset == "synfix3":
        g,label = syntetic_dynamic_graph("./dataset/SYNFIXZ3")
    
    elif args.dataset == "synfix6": 
        g,label = syntetic_dynamic_graph("./dataset/SYNFIXZ6")
        
    elif args.dataset == "synvar3":
        g,label = syntetic_dynamic_graph("./dataset/SYNVARZ3")
        
    elif args.dataset == "synvar6":
        g,label = syntetic_dynamic_graph("./dataset/SYNVARZ6")
        
    elif args.dataset == "birth_death":
        g,label = syntetic_event_dynamic_graph("./dataset/SYNEVENT/birth_death", start = 1)
        
    elif args.dataset == "expansion_contraction":
        g,label = syntetic_event_dynamic_graph("./dataset/SYNEVENT/expansion_contraction", start = 1)
        
    elif args.dataset == "intermittent":
        g,label = syntetic_event_dynamic_graph("./dataset/SYNEVENT/intermittent", start = 1)
        
    elif args.dataset == "merge_split":
        g,label = syntetic_event_dynamic_graph("./dataset/SYNEVENT/merge_split", start = 1)
        
    elif args.dataset == "mobile_phone_call":
        g = phone_call("./dataset/mobile_phone_call/CellPhoneCallRecords.csv")
        
    else:
        raise ValueError("This dataset cannot be found")
    
    
    # collect parameters for algorithm
    pop_size = args.population
    generation = args.generation
    CID = args.CID
    mutation_prob = args.Mp
    crossover_prob = args.Cp
    transfer_prob = args.Tp
    max_num_cliques = args.Md
    directory = args.output
    
    print("Parameters:")
    print("Population size:", pop_size)
    print("Number of generations:", generation)
    print("CID threshold:", CID)
    print("Max depth of search tree:", max_num_cliques)
    print("Transfer probability", transfer_prob)
    print("Crossover probability", crossover_prob)
    print("Mutation probability", mutation_prob)
    print()
    
    
    # run model
    print("Start running the TMOGA algorithm")
    tmoga = TMOGA(g, pop_size, generation, CID = CID, mutation_prob = mutation_prob, crossover_prob = crossover_prob, transfer_prob = transfer_prob, max_num_cliques = max_num_cliques)
    pop_solutions_tmoga, pop_encoding_solution = tmoga.start()
    print("End running the TMOGA algorithm")
    print()
    
    print("Evaluation:")
    modularity = list(map(lambda x:round(evaluation.Modularity(g[x], pop_solutions_tmoga[x]), 3), range(len(g))))
    
    print("Modularity for each snapshot:", modularity)
    if args.dataset != "mobile_phone_call":
        NMI = (list(map(lambda x:round(evaluation.NMI_with_Truth(label[x], pop_solutions_tmoga[x], locus = True), 3), range(len(g)))))
        print("NMI for each snapshot:", NMI)
    print()    
    
    print("The solutions are saved at: " + directory + "/")
    write_locus(pop_solutions_tmoga, directory)
    
    
