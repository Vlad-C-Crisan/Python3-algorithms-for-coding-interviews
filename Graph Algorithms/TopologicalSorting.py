"""Python3 implementation of Topological Sorting using a modification of the Depth First Search (DFS) algorithm

In this file, the class Graph constructs an directed graph as adjacency list. For our implementation of Topological
Sorting, we assume that a directed edge between node_1 and node_2 means that node_1 has to come before node_2 in
topological order. If one wants to use this implementation for the reverse scenario, the only adjustment to be done
is to remove the line 'nodes_list.reverse()' at the end of the dfs_top_sort function.

The file contains the following classes:
    Graph - implementation of a directed graph using adjacency list

    TestTopSort - test cases for the Topological Sorting algorithm

The file contains the following functions
    * dfs_top_sort - function that takes as input a directed graph and returns a list
        containing a topological sorting of the vertices in graph, provided that the graph is acyclic

    * dfs_visit - recursive function used inside the dfs_top_sort function
        it takes as input a graph, a node in the graph to be processed, the list of colors of the nodes,
        and a boolean indicating whether we have found a cycle or not. As long as we have not encountered
        any cycles, the function performs a standard depth first search, and adds the nodes that were visited
        to a list. After all the nodes have been visited, the list of nodes will contain the graph nodes, in
        inverse topological order."""

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

        add_edge (from_node, to_node)
            adds from_node and to_node to the graph
            adds the edge between from_node and to_node
            adds to_node to the neighbors of from_node
            adds from_node to the neighbors of to_node



    """
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node):
        # first add the two nodes to the graph.nodes, in case we forgot to do this before
        self.add_node(from_node)
        self.add_node(to_node)

        # add the edge in the graph
        if from_node in self.edges:
            self.edges[from_node].append(to_node)
        else:
            self.edges[from_node] = [to_node]


def dfs_top_sort(graph):
    nodes_list = []
    color = {node: 'white' for node in graph.nodes}
    found_cycle = [False]

    for node in graph.nodes:
        if color[node] == 'white':
            dfs_visit(graph, node, color, nodes_list, found_cycle)
        if found_cycle[0]:
            break

    if found_cycle[0]:
        nodes_list = []
    if nodes_list:
        nodes_list.reverse()
        return nodes_list
    else:
        return 'the given graph has a cycle'


def dfs_visit(graph, node, color, nodes_list, found_cycle):
    if found_cycle[0]:
        return
    color[node] = 'gray'
    for neighbor in graph.edges[node]:
        if color[neighbor] == 'gray':
            found_cycle[0] = True
            return
        elif color[neighbor] == 'white':
            dfs_visit(graph, neighbor, color, nodes_list, found_cycle)
    color[node] = 'black'
    nodes_list.append(node)


class TestTopSort(unittest.TestCase):

    def setUp(self):
        # first construct an acyclic graph
        self.graph_1 = Graph()
        self.graph_1.add_edge('A', 'B')
        self.graph_1.add_edge('B', 'C')
        self.graph_1.add_edge('C', 'D')
        self.graph_1.add_edge('D', 'E')
        self.graph_1.add_edge('E', 'F')

        # now construct a graph with a cycle
        self.graph_2 = Graph()
        self.graph_2.add_edge('A', 'B')
        self.graph_2.add_edge('B', 'C')
        self.graph_2.add_edge('C', 'D')
        self.graph_2.add_edge('D', 'B')

    def test_top_sort_1(self):
        actual = dfs_top_sort(self.graph_1)
        print(actual)
        expected = ['A', 'B', 'C', 'D', 'E', 'F']
        self.assertEqual(actual, expected)

    def test_top_sort_2(self):
        actual = dfs_top_sort(self.graph_2)
        expected = 'the given graph has a cycle'
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
