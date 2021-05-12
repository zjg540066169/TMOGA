# -*- coding: utf-8 -*-
"""
Extract transfered feature in communities.

@auth: Jungang Zou
@date: 2018/05/10
"""
import networkx as nx
from utils.evaluation import evaluation
    
class Clique_Discover(object):
    def __init__(self):
        pass
    
    @classmethod
    def clique_discover(self, G, clusters, CID = 0.8):
        #print(G, clusters, CID)
        clique_list = []
        for c in clusters:
            #print(self.__clique_in_community(G, c, CID))
            clique_list += self.__clique_in_community(G, c, CID)
        #print(clique_list)
        return sorted(clique_list, key = lambda x:len(x))
            
    
    @classmethod
    def __clique_in_community(self, G, c, CID = 0.8):
        if evaluation.community_CID(G, c) >= CID:
            return [c]
        cliques = []
        c = sorted(c)
        searched = set()
        for i in range(len(c) - 1):
            current_node = c[i]
            if current_node in searched:
                continue
            neighbor = [j for j in set(G[current_node].keys()).intersection(c) if j > current_node]
            result = self.__clique_search(G, set(c), set([current_node]), neighbor, current_node, CID = CID)
            if len(result) > 0:
                searched = searched.union(result)
                cliques.append(list(result))
        return cliques
    
            
    @classmethod
    def __clique_search(self, G, community, v_subgraph, v_candidate, current_node, edges = 0, CID = 0.8):
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
                result = self.__clique_search(G, community, new_v_subgraph, v_candidate_new, current_node, new_edges, CID)
                if len(clique_max) < len(result):
                    clique_max = result
        #print(clique_max)
        if len(clique_max)>2:
            return clique_max
        else:
            return []
                
                
    
    
    
    
    
        

if __name__=='__main__':
    from utils.evaluation import evaluation
    from networkx.algorithms import community
    from utils.visualization import visualization
    g = nx.karate_club_graph()
    communities_generator = community.girvan_newman(g)
    top_level_communities = next(communities_generator)
    next_level_communities = next(communities_generator)
    clusters = sorted(map(sorted, next_level_communities))
    a = Clique_Discover.clique_discover(g, clusters, CID = 0.8)
    print(a)
    #visualization.visualize_cliques(g, a)
    
    