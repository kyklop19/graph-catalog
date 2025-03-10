from algorithms.searching import dfs
from constants import AdjList


def is_bipartite(graph: AdjList) -> bool:
    """Test whether the given graph is bipartite

    Colors vertices with 2 colors in an alternating manner and checks whether
    neighboring vertices have the other color

    Args:
        graph (AdjList): Graph in adjacency list representation

    Returns:
        bool: True when graph is bipartite
    """

    res = True
    coloring = [0] * len(graph)
    for curr_vertex, dfs_states in dfs(graph):
        parent = dfs_states.parents[curr_vertex]
        if parent is None:
            color = 1
        else:
            color = -coloring[parent]
        coloring[curr_vertex] = color
        for nbr, __ in graph[curr_vertex]:
            if coloring[nbr] == coloring[curr_vertex]:
                res = False
                break
        if not res:
            break
    return res
