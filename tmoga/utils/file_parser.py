#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file provides functions to read data into networkx

@auth: Jungang Zou
@date: 2021/05/05
"""
import numpy as np
import networkx as nx
import os
import pandas as pd
from tmoga.utils.evaluation import evaluation
def syntetic_read_edgelist(filename,weighted = False, return_graph = False, start = 0):
    idmap = set()
    edge_cache = {}
    if return_graph:
        G = nx.Graph()
    with open(filename) as f:
        for line in f:
            if weighted:
                u,v,w = [int(x) for x in line.strip().split()]
            else:
                tmp = [x for x in line.strip().split()]
                u,v,w  = int(tmp[0]),int(tmp[1]),1.0
                if return_graph:
                    G.add_edge(u - start, v - start)
            edge_cache[(u - start,v - start)] = w
            idmap.add(u - start)
            idmap.add(v - start)
                   
                    
            
    idmap = list(idmap)                                   
    idmap_inv = {nid: i for i,nid in enumerate(idmap)}  
    N = len(idmap)
    adj_mat = np.zeros((N,N))
    for (u,v),w in edge_cache.items():
        adj_mat[idmap_inv[u],idmap_inv[v]] = w
    adj_mat += adj_mat.T
    if return_graph:
        return G
    else:
        return idmap, idmap_inv, adj_mat
   
def syntetic_read_label(filename, start = 0, clusters = False):
    label = {}
    if not clusters:
        with open(filename) as f:
            for line in f:
                node, community = [int(x) for x in line.strip().split()]
                label[community - start] = label.get(community - start, [])
                label[community - start].append(node - start)
    else:
        com = 0
        with open(filename) as f:
            for line in f:
                nodes = [int(x) for x in line.strip().split()]
                if len(nodes) > 0:
                    label[com] = (np.array(nodes) - start).tolist()
                    com += 1
    return label
    
def syntetic_dynamic_graph(directory, truth = True, start = 0):
    files = os.listdir(directory)
    dynamic_graphs = []
    truth_label = []
    for i in range(1000000):
        file_name = directory + "/" + str(i)
        if str(i) + ".edgelist" not in files:
            break
        #print()
        
        dynamic_graphs.append(syntetic_read_edgelist(file_name + ".edgelist", return_graph=True, start= start))
        if truth:
            truth_label.append(syntetic_read_label(file_name + ".comm"))
    if truth:
        return dynamic_graphs, truth_label
    return dynamic_graphs

def phone_call(file_path):
    d = pd.read_csv(file_path)
    graph_list = []
    t = d.iloc[0, 2][:8]
    G = nx.Graph()
    for i in range(len(d)):
        current_time = d.iloc[i, 2][:8]
        #print(current_time)
        if current_time == t:
            G.add_edge(d.iloc[i, 0], d.iloc[i, 1])
        else:
            graph_list.append(G)
            G = nx.Graph()
            G.add_edge(d.iloc[i, 0], d.iloc[i, 1])
        t = current_time
    graph_list.append(G)
    return graph_list


        

def syntetic_event_dynamic_graph2(graph_path, community_path):
    d = pd.read_csv(graph_path, header = None, sep = " ")
    graph_list = []
    d = d.iloc[:, [0, 1, 3]]
    t = d.iloc[0, 2]
    G = nx.Graph()
    for i in range(len(d)):
        current_time = d.iloc[i, 2]
        #print(current_time)
        if current_time == t:
            G.add_edge(d.iloc[i, 0], d.iloc[i, 1])
        else:
            graph_list.append(G)
            G = nx.Graph()
            G.add_edge(d.iloc[i, 0], d.iloc[i, 1])
        t = current_time
    graph_list.append(G)
    c = pd.read_csv(community_path, header = None, sep = " ")
    label_list = []
    t = c.iloc[0, 0]
    label = {}
    for i in range(len(c)):
        current_time = d.iloc[i, 0]
        if current_time == t:
            community = c.iloc[i, 2]
            label[community] = label.get(community, [])
            label[community].append(c.iloc[i, 1])
        else:
            label_list.append(label)
            label = {}
            community = c.iloc[i, 2]
            label[community] = label.get(community, [])
            label[community].append(c.iloc[i, 1])
        t = current_time
    label_list.append(label)
    
    
    return graph_list, label_list


def syntetic_event_dynamic_graph(directory, truth = True, start = 1):
    files = os.listdir(directory)
    dynamic_graphs = []
    truth_label = []
    #print(directory)
    for i in range(1, 1000000):
        file_name = directory + "/" + str(i)
        #print(file_name)
        if str(i) + ".edges" not in files:
            break
        #print()
        
        dynamic_graphs.append(syntetic_read_edgelist(file_name + ".edges", return_graph=True, start= start))
        if truth:
            truth_label.append(syntetic_read_label(file_name + ".comm", clusters = True, start = start))
    if truth:
        return dynamic_graphs, truth_label
    return dynamic_graphs


def write_locus(pop_solutions_tmoga, directory):
    for i in range(len(pop_solutions_tmoga)):
        path = directory  + "/" + str(i) + ".comm"
        node_community = evaluation.community_nodes_to_node_community(evaluation.parse_locus_solution(pop_solutions_tmoga[i]))
        sorted_answer = sorted(node_community.items(), key = lambda x:x[0])
        with open(path, "w") as f:
            for line in sorted_answer:
                f.write(str(line[0]) + " " + str(line[1]) + "\n")
    

if __name__ == "__main__":
    a, c = syntetic_event_dynamic_graph("../dataset/syntetic_event/intermittent", start = 1)
    #g = enron_email("../dataset/enron_email/enron_corrected.csv")#phone_call("../dataset/cell_phone_call/CellPhoneCallRecords.csv")
    #g, label = syntetic_dynamic_graph("../dataset/syntetic2")
        