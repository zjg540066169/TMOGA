# TMOGA

## Overview
TMOGA(feature Transfer based Multi-Objective Genetic algorithm) is a multi-objective genetic algorithm to solve community detection problem on dynamic networks. The whole algorithm is written by Python, which takes a list of Graph class from Networkx as input and a list of final locus-based solutions as output.

Inspired by transfer learning mechanism, the algorithm uses feature transfer mechanism to improve the results. It can keep the useful information from last snapshot network, to help the optimization of current network community structures. This unique mechanism can significantly improve the stability and accuracy of algorithms. Although additional time is needed to run feature transfer, the additional running time can be ignored compared with genetic algorithm part in practice. 

For more details on the algorithm and its applications, please consult the following paper:
"Transfer Learning Based Multi-Objective Evolutionary Algorithm for Community Detection of Dynamic Complex Networks" (arxiv: https://arxiv.org/abs/2109.15136)

## Requirement
* Python >= 3.7
* networkx >= 2.5
* argparse >= 1.1
* python-louvain >= 0.15
* joblib >= 0.17.0
* tqdm >= 4.50.2
* numpy >= 1.19.2
* matplotlib >= 3.3.2
* sklearn >= 0.23.2
* pandas >= 1.1.3

