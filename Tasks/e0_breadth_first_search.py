from typing import Hashable, List
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """


    print(g, start_node)
    return list(g.nodes)



graph = nx.Graph()
graph.add_nodes_from("ABCDEFGHIJ")
graph.add_edges_from([
    ('A', 'B'),
    ('A', 'F'),
    ('B', 'G'),
    ('F', 'G'),
    ('G', 'C'),
    ('G', 'H'),
    ('G', 'I'),
    ('C', 'H'),
    ('I', 'H'),
    ('H', 'D'),
    ('H', 'E'),
    ('H', 'J'),
    ('E', 'D'),
])
bfs(graph, "A")