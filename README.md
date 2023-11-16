# TMOGA for Dynamic Community Detection Problem

TMOGA(feature Transfer based Multi-Objective Genetic algorithm) is a multi-objective genetic algorithm to solve community detection problem on dynamic networks. The whole algorithm is written by Python, which takes a list of Graph class from Networkx as input and a list of final community partitions as output.

Inspired by transfer learning mechanism, the algorithm uses feature transfer mechanism to improve the results. It can keep the useful information from last snapshot network, to help the optimization of current network community structures. This unique mechanism can significantly improve the stability and accuracy of algorithms. Although additional time is needed to run feature transfer, the additional running time can be ignored compared with genetic algorithm part in practice. 

For more details on the algorithm and its applications, please consult the following paper:
"Transfer Learning Based Multi-Objective Genetic Algorithm for Dynamic Community Detection" (arxiv: https://arxiv.org/abs/2109.15136)

## Installation

You can install this package from pip with

`pip install tmoga=0.14.0`


## Requirement
* Python >= 3.9
* networkx >= 3.1
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
      <th width="40%" >source</th>
   </tr>
   <tr>
      <td style="text-align:center" width="25%" rowspan="8" colspan="1">Synthetic datasets</td>
      <td style="text-align:center" width="13%" colspan="1" rowspan="2">SYN-FIX</td>
      <td style="text-align:center" width="30%" colspan="1">Z = 3</td>
      <td rowspan="4" >Kim, M. S., & Han, J. (2009). A particle-and-density based evolutionary clustering method for dynamic networks. Proceedings of the VLDB Endowment, 2(1), 622-633.</td>
   </tr>
   <tr>
    <td style="text-align:center" width="30%" colspan="1">Z = 6</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="1" rowspan="2">SYN-VAR</td>
      <td style="text-align:center" width="30%" colspan="1">Z = 3</td>
   </tr>
   <tr>
    <td style="text-align:center" width="30%" colspan="1">Z = 6</td>
   </tr>
   <tr>
      <td style="text-align:center" colspan="1" rowspan="4">SYN-EVENT</td>
      <td style="text-align:center" width="30%">Birth and Death</td>
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
      <td style="text-align:center" rowspan="1" >Real-world dataset</td>
      <td style="text-align:center" colspan="2" >Mobile Phone Communication Network</td>
      <td>http://visualdata.wustl.edu/varepository</td>
   </tr>
</table>

It is worthwhile to note, the generating tool for SYN-EVENT datasets can be found at http://mlg.ucd.ie/dynamic/. The parameters for each dataset can found at such path: ./dataset/SYNEVENT/*/generation_parameters.txt.

## Usage

### Command Line
We list some datasets in common research above, and we can run command at the root directory to test TMOGA:

`python3 ./main.py output -d dataset -g generation -p population  --CID cid  --Md md --Tp tp --Cp cp --Mp mp`

* output is directory that community files should be saved. Required.
* -d specifies running dataset. Value can be one of (*synfix3, synfix6, synvar3, synvar6, birth_death, expansion_contraction, intermittent, merge_split, mobile_phone_call*). Default value is *synfix3*.
* -g specifies number of generations. Value should be positive integer. Default value is 100.
* -p specifies population size. Value should be positive integer. Default value is 200.
* --CID specifies the CID threshold. Value should be in [0, 1]. Default value is 0.8.
* --Md specifies the max depth of search tree. Value should be small positive integer. Default value is 5.
* --Tp specifies transfer probability. Value should be in [0, 1]. Default value is 0.5.
* --Cp specifies crossover probability. Value should be in [0, 1]. Default value is 0.8.
* --Mp specifies mutation probability. Value should be in [0, 1]. Default value is 0.2.

An example can be:

`python3 ./main.py ./ -d synfix6 -g 20 -p 20  --CID 0.5  --Md 5 --Tp 0.5 --Cp 0.5 --Mp 0.2`

### Python Library
After installation from pip, we can import TMOGA algorithm and some evaluation functions in Python shell

`from tmoga import TMOGA, evaluation`

`TMOGA` is the main class for TMOGA algorithm, its parameters are as follows:

* graph_list(required):  the input data, which is a list of Graph class in Networkx.
* pop_size(default 150): the population size.
* max_gen(default 50):   the number of generations in NSGA-II.
* CID(default 0.5):      the CID threshold. More details are included in paper.
* transfer_prob(default 0.9): the transfer probability of features obtained at last snapshot.
* mutation_prob(default 0.9): the mutation probability of NSGA-II.
* crossover_prob(default 0.9): the uniform crossover probability of NSGA-II.
* max_num_cliques(default 5): the max depth of search tree. More details are included in paper.
* first_round_generation(default None): the number of generations specified for the first network snapshot. Since TMOGA applies the ordinary NSGA-II framework without feature transfer mechanism at the first snapshot, we can specify more generations for the first network.
* sde(default False): whether to use Shift-based Density Estimation Method to calculate crowding distance in NSGA-II (introduced in M. Li, S. Yang, X. Liu, Shift-based density estimation for pareto-based algorithms in manyobjective optimization, IEEE Transactions on Evolutionary Computation 18 (3) (2013) 348–365.).

For example, if we already have dynamic networks list, we can directly run code like: 

```
dynamic_network = [some Networkx-Graph objects]
tmoga_model = TMOGA(dynamic_network)
solutions, solutions_population = tmoga_model.start()
```

where `solutions` is a list of best locus-based solutions, `solutions_population` is a list of all locus-based solutions.

By using evaluation class, we can simply convert locus-based solutions to normal solutions:

```
 for i in range(len(solutions)):
     communities = evaluation.parse_locus_solution(solutions[i])
     print(communities)
```

At last, we get the final results for community detection in dynamic network.



### Visualization
This package provides some visualization functions for dynamic network in /tmoga/utils/visualization.py. 

To visualize the locus-encoding solutions obtained by TMOGA, we can run codes like:
```
 from tmoga.utils.visualization import visualization
 for i in range(len(solutions)):
     visualization.visualize_locus_solution(dynamic_network[i], solutions[i], node_label = False)
```

To visualize the direct-encoding solutions obtained by other algorithms, we can run codes like:
```
 from tmoga.utils.visualization import visualization
 from tmoga.utils.evaluation import evaluation
 
 # convert locus-encoding solution to direct-enncoding solution by using 'evaluation' class
 direct_0 = evaluation.locus_to_direct(solutions[0])
 visualization.visualize_direct_solution(dynamic_network[0], direct_0, node_label = True)
```

To visualize the cliques obtained for the first graph, we can run codes like:
``` 
 from tmoga.utils.visualization import visualization
 cliques = tmoga_model.get_cliques()
 visualization.visualize_cliques(dynamic_network[0], cliques[0])
```

To visualize the initial solutions obtained by feature transfer, we can run codes like:
``` 
 from tmoga.utils.visualization import visualization
 init_pop = tmoga_model.get_initial_populations()
 for i in range(len(init_pop)):
     visualization.visualize_locus_solution(dynamic_network[i], init_pop[i][0], node_label = False)
```



## Disclaimer

If you find there is any bug, please contact me: jungang.zou@gmail.com.
