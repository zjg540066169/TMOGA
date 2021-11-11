# -*- coding: utf-8 -*-
"""
Extract transfered feature in communities. (feature extraction)

@auth: Jungang Zou
@date: 2018/05/10
"""
import networkx as nx
from tmoga.utils.evaluation import evaluation
import multiprocessing
from joblib import Parallel, delayed

class Clique_Discover(object):
    def __init__(self):
        pass
    
    @classmethod
    def clique_discover(self, G, clusters, CID = 0.8, max_num_cliques = 5):
        #print(G, clusters, CID)
        clique_list = []
        num_cores = multiprocessing.cpu_count()
        results = Parallel(n_jobs=num_cores)(delayed(self.clique_in_community)(G, clusters[i], CID, max_num_cliques) for i in range(len(clusters)))
        #print(results)                
        for i in results:
            if len(i) > 0:
                clique_list.extend(i)
        #print(clique_list)    
        return sorted(clique_list, key = lambda x:len(x))
            
    
    @classmethod
    def clique_in_community(self, G, c, CID = 0.8, max_num_cliques = 5):
        if len(c) <= 2:
            return []
        if evaluation.community_CID(G, c) >= CID:
            return [c]
        
        cliques = []
        c = sorted(c)
        searched = set()
        for i in range(len(c) - 1):
            #print(searched, c[i])
            current_node = c[i]
            if current_node in searched:
                continue
            neighbor = [j for j in set(G[current_node].keys()).intersection(c) if j > current_node and j not in searched]
            #print(searched, c[i], neighbor)
            result = self.clique_search(G, set(c), set([current_node]), neighbor, current_node, CID = CID, max_num_cliques = max_num_cliques, searched = searched)
            if len(result) > 0:
                searched = searched.union(result)
                cliques.append(list(result))
            
        return cliques
    
            
    @classmethod
    def clique_search(self, G, community, v_subgraph, v_candidate, current_node, edges = 0, CID = 0.8, max_num_cliques = 5, searched = []):
        clique_max = v_subgraph
        
        while len(v_candidate) != 0:
            w = v_candidate[0]
            
            v_candidate.remove(v_candidate[0])
            w_neighbor = set(G[w].keys())
            new_edges = edges
            v_candidate_new = v_candidate.copy()
            for n in w_neighbor:
                #print(n)
                
                if n in v_subgraph:
                    new_edges += 1
                    #print(n)
                    continue
                elif n in searched:
                    continue
                elif n <= current_node:
                    continue
                elif n in v_candidate:
                    continue
                elif n not in community:
                    continue
                else:
                    v_candidate_new.append(n)
            
            if (new_edges * 2 / (len(v_subgraph) * (len(v_subgraph) + 1)) < CID):
                continue
            else:
                new_v_subgraph = v_subgraph.copy()
                new_v_subgraph.add(w)
                if len(new_v_subgraph) >= max_num_cliques:
                    return new_v_subgraph
                result = self.clique_search(G, community, new_v_subgraph, v_candidate_new, current_node, new_edges, CID, max_num_cliques, searched = searched)
                if len(clique_max) < len(result):
                    clique_max = result
        #print(clique_max)
        if len(clique_max)>2:
            return clique_max
        else:
            return []