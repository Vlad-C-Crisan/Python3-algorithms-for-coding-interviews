# Python3-algorithms-for-coding-interviews

[Overview](#overview)

[Graph Algorithms](#graph-algorithms)

1. [Breadth First Search (BFS)](#breadth-first-search-algorithm)

2. [Depth First Search (DFS)](#depth-first-search-algorithm)

3. [Topological Sorting](#topological-sorting-algorithm)

4. [Bellman-Ford](#bellman-ford-algorithm)

5. [Dijkstra's algorithm](#dijkstra-algorithm)

6. [Minimum Spanning trees (Prim's algorithm)](#minimum-spanning-trees)

[Sorting algorithms and order statistics](#sorting-algorithms-and-order-statistics)

1. [Merge Sort](#merge-sort)

2. [Quick Sort](#quicksort)

3. [Heap Sort](#heap-sort)

4. [Counting Sort](#counting-sort)

5. [Linear Select](#linear-select)

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
and follows closely the ideas from this link: https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

The implementation file contains the following classes:
1. Graph - implementation of a graph using adjacency list;

2. PriorityQueue - implementation of a min priority queue.

The file also contains the following function:
1. prim - takes as input a graph and a source, and returns a minimum spanning tree rooted at the source.


### Complexity

The algorithm runs in O(E\*log(V)) time. This is **NOT** the fastest possible implementation: there exists an implementation that uses Fibonacci heaps and runs in O(E+Vlog(V))-see Chapter 23 in [[1]](#1).


# Sorting algorithms and order statistics

## [Merge-sort](../master/Sorting%20algorithms%20and%20order%20statistics/merge_sort.py)

### Description
Merge-sort is a general purpose, comparison-based sorting algorithm. It uses the divide and conquer paradigm for sorting: given an array of comparable elements (e.g. numbers, strings, dates), with the array length being at least 2, the algorithm divides the array in two halves, sorts each half and then merges the two sorted halves back into a sorted array (hence the name merge sort). Its power can be seen for example in the fact that the sorting algorithm used by Python, called Timsort, is a hybrid sorting algorithm that uses a combination of merge sort and insertion sort. For more details regarding merge sort and the divide and conquer paradigm, see, for example, Chapter 4 in [[1]](#1).

### Implementation

Our implementation of merge sort uses a recursive approach, following the divide and conquer paradigm desribed above. This means that in addition to the given time complexity, there is a O(N) space complexity on the call stack (for a discussion of this see, for example, https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity).

The implementation file contains the following functions:
1. merge_sort - recursive function that takes as input an array, a start index and an end index, and sorts the input array between the two given indices (inclusive) in ascending order. The function
is designed to have default arguments, so that it can also be called in the natural way, by giving it only the array as input, when we want to sort the entire array.

2. merge - auxiliary function used by merge_sort; it takes as input an array and three indices (start, middle, end) and assumes that the input array is sorted in ascending order between start and middle (inclusive) and between middle and end (inclusive), respectively. The function returns an array containing all elements between start and end of the input array, sorted in ascending order.

### Complexity

The running time of the function for an array of size n is O(n\*log(n)), which, without any extra assumptions regarding the elements of the array, is the best possible runtime (for a proof of this, see, for example, [[1]](#1)).

## [Quicksort](../master/Sorting%20algorithms%20and%20order%20statistics/quick_sort_randomized.py)

### Description
Quicksort is, like merge-sort, a general purpose, divide and conquer, sorting algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

As the algorithm relies on a choice of a pivot, and this is chosen randomly, we cannot talk about a general runtime of the algorithm, but rather of an expected runtime. When implemented well, this expected runtime is typically faster than other general purpose sorting algorithms, like merge sort or heap sort. Compared to merge sort, for example, the downside of the quick sort algorithm is that its worst running time is O(n^2) for an array of size n.

Quick sort procedure is an in place procedure, and the only additional space complexity comes from the recursive calls, which can be made to be O(log(n)) in the worst case, using Sedgewick's trick to limit the recursive calls. For more details, see, for example, 
https://en.wikipedia.org/wiki/Quicksort#Space_complexity

### Implementation
The file contains the following functions
1. quick_sort - recursive function that takes as input an array, a start index and an end index, and sorts the input array between the two given indices (inclusive) in ascending order. The function is designed to have default arguments, so that it can also be called in the natural way by simply giving it only the array as input, when we want to sort the entire array.

2. randomized_partition - auxiliary function used by quick_sort; it takes as input an array and two indices (start_index, and end_index); it selects a random element (pivot) of the array that lies between the two input indices and returns the array partitioned around the pivot, with all elements that are <= pivot lying to the left of the pivot and all elements that are  > pivot lying to the right of the pivot.

### Complexity
The expected running time of the function for an array of size n is O(n\*log(n)). For a proof of this fact, see for
example Chapter 7 in [[1]](#1).

## [Heap-sort](../master/Sorting%20algorithms%20and%20order%20statistics/heap_sort.py)

### Description
Like merge-sort and quicksort, heap-sort is a general purpose, comparison-based, sorting algorithm. The algorithm is based on binary heap data structure (hence its name heap-sort). The algorithm can be implemented in place and without recursion, making it asymptotically optimal regarding both space and time complexities. The reason why in practice one rarely uses it compared to merge-sort or quicksort is that the constant implied in the time complexity O(n\*log(n)) of its runtime is typically larger than the one involved in merge sort or quick sort, making it slower than its competitors. For a more detailed discussion about heap sort and the binary heap data structure, see for example Chapter 6 in [[1]](#1).

### Implementation


The implementation file contains the following functions:

1. heap_sort - function that takes as input an array and sorts its elements in ascending order;

2. max_heapify - auxiliary function used by heap_sort. It takes as input an array, a start_index and a heap_size. The function assumes that the input array satisfies the max heap property starting from both left(start_index) and right(start_index), but that start_index might be smaller than its children, thus violating the max heap property. For more details, see Chapter 6.2 in [[1]](#1).

While our implementation of the auxiliary function max_heapify is recursive, this can be easily turned into an iterative procedure, making the heap_sort procedure have O(1) space complexity.

### Complexity
The running time of the function for an array of size n is O(n\*log(n)).


## [Counting sort](../master/Sorting%20algorithms%20and%20order%20statistics/counting_sort.py)

### Description
Counting sort is a sorting algorithm typically used when we know that the elements of the input array are integers within a fixed range of values. Because it makes this extra assumption regarding the nature of the numbers the input array contains, its running time is faster than the one of the fastest general purpose sorting algorithms presented above. An important detail about the algorithm is that it is stable, i.e., equal elements appear in the output in the same order the appear in the input. This is essential for other algorithms that use counting sort as a subroutine, for example radix sort. For more details, see Chapter 8.2 in [[1]](#1).

### Implementation
The count_sort function provided in the implementation file takes as input an array and an integer k, and assumes that all elements in the input array are integers from the set {0,1, ..., k}. The function outputs an array consisting of the elements of the input array, sorted in ascending order. 


### Complexity
The time complexity and space complexity for the counting sort algorithm are both O(n+k).

## [Linear select](../master/Sorting%20algorithms%20and%20order%20statistics/linear_select.py)

### Description
The Select algorithm determines the kth smallest element of an input array of n >= k (distinct) elements in O(n) time. Notice that this is much faster than using a general purpose sorting algorithm and then looping to find the kth largest element (which would take O(n\*log(n)) time). To achieve this performance, the algorithm uses a clever approach for finding a suitable pivot for the array that serves as a candidate for the kth smallest element, and then proceeds in a similar fashion to quick sort. For the concrete steps involved in the Select algorithm, see, for example, Chapter 9.3 in [[1]](#1).

### Implementation
The implementation file contains the following functions:
1. find_kth_smallest - recursive function that takes as input an array, the value of k, a start index and an end index; the function returns the kth smallest element from the elements of the input array lying between the input indices. The function is designed to have default arguments, so that it can also be called in the natural way by simply giving it as input the array and the value of k. See the implementation and the test cases for more
details.

2. find_median - auxiliary function used find_kth_smallest that takes as input an array and returns the (upper) median in a given array. Within the function find_kth_smallest, this auxiliary function is called only
on arrays consisting of at most 5 elements, and, therefore, its contribution to the total runtime is constant.

3. partition -  auxiliary function used find_kth_smallest that takes as input an array, a pivot value, start and end indices, and partitions the elements of the array that lie between the input indices around the pivot value, so that all values less than the pivot value come to the left, and all greater values come to the right of the pivot value.

### Complexity
The runtime complexity of the algorithm is O(n), where n is the length of the input array.