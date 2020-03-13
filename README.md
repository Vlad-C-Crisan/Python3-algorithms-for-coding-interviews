# Python3-algorithms-for-coding-interviews

[Overview](#-overview)

[Graph Algorithms](#-graph-algorithms)


# Overview

This repository contains the Python3 implementation of the most commonly used graph and sorting algorithms in coding interviews.

The algorithms are grouped into two main categories: Graph Algorithms and Sorting and order statistics, respectively.

Each file contains a separate algorithm, as indicated by the file's name. Detailed description of the implementation, as well as test cases are provided in each file.

All files represent own implementations of the algorithms and I take full responsibility for any mistakes. The main reference I used is the book 
<a id="1">[1]</a> 
Cormen, T. H., Leiserson, C. E., Rivest, R. L., Stein, C. (2009).
Introduction to Algorithms, 3rd edition.
The MIT Press.

# [Graph Algorithms](../master/Graph%20Algorithms)

## [Bellman-Ford algorithm](../master/Graph%20Algorithms/bellman_ford.py)

Bellman–Ford algorithm computes the shortest paths from a single source vertex to all of the other vertices in a weighted, directed graph. Unlike Dijkstra's algorithm, Bellman-Ford allows for negative weights, at the cost of higher time complexity.

The algorithm runs in O(VE) time. For a detailed analysis of this and the proof of correctness, see for example Chapter 24.1 in [1](#1).

Our implementation of the Bellman-Ford algorithm assumes that the graph is implemented as adjacency list stored as dictionary and that it contains a set of distances (costs) stored as dictionary where the keys are node tuples (source_node, target_node) and the values are represented by the distances between the nodes. See the below implementation of the class Graph.






