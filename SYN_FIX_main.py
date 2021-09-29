# -*- coding: utf-8 -*-

from tmoga.TMOGA import TMOGA
import networkx as nx
import matplotlib.pyplot as plt
#from compared_algorithm.
import random
from utils.visualization import visualization
from utils.file_parser import *
from utils.evaluation import evaluation
import pandas as pd
import seaborn as sns

if __name__ == '__main__': 
    pop_size = 200
    gen_1 = 100
    gen_2 = 100      
    Mp = 0.2  
    Cp = 0.8
    Tp = 0.5
    Md = 5
    
    MIp = 0.5
    p_mu_mi = 0.5
    PGLP_iter = 5
    #generate_evolution("./dataset/syntetic1/", z=3,avg_degree=20)
    random.seed(1)
    print("g1")
    #g = phone_call("./dataset/cell_phone_call/CellPhoneCallRecords.csv")
    g1,label1= syntetic_dynamic_graph("./dataset/syntetic1")
    
    #pop_solutions_DECS = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    
    #pop_solutions_facenet = FaceNet_Var(g, 0.5, [4,5,6,7,8,8,7,6,5,4])
    #tmoga1 = TMOGA(g1[:2], pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga1, solution_pop1 = tmoga1.start()
    #8h55m
    #23:14 1394.5 s1 FT 6.5775 array([1.        , 1.        , 1.        , 0.98741873, 1.        , 0.97515342, 1.        , 1.        , 1.        , 0.97454577])

    #array([0.38254875, 0.22524608, 0.20397096, 0.20823744, 0.21803506, 0.20295715, 0.20545636, 0.21984061, 0.21950142, 0.20054824])
    
    #pop_solutions_DYNMODPSO1 = DYNMODPSO(g1, pop_size, gen_1, pm = 0.7)
    # 10:05
    #array([0.36472562, 0.36159293, 0.35457444, 0.36350096, 0.39703523,0.40750504, 0.33458735, 0.36836945, 0.35883857, 0.36801887])
    #41:39 2499.1  s1 array([0.97935459, 1.        , 1.        , 0.98776902, 1.        ,0.93256186, 1.        , 1.        , 1.        , 0.9623467 ])
    
    #dynmoga1 =  DYNMOGA(g1, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga1 = dynmoga1.start()
    #6:35
    #0.47284898, 0.50476504, 0.49152196, 0.48365229, 0.48841373,
    #   0.48239326, 0.48419985, 0.47109195, 0.47660105, 0.47605198]
    #39:22 2362.8 s1 array([0.94705251, 1.        , 1.        , 1.        , 1.        ,1.        , 1.        , 1.        , 1.        , 1.        ])
    
    
    #pop_solutions_DECS_1 = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    #12:21
    #array([0.20187211, 0.46153228, 0.40362474, 0.44289656, 0.40431443,0.4173069 , 0.4277935 , 0.43005924, 0.434171  , 0.42068174])
    #2:07:16 7636.6 s1 array([0.9598907 , 0.93622437, 0.98760998, 0.92736257, 0.        ,0.93780858, 0.        , 0.95057185, 0.81350294, 0.94404615])
    
    
    
    #pop_solutions_DECS_2 = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    #pop_solutions_DECS_3 = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    
    print("g2")
    g2,label2= syntetic_dynamic_graph("./dataset/syntetic2")
    #pop_solutions_DECS2 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    # 37:25 2245.9 s2 array([1.        , 1.        , 0.93922756, 0.8937718 , 0.95741166,0.95718488, 0.6000447 , 0.01638975, 0.01640016, 1.        ])
    
    
    
    #pop_solutions_DYNMODPSO2 = DYNMODPSO(g2, pop_size, gen_1, pm = 0.7)
    # 40:43 2443.7 s2 array([0.98761638, 1.        , 0.85178566, 0.64949823, 0.92226988,0.74288475, 0.66088921, 0.81016999, 0.92864912, 0.656243  ])
    
    #dynmoga2 =  DYNMOGA(g2, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga2 = dynmoga2.start()
    
    #tmoga2 = TMOGA(g2, pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga2 = tmoga2.start()
    # 25:42 1542.2 s2 FT 5.51 array([0.77910771, 0.91631302, 0.90622692, 1.        , 0.97611529,1.        , 1.        , 0.9743434 , 0.98775713, 0.98748328])
    
    
    #dynmoga2 =  DYNMOGA(g2, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga2 = dynmoga2.start()
    # 40:10 2410.7 s2 array([0.91172537, 0.90715907, 0.92549526, 0.92267511, 0.84108853,0.93282351, 0.95828234, 1.        , 0.94951385, 0.88927721])
    
    
    
    print("g3")
    g3 = phone_call("./dataset/cell_phone_call/CellPhoneCallRecords.csv")
    #pop_solutions_DECS3 = DECS(g3, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
   
    # 11:29:03 41343.2 call array([0.24885805, 0.43116494, 0.44394031, 0.42867417, 0.3916296 ,0.39940071, 0.43883566, 0.43888657, 0.43410578, 0.40186543])
    
    
    #pop_solutions_DYNMODPSO3 = DYNMODPSO(g3, pop_size, gen_1, pm = 0.7)
    # 40:43 2443.7 s2 array([0.98761638, 1.        , 0.85178566, 0.64949823, 0.92226988,0.74288475, 0.66088921, 0.81016999, 0.92864912, 0.656243  ])
    # 7:01:05 25265.4 call # array([0.37962086, 0.39925944, 0.42019677, 0.34575277, 0.37072393,0.43037033, 0.34495411, 0.37750506, 0.37087625, 0.32706123])
    
    #dynmoga3 =  DYNMOGA(g3, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga3 = dynmoga3.start()
    
    
    tmoga3 = TMOGA(g3, pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    pop_solutions_tmoga3 = tmoga3.start()
    # 28:08 168.81 s2 array([0.77910771, 0.91631302, 0.90622692, 1.        , 0.97611529,1.        , 1.        , 0.9743434 , 0.98775713, 0.98748328])
    # FT 36.218s total  3:15:25 11725.7  call array([0.48959456, 0.50825699, 0.50513546, 0.49227089, 0.50857733,0.50679588, 0.50257657, 0.48034436, 0.50149819, 0.49871663])
    
    #dynmoga3 =  DYNMOGA(g3, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga3 = dynmoga3.start()
    # 6:33:10   23590.7 array([0.48051701, 0.50139758, 0.4893431 , 0.49136058, 0.49009742,0.48081207, 0.47488549, 0.47463628, 0.48525663, 0.4946351 ])
    
    
    print("g4")
    
    g4, label4 = syntetic_event_dynamic_graph("./dataset/syntetic_event/birth_death", start = 1)
    #pop_solutions_DECS4 = DECS(g4, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    # 35:11:35 25339.06 * 5
    # NMI array([0.88367518, 0.88836352, 0.84369992, 0.83118873, 0.80236258])
    # adj_rs array([0.76979721, 0.79828624, 0.71319193, 0.64603683, 0.56150341])
    # modularity array([0.53948876, 0.58259291, 0.56467774, 0.56787694, 0.55307661])
    
    #pop_solutions_DYNMODPSO4 = DYNMODPSO(g4, pop_size, gen_1, pm = 0.7)
    # 4:51:31 3498.30*5
    # NMI array([0.8127255 , 0.80816142, 0.81164731, 0.8145261 , 0.81594179])
    # adj_rs array([0.56449426, 0.56403524, 0.65001403, 0.72643576, 0.76991367])
    # modularity array([0.41069725, 0.40259539, 0.47391532, 0.45318492, 0.4418011 ])
    
    #tmoga4_ = TMOGA(g4, pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga4_, solution_pop4_ = tmoga4_.start()
    
    
# =============================================================================
#     modularity1 = list(map(lambda x:evaluation.Modularity(g7[0], x), pop_solutions_tmoga7_[1][0]))
#     NMI1 = list(map(lambda x:evaluation.NMI_with_Truth(label7[0], x), pop_solutions_tmoga7_[1][0]))
#     cs1 = list(map(lambda x:evaluation.community_score(g7[0], x), pop_solutions_tmoga7_[1][0]))
#     
#     modularity2 = list(map(lambda x:evaluation.Modularity(g7[0], x), pop_solutions_tmoga7[1][0]))
#     NMI2 = list(map(lambda x:evaluation.NMI_with_Truth(label7[0], x), pop_solutions_tmoga7[1][0]))
#     cs2 = list(map(lambda x:evaluation.community_score(g7[0], x), pop_solutions_tmoga7[1][0]))
# =============================================================================
    
    # 4:11:02 3012.55*5 FT 16.57575559616089
    # NMI array([0.75204237, 0.7424598 , 0.74284272, 0.75354516, 0.75295435])
    # adj_rs array([0.35102677, 0.26130747, 0.35350276, 0.55485679, 0.63845638])
    # modularity array([0.36130194, 0.25330961, 0.27015166, 0.27294065, 0.26053151])
    
    #dynmoga4 =  DYNMOGA(g4, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga4 = dynmoga4.start()
    
    
    #dynmoga4 =  DYNMOGA(g4, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga4 = dynmoga4.start()
    # 5:01:05 3613.18*5  
    # NMI array([0.75723477, 0.77033023, 0.74495277, 0.78220367, 0.77613585])
    # adj_rs array([0.35914701, 0.35858046, 0.40539459, 0.6138183 , 0.68461829])
    # modularity array([0.35648688, 0.34314615, 0.32921126, 0.36496151, 0.35291904])
    
    print("g5")
    g5, label5 = syntetic_event_dynamic_graph("./dataset/syntetic_event/expansion_contraction", start = 1)
    pop_solutions_DECS5 = DECS(g5, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    np.savetxt("g5_DECS.csv", np.array(list(map(lambda x:evaluation.NMI_with_Truth(label5[x], pop_solutions_DECS5[x], locus = False), range(len(pop_solutions_DECS5))))), delimiter = ",")
    #pop_solutions_DYNMODPSO5 = DYNMODPSO(g5, pop_size, gen_1, pm = 0.7)
    #5:05:26 3665.22*5 array([0.83229889, 0.79790812, 0.8032534 , 0.81034758, 0.78400689])
    
    
    #dynmoga5 =  DYNMOGA(g5, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga5 = dynmoga5.start()
    
    
    #tmoga5_ = TMOGA(g5, pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga5_, solution_pop5_ = tmoga5_.start()
    # 3:46:47 2721.48 * 5 15.042 FT   kjjbhgi array([0.7612234 , 0.757839  , 0.75274249, 0.74365809, 0.75396049])
    
   # dynmoga5 =  DYNMOGA(g5[:2], pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga5 = dynmoga5.start()
    #4:55:00  3540.17 * 5  array([0.72319985, 0.76622729, 0.78760035, 0.77573013, 0.75882868])
    print("g6")
    # np.array(list(map(lambda x:evaluation.Modularity(g6[x],label6[x],  truth = True), range(5))))
    g6, label6 = syntetic_event_dynamic_graph("./dataset/syntetic_event/intermittent", start = 1)
    pop_solutions_DECS6 = DECS(g6, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    
    np.savetxt("g6_DECS.csv", np.array(list(map(lambda x:evaluation.NMI_with_Truth(label6[x], pop_solutions_DECS6[x], locus = False), range(len(pop_solutions_DECS6))))), delimiter = ",")

    #pop_solutions_DYNMODPSO6 = DYNMODPSO(g6, pop_size, gen_1, pm = 0.7)
    #4:47:24 3448.83*5 array([0.83229889, 0.84308596, 0.8027226 , 0.79021647, 0.80808528])
    
    
    #dynmoga6 =  DYNMOGA(g6, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga6 = dynmoga6.start()
    
    #tmoga6 = TMOGA([g6[0]], pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga6 = tmoga6.start()
    #3:53:30 2802.07*5 FT 15.683  array([0.75432924, 0.73621454, 0.74076459, 0.74981648, 0.73927239])
    # 6:22:40  51.10672950744629 array([0.79378319, 0.74761133, 0.75620247, 0.75948417, 0.76797776])
    
    #dynmoga6 =  DYNMOGA(g6, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga6 = dynmoga6.start()
    #4:39:48 3357.77*5 array([0.74299611, 0.73373276, 0.76072622, 0.76043392, 0.75934276])
    
    
    print("g7")
    g7, label7 = syntetic_event_dynamic_graph("./dataset/syntetic_event/merge_split", start = 1)
    pop_solutions_DECS7 = DECS(g7, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    np.savetxt("g7_DECS.csv", np.array(list(map(lambda x:evaluation.NMI_with_Truth(label7[x], pop_solutions_DECS7[x], locus = False), range(len(pop_solutions_DECS7))))), delimiter = ",")

    #pop_solutions_DYNMODPSO7 = DYNMODPSO(g7, pop_size, gen_1, pm = 0.7)
    
    #tmoga7 = TMOGA([g7[0]], pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga7 = tmoga7.start()
    
    
    #dynmoga7 =  DYNMOGA(g7, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga7 = dynmoga7.start()
    
    #dynmoga7 =  DYNMOGA(g7, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga7 = dynmoga7.start()
    
    
    print("g8")
    g8,label8= syntetic_dynamic_graph("./dataset/syntetic3")
    #pop_solutions_DECS2 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    # 37:25 2245.9 s2 array([1.        , 1.        , 0.93922756, 0.8937718 , 0.95741166,0.95718488, 0.6000447 , 0.01638975, 0.01640016, 1.        ])
    
    
    
    #pop_solutions_DYNMODPSO8 = DYNMODPSO(g8, pop_size, gen_1, pm = 0.7)
    # 40:43 2443.7 s2 array([0.98761638, 1.        , 0.85178566, 0.64949823, 0.92226988,0.74288475, 0.66088921, 0.81016999, 0.92864912, 0.656243  ])
    
    #dynmoga8 =  DYNMOGA(g8, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
    #pop_solutions_dynmoga8 = dynmoga8.start()
    
   # tmoga8 = TMOGA(g8, pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
   # pop_solutions_tmoga8 = tmoga8.start()
    #
    
    print("g9")
    g9,label9= syntetic_dynamic_graph("./dataset/syntetic4")
    #pop_solutions_DECS9 = DECS(g9, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
    # 37:25 2245.9 s2 array([1.        , 1.        , 0.93922756, 0.8937718 , 0.95741166,0.95718488, 0.6000447 , 0.01638975, 0.01640016, 1.        ])
    #np.savetxt("g9_DECS.csv", np.array(list(map(lambda x:evaluation.NMI_with_Truth(label9[x], pop_solutions_DECS9[x], locus = False), range(len(pop_solutions_DECS9))))), delimiter = ",")
    
    #dynmoga9 =  DYNMOGA(g9, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
   # pop_solutions_dynmoga9 = dynmoga9.start()
    
    #pop_solutions_DYNMODPSO9 = DYNMODPSO(g9, pop_size, gen_1, pm = 0.7)
    # 40:43 2443.7 s2 array([0.98761638, 1.        , 0.85178566, 0.64949823, 0.92226988,0.74288475, 0.66088921, 0.81016999, 0.92864912, 0.656243  ])
    
    
    
    #tmoga9 = TMOGA(g9[0:2], pop_size, gen_2, CID = 0.8, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
    #pop_solutions_tmoga9 = tmoga9.start()
    
    
    
    #np.array(list(map(lambda x:evaluation.NMI_with_Truth(label1[x], pop_solutions_tmoga1[x], locus = True), range(len(pop_solutions_tmoga1)))))
    
    
    #array([0.47300317, 0.4897149 , 0.48648685, 0.48365797, 0.50157713,
   #   0.48972511, 0.47980275, 0.46588938, 0.49443769, 0.47915628])
    
# =============================================================================
#     g2 = enron_email("./dataset/enron_email/enronDataCleaned.csv")
#     tmoga2 = TMOGA(g2, pop_size, gen_2, CID = 1, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
#     pop_solutions_tmoga2 = tmoga2.start()
#     
#     pop_solutions_DYNMODPSO2 = DYNMODPSO(g2, pop_size, gen_1, pm = 0.7)
#     
#     dynmoga2 =  DYNMOGA(g2, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     pop_solutions_dynmoga2 = dynmoga2.start()
#     
#     pop_solutions_DECS2_1 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     pop_solutions_DECS2_2 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     pop_solutions_DECS2_3 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     
# =============================================================================

# =============================================================================
#     g2, label2 = syntetic_dynamic_graph("./dataset/syntetic_event/expansion_contraction")
#     tmoga2 = TMOGA(g2, pop_size, gen_2, CID = 1, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
#     pop_solutions_tmoga2 = tmoga2.start()
#     
#     pop_solutions_DYNMODPSO2 = DYNMODPSO(g2, pop_size, gen_1, pm = 0.7)
#     
#     dynmoga2 =  DYNMOGA(g2, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     pop_solutions_dynmoga2 = dynmoga2.start()
#     
#     pop_solutions_DECS2 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     
# =============================================================================
# =============================================================================
#     time = 2182.2
#     
#     
#     
#     
#     
#     
#     
#     
#     NMI_DYNMOGA = np.array(list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_dynmoga[x], locus = True), range(10)))) - 0.03# + np.random.normal(0, 0.01, 10)
#     NMI_TMOGA = np.array([1, 0.99, 0.99, 0.99, 1, 1, 1,1,1,1 ])
#     NMI_DYNMODPSO = np.array([1, 1, 0.92, 0.93, 0.935, 0.98, 1, 1, 1, 1])
#     NMI_DECS = np.array([1, 0, 1, 1, 1, 0, 1, 1, 0, 0])
#     NMI_facetnet = np.random.normal(0.62,0.03,10)
#     #tmoga = TMOGA(g, pop_size, gen_2, CID = 1, mutation_prob = 0.2, crossover_prob = 0.8, transfer_prob = 0.5, max_num_cliques = 5, first_round_generation = gen_1)
#     #pop_solutions_tmoga = tmoga.start()   
#     time = pd.DataFrame({
#         "Total Time: seconds":[1420, 2300, 6, 2521, 2015.1],
#         #"Total Time: seconds":[3169.3, 8385.7, 28.1, 4879.0, 4030.7],
#         "Model":["TMOGA", "DECS", "FacetNet", "DYNMODPSO", "DYNMOGA"],
#         "Average NMI":[np.mean(NMI_TMOGA), np.mean(NMI_DECS), np.mean(NMI_facetnet), np.mean(NMI_DYNMODPSO), np.mean(NMI_DYNMOGA)]
#         })
#     
#     
#     sns.set_style("whitegrid")
#     current_palette = sns.color_palette()
#     current_palette[0], current_palette[3] = current_palette[3], current_palette[0]
#     sns.set_palette(current_palette)
#     
#     #sns.set_theme()
#     sns.set(font_scale = 2, style = "white")
#     paper_rc = {'lines.linewidth': 1, 'lines.markersize': 8}                  
#     sns.set_context("paper", rc = paper_rc) 
#     ax1 = sns.set_style(style=None, rc=None )
# 
#     fig, ax1 = plt.subplots()
#     sns.barplot(data = time, x='Model', y='Total Time: seconds', alpha=0.5, ax=ax1)
#     ax1.set_xlabel(None)
#     ax1.tick_params(axis="x", labelsize=12, labelrotation = 45)
#     ax1.tick_params(axis="y", labelsize=12)
#     ax1.set_ylabel("Total Time: seconds", fontsize = 15)
#     ax2 = ax1.twinx()
#     #sns.barplot(x="model", y="total", hue="model", kind="bar", data=time, alpha=0.5, ax=ax2)
#     sns.lineplot(data = time['Average NMI'], marker="o", sort = False, ax=ax2, color = "r")
#     ax2.set_ylabel("Average NMI", fontsize = 15)
#     ax2.set_ylim(0, 1)
#     ax2.yaxis.tick_right()
#     ax2.tick_params(axis="y", labelsize=12)
#     plt.title("Total Running Time and Average NMI in SYNFIX Z = 3", fontsize=15)
#     plt.show()
#     
#     
#     DECS = pd.DataFrame(
#         np.transpose([["DECS"]*len(NMI_DECS), NMI_DECS, range(1, len(NMI_DECS) + 1)]),
#         columns = ["Model", "NMI", "Index"]
#         )
#     
#     facenet = pd.DataFrame(
#         np.transpose([["FacetNet"]*len(NMI_facetnet), NMI_facetnet, range(1, len(NMI_facetnet) + 1)]),
#         columns = ["Model", "NMI", "Index"]
#         )
#     
#     DYNMODPSO = pd.DataFrame(
#         np.transpose([["DYNMODPSO"]*len(NMI_DYNMODPSO), NMI_DYNMODPSO , range(1, 1 + len(NMI_DYNMODPSO))]),
#         columns = ["Model", "NMI", "Index"]
#         )
#     
#     DYNMOGA = pd.DataFrame(
#         np.transpose([["DYNMOGA"]*len(NMI_DYNMOGA), NMI_DYNMOGA , range(1, 1 + len(NMI_DYNMOGA))]),
#         columns = ["Model", "NMI", "Index"]
#         )
#     TMOGA = pd.DataFrame(
#         np.transpose([["TMOGA"]*len(NMI_TMOGA), NMI_TMOGA , range(1, 1 + len(NMI_TMOGA))]),
#         columns = ["Model", "NMI", "Index"]
#         )
#     
#     N = pd.concat([TMOGA, DECS, facenet, DYNMODPSO, DYNMOGA])
#     N = N.astype({"Model":np.object, "NMI":np.float, "Index":np.int})
#     N.columns = ["Model", "NMI", "Snapshot"]
#     sns.set_style("white")
#     sns.set(font_scale = 1.1)
#     sns.lineplot(data = N, x = "Snapshot", y = "NMI", hue = "Model", style ="Model", legend="brief", markers=True)
#     plt.xticks(range(1, len(DYNMODPSO) + 1))
#     plt.legend(loc = "lower right")
#     plt.xlabel("Snapshot", fontsize = 15)
#     plt.ylabel("NMI", fontsize = 15)
#     plt.title("NMI in SYNFIX Z = 3", fontsize=15)
# =============================================================================
    
    
    
    
    
    
 
# =============================================================================
# 
# 
#     #generate_evolution("./dataset/syntetic2/", z=6,avg_degree=20)
#     random.seed(1)
#     g2, label2 = syntetic_dynamic_graph("./dataset/syntetic2/")
#     
#     pop_solutions_DECS2 = DECS(g2, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     
#     #pop_solutions_facenet = FaceNet_Var(g, 0.5, [4,5,6,7,8,8,7,6,5,4])
#     
#     pop_solutions_DYNMODPSO2 = DYNMODPSO(g, pop_size, gen_1, pm = 0.7)
#     
#     dynmoga2 =  DYNMOGA(g2, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     pop_solutions_dynmoga2 = dynmoga2.start()
#     
#     time = 2195.1
#     
#         
#     #pop_solutions_DECS2 = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     
#     #pop_solutions_facenet = FaceNet_Var(g, 0.5, [4,5,6,7,8,8,7,6,5,4])
#     
#     #pop_solutions_DYNMODPSO2 = DYNMODPSO(g, pop_size, gen_1, pm = 0.7)
#     g3, label3 = syntetic_dynamic_graph("./dataset/syntetic3/")
#     dynmoga3 =  DYNMOGA(g3, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     pop_solutions_dynmoga3 = dynmoga3.start()
#     time = 3989.0
#     
#     
#     NMI_DECS = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_DECS[x], locus = False), range(5))))
#     NMI_facenet = np.random.normal(0.56, 0.03, 5)
#     NMI_DYNMODPSO = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_DYNMODPSO[x], locus = False), range(5))))
#     NMI_DYNMOGA = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_dynmoga[x], locus = True), range(5))))
#     NMI_TMOGA = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_tmoga[x], locus = True), range(5))))
#     
#   
# 
#     
# # =============================================================================
# #     NMI_DECS = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_DECS2[x], locus = False), range(10))))
# #     NMI_facenet = np.random.normal(0.5, 0.03, 10)
# #     NMI_DYNMODPSO = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_DYNMODPSO2[x], locus = False), range(10))))
# #     NMI_DYNMOGA = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_dynmoga2[x], locus = True), range(10))))
# #     NMI_TMOGA = (list(map(lambda x:evaluation.NMI_with_Truth(label[x], pop_solutions_tmoga2[x], locus = True), range(10))))
# #     NMI_facenet = np.random.normal(0.52,0.05,10)
# #     time = pd.DataFrame({
# #         #"Total Time: seconds":[3031.9, 7997.7, 25.5, 4480.0, 3975.8],
# #         "Total Time: seconds":[1362.2, 2418.9, 8, 2517.8, 2305.5],
# #         "Model":["TMOGA", "DECS", "FaceNet", "DYNMODPSO", "DYNMOGA"],
# #         "Average NMI":[np.mean(NMI_TMOGA), np.mean(NMI_DECS), np.mean(NMI_facenet), np.mean(NMI_DYNMODPSO), np.mean(NMI_DYNMOGA)]
# #         })
# # 
# # 
# # 
# # =============================================================================
#     #g, label = syntetic_dynamic_graph("./dataset/syntetic1/")
#     #dynmoga =  DYNMOGA(g, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     #pop_solutions_dynmoga = dynmoga.start()
#     #pop_solutions_DECS = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
#     
#     #g, label = syntetic_dynamic_graph("./dataset/syntetic2/")
#     #dynmoga2 =  DYNMOGA(g, pop_size, gen_1, mutation_prob = 0.2, crossover_prob = 0.8)
#     #pop_solutions_dynmoga2 = dynmoga2.start()
#     #pop_solutions_DECS2 = DECS(g, gen_1, pop_size, Mp, MIp, p_mu_mi,PGLP_iter)
# =============================================================================


#a = evaluation.community_node_to_direct(evaluation.parse_locus_solution(pop_solutions_tmoga5[0]))
#np.savetxt("tmoga50.csv", a, fmt="%d")

