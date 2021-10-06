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
      <th  colspan="3">dataset</th>
      <th width="80%" >source</th>
   </tr>
   <tr>
      <td style="text-align:center" width="12%" rowspan="6" colspan="1">synthetic datasets</td>
      <td style="text-align:center" width="13%" colspan="2">SYN-FIX</td>
      <td rowspan="2" >Kim, M. S., & Han, J. (2009). A particle-and-density based evolutionary clustering method for dynamic networks. Proceedings of the VLDB Endowment, 2(1), 622-633.</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="2">SYN-VAR</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="1" rowspan="4">SYN-EVENT</td>
      <td style="text-align:center" width="13%">Birth and Death</td>
      <td rowspan="4">Greene, D., Doyle, D., & Cunningham, P. (2010, August). Tracking the evolution of communities in dynamic social networks. In 2010 international conference on advances in social networks analysis and mining (pp. 176-183). IEEE.</td>
   
   <tr>
     <td style="text-align:center" colspan="1">Expansion and Contraction</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="1">Intermittent Communities</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="1">Merge and Split</td>
   </tr>
</tr>
   <tr>
      <td style="text-align:center" rowspan="2" >Real-world datasets</td>
      <td style="text-align:center" >Cellphone Calls</td>
      <td>http://visualdata.wustl.edu/varepository</td>
   </tr>
</table>

