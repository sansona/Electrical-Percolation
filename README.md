# Electrical-Percolation

Goal: utilizes quick union algorithms to model electrical percolation in conductors and superconductors

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
