from graph_catalog.algorithms.searching import DFSOrder, dfs
from graph_catalog.constants import AdjList


def find_topological_ordering(graph: AdjList) -> list[int] | None:
    """Find topological ordering of the given directed graph if any exists

    Args:
        graph (AdjList): Directed graph as adjacency list

    Returns:
        list[int]|None: List of vertex indexes in topological order if graph is acyclic else None
    """
    res = []

    for curr_vertex, dfs_states in dfs(
        graph, search_order=DFSOrder.PREORDER | DFSOrder.POSTORDER
    ):
        if dfs_states.closing_orders[curr_vertex] == -1:
            for nbr, __ in graph[curr_vertex]:
                if (
                    dfs_states.opening_orders[nbr] != -1
                    and dfs_states.closing_orders[nbr] == -1
                ):
                    res = None
                    break
        else:
            res.append(curr_vertex)

        if res is None:
            break

    if res is not None:
        res.reverse()
    return res
