""" Python3 implementation of Dijkstra\'s algorithm.

The below implementation of Dijkstra\'s algorithm runs in O(V^2+E) = O(V^2).
This is NOT the fastest implementation: there exists an implementation that uses Fibonacci heaps 
and runs in O(V*log(V)+E)-see Chapter 24.3 in 3rd edition of Cormen - Introduction to Algorithms.
 
The below implementation of Dijkstra\'s algorithm assumes that the Graph is
implemented as adjacency list stored as dictionary and that it contains a set of 
distances (costs) stored as dictionary where the keys are node tuples (source_node, target_node)
and the values are represented by the distances between the nodes. See the below 
implementation of the class Graph."""

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

        # add the edge in the directed graph
        if source_node in self.edges:
            self.edges[source_node].append(target_node)
        else:
            self.edges[source_node] = [target_node]

        # add the distance between the two nodes
        self.distances[(source_node, target_node)] = distance


def dijkstra(graph, source):
    """"This function returns a dictionary consisting of shortest paths in the form
    node: parent on path, with the source node having source: None.
    It is designed so that it can be easily modified to also return
    the distances or to explicitly reconstruct the path for one specific node"""

    # first assert that the source node is indeed in our graph
    assert source in graph.nodes

    # create a set of all nodes to visit by retrieving the keys from graph.edges
    nodes_to_visit = {node for node in graph.nodes}

    # create a dictionary of distances, initialized to infinity and then update for source
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0

    # create a dictionary that stores the parent of each node on the path from source
    previous_on_path = {node: None for node in graph.nodes}

    while nodes_to_visit:
        # find the node storing the minimum distance in distances, from those that are to be visited
        min_node = None
        min_distance = float('inf')
        for node in nodes_to_visit:
            if distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]

        if min_node is None:
            break

        nodes_to_visit.remove(min_node)

        for neighbor in graph.edges[min_node]:
            if distances[neighbor] > distances[min_node] + graph.distances[(min_node, neighbor)]:
                distances[neighbor] = distances[min_node] + graph.distances[(min_node, neighbor)]
                previous_on_path[neighbor] = min_node
    return previous_on_path


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge('A', 'B', 5)
        self.graph.add_edge('B', 'A', 5)
        self.graph.add_edge('B', 'C', 3)
        self.graph.add_edge('B', 'D', 6)
        self.graph.add_edge('C', 'D', 2)

    def test_dijkstra(self):
        actual = dijkstra(self.graph, 'B')
        expected = {'B': None, 'A': 'B', 'C': 'B', 'D': 'C'}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
