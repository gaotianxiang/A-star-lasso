# A * Lasso

Python implementation of paper [A* Lasso for Learning a Sparse 
Bayesian Network Structure for Continuous Variables](https://papers.nips.cc/paper/5174-a-lasso-for-learning-a-sparse-bayesian-network-structure-for-continuous-variables)

### Generating simulated data 

```
python make_data.py
```
This script will generate sample data.  You can adjust the number of datasets 
you want to simulate as well as the strength of your edges (beta values). 
Sample benchmark networks are included in the `networks/` folder.  You can also specify 
your own networks by editing these files. 

### Running DP Lasso 

All the code for running DP Lasso is in the `dp_lasso/` folder. There is a demo 
called `run_dp_lasso.py` that you should run. DP Lasso generates the optimal 
solution.  However, it requires exponential time.  

```
python run_dp_lasso.py
```

### Running A* Lasso 

All the code for running A* Lasso is in the `a_star_lasso/` folder. There is a demo 
called `run_astar_lasso.py` that you should run.  In the demo, you have the option to run: 

-  A* Lasso - using `wrap_a_star_lasso.py `
This runs the optimal A* Lasso.  
``` 
python run_astar_lasso.py
```

-  A* Lasso with Pruning - using wrapAstarLassoPrune.m  
This uses our heuristic strategy to prune the queue so that the solution 
is attained much faster without significant compromise in quality. You 
should use this if the networks are larger than 20 nodes. 