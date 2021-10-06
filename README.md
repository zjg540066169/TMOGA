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

## Datasets
Some classic datasets of dynamic community detection problems are included in this project. The sources are listed here:

<table>
   <tr>
      <th  colspan="2">Dataset</th>
      <th width="80%" >Source</th>
   </tr>
   <tr>
      <td style="text-align:center" width="12%" rowspan="3" >Synthetic datasets</td>
      <td style="text-align:center" width="13%" >SYN-FIX</td>
      <td rowspan="2" >M.-S. Kim and J. Han, “A particle-and-density based evolutionary clustering method for dynamic networks,” Proc. VLDB Endow., vol. 2, no. 1, pp. 622–633, 2009.</td>
   </tr>
   <tr>
      <td style="text-align:center" >SYN-VAR</td>
   </tr>
   <tr>
      <td style="text-align:center">SYN-EVENT</td>
      <td>D. Greene, D. Doyle, and P. Cunningham, “Tracking the evolution of communities in dynamic social networks,” in Proc. Int. Conf. Adv. Soc. Netw. Anal. Min. (ASONAM), pp. 176–183, 2010.</td>
   </tr>
   <tr>
      <td style="text-align:center" rowspan="2" >Real-world datasets</td>
      <td style="text-align:center" >Cellphone Calls</td>
      <td>http://www.cs.umd.edu/hcil/VASTchallenge08/</td>
   </tr>
   <tr>
      <td style="text-align:center" >Enron Mail</td>
      <td>http://www.cs.cmu.edu/~enron/</td>
   </tr>
</table>

