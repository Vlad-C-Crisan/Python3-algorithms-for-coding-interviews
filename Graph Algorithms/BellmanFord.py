""" Python3 implementation of Bellman-Ford algorithm (single source shortest paths to all nodes).

The algorithm runs in O(VE) time. For a detailed analysis of this and the proof of correctness,
see for example Chapter 24.1 in 3rd edition of Cormen - Introduction to Algorithms.

The below implementation of the Bellman-Ford algorithm assumes that the Graph is
implemented as adjacency list stored as dictionary and that it contains a set of 
distances (costs) stored as dictionary where the keys are node tuples (source_node, target_node)
and the values are represented by the distances between the nodes. See the below 
implementation of the class Graph.

The file contains the following functions
    * initialize - auxiliary function used by the Bellman-Ford algorithm;
    it takes as input a graph and a source, and initializes a dictionary of distances and a
    dictionary of node parents corresponding to the given graph and source as follows: the distance to source
    is set to 0, while the distance to every other node in the graph is set to +infinity. The parent of every
    node (stored in the dictionary called previous_on_path) is set to be None.

    * relax - auxiliary function used by the Bellman-Ford algorithm;
    it takes as input a graph, a node, a neighbor of the node in the graph, a dictionary of distances and
    a dictionary of parents. The function checks if we can improve the current shortest path to the input node
    by going through the input neighbor node. If this is the case, the function updates the dictionary of distances
    and the one of parents.

    * bellman_ford - the main function of the file, that takes as input a graph and a source and returns either
    the shortest path to all the other nodes in the graph, or it flags that it found a negative cycle in the graph
"""


from collections import defaultdict
import unittest


class Graph:
    """
        An implementation of a directed graph using adjacency list representation

        Attributes
        ----------

            nodes : set
                a set consisting of all the nodes in the graph

            edges : dict
                a dictionary storing all edges, in the format node : [list of neighboring nodes]

            distances: dict
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
        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, source_node, target_node, distance):
        # first add the two nodes to the graph.nodes, in case we forgot to do this before
        self.add_node(source_node)
        self.add_node(target_node)

        # add the edge in the oriented graph
        if source_node in self.edges:
            self.edges[source_node].append(target_node)
        else:
            self.edges[source_node] = [target_node]

        # add the distance between the two nodes
        self.distances[(source_node, target_node)] = distance


def initialize(graph, source):
    distance = {node: float('inf') for node in graph.nodes}
    previous_on_path = {node: None for node in graph.nodes}
    distance[source] = 0
    return distance, previous_on_path


def relax(graph, node, neighbor, distance, previous_on_path):
    # check if distance between node and neighbor is smaller than what we currently have
    if distance[neighbor] > distance[node] + graph.distances[(node, neighbor)]:
        distance[neighbor] = distance[node] + graph.distances[(node, neighbor)]
        previous_on_path[neighbor] = node


def bellman_ford(graph, source):
    distance, previous_on_path = initialize(graph, source)
    for j in range(len(graph.nodes)):
        for node in graph.nodes:
            for neighbor in graph.edges[node]:
                relax(graph, node, neighbor, distance, previous_on_path)

    # check for negative cycles
    for node in graph.nodes:
        for neighbor in graph.edges[node]:
            assert distance[neighbor] <= distance[node] + graph.distances[(node, neighbor)], "Negative cycle!"

    return distance, previous_on_path


class TestBellmanFord(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B', -1)
        self.graph.add_edge('B', 'C', 8)
        self.graph.add_edge('A', 'C', 9)
        self.graph.add_edge('B', 'D', 7)
        self.graph.add_edge('C', 'D', -4)

    def test_bellman_ford_1(self):
        actual = bellman_ford(self.graph, 'A')
        expected = ({'A': 0, 'B': -1, 'C': 7, 'D': 3}, {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'})
        self.assertEqual(actual, expected)

    def test_bellman_ford_2(self):
        actual = bellman_ford(self.graph, 'B')
        expected = ({'A': float('inf'), 'B': 0, 'C': 8, 'D': 4}, {'A': None, 'B': None, 'C': 'B', 'D': 'C'})
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
