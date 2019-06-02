"""Python3 implementations of the recursive and iterative versions of the Depth First Search (DFS) algorithm

The algorithms can be run on both directed and undirected graphs. In this file,
the class Graph constructs an undirected graph as adjacency list. To transform it into a
directed graph, simply modify the method add_edge inside the Graph class.

The file contains the following classes:
    Graph - implementation of a graph using adjacency list

    TestDFS - test cases for the two implementations of the DFS algorithm

The file contains the following functions
    * recursive_dfs - recursive function that takes as input a graph, a source node, and
        a target node, and returns a boolean indicating whether there is a path from source
        to target in the given graph

    * iterative_dfs - a non-recursive implementation (using stack) of DFS, that takes as input a graph,
        a source node and a target node, and returns a boolean indicating whether there is a path from
        source to target in the given graph"""

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


    Methods
    ----------

        add_node(node)
            adds node to graph

        add_edge (node_1, node_2)
            adds node_1 and node_2 to the graph
            adds the edge between node_1 and node_2
            adds node_2 to the neighbors of node_1
            adds node_1 to the neighbors of node_2



    """
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node_1, node_2):
        # first add the two nodes to the graph.nodes, in case we forgot to do this before
        self.add_node(node_1)
        self.add_node(node_2)

        # add the edges in the graph
        if node_1 in self.edges:
            self.edges[node_1].append(node_2)
        else:
            self.edges[node_1] = [node_2]

        if node_2 in self.edges:
            self.edges[node_2].append(node_1)
        else:
            self.edges[node_2] = [node_1]


def recursive_dfs(graph, source, target, visited_nodes=set()):
    if source not in graph.nodes:
        raise ValueError('source node is not in the graph')
    if source == target:  # the base case
        return True
    visited_nodes.add(source)

    for neighbor in graph.edges[source]:
        if neighbor not in visited_nodes:
            if recursive_dfs(graph, neighbor, target, visited_nodes):
                return True
    return False


def iterative_dfs(graph, source, target):
    visited_nodes = set()
    stack = [source]

    while stack:
        current_node = stack.pop()
        if current_node in visited_nodes:
            continue  # skip the rest of the body and begin next iteration

        visited_nodes.add(current_node)

        if current_node == target:
            return True

        for neighbor in graph.edges[current_node]:
            if neighbor not in visited_nodes:
                stack.append(neighbor)

    return False


class TestDFS(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'D')
        self.graph.add_edge('D', 'E')
        self.graph.add_edge('D', 'C')
        self.graph.add_edge('F', 'G')
        self.graph.add_node('H')

    def test_recursive_1(self):
        actual = recursive_dfs(self.graph, 'A', 'E')
        expected = True
        self.assertEqual(actual, expected)

    def test_recursive_2(self):
        actual = recursive_dfs(self.graph, 'A', 'G')
        expected = False
        self.assertEqual(actual, expected)

    def test_iterative_1(self):
        actual = iterative_dfs(self.graph, 'B', 'C')
        expected = True
        self.assertEqual(actual, expected)

    def test_iterative_2(self):
        actual = iterative_dfs(self.graph, 'E', 'H')
        expected = False
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
