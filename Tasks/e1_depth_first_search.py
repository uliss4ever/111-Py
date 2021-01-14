from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    nods_visit = [start_node]
    stk = [start_node]
    while stk:
        node = stk[-1]
        if node not in nods_visit:
            nods_visit.append(node)
        remv = True
        for nxt in g[node]:
            if nxt not in nods_visit:
                stk.append(nxt)
                remv = False
                break
        if remv == True:
            stk.pop()

    return nods_visit

graph = nx.Graph()
graph.add_nodes_from("ABCDEFG")
graph.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('E', 'G'),
])

print(dfs(graph, "A"))
