# Electrical-Percolation

Goal: utilizes quick union algorithms to model electrical percolation in conductors

Quick union is an union-find algorithm that allows one to traverse a series of connected nodes to determine the connectivity between nodes. The data structure involves organizing the overall data into a tree with nodes and roots, where nodes are directly connected to other nodes and the root is the uppermost level.

Quick union algorithms have two main functions:
  1. Union: connects two given nodes
  2. Find: determines if two given nodes are connected via. some pathway through the tree.
  
The goal of union-find algorithms is to efficiently perform these two actions - most commonly the find function. In the basic quick union algorithm, the find function determines connectivity by comparing the two roots of the given nodes. If two nodes have the same root, they are connected. This algorithm is computationally inefficient as both union and find functions are expensive and the resulting tree structure makes traversal difficult. This is improved by adding weight and path compression functionality, which lead to a more efficient algorithm:

1. Quick union:
  - compares roots to determine connectivity
  - both union and find are inefficient
  - tendency for trees to grow tall, leading to inefficient traversal
  - O(n^2)
  
2. Weighted quick union:
  - establishes weights of different branches and attaches smaller branches to larger ones, reducing tree height
  - O(lgN)
  
3. Weighted quick union with path compression:
  - reattaches branches to root upon traversal, flattening out tree structure furthermore
  - O(lg* N) in theory, O(1) in practice

Electric percolation is modelled by starting off with a lattice of m insulating atoms and randomly choosing atoms to become conductive. After each switch, the conductivity of the lattice is tested and the process is repeated until the lattice is conductive. The condition for conductivity requires that there be a conductive pathway between a fictitious top and bottom atom that are connected to the top and bottom planes of the lattice respectively. Thus, by applying a quick union algorithm to determine the connectivity of the two fictitious atoms, one can algorithmically and efficiently determine the conductivity of the lattice as a whole.

In this project, a 2D lattice of 10,000 atoms was utilized to determine the percolation threshhold - the percentage of atoms that have to be conductive, on average, to lead to a conductive lattice. A simple monte carlo simulation is implemented to probe the simulation n times in order to calculate the average expected threshhold value and create a distribution of values, which can be seen below for n = 10, 100, 1000, and 10000 samples:

![montecarlo10](https://user-images.githubusercontent.com/17757035/35840102-efede612-0aa8-11e8-9d48-ace0a75a36c6.png)
```
The average threshhold value for 10000 atoms over 10 samples is 44.5, with a confidence interval of [38.8, 50.2]
```

![montecarlo100](https://user-images.githubusercontent.com/17757035/35840105-f14a3a88-0aa8-11e8-9cd8-117c79f76c31.png)
```
The average threshhold value for 10000 atoms over 100 samples is 41.4, with a confidence interval of [39.3, 43.4]
```

![montecarlo1000](https://user-images.githubusercontent.com/17757035/35840106-f1735666-0aa8-11e8-814d-be749d072023.png)
```
The average threshhold value for 10000 atoms over 1000 samples is 40.2, with a confidence interval of [39.5, 40.9]
```

![montecarlo10000](https://user-images.githubusercontent.com/17757035/35840108-f1e135a0-0aa8-11e8-91ff-59b696dd0874.png)
```
The average threshhold value for 10000 atoms over 10000 samples is 40.2, with a confidence interval of [40.0, 40.4]
```

The results seem to indicate that, for a (very) small 2D lattice, roughly 40% of atoms need to be conductive for a conductive pathway to be present. This simulation doesn't account for directional bonds or long-range order, so the results are not likely to be groundbreaking (or really useful) in any way, but proves to demonstrate a simple modeling of conductivity utilizing a search algorithm.
