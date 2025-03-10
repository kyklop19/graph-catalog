from algorithms.cycles import check_for_cycle_directed
from algorithms.searching import DFSOrder, dfs
from constants import AdjList


def find_topological_ordering(graph: AdjList) -> list[int]:
    """Find toplogical ordering of the given graph

    Args:
        graph (AdjList): _description_

    Returns:
        list[int]: _description_
    """
    res = []

    if not check_for_cycle_directed(graph):
        for curr_vertex, dfs_states in dfs(graph, search_order=DFSOrder.POSTORDER):
            res.append(curr_vertex)

    res.reverse()
    return res
