from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as mpl



def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g"""

    shortest_path = {}
    to_visit = []

    shortest_path[starting_node] = 0
    for current_node in g.nodes:
        if current_node != starting_node:
                shortest_path[current_node] = float("inf")
    to_visit.append(starting_node)
    print(shortest_path)
    while to_visit:
        current_node = to_visit.pop(0)
        for node in g.neighbors(current_node):
            if node not in to_visit:
                if shortest_path[node] > g[current_node][node]["weight"] + shortest_path[current_node]:
                    shortest_path[node] = g[current_node][node]["weight"] +  shortest_path[current_node]
                    to_visit.append(node)
                    print(shortest_path)
                    print(to_visit)

    return shortest_path



if __name__ == "__main__":
        g = nx.DiGraph()
        g.add_nodes_from("ABCDEFG")
        g.add_weighted_edges_from([
                ("A", "B", 1),
                ("B", "C", 3),
                ("C", "E", 4),
                ("E", "F", 3),
                ("B", "E", 8),
                ("C", "D", 1),
                ("D", "E", 2),
                ("B", "D", 2),
                ("G", "D", 1),
                ("D", "A", 2),
            ])
        # nx.draw(g, with_labels=True)
        # mpl.show()




