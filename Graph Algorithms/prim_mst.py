""" A Python3 implementation of Prim\'s algorithm (Minimum spanning trees)

The algorithm runs in O(E*log(V)) time. This is NOT the fastest implementation:
there exists an implementation that uses Fibonacci heaps and runs in O(E+Vlog(V))
-see Chapter 23 in 3rd edition of Cormen - Introduction to Algorithms.
The below implementation is the Python3 code for the algorithm given in
Chapter 23.2 in 3rd edition of Cormen - Introduction to Algorithms.

The below implementation of Prim\'s algorithm assumes that the Graph is
implemented as adjacency list, stored as dictionary. See the below
implementation of the class Graph.

We also implement our own min priority queue, mainly because of inability to find
an efficient way of retrieving index of an element in a queue in the Python heapq module.
The below implementation is based on the heap implementation from Cormen Chapter 6
and follows closely the ideas from this link
https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

The file contains the following classes:
    Graph - implementation of a graph using adjacency list

    PriorityQueue - implementation of a min priority queue

    TestPrim - test cases for the implementation of Prim's algorithm

The file contains the following function
    * prim - takes as input a graph and a source, and returns a minimum spanning tree rooted at the source
"""

from collections import defaultdict
import unittest


class Graph:
    """
    An implementation of an undirected graph using adjacency list representation

    Attributes
    ----------

        nodes : set
            a set consisting of all the nodes in the graph

        edges : dict
            a dictionary storing all edges, in the format node : [list of neighboring nodes]

        weights: dict
            a dictionary storing the weights of each edge, in the format (node_1, node_2) : weight of edge

    Methods
    ----------

        add_node(node)
            adds node to graph

        add_edge (node_1, node_2, weight)
            adds node_1 and node_2 to the graph, together with the corresponding edges and weight
            adds node_2 to the neighbors of node_1
            adds node_1 to the neighbors of node_2



    """
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weights = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, source_node, target_node, weight):
        # first add the two nodes to the graph.nodes, in case we forgot to do this before
        self.add_node(source_node)
        self.add_node(target_node)

        # add the edges in the graph
        if source_node in self.edges:
            self.edges[source_node].append(target_node)
        else:
            self.edges[source_node] = [target_node]

        if target_node in self.edges:
            self.edges[target_node].append(source_node)
        else:
            self.edges[target_node] = [source_node]

        # add the weight (cost) between the two nodes
        self.weights[(source_node, target_node)] = weight
        self.weights[(target_node, source_node)] = weight


class PriorityQueue:
    """
    Own implementation of a min-priority queue

    Attributes:
        ----------
        queue: list
            list of tuples (node, distance)

        size : int
            size of the queue

        indices: dict
            dictionary storing the index of a node in queue in the form node : index

    Methods:
        ----------
        is_empty
            returns a boolean corresponding to the priority queue being empty or not

        in_queue(node)
            checks if the input node is in the priority queue

        add_node(node, distance)
            adds the list [node, distance] to the queue, updating the size and indices attributes

        swap_nodes(first_node, second_node)
            swaps the list containing first_node with the list containing second_node inside the queue

        heapify(index)
            maintains the min priority queue property of the queue starting from position equal to index

        extract_min
            returns and removes the node with the minimum distance from the queue, maintaining the min queue property

        decrease_key (node, new_distance)
            decreases the distance associated with node in the queue to the new_distance value
            it assumes that new_distance is strictly smaller than the original distance
    """

    def __init__(self):
        self.queue = []
        self.size = 0
        self.indices = {}

    def is_empty(self):
        return True if self.size == 0 else False

    def in_queue(self, node):
        if self.indices[node] < self.size:
            return True
        return False

    def add_node(self, node, distance):
        self.queue.append([node, distance])
        self.indices[node] = self.size
        self.size += 1

    def swap_nodes(self, u, v):
        self.queue[self.indices[u]], self.queue[self.indices[v]] = \
            self.queue[self.indices[v]], self.queue[self.indices[u]]
        self.indices[u], self.indices[v] = self.indices[v], self.indices[u]

    def heapify(self, idx):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
        if left < self.size and self.queue[left][1] < self.queue[smallest][1]:
            smallest = left
        if right < self. size and self.queue[right][1] < self.queue[smallest][1]:
            smallest = right

        if smallest != idx:
            self.swap_nodes(self.queue[smallest][0], self.queue[idx][0])
            self.heapify(smallest)

    def extract_min(self):
        if self.is_empty():
            return

        min_node = self.queue[0][0]
        [last_node, last_distance] = self.queue[self.size - 1]
        self.queue[0] = [last_node, last_distance]
        self.indices[last_node] = 0
        self.indices[min_node] = self.size - 1

        # Reduce heap size and heapify
        self.size -= 1
        self.heapify(0)

        return min_node

    def decrease_key(self, node, distance):

        # Get the index of v in  heap array
        idx = self.indices[node]

        # Get the node and update its dist value
        self.queue[idx][1] = distance

        # Travel up while the complete tree is not heapified.
        while idx > 0 and self.queue[idx][1] < self.queue[(idx - 1) // 2][1]:
            # Swap this node with its parent
            self.swap_nodes(self.queue[idx][0], self.queue[(idx - 1)//2][0])

            # move to parent index
            idx = (idx - 1) // 2


def prim(graph, source):
    """implementation of Prim's algorithm on a graph from a given source

    the function first creates the min priority queue and initializes the distances and parents
    for each node. These are necessary for initializing the minimum spanning tree that initially
    consists only of the source node and will be gradually grown during the algorithm"""

    # initialize the priority queue
    priority_queue = PriorityQueue()
    for node in graph.nodes:
        priority_queue.add_node(node, float('inf'))

    # change the distance to the source to 0
    source_index = priority_queue.indices[source]
    priority_queue.queue[source_index][1] = 0

    # change the index of the source to be 0. this avoids building a min-heap, as everything else is infinity
    priority_queue.swap_nodes(source, priority_queue.queue[0][0])

    # initialize the dictionary of parents
    previous_on_path = {node: None for node in graph.nodes}

    while priority_queue.size > 0:
        current_node = priority_queue.extract_min()
        for neighbor in graph.edges[current_node]:
            if priority_queue.in_queue(neighbor) and \
                    priority_queue.queue[priority_queue.indices[neighbor]][1] > graph.weights[(current_node, neighbor)]:
                previous_on_path[neighbor] = current_node
                priority_queue.decrease_key(neighbor, graph.weights[(current_node, neighbor)])
    return previous_on_path


class TestPrim(unittest.TestCase):
    """"Test case taken from Cormen, Chapter 23.2, Figure 23.5"""

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B', 4)
        self.graph.add_edge('A', 'H', 8)
        self.graph.add_edge('B', 'C', 8)
        self.graph.add_edge('B', 'H', 11)
        self.graph.add_edge('C', 'D', 7)
        self.graph.add_edge('C', 'F', 4)
        self.graph.add_edge('C', 'I', 2)
        self.graph.add_edge('D', 'E', 9)
        self.graph.add_edge('D', 'F', 14)
        self.graph.add_edge('E', 'F', 10)
        self.graph.add_edge('F', 'G', 2)
        self.graph.add_edge('G', 'I', 6)
        self.graph.add_edge('G', 'H', 1)
        self.graph.add_edge('H', 'I', 7)

    def test_prim_1(self):
        actual = prim(self.graph, 'B')
        expected = {'H': 'G', 'C': 'B', 'A': 'B', 'D': 'C', 'I': 'C', 'G': 'F', 'F': 'C', 'B': None, 'E': 'D'}
        self.assertEqual(actual, expected)

    def test_prim_2(self):
        # a test where the algorithm had a choice and there are two possible solutions
        actual = prim(self.graph, 'A')

        expected_1 = {'A': None, 'B': 'A', 'C': 'B', 'D': 'C', 'E': 'D', 'F': 'C', 'I': 'C', 'G': 'F', 'H': 'G'}
        expected_2 = {'F': 'G', 'C': 'F', 'I': 'C', 'D': 'C', 'G': 'H', 'B': 'A', 'E': 'D', 'H': 'A', 'A': None}
        self.assertTrue(actual == expected_1 or actual == expected_2)


unittest.main(verbosity=2)