# Python3-algorithms-for-coding-interviews

[Overview](#overview)

[Graph Algorithms](#graph-algorithms)
	- [Breadth First Search (BFS)](#breadth-first-search-algorithm)
	- [Depth First Search (DFS)](#depth-first-search-algorithm)
	- [Topological Sorting](#topological-sorting-algorithm)
	- [Bellman-Ford](#bellman-ford-algorithm)
	- [Dijkstra's algorithm](#dijkstra-algorithm)
	- [Minimum Spanning trees (Prim's algorithm)](#minimum-spanning-trees)


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

## [Breadth-first search algorithm](../master/Graph%20Algorithms/bfs.py)

### Description
Breadth First Search (BFS) is a graph algorithm typically used for finding shortest path between a source and a target node. Alternative use cases involve finding the connected component of a given node in a graph, or finding all connected components of a graph. We present implementations of all the aforementioned use cases.

The algorithms can be run on both directed and undirected graphs. In the implementation file,
the class Graph constructs an undirected graph as adjacency list. To transform it into a
directed graph, simply modify the method add_edge inside the Graph class.

### Implementation

The implementation file contains the following functions:

1. bfs_path - takes as input a graph and a source, and returns a dictionary representing the connected component rooted at source;

2. bfs_target - takes as input a graph, a source node and a target node from the graph and returns a list representing the path from source to target, if this exists;

3. reconstruct_path - takes as input a dictionary representing a path from a source to a target, together with the target node, and returns a list representing the path from source to target;

4. bfs_all_graph - takes as input a graph and returns a set consisting of all connected components of the graph, each component represented as a frozenset.

### Complexity

The algorithm BFS used for finding the shortest path between a source and a target node runs in O(E) time, where E represents the number of edges in the connected component of the source node.

## [Depth-first search algorithm](../master/Graph%20Algorithms/dfs.py)

### Description
Depth-first search (DFS) is an algorithm typically used for traversing or searching a graph, most of the time a tree. Another important use case is as a subroutine in the topological sorting algorithm, which we discuss below.

Unlike BFS, DFS starts at the source node and explores as far as possible along each branch before backtracking (hence its name depth-first). Unlike BFS, given a source and a target that are part of the same connected component, DFS will not necessarily find the shortest path between the two nodes. Unlike BFS, DFS has both a recursive and an iterative implementation. 

Same as with BFS, DFS can be run on both directed and undirected graphs.


### Implementation
The implementation file contains the following functions:

1. recursive_dfs - recursive function that takes as input a graph, a source node, and a target node, and returns a boolean indicating whether there is a path from source to target in the given graph;

2. iterative_dfs - a non-recursive implementation (using stack) of DFS, that takes as input a graph, a source node and a target node, and returns a boolean indicating whether there is a path from source to target in the given graph.

### Complexity
The time complexity of the DFS algorithm is O(E), where E represents the number of edges in the graph.

## [Topological sorting algorithm](../master/Graph%20Algorithms/topological_sorting.py)

## Description
The topological sort algorithm takes a directed graph and returns an array of the nodes, where each node appears before all the nodes it points to.


## Implementation

Our implementation of Topological Sorting using a modification of the Depth First Search (DFS) algorithm.

In our implementation file, the class Graph constructs a directed graph as adjacency list. For our implementation of Topological Sorting, we assume that a directed edge between node_1 and node_2 means that node_1 has to come before node_2 in topological order. If one wants to use this implementation for the reverse scenario, the only adjustment to be done is to remove the line 'nodes_list.reverse()' at the end of the dfs_top_sort function.


The implementation file contains the following functions:
1. dfs_top_sort - function that takes as input a directed graph and returns a list containing a topological sorting of the vertices in graph, provided that the graph is acyclic;

2. dfs_visit - recursive function used inside the dfs_top_sort function. It takes as input a graph, a node in the graph to be processed, the list of colors of the nodes, and a boolean indicating whether we have found a cycle or not. As long as we have not encountered any cycles, the function performs a standard depth first search, and adds the nodes that were visited to a list. After all the nodes have been visited, the list of nodes will contain the graph nodes, in inverse topological order.

## Complexity

The time complexity of the algorithm is the same as the one of DFS, namely O(E), where E represents the number of edges in the graph.



## [Bellman-Ford algorithm](../master/Graph%20Algorithms/bellman_ford.py)

### Description
Bellman–Ford algorithm computes the shortest paths from a single source vertex to all of the other vertices in a weighted, directed graph. Unlike Dijkstra's algorithm, Bellman-Ford allows for negative weights, at the cost of higher time complexity.

### Implementation

Our implementation of the Bellman-Ford algorithm assumes that the graph is implemented as adjacency list stored as dictionary and that it contains a set of distances (costs) stored as dictionary where the keys are node tuples (source_node, target_node) and the values are represented by the distances between the nodes. See the implementation of the class Graph in the file.

The implementation file contains the following functions:

1. initialize - auxiliary function used by the Bellman-Ford algorithm;
..* the function takes as input a graph and a source, and initializes a dictionary of distances and a dictionary of node parents corresponding to the given graph and source as follows: the distance to source is set to 0, while the distance to every other node in the graph is set to +infinity. The parent of every node (stored in the dictionary called previous_on_path) is set to be None.

2. relax - auxiliary function used by the Bellman-Ford algorithm;
..* the function takes as input a graph, a node, a neighbor of the node in the graph, a dictionary of distances and a dictionary of parents. The function checks if we can improve the current shortest path to the input node by going through the input neighbor node. If this is the case, the function updates the dictionary of distances
and the one of parents.

3. bellman_ford - the main function of the file; 
..* the function takes as input a graph and a source and returns either the shortest path to all the other nodes in the graph, or it flags that it found a negative cycle in the graph.

### Complexity

The algorithm runs in O(VE) time, where V represents the number of vertices, and E represents the number of edges of the graph. For a detailed analysis of this and the proof of correctness, see for example Chapter 24.1 in [[1]](#1).


## [Dijkstra algorithm](../master/Graph%20Algorithms/dijkstra.py)

### Description
Dijkstra's algorithm is used for finding the shortest path from a single source vertex to all other vertices in a weighted graph, where each edge has a positive weight. The extra requirement that the edges have positive weights allows for a gain in the time complexity, over the Bellman-Ford algorithm (see below).

 
### Implementation
Our implementation of Dijkstra's algorithm assumes that the Graph is implemented as adjacency list stored as dictionary and that it contains a set of distances (costs) stored as dictionary, where the keys are node tuples (source_node, target_node) and the values are represented by the distances between the nodes. For more details, see the implementation of the class Graph in the file.

The implementation file contains in addition the following function:

1. dijkstra - returns a dictionary consisting of shortest paths in the form node: parent on path, with the source node having source: None. It is designed so that it can be easily modified to also return the distances or to explicitly reconstruct the path for one specific node.

### Complexity
Our implementation of Dijkstra's algorithm runs in O(V^2+E) = O(V^2). This is **NOT** the fastest possible implementation: there exists an implementation that uses Fibonacci heaps and runs in O(Vlog(V)+E)-see Chapter 24.3 in [[1]](#1).

## [Minimum Spanning Trees](../master/Graph%20Algorithms/prim_mst.py)

### Description
Prim's algorithm is used for finding a minimum spanning tree for a weighted undirected graph. More precisely, the algorithm finds a subset of the edges that forms a tree and that includes every vertex, and this subset satisfies the property that the total weight of all the edges in the tree is minimized.

### Implementation

Our implementation of Prim's algorithm assumes that the Graph is implemented as adjacency list, stored as dictionary.

We also implement our own min priority queue, mainly because of inability to find an efficient way of retrieving index of an element in a queue in the Python heapq module. This implementation is based on the heap implementation from Chapter 6 [[1]](#1)
and follows closely the ideas from this [link]: https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

The implementation file contains the following classes:
1. Graph - implementation of a graph using adjacency list;

2. PriorityQueue - implementation of a min priority queue.

The file also contains the following function:
1. prim - takes as input a graph and a source, and returns a minimum spanning tree rooted at the source.


### Complexity

The algorithm runs in O(E\*log(V)) time. This is **NOT** the fastest possible implementation: there exists an implementation that uses Fibonacci heaps and runs in O(E+Vlog(V))-see Chapter 23 in [[1]](#1).