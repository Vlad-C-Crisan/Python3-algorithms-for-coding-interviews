""" A Python3 implementation of various versions of Breadth First Search (BFS) algorithm

The algorithms can be run on both directed and undirected graphs. In this file,
the class Graph constructs an undirected graph as adjacency list. To transform it into a
directed graph, simply modify the method add_edge inside the Graph class.

The file contains the following classes:
    Graph - implementation of a graph using adjacency list

    TestBFS - test cases for the various implementations of the BFS algorithm

The file contains the following functions
    * bfs_path - takes as input a graph and a source, and returns a dictionary
        representing the connected component rooted at source

    *bfs_target - takes as input a graph, a source node and a target node from the graph
        and returns a list representing the path from source to target, if this exists

    *reconstruct_path - takes as input a dictionary representing a path from a source to a target,
        together with the target node, and returns a list representing the path from source to target

    *bfs_all_graph - takes as input a graph and returns a set consisting of all connected components
        of the graph, each component represented as a frozenset
"""

from collections import deque
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


def bfs_path(graph, source):
    if source not in graph.nodes:
        raise ValueError('The given source node is not in the graph')

    previous_on_path = {source: None}  # this serves both as path and as visited nodes indicator
    nodes_queue = deque()
    nodes_queue.append(source)

    while nodes_queue:
        current = nodes_queue.popleft()

        for neighbor in graph.edges[current]:
            if neighbor not in previous_on_path:
                nodes_queue.append(neighbor)
                previous_on_path[neighbor] = current

    return previous_on_path


def bfs_target(graph, source, target):
    if source not in graph.nodes:
        raise ValueError('The given source node is not in the graph')

    if target not in graph.nodes:
        raise ValueError('The given target node is not in the graph')

    previous_on_path = {source: None}  # this serves both as path and as visited nodes indicator
    nodes_queue = deque()
    nodes_queue.append(source)

    while nodes_queue:
        current = nodes_queue.popleft()
        if current == target:
            return reconstruct_path(previous_on_path, target)

        for neighbor in graph.edges[current]:
            if neighbor not in previous_on_path:
                nodes_queue.append(neighbor)
                previous_on_path[neighbor] = current

    return 'Target node cannot be reached from the source node'


def reconstruct_path(path_dictionary, target):
    # store nodes in backwards order first, starting from target
    reversed_path = []
    current = target
    while current:
        reversed_path.append(current)
        current = path_dictionary[current]
    reversed_path.reverse()
    return reversed_path


def bfs_all_graph(graph):
    visited_nodes = set()
    connected_components = set()
    for node in graph.nodes:
        if node not in visited_nodes:
            path, visited_nodes = bfs_all_aux(graph, node, visited_nodes)
            connected_components.add(frozenset(path))  # frozenset needed to make it hashable
    return connected_components


def bfs_all_aux(graph, source, visited=set()):
    if source not in graph.nodes:
        raise ValueError('The given source node is not in the graph')

    previous_on_path = {source: None}
    nodes_queue = deque()
    nodes_queue.append(source)
    visited.add(source)

    while nodes_queue:
        current = nodes_queue.popleft()

        for neighbor in graph.edges[current]:
            if neighbor not in visited:
                nodes_queue.append(neighbor)
                previous_on_path[neighbor] = current
                visited.add(neighbor)

    return previous_on_path, visited


class TestBFS(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'D')
        self.graph.add_edge('D', 'E')
        self.graph.add_edge('D', 'C')
        self.graph.add_edge('F', 'G')
        self.graph.add_node('H')

    def test_bfs_path_1(self):
        actual = bfs_path(self.graph, 'A')
        expected = {'A': None, 'B': 'A', 'D': 'A', 'E': 'D', 'C': 'D'}
        self.assertEqual(actual, expected)

    def test_bfs_path_2(self):
        actual = bfs_path(self.graph, 'H')
        expected = {'H': None}
        self.assertEqual(actual, expected)

    def test_bfs_with_target(self):
        actual = bfs_target(self.graph, 'A', 'C')
        expected = ['A', 'D', 'C']
        self.assertEqual(actual, expected)

    def test_connected_components(self):
        actual = bfs_all_graph(self.graph)
        expected = set()
        expected.add(frozenset({'A', 'B', 'C', 'D', 'E'}))
        expected.add(frozenset({'F', 'G'}))
        expected.add(frozenset({'H'}))
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
